"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import dataclasses as d
import math
import typing as h

import numpy as nmpy
from p_pattern.type.model.parameter import (
    parameter_h,
    parameter_interval_h,
    parameter_precision_h,
)

array_t = nmpy.ndarray
number_sampler_t = nmpy.random.Generator


@d.dataclass(slots=True, repr=False, eq=False)
class shape_sampler_t:
    Samples: h.Callable[[int], array_t]
    NewSimilarSamples: h.Callable[[parameter_h, float, int], array_t]

    @classmethod
    def New(
        cls,
        interval: parameter_interval_h,
        precision: parameter_precision_h,
        stripe: type[parameter_h],
        sampler: number_sampler_t,
        /,
    ) -> h.Self:
        """"""
        first, last = interval
        IntegerSamples = sampler.integers
        RealSamples = sampler.uniform

        if precision is None:
            if stripe is int:
                Samples = lambda _arg: IntegerSamples(first, high=last + 1, size=_arg)
            else:
                Samples = lambda _arg: RealSamples(low=first, high=last, size=_arg)
        else:
            if stripe is int:
                maximum = (last - first) // precision
            else:
                maximum = int((last - first) / precision)
            Samples = (
                lambda _arg: precision * IntegerSamples(0, high=maximum + 1, size=_arg)
                + first
            )

        NewSimilarSamples = lambda _ref, _frt, _nbr: _SimilarSamples(
            _ref, stripe, interval, _frt, _nbr, IntegerSamples, RealSamples
        )

        return cls(Samples=Samples, NewSimilarSamples=NewSimilarSamples)


def _SimilarSamples(
    reference: parameter_h,
    stripe: type[parameter_h],
    interval: parameter_interval_h,
    fraction: float,
    n_samples: int,
    IntegerSamples,
    RealSamples,
    /,
) -> array_t:
    """
    Note that the (optional) precision is ignored.
    """
    first = max(reference * (1.0 - fraction), interval[0])
    last = min(reference * (1.0 + fraction), interval[1])

    if stripe is int:
        return IntegerSamples(
            math.floor(first), high=math.ceil(last) + 1, size=n_samples
        )
    else:
        if last < interval[1]:
            last = math.nextafter(last, last + 1.0)
        return RealSamples(low=first, high=last, size=n_samples)


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
