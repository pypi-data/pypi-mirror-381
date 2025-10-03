"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2023
SEE COPYRIGHT NOTICE BELOW
"""

GPU_LOGGING_ERROR = (
    "GPU details cannot be logged because the Tensorflow and/or Tensorrt package(s) "
    "(https://www.tensorflow.org/, https://developer.nvidia.com/tensorrt)"
    "is/are not installed or not importable."
)

MEMORY_MEASURE_ERROR = (
    "Memory usage cannot be shown because the Psutil package "
    "(https://psutil.readthedocs.io/en/latest/)"
    "is not installed or not importable."
)

MISSING_RICH_MESSAGE = (
    "The Rich console handler is not available because the Rich package "
    "(https://rich.readthedocs.io/en/stable/) "
    "is not installed or not importable. "
    "Falling back to the raw console."
)

CANNOT_SAVE_RECORDS = "Cannot save logging records"

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
