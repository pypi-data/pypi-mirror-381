"""
Browser-based plotting GUI for soil/foundation/piles using PyVista + trame.
Redesigned based on working test.py patterns for better reliability.

Install requirements if missing:
    pip install pyvista trame trame-vtk trame-vuetify
"""

from __future__ import annotations
from typing import Optional
import os
import json
import numpy as np


class SoilFoundationPlotter:
    """
    Browser-based GUI for fast visualization of soil layers, foundation blocks,
    and piles using PyVista + trame. Based on reliable patterns from test.py.
    """

    def __init__(
        self,
        structure_info: Optional[dict] = None,
        soil_info: Optional[dict] = None,
        foundation_info: Optional[dict] = None,
        pile_info: Optional[dict] = None,
        info_file: Optional[str] = None,
        server_name: str = "soil_foundation_plotter",
        port: int = 8080,
        title: str = "Soil/Foundation Plotter",
    ) -> None:
        try:
            import pyvista as pv
        except Exception as exc:
            raise RuntimeError(
                "pyvista is required for SoilFoundationPlotter."
            ) from exc

        self.pv = pv
        self.title = title
        self.port = port
        
        # Load configuration data
        (
            self.structure_info,
            self.soil_info,
            self.foundation_info,
            self.pile_info,
        ) = self._load_infos(structure_info, soil_info, foundation_info, pile_info, info_file)
        
        # In-memory cached actual meshes (no disk persistence)
        self._actual_soil = None
        self._actual_pile = None
        self._actual_foundation = None
        self._scalars = ["Mesh", "Core", "Region", "ElementTag", "MaterialTag"]
        # Optional public aliases
        # self.actual_soil = None
        # self.actual_pile = None
        # self.actual_foundation = None
        self._discretized_exists = False
        # Extra actors toggled from UI
        self._axes_actor = None
        self._grid_actor = None

        # Handle mesh file
        mesh_file = self.structure_info.get("mesh_file", None) if self.structure_info else None
        if mesh_file == "" or (mesh_file and not os.path.isfile(mesh_file)):
            mesh_file = None
            print("Warning: mesh file is not a valid file")
        self._mesh_file = mesh_file

        # Configure PyVista for web rendering
        pv.OFF_SCREEN = True
        pv.set_plot_theme("document")

        # Initialize PyVista plotter with proper settings for web
        self.plotter = pv.Plotter(
            off_screen=True,
            notebook=False,
            window_size=(1000, 700)
        )
        self.plotter.background_color = "white"

        # Store references to added objects
        self.objects = {}
        
        # State defaults
        self.state_defaults = {
            "show_soil": True,
            "soil_opacity": 0.35,
            "show_foundation": True,
            "foundation_opacity": 0.55,
            "show_piles": True,
            "piles_opacity": 1.0,
            "show_mesh": bool(mesh_file),
            "mesh_opacity": 1.0,
            "discretized": self._discretized_exists,
            "show_axes": False,
            "show_grid": False,
            "selected_scalar": "Mesh",
        }

        # Setup server
        self._setup_server(server_name)
        
        # Pre-populate scene
        self.quick_plot()

    def _setup_server(self, server_name: str):
        """Setup the trame server and UI"""
        try:
            from trame.app import get_server
            import trame_vuetify as _tv
            
            # Get Vuetify version
            _tv_ver = getattr(_tv, "__version__", "2.0.0")
            _tv_major = int(str(_tv_ver).split(".")[0])
            
            self.server = get_server(server_name)
            
            # Configure client type based on Vuetify version
            if _tv_major >= 3:
                self.server.client_type = "vue3"
                from trame.ui.vuetify3 import SinglePageWithDrawerLayout
                from trame.widgets import vuetify3 as vuetify
            else:
                self.server.client_type = "vue2"
                from trame.ui.vuetify import SinglePageWithDrawerLayout
                from trame.widgets import vuetify
                
            from trame.widgets import html, vtk as vtk_widgets
            
        except Exception as exc:
            raise RuntimeError(
                "SoilFoundationPlotter requires 'trame' stack. Install with: "
                "pip install trame trame-vtk trame-vuetify"
            ) from exc

        state, ctrl = self.server.state, self.server.controller
        
        # Initialize state variables
        state.update(self.state_defaults)
        # Provide scalar items via state to avoid string-splitting in VSelect
        try:
            state.scalars = list(self._scalars)
        except Exception:
            state.scalars = ["None", "Core", "Region", "ElementTag", "MaterialTag"]
        # Visual styles for toggle buttons
        try:
            state.show_axes_variant = "text"
            state.show_axes_color = "grey"
            state.show_grid_variant = "text"
            state.show_grid_color = "grey"
        except Exception:
            pass
        
        # Define controller methods
        @ctrl.set("quick_plot")
        def quick_plot_handler():
            self.quick_plot()
            
        @ctrl.set("actual_plot")
        def actual_plot_handler():
            self.actual_plot()
            
        @ctrl.set("discretize")
        def discretize_handler():
            self.discretize_and_save()
            
        @ctrl.set("clear_all")
        def clear_all_handler():
            self.clear_all()
            
        @ctrl.set("reset_camera")
        def reset_camera_handler():
            self.reset_camera()

        # Camera view helpers
        @ctrl.set("view_iso")
        def view_iso_handler():
            try:
                self.plotter.camera_position = "iso"
            except Exception:
                try:
                    self.plotter.view_isometric()
                except Exception:
                    pass
            self.update_view()

        @ctrl.set("view_xy")
        def view_xy_handler():
            try:
                self.plotter.view_xy()
            except Exception:
                try:
                    self.plotter.camera_position = "xy"
                except Exception:
                    pass
            self.update_view()

        @ctrl.set("view_xz")
        def view_xz_handler():
            try:
                self.plotter.view_xz()
            except Exception:
                try:
                    self.plotter.camera_position = "xz"
                except Exception:
                    pass
            self.update_view()

        @ctrl.set("view_yz")
        def view_yz_handler():
            try:
                self.plotter.view_yz()
            except Exception:
                try:
                    self.plotter.camera_position = "yz"
                except Exception:
                    pass
            self.update_view()

        # Simple toggle helpers for small icon buttons
        @ctrl.set("toggle_axes")
        def toggle_axes_handler():
            try:
                self.server.state.show_axes = not bool(getattr(self.server.state, "show_axes", False))
                if hasattr(self.server.state, "flush"):
                    self.server.state.flush("show_axes")
            except Exception:
                pass

        @ctrl.set("toggle_grid")
        def toggle_grid_handler():
            try:
                self.server.state.show_grid = not bool(getattr(self.server.state, "show_grid", False))
                if hasattr(self.server.state, "flush"):
                    self.server.state.flush("show_grid")
            except Exception:
                pass

        # State change handlers
        @state.change("show_soil", "show_foundation", "show_piles", "show_mesh")
        def on_visibility_change(**kwargs):
            self._apply_visibility()
            
        @state.change("soil_opacity", "foundation_opacity", "piles_opacity", "mesh_opacity")
        def on_opacity_change(**kwargs):
            self._apply_opacity()

        @state.change("selected_scalar")
        def on_scalar_change(selected_scalar, **kwargs):
            if self._discretized_exists:
                try:
                    self.actual_plot(selected_scalar)
                except Exception as e:
                    print(f"Scalar change error: {e}")

        @state.change("show_axes")
        def on_show_axes_change(show_axes, **kwargs):
            try:
                if bool(show_axes):
                    try:
                        # Prefer explicit boolean toggle if supported
                        self.plotter.show_axes(True)
                    except TypeError:
                        # Older versions: calling without args enables
                        self.plotter.show_axes()
                    except Exception:
                        # Fallback to adding an axes actor in-scene
                        if self._axes_actor is None:
                            self._axes_actor = self.plotter.add_axes()
                    # update styles
                    if hasattr(self.server, 'state'):
                        self.server.state.show_axes_variant = "elevated"
                        self.server.state.show_axes_color = "primary"
                else:
                    hid_ok = False
                    try:
                        # Prefer explicit boolean toggle off
                        self.plotter.show_axes(False)
                        hid_ok = True
                    except Exception:
                        pass
                    if not hid_ok:
                        try:
                            # Some versions expose hide_axes()
                            self.plotter.hide_axes()
                            hid_ok = True
                        except Exception:
                            pass
                    if not hid_ok and self._axes_actor is not None:
                        # Last resort: try removing stored actor
                        try:
                            self.plotter.remove_actor(self._axes_actor)
                        except Exception:
                            pass
                        self._axes_actor = None
                    # update styles
                    if hasattr(self.server, 'state'):
                        self.server.state.show_axes_variant = "text"
                        self.server.state.show_axes_color = "grey"
            except Exception as e:
                print(f"Axes toggle error: {e}")
            self.update_view()

        @state.change("show_grid")
        def on_show_grid_change(show_grid, **kwargs):
            try:
                if bool(show_grid):
                    try:
                        # Most versions simply enable with no args
                        self.plotter.show_grid()
                    except TypeError:
                        # Some versions allow explicit boolean
                        self.plotter.show_grid(True)
                    except Exception:
                        # Fallback try returning actor
                        try:
                            self._grid_actor = self.plotter.show_grid(return_actor=True)
                        except Exception:
                            self._grid_actor = None
                    # update styles
                    if hasattr(self.server, 'state'):
                        self.server.state.show_grid_variant = "elevated"
                        self.server.state.show_grid_color = "primary"
                else:
                    removed = False
                    try:
                        # Proper API to remove bounds axes grid
                        self.plotter.remove_bounds_axes()
                        removed = True
                    except Exception:
                        pass
                    if not removed:
                        try:
                            # Some versions allow disabling grid this way
                            self.plotter.show_grid(False)
                            removed = True
                        except Exception:
                            pass
                    if not removed and self._grid_actor is not None:
                        try:
                            self.plotter.remove_actor(self._grid_actor)
                            removed = True
                        except Exception:
                            pass
                        self._grid_actor = None
                    # update styles
                    if hasattr(self.server, 'state'):
                        self.server.state.show_grid_variant = "text"
                        self.server.state.show_grid_color = "grey"
            except Exception as e:
                print(f"Grid toggle error: {e}")
            self.update_view()

        # Create the layout
        with SinglePageWithDrawerLayout(self.server) as layout:
            layout.title.set_text(self.title)
            layout.icon.click = ctrl.reset_camera

            with layout.drawer:
                # Action buttons
                vuetify.VDivider()
                vuetify.VBtn(
                    "Quick Plot", 
                    color="primary", 
                    click=ctrl.quick_plot, 
                    block=True,
                    prepend_icon="mdi-chart-scatter-plot" if _tv_major >= 3 else None
                )
                vuetify.VBtn(
                    "Discretize",
                    color="success",
                    click=ctrl.discretize,
                    block=True,
                    classes="mt-2",
                    disabled=("discretized", self._discretized_exists),
                    prepend_icon="mdi-cube-scan" if _tv_major >= 3 else None
                )
                vuetify.VBtn(
                    "Actual Plot",
                    color="success",
                    click=ctrl.actual_plot,
                    block=True,
                    classes="mt-2",
                    prepend_icon="mdi-cube-outline" if _tv_major >= 3 else None
                )
                vuetify.VBtn(
                    "Reset Camera",
                    color="secondary",
                    click=ctrl.reset_camera,
                    block=True,
                    classes="mt-2",
                    prepend_icon="mdi-camera-outline" if _tv_major >= 3 else None
                )
                vuetify.VBtn(
                    "Clear All",
                    color="error",
                    click=ctrl.clear_all,
                    block=True,
                    classes="mt-2",
                    prepend_icon="mdi-delete" if _tv_major >= 3 else None
                )

                # Visibility controls
                vuetify.VDivider(classes="my-3")
                html.Div("Visibility", classes="text-subtitle-2 mt-1 mb-1")
                vuetify.VSwitch(
                    v_model=("show_soil", self.state_defaults["show_soil"]), 
                    label="Show Soil", 
                    dense=True
                )
                vuetify.VSwitch(
                    v_model=("show_foundation", self.state_defaults["show_foundation"]), 
                    label="Show Foundation", 
                    dense=True
                )
                vuetify.VSwitch(
                    v_model=("show_piles", self.state_defaults["show_piles"]), 
                    label="Show Piles", 
                    dense=True
                )
                vuetify.VSwitch(
                    v_model=("show_mesh", self.state_defaults["show_mesh"]), 
                    label="Show Building", 
                    dense=True
                )

                # Opacity controls
                vuetify.VDivider(classes="my-3")
                html.Div("Opacity", classes="text-subtitle-2 mt-1 mb-1")
                vuetify.VSlider(
                    v_model=("soil_opacity", self.state_defaults["soil_opacity"]), 
                    min=0.0, 
                    max=1.0, 
                    step=0.05, 
                    label="Soil", 
                    hide_details=True
                )
                vuetify.VSlider(
                    v_model=("foundation_opacity", self.state_defaults["foundation_opacity"]), 
                    min=0.0, 
                    max=1.0, 
                    step=0.05, 
                    label="Foundation", 
                    hide_details=True
                )
                vuetify.VSlider(
                    v_model=("piles_opacity", self.state_defaults["piles_opacity"]), 
                    min=0.0, 
                    max=1.0, 
                    step=0.05, 
                    label="Piles", 
                    hide_details=True
                )
                vuetify.VSlider(
                    v_model=("mesh_opacity", self.state_defaults["mesh_opacity"]), 
                    min=0.0, 
                    max=1.0, 
                    step=0.05, 
                    label="Building", 
                    hide_details=True
                )

                # Scalar selection
                vuetify.VDivider(classes="my-3")
                html.Div("Scalar coloring", classes="text-subtitle-2 mt-1 mb-1")
                vuetify.VSelect(
                    v_model=("selected_scalar", self.state_defaults["selected_scalar"]),
                    label="Scalars",
                    items=("scalars", self._scalars),
                    dense=True,
                    clearable=True,
                )

                # Object count display
                vuetify.VDivider(classes="my-3")
                vuetify.VChip(
                    f"Objects: {len(self.objects)}",
                    color="info",
                    variant="elevated" if _tv_major >= 3 else "default",
                    classes="ma-1"
                )

                # Bottom-left compact tools (axes/grid toggles and camera views)
                from trame.widgets import html as _html  # local alias to avoid confusion
                with _html.Div(style="position: absolute; left: 12px; bottom: 12px; z-index: 10;"):
                    # Grid container for two rows, spaced buttons
                    with _html.Div(style="display: grid; grid-template-columns: repeat(3, max-content); gap: 10px 12px;"):
                        if _tv_major >= 3:
                            vuetify.VBtn(
                                icon="mdi-axis-arrow",
                                size="large",
                                variant=("show_axes_variant", "text"),
                                color=("show_axes_color", "grey"),
                                click=ctrl.toggle_axes,
                            )
                            vuetify.VBtn(
                                icon="mdi-grid",
                                size="large",
                                variant=("show_grid_variant", "text"),
                                color=("show_grid_color", "grey"),
                                click=ctrl.toggle_grid,
                            )
                            vuetify.VBtn(
                                icon="mdi-cube-scan",
                                size="large",
                                color="secondary",
                                click=ctrl.view_iso,
                            )
                            vuetify.VBtn(
                                icon="mdi-axis-z-arrow",
                                size="large",
                                color="secondary",
                                click=ctrl.view_xy,
                            )
                            vuetify.VBtn(
                                icon="mdi-axis-y-arrow",
                                size="large",
                                color="secondary",
                                click=ctrl.view_xz,
                            )
                            vuetify.VBtn(
                                icon="mdi-axis-x-arrow",
                                size="large",
                                color="secondary",
                                click=ctrl.view_yz,
                            )
                        else:
                            # Vuetify v2 buttons, larger and spaced
                            vuetify.VBtn(
                                icon=True,
                                large=True,
                                depressed=("show_axes", False),
                                color=("show_axes_color", "grey"),
                                click=ctrl.toggle_axes,
                                children=[vuetify.VIcon("mdi-axis-arrow")] 
                            )
                            vuetify.VBtn(
                                icon=True,
                                large=True,
                                depressed=("show_grid", False),
                                color=("show_grid_color", "grey"),
                                click=ctrl.toggle_grid,
                                children=[vuetify.VIcon("mdi-grid")] 
                            )
                            vuetify.VBtn(
                                icon=True,
                                large=True,
                                color="secondary",
                                click=ctrl.view_iso,
                                children=[vuetify.VIcon("mdi-cube-scan")] 
                            )
                            vuetify.VBtn(
                                icon=True,
                                large=True,
                                color="secondary",
                                click=ctrl.view_xy,
                                children=[vuetify.VIcon("mdi-axis-z-arrow")] 
                            )
                            vuetify.VBtn(
                                icon=True,
                                large=True,
                                color="secondary",
                                click=ctrl.view_xz,
                                children=[vuetify.VIcon("mdi-axis-y-arrow")] 
                            )
                            vuetify.VBtn(
                                icon=True,
                                large=True,
                                color="secondary",
                                click=ctrl.view_yz,
                                children=[vuetify.VIcon("mdi-axis-x-arrow")] 
                            )

            with layout.content:
                with vuetify.VContainer(fluid=True, classes="pa-0 fill-height"):
                    # Create the VTK view
                    self.html_view = vtk_widgets.VtkRemoteView(
                        self.plotter.ren_win,
                        ref="view",
                        interactive_ratio=1,
                        interactive_quality=60,
                        still_quality=98,
                        style="width: 100%; height: 100vh;",
                    )
                    
                    # Set controller methods for view updates
                    ctrl.view_update = self.html_view.update
                    ctrl.view_reset_camera = self.html_view.reset_camera

    def quick_plot(self) -> None:
        """Fast scene build: soil/foundation as boxes, piles as cylinders."""
        print("Building quick plot...")
        
        # Clear existing objects
        self.clear_all()

        # Soil layers as boxes with khaki color palette
        if self.soil_info is not None and "soil_profile" in self.soil_info:
            self._add_soil_layers()

        # Foundation blocks as boxes
        if self.foundation_info is not None and "foundation_profile" in self.foundation_info:
            self._add_foundation_blocks()

        # Piles as cylinders
        if self.pile_info is not None and "pile_profile" in self.pile_info:
            self._add_piles()

        # Optional mesh file
        if self._mesh_file:
            self._add_mesh_file()

        # Apply current visibility and opacity settings
        self._apply_visibility()
        self._apply_opacity()
        
        # Reset camera and update view
        self.reset_camera()
        self.update_view()
        print(f"Quick plot complete. Total objects: {len(self.objects)}")


    def _add_soil_layers(self):
        """Add soil layers to the scene"""
        khaki_colors = [
            "#F0E68C", "#DEB887", "#D2B48C", "#BDB76B", "#F4A460", "#CD853F",
            "#A0522D", "#8B7355", "#6B8E23", "#556B2F", "#8FBC8F", "#9ACD32",
        ]
        
        x_min = self.soil_info.get("x_min", 0.0)
        x_max = self.soil_info.get("x_max", 0.0)
        y_min = self.soil_info.get("y_min", 0.0)
        y_max = self.soil_info.get("y_max", 0.0)
        
        for idx, layer in enumerate(self.soil_info["soil_profile"]):
            z_bot = layer.get("z_bot", 0.0)
            z_top = layer.get("z_top", 0.0)
            if z_top <= z_bot:
                continue
                
            center = ((x_min + x_max) * 0.5, (y_min + y_max) * 0.5, (z_bot + z_top) * 0.5)
            x_len = max(1e-6, x_max - x_min)
            y_len = max(1e-6, y_max - y_min)
            z_len = max(1e-6, z_top - z_bot)
            
            box = self.pv.Cube(center=center, x_length=x_len, y_length=y_len, z_length=z_len)
            soil_color = khaki_colors[idx % len(khaki_colors)]
            
            name = f"soil_{idx}"
            actor = self.plotter.add_mesh(
                box,
                name=name,
                color=soil_color,
                opacity=self.state_defaults["soil_opacity"],
                smooth_shading=False,
                show_edges=True,
            )
            self.objects[name] = {
                "mesh": box, 
                "actor": actor, 
                "type": "soil", 
                "layer": idx
            }

    def _add_foundation_blocks(self):
        """Add foundation blocks to the scene"""
        for fidx, f in enumerate(self.foundation_info["foundation_profile"]):
            try:
                x_min, x_max = f["x_min"], f["x_max"]
                y_min, y_max = f["y_min"], f["y_max"]
                z_bot, z_top = f["z_bot"], f["z_top"]
            except KeyError:
                continue
                
            if x_max <= x_min or y_max <= y_min or z_top <= z_bot:
                continue
                
            center = ((x_min + x_max) * 0.5, (y_min + y_max) * 0.5, (z_bot + z_top) * 0.5)
            box = self.pv.Cube(
                center=center,
                x_length=max(1e-6, x_max - x_min),
                y_length=max(1e-6, y_max - y_min),
                z_length=max(1e-6, z_top - z_bot),
            )
            
            name = f"foundation_{fidx}"
            actor = self.plotter.add_mesh(
                box,
                name=name,
                color="#A27EA8",
                opacity=self.state_defaults["foundation_opacity"],
                smooth_shading=False,
                show_edges=True,
            )
            self.objects[name] = {
                "mesh": box, 
                "actor": actor, 
                "type": "foundation", 
                "index": fidx
            }

    def _add_piles(self):
        """Add piles to the scene (supports single and grid definitions)"""
        pidx = 0
        for pile in self.pile_info["pile_profile"]:
            ptype = str(pile.get("type", "single")).lower()
            
            if ptype == "grid":
                pidx = self._add_pile_grid(pile, pidx)
            else:
                pidx = self._add_single_pile(pile, pidx)

    def _add_pile_grid(self, pile, pidx):
        """Add a grid of piles"""
        try:
            x_start = float(pile["x_start"])
            y_start = float(pile["y_start"])
            spacing_x = float(pile["spacing_x"])
            spacing_y = float(pile["spacing_y"])
            nx = int(pile["nx"])
            ny = int(pile["ny"])
            z_top = float(pile["z_top"])
            z_bot = float(pile["z_bot"])
            radius = float(pile.get("r", 0.2))
        except (KeyError, ValueError):
            return pidx
            
        if nx < 1 or ny < 1 or spacing_x <= 0 or spacing_y <= 0:
            return pidx
            
        height = abs(z_top - z_bot)
        direction = (0.0, 0.0, z_top - z_bot)
        
        for i in range(nx):
            for j in range(ny):
                x = x_start + i * spacing_x
                y = y_start + j * spacing_y
                center = (x, y, (z_top + z_bot) * 0.5)
                
                cyl = self.pv.Cylinder(
                    center=center, 
                    direction=direction, 
                    radius=max(1e-6, radius), 
                    height=max(1e-6, height), 
                    resolution=24
                )
                
                name = f"pile_{pidx}"
                actor = self.plotter.add_mesh(
                    cyl,
                    name=name,
                    color="#55AA66",
                    opacity=self.state_defaults["piles_opacity"],
                    smooth_shading=True,
                    show_edges=True,
                )
                self.objects[name] = {
                    "mesh": cyl, 
                    "actor": actor, 
                    "type": "pile", 
                    "index": pidx,
                    "grid_pos": (i, j)
                }
                pidx += 1
                
        return pidx

    def _add_single_pile(self, pile, pidx):
        """Add a single pile"""
        try:
            x_top = float(pile["x_top"])
            y_top = float(pile["y_top"])
            z_top = float(pile["z_top"])
            x_bot = float(pile.get("x_bot", x_top))
            y_bot = float(pile.get("y_bot", y_top))
            z_bot = float(pile.get("z_bot", z_top - 1.0))
            radius = float(pile.get("r", 0.2))
        except (KeyError, ValueError):
            return pidx + 1
            
        direction = (x_top - x_bot, y_top - y_bot, z_top - z_bot)
        height = (direction[0]**2 + direction[1]**2 + direction[2]**2) ** 0.5
        center = ((x_top + x_bot) * 0.5, (y_top + y_bot) * 0.5, (z_top + z_bot) * 0.5)
        
        cyl = self.pv.Cylinder(
            center=center, 
            direction=direction, 
            radius=max(1e-6, radius), 
            height=max(1e-6, height), 
            resolution=24
        )
        
        name = f"pile_{pidx}"
        actor = self.plotter.add_mesh(
            cyl,
            name=name,
            color="#55AA66",
            opacity=self.state_defaults["piles_opacity"],
            smooth_shading=True,
            show_edges=True,
        )
        self.objects[name] = {
            "mesh": cyl, 
            "actor": actor, 
            "type": "pile", 
            "index": pidx
        }
        
        return pidx + 1

    def _add_mesh_file(self):
        """Add mesh file to the scene"""
        try:
            mesh = self.pv.read(self._mesh_file)
            name = "mesh_file"
            actor = self.plotter.add_mesh(
                mesh,
                name=name,
                color="#333333",
                opacity=self.state_defaults["mesh_opacity"],
                show_edges=True,
                render_lines_as_tubes=True,
                line_width=2.0,
            )
            self.objects[name] = {
                "mesh": mesh, 
                "actor": actor, 
                "type": "mesh"
            }
        except Exception as e:
            print(f"Failed to load mesh file {self._mesh_file}: {e}")

    def clear_all(self):
        """Clear all objects from the plotter"""
        self.plotter.clear()
        self.objects.clear()
        self.update_view()
        print("Cleared all objects")

    def reset_camera(self):
        """Reset the camera to default position"""
        self.plotter.reset_camera()
        self.plotter.camera_position = "iso"
        self.update_view()

    def _apply_visibility(self):
        """Apply visibility settings based on current state"""
        if not hasattr(self.server, 'state'):
            return
            
        state = self.server.state
        vis_map = {
            "soil": getattr(state, "show_soil", True),
            "foundation": getattr(state, "show_foundation", True),
            "pile": getattr(state, "show_piles", True),
            "mesh": getattr(state, "show_mesh", True),
        }
        
        for name, obj_data in self.objects.items():
            obj_type = obj_data["type"]
            if obj_type in vis_map:
                try:
                    actor = obj_data["actor"]
                    actor.SetVisibility(1 if vis_map[obj_type] else 0)
                except Exception as e:
                    print(f"Error setting visibility for {name}: {e}")
        
        self.update_view()

    def _apply_opacity(self):
        """Apply opacity settings based on current state"""
        if not hasattr(self.server, 'state'):
            return
            
        state = self.server.state
        opa_map = {
            "soil": getattr(state, "soil_opacity", 0.35),
            "foundation": getattr(state, "foundation_opacity", 0.55),
            "pile": getattr(state, "piles_opacity", 1.0),
            "mesh": getattr(state, "mesh_opacity", 0.3),
        }
        
        for name, obj_data in self.objects.items():
            obj_type = obj_data["type"]
            if obj_type in opa_map:
                try:
                    actor = obj_data["actor"]
                    opacity = max(0.0, min(1.0, opa_map[obj_type]))
                    actor.GetProperty().SetOpacity(opacity)
                except Exception as e:
                    print(f"Error setting opacity for {name}: {e}")
        
        self.update_view()

    def update_view(self):
        """Update the 3D view"""
        try:
            if hasattr(self, 'html_view'):
                self.html_view.update()
        except Exception as e:
            print(f"View update error (normal during initialization): {e}")

    def _load_infos(
        self,
        structure_info: Optional[dict],
        soil_info: Optional[dict],
        foundation_info: Optional[dict],
        pile_info: Optional[dict],
        info_file: Optional[str],
    ):
        """Load configuration from file or use provided dicts"""
        if info_file is not None and (not structure_info or not soil_info or not foundation_info or not pile_info):
            if not os.path.isfile(info_file):
                raise FileNotFoundError(f"info_file not found: {info_file}")
            with open(info_file, "r") as f:
                info = json.load(f)
            structure_info = structure_info or info.get("structure_info", None)
            soil_foundation_info = info.get("soil_foundation_info", {})
            soil_info = soil_info or soil_foundation_info.get("soil_info", None)
            foundation_info = foundation_info or soil_foundation_info.get("foundation_info", None)
            pile_info = pile_info or soil_foundation_info.get("pile_info", None)
        return structure_info, soil_info, foundation_info, pile_info

    def start_server(self, **kwargs):
        """Start the trame server"""
        print(f"Starting Soil Foundation Plotter on port {self.port}")
        print(f"Open browser to: http://localhost:{self.port}")
        print("Press Ctrl+C to stop the server")
        
        self.server.start(port=self.port, **kwargs)

    def get_object_list(self):
        """Get a list of all objects in the scene"""
        return list(self.objects.keys())

    def get_object_info(self, name):
        """Get information about a specific object"""
        return self.objects.get(name, None)

    def remove_object(self, name):
        """Remove a specific object by name"""
        if name in self.objects:
            self.plotter.remove_actor(name)
            del self.objects[name]
            self.update_view()
            print(f"Removed object: {name}")


    def actual_plot(self, scalar = None):
        """Build and render the actual meshes returned by the model builder."""
        # Clear existing scene
        self.clear_all()
        if scalar == "Mesh" or scalar == "None":
            scalar = None

        # If already computed, reuse in-memory cached meshes; otherwise compute once
        pile_mesh, foundation_mesh, soil_mesh = None, None, None
        if self._discretized_exists and self._actual_soil is not None:
            pile_mesh = self._actual_pile
            foundation_mesh = self._actual_foundation
            soil_mesh = self._actual_soil
        else:
            pile_mesh, foundation_mesh, soil_mesh = self._compute_actual_meshes()
            if pile_mesh is None and foundation_mesh is None and soil_mesh is None:
                return
            # Cache in memory and mark as discretized
            self._actual_pile = pile_mesh
            self._actual_foundation = foundation_mesh
            self._actual_soil = soil_mesh
            # self.actual_pile = pile_mesh
            # self.actual_foundation = foundation_mesh
            # self.actual_soil = soil_mesh
            self._discretized_exists = True
            try:
                if hasattr(self, 'server'):
                    self.server.state.discretized = True
                    if hasattr(self.server.state, 'flush'):
                        self.server.state.flush()
            except Exception:
                pass

        # Add meshes to the scene with appropriate types
        try:
            if soil_mesh is not None and soil_mesh.n_cells > 0:
                soil_actor = self.plotter.add_mesh(
                    soil_mesh,
                    name="soil_mesh",
                    color="#C2B280",  # khaki-like
                    opacity=self.state_defaults["soil_opacity"],
                    show_edges=True,
                    scalars=scalar,
                )
                self.objects["soil_mesh"] = {
                    "mesh": soil_mesh,
                    "actor": soil_actor,
                    "type": "soil",
                }

            if foundation_mesh is not None and foundation_mesh.n_cells > 0:
                foundation_actor = self.plotter.add_mesh(
                    foundation_mesh,
                    name="foundation_mesh",
                    color="grey",
                    opacity=self.state_defaults["foundation_opacity"],
                    show_edges=True,
                    scalars=scalar,
                )
                self.objects["foundation_mesh"] = {
                    "mesh": foundation_mesh,
                    "actor": foundation_actor,
                    "type": "foundation",
                }

            if pile_mesh is not None and pile_mesh.n_cells > 0:
                pile_actor = self.plotter.add_mesh(
                    pile_mesh,
                    name="pile_mesh",
                    color="#55AA66",
                    opacity=self.state_defaults["piles_opacity"],
                    show_edges=True,
                    scalars=scalar,
                    render_lines_as_tubes=True,
                    line_width=6.0,
                )
                self.objects["pile_mesh"] = {
                    "mesh": pile_mesh,
                    "actor": pile_actor,
                    "type": "pile",
                }
        except Exception as exc:
            print(f"Error adding actual meshes: {exc}")

        # Optional building mesh from file
        if self._mesh_file:
            self._add_mesh_file()

        # Apply current toggles and opacities
        self._apply_visibility()
        self._apply_opacity()

        # Reset camera and update
        self.reset_camera()
        self.update_view()

    


    def _compute_actual_meshes(self):
        """Compute the actual meshes using the model builder."""
        try:
            from femora.components.simcenter.eeuq.soil_foundation_type_one import soil_foundation_type_one
            return soil_foundation_type_one(
                structure_info=self.structure_info,
                soil_info=self.soil_info,
                foundation_info=self.foundation_info,
                pile_info=self.pile_info,
                plotting=True,
            )
            
            
        except Exception as exc:
            print(f"Discretization failed: {exc}")
            return None, None, None

    def _check_discretized_exists(self) -> bool:
        """Check if meshes are cached in memory (no disk)."""
        return self._actual_soil is not None and self._actual_pile is not None and self._actual_foundation is not None

    def _save_discretized(self, pile_mesh, foundation_mesh, soil_mesh):
        """No-op: we keep meshes in memory only based on user request."""
        self._actual_pile = pile_mesh
        self._actual_foundation = foundation_mesh
        self._actual_soil = soil_mesh
        # self.actual_pile = pile_mesh
        # self.actual_foundation = foundation_mesh
        # self.actual_soil = soil_mesh

    def _load_discretized(self):
        """Return already-cached meshes from memory."""
        return self._actual_pile, self._actual_foundation, self._actual_soil

    def discretize_and_save(self):
        """One-time discretization: compute and cache in memory, then disable the button forever."""
        if self._discretized_exists:
            print("Discretized meshes already exist. Skipping.")
            return
        pile_mesh, foundation_mesh, soil_mesh = self._compute_actual_meshes()
        if pile_mesh is None and foundation_mesh is None and soil_mesh is None:
            return
        self._save_discretized(pile_mesh, foundation_mesh, soil_mesh)
        self._discretized_exists = True
        try:
            if hasattr(self, 'server'):
                self.server.state.discretized = True
                if hasattr(self.server.state, 'flush'):
                    self.server.state.flush()
        except Exception:
            pass
                                

# Example usage
if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(__file__)) 
    structure_info = {
        "num_partitions": 1,
        "x_min": -13.716,
        "y_min": -13.716,
        "z_min": 0.,
        "x_max": 13.716,
        "y_max": 13.716,
        "z_max": 40.8432,
        "columns_base":[
            {"tag":101, "x":-13.71600, "y":-13.71600,  "z":0.00000 },
            {"tag":102, "x":-4.57200,  "y":-13.71600,  "z":0.00000 },
            {"tag":103, "x":4.57200,   "y":-13.71600,  "z":0.00000 },
            {"tag":104, "x":13.71600,  "y":-13.71600,  "z":0.00000 },
            {"tag":105, "x":-13.71600, "y":-4.57200,   "z":0.00000 },
            {"tag":106, "x":-4.57200,  "y":-4.57200,   "z":0.00000 },
            {"tag":107, "x":4.57200,   "y":-4.57200,   "z":0.00000 },
            {"tag":108, "x":13.71600,  "y":-4.57200,   "z":0.00000 },
            {"tag":109, "x":-13.71600, "y":4.57200,    "z":0.00000 },
            {"tag":110, "x":-4.57200,  "y":4.57200,    "z":0.00000 },
            {"tag":111, "x":4.57200,   "y":4.57200,    "z":0.00000 },
            {"tag":112, "x":13.71600,  "y":4.57200,    "z":0.00000 },
            {"tag":113, "x":-13.71600, "y":13.71600,   "z":0.00000 },
            {"tag":114, "x":-4.57200,  "y":13.71600,   "z":0.00000 },
            {"tag":115, "x":4.57200,   "y":13.71600,   "z":0.00000 },
            {"tag":116, "x":13.71600,  "y":13.71600,   "z":0.00000 },
        ],  
        "model_file":r"steel_frame_tcl", 
        "mesh_file" :r"building.vtkhdf",
    }


    # soil information from bottom to top
    soil_info = {
        "x_min": -64,
        "x_max":  64,
        "y_min": -64,
        "y_max":  64,
        "nx": 32,
        "ny": 32,
        "gravity_x": 0.0,
        "gravity_y": 0.0,
        "gravity_z": -9.81,
        "num_partitions": 8,
        "boundary_conditions": "periodic", # could be "DRM" 
        "DRM_options": {
            "absorbing_layer_type": "PML",  # could be "PML" or "Rayleigh" 
            "num_partitions": 8,
            "number_of_layers": 5,
            "Rayleigh_damping": 0.95,
            "match_damping": False, # if true the Rayleigh damping will be matched to the soil damping
        },
        "soil_profile" : [
        {"z_bot":-48, "z_top":-40, "nz":2, 
        "material":"Elastic", 
        "mat_props":[2031050.557968521, 0.306925827695258, 2.16275], 
        "damping":"Frequency-Rayleigh", "damping_props":[0.0211, 3, 15]
        },
        {"z_bot":-40,  "z_top":-32, "nz":2, 
        "material":"Elastic", 
        "mat_props":[1762809.8758694725, 0.30694522251297574, 2.1586],
        "damping":"Frequency-Rayleigh", "damping_props":[0.0221, 3, 15]
        },
        {"z_bot":-32,  "z_top":-24, "nz":2, 
        "material":"Elastic", 
        "mat_props":[1495388.2483252182, 0.306974948361342, 2.15445],
        "damping":"Frequency-Rayleigh", "damping_props":[0.0234, 3, 15]
        },
        {"z_bot":-24,  "z_top":-16,  "nz":2, 
        "material":"Elastic", 
        "mat_props":[1229028.6525414723, 0.30699478245814293, 2.15035],
        "damping":"Frequency-Rayleigh", "damping_props":[0.0249, 3, 15]
        },  
        {"z_bot":-16,  "z_top":-8,  "nz":2, 
        "material":"Elastic", 
        "mat_props":[963419.3475957835, 0.3070002901446228, 2.1462],
        "damping":"Frequency-Rayleigh", "damping_props":[0.0269, 3, 15]
        },
        {"z_bot":-8,  "z_top":0,  "nz":2, 
        "material":"Elastic",
        "mat_props":[698103.0346931004, 0.30696660596216024, 2.14205],
        "damping":"Frequency-Rayleigh", "damping_props":[0.0296, 3, 15]  
        }   
        ]
    }



    # foundation information
    foundation_info = {
        "gravity_x": 0.0,
        "gravity_y": 0.0,
        "gravity_z": -9.81, 
        "embedded" : True,  # if the foundation is embedded in the soil or not True/False.
        "dx": 2.0,          # mesh size in x direction
        "dy": 2.0,          # mesh size in y direction
        "dz": 0.3,          # mesh size in z direction
        "gravity_x": 0.0,
        "gravity_y": 0.0,
        "gravity_z": -9.81,
        "num_partitions": 2,
        "column_embedment_depth":0.3, # embedment depth of the columns in the foundation
        "column_section_props":{
            "E": 30e6,    # Elastic Modulus
            "A": 0.282,     # Area
            "Iy": 0.0063585, # Moment of Inertia Iy
            "Iz": 0.0063585, # Moment of Inertia Iz
            "G": 12.5e6,   # Shear Modulus
            "J": 0.012717   # Moment of Inertia J
        },

        "foundation_profile" : [
            {"x_min":-20,  "x_max":20, 
            "y_min":-20,  "y_max":20,  
            "z_top":0,    "z_bot":-1.2, 
            "material":"Elastic", "mat_props":[30e6, 0.2, 2.4] 
            },
        ]
    }


    # pile information
    pile_info = {
        "pile_profile" : [
            {
                "type": "grid",  # could be "grid" or "single"
                "x_start": -10 , "y_start": -10 ,
                "spacing_x": 5 , "spacing_y": 5 ,
                "nx": 5 , "ny": 5 ,
                "z_top": -0.5 , "z_bot": -10 ,
                "nz": 15 ,"r":0.3, "section": "No-Section", 
                "material":"Elastic", 
                "mat_props":[30e6, 0.282, 0.0063585, 0.0063585, 12.5e6, 0.012717], 
                "transformation": ["Linear", 0.0, 1.0, 0.0]
            },
        ],

        "pile_interface": {
            "num_points_on_perimeter": 8,   # number of points on the perimeter of the pile interface
            "num_points_along_length": 4,   # number of points along the length of the pile interface
            "penalty_parameter": 1.0e12
        },
    }
    

    # Create and start the plotter
    plotter = SoilFoundationPlotter(
        structure_info=structure_info,
        soil_info=soil_info,
        foundation_info=foundation_info,
        pile_info=pile_info,
        port=8081
    )
    
    plotter.start_server()

