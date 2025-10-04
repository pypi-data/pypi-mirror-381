import functools
import logging
from io import TextIOBase
from typing import Callable, List, Optional, Tuple, TypeVar, Union

from simplini.core import (
    IniConfigBase,
    IniConfigOption,
    IniConfigSection,
    IniFlavour,
    SimpliniError,
    ValuePresentationStyle,
)

T = TypeVar("T")
ParseFn = Callable[[], T]


LOGGER = logging.getLogger(__name__)


class PositionContext:
    def __init__(
        self,
        line: str,
        line_number: int,
        column_number: int,
        lines_before: Optional[List[str]] = None,
    ):
        self.line = line
        # 1-based line number of the line
        self.line_number = line_number
        # 1-based position in the current line
        self.column_number = column_number
        # zero or multiple lines before the current line
        self.lines_before = lines_before


class ParsingError(SimpliniError):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message: str = message
        self.position: Optional[int] = None
        self.position_context: Optional[PositionContext] = None

    def extend_message(self, message: str) -> None:
        self.message += message
        self.args = (self.args[0] + message,) + self.args[1:]


class RecursiveDescentParserBase:
    def __init__(self, text_io: TextIOBase):
        self.text_io: TextIOBase = text_io
        self.deepest_error: Optional[ParsingError] = None

    def parsing_error(self, message: str) -> ParsingError:
        position = self.text_io.tell()

        error = ParsingError(message)
        error.position = position

        # update deepest error
        if self.deepest_error is None or position > self.deepest_error.position:
            self.deepest_error = error

        return error

    @staticmethod
    def represent(char: str) -> str:
        if char == "\n":
            return "LF"
        elif char == "\r":
            return "CR"
        elif char == "":
            return "EOF"
        else:
            return f'"{char}"'

    def expect(
        self,
        expected: Union[str, List[str]],
        error: Optional[str] = None,
    ) -> str:
        actual = self.text_io.read(1)

        if isinstance(expected, str):
            expected = [expected]

        for value in expected:
            if actual == value:
                break
        else:
            if not error:
                error = (
                    f"Expected {' OR '.join(self.represent(v) for v in expected)}, "
                    f"but encountered {self.represent(actual)}"
                )
            raise self.parsing_error(error)

        return actual

    def expect_eof(self) -> None:
        char = self.text_io.read(1)

        if char != "":
            raise self.parsing_error(f'Expected EOF, but encountered "{char}"')

        return None

    def accept(
        self,
        value_or_predicate: Union[Callable[[str], bool], str],
    ) -> Tuple[bool, Optional[str]]:
        char = self.text_io.read(1)

        # reached EOF
        if char == "":
            return False, None

        if not callable(value_or_predicate):

            def predicate(c: str) -> bool:
                return c == value_or_predicate
        else:
            predicate = value_or_predicate
            assert callable(predicate)

        if not predicate(char):
            self.text_io.seek(self.text_io.tell() - 1)
            return False, None

        return True, char

    def accept_multiple(
        self,
        value_or_predicate: Union[Callable[[str], bool], str],
    ) -> Tuple[bool, str]:
        chars = ""
        accepted, char = self.accept(value_or_predicate)

        if not accepted:
            return False, chars

        while accepted:
            assert char is not None
            chars += char
            accepted, char = self.accept(value_or_predicate)

        return True, chars

    def multiple(self, parse_fn: ParseFn) -> List[T]:
        results = []

        while True:
            ok, result = self.optional(parse_fn)

            if not ok:
                break

            assert result is not None
            results.append(result)

        return results

    def optional(self, parse_fn: ParseFn) -> Tuple[bool, Optional[T]]:
        position = self.text_io.tell()

        try:
            result = parse_fn()
            return True, result
        except ParsingError:
            self.text_io.seek(position)
            return False, None

    def choice(self, parse_fns: List[ParseFn]) -> Tuple[int, T]:
        last_error = None
        position = self.text_io.tell()

        for parser_idx, parse_fn in enumerate(parse_fns):
            try:
                result = parse_fn()
                return parser_idx, result
            except ParsingError as e:
                last_error = e
                self.text_io.seek(position)

        assert last_error is not None
        raise last_error

    def peek(self, length: int) -> T:
        position = self.text_io.tell()
        peeked = self.text_io.read(length)
        self.text_io.seek(position)
        return peeked

    def hinted_choice(
        self,
        hinted_parse_fns: List[Tuple[Union[Optional[str], List[str]], ParseFn]],
    ) -> Tuple[int, T]:
        position = self.text_io.tell()
        last_error = None

        for parser_idx, (hint, parse_fn) in enumerate(hinted_parse_fns):
            if hint:
                if isinstance(hint, str):
                    hint = [hint]

                for single_hint_value in hint:
                    peeked = self.peek(len(single_hint_value))

                    # hint matched, so we know this branch is what we need
                    if single_hint_value == peeked:
                        return parser_idx, parse_fn()
            else:  # empty hint, attempt the branch and go to next if not successful
                try:
                    return parser_idx, parse_fn()
                except ParsingError as e:
                    self.text_io.seek(position)
                    last_error = e

        assert last_error is not None
        raise last_error


class IniParserImpl(RecursiveDescentParserBase):
    def __init__(
        self,
        text_io: TextIOBase,
        flavour: IniFlavour,
    ):
        super().__init__(text_io)
        self.flavour = flavour

    def resolve_escape_sequence(self, sequence: str) -> str:
        if sequence not in self.flavour.escape_sequences:
            raise self.parsing_error(f"Unknown escape sequence: {sequence}")
        return self.flavour.escape_sequences[sequence]

    def parse_quoted_string(self) -> str:
        self.parse_whitespaces()
        self.expect(self.flavour.quote_character)

        value = ""

        while True:
            char = self.text_io.read(1)
            if char == self.flavour.escape_character:
                next_char = self.text_io.read(1)
                value += self.resolve_escape_sequence(next_char)
            elif char == self.flavour.new_line:
                raise self.parsing_error(
                    "New line encountered before closing quoted string"
                )
            elif char == "":
                raise self.parsing_error("EOF encountered before closing quoted string")
            else:  # normal character
                if char == self.flavour.quote_character:
                    break
                value += char

        self.parse_whitespaces()

        return value

    def parse_triple_quoted_string(self) -> str:
        self.parse_whitespaces()

        self.expect(self.flavour.quote_character)
        self.expect(self.flavour.quote_character)
        self.expect(self.flavour.quote_character)

        value = ""

        while True:
            char = self.text_io.read(1)

            if char == self.flavour.escape_character:
                next_char = self.text_io.read(1)
                value += self.resolve_escape_sequence(next_char)
            else:  # normal character:
                if char == self.flavour.quote_character:
                    # check if it's the end of the triple-quoted string
                    next_char = self.text_io.read(1)
                    if next_char == self.flavour.quote_character:
                        next_next_char = self.text_io.read(1)
                        if next_next_char == self.flavour.quote_character:
                            break
                        else:
                            value += char + next_char + next_next_char
                    else:
                        value += char + next_char
                else:
                    value += char

        self.parse_whitespaces()

        return value

    def parse_unquoted_string(self) -> str:
        self.parse_whitespaces()

        _, value = self.accept_multiple(
            lambda c: c
            not in (self.flavour.new_line,) + tuple(self.flavour.comment_markers),
            # even if nothing is accepted we consider the value to be empty
        )

        assert value is not None

        # strip trailing spaces
        value = value.rstrip()

        if self.flavour.quote_character in value:
            raise self.parsing_error(
                "Quote character inside non-quoted strings is forbidden as ambiguous"
            )

        self.parse_whitespaces()

        return value

    def is_option_name_char(self, c: str) -> bool:
        # here is what TOML allows: A-Za-z0-9_-
        # see https://toml.io/en/v1.0.0
        # we will allow a bit more for now
        return c.isalnum() or c in ("_", "-", ".", ":")

    def parse_option_name(self) -> str:
        _, option_name = self.accept_multiple(
            self.is_option_name_char,
        )

        if not option_name:
            raise self.parsing_error("Expected option name to be non-empty string")

        return option_name

    def parse_option_value(self) -> Tuple[str, ValuePresentationStyle]:
        if self.flavour.allow_unquoted_values:
            parser_idx, value = self.hinted_choice(
                [
                    (self.flavour.quote_character * 3, self.parse_triple_quoted_string),
                    (self.flavour.quote_character, self.parse_quoted_string),
                    (None, self.parse_unquoted_string),
                ]
            )

            if parser_idx == 0:
                return value, ValuePresentationStyle.TRIPLE_QUOTED
            elif parser_idx == 1:
                return value, ValuePresentationStyle.QUOTED
            elif parser_idx == 2:
                return value, ValuePresentationStyle.UNQUOTED
            else:
                raise NotImplementedError(parser_idx)
        else:
            parser_idx, value = self.hinted_choice(
                [
                    (self.flavour.quote_character * 3, self.parse_triple_quoted_string),
                    (
                        self.flavour.quote_character,
                        self.parse_quoted_string,
                    ),
                ]
            )

            if parser_idx == 0:
                return value, ValuePresentationStyle.TRIPLE_QUOTED
            elif parser_idx == 1:
                return value, ValuePresentationStyle.QUOTED
            else:
                raise NotImplementedError(parser_idx)

    def parse_option(self) -> IniConfigOption:
        comments = self.parse_comments()
        self.parse_whitespaces()
        option_name = self.parse_option_name()
        self.parse_whitespaces()
        self.expect(self.flavour.key_value_separators)
        self.parse_whitespaces()

        option_value, option_value_style = self.parse_option_value()

        _, inline_comment = self.optional(self.parse_comment_line)
        self.multiple(self.parse_empty_line)

        option = IniConfigOption(option_name, option_value)
        option.comment = comments
        option.inline_comment = inline_comment
        option.style = option_value_style
        return option

    def is_whitespace(self, char: str) -> bool:
        return char in self.flavour.whitespace_characters

    def parse_whitespaces(self) -> str:
        return self.accept_multiple(self.is_whitespace)[1]

    def parse_section_body(self, section: IniConfigSection) -> None:
        options = self.multiple(self.parse_option)

        for option in options:
            assert option is not None

            if option.key in section.options:
                raise self.parsing_error(
                    f'Option "{option.key}" was present multiple times'
                )

            section.options[option.key] = option

    def parse_comment_line(self) -> str:
        self.accept_multiple(self.is_whitespace)
        self.expect(self.flavour.comment_markers)

        _, comment = self.accept_multiple(
            lambda c: c != self.flavour.new_line,
        )

        # accept new line if present as well
        self.accept(self.flavour.new_line)

        # strip leading/trailing spaces
        return comment.strip()

    def parse_empty_line(self) -> str:
        self.accept_multiple(self.is_whitespace)
        self.expect(self.flavour.new_line)
        return ""

    def parse_comments(self) -> List[str]:
        def parse_comment_or_empty_line() -> Tuple[int, str]:
            parser_idx, parsed_value = self.choice(
                [
                    self.parse_comment_line,
                    self.parse_empty_line,
                ]
            )
            return parser_idx, parsed_value

        parsed = self.multiple(parse_comment_or_empty_line)

        # drop empty lines
        comment_lines = [line for idx, line in parsed if idx == 0]

        # strip the comments
        return [comment.strip() for comment in comment_lines]

    def parse_section(self) -> IniConfigSection:
        comments = self.parse_comments()

        # parse section name
        self.expect("[")

        _, section_name = self.accept_multiple(
            lambda c: c not in ("]", self.flavour.new_line),
        )

        if not section_name:
            raise self.parsing_error("Expected section name to be non-empty")

        self.expect("]")
        self.accept_multiple(self.is_whitespace)

        alt_idx, result = self.hinted_choice(
            [
                (self.flavour.comment_markers, self.parse_comment_line),
                (
                    None,
                    lambda: self.expect(
                        self.flavour.new_line,
                        "Expected end of line after section header",
                    ),
                ),
            ]
        )

        section = IniConfigSection(section_name)

        if alt_idx == 0:
            section.inline_comment = result

        section.comment = comments

        self.parse_section_body(section)

        return section

    def parse_comments_only_document_edge_case(self, config: IniConfigBase):
        comment = self.parse_comments()

        self.expect_eof()

        config.unnamed_section.comment = comment

        return config

    def parse_normal(self, config: IniConfigBase):
        # parse unnamed section
        config.unnamed_section = IniConfigSection(None)
        self.parse_section_body(config.unnamed_section)

        # then any number of other sections
        sections = self.multiple(self.parse_section)

        for section in sections:
            assert section is not None

            if section.name in config.sections:
                raise self.parsing_error(
                    f'Section "{section.name}" was present multiple times'
                )

            config.sections[section.name] = section

        config.trailing_comment = self.parse_comments()

        self.expect_eof()

        return config

    def parse(self, config: IniConfigBase):
        self.choice(
            [
                functools.partial(self.parse_comments_only_document_edge_case, config),
                functools.partial(self.parse_normal, config),
            ]
        )


class IniParser:
    @staticmethod
    def position_context(
        text_io: TextIOBase,
        position: int,
        context_lines: int = 1,
    ) -> Optional[PositionContext]:
        fd = text_io.fileno()

        # re-open file w/o automatic new-line conversion so that
        # position is relevant on platforms where new lines are of different
        # len from Unix style (LF)
        with open(
            fd,
            mode="r",
            encoding=text_io.encoding,
            newline="",
            closefd=False,
        ) as raw:
            raw.seek(0)

            read_bytes = 0
            lines = raw.readlines()

            for line_idx, line in enumerate(lines):
                line_size_bytes = len(line.encode(text_io.encoding))
                if position < read_bytes + line_size_bytes:
                    column_idx = 0
                    col_bytes = 0

                    # we found the line, now find which character specifically
                    while position > read_bytes + col_bytes + 1:
                        col_bytes += len(line[column_idx].encode(text_io.encoding))
                        column_idx += 1

                    return PositionContext(
                        line=line,
                        line_number=line_idx + 1,
                        column_number=column_idx + 1,
                        lines_before=lines[line_idx - context_lines : line_idx],
                    )

                read_bytes += line_size_bytes

            # edge case -- position points right after
            # the last character of the text
            if position == read_bytes:
                return PositionContext(
                    line=lines[-1],
                    line_number=line_idx + 1,
                    column_number=len(lines[-1]),
                    lines_before=lines[-1 - context_lines : -1],
                )

            # unable to determine
            return None

    def parse(
        self,
        text_io: TextIOBase,
        instance: IniConfigBase,
        flavour: IniFlavour,
    ) -> None:
        parser = IniParserImpl(
            text_io,
            flavour=flavour,
        )

        try:
            parser.parse(instance)
        except ParsingError as err:
            effective: ParsingError = parser.deepest_error

            assert effective is not None

            position_context = self.position_context(
                text_io,
                effective.position,
            )

            if position_context:
                effective.position_context = position_context

                error_marker = "> "
                padding = " " * len(error_marker)

                position_message = padding + "..." + "\n"
                for line_before in position_context.lines_before:
                    position_message += padding + line_before

                position_message += error_marker
                position_message += position_context.line.rstrip("\n") + "\n"
                position_message += " " * (
                    position_context.column_number - 1 + len(error_marker)
                )
                position_message += "^\n"

                position_message += (
                    f"Line {position_context.line_number}, "
                    f"Column {position_context.column_number}, "
                    f"Byte {effective.position}\n"
                )

                effective.extend_message("\n\n" + position_message)

            raise effective from err
