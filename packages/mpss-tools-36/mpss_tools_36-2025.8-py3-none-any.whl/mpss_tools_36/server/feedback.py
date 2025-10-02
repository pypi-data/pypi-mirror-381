"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import dataclasses as d
import time
import typing as h
from multiprocessing import Process as process_t
from multiprocessing import Value as shared_value_t
from multiprocessing import current_process as CurrentProcess
from threading import Thread as thread_t

from mpss_tools_36.server.constant import MAIN_PROCESS_NAME

send_feedback_h = h.Callable[[int, int], None]

_DONE = "▮"
_TO_DO = "▯"
_UNKNOWN_VALUE = "???"


@d.dataclass(slots=True, repr=False, eq=False)
class server_t:
    n_iterations_per_task: int | h.Sequence[int]

    prefix: str = ""
    feedback_period: float = 3.0
    print_report: bool = False

    _message_template: str = d.field(init=False)
    _shared_iterations_per_task: list[h.Any] = d.field(init=False, default_factory=list)
    _shared_main_counter_per_task: list[h.Any] = d.field(
        init=False, default_factory=list
    )
    _thread: thread_t | None = d.field(init=False, default=None)

    def __post_init__(self) -> None:
        """"""
        assert CurrentProcess().name == MAIN_PROCESS_NAME

        self._message_template = (
            self.prefix + "|{}{: >6.2f}% {}| @ {}s/it #{} +{} -{}:{}"
        )

    def NewFeedbackSendingFunction(self) -> send_feedback_h:
        """"""
        shared_iterations, shared_main_counter = (
            shared_value_t("Q"),
            shared_value_t("Q"),
        )

        self._shared_iterations_per_task.append(shared_iterations)
        self._shared_main_counter_per_task.append(shared_main_counter)

        def _SendFeedback(iterations: int, main_counter: int, /) -> None:
            #
            shared_iterations.value = iterations
            shared_main_counter.value = main_counter

        return _SendFeedback

    def Start(self) -> None:
        """
        For sequential processing.
        """
        process = CurrentProcess()
        assert process.name == MAIN_PROCESS_NAME
        assert self._thread is None

        self._thread = thread_t(target=self.RunUntilExhausted, args=((process,),))
        self._thread.start()

    def RunUntilExhausted(self, tasks: h.Sequence[process_t], /) -> None:
        """
        For parallel processing (when called directly).
        """
        reference = start_time = time.time()

        n_tasks = self._shared_iterations_per_task.__len__()
        assert n_tasks > 0

        if isinstance(self.n_iterations_per_task, int):
            self.n_iterations_per_task = n_tasks * (self.n_iterations_per_task,)
        else:
            assert self.n_iterations_per_task.__len__() == n_tasks, (
                self.n_iterations_per_task.__len__(),
                n_tasks,
            )
        n_iterations_total = float(sum(self.n_iterations_per_task))
        if n_iterations_total == 0.0:
            return

        # See below about format.
        half_bar = 20 * _TO_DO
        message = self._message_template.format(
            half_bar,
            0.0,
            half_bar,
            _UNKNOWN_VALUE,
            _UNKNOWN_VALUE,
            "00",
            _UNKNOWN_VALUE,
            n_tasks,
        )
        message_length = message.__len__()
        print(f"{message}\r", end="", flush=True)

        while True:
            n_iterations_completed, total_main_counter = 0.0, 0
            n_active_tasks = n_tasks
            for task, n_iterations, shared_iterations, shared_main_counter in zip(
                tasks,
                self.n_iterations_per_task,
                self._shared_iterations_per_task,
                self._shared_main_counter_per_task,
                strict=True,
            ):
                iterations = shared_iterations.value
                if (iterations < 0) or (
                    (iterations < n_iterations) and not task.is_alive()
                ):
                    iterations = n_iterations
                    shared_iterations.value = n_iterations
                n_iterations_completed += iterations
                total_main_counter += shared_main_counter.value

                if iterations == n_iterations:
                    n_active_tasks -= 1

            if n_active_tasks == 0:
                break

            now = time.time()
            if now - reference < self.feedback_period:
                time.sleep(1.0)
                continue
            reference = now

            completion = n_iterations_completed / n_iterations_total

            elapsed_time = now - start_time
            if completion > 0.0:
                remaining_time = (elapsed_time / completion) - elapsed_time
                remaining_time = FormatedDuration(remaining_time)
            else:
                remaining_time = _UNKNOWN_VALUE
            if n_iterations_completed > 0.0:
                period = n_tasks * elapsed_time / n_iterations_completed
                period = f"{period:.2f}"
            else:
                period = _UNKNOWN_VALUE

            # 48 = 20_X_or_- (as in [:20])
            #    + 6_percent (as in 6.2f) + 1_% + 1_space
            #    + 20_X_or_- (as in [-20:]).
            n_completed = int(round(48.0 * completion))
            bar = f"{n_completed * _DONE}{(48 - n_completed) * _TO_DO}"
            message = self._message_template.format(
                bar[:20],
                100.0 * completion,
                bar[-20:],
                period,
                total_main_counter,
                FormatedDuration(elapsed_time),
                remaining_time,
                n_active_tasks,
            )
            message_length = max(message_length, message.__len__())
            print(f"{message: <{message_length}}\r", end="", flush=True)

            time.sleep(1.0)

        if self.print_report:
            elapsed_time = time.time() - start_time
            period = n_tasks * elapsed_time / n_iterations_total
            message = (
                f"{self.prefix}Summary: "
                f"{period:.2f}s/it "
                f"#{total_main_counter} "
                f"+{FormatedDuration(elapsed_time)}"
            )
            print(f"{message: <{message_length}}", flush=True)
        else:
            space = " "
            print(f"{space: <{message_length}}\r", end="", flush=True)

    def Stop(self) -> None:
        """
        For sequential processing.
        Safe to call on an un-started server.
        """
        assert CurrentProcess().name == MAIN_PROCESS_NAME

        if self._thread is not None:
            self._thread.join()
            self._thread = None

    def ReportTaskStarting(self, n_tasks: int, /) -> None:
        """"""
        if n_tasks > 0:
            print(f"{self.prefix}Starting {n_tasks} tasks...", flush=True)
        else:
            print(f"{self.prefix}All tasks started.", flush=True)


def FormatedDuration(duration: float, /) -> str:
    """"""
    if duration >= 86400:
        return "1d+"

    output = time.strftime("%Hh%Mm%Ss", time.gmtime(duration))
    while output.startswith("00"):
        output = output[3:]

    if output.__len__() > 0:
        return output
    return "00s"


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
