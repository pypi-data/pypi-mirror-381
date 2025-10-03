"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2023
SEE COPYRIGHT NOTICE BELOW
"""

from datetime import datetime as date_time_t

from logger_36.constant.chronos import FORMATTED_START_DATE_TIME, START_DATE_TIME
from logger_36.constant.record import SHOW_WHEN_ATTR, SHOW_WHERE_ATTR
from logger_36.instance.logger import L
from logger_36.task.measure.chronos import FormattedElapsedTime
from logger_36.type.logger import logger_t


_START_NAME = "START"
_START_PLACEHOLDER = "..."  # Must not be longer than _START_NAME.
_END_NAME = "END"


def LogElapsedTime(*, logger: logger_t = L) -> None:
    """"""
    now = date_time_t.now()

    message = (
        f"Elapsed Time: {FormattedElapsedTime(now, with_separator=False)} "
        f"(since {FORMATTED_START_DATE_TIME})"
    )
    if logger.intermediate_times.__len__() > 0:
        intermediate_e_times = []
        for (start_name, start_time), (end_name, end_time) in zip(
            [(_START_NAME, START_DATE_TIME)] + logger.intermediate_times,
            logger.intermediate_times + [(_END_NAME, now)],
            strict=True,
        ):
            if start_name != _START_NAME:
                start_name = _START_PLACEHOLDER
            e_time = FormattedElapsedTime(
                end_time, reference=start_time, with_separator=False
            )
            intermediate_e_times.append((start_name, end_name, e_time))
        max_length_end = max(map(len, (_[1] for _ in intermediate_e_times)))
        intermediate_e_times = "\n    ".join(
            f"{_: <{_START_NAME.__len__()}} → {__: <{max_length_end}}   +{___}"
            for _, __, ___ in intermediate_e_times
        )
        message += "\n    " + intermediate_e_times
        logger.intermediate_times.clear()

    logger.info(message, extra={SHOW_WHEN_ATTR: False, SHOW_WHERE_ATTR: False})


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
