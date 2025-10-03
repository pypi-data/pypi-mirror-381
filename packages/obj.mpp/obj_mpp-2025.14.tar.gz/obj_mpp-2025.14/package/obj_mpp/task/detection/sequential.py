"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2018
SEE COPYRIGHT NOTICE BELOW
"""

import typing as h
from multiprocessing.managers import ListProxy as list_shared_t

from logger_36 import L
from mpss_tools_36.numpy_ import AdditionalSharedCopy, DisposeSharedArrayCopy
from mpss_tools_36.server.data import DataFromServer, line_end_t
from mpss_tools_36.server.data import server_t as data_server_t
from mpss_tools_36.server.feedback import send_feedback_h
from obj_mpp.constant.catalog import MPM_CATALOG_SECTION, Q_CATALOG_SECTION
from obj_mpp.task.catalog.importer import ImportedElement
from obj_mpp.type.detection import detection_t
from p_pattern.type.instance.parameter.position import coordinate_h
from p_pattern.type.model.parameter import parameter_h as mark_h
from p_pattern.type.sampler.domain import chunked_domain_h, domain_h, interval_h
from p_pattern.type.sampler.instance import sampler_t


def DetectObjectsInOneChunk(
    detection_or_prm: detection_t | dict[str, h.Any],
    /,
    *,
    n_workers: int = 0,
    task_id: int = 0,
    config_server: data_server_t | None = None,
    signal_server: data_server_t | None = None,
    config_line: tuple[line_end_t | None, line_end_t | None] = (None, None),
    signal_line: tuple[line_end_t | None, line_end_t | None] = (None, None),
    lock: h.Any | None = None,
    output: list_shared_t[tuple[tuple[coordinate_h | mark_h, ...], ...]] | None = None,
    SendFeedback: send_feedback_h | None = None,
) -> None:
    """
    When called in sequential mode:
        - detection_or_prm is a detection,
        - domain is the full signal domain,
        - output is None since the detection serves as output,
        - previous_detection is None since the detection has been initialized with the
        history.
    When called in parallel mode:
        - detection_or_prm is a parameter dictionary,
        - domain is a domain chunk,
        - output is a multiprocessing.Manager (shared) list,
        - previous_detection is a list of instance descriptions in the domain chunk, or
        None.
    """
    if SendFeedback is None:
        SendFeedback = lambda _, __: None

    model_t = ImportedElement(
        DataFromServer(*config_line, "object", server=config_server)["definition"],
        MPM_CATALOG_SECTION,
    )
    model = model_t()
    mark_ranges = DataFromServer(*config_line, "mark_ranges", server=config_server)
    if not model.ShapeIntervalsAreValid(mark_ranges):
        L.CommitIssues()
        SendFeedback(-1, 0)
        return

    model.SetShapeIntervals(mark_ranges)

    quality_context_t = ImportedElement(
        DataFromServer(*config_line, "quality", server=config_server)["definition"],
        Q_CATALOG_SECTION,
    )
    if quality_context_t is not None:
        quality_context_t = quality_context_t[0]

    if L.has_staged_issues:
        L.CommitIssues()
        SendFeedback(-1, 0)
        return

    signal_lengths = DataFromServer(
        *signal_line, "signal_lengths", server=signal_server
    )
    signal_domain = tuple((0, _ - 1) for _ in signal_lengths)
    map_or_pdf = DataFromServer(*signal_line, "map_or_pdf", server=signal_server)
    if map_or_pdf is None:
        domain, map_or_pdf_shared_memory = signal_domain, None
        precision = DataFromServer(*config_line, "object", server=config_server)[
            "center"
        ]
        if isinstance(precision, h.Sequence) and (
            precision.__len__() != domain.__len__()
        ):
            L.error(
                f"Mismatch between domain dimension ({domain.__len__()}) and "
                f"number of precisions ({precision.__len__()})."
            )
            SendFeedback(-1, 0)
            return
    else:
        domain, map_or_pdf_shared_memory = AdditionalSharedCopy(map_or_pdf)
        precision = None
    if n_workers > 1:
        chunked_bounds = ChunkedBounds(signal_lengths, signal_domain, n_workers)
        before, chunks, after = chunked_bounds
        restriction = before + (chunks[task_id - 1],) + after
    else:
        restriction = None

    sampler = sampler_t(
        model=model,
        domain=domain,
        restriction=restriction,
        precision=precision,
        seed=DataFromServer(*config_line, "mpp", server=config_server)["seed"],
    )
    if map_or_pdf_shared_memory is not None:
        DisposeSharedArrayCopy(map_or_pdf_shared_memory)
    if (sampler is None) or (sampler.position is None):
        L.error("Position sampling cannot be done.")
        SendFeedback(-1, 0)
        return

    q_kwargs = (DataFromServer(*config_line, "quality_prm", server=config_server),)
    s_kwargs = (
        DataFromServer(*config_line, "signal_processing_prm", server=config_server),
    )
    if q_kwargs is None:
        q_kwargs = {}
    else:
        q_kwargs = dict(zip(q_kwargs[:-1:2], q_kwargs[1::2]))
    if s_kwargs is None:
        s_kwargs = {}
    else:
        s_kwargs = dict(zip(s_kwargs[:-1:2], s_kwargs[1::2]))
    quality_context = quality_context_t(domain=sampler.position.domain)
    quality_context.SetKwargs(q_kwargs, s_kwargs)

    signal_for_qty_name = DataFromServer(
        *signal_line, "signal_for_qty", server=signal_server
    )
    signal_for_qty, signal_for_qty_raw = AdditionalSharedCopy(signal_for_qty_name)
    if quality_context.SetSignal(signal_for_qty, sampler):
        L.error("Signal skipped by quality context.")
        SendFeedback(-1, 0)
        return

    if isinstance(detection_or_prm, detection_t):
        detection = detection_or_prm
        detection.sampler = sampler
    else:
        detection = detection_t(sampler=sampler, **detection_or_prm)

    for i_idx in range(1, detection.n_iterations + 1):
        candidates = detection.NewCandidates(quality_context)
        if candidates.__len__() > 0:
            detection.Update(candidates)
            detection.Refine(quality_context)

        SendFeedback(i_idx, detection.__len__())
    DisposeSharedArrayCopy(signal_for_qty_raw)

    detection.FilterOutCropped()

    if output is not None:
        with lock:
            output.append(
                (sampler.position.domain.lengths,)
                + tuple(_.as_tuple for _ in detection)
            )


def ChunkedBounds(
    lengths: tuple[int, ...], domain: domain_h, n_workers: int, /
) -> chunked_domain_h:
    """"""
    max_length = max(lengths)
    where = lengths.index(max_length)
    chunks = _ChunksForLength(n_workers, max_length)

    return domain[:where], chunks, domain[(where + 1) :]


def _ChunksForLength(n_workers: int, length: int, /) -> tuple[interval_h, ...]:
    """"""
    if n_workers < length:
        chunk_size = length // n_workers
        remainder = length % n_workers
        chunk_sizes = n_workers * [chunk_size]
        for chunk_idx in range(remainder):
            chunk_sizes[chunk_idx] += 1
    else:
        chunk_sizes = length * [1]

    output = [(0, chunk_sizes[0] - 1)]
    for chunk_idx, chunk_size in enumerate(chunk_sizes[1:]):
        last = output[chunk_idx][1]
        output.append((last + 1, last + chunk_size))

    return tuple(output)


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
