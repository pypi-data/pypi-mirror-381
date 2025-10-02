"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2023
SEE COPYRIGHT NOTICE BELOW
"""

import dataclasses as d
import logging as l
import typing as h

from logger_36.type.logger import logger_t


@d.dataclass(slots=True, repr=False, eq=False)
class loggers_t(dict[h.Hashable, logger_t]):
    active: logger_t | None = d.field(init=False, default=None)

    def AddNew(
        self,
        uid: h.Hashable,
        /,
        *,
        name: str | None = None,
        level: int = l.NOTSET,
        exit_on_error: bool = False,
        exit_on_critical: bool = False,
        activate_wrn_interceptions: bool = True,
        activate_log_interceptions: bool = True,
        activate_exc_interceptions: bool = True,
    ) -> None:
        """"""
        logger = logger_t(
            exit_on_error=exit_on_error,
            exit_on_critical=exit_on_critical,
            name_=name,
            level_=level,
            activate_wrn_interceptions=activate_wrn_interceptions,
            activate_log_interceptions=activate_log_interceptions,
            activate_exc_interceptions=activate_exc_interceptions,
        )
        self.Add(uid, logger)

    def Add(self, uid: h.Hashable, logger: logger_t, /) -> None:
        """"""
        if uid in self:
            raise NameError(f"Logger with name/identity {uid} already exists.")

        self[uid] = logger
        self.active = logger

    def SetActive(self, uid: h.Hashable, /) -> None:
        """"""
        self.active = self[uid]


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
