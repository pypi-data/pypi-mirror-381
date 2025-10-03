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
from random import choices
from string import ascii_lowercase as ASCII_LOWERCASE


import numpy as np

from wulfric.cell._basic_manipulation import get_reciprocal
from wulfric.cell._voronoi import get_wigner_seitz_cell, get_lattice_points
from wulfric.constants import ATOM_COLORS
from wulfric.crystal._atoms import get_atom_species

try:
    import plotly.graph_objects as go  # noqa: F401
    from plotly.subplots import make_subplots

    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# Save local scope at this moment
old_dir = set(dir())
old_dir.add("old_dir")


_LEGEND_SETTINGS = {
    "top": dict(yanchor="bottom", y=1.0, xanchor="center", x=0.5),
    "bottom": dict(yanchor="top", y=0.0, xanchor="center", x=0.5),
    "left": dict(yanchor="middle", y=0.5, xanchor="right", x=0.0),
    "right": dict(yanchor="middle", y=0.5, xanchor="left", x=1.0),
}


# Source: https://gamedev.stackexchange.com/questions/38536/given-a-rgb-color-x-how-to-find-the-most-contrasting-color-y
def _get_good_contrast(hex_color):
    hex_color = hex_color[1:]
    R, G, B = [int(hex_color[i : i + 2], 16) / 255 for i in (0, 2, 4)]

    gamma = 2.2
    L = 0.2126 * R**gamma + 0.7152 * G**gamma + 0.0722 * B**gamma

    if L > 0.5**gamma:
        return "#000000"

    return "#FFFFFF"


class PlotlyEngine:
    r"""
    Plotting engine based on |plotly|_.

    Parameters
    ----------
    fig : plotly graph object, optional
        Figure to plot on. If not provided, then a new one is created as
        ``fig = go.Figure()``.
    _sphinx_gallery_fix : bool, default  False
        Fixes display issues when building documentation using sphinx gallery.
        Please, always ignore this argument

    Attributes
    ----------
    fig : plotly graph object
        Figure to plot on.

    Notes
    -----
    This class is a part of ``wulfric[visual]``
    """

    def __init__(self, fig=None, _sphinx_gallery_fix=False, rows=1, cols=1):
        if not PLOTLY_AVAILABLE:
            raise ImportError(
                'Plotly is not available. Please install it with "pip install plotly"'
            )

        if fig is None:
            fig = make_subplots(
                rows=rows,
                cols=cols,
                specs=[[{"type": "scene"} for _ in range(cols)] for _ in range(rows)],
            )
        self.fig = fig

        self.fig.update_layout(template="none")

        self._sphinx_gallery_fix = _sphinx_gallery_fix

        # Fix for plotly #7143
        self.x_range = {}
        self.y_range = {}
        self.z_range = {}

    # Fix for plotly #7143
    def _update_range(self, x_min, x_max, y_min, y_max, z_min, z_max, row=1, col=1):
        if (row, col) not in self.x_range:
            self.x_range[(row, col)] = np.array([x_min, x_max], dtype=float)
            self.y_range[(row, col)] = np.array([y_min, y_max], dtype=float)
            self.z_range[(row, col)] = np.array([z_min, z_max], dtype=float)
        else:
            self.x_range[(row, col)][0] = min(self.x_range[(row, col)][0], x_min)
            self.x_range[(row, col)][1] = max(self.x_range[(row, col)][1], x_max)
            self.y_range[(row, col)][0] = min(self.y_range[(row, col)][0], y_min)
            self.y_range[(row, col)][1] = max(self.y_range[(row, col)][1], y_max)
            self.z_range[(row, col)][0] = min(self.z_range[(row, col)][0], z_min)
            self.z_range[(row, col)][1] = max(self.z_range[(row, col)][1], z_max)

    # Fix for plotly #7143
    def _update_fig_aspect_range(self):
        for row, col in self.x_range:
            xlim = 1.05 * self.x_range[(row, col)]
            ylim = 1.05 * self.y_range[(row, col)]
            zlim = 1.05 * self.z_range[(row, col)]

            self.fig.update_scenes(
                xaxis=dict(range=xlim),
                yaxis=dict(range=ylim),
                zaxis=dict(range=zlim),
                aspectmode="manual",
                aspectratio=dict(
                    x=abs((xlim[1] - xlim[0]) / (zlim[1] - zlim[0])),
                    y=abs((ylim[1] - ylim[0]) / (zlim[1] - zlim[0])),
                    z=1,
                ),
                row=row,
                col=col,
            )

    def show(self, axes_visible=True, legend_position="top", **kwargs):
        r"""
        Shows the figure in the interactive mode.

        Parameters
        ----------
        axes_visible : bool, default True
            Whether to show axes.
        legend_position : str, default "top"
            Positions of the legend, case insensitive.
        **kwargs
            Passed directly to the |plotly-update-layout|_.
        """

        if not axes_visible:
            self.fig.update_scenes(
                xaxis_visible=False, yaxis_visible=False, zaxis_visible=False
            )

        legend_position = legend_position.lower()

        if legend_position not in list(_LEGEND_SETTINGS):
            raise ValueError(
                f"Supported values for legend_position are {list(_LEGEND_SETTINGS)}, got {legend_position}."
            )
        legend = _LEGEND_SETTINGS[legend_position]

        self.fig.update_layout(**kwargs, legend=legend)

        # Fix for plotly #7143
        self._update_fig_aspect_range()

        if self._sphinx_gallery_fix:
            return self.fig

        self.fig.show()

    def save(
        self,
        output_name="wulfric-plot.html",
        axes_visible=True,
        legend_position="top",
        kwargs_write_html=None,
        **kwargs,
    ):
        r"""
        Saves the figure in the html file.

        Parameters
        ----------
        output_name : str, default "lattice_graph.html"
            Name of the file to be saved. With extension.
        axes_visible : bool, default True
            Whether to show axes.
        legend_position : str, default "top"
            Positions of the legend, case insensitive.
        kwargs_write_html : dict, optional
            Passed directly to the |plotly-write-html|_.
        **kwargs
            Passed directly to the |plotly-update-layout|_.
        """

        if kwargs_write_html is None:
            kwargs_write_html = {}

        if not axes_visible:
            self.fig.update_scenes(
                xaxis_visible=False, yaxis_visible=False, zaxis_visible=False
            )

        legend_position = legend_position.lower()

        if legend_position not in list(_LEGEND_SETTINGS):
            raise ValueError(
                f"Supported values for legend_position are {list(_LEGEND_SETTINGS)}, got {legend_position}."
            )
        legend = _LEGEND_SETTINGS[legend_position]

        self.fig.update_layout(**kwargs, legend=legend)

        # Fix for plotly #7143
        self._update_fig_aspect_range()

        self.fig.write_html(output_name, **kwargs_write_html)

    def plot_points(
        self,
        points,
        colors="#000000",
        legend_label=None,
        legend_group=None,
        scale=1,
        row=1,
        col=1,
    ):
        r"""
        Plots a set of points.

        Parameters
        ----------
        points : (N, 3) |array-like|_
            Coordinates of the points.
        colors : str or list of str, default "#000000"
            Color of the line. Any value that is supported by |plotly|_.
        legend_label : str, optional
            Label of the line that is displayed in the figure.
        legend_group : str, optional
            Legend's group. If ``None``, then defaults to the random string of 10
            characters.
        scale : float, default 1
            Scale for the size of point's markers. Use ``scale>1`` to increase the size.
        row : int, default 1
            Row of the subplot.
        col : int, default 1
            Column of the subplot.
        """

        if legend_group is None:
            legend_group = "".join(choices(ASCII_LOWERCASE, k=10))

        points = np.array(points).T

        self.fig.add_traces(
            data=dict(
                type="scatter3d",
                mode="markers",
                legendgroup=legend_group,
                name=legend_label,
                showlegend=legend_label is not None,
                x=points[0],
                y=points[1],
                z=points[2],
                marker=dict(size=2 * scale, color=colors),
                hoverinfo="none",
            ),
            rows=row,
            cols=col,
        )

        # Fix for plotly #7143
        self._update_range(
            x_min=points[0].min(),
            x_max=points[0].max(),
            y_min=points[1].min(),
            y_max=points[1].max(),
            z_min=points[2].min(),
            z_max=points[2].max(),
            row=row,
            col=col,
        )

    def plot_line(
        self,
        start_point,
        end_point,
        color="#000000",
        legend_label=None,
        legend_group=None,
        row=1,
        col=1,
    ):
        r"""
        Plots a single line between ``start_point`` to ``end_point``.

        Parameters
        ----------
        start_point : (3, ) |array-like|_
            First end of the line.
        end_point : (3, ) |array-like|_
            Second point of the line.
        color : str, default "#000000"
            Color of the line. Any value that is supported by |plotly|_.
        legend_label : str, optional
            Label of the line that is displayed in the figure.
        legend_group : str, optional
            Legend's group. If ``None``, then defaults to the random string of 10
            characters.
        row : int, default 1
            Row of the subplot.
        col : int, default 1
            Column of the subplot.
        """

        if legend_group is None:
            legend_group = "".join(choices(ASCII_LOWERCASE, k=10))

        x, y, z = np.array([start_point, end_point]).T

        self.fig.add_traces(
            data=dict(
                type="scatter3d",
                mode="lines",
                legendgroup=legend_group,
                name=legend_label,
                showlegend=legend_label is not None,
                x=x,
                y=y,
                z=z,
                line=dict(color=color),
                hoverinfo="none",
            ),
            rows=row,
            cols=col,
        )

        # Fix for plotly #7143
        self._update_range(
            x_min=x.min(),
            x_max=x.max(),
            y_min=y.min(),
            y_max=y.max(),
            z_min=z.min(),
            z_max=z.max(),
            row=row,
            col=col,
        )

    def plot_vector(
        self,
        start_point,
        end_point,
        color="#000000",
        vector_label=None,
        legend_label=None,
        legend_group=None,
        row=1,
        col=1,
    ):
        r"""
        Plots a single vector pointing from ``start_point`` to ``end_point``.

        Parameters
        ----------
        start_point : (3, ) |array-like|_
            Start point of the vector.
        end_point : (3, ) |array-like|_
            End point of the vector.
        color : str, default "#000000"
            Color of the vector and its label. Any value that is supported by |plotly|_.
        vector_label : str, optional
            Label of the vector that is displayed in the figure.
        legend_label : str, optional
            Label for the legend. Entry in legend only showed if
            ``legend_label is not None``.
        legend_group : str, optional
            Legend's group. If ``None``, then defaults to the random string of 10
            characters.
        row : int, default 1
            Row of the subplot.
        col : int, default 1
            Column of the subplot.
        """

        if legend_group is None:
            legend_group = "".join(choices(ASCII_LOWERCASE, k=10))

        x, y, z = np.array([start_point, end_point]).T

        self.fig.add_traces(
            data=[
                dict(
                    type="scatter3d",
                    mode="lines",
                    legendgroup=legend_group,
                    name=legend_label,
                    showlegend=legend_label is not None,
                    x=x,
                    y=y,
                    z=z,
                    line=dict(color=color, width=3),
                    hoverinfo="none",
                ),
                dict(
                    type="cone",
                    legendgroup=legend_group,
                    showlegend=False,
                    x=[x[1]],
                    y=[y[1]],
                    z=[z[1]],
                    u=[0.4 * (x[1] - x[0])],
                    v=[0.4 * (y[1] - y[0])],
                    w=[0.4 * (z[1] - z[0])],
                    anchor="tip",
                    colorscale=[[0, color], [1, color]],
                    showscale=False,
                    hoverinfo="none",
                ),
            ],
            rows=row,
            cols=col,
        )
        if vector_label is not None:
            self.fig.add_traces(
                data=dict(
                    type="scatter3d",
                    mode="text",
                    legendgroup=legend_group,
                    showlegend=False,
                    x=[1.2 * (x[1] - x[0]) + x[0]],
                    y=[1.2 * (y[1] - y[0]) + y[0]],
                    z=[1.2 * (z[1] - z[0]) + z[0]],
                    marker=dict(size=0),
                    text=vector_label,
                    textfont=dict(size=12, color=color),
                    textposition="top center",
                    hoverinfo="none",
                ),
                rows=row,
                cols=col,
            )

            # Fix for plotly #7143
            self._update_range(
                x_min=1.2 * (x[1] - x[0]) + x[0],
                x_max=1.2 * (x[1] - x[0]) + x[0],
                y_min=1.2 * (y[1] - y[0]) + y[0],
                y_max=1.2 * (y[1] - y[0]) + y[0],
                z_min=1.2 * (z[1] - z[0]) + z[0],
                z_max=1.2 * (z[1] - z[0]) + z[0],
                row=row,
                col=col,
            )

        # Fix for plotly #7143
        self._update_range(
            x_min=x.min(),
            x_max=x.max(),
            y_min=y.min(),
            y_max=y.max(),
            z_min=z.min(),
            z_max=z.max(),
            row=row,
            col=col,
        )

    def plot_cell(
        self,
        cell,
        color="#000000",
        plot_vectors=True,
        vector_label="a",
        shift=(0, 0, 0),
        legend_label=None,
        legend_group=None,
        row=1,
        col=1,
    ):
        r"""
        Plots given ``cell`` as is.

        Parameters
        ----------
        cell : (3, 3) |array-like|_
            Matrix of a cell, rows are interpreted as vectors.
        color : str, default "#000000"
            Colour for the cell and the labels. Any value that is supported by |plotly|_.
        plot_vectors : bool, default True
            Whether to plot lattice vectors.
        vector_label : str, default "a"
            Vector's label, ignored if ``plot_vectors = False``.
        shift : (3, ) |array-like|_, default (0.0, 0.0, 0.0)
            Absolute coordinates of the corner of the cell, from which the three lattice
            vectors are plotted.
        legend_label : str, optional
            Label for the legend. Entry in legend only showed if
            ``legend_label is not None``.
        legend_group : str, optional
            Legend's group. If ``None``, then defaults to the random string of 10
            characters.
        row : int, default 1
            Row of the subplot.
        col : int, default 1
            Column of the subplot.
        """

        cell = np.array(cell)

        if legend_group is None:
            legend_group = "".join(choices(ASCII_LOWERCASE, k=10))

        shift = np.array(shift)

        # Plot vectors
        if plot_vectors:
            for i in range(3):
                self.plot_vector(
                    start_point=shift,
                    end_point=shift + cell[i],
                    color=color,
                    vector_label=f"{vector_label}{i + 1}",
                    legend_group=legend_group,
                    row=row,
                    col=col,
                )

        # Plot the cell borders
        for i in range(0, 3):
            j = (i + 1) % 3
            k = (i + 2) % 3
            self.plot_line(
                start_point=shift,
                end_point=shift + cell[i],
                color=color,
                legend_label=legend_label,
                legend_group=legend_group,
                row=row,
                col=col,
            )
            if legend_label is not None:
                legend_label = None
            self.plot_line(
                start_point=shift + cell[i],
                end_point=shift + cell[i] + cell[j],
                color=color,
                legend_group=legend_group,
                row=row,
                col=col,
            )
            self.plot_line(
                start_point=shift + cell[i],
                end_point=shift + cell[i] + cell[k],
                color=color,
                legend_group=legend_group,
                row=row,
                col=col,
            )
            self.plot_line(
                start_point=shift + cell[i] + cell[j],
                end_point=shift + cell[i] + cell[j] + cell[k],
                color=color,
                legend_group=legend_group,
                row=row,
                col=col,
            )

    def plot_wigner_seitz_cell(
        self,
        cell,
        plot_vectors=True,
        vector_label="a",
        color="#000000",
        shift=(0.0, 0.0, 0.0),
        legend_label=None,
        legend_group=None,
        row=1,
        col=1,
    ):
        r"""
        Plots Wigner-Seitz cell of the lattice spawned by the given ``cell``.

        Parameters
        ----------
        cell : (3, 3) |array-like|_
            Matrix of a cell, rows are interpreted as vectors.
        plot_vectors : bool, default True
            Whether to plot lattice vectors.
        vector_label : str, default "a"
            Vector's label, ignored if ``plot_vectors = False``.
        color : str, default "#000000"
            Colour for the cell and labels. Any value that is supported by |plotly|_.
        shift : (3, ) |array-like|_, default (0.0, 0.0, 0.0)
            Absolute coordinates of the center of the Wigner-Seitz cell.
        legend_label : str, optional
            Label for the legend. Entry in legend only showed if
            ``legend_label is not None``.
        legend_group : str, optional
            Legend's group. If ``None``, then defaults to the random string of 10
            characters.
        row : int, default 1
            Row of the subplot.
        col : int, default 1
            Column of the subplot.
        """

        cell = np.array(cell)

        if legend_group is None:
            legend_group = "".join(choices(ASCII_LOWERCASE, k=10))

        # Plot vectors
        if plot_vectors:
            for i in range(3):
                self.plot_vector(
                    start_point=shift,
                    end_point=shift + cell[i],
                    color=color,
                    vector_label=f"{vector_label}{i + 1}",
                    legend_group=legend_group,
                    row=row,
                    col=col,
                )

        vertices, edges = get_wigner_seitz_cell(cell=cell)
        for start_index, end_index in edges:
            self.plot_line(
                start_point=shift + vertices[start_index],
                end_point=shift + vertices[end_index],
                color=color,
                legend_label=legend_label,
                legend_group=legend_group,
                row=row,
                col=col,
            )
            if legend_label is not None:
                legend_label = None

    def plot_brillouin_zone(
        self,
        cell,
        plot_vectors=True,
        vector_label="b",
        color="#FF4D67",
        shift=(0.0, 0.0, 0.0),
        legend_label=None,
        legend_group=None,
        row=1,
        col=1,
    ):
        r"""

        Plots Brillouin zone.

        Parameters
        ----------
        cell : (3, 3) |array-like|_
            Matrix of a cell, rows are interpreted as vectors.
        plot_vectors : bool, default True
            Whether to plot lattice vectors.
        vector_label : str, default "b"
            Vector's label, ignored if ``plot_vectors = False``.
        color : str, default "#FF4D67"
            Colour for the Brillouin zone and labels. Any value that is supported by |plotly|_.
        shift : (3, ) |array-like|_, default (0.0, 0.0, 0.0)
            Absolute coordinates of the center of the Brillouin zone.
        legend_label : str, optional
            Label for the legend. Entry in legend only showed if
            ``legend_label is not None``.
        legend_group : str, optional
            Legend's group. If ``None``, then defaults to the random string of 10
            characters.
        row : int, default 1
            Row of the subplot.
        col : int, default 1
            Column of the subplot.
        """

        self.plot_wigner_seitz_cell(
            cell=get_reciprocal(cell),
            plot_vectors=plot_vectors,
            vector_label=vector_label,
            color=color,
            shift=shift,
            legend_label=legend_label,
            legend_group=legend_group,
            row=row,
            col=col,
        )

    def plot_kpath(
        self,
        kp,
        color="#000000",
        shift=(0.0, 0.0, 0.0),
        legend_label=None,
        legend_group=None,
        row=1,
        col=1,
    ):
        r"""
        Plots k-path in the reciprocal space.

        Parameters
        ----------
        kp : :py:class:`.Kpoints`
            K-points and k-path.
        color : str, default "#000000"
            Colour for the plot. Any value that is supported by |plotly|_.
        shift : (3, ) |array-like|_, default (0, 0, 0)
            Absolute coordinates of the shift in reciprocal space.
        legend_label : str, optional
            Label for the legend. Entry in legend only showed if
            ``legend_label is not None``.
        legend_group : str, optional
            Legend's group. If ``None``, then defaults to the random string of 10
            characters.
        row : int, default 1
            Row of the subplot.
        col : int, default 1
            Column of the subplot.
        """

        shift = np.array(shift)

        if legend_group is None:
            legend_group = "".join(choices(ASCII_LOWERCASE, k=10))

        for subpath in kp.path:
            xyz = []
            for i in range(len(subpath)):
                xyz.append(shift + kp.hs_coordinates[subpath[i]] @ kp.rcell)

            xyz = np.array(xyz).T
            self.fig.add_traces(
                data=dict(
                    type="scatter3d",
                    mode="lines",
                    name=legend_label,
                    legendgroup=legend_group,
                    showlegend=legend_label is not None,
                    x=xyz[0],
                    y=xyz[1],
                    z=xyz[2],
                    line=dict(width=3, color=color),
                    hoverinfo="none",
                ),
                rows=row,
                cols=col,
            )
            if legend_label is not None:
                legend_label = None

        # Fix for plotly #7143
        self._update_range(
            x_min=xyz[0].min(),
            x_max=xyz[0].max(),
            y_min=xyz[1].min(),
            y_max=xyz[1].max(),
            z_min=xyz[2].min(),
            z_max=xyz[2].max(),
            row=row,
            col=col,
        )

    def plot_kpoints(
        self,
        kp,
        color="#000000",
        shift=(0.0, 0.0, 0.0),
        legend_label=None,
        legend_group=None,
        scale=1,
        only_from_kpath=False,
        row=1,
        col=1,
    ):
        r"""
        Plots high-symmetry k-points in the reciprocal space.

        Parameters
        ----------
        kp : :py:class:`.Kpoints`
            K-points and k-path.
        color : str, default "#000000"
            Colour for the plot. Any value that is supported by |plotly|_.
        shift : (3, ) |array-like|_, default (0, 0, 0)
            Absolute coordinates of the shift in reciprocal space.
        legend_label : str, optional
            Label for the legend. Entry in legend only showed if
            ``legend_label is not None``.
        legend_group : str, optional
            Legend's group. If ``None``, then defaults to the random string of 10
            characters.
        scale : float, default 1
            Scale for the size of point's markers and text labels. Use ``scale>1`` to
            increase the size.
        only_from_kpath : bool, default False
            Whether to plot all pre-defined points or only the ones that included into the
            predefined k-path.
        row : int, default 1
            Row of the subplot.
        col : int, default 1
            Column of the subplot.
        """

        shift = np.array(shift)

        if legend_group is None:
            legend_group = "".join(choices(ASCII_LOWERCASE, k=10))

        p_abs = []
        p_rel = []
        labels = []
        path_points = []
        for subpath in kp.path:
            path_points += subpath
        for point in kp.hs_names:
            if not only_from_kpath or point in path_points:
                p_abs.append(shift + kp.hs_coordinates[point] @ kp.rcell)
                p_rel.append(kp.hs_coordinates[point])

                labels.append(point)

        p_abs = np.array(p_abs).T

        self.fig.add_traces(
            data=dict(
                type="scatter3d",
                mode="markers+text",
                legendgroup=legend_group,
                name=legend_label,
                showlegend=legend_label is not None,
                x=p_abs[0],
                y=p_abs[1],
                z=p_abs[2],
                marker=dict(size=5 * scale, color=color),
                text=labels,
                textposition="top center",
                textfont=dict(size=13 * scale, color=color),
                hovertext=p_rel,
                hoverinfo="text",
            ),
            rows=row,
            cols=col,
        )

        # Fix for plotly #7143
        self._update_range(
            x_min=p_abs[0].min(),
            x_max=p_abs[0].max(),
            y_min=p_abs[1].min(),
            y_max=p_abs[1].max(),
            z_min=p_abs[2].min(),
            z_max=p_abs[2].max(),
            row=row,
            col=col,
        )

    def plot_lattice(
        self,
        cell,
        color="#000000",
        range=(1, 1, 1),
        shift=(0, 0, 0),
        legend_label=None,
        legend_group=None,
        row=1,
        col=1,
    ):
        r"""
        Plots lattice points spawned by the given ``cell``.

        Parameters
        ----------
        cell : (3, 3) |array-like|_
            Matrix of a cell, rows are interpreted as vectors.
        color : str, default "#000000"
            Color of the points. Any value that is supported by |plotly|_.
        range : (3, ) tuple of int, default (1, 1, 1)
            How many lattice points to plot. All lattice points with relative coordinates
            ``r_1``, ``r_2``, ``r_3``, that fulfil

            * ``-range[0] <= r_1 <= range[0]``
            * ``-range[1] <= r_2 <= range[1]``
            * ``-range[2] <= r_3 <= range[2]``

            are plotted.
        shift : (3, ) |array-like|_, default (0, 0, 0)
            Absolute coordinates of the corner of the cell, from which the three lattice
            vectors are plotted.
        legend_label : str, optional
            Label for the legend. Entry in legend only showed if
            ``legend_label is not None``.
        legend_group : str, optional
            Legend's group. If ``None``, then defaults to the random string of 10
            characters.
        row : int, default 1
            Row of the subplot.
        col : int, default 1
            Column of the subplot.
        """

        cell = np.array(cell)

        if legend_group is None:
            legend_group = "".join(choices(ASCII_LOWERCASE, k=10))

        points = (
            get_lattice_points(cell=cell, range=range, relative=False, flat=True)
            + np.array(shift)[np.newaxis, :]
        )

        self.plot_points(
            points=points,
            colors=color,
            legend_label=legend_label,
            legend_group=legend_group,
            row=row,
            col=col,
        )

    def plot_atoms(
        self,
        cell,
        atoms,
        colors=None,
        legend_label=None,
        legend_group=None,
        shift=(0, 0, 0),
        scale=1,
        row=1,
        col=1,
    ):
        r"""
        Plots a set of atoms.

        Parameters
        ----------
        cell : (3, 3) |array-like|_
            Matrix of a cell, rows are interpreted as vectors.
        atoms : dict
            Dictionary with N atoms. Expected keys:

            *   "positions" : (N, 3) |array-like|_

                Positions of the atoms in the basis of lattice vectors (``cell``). In other
                words - relative coordinates of atoms.
            *   "names" : (N, ) list of str, optional
                See Notes

            *   "species" : (N, ) list of str, optional
                See Notes

        colors : str or list of str, optional
            Color of the atoms. Any value that is supported by |plotly|_. If ``None``,
            then color is deduced based on atoms's species.
        legend_label : str, optional
            Label of the line that is displayed in the figure.
        legend_group : str, optional
            Legend's group. If ``None``, then defaults to the random string of 10
            characters.
        scale : float, default 1
            Scale for the size of atoms's markers and text labels. Use ``scale>1`` to
            increase the size.
        row : int, default 1
            Row of the subplot.
        col : int, default 1
            Column of the subplot.

        Notes
        =====
        ``atoms["names"]`` is used to deduce atom's species if necessary via
        :py:func:`wulfric.crystal.get_atom_species`.

        ``atoms["species"] is used to define atom's colors if ``colors is None``
        """
        cell = np.array(cell)

        if legend_group is None:
            legend_group = "".join(choices(ASCII_LOWERCASE, k=10))

        points = atoms["positions"] @ cell + np.array(shift)[np.newaxis, :]

        points = points.T

        if "names" in atoms:
            names = atoms["names"]
        else:
            names = [f"X{i + 1}" for i in range(len(atoms["positions"]))]

        if colors is None:
            if "species" in atoms:
                species = atoms["species"]
            else:
                species = [
                    get_atom_species(name=name, raise_on_fail=False) for name in names
                ]

            colors = [ATOM_COLORS[_] for _ in species]

        text_color = [_get_good_contrast(color) for color in colors]

        self.fig.add_traces(
            data=dict(
                type="scatter3d",
                mode="markers+text",
                legendgroup=legend_group,
                name=legend_label,
                showlegend=legend_label is not None,
                x=points[0],
                y=points[1],
                z=points[2],
                text=names,
                marker=dict(size=14 * scale, color=colors),
                hoverinfo="none",
                textfont=dict(size=10 * scale, color=text_color),
                textposition="middle center",
            ),
            rows=row,
            cols=col,
        )

        # Fix for plotly #7143
        self._update_range(
            x_min=points[0].min(),
            x_max=points[0].max(),
            y_min=points[1].min(),
            y_max=points[1].max(),
            z_min=points[2].min(),
            z_max=points[2].max(),
            row=row,
            col=col,
        )


# Populate __all__ with objects defined in this file
__all__ = list(set(dir()) - old_dir)
# Remove all semi-private objects
__all__ = [i for i in __all__ if not i.startswith("_")]
del old_dir
