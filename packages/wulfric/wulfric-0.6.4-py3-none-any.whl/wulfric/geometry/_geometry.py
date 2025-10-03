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
from math import cos, sqrt

import numpy as np

from wulfric._numerical import compare_with_tolerance
from wulfric.constants._numerical import TODEGREES, TORADIANS

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


def get_volume(*args):
    r"""
    Computes volume.

    Three types of arguments are expected:

    * One argument.
        Matrix ``cell``.
        Volume is computed as:

        .. math::
            V = \boldsymbol{v_1} \cdot (\boldsymbol{v_2} \times \boldsymbol{v_3})
    * Three arguments.
        Vectors ``v1``, ``v2``, ``v3``.
        Volume is computed as:

        .. math::
            V = \boldsymbol{v_1} \cdot (\boldsymbol{v_2} \times \boldsymbol{v_3})
    * Six arguments.
        Parameters ``a``, ``b``, ``c``, ``alpha``, ``beta``, ``gamma``.
        Volume is computed as:

        .. math::
            V = abc\sqrt{1+2\cos(\alpha)\cos(\beta)\cos(\gamma)-\cos^2(\alpha)-\cos^2(\beta)-\cos^2(\gamma)}


    Parameters
    ----------
    v1 : (3,) |array-like|_
        First vector.
    v2 : (3,) |array-like|_
        Second vector.
    v3 : (3,) |array-like|_
        Third vector.
    cell : (3, 3) |array-like|_
        Matrix of a cell, rows are interpreted as vectors.
    a : float, default 1
        Length of the :math:`v_1` vector.
    b : float, default 1
        Length of the :math:`v_2` vector.
    c : float, default 1
        Length of the :math:`v_3` vector.
    alpha : float, default 90
        Angle between vectors :math:`v_2` and :math:`v_3`. In degrees.
    beta : float, default 90
        Angle between vectors :math:`v_1` and :math:`v_3`. In degrees.
    gamma : float, default 90
        Angle between vectors :math:`v_1` and :math:`v_2`. In degrees.

    Returns
    -------
    volume : float
        Volume of corresponding region in space.

    Examples
    --------

    .. doctest::

        >>> import wulfric
        >>> wulfric.geometry.get_volume([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        1.0
        >>> wulfric.geometry.get_volume([1, 0, 0], [0, 1, 0], [0, 0, 1])
        1.0
        >>> wulfric.geometry.get_volume(1, 1, 1, 90, 90, 90)
        1.0
    """

    if len(args) == 1:
        cell = np.array(args[0])
    elif len(args) == 3:
        cell = np.array(args)
    elif len(args) == 6:
        a, b, c, alpha, beta, gamma = args
        alpha = alpha * TORADIANS
        beta = beta * TORADIANS
        gamma = gamma * TORADIANS
        sq_root = (
            1
            + 2 * cos(alpha) * cos(beta) * cos(gamma)
            - cos(alpha) ** 2
            - cos(beta) ** 2
            - cos(gamma) ** 2
        )
        return a * b * c * sqrt(sq_root)
    else:
        raise ValueError(
            "Unable to identify input. "
            + "Supported: one (3, 3) array-like, or three (3,) array-like, or 6 floats."
        )

    return float(abs(np.linalg.det(cell)))


def get_angle(v1, v2, radians=False):
    r"""
    Computes angle between two vectors.

    .. math::

        \alpha
        =
        \dfrac{(\boldsymbol{v_1} \cdot \boldsymbol{v_2})}
        {\vert\boldsymbol{v_1}\vert\cdot\vert\boldsymbol{v_2}\vert}

    Parameters
    ----------
    v1 : (3,) |array-like|_
        First vector.
    v2 : (3,) |array-like|_
        Second vector.
    radians : bool, default False
        Whether to return value in radians.

    Returns
    -------
    angle: float
        Angle in degrees or radians (see ``radians``).

    Raises
    ------
    ValueError
        If one of the vectors is zero vector (or both). Norm is compared against
        :numpy:`finfo`\ (float).eps.

    Examples
    --------

    .. doctest::

        >>> import wulfric
        >>> wulfric.geometry.get_angle([1, 0, 0], [0, 0, 1])
        90.0
        >>> wulfric.geometry.get_angle([1, 0, 0], [1, 0, 0])
        0.0
        >>> round(wulfric.geometry.get_angle([1, 0, 0], [1, 1, 1]), 4)
        54.7356
    """

    # Normalize vectors
    v1_norm = np.linalg.norm(v1)
    v2_norm = np.linalg.norm(v2)
    if abs(v1_norm) <= np.finfo(float).eps or abs(v2_norm) <= np.finfo(float).eps:
        raise ValueError("Angle is ill defined (zero vector).")

    v1 = np.array(v1) / v1_norm
    v2 = np.array(v2) / v2_norm

    alpha = np.arccos(np.clip(np.dot(v1, v2), -1.0, 1.0))
    if radians:
        return float(alpha)

    return float(alpha * TODEGREES)


def parallelepiped_check(
    a,
    b,
    c,
    alpha,
    beta,
    gamma,
    raise_error=False,
    length_tolerance=1e-8,
    angle_tolerance=1e-4,
):
    r"""
    Checks if parallelepiped is valid.

    The conditions are

    * :math:`a > 0`
    * :math:`b > 0`
    * :math:`c > 0`
    * :math:`0 < \alpha < 180`
    * :math:`0 < \beta < 180`
    * :math:`0 < \gamma < 180`
    * :math:`\gamma < \alpha + \beta < 360 - \gamma`
    * :math:`\beta < \alpha + \gamma < 360 - \beta`
    * :math:`\alpha < \beta + \gamma < 360 - \alpha`

    Parameters
    ----------
    a : float
        Length of the :math:`\boldsymbol{v_1}` vector.
    b : float
        Length of the :math:`\boldsymbol{v_2}` vector.
    c : float
        Length of the :math:`\boldsymbol{v_3}` vector.
    alpha : float
        Angle between vectors :math:`\boldsymbol{v_2}` and :math:`\boldsymbol{v_3}`. In degrees.
    beta : float
        Angle between vectors :math:`\boldsymbol{v_1}` and :math:`\boldsymbol{v_3}`. In degrees.
    gamma : float
        Angle between vectors :math:`\boldsymbol{v_1}` and :math:`\boldsymbol{v_2}`. In degrees.
    raise_error : bool, default False
        Whether to raise error if parameters can not form a parallelepiped.
    length_tolerance : float, default :math:`10^{-8}`
        Numerical tolerance for the length variables. Default value is chosen in the
        contexts of condense matter physics, assuming that length is given in Angstroms.
        Please choose appropriate tolerance for your problem.
    angle_tolerance : float, default :math:`10^{-4}`
        Numerical tolerance for the angle variables. Default value is chosen in
        the contexts of condense matter physics, assuming that angles are in degrees.
        Please choose appropriate tolerance for your problem.

    Returns
    -------
    result: bool
        Whether the parameters could from a parallelepiped.

    Raises
    ------
    ValueError
        If parameters can not form a parallelepiped.
        Only raised if ``raise_error`` is ``True`` (it is ``False`` by default).

    Examples
    --------

    .. doctest::

        >>> import wulfric
        >>> wulfric.geometry.parallelepiped_check(1, 1, 1, 90, 90, 90)
        True
        >>> wulfric.geometry.parallelepiped_check(1, 1, 1, 30, 20, 110)
        False
        >>> wulfric.geometry.parallelepiped_check(1, -1, 1, 90, 90, 90)
        False
        >>> wulfric.geometry.parallelepiped_check(1, 0, 1, 90, 90, 90)
        False
        >>> wulfric.geometry.parallelepiped_check(1, 1, 1, 90, 199, 90)
        False

    """

    result = (
        compare_with_tolerance(a, ">", 0.0, eps=length_tolerance)
        and compare_with_tolerance(b, ">", 0.0, eps=length_tolerance)
        and compare_with_tolerance(c, ">", 0.0, eps=length_tolerance)
        and compare_with_tolerance(alpha, "<", 180.0, eps=angle_tolerance)
        and compare_with_tolerance(beta, "<", 180.0, eps=angle_tolerance)
        and compare_with_tolerance(gamma, "<", 180.0, eps=angle_tolerance)
        and compare_with_tolerance(alpha, ">", 0.0, eps=angle_tolerance)
        and compare_with_tolerance(beta, ">", 0.0, eps=angle_tolerance)
        and compare_with_tolerance(gamma, ">", 0.0, eps=angle_tolerance)
        and compare_with_tolerance(gamma, "<", alpha + beta, eps=angle_tolerance)
        and compare_with_tolerance(
            alpha + beta, "<", 360.0 - gamma, eps=angle_tolerance
        )
        and compare_with_tolerance(beta, "<", alpha + gamma, eps=angle_tolerance)
        and compare_with_tolerance(
            alpha + gamma, "<", 360.0 - beta, eps=angle_tolerance
        )
        and compare_with_tolerance(alpha, "<", beta + gamma, eps=angle_tolerance)
        and compare_with_tolerance(
            beta + gamma, "<", 360.0 - alpha, eps=angle_tolerance
        )
    )

    if not result and raise_error:
        message = "Parameters could not form a parallelepiped:\n"
        message += f"a = {a}"
        if not compare_with_tolerance(a, ">", 0.0, eps=length_tolerance):
            message += f" (a <= 0 with numerical tolerance: {length_tolerance})"
        message += "\n"
        message += f"b = {b}"
        if not compare_with_tolerance(b, ">", 0.0, eps=length_tolerance):
            message += f" (b <= 0 with numerical tolerance: {length_tolerance})"
        message += "\n"
        message += f"c = {c}"
        if not compare_with_tolerance(c, ">", 0.0, eps=length_tolerance):
            message += f" (c <= 0 with numerical tolerance: {length_tolerance})"
        message += "\n"
        message += f"alpha = {alpha}\n"
        if not compare_with_tolerance(alpha, "<", 180.0, eps=angle_tolerance):
            message += f"  (alpha >= 180 with numerical tolerance: {angle_tolerance})\n"
        if not compare_with_tolerance(alpha, ">", 0.0, eps=angle_tolerance):
            message += f"  (alpha <= 0 with numerical tolerance: {angle_tolerance})\n"
        message += f"beta = {beta}\n"
        if not compare_with_tolerance(beta, "<", 180.0, eps=angle_tolerance):
            message += f"  (beta >= 180 with numerical tolerance: {angle_tolerance})\n"
        if not compare_with_tolerance(beta, ">", 0.0, eps=angle_tolerance):
            message += f"  (beta <= 0 with numerical tolerance: {angle_tolerance})\n"
        message += f"gamma = {gamma}\n"
        if not compare_with_tolerance(gamma, "<", 180.0, eps=angle_tolerance):
            message += f"  (gamma >= 180 with numerical tolerance: {angle_tolerance})\n"
        if not compare_with_tolerance(gamma, ">", 0.0, eps=angle_tolerance):
            message += f"  (gamma <= 0 with numerical tolerance: {angle_tolerance})\n"
        if not compare_with_tolerance(gamma, "<", alpha + beta, eps=angle_tolerance):
            message += f"Inequality gamma < alpha + beta is not satisfied with numerical tolerance: {angle_tolerance}\n"
        if not compare_with_tolerance(
            alpha + beta, "<", 360.0 - gamma, eps=angle_tolerance
        ):
            message += f"Inequality alpha + beta < 360 - gamma is not satisfied with numerical tolerance: {angle_tolerance}\n"
        if not compare_with_tolerance(beta, "<", alpha + gamma, eps=angle_tolerance):
            message += f"Inequality beta < alpha + gamma is not satisfied with numerical tolerance: {angle_tolerance}\n"
        if not compare_with_tolerance(
            alpha + gamma, "<", 360.0 - beta, eps=angle_tolerance
        ):
            message += f"Inequality alpha + gamma < 360 - beta is not satisfied with numerical tolerance: {angle_tolerance}\n"
        if not compare_with_tolerance(alpha, "<", beta + gamma, eps=angle_tolerance):
            message += f"Inequality alpha < beta + gamma is not satisfied with numerical tolerance: {angle_tolerance}\n"
        if not compare_with_tolerance(
            beta + gamma, "<", 360.0 - alpha, eps=angle_tolerance
        ):
            message += f"Inequality beta + gamma < 360 - alpha is not satisfied with numerical tolerance: {angle_tolerance}\n"
        raise ValueError(message)

    return result


def get_spherical(
    vector, in_degrees=True, polar_axis=[0, 0, 1], radial_line_zero=[1, 0, 0]
):
    R"""
    Compute |spherical-coordinates|_ of a vector.

    :math:`(v^x, v^y, v^z) \rightarrow (r, \theta, \phi)`

    Parameters
    ----------
    vector : (3,) |array-like|_
        Vector to be converted.
    in_degrees : bool, default True
        Whether to return angles in degrees or radians. If ``True``, then angles are
        returned in degrees.
    polar_axis : (3,) |array-like|_
        Polar axis (see notes). By default oriented along :math:`+z`.
    radial_line_zero : (3,) |array-like|_
        Zero of the radial line (see notes). By default oriented along :math:`+x`.

    Returns
    -------
    r : float
        Length of the ``vector``.
    polar_angle : float
        Polar angle. Returned in degrees if ``in_degrees = True``, in radians otherwise.
    azimuthal_angle : float
        Azimuthal angle. Returned in degrees if ``in_degrees = True``, in radians
        otherwise.

    Notes
    -----
    ``polar_angle`` is defined as the angle between the polar axis and the given
    ``vector`` with :math:`0 \le \alpha_{polar} \le \pi`.

    Azimuthal angle is defined as the angle of the rotation of the radial line around the
    polar axis. This angle is measured from the ``radial_line_zero`` in accordance to the
    right-hand rule. :math:`0 \le \alpha_{azimuthal} \le 2\pi`.

    Radial line is the projection of the ``vector`` on the plane perpendicular to the
    ``polar_axis``.

    If azimuthal angle is ill-defined, then wulfric returns

    * :math:`0` if polar angle is :math:`0`.
    * :math:`\pi` if polar angle is :math:`\pi`.


    Examples
    --------

    .. doctest::

        >>> import wulfric
        >>> wulfric.geometry.get_spherical([1, 0, 0])
        (1.0, 90.0, 0.0)
        >>> wulfric.geometry.get_spherical([-1, 0, 0])
        (1.0, 90.0, 180.0)
        >>> wulfric.geometry.get_spherical([0, 1, 0])
        (1.0, 90.0, 90.0)
        >>> wulfric.geometry.get_spherical([0, -1, 0])
        (1.0, 90.0, 270.0)
        >>> wulfric.geometry.get_spherical([0, 0, 1])
        (1.0, 0.0, 0.0)
        >>> wulfric.geometry.get_spherical([0, 0, -1])
        (1.0, 180.0, 180.0)
        >>> wulfric.geometry.get_spherical([1, 0, 0], polar_axis=[1, 0, 0])
        (1.0, 0.0, 0.0)

    """
    polar_axis = np.array(polar_axis) / np.linalg.norm(polar_axis)
    radial_line_zero = np.array(radial_line_zero) / np.linalg.norm(radial_line_zero)
    r = float(np.linalg.norm(vector))
    vector = np.array(vector) / r

    if np.allclose(vector, polar_axis):
        polar, azimuthal = 0.0, 0.0
    elif np.allclose(vector, -polar_axis):
        polar, azimuthal = np.pi, np.pi
    else:
        polar = float(np.arccos(np.clip(np.dot(vector, polar_axis), -1, 1)))

        vector = vector - polar_axis * np.dot(vector, polar_axis)
        vector /= np.linalg.norm(vector)

        # This one is more complex, as it is from 0 to 360
        azimuthal = float(np.arccos(np.clip(np.dot(vector, radial_line_zero), -1, 1)))

        if np.linalg.det([polar_axis, radial_line_zero, vector]) >= 0:
            pass
        else:
            azimuthal = 2 * np.pi - azimuthal

    if in_degrees:
        return r, polar * TODEGREES, azimuthal * TODEGREES
    else:
        return r, polar, azimuthal


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
