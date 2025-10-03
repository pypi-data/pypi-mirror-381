"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2018
SEE COPYRIGHT NOTICE BELOW
"""

from multiprocessing import Manager as NewSharingManager

import numpy as nmpy
import obj_mpp.task.detection.parallel as prll
from conf_ini_g.api.functional import config_typed_h
from logger_36 import L
from logger_36.constant.message import LINE_INDENT
from mpss_tools_36.server.data import server_t as data_server_t
from mpss_tools_36.server.feedback import server_t as feedback_server_t
from mpss_tools_36.server.feedback_fake import server_t as fake_feedback_server_t
from obj_mpp.task.detection.sequential import DetectObjectsInOneChunk
from obj_mpp.type.detection import detection_t
from p_pattern.type.instance.generic import instance_t

array_t = nmpy.ndarray


def DetectedObjects(
    instance_tt: type[instance_t],
    config: config_typed_h,
    config_server: data_server_t,
    signal_server: data_server_t,
    n_workers: int,
    /,
) -> list[instance_t]:
    """"""
    n_new_per_iteration = config["mpp"]["n_new_per_iteration"] // n_workers
    if n_new_per_iteration == 0:
        L.warning(
            "Number of generated marked points in each chunk per iteration is zero."
        )
        return []

    detection_prm = {
        "instance_tt": instance_tt,
        "max_overlap": config["constraints"]["max_overlap"],
        "min_quality": config["quality"]["min_value"],
        "only_un_cropped": config["object"]["only_un_cropped"],
        "n_iterations": config["mpp"]["n_iterations"],
        "n_new_per_iteration": n_new_per_iteration,
        "refinement_interval": config["refinement"]["interval"],
        "n_new_per_refinement": config["refinement"]["n_attempts"],
        "max_refinement_variation": config["refinement"]["max_variation"],
    }
    detection = detection_t(**detection_prm)

    if config["output"]["feedback"] == "true":
        actual_feedback_server_t = feedback_server_t
    else:
        actual_feedback_server_t = fake_feedback_server_t
    feedback_server = actual_feedback_server_t(
        n_iterations_per_task=detection_prm["n_iterations"],
        feedback_period=2,
        print_report=True,
        prefix=LINE_INDENT,
    )

    L.SetInstantName("Ready for detection")

    if n_workers > 1:
        sharing_manager = NewSharingManager()
        output = sharing_manager.list()
        lock = sharing_manager.Lock()

        prll.DetectObjectsInAllChunks(
            detection_prm,
            config_server,
            signal_server,
            n_workers,
            output,
            lock,
            feedback_server,
        )

        if output.__len__() == n_workers:
            L.info(
                f"Marked point(s) per task: {tuple(_.__len__() - 1 for _ in output)}"
            )
            domain_lengths = output[0][0]
            grid_sites = tuple(nmpy.indices(domain_lengths))
            for from_chunk_w_lengths in output:
                from_chunk = from_chunk_w_lengths[1:]
                if from_chunk.__len__() == 0:
                    continue
                detection.Update(
                    from_chunk,
                    domain_lengths=domain_lengths,
                    grid_sites=grid_sites,
                    live_mode=False,
                )
        else:
            L.error(
                f"Only {output.__len__()} worker(s) out of {n_workers} run thoroughly"
            )

        sharing_manager.shutdown()
    else:
        SendFeedback = feedback_server.NewFeedbackSendingFunction()
        feedback_server.Start()

        DetectObjectsInOneChunk(
            detection,
            config_server=config_server,
            signal_server=signal_server,
            SendFeedback=SendFeedback,
        )

        feedback_server.Stop()

        signal_server.DisposeSharedResources()

    L.SetInstantName("Detection done")

    return detection.AsListWithDecreasingQualities()


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
