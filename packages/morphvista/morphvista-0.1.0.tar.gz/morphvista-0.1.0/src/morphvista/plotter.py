from typing import Optional

import numpy as np
import pandas as pd
import pyvista as pv

from morphsync import MorphSync


def edges_to_lines(edges: np.ndarray) -> np.ndarray:
    lines = np.column_stack((np.full((len(edges), 1), 2), edges))
    return lines


def get_hue_info(layer, hue, clim):
    if hue is None:
        return None, None
    if isinstance(hue, str):
        scalars = layer.nodes[hue].values
    elif isinstance(hue, (np.ndarray, pd.Series)):
        scalars = hue

    if clim is not None and isinstance(clim, tuple):
        return scalars, clim

    if clim is None:
        return scalars, None
    elif clim == "robust":
        low, high = np.nanpercentile(scalars, [2, 98])
    elif clim == "symmetric":
        low, high = np.nanmin(scalars), np.nanmax(scalars)
        val = max(abs(low), abs(high))
        low, high = -val, val
    clim = (low, high)
    return scalars, clim


class MorphPlotter(pv.Plotter):
    def add_mesh_layer(
        self,
        morph: MorphSync,
        layer_name: str = "mesh",
        hue: Optional[str] = None,
        clim: Optional[tuple] = None,
        **kwargs,
    ) -> pv.Actor:
        """Add a mesh layer from a MorphSync object to the plotter.

        Parameters
        ----------
        morph :
            A MorphSync object containing the mesh layer.
        layer_name :
            The name of the mesh layer to add.
        hue :
            The name of the node attributes to use for coloring the mesh.
        clim :
            Color limits for the scalar values. If None, defaults to the min and max of
            the scalar values. If 'robust', uses the 2nd and 98th percentiles. If
            'symmetric', uses symmetric limits around zero.
        **kwargs :
            Additional keyword arguments to pass to [pyvista.Plotter.add_mesh][].

        See Also
        --------
        [pyvista.Plotter.add_mesh][]
        """
        if (
            morph.has_layer(layer_name)
            and morph.get_layer(layer_name).is_spatially_valid
        ):
            mesh_layer = morph.get_layer(layer_name)
            mesh = pv.make_tri_mesh(mesh_layer.vertices, mesh_layer.faces)
            scalars, clim = get_hue_info(mesh_layer, hue, clim=clim)
            return super().add_mesh(
                mesh,
                scalars=scalars,
                clim=clim,
                scalar_bar_args={"title": hue} if isinstance(hue, str) else None,
                **kwargs,
            )

    def add_graph_layer(
        self,
        morph: MorphSync,
        layer_name: str = "graph",
        hue: Optional[str] = None,
        clim: Optional[tuple] = None,
        **kwargs,
    ) -> pv.Actor:
        """Add a graph layer from a MorphSync object to the plotter.

        Parameters
        ----------
        morph :
            A MorphSync object containing the graph layer.
        layer_name :
            The name of the graph layer to add.
        hue :
            The name of the node attributes to use for coloring the graph.
        clim :
            Color limits for the scalar values. If None, defaults to the min and max of
            the scalar values. If 'robust', uses the 2nd and 98th percentiles. If
            'symmetric', uses symmetric limits around zero.
        **kwargs :
            Additional keyword arguments to pass to [pyvista.Plotter.add_mesh][].

        See Also
        --------
        [pyvista.Plotter.add_mesh][]
        """
        if (
            morph.has_layer(layer_name)
            and morph.get_layer(layer_name).is_spatially_valid
        ):
            graph_layer = morph.get_layer(layer_name)
            lines = edges_to_lines(graph_layer.facets_positional)
            line_poly = pv.PolyData(graph_layer.vertices, lines=lines)
            scalars, clim = get_hue_info(graph_layer, hue, clim)
            return super().add_mesh(
                line_poly,
                scalars=scalars,
                clim=clim,
                scalar_bar_args={"title": hue} if isinstance(hue, str) else None,
                **kwargs,
            )

    def add_point_layer(
        self,
        morph: MorphSync,
        layer_name: str = "points",
        hue: Optional[str] = None,
        clim: Optional[tuple] = None,
        **kwargs,
    ) -> pv.Actor:
        """Add a point layer from a MorphSync object to the plotter.

        Parameters
        ----------
        morph :
            A MorphSync object containing the point layer.
        layer_name :
            The name of the point layer to add.
        hue :
            The name of the node attributes to use for coloring the points.
        clim :
            Color limits for the scalar values. If None, defaults to the min and max of
            the scalar values. If 'robust', uses the 2nd and 98th percentiles. If
            'symmetric', uses symmetric limits around zero.
        **kwargs :
            Additional keyword arguments to pass to [pyvista.Plotter.add_points][].

        See Also
        --------
        [pyvista.Plotter.add_points][]
        """
        if (
            morph.has_layer(layer_name)
            and morph.get_layer(layer_name).is_spatially_valid
        ):
            points_layer = morph.get_layer(layer_name)
            scalars, clim = get_hue_info(points_layer, hue, clim)

            return super().add_points(
                points_layer.vertices,
                scalars=scalars,
                clim=clim,
                scalar_bar_args={"title": hue} if isinstance(hue, str) else None,
                **kwargs,
            )
