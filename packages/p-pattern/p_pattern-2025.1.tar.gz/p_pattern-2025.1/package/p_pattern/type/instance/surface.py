"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import typing as h

import numpy as nmpy
from p_pattern.type.instance.generic import instance_t as _base_t

array_t = nmpy.ndarray


class instance_t(_base_t):
    def Intersects(self, other: h.Self, max_overlap: float, /) -> bool:
        """"""
        bbox_1 = self.bbox
        bbox_2 = other.bbox
        if (
            (bbox_1.min_s[0] > bbox_2.max_s[0])
            or (bbox_2.min_s[0] > bbox_1.max_s[0])
            or (bbox_1.min_s[1] > bbox_2.max_s[1])
            or (bbox_2.min_s[1] > bbox_1.max_s[1])
        ):
            return False

        region_1 = self.region
        region_2 = other.region
        area_2 = other.area

        inter_min_row = max(bbox_1.min_s[0], bbox_2.min_s[0])
        inter_max_row = min(bbox_1.max_s[0], bbox_2.max_s[0])
        inter_min_col = max(bbox_1.min_s[1], bbox_2.min_s[1])
        inter_max_col = min(bbox_1.max_s[1], bbox_2.max_s[1])

        region_1_min_row = max(inter_min_row - bbox_1.min_s[0], 0)
        region_1_max_row = min(inter_max_row - bbox_1.min_s[0] + 1, region_1.shape[0])
        region_1_min_col = max(inter_min_col - bbox_1.min_s[1], 0)
        region_1_max_col = min(inter_max_col - bbox_1.min_s[1] + 1, region_1.shape[1])

        region_2_min_row = max(inter_min_row - bbox_2.min_s[0], 0)
        region_2_max_row = min(inter_max_row - bbox_2.min_s[0] + 1, region_2.shape[0])
        region_2_min_col = max(inter_min_col - bbox_2.min_s[1], 0)
        region_2_max_col = min(inter_max_col - bbox_2.min_s[1] + 1, region_2.shape[1])

        domain_1 = (
            slice(region_1_min_row, region_1_max_row),
            slice(region_1_min_col, region_1_max_col),
        )
        domain_2 = (
            slice(region_2_min_row, region_2_max_row),
            slice(region_2_min_col, region_2_max_col),
        )

        return self._RegionIntersects(domain_1, region_2, domain_2, area_2, max_overlap)

    def Tangents(self) -> tuple[tuple[array_t, ...] | None, array_t | None]:
        """
        Not really "implemented" since it relies on the not-implemented Normals method.
        """
        cache_entry = self.Tangents.__name__

        if cache_entry not in self._cache:
            sites, normals = self.Normals()
            if sites is None:
                tangents = None
            else:
                tangents = nmpy.empty_like(normals)
                tangents[:, 0] = -normals[:, 1]
                tangents[:, 1] = normals[:, 0]

            self._cache[cache_entry] = (sites, tangents)

        return self._cache[cache_entry]


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
