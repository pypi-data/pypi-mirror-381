"""
Copyright CNRS/Inria/UniCA
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2018
SEE COPYRIGHT NOTICE BELOW
"""

import multiprocessing as prll
import typing as h
from multiprocessing import Process as process_t
from multiprocessing.managers import ListProxy as list_shared_t

from mpss_tools_36.server.data import server_t as data_server_t
from mpss_tools_36.server.feedback_fake import server_t as feedback_server_t
from mpss_tools_36.task import StartAndTrackTasks
from obj_mpp.task.detection.sequential import DetectObjectsInOneChunk
from p_pattern.type.instance.parameter.position import coordinate_h
from p_pattern.type.model.parameter import parameter_h as mark_h


def DetectObjectsInAllChunks(
    detection_prm: dict[str, h.Any],
    config_server: data_server_t,
    signal_server: data_server_t,
    n_workers: int,
    output: list_shared_t[tuple[tuple[coordinate_h | mark_h, ...], ...]],
    lock: h.Any,
    feedback_server: feedback_server_t,
    /,
) -> None:
    """"""
    # Alternative: ProcessPoolExecutor + executor.submit + as_completed + .result().
    tasks = []
    for task_id in range(1, n_workers + 1):
        task = process_t(
            target=DetectObjectsInOneChunk,
            args=(detection_prm,),
            kwargs={
                "n_workers": n_workers,
                "task_id": task_id,
                "config_line": config_server.NewLine(),
                "signal_line": signal_server.NewLine(),
                "lock": lock,
                "output": output,
                "SendFeedback": feedback_server.NewFeedbackSendingFunction(),
            },
        )
        tasks.append(task)

    config_server.Start()
    signal_server.Start()

    StartAndTrackTasks(tasks, feedback_server=feedback_server)

    config_server.Stop(should_dispose_shared_resources=False)
    signal_server.Stop()


def NParallelWorkers(hint: int, /) -> int:
    """"""
    if (hint != 1) and (prll.get_start_method(allow_none=False) == "fork"):
        if hint > 0:
            output = hint
        else:
            output = (3 * prll.cpu_count()) // 2
    else:
        # Disables parallel computation if requested or if using Windows, since pickle
        # cannot handle it.
        output = 1

    return output


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
