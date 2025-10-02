"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import dataclasses as d
import time
import typing as h
from multiprocessing import Lock as NewLock

from mpss_tools_36.server.feedback import FormatedDuration, send_feedback_h
from mpss_tools_36.server.feedback import server_t as base_t


@d.dataclass(slots=True, repr=False, eq=False)
class server_t(base_t):
    previous_task_idx: int = d.field(init=False, default=-1)
    lock: h.Any = d.field(init=False, default_factory=NewLock)

    @staticmethod
    def _SendFeedback(
        iterations: int,
        main_counter: int,
        /,
        *,
        task_idx: int = -1,
        n_iterations_per_task: int | h.Sequence[int] = 0,
        prefix: str = "",
        start_time: float = 0.0,
        period: float = 0.0,
        lock: h.Any = None,
    ) -> None:
        """
        Setting method attributes does not work with a class method.
        """
        if isinstance(n_iterations_per_task, int):
            n_iterations = n_iterations_per_task
        else:
            n_iterations = n_iterations_per_task[task_idx]
        if n_iterations == 0:
            return

        prologue = f"{prefix}{task_idx + 1}: "
        now = time.time()
        elapsed_time = now - start_time
        elapsed_time_formatted = FormatedDuration(elapsed_time)

        if (iterations is None) or (iterations == n_iterations):
            message = f"{prologue}DONE #{main_counter} +{elapsed_time_formatted}"
            with lock:
                print(f"{message: <50}", flush=True)
            return

        with lock:
            reference = getattr(server_t._SendFeedback, "reference", start_time)
        if now - reference < period:
            return

        if iterations > 0:
            total_time = (elapsed_time * n_iterations) / iterations
            remaining_time = FormatedDuration(total_time - elapsed_time)
        else:
            remaining_time = "???"
        message = (
            f"{prologue}{iterations}/{n_iterations} #{main_counter} "
            f"+{elapsed_time_formatted} -{remaining_time}"
        )

        with lock:
            setattr(server_t._SendFeedback, "reference", now)
            print(f"{message: <50}\r", end="", flush=True)

    def NewFeedbackSendingFunction(self) -> send_feedback_h:
        """"""
        start_time = time.time()  # Assign to variable to allow for proper closure.
        task_idx = self.previous_task_idx + 1
        self.previous_task_idx = task_idx

        return lambda _, __: self.__class__._SendFeedback(
            _,
            __,
            task_idx=task_idx,
            n_iterations_per_task=self.n_iterations_per_task,
            prefix=self.prefix,
            start_time=start_time,
            period=self.feedback_period,
            lock=self.lock,
        )

    def RunUntilExhausted(self) -> None:
        """"""
        pass


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
