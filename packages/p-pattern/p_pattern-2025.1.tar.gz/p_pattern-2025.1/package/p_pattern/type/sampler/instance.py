"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import dataclasses as d
import typing as h

import numpy as nmpy
from p_pattern.extension.type import number_h
from p_pattern.type.instance.parameter.position import position_h
from p_pattern.type.model.generic import model_t
from p_pattern.type.model.parameter import parameter_h
from p_pattern.type.sampler.domain import domain_h
from p_pattern.type.sampler.number import (
    new_samples_integer_h,
    new_samples_real_h,
    number_sampler_t,
)
from p_pattern.type.sampler.position import position_sampler_t
from p_pattern.type.sampler.shape import shape_sampler_t

array_t = nmpy.ndarray


@d.dataclass(slots=True, repr=False, eq=False)
class sampler_t:
    """
    domain: domain_h, domain_with_precisions_h, or array_t at instantiation time, and
    educated_domain_t after initialization.
    """

    model: model_t
    seed: int | None = None

    domain: d.InitVar[domain_h | array_t] = ()
    restriction: d.InitVar[domain_h | None] = None
    precision: d.InitVar[int | float | tuple[int | float, ...] | None] = None

    number: number_sampler_t = d.field(init=False)
    IntegerSamples: new_samples_integer_h = d.field(init=False)
    RealSamples: new_samples_real_h = d.field(init=False)
    position: position_sampler_t = d.field(init=False)
    shape: dict[str, shape_sampler_t] = d.field(init=False, default_factory=dict)

    def __post_init__(
        self,
        domain: domain_h | array_t,
        restriction: domain_h | None,
        precision: int | float | tuple[int | float, ...] | None,
    ) -> None:
        """"""
        if self.seed is None:
            self.number = nmpy.random.default_rng()
        else:
            self.number = nmpy.random.default_rng(seed=self.seed)
        self.IntegerSamples = self.number.integers
        self.RealSamples = self.number.uniform

        self.position = position_sampler_t.New(
            domain, restriction, precision, self.model.dimension
        )
        if self.position is None:
            return

        for name, parameter in self.model.items():
            self.shape[name] = shape_sampler_t.New(
                parameter.interval[0],
                parameter.interval[1],
                parameter.type,
                self.number,
            )

    def NewRawSamples(
        self, n_samples: int, /
    ) -> h.Iterator[tuple[position_h, tuple[number_h, ...]]]:
        """"""
        if self.position is None:
            return

        positions = self.position.Samples(
            n_samples, IntegerSamples=self.IntegerSamples, RealSamples=self.RealSamples
        )
        shapes = (_.Samples(n_samples) for _ in self.shape.values())

        dimension = self.model.dimension
        for sample in zip(*positions, *shapes, strict=True):
            yield sample[:dimension], sample[dimension:]

    def NewRawSimilarSamples(
        self,
        position: position_h,
        shape: tuple[parameter_h, ...],
        radius: float,
        n_similar: int,
        /,
        *,
        fraction: float = 0.1,
    ) -> h.Iterator[tuple[position_h, tuple[number_h, ...]]]:
        """"""
        positions = self.position.NewSimilarSamples(
            position, radius, n_similar, self.RealSamples
        )
        shapes = (
            __.NewSimilarSamples(_, fraction, n_similar)
            for _, __ in zip(shape, self.shape.values(), strict=True)
        )

        dimension = self.model.dimension
        for sample in zip(*positions, *shapes, strict=True):
            yield sample[:dimension], sample[dimension:]


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
