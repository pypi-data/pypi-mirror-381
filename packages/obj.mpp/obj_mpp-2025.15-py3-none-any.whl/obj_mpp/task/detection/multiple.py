"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2018
SEE COPYRIGHT NOTICE BELOW
"""

from pathlib import Path as path_t

from conf_ini_g.interface.storage.config import SaveConfigToINIDocument
from conf_ini_g.type.dict import config_typed_h
from logger_36.catalog.logger.chronos import LogElapsedTime
from logger_36.instance.logger import L
from logger_36.task.measure.chronos import TimeStamp
from mpss_tools_36.server.data import SendDataToServer, server_t
from obj_mpp.constant.catalog import (
    I_CATALOG_SECTION,
    MPI_CATALOG_SECTION,
    MPM_CATALOG_SECTION,
    O_CATALOG_SECTION,
)
from obj_mpp.interface.console.detection import ReportDetectedMarkedPoints
from obj_mpp.interface.storage.save import detection as svdt
from obj_mpp.interface.storage.save.generic import CreateOutputFolder, OutputDocument
from obj_mpp.task.catalog.importer import ImportedElement
from obj_mpp.task.detection import parallel as prll
from obj_mpp.task.detection.single import DetectedObjects as DetectedObjectsSingle
from obj_mpp.task.validation.interface import CheckOutputFunction, CheckRequestedOutputs
from obj_mpp.type.signal.context import signal_context_t
from p_pattern.type.instance.generic import instance_t as base_instance_t

SaveDetection = dict(
    zip(
        ("contour", "region", "region_numpy"),
        (
            svdt.SaveDetectionAsContourImage,
            svdt.SaveDetectionAsRegionImage,
            svdt.SaveDetectionAsRegionNumpyArray,
        ),
        strict=True,
    )
)


def DetectedObjects(config: config_typed_h, /) -> dict[path_t, list[base_instance_t]]:
    """"""
    output = {}

    L.ResetEventCounts()
    time_tag = TimeStamp()

    config_server = server_t(name="config", data=config)
    signal_server = server_t(name="signal", is_read_only=False)

    model_t = ImportedElement(config["object"]["definition"], MPM_CATALOG_SECTION)
    instance_t = ImportedElement(config["object"]["definition"], MPI_CATALOG_SECTION)
    model = model_t()
    dimension = model.dimension

    LoadedSignalMapOrPDF = ImportedElement(
        config["signal"]["loading_function"], I_CATALOG_SECTION
    )

    n_workers = prll.NParallelWorkers(config["mpp"]["n_parallel_workers"])
    if n_workers > 1:
        L.MakeMultiSafe()

    requested_outputs = config["output"]["what"]
    if requested_outputs is None:
        requested_outputs = ()
    else:
        requested_outputs = tuple(map(str.strip, requested_outputs.split(",")))
        CheckRequestedOutputs(requested_outputs)
    if config["output"]["output_function"] is None:
        ReportDetectionResult = None
    else:
        ReportDetectionResult = ImportedElement(
            config["output"]["output_function"], O_CATALOG_SECTION
        )
        CheckOutputFunction(ReportDetectionResult, config["output_prm"])

    output_folder = config["output"]["base_folder"]
    if output_folder is not None:
        output_folder = CreateOutputFolder(output_folder / time_tag)

    # No map or PDF by default.
    SendDataToServer(None, None, map_or_pdf=None, server=signal_server)

    signal_context = signal_context_t(
        signal_path_or_folder=config["signal"]["path"],
        map_or_pdf_path_or_folder=config["object"]["center"],
    )
    for signal_idx, (
        signal_path,
        signal_is_valid,
        _,  # signal_is_new
        signal_id,
        map_or_pdf_path,
        map_or_pdf_is_valid,
        map_or_pdf_is_new,
        __,  # map_or_pdf_id
    ) in enumerate(signal_context.SignalDetails(), start=1):
        L.DisplayRule()
        L.info(f"Signal#{signal_idx}: {signal_path}")

        L.SetInstantName(f"Ready for signal {signal_idx}")

        if (not signal_is_valid) or (
            (map_or_pdf_path is not None) and not map_or_pdf_is_valid
        ):
            L.error(
                f"Invalid signal(s):\n"
                f"    {signal_path}:{signal_is_valid}\n"
                f"    {map_or_pdf_path}:{map_or_pdf_is_valid}"
            )
            continue

        if not _LoadSignalAndSendToServer(
            signal_path,
            signal_context,
            dimension,
            LoadedSignalMapOrPDF,
            signal_server,
            **config["signal_loading_prm"],
        ):
            continue
        if (map_or_pdf_path is not None) and map_or_pdf_is_new:
            if not _LoadMapOrPDFAndSendToServer(
                map_or_pdf_path,
                signal_context,
                LoadedSignalMapOrPDF,
                signal_server,
                **config["signal_loading_prm"],
            ):
                continue

        L.SetInstantName(f"Signal {signal_idx} loaded")

        local_output = DetectedObjectsSingle(
            instance_t, config, config_server, signal_server, n_workers
        )
        output[signal_path] = local_output

        if L.has_staged_issues:
            L.CommitIssues()
            continue

        if local_output.__len__() == 0:
            continue

        if config["output"]["console"]:
            ReportDetectedMarkedPoints(local_output, model)

        if output_folder is not None:
            L.info(f"Saving detection result to {output_folder}...")
            SaveConfigToINIDocument(
                config, OutputDocument(output_folder, "config", "ini", signal_id)
            )
            if "csv" in requested_outputs:
                svdt.SaveDetectionInCSVFormat(
                    local_output,
                    model,
                    signal_id,
                    None,
                    output_folder,
                    sep=config["output"]["marks_separator"],
                )
            if "json" in requested_outputs:
                svdt.SaveDetectionInJSONFormat(local_output, signal_id, output_folder)
            for what in requested_outputs:
                if what not in ("csv", "json"):
                    SaveDetection[what](
                        dimension,
                        signal_context.lengths,
                        local_output,
                        signal_id,
                        output_folder,
                    )

        # Leave here so that in case it contains blocking instructions (like matplotlib
        # show()), it does not delay saving to files above.
        if ReportDetectionResult is not None:
            L.info(
                f"Reporting detection result with {ReportDetectionResult.__name__}..."
            )
            L.SetInstantName(f"Reporting for signal {signal_idx}")
            ReportDetectionResult(
                model,
                local_output,
                signal_context.signal_original,
                output_folder,
                signal_context.lengths,
                signal_id=signal_id,
                **config["output_prm"],
            )

    config_server.DisposeSharedResources()

    L.RemoveMultiSafety()
    LogElapsedTime()

    return output


def _LoadSignalAndSendToServer(
    path: path_t,
    context: signal_context_t,
    dimension: int,
    LoadedSignal,
    server: server_t,
    **signal_loading_prm,
) -> bool:
    """"""
    loaded, error = LoadedSignal(path, **signal_loading_prm)
    if error is None:
        context.SetSignals(loaded, dimension)

        L.info(
            f"{path}:\n"
            f"    shape={context.signal_original.shape}\n"
            f"    size={context.signal_original.nbytes / 10**6:_.3f}MB"
        )
        L.info(
            f"Signal for Quality:\n"
            f"    shape={context.signal_for_qty.shape}\n"
            f"    size={context.signal_for_qty.nbytes / 10**6:_.3f}MB"
        )

        SendDataToServer(
            None,
            None,
            signal_lengths=context.lengths,
            signal_for_qty=context.signal_for_qty,
            server=server,
        )
        context.signal_for_qty = None
        return True

    L.error(f"Unable to load {path}:\n{error}")
    return False


def _LoadMapOrPDFAndSendToServer(
    path: path_t,
    context: signal_context_t,
    LoadedMapOrPDF,
    server: server_t,
    **signal_loading_prm,
) -> bool:
    """"""
    loaded, error = LoadedMapOrPDF(path, **signal_loading_prm)
    if error is None:
        context.SetMapOrPDF(loaded)

        L.info(
            f"{path}:\n"
            f"    shape={context.map_or_pdf.shape}\n"
            f"    size={context.map_or_pdf.nbytes / 10**6:_.3f}MB"
        )

        SendDataToServer(None, None, map_or_pdf=context.map_or_pdf, server=server)
        context.map_or_pdf = None
        return True

    L.error(f"Unable to load {path}:\n{error}")
    return False


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
