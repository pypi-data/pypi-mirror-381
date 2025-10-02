"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import dataclasses as d
import typing as h
from multiprocessing import Queue as NewQueue
from multiprocessing import current_process as CurrentProcess
from multiprocessing.shared_memory import SharedMemory as shared_memory_t
from queue import Empty as EmptyError
from threading import Thread as thread_t

import json_any as json
import numpy as nmpy
from mpss_tools_36.numpy_ import DisposeOriginalSharedArray, NewSharedArray
from mpss_tools_36.server.constant import (
    DELETION_DONE,
    MAIN_PROCESS_NAME,
    REQUEST_CHECK,
    REQUEST_CLOSE,
    REQUEST_DELETE,
    REQUEST_GET,
    REQUEST_SET,
    REQUEST_STATUS,
    REQUEST_STOP,
    STORAGE_DONE,
)

array_t = nmpy.ndarray
# name, {datum_name: datum_type_as_str}, is_read_only, is_running.
server_status_h = tuple[str, dict[str, str], bool, bool]


line_end_t = type(NewQueue())


class line_t(h.NamedTuple):
    request: line_end_t
    answer: line_end_t


@d.dataclass(slots=True, repr=False, eq=False)
class server_t:
    """
    Numpy arrays must be set (using REQUEST_SET_NUMPY) and requested alone.

    The type of data can be h.Any at instantiation time, in which case it is considered
    as an object which will be converted into an attribute-name/attribute-value
    dictionary.
    """

    name: str

    data: dict[str, h.Any] | h.Any = d.field(default_factory=dict)
    is_read_only: bool = True

    _lines: list[line_t] = d.field(init=False, default_factory=list)
    _shared_array_memory: dict[str, shared_memory_t] | None = d.field(init=False)
    _thread: thread_t | None = d.field(init=False, default=None)

    @property
    def status(self) -> server_status_h:
        """
        is_running: Always False for a fake_server_t.
        """
        return (
            self.name,
            {
                _: f"{type(__).__module__}.{type(__).__name__}"
                for _, __ in self.data.items()
            },
            self.is_read_only,
            self._thread is not None,
        )

    def __post_init__(self) -> None:
        """"""
        assert CurrentProcess().name == MAIN_PROCESS_NAME

        self._shared_array_memory = {}

        if isinstance(self.data, dict):
            return

        data = {}
        for attribute in dir(self.data):
            if attribute[0] != "_":
                data[attribute] = getattr(self.data, attribute)
        self.data = data

    def NewLine(self) -> tuple[line_end_t | h.Self, line_end_t | h.Self]:
        """"""
        assert self._thread is None

        request_line_end, answer_line_end = NewQueue(), NewQueue()
        self._lines.append(line_t(request=request_line_end, answer=answer_line_end))

        return request_line_end, answer_line_end

    def Start(self) -> None:
        """"""
        assert CurrentProcess().name == MAIN_PROCESS_NAME
        assert self._thread is None

        self._thread = thread_t(target=self._Run)
        self._thread.start()

    def _Run(self) -> None:
        """"""
        active_lines = list(self._lines)
        while active_lines.__len__() > 0:
            requests = []
            for line in tuple(active_lines):
                request_line_end = line.request
                try:
                    request = request_line_end.get(False)
                except EmptyError:
                    pass
                else:
                    requests.append((request_line_end, line.answer, request))

            for request_line_end, answer_line_end, request in requests:
                if isinstance(request, tuple):
                    request, *arguments = request
                else:
                    arguments = ()
                # assert isinstance(request, str)

                if request == REQUEST_GET:
                    # arguments must be a typing.Sequence of str.
                    data = self.RequestedData(*arguments)
                    jsoned, issues = json.JsonStringOf(data)
                    if issues is None:
                        answer_line_end.put(jsoned)
                    else:
                        raise RuntimeError(
                            f"Un-jsonable object:\n{type(data).__name__}\n"
                            + "\n".join(issues)
                        )
                elif request == REQUEST_SET:
                    # arguments must be a typing.Sequence with a single, jsoned
                    # dict[str, typing.Any].
                    un_jsoned, issues = json.ObjectFromJsonString(arguments[0])
                    if issues is None:
                        self.StoreData(**un_jsoned)
                        answer_line_end.put(STORAGE_DONE)  # For synchronization.
                    else:
                        raise RuntimeError(
                            f"Un-de-jsonable object:\n{arguments[0]}\n"
                            + "\n".join(issues)
                        )
                elif request == REQUEST_DELETE:
                    # arguments must be a typing.Sequence of str.
                    self.DeleteData(*arguments)
                    answer_line_end.put(DELETION_DONE)  # For synchronization.
                elif request == REQUEST_CHECK:
                    # arguments must be a typing.Sequence of str.
                    answer_line_end.put(self.HasData(*arguments))
                elif request == REQUEST_STATUS:
                    answer_line_end.put(self.status)
                elif request == REQUEST_CLOSE:
                    active_lines.remove(
                        line_t(request=request_line_end, answer=answer_line_end)
                    )
                elif request == REQUEST_STOP:
                    active_lines.clear()
                    break
                else:
                    raise ValueError(
                        f'Unknown request "{request}" sent to '
                        f'data server "{self.name}".'
                    )

    def HasData(self, *names) -> h.Any:
        """"""
        if (n_names := names.__len__()) == 0:
            return self.data.__len__() > 0

        if n_names == 1:
            return names[0] in self.data

        return tuple(_ in self.data for _ in names)

    def RequestedData(self, *names) -> h.Any:
        """
        If called indirectly (as a result of a request from a subprocess), returned data
        must be jsoned.
        """
        if (n_names := names.__len__()) == 0:
            return self.data

        if n_names == 1:
            return self.data[names[0]]

        return tuple(self.data[_] for _ in names)

    def StoreData(self, **data) -> None:
        """
        If called indirectly (as a result of a request from a subprocess), data in
        arguments have been jsoned.
        """
        if self.is_read_only:
            raise RuntimeError(
                f'Attempt to modify read-only data server "{self.name}".'
            )

        for name, value in data.items():
            if isinstance(value, array_t) and (self._shared_array_memory is not None):
                if name in self._shared_array_memory:
                    DisposeOriginalSharedArray(self._shared_array_memory[name])
                _, sharing_name, shared_memory = NewSharedArray(value)
                self.data[name] = sharing_name
                self._shared_array_memory[name] = shared_memory
            else:
                self.data[name] = value

    def DeleteData(self, *names) -> None:
        """"""
        if names.__len__() == 0:
            names = tuple(self.data.keys())

        for name in names:
            if (self._shared_array_memory is not None) and (
                name in self._shared_array_memory
            ):
                DisposeOriginalSharedArray(self._shared_array_memory[name])
                del self._shared_array_memory[name]
            del self.data[name]

    def Stop(self) -> None:
        """
        Can also be used to clear the resources of an un-started server.
        """
        assert CurrentProcess().name == MAIN_PROCESS_NAME

        if self._lines.__len__() > 0:
            if self._thread is not None:
                self._lines[0].request.put(REQUEST_STOP)
                while self._thread.is_alive():
                    pass
            for line_ends in self._lines:
                for line_end in line_ends:
                    line_end.close()
                    line_end.join_thread()
            self._lines.clear()

        if self._shared_array_memory is not None:
            for shared_memory in self._shared_array_memory.values():
                DisposeOriginalSharedArray(shared_memory)
            self._shared_array_memory.clear()

        if self._thread is not None:
            self._thread.join()
            self._thread = None


def DataFromServer(
    request_line_end: line_end_t | None,
    answer_line_end: line_end_t | None,
    /,
    *names,
    server: server_t | None = None,
) -> h.Any:
    """"""
    if server is None:
        if names.__len__() == 0:
            request = REQUEST_GET
        else:
            request = (REQUEST_GET, *names)
        request_line_end.put(request)

        jsoned = answer_line_end.get()
        un_jsoned, issues = json.ObjectFromJsonString(jsoned)
        if issues is None:
            return un_jsoned
        else:
            raise RuntimeError(
                f"Un-de-jsonable object:\n{jsoned}\n" + "\n".join(issues)
            )

    return server.RequestedData(*names)


def SendDataToServer(
    request_line_end: line_end_t | None,
    answer_line_end: line_end_t | None,
    /,
    *,
    server: server_t | None = None,
    **data,
) -> None:
    """"""
    if server is None:
        jsoned, issues = json.JsonStringOf(data)
        if issues is None:
            request_line_end.put((REQUEST_SET, jsoned))
        else:
            raise RuntimeError(f"Un-jsonable object:\n{data}\n" + "\n".join(issues))
        # Wait for setting confirmation for synchronization purposes. Thus, it will not
        # be possible to set again the same element before the current storage is
        # effective.
        acknowledgment = answer_line_end.get()
        if acknowledgment != STORAGE_DONE:
            raise RuntimeError(
                f"Unexpected storage acknowledgment received: {acknowledgment}"
            )
    else:
        server.StoreData(**data)


def DeleteDataFromServer(
    request_line_end: line_end_t | None,
    answer_line_end: line_end_t | None,
    /,
    *names,
    server: server_t | None = None,
) -> None:
    """"""
    if server is None:
        request_line_end.put((REQUEST_DELETE, *names))
        # Wait for deletion confirmation for synchronization purposes. Thus, the server
        # will not confirm the presence of in-the-course-of-deletion data.
        acknowledgment = answer_line_end.get()
        if acknowledgment != DELETION_DONE:
            raise RuntimeError(
                f"Unexpected deletion acknowledgment received: {acknowledgment}"
            )
    else:
        server.DeleteData(*names)


def ServerHasData(
    request_line_end: line_end_t | None,
    answer_line_end: line_end_t | None,
    /,
    *names,
    server: server_t | None = None,
) -> h.Any:
    """"""
    if server is None:
        if names.__len__() == 0:
            request = REQUEST_CHECK
        else:
            request = (REQUEST_CHECK, *names)
        request_line_end.put(request)

        return answer_line_end.get()

    return server.HasData(*names)


def StatusOfServer(
    request_line_end: line_end_t | None,
    answer_line_end: line_end_t | None,
    /,
    *,
    server: server_t | None = None,
) -> server_status_h:
    """"""
    if server is None:
        request_line_end.put(REQUEST_STATUS)
        return answer_line_end.get()

    return server.status


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
