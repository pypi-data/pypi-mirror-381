"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2018
SEE COPYRIGHT NOTICE BELOW
"""

import collections.abc as a
import dataclasses as d
import typing as h
from pathlib import Path as path_t

import numpy as nmpy
from p_pattern.type.sampler.domain import domain_h

array_t = nmpy.ndarray


@d.dataclass(slots=True, repr=False, eq=False)
class signal_context_t:
    """
    Domain-related details correspond to the domain the marked points will be
    superimposed on. In particular, the dimension is the dimension of marked points.
    """

    signal_path_or_folder: path_t
    map_or_pdf_path_or_folder: path_t | str | None

    signal_path: path_t = d.field(init=False, default=None)
    map_or_pdf_path: path_t = d.field(init=False, default=None)

    lengths: tuple[int, ...] = d.field(init=False)

    signal_original: h.Any = d.field(init=False)
    signal_for_qty: h.Any = d.field(init=False)
    map_or_pdf: array_t | None = d.field(init=False, default=None)

    def __post_init__(self) -> None:
        """"""
        self.signal_path_or_folder = path_t(self.signal_path_or_folder)
        if isinstance(self.map_or_pdf_path_or_folder, str):
            self.map_or_pdf_path_or_folder = path_t(self.map_or_pdf_path_or_folder)
        elif isinstance(self.map_or_pdf_path_or_folder, path_t):
            pass
        else:  # Domain precision(s) for position sampling.
            self.map_or_pdf_path_or_folder = None

    def SignalDetails(
        self,
    ) -> a.Iterator[tuple[path_t, bool, bool, str, path_t | None, bool, bool, str]]:
        """"""
        if self.map_or_pdf_path_or_folder is None:
            MapOrPDFPathFromSignal = lambda _: None
        elif self.map_or_pdf_path_or_folder.is_file():
            MapOrPDFPathFromSignal = lambda _: self.map_or_pdf_path_or_folder
        elif self.signal_path_or_folder.is_file():
            MapOrPDFPathFromSignal = lambda _: self.map_or_pdf_path_or_folder / _.name
        else:
            MapOrPDFPathFromSignal = (
                lambda _: self.map_or_pdf_path_or_folder
                / _.relative_to(self.signal_path_or_folder)
            )

        if self.signal_path_or_folder.is_dir():
            signal_paths = self.signal_path_or_folder.rglob("*.*")
        else:
            signal_paths = (self.signal_path_or_folder,)
        for path in signal_paths:
            output = []
            for current, attribute in (
                (path, "signal_path"),
                (MapOrPDFPathFromSignal(path), "map_or_pdf_path"),
            ):
                previous = getattr(self, attribute)
                setattr(self, attribute, current)
                output.extend(
                    (
                        current,
                        (current is not None) and current.is_file(),
                        current != previous,
                        f"{path.stem}_{path.suffix[1:]}",
                    )
                )

            yield tuple(output)

    def SetSignals(self, signal: h.Any, dimension: int, /) -> None:
        """"""
        assert nmpy.all(signal >= 0)

        self.lengths = signal.shape[:dimension]

        self.signal_original = signal
        self.signal_for_qty = nmpy.empty_like(signal, dtype=nmpy.uint16)
        signal_max = signal.max()
        if signal_max == 0:
            signal_max = 1.0
        nmpy.rint(
            (2**16 - 1) * (signal / signal_max),
            casting="unsafe",
            out=self.signal_for_qty,
        )

    def SetMapOrPDF(self, map_or_pdf: array_t, /) -> None:
        """"""
        assert nmpy.all(map_or_pdf >= 0)

        array_sum = map_or_pdf.sum()
        if array_sum == 0:
            array_sum = 1.0
        self.map_or_pdf = (map_or_pdf / array_sum).astype(dtype=nmpy.float16)


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
