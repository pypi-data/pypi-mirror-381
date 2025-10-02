"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import typing as h
from multiprocessing import Process as process_t

from mpss_tools_36.server.feedback import server_t


def StartAndTrackTasks(
    tasks: h.Sequence[process_t], /, *, feedback_server: server_t | None = None
) -> None:
    """"""
    feedback_server_exists = feedback_server is not None

    if feedback_server_exists:
        feedback_server.ReportTaskStarting(tasks.__len__())
        prefix = feedback_server.prefix
    else:
        prefix = ""

    for task in tasks:
        task.start()

    if feedback_server_exists:
        feedback_server.ReportTaskStarting(0)
        feedback_server.RunUntilExhausted(tasks)

    for task_id, task in enumerate(tasks, start=1):
        if task.exitcode is None:
            task.join()
        if task.exitcode != 0:
            print(f"{prefix}Task {task_id} exited with error code {task.exitcode}.")


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
