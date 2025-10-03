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
old_dir = set(dir())
old_dir.add("old_dir")


def compare_with_tolerance(x, condition, y, eps=None, rtol=1e-5, atol=1e-8):
    r"""
    Compares two numbers with given accuracy.

    The formal definition is taken from [1]_:

    .. math::

        \begin{matrix}
            x < y  & x < y - \varepsilon \\
            x > y  & y < x - \varepsilon \\
            x \le y & \text{ not } (y < x - \varepsilon) \\
            x \ge y & \text{ not } (x < y - \varepsilon) \\
            x = y  & \text{ not } (x < y - \varepsilon \text{ or } y < x - \varepsilon) \\
            x \ne y & x < y - \varepsilon \text{ or } y < x - \varepsilon
        \end{matrix}

    Parameters
    ----------
    x : float
        First number.
    condition : str
        Condition to compare with. One of "<", ">", "<=", ">=", "==", "!=".
    y : float
        Second number.
    eps : float, optional
        Tolerance. Used for the comparison if provided. If ``None``, then computed as:

        .. code-block:: python

            eps = atol + rtol * abs(y)

    rtol : float, default :math:`10^{-5}`
        Relative tolerance.
    atol : float, default :math:`10^{-8}`
        Absolute tolerance.

    Returns
    -------
    result: bool
        Whether the ``condition`` is satisfied within given tolerance.

    Raises
    ------
    ValueError
        If ``condition`` is not one of "<", ">", "<=", ">=", "==", "!=".

    References
    ----------
    .. [1] Grosse-Kunstleve, R.W., Sauter, N.K. and Adams, P.D., 2004.
        Numerically stable algorithms for the computation of reduced unit cells.
        Acta Crystallographica Section A: Foundations of Crystallography,
        60(1), pp.1-6.

    Examples
    --------

    .. doctest::

        >>> import wulfric
        >>> wulfric.compare_with_tolerance(1, "==", 1.0000001, eps=1e-6)
        True
        >>> wulfric.compare_with_tolerance(1, "==", 1.0000001, eps=1e-8)
        False
    """

    if eps is None:
        eps = atol + rtol * abs(y)

    if condition == "<":
        return x < y - eps
    if condition == ">":
        return y < x - eps
    if condition == "<=":
        return not y < x - eps
    if condition == ">=":
        return not x < y - eps
    if condition == "==":
        return not (x < y - eps or y < x - eps)
    if condition == "!=":
        return x < y - eps or y < x - eps

    raise ValueError(
        f'Expected one of "<", ">", "<=", ">=", "==", "!=" as condition, got "{condition}".'
    )


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
