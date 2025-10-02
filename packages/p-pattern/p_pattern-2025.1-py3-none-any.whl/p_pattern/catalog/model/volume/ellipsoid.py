"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import dataclasses as d

from p_pattern.constant.shape import (
    DEFAULT_RADII_RATIO_ANY_DEFINITION,
    DEFAULT_RADII_RATIO_LARGER_DEFINITION,
    DEFAULT_RADIUS_DEFINITION,
)
from p_pattern.type.model.parameter import parameter_t
from p_pattern.type.model.volume import model_t as _base_t


@d.dataclass(slots=True, repr=False, eq=False)
class ellipsoid_t(_base_t):
    def __post_init__(self) -> None:
        """"""
        _base_t.__post_init__(self)
        self.update(
            {
                "semi_minor_axis": DEFAULT_RADIUS_DEFINITION,
                "major_minor_ratio": DEFAULT_RADII_RATIO_LARGER_DEFINITION,
                "third_minor_ratio": DEFAULT_RADII_RATIO_ANY_DEFINITION,
                "rc_angle": parameter_t.NewAngle(1.0),  # Rotation in RowxCol-plane.
                "rd_angle": parameter_t.NewAngle(2.0),  # Rotation in RowxDep-plane.
            }
        )

    @staticmethod
    def ShapeHeader() -> tuple[str, ...]:
        """"""
        return (
            "Semi Minor Axis",
            "Semi Major Axis",
            "Semi Third Axis",
            "Angle (radian)",
            "Second Angle (radian)",
        )

    @classmethod
    def EducatedShapeHeader(cls) -> tuple[str, ...]:
        """"""
        return cls.ShapeHeader()[:3] + (
            "Angle (radian)",
            "Angle (degree)",
            "Second Angle (radian)",
            "Second Angle (degree)",
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
