"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2018
SEE COPYRIGHT NOTICE BELOW
"""

import sys as sstm

from conf_ini_g.api.console import CommandLineConfig, CommandLineParser
from conf_ini_g.api.functional import config_definition_h as config_raw_h
from conf_ini_g.api.functional import config_t as config_definition_t
from logger_36 import L
from logger_36.catalog.logger.system import LogSystemDetails
from obj_mpp.config.app import APP_NAME
from obj_mpp.constant.config.definition import DEFINITION
from obj_mpp.task.catalog.specifier import (
    SpecifyCatalogMarkedPoints,
    SpecifyCatalogQualities,
)
from obj_mpp.task.detection.multiple import DetectedObjects


def Main() -> None:
    """"""
    L.MakeMonochrome()
    LogSystemDetails()

    config, *_ = Config(APP_NAME, DEFINITION)
    _ = DetectedObjects(config.active_as_typed_dict)

    # LogElapsedTime()  # FIXME: Why logging here does not print anything?


def Config(
    title: str, definition_raw: config_raw_h, /
) -> tuple[config_definition_t, bool]:
    """"""
    definition = config_definition_t(definition_raw)
    SpecifyCatalogMarkedPoints(definition)
    SpecifyCatalogQualities(definition)

    parser = CommandLineParser(title, definition)
    config_cmdline, advanced_mode, ini_path = CommandLineConfig(parser)

    if (config_cmdline.__len__() == 0) and (ini_path is None):
        raise RuntimeError(
            "No Configuration passed, either as an INI file or "
            "as command-line arguments."
        )

    issues = definition.UpdateFromINI(ini_path)
    issues.extend(definition.UpdateFromDict(config_cmdline))
    if issues.__len__() > 0:
        # Issues can have has_actual_expected indicators. They are removed here.
        issues = (_ if isinstance(_, str) else _[0] for _ in issues)
        L.critical("!!!!\n" + "\n".join(issues) + "\n!!!!")
        sstm.exit(1)

    return definition, advanced_mode


if __name__ == "__main__":
    #
    Main()


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
