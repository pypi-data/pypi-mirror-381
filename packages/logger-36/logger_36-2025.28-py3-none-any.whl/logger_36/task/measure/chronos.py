"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2023
SEE COPYRIGHT NOTICE BELOW
"""

from datetime import datetime as date_time_t

from logger_36.config.message import ELAPSED_TIME_SEPARATOR
from logger_36.constant.chronos import START_DATE_TIME
from logger_36.constant.message import TIME_LENGTH


def TimeStamp(*, precision: str = "microseconds") -> str:
    """
    precision: See documentation of date_time_t.isoformat.
    """
    return (
        date_time_t.now()
        .isoformat(timespec=precision)
        .replace(".", "_")
        .replace(":", "-")
    )


def FormattedElapsedTime(
    now: date_time_t,
    /,
    *,
    reference: date_time_t = START_DATE_TIME,
    with_separator: bool = True,
) -> str:
    """"""
    output = str(now - reference)

    if output.startswith("0:"):
        output = output[2:]
    while output.startswith("00:"):
        output = output[3:]
    if output[0] == "0":
        output = output[1:]

    if with_separator:
        output = ELAPSED_TIME_SEPARATOR + output

    if output.__len__() > TIME_LENGTH:
        return output[:TIME_LENGTH]
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
