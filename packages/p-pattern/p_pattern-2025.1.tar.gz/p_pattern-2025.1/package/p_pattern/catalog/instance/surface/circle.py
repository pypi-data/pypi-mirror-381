"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import math
from ctypes import c_double, c_size_t, c_void_p

import numpy as nmpy
from p_pattern.catalog.instance.c_extension import RegionImplementationInC
from p_pattern.catalog.instance.surface.superquadric import Region
from p_pattern.type.instance.surface import instance_t as _base_t
from p_pattern.type.model.parameter import parameter_h

array_t = nmpy.ndarray


_Region_C = RegionImplementationInC(
    __file__, (c_void_p, c_void_p, c_size_t, c_double, c_double, c_double, c_void_p)
)


class circle_t(_base_t):
    @property
    def educated_shape(self) -> tuple[parameter_h, ...]:
        """"""
        return (self.shape[0],)

    def _CoarseBoundingBoxHalfLengths(self) -> tuple[int, ...]:
        """"""
        radius = math.ceil(self.shape[0]).__int__()

        return radius, radius

    def _Region(self, grid_sites: tuple[array_t, ...], /) -> array_t:
        """"""
        return Region(
            self.shape[0],
            None,
            None,
            None,
            None,
            self.position,
            self.bbox.domain,
            _Region_C,
            grid_sites,
        )

    def Normals(self) -> tuple[tuple[array_t, ...] | None, array_t | None]:
        """"""
        cache_entry = self.Normals.__name__

        if cache_entry not in self._cache:
            contour = self.Contour()
            sites = contour.nonzero()

            if sites[0].size > 0:
                normals = nmpy.transpose(sites).astype(nmpy.float64) + [
                    [
                        self.bbox.min_s[0] - self.position[0],
                        self.bbox.min_s[1] - self.position[1],
                    ]
                ]
                normal_norms = nmpy.sqrt((normals**2).sum(axis=1, keepdims=True))
                # When the analytical normal expression is evaluated at (0,0), it
                # results in a null normal. This occurs whenever the contour "passes
                # through the center" (very thick contour and/or very thin object).
                normal_norms[normal_norms == 0.0] = 1.0
                normals /= normal_norms
            else:
                sites = normals = None

            self._cache[cache_entry] = (sites, normals)

        return self._cache[cache_entry]

    def _RadiusForSimilarPositions(self, /, *, fraction: float = 0.1) -> float:
        """"""
        return 0.5 * fraction * self.shape[0] * (1.0 + 1.0)

    def FormattedShape(self) -> str:
        """"""
        return f"{self.shape[0]:.2f}"


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
