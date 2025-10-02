"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2023
SEE COPYRIGHT NOTICE BELOW
"""

import pkgutil as pkgs
import sys as s


def Modules(
    *,
    only_loaded: bool = True,
    with_version: bool = True,
    formatted: bool = False,
    indent: int = 0,
) -> tuple[str, ...] | str:
    """"""
    output = []

    if only_loaded:
        modules = s.modules
        module_names = set(modules.keys()).difference(s.stdlib_module_names)
        module_names = sorted(module_names, key=str.lower)
    else:
        modules = None
        module_names = _ModulesUsingPkgUtil()
    max_length = 0
    m_idx = 0
    for name in module_names:
        if name.startswith("_") or ("." in name):
            continue

        if with_version:
            if modules is None:
                version = "?"
            else:
                module = modules[name]
                # strip: Some packages have a \n at the end of their version. Just in
                # case, let's strip it left and right.
                version = getattr(module, "__version__", "?").strip()
            element = f"{name}={version}"
        else:
            element = name

        if formatted and (m_idx > 0) and (m_idx % 4 == 0):
            output.append("\n")
        output.append(element)

        if formatted:
            max_length = max(max_length, element.__len__())
            m_idx += 1

    if formatted:
        max_length += 4
        AlignedInColumns = lambda _: f"{_:{max_length}}" if _ != "\n" else "\n"
        output = map(AlignedInColumns, output)
        output = "".join(output).rstrip()

        spaces = indent * " "
        return spaces + f"\n{spaces}".join(map(str.rstrip, output.splitlines()))

    return tuple(output)


def _ModulesUsingPkgUtil() -> tuple[str, ...]:
    """
    Returns more results than using importlib.
    """
    return tuple(
        sorted(
            _elm.name
            for _elm in pkgs.iter_modules()
            if _elm.ispkg and (_elm.name[0] != "_") and ("__" not in _elm.name)
        )
    )


# import importlib.metadata as mprt
# def _ModulesUsingImportlib() -> tuple[str, ...]:
#     """"""
#     return tuple(
#         sorted(
#             _elm
#             for _elm in mprt.packages_distributions()
#             if (_elm[0] != "_") and ("__" not in _elm) and ("/" not in _elm)
#         )
#     )


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
