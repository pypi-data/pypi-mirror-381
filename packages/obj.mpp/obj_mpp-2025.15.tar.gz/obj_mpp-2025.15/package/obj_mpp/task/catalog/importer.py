"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2018
SEE COPYRIGHT NOTICE BELOW
"""

import inspect as nspt
import typing as h
from pathlib import Path as path_t

from logger_36 import L
from obj_mpp.constant.catalog import catalog_section_t
from obj_mpp.constant.config.parameter import MOD_ELM_SEPARATOR
from obj_mpp.extension.importer import IsOriginalAndExported, ModuleFromPath


def ImportedElement(query: str | None, catalog_section: catalog_section_t, /) -> h.Any:
    """"""
    output = {}

    if query is None:
        path = None
    else:
        path, query = _ModuleAndElement(query)
    if path is None:
        path = catalog_section.BasePath()
        # Tuple-d for potential error message below.
        paths = tuple(path.glob(catalog_section.pattern))
    else:
        paths = (path,)

    for path in paths:
        module = ModuleFromPath(path)
        for name, value in nspt.getmembers(module, catalog_section.type_for_getmembers):
            if IsOriginalAndExported(name, value, path) and (
                (catalog_section.type_for_issubclass is None)
                or issubclass(value, catalog_section.type_for_issubclass)
            ):
                name = catalog_section.ElementName(name)
                value = catalog_section.ElementValue(value)
                if query is None:
                    output[name] = value
                elif name == query:
                    return value

    if query is None:
        return output

    paths = "\n".join(map(str, paths))
    L.StageIssue(f'Element "{query}" not found in:\n{paths}')
    return None


def _ModuleAndElement(composite: str, /) -> tuple[path_t | None, str]:
    """"""
    if MOD_ELM_SEPARATOR in composite:
        document, element = composite.rsplit(sep=MOD_ELM_SEPARATOR, maxsplit=1)
        if document.__len__() > 0:
            document = path_t(document)
        else:
            document = None
    else:
        document = None
        element = composite

    return document, element


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

This software is being developed by Eric Debreuve, a CNRS employee and
member of team Morpheme.
Team Morpheme is a joint team between Inria, CNRS, and UniCA.
It is hosted by the Centre Inria d'Université Côte d'Azur, Laboratory
I3S, and Laboratory iBV.

CNRS: https://www.cnrs.fr/index.php/en
Inria: https://www.inria.fr/en/
UniCA: https://univ-cotedazur.eu/
Centre Inria d'Université Côte d'Azur: https://www.inria.fr/en/centre/sophia/
I3S: https://www.i3s.unice.fr/en/
iBV: http://ibv.unice.fr/
Team Morpheme: https://team.inria.fr/morpheme/
"""
