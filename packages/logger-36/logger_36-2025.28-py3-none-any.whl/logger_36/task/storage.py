"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2023
SEE COPYRIGHT NOTICE BELOW
"""

import logging as l
from io import IOBase as io_base_t
from pathlib import Path as path_t

from logger_36.constant.error import CANNOT_SAVE_RECORDS
from logger_36.constant.html import (
    BODY_PLACEHOLDER,
    HTML_SUFFIX,
    MINIMAL_HTML,
    TITLE_PLACEHOLDER,
)
from logger_36.extension.file import NewTemporaryFile
from logger_36.instance.logger import L
from logger_36.type.logger import logger_t


def SaveLOGasHTML(
    path: str | path_t | io_base_t | None = None, /, *, logger: logger_t = L
) -> None:
    """
    From first console handler found.
    """
    records = logger_t.Records(logger)
    if records is None:
        logger.warning(
            f"{CANNOT_SAVE_RECORDS}: No handlers with recording capability found"
        )
        return
    if records.__len__() == 0:
        return

    if isinstance(records[0][1], str):
        records = map(_HighlightedRecord, records)
    else:
        records = map(lambda _: str(_[1]), records)
    body = "\n".join(records)
    html = MINIMAL_HTML.replace(TITLE_PLACEHOLDER, logger.name).replace(
        BODY_PLACEHOLDER, body
    )

    if path is None:
        path = logger_t.StoragePath(logger, HTML_SUFFIX)
        logger.info(f'Saving LOG as HTML in "{path}"')
    elif isinstance(path, str):
        path = path_t(path)
        if path.exists():
            existing = path
            path = NewTemporaryFile(HTML_SUFFIX)
            logger.warning(
                f'File "{existing}" already exists: '
                f'Saving LOG as HTML in "{path}" instead'
            )
    else:
        path.write(html)
        return

    with open(path, "w") as accessor:
        accessor.write(html)


def _HighlightedRecord(record: tuple[int, str, bool], /) -> str:
    """"""
    level, message, is_not_a_rule = record

    if is_not_a_rule:
        if level == l.DEBUG:
            color = "BlueViolet"
        elif level == l.INFO:
            color = "black"
        elif level == l.WARNING:
            color = "gold"
        elif level == l.ERROR:
            color = "orange"
        elif level == l.CRITICAL:
            color = "red"
        else:
            color = "black"
    else:
        color = "DarkTurquoise"

    return f'<span style="color:{color}">{message}</span>'


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
