"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import dataclasses as d
import math
import typing as h

from logger_36 import L
from p_pattern.extension.type import integer_h, real_h
from p_pattern.type.model.parameter import (
    parameter_h,
    parameter_interval_h,
    parameter_precision_h,
    parameter_t,
)


@d.dataclass(slots=True, repr=False, eq=False)
class model_t(dict[str, parameter_t]):
    """
    Position parameters are not stored in the model.
    """

    dimension: int = d.field(init=False)  # Set by subclasses.

    def ShapeIntervalsAreValid(self, intervals: dict[str, h.Any], /) -> bool:
        """
        Position does not need to be checked since there are no a priori constraints on
        it. It will simply be set for sampling.
        """
        valid_names = tuple(self.keys())
        issues = []
        for name, interval in intervals.items():
            if name not in valid_names:
                issues.append(
                    (
                        "Invalid mark range",
                        {
                            "actual": name,
                            "expected": valid_names,
                            "expected_is_choices": True,
                        },
                    )
                )
                continue

            definition = self[name]

            if issubclass(definition.type, integer_h):
                valid_types = int
            elif issubclass(definition.type, real_h):
                valid_types = (int, float)
            else:
                valid_types = definition.type
            if (
                (not isinstance(interval, tuple))
                or ((interval.__len__() != 2) and (interval.__len__() != 3))
                or (not all(isinstance(_elm, valid_types) for _elm in interval))
            ):
                issues.append(
                    (
                        f'Invalid range for mark "{name}"',
                        {
                            "actual": interval,
                            "expected": "2- or 3-tuple of integers/floats",
                        },
                    )
                )
                continue

            if not isinstance(definition.type, integer_h | real_h):
                continue

            if (interval.__len__() == 3) and (interval[2] < 0):
                issues.append(
                    (
                        "Invalid precision",
                        {
                            "actual": interval[2],
                            "expected": "Value positive or equal to zero",
                        },
                    )
                )

            if interval[0] > interval[1]:
                issues.append(
                    f"From_{interval[0]} !>! to_{interval[1]} for mark '{name}'"
                )
                continue

            if interval[0] < definition.min:
                issues.append(
                    f"Range start out-of-bound ({interval[0]} < {definition.min}; "
                    f"expected: >=) for mark '{name}'"
                )
            elif (
                (definition.type is int)
                and (interval[0] == definition.min)
                and not definition.min_inclusive
            ):
                issues.append(
                    f"Range start out-of-bound ({interval[0]} <= {definition.min}; "
                    f"expected: >) for mark '{name}'"
                )

            if interval[1] > definition.max:
                issues.append(
                    f"Range end out-of-bound ({interval[1]} > {definition.min}; "
                    f"expected: <=) for mark '{name}'"
                )
            elif (
                (definition.type is int)
                and (interval[1] == definition.max)
                and not definition.max_inclusive
            ):
                issues.append(
                    f"Range end out-of-bound ({interval[1]} >= {definition.min}; "
                    f"expected: <) for mark '{name}'"
                )

        for issue in issues:
            if isinstance(issue, str):
                L.StageIssue(issue)
            else:
                L.StageIssue(issue[0], **(issue[1]))

        return issues.__len__() == 0

    def SetShapeIntervals(
        self,
        intervals: dict[
            str,
            parameter_interval_h
            | tuple[parameter_h, parameter_h, parameter_precision_h],
        ],
        /,
    ) -> None:
        """"""
        for name, parameter in self.items():
            if (actual := intervals.get(name)) is None:
                default_interval = parameter.default_interval
                precision = parameter.default_precision
                if default_interval is None:
                    # TODO: Remove error checking here. Everything should be tested in
                    #     ShapeIntervalsAreValid.
                    L.StageIssue(f"{name}: Missing required range.")
                    continue
                else:
                    first, last = default_interval
            else:
                first, last, *precision = actual
                if precision.__len__() > 0:
                    precision = precision[0]
                else:
                    precision = parameter.default_precision

            first_original = first
            last_original = last
            stripe = parameter.type

            if precision is not None:
                if precision == 0:
                    precision = None
                else:
                    if stripe is int:
                        precision = int(precision)
                    else:
                        precision = float(precision)
                    first = precision * math.ceil(first / precision)
                    last = precision * math.floor(last / precision)
                    if last < first:
                        precision = None
                        # TODO: Remove error checking here. Everything should be tested
                        #     in ShapeIntervalsAreValid.
                        L.StageIssue(
                            f"{name}: Invalid interval/precision combination "
                            f"leading to empty range."
                        )

            if stripe is float:
                # Adaptation of interval to numpy.uniform generating samples in [a,b[.
                if (first == first_original) and not parameter.min_inclusive:
                    first = math.nextafter(first, first + 1.0)
                if (last < last_original) or parameter.max_inclusive:
                    last = math.nextafter(last, last + 1.0)

            self[name].interval = ((first, last), precision)

    def DescriptionHeader(
        self, /, *, educated_version: bool = False
    ) -> tuple[str, ...]:
        """"""
        if educated_version:
            shape_parameters = self.EducatedShapeHeader()
        else:
            shape_parameters = self.ShapeHeader()

        return "Type", *self.PositionHeader(), *shape_parameters

    @staticmethod
    def PositionHeader() -> tuple[str, ...]:
        """"""
        raise NotImplementedError

    @staticmethod
    def ShapeHeader() -> tuple[str, ...]:
        """"""
        raise NotImplementedError

    @staticmethod
    def EducatedShapeHeader() -> tuple[str, ...]:
        """"""
        raise NotImplementedError


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
