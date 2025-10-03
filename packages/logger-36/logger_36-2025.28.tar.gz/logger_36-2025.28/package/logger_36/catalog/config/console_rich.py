"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2023
SEE COPYRIGHT NOTICE BELOW
"""

import logging as l

from rich.color import Color as color_t  # noqa
from rich.style import Style as style_t  # noqa

"""
Colors: See https://rich.readthedocs.io/en/stable/appendix/colors.html.
"""
WHITE_COLOR = "grey85"
GRAY_COLOR = "grey58"

LEVEL_COLOR: dict[int, str | style_t] = {
    l.DEBUG: "orchid",
    l.INFO: GRAY_COLOR,
    l.WARNING: "yellow1",
    l.ERROR: "dark_orange",
    l.CRITICAL: "bright_red",
}
ACTUAL_COLOR = LEVEL_COLOR[l.CRITICAL]
EXPECTED_COLOR = "green3"
RULE_COLOR = "sky_blue3"

ALTERNATIVE_BACKGROUND_FOR_LIGHT = style_t(bgcolor=color_t.from_rgb(230, 230, 230))
ALTERNATIVE_BACKGROUND_FOR_DARK = style_t(bgcolor=color_t.from_rgb(25, 25, 25))

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
