"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import typing as h

from p_pattern.type.sampler.domain import domain_indexer_h


class bbox_t:
    """
    domain: To be used in numpy array indexing.
    """

    __slots__ = ("min_s", "max_s", "domain", "_lengths")

    min_s: tuple[int, ...]
    max_s: tuple[int, ...]
    domain: domain_indexer_h
    _lengths: tuple[int, ...] | None

    def __init__(self, min_s: h.Sequence[int], max_s: h.Sequence[int], /) -> None:
        """"""
        self.min_s = tuple(min_s)
        self.max_s = tuple(max_s)
        self.domain = tuple(
            slice(_, __ + 1) for _, __ in zip(self.min_s, self.max_s, strict=True)
        )
        self._lengths = None

    @property
    def lengths(self) -> tuple[int, ...]:
        """"""
        if self._lengths is None:
            self._lengths = tuple(_.stop - _.start for _ in self.domain)
        return self._lengths

    def SlicesOfDilated(
        self, dilation: int, domain_lengths: tuple[int, ...], /
    ) -> domain_indexer_h:
        """
        dilation: Can be negative.
        """
        dilated_min_s = (max(0, _min - dilation) for _min in self.min_s)
        dilated_max_s = (
            min(_lgt - 1, _max + dilation)
            for _max, _lgt in zip(self.max_s, domain_lengths, strict=True)
        )

        return tuple(
            slice(_, __ + 1) for _, __ in zip(dilated_min_s, dilated_max_s, strict=True)
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
