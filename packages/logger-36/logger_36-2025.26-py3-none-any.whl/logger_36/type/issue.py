"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2023
SEE COPYRIGHT NOTICE BELOW
"""

import logging as l
import typing as h

from logger_36.config.issue import ISSUE_BASE_CONTEXT
from logger_36.constant.issue import ISSUE_LEVEL_SEPARATOR
from logger_36.constant.message import expected_op_h
from logger_36.extension.sentinel import NOT_PASSED
from logger_36.task.format.message import MessageWithActualExpected

issue_t = str


def NewIssue(
    context: str,
    separator: str,
    message: str,
    /,
    *,
    level: int = l.ERROR,
    actual: h.Any = NOT_PASSED,
    expected: h.Any | None = None,
    expected_is_choices: bool = False,
    expected_op: expected_op_h = "=",
    with_final_dot: bool = True,
) -> tuple[issue_t, bool]:
    """"""
    if context.__len__() == 0:
        context = ISSUE_BASE_CONTEXT
    message, has_actual_expected = MessageWithActualExpected(
        message,
        actual=actual,
        expected=expected,
        expected_is_choices=expected_is_choices,
        expected_op=expected_op,
        with_final_dot=with_final_dot,
    )

    return (
        f"{level}{ISSUE_LEVEL_SEPARATOR}{context}{separator}{message}",
        has_actual_expected,
    )


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
