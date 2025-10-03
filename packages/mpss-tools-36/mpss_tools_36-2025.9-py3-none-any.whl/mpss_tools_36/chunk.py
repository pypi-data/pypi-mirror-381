"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

from math import ceil


def ChunksForRange(
    *,
    start: int = 0,
    end: int | None = None,
    end_p_1: int | None = None,
    n_elements: int | None = None,
    n_chunks: int | None = None,
    chunk_size: int | None = None,
    return_bounds_only: bool = True,
    bound_end_should_be_p_1: bool = True,
) -> tuple[tuple[int, int], ...] | tuple[tuple[int, ...], ...]:
    """
    Integer range to split into chunks defined by: start and (end or end_p_1 or
    n_elements).
    Way to split range defined by: n_chunks, chunk_size.
    Format of returned chunks defined by: return_bounds_only, bound_end_should_be_p_1.
    """
    if n_elements is not None:
        end_p_1 = start + n_elements
    elif end_p_1 is not None:
        n_elements = end_p_1 - start
    elif end is not None:
        end_p_1 = end + 1
        n_elements = end_p_1 - start
    else:
        raise ValueError(
            'One argument must not be None among "n_elements", "end_p_1", and "end".'
        )

    if n_chunks is not None:
        assert n_chunks <= n_elements
        chunk_size = int(ceil(n_elements / n_chunks))
        # should_even_chunks = True
    else:
        assert (chunk_size is not None) and (chunk_size <= n_elements)
        # should_even_chunks = False

    if return_bounds_only and not bound_end_should_be_p_1:
        end_offset = -1
    else:
        end_offset = 0
    bounds = tuple(
        (_, min(_ + chunk_size, end_p_1) + end_offset)
        for _ in range(start, end_p_1, chunk_size)
    )

    if return_bounds_only:
        return bounds

    return tuple(tuple(range(_stt, _end)) for _stt, _end in bounds)


def DescriptionsForChunks(
    description: str, chunk_bounds: tuple[tuple[int, int], ...], /
) -> tuple[str, ...]:
    """
    description: Base description to be completed with chunk details.
    """
    highest_start, highest_end_p_1 = chunk_bounds[-1]
    width_start = str(highest_start).__len__()
    width_end = str(highest_end_p_1 - 1).__len__()

    return tuple(
        f"{description}[{_stt:{width_start}}..{_ep1 - 1:{width_end}}]#{_ep1 - _stt}"
        for _stt, _ep1 in chunk_bounds
    )


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
