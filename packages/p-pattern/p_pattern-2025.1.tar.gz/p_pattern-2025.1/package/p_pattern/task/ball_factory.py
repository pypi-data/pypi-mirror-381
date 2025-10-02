"""
Copyright CNRS (https://www.cnrs.fr/index.php/en)
Contributor(s): Eric Debreuve (eric.debreuve@cnrs.fr) since 2025
SEE COPYRIGHT NOTICE BELOW
"""

import numpy as nmpy
import scipy.ndimage as spim
import skimage.morphology as mrph

array_t = nmpy.ndarray


# TODO: Remove global variable... or not.
per_dim_and_radius: dict[int, dict[int, array_t]] = {}


def OfDimensionAndRadius(dimension: int, radius: int, /) -> array_t:
    """"""
    global per_dim_and_radius

    if dimension not in per_dim_and_radius:
        per_dim_and_radius[dimension] = {}

    per_radius = per_dim_and_radius[dimension]

    if radius not in per_radius:
        if dimension == 1:
            ball = nmpy.full(2 * radius + 1, True, dtype=nmpy.bool_)
        elif dimension == 2:
            ball = mrph.disk(radius, dtype=nmpy.bool_)
        elif dimension == 3:
            ball = mrph.ball(radius, dtype=nmpy.bool_)
        else:
            chart = nmpy.ones(dimension * (2 * radius + 1,), dtype=nmpy.float64)
            center = dimension * (radius,)
            chart[(*center,)] = 0.0
            distances = spim.distance_transform_edt(chart)
            ball = distances <= radius
        per_radius[radius] = ball

    return per_radius[radius]


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
