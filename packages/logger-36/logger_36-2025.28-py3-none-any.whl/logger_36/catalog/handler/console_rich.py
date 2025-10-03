"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2023
SEE COPYRIGHT NOTICE BELOW
"""

import logging as l
import typing as h

from logger_36.catalog.config.console_rich import (
    ACTUAL_COLOR,
    ALTERNATIVE_BACKGROUND_FOR_DARK,
    ALTERNATIVE_BACKGROUND_FOR_LIGHT,
    EXPECTED_COLOR,
    GRAY_COLOR,
    LEVEL_COLOR,
    RULE_COLOR,
    WHITE_COLOR,
)
from logger_36.config.message import ACTUAL_PATTERNS, EXPECTED_PATTERNS
from logger_36.constant.message import CONTEXT_LENGTH
from logger_36.constant.record import HAS_ACTUAL_EXPECTED_ATTR
from logger_36.type.handler import non_file_handler_t as base_t
from rich.console import Console as console_t  # noqa
from rich.console import RenderableType as renderable_t  # noqa
from rich.markup import escape as EscapedVersion  # noqa
from rich.rule import Rule as rule_t  # noqa
from rich.style import Style as style_t  # noqa
from rich.text import Text as text_t  # noqa
from rich.traceback import install as InstallTracebackHandler  # noqa

_COMMON_TRACEBACK_ARGUMENTS = ("theme", "width")
_EXCLUSIVE_TRACEBACK_ARGUMENTS = (
    "extra_lines",
    "indent_guides",
    "locals_hide_dunder",
    "locals_hide_sunder",
    "locals_max_length",
    "locals_max_string",
    "max_framesshow_locals",
    "suppress",
    "word_wrap",
)


class console_rich_handler_t(base_t):
    """
    alternating_logs:
    - 0: disabled
    - 1: enabled for dark background
    - 2: enabled for light background
    """

    def __init__(
        self, name: str | None, message_width: int, level: int, kwargs
    ) -> None:
        """"""
        alternating_logs = kwargs.pop("alternating_logs", 0)
        should_install_traceback = kwargs.pop("should_install_traceback", False)

        assert alternating_logs in (0, 1, 2)

        base_t.__init__(self, name, message_width, EscapedVersion, level, kwargs)

        self.console = None  # console_t | None.
        if alternating_logs == 0:
            self.background_style = None
        elif alternating_logs == 1:
            self.background_style = ALTERNATIVE_BACKGROUND_FOR_DARK
        else:
            self.background_style = ALTERNATIVE_BACKGROUND_FOR_LIGHT
        self._should_style_background = False

        self.__post_init_local__(should_install_traceback, **kwargs)

    def __post_init_local__(self, should_install_traceback: bool, **kwargs) -> None:
        """"""
        traceback_kwargs = {}
        if should_install_traceback:
            for key in kwargs:
                if key in _COMMON_TRACEBACK_ARGUMENTS:
                    traceback_kwargs[key] = kwargs[key]
                elif key in _EXCLUSIVE_TRACEBACK_ARGUMENTS:
                    traceback_kwargs[key] = kwargs.pop(key)

        self.console = console_t(highlight=False, force_terminal=True, **kwargs)

        if should_install_traceback:
            traceback_kwargs["console"] = self.console
            InstallTracebackHandler(**traceback_kwargs)

    @classmethod
    def New(
        cls,
        /,
        *,
        name: str | None = None,
        message_width: int = -1,
        level: int = l.NOTSET,
        **kwargs,
    ) -> h.Self:
        """"""
        return cls(name, message_width, level, kwargs)

    def Rule(self, /, *, text: str | None = None, color: str = "black") -> str | rule_t:
        """"""
        if text in (None, ""):
            return rule_t(style=color)
        return rule_t(title=text_t(text, style=f"bold {color}"), style=color)

    def emit(self, record: l.LogRecord, /) -> None:
        """"""
        message, is_not_a_rule, where_location = self.MessageFromRecord(
            record, rule_color=RULE_COLOR
        )
        if is_not_a_rule:
            if self._should_style_background:
                background_style = self.background_style
            else:
                background_style = None
            message = HighlightedVersion(
                self.console,
                message,
                getattr(record, HAS_ACTUAL_EXPECTED_ATTR, False),
                where_location,
                record.levelno,
                background_style,
            )
        self.console.print(message, crop=False, overflow="ignore")
        self._should_style_background = not self._should_style_background

    def EmitMessage(self, message: str | renderable_t, /) -> None:
        """"""
        self.console.print(message, crop=False, overflow="ignore")


def HighlightedVersion(
    _: console_t,
    message: str,
    has_actual_expected: bool,
    where_location: int | None,
    log_level: int,
    background_style: style_t | None,
    /,
) -> renderable_t:
    """"""
    output = text_t(message, WHITE_COLOR)

    output.stylize(LEVEL_COLOR[log_level], end=CONTEXT_LENGTH)
    if where_location is not None:
        output.stylize(GRAY_COLOR, start=where_location)
    if has_actual_expected:
        _ = output.highlight_words(ACTUAL_PATTERNS, style=ACTUAL_COLOR)
        _ = output.highlight_regex(EXPECTED_PATTERNS, style=EXPECTED_COLOR)

    if background_style is not None:
        output.stylize(background_style)

    return output


"""
COPYRIGHT NOTICE

This software is governed by the CeCILL  license under French law and
abiding by the rules of distribution of free software.  You can  use,
modify and/ or redistribute the software under the terms of the CeCILL
license as circulated by CEA, CNRS and INRIA at the following URL
"http://www.cecill.info".

As a counterpart to the access to the source code and  rights to copy,
modify and redistribute granted by the license, users are provided only
with a limited warranty  and the software's author,  the holder of the
economic rights,  and the successive licensors  have only  limited
liability.

In this respect, the user's attention is drawn to the risks associated
with loading,  using,  modifying and/or developing or reproducing the
software by the user in light of its specific status of free software,
that may mean  that it is complicated to manipulate,  and  that  also
therefore means  that it is reserved for developers  and  experienced
professionals having in-depth computer knowledge. Users are therefore
encouraged to load and test the software's suitability as regards their
requirements in conditions enabling the security of their systems and/or
data to be ensured and,  more generally, to use and operate it in the
same conditions as regards security.

The fact that you are presently reading this means that you have had
knowledge of the CeCILL license and that you accept its terms.

SEE LICENCE NOTICE: file README-LICENCE-utf8.txt at project source root.
"""
