# ================================== LICENSE ===================================
# Wulfric - Cell, Atoms, K-path, visualization.
# Copyright (C) 2023-2025 Andrey Rybakov
#
# e-mail: anry@uv.es, web: adrybakov.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ================================ END LICENSE =================================
from math import cos, pi, sin

import numpy as np
import pytest
from hypothesis import example, given
from hypothesis import strategies as st
from hypothesis.extra.numpy import arrays as harrays

from wulfric._numerical import compare_with_tolerance
from wulfric.constants._numerical import TORADIANS
from wulfric.geometry._geometry import (
    get_angle,
    get_spherical,
    get_volume,
    parallelepiped_check,
)

ANGLE_TOLERANCE = 1e-4
LENGTH_TOLERANCE = 1e-8
MIN_LENGTH = 0.0
MAX_LENGTH = 1e7


################################################################################
#                                     Angle                                    #
################################################################################
@given(
    harrays(float, 3, elements=st.floats(allow_infinity=False, allow_nan=False)),
    harrays(float, 3, elements=st.floats(allow_infinity=False, allow_nan=False)),
)
def test_get_angle(v1, v2):
    if (
        abs(np.linalg.norm(v1)) > np.finfo(float).eps
        and abs(np.linalg.norm(v2)) > np.finfo(float).eps
    ):
        result_degrees = get_angle(v1, v2)
        result_radians = get_angle(v1, v2, radians=True)
        assert 0.0 <= result_degrees <= 180.0
        assert 0.0 <= result_radians <= pi
    else:
        with pytest.raises(ValueError):
            result_degrees = get_angle(v1, v2)


@example(0)
@example(0.0000000001)
@given(st.floats(min_value=-360, max_value=360))
def test_get_angle_values(alpha):
    v1 = np.array([1.0, 0.0, 0.0])
    v2 = np.array([cos(alpha * TORADIANS), sin(alpha * TORADIANS), 0.0])

    if alpha < 0:
        alpha = 360 + alpha

    if alpha > 180:
        alpha = 360 - alpha

    assert abs(get_angle(v1, v2) - alpha) < ANGLE_TOLERANCE


def test_get_angle_raises():
    with pytest.raises(ValueError):
        get_angle([0, 0, 0], [0, 0, 0])
    with pytest.raises(ValueError):
        get_angle([0, 0, 0], [1.0, 0, 0])


################################################################################
#                                    Volume                                    #
################################################################################
@pytest.mark.parametrize(
    "args, result, eps",
    [((4, 4.472, 4.583, 79.03, 64.13, 64.15), 66.3840797, LENGTH_TOLERANCE)],
)
def test_get_volume_example(args, result, eps):
    assert get_volume(*args) - result < eps


# No need to test the vectors - they take the same route as the cell
# if the vectors will move from rows to columns it is not a problem as well
# since the volume of the cell is its determinant
@example(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
@example(np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]]))
@given(
    harrays(
        float, (3, 3), elements=st.floats(min_value=MIN_LENGTH, max_value=MAX_LENGTH)
    )
)
def test_get_volume_with_cell(cell):
    assert get_volume(cell) >= 0


@given(
    st.floats(
        min_value=MIN_LENGTH,
        max_value=MAX_LENGTH,
    ),
    st.floats(
        min_value=MIN_LENGTH,
        max_value=MAX_LENGTH,
    ),
    st.floats(
        min_value=MIN_LENGTH,
        max_value=MAX_LENGTH,
    ),
    st.floats(min_value=0, max_value=360),
    st.floats(min_value=0, max_value=360),
    st.floats(min_value=0, max_value=360),
)
def test_get_volume_parameters(a, b, c, alpha, beta, gamma):
    if parallelepiped_check(a, b, c, alpha, beta, gamma):
        assert get_volume(a, b, c, alpha, beta, gamma) > 0


################################################################################
#                             Parallelepiped check                             #
################################################################################
@given(
    st.floats(min_value=MIN_LENGTH, max_value=MAX_LENGTH),
    st.floats(min_value=MIN_LENGTH, max_value=MAX_LENGTH),
    st.floats(min_value=MIN_LENGTH, max_value=MAX_LENGTH),
    st.floats(min_value=0, max_value=360),
    st.floats(min_value=0, max_value=360),
    st.floats(min_value=0, max_value=360),
)
def test_parallelepiped_check(a, b, c, alpha, beta, gamma):
    assert parallelepiped_check(a, b, c, alpha, beta, gamma) == (
        compare_with_tolerance(a, ">", 0.0, eps=LENGTH_TOLERANCE)
        and compare_with_tolerance(b, ">", 0.0, eps=LENGTH_TOLERANCE)
        and compare_with_tolerance(c, ">", 0.0, eps=LENGTH_TOLERANCE)
        and compare_with_tolerance(alpha, "<", 180.0, eps=ANGLE_TOLERANCE)
        and compare_with_tolerance(beta, "<", 180.0, eps=ANGLE_TOLERANCE)
        and compare_with_tolerance(gamma, "<", 180.0, eps=ANGLE_TOLERANCE)
        and compare_with_tolerance(alpha, ">", 0.0, eps=ANGLE_TOLERANCE)
        and compare_with_tolerance(beta, ">", 0.0, eps=ANGLE_TOLERANCE)
        and compare_with_tolerance(gamma, ">", 0.0, eps=ANGLE_TOLERANCE)
        and compare_with_tolerance(gamma, "<", alpha + beta, eps=ANGLE_TOLERANCE)
        and compare_with_tolerance(
            alpha + beta, "<", 360.0 - gamma, eps=ANGLE_TOLERANCE
        )
        and compare_with_tolerance(beta, "<", alpha + gamma, eps=ANGLE_TOLERANCE)
        and compare_with_tolerance(
            alpha + gamma, "<", 360.0 - beta, eps=ANGLE_TOLERANCE
        )
        and compare_with_tolerance(alpha, "<", beta + gamma, eps=ANGLE_TOLERANCE)
        and compare_with_tolerance(
            beta + gamma, "<", 360.0 - alpha, eps=ANGLE_TOLERANCE
        )
    )


################################################################################
#                             Spherical coordinates                            #
################################################################################
@given(
    st.floats(min_value=MIN_LENGTH + LENGTH_TOLERANCE, max_value=MAX_LENGTH),
    st.floats(min_value=0.1, max_value=180 - 0.1),
    st.floats(min_value=0.1, max_value=360),
)
def test_get_spherical(r, theta, phi):
    vector = r * np.array(
        [
            np.cos(phi * TORADIANS) * np.sin(theta * TORADIANS),
            np.sin(phi * TORADIANS) * np.sin(theta * TORADIANS),
            np.cos(theta * TORADIANS),
        ]
    )

    c_r, c_theta, c_phi = get_spherical(vector, in_degrees=True)

    assert compare_with_tolerance(theta, "==", c_theta, eps=ANGLE_TOLERANCE)
    assert compare_with_tolerance(phi, "==", c_phi, eps=ANGLE_TOLERANCE)
    assert compare_with_tolerance(r, "==", c_r, eps=LENGTH_TOLERANCE)
