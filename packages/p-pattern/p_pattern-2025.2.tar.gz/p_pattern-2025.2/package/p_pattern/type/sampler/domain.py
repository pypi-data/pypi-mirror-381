"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import typing as h

import numpy as nmpy
from p_pattern.extension.type import number_h

interval_h = tuple[number_h, number_h]  # Closed interval.
precision_h = number_h | None  # None=infinite.

interval_with_precision_h = tuple[number_h, number_h, precision_h]
domain_precisions_h = precision_h | tuple[precision_h, ...]

domain_h = tuple[interval_h, ...]
domain_indexer_h = tuple[slice, ...]
chunked_domain_h = tuple[domain_h, tuple[interval_h, ...], domain_h]

array_t = nmpy.ndarray


class educated_domain_t(h.NamedTuple):
    """
    Everything but restriction and effective is relative to the full domain.
    Restriction is a potential restriction of the full domain.
    Effective is the restriction if there is one, else the full domain.
    """

    dimension: int
    bounds: domain_h
    lengths: tuple[int, ...]
    precisions: domain_precisions_h | None
    sites: tuple[array_t, ...]
    sites_flat: tuple[array_t, ...]

    restriction: domain_h | None
    effective: domain_h

    @classmethod
    def New(
        cls,
        definition: domain_h | array_t,
        /,
        *,
        restriction: domain_h | None = None,
        precision: int | float | tuple[int | float, ...] | None = None,
        expected_dimension: int | None = None,
    ) -> h.Self:
        """"""
        if isinstance(definition, array_t):
            lengths = definition.shape
            if expected_dimension is not None:
                # Why limiting to the first dimension components? To fit 2-D patterns on
                # 2-D, color images for example.
                lengths = lengths[:expected_dimension]
            definition = tuple((0, _ - 1) for _ in lengths)
            precision = None
        else:
            lengths = tuple(_[1] + 1 for _ in definition)
            if precision is None:
                pass
            elif isinstance(precision, number_h):
                precision = expected_dimension * (float(precision),)
            else:
                precision = tuple(None if _ is None else float(_) for _ in precision)

            assert (expected_dimension is None) or (
                definition.__len__() == expected_dimension
            ), (definition.__len__(), expected_dimension)

        sites = tuple(nmpy.indices(lengths))
        sites_flat = tuple(_.flatten() for _ in sites)

        if restriction is None:
            effective = definition
        else:
            effective = restriction

        return cls(
            dimension=definition.__len__(),
            bounds=definition,
            lengths=lengths,
            precisions=precision,
            sites=sites,
            sites_flat=sites_flat,
            restriction=restriction,
            effective=effective,
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
