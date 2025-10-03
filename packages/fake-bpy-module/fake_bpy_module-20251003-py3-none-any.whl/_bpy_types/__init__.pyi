import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types
import mathutils

class AddonPreferences:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class AssetShelf:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class _GenericBone:
    """functions for bones, common between Armature/Pose/Edit bones.
    internal subclassing use only.
    """

    basename: typing.Any
    center: typing.Any
    children_recursive: typing.Any
    children_recursive_basename: typing.Any
    parent_recursive: typing.Any
    vector: typing.Any
    x_axis: typing.Any
    y_axis: typing.Any
    z_axis: typing.Any

    def parent_index(self, parent_test) -> None:
        """The same as bone in other_bone.parent_recursive
        but saved generating a list.

                :param parent_test:
        """

    def translate(self, vec) -> None:
        """Utility function to add vec to the head and tail of this bone.

        :param vec:
        """

class BoneCollection:
    bl_rna: typing.Any
    bones_recursive: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class Collection(bpy.types.ID):
    bl_rna: typing.Any
    children_recursive: typing.Any
    id_data: typing.Any
    users_dupli_group: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class Context:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def copy(self) -> dict[str, typing.Any]:
        """Get context members as a dictionary.

        :return:
        :rtype: dict[str, typing.Any]
        """

    def path_resolve(self, path: str, coerce: bool = True) -> None:
        """Returns the property from the path, raise an exception when not found.

        :param path: patch which this property resolves.
        :type path: str
        :param coerce: optional argument, when True, the property will be converted into its Python representation.
        :type coerce: bool
        """

    def temp_override(self) -> None:
        """Context manager to temporarily override members in the context.

        :return: The context manager .
        """

class FileHandler:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class Gizmo:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def draw_custom_shape(
        self,
        shape: typing.Any,
        *,
        matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
        | mathutils.Matrix
        | None = None,
        select_id: int | None = None,
    ) -> None:
        """Draw a shape created form `Gizmo.draw_custom_shape`.

                :param shape: The cached shape to draw.
                :type shape: typing.Any
                :param matrix: 4x4 matrix, when not given `Gizmo.matrix_world` is used.
                :type matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix | None
                :param select_id: The selection id.
        Only use when drawing within `Gizmo.draw_select`.
                :type select_id: int | None
        """

    @staticmethod
    def new_custom_shape(
        type: str, verts: collections.abc.Sequence[collections.abc.Sequence[float]]
    ) -> typing.Any:
        """Create a new shape that can be passed to `Gizmo.draw_custom_shape`.

        :param type: The type of shape to create in (POINTS, LINES, TRIS, LINE_STRIP).
        :type type: str
        :param verts: Sequence of 2D or 3D coordinates.
        :type verts: collections.abc.Sequence[collections.abc.Sequence[float]]
        :return: The newly created shape (the return type make change).
        :rtype: typing.Any
        """

class GizmoGroup:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class GreasePencilDrawing:
    bl_rna: typing.Any
    id_data: typing.Any
    strokes: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class _GenericUI:
    @classmethod
    def append(cls, draw_func) -> None:
        """Append a draw function to this menu,
        takes the same arguments as the menus draw function

                :param draw_func:
        """

    @classmethod
    def is_extended(cls) -> None: ...
    @classmethod
    def prepend(cls, draw_func) -> None:
        """Prepend a draw function to this menu, takes the same arguments as
        the menus draw function

                :param draw_func:
        """

    @classmethod
    def remove(cls, draw_func) -> None:
        """Remove a draw function that has been added to this menu.

        :param draw_func:
        """

class RenderEngine:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class KeyingSetInfo:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class Library(bpy.types.ID):
    bl_rna: typing.Any
    id_data: typing.Any
    users_id: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class Light(bpy.types.ID):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def cycles(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def inline_shader_nodes(self) -> None:
        """Get the inlined shader nodes of this light. This preprocesses the node tree
        to remove nested groups, repeat zones and more.

                :return: The inlined shader nodes.
        """

class Macro:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    @classmethod
    def define(cls, operator: str) -> bpy.types.OperatorMacro:
        """Append an operator to a registered macro class.

        :param operator: Identifier of the operator. This does not have to be defined when this function is called.
        :type operator: str
        :return: The operator macro for property access.
        :rtype: bpy.types.OperatorMacro
        """

class Material(bpy.types.ID):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def cycles(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def inline_shader_nodes(self) -> None:
        """Get the inlined shader nodes of this material. This preprocesses the node tree
        to remove nested groups, repeat zones and more.

                :return: The inlined shader nodes.
        """

class Mesh(bpy.types.ID):
    bl_rna: typing.Any
    edge_creases: typing.Any
    edge_keys: typing.Any
    id_data: typing.Any
    vertex_creases: typing.Any
    vertex_paint_mask: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def cycles(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def edge_creases_ensure(self) -> None: ...
    def edge_creases_remove(self) -> None: ...
    def from_pydata(
        self,
        vertices: collections.abc.Iterable[collections.abc.Sequence[float]],
        edges: collections.abc.Iterable[collections.abc.Sequence[int]],
        faces: collections.abc.Iterable[collections.abc.Sequence[int]],
        shade_flat=True,
    ) -> None:
        """Make a mesh from a list of vertices/edges/faces
        Until we have a nicer way to make geometry, use this.

                :param vertices: float triplets each representing (X, Y, Z)
        eg: [(0.0, 1.0, 0.5), ...].
                :type vertices: collections.abc.Iterable[collections.abc.Sequence[float]]
                :param edges: int pairs, each pair contains two indices to the
        vertices argument. eg: [(1, 2), ...]

        When an empty iterable is passed in, the edges are inferred from the polygons.
                :type edges: collections.abc.Iterable[collections.abc.Sequence[int]]
                :param faces: iterator of faces, each faces contains three or more indices to
        the vertices argument. eg: [(5, 6, 8, 9), (1, 2, 3), ...]
                :type faces: collections.abc.Iterable[collections.abc.Sequence[int]]
                :param shade_flat:
        """

    def shade_flat(self) -> None:
        """Render and display faces uniform, using face normals,
        setting the "sharp_face" attribute true for every face

        """

    def shade_smooth(self) -> None:
        """Render and display faces smooth, using interpolated vertex normals,
        removing the "sharp_face" attribute

        """

    def vertex_creases_ensure(self) -> None: ...
    def vertex_creases_remove(self) -> None: ...
    def vertex_paint_mask_ensure(self) -> None: ...
    def vertex_paint_mask_remove(self) -> None: ...

class MeshEdge:
    bl_rna: typing.Any
    id_data: typing.Any
    key: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class MeshLoopTriangle:
    bl_rna: typing.Any
    center: typing.Any
    edge_keys: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class MeshPolygon:
    bl_rna: typing.Any
    edge_keys: typing.Any
    id_data: typing.Any
    loop_indices: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class Node:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def is_registered_node_type(self, *args, **kwargs) -> None:
        """Node.is_registered_node_type()
        True if a registered node type

                :param args:
                :param kwargs:
        """

    @classmethod
    def poll(cls, _ntree) -> None:
        """

        :param _ntree:
        """

class NodeSocket:
    bl_rna: typing.Any
    id_data: typing.Any
    links: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class NodeTree(bpy.types.ID):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class NodeTreeInterfaceItem:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class Object(bpy.types.ID):
    bl_rna: typing.Any
    children: typing.Any
    children_recursive: typing.Any
    id_data: typing.Any
    users_collection: typing.Any
    users_scene: typing.Any

    def active_selection_set(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def cycles(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def evaluated_geometry(self) -> None:
        """Get the evaluated geometry set of this evaluated object. This only works for
        objects that contain geometry data like meshes and curves but not e.g. cameras.

                :return: The evaluated geometry.
        """

    def selection_sets(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

class Operator:
    bl_rna: typing.Any
    id_data: typing.Any

    def as_keywords(self, *, ignore=()) -> None:
        """Return a copy of the properties as a dictionary.

        :param ignore:
        """

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class PropertyGroup:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class Sound(bpy.types.ID):
    bl_rna: typing.Any
    factory: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class Text(bpy.types.ID):
    bl_rna: typing.Any
    id_data: typing.Any

    def as_module(self) -> None: ...
    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def region_as_string(self) -> str:
        """

        :return: The specified region as a string.
        :rtype: str
        """

    def region_from_string(self) -> None: ...

class Texture(bpy.types.ID):
    bl_rna: typing.Any
    id_data: typing.Any
    users_material: typing.Any
    users_object_modifier: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class USDHook:
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class WindowManager(bpy.types.ID):
    bl_rna: typing.Any
    clipboard: typing.Any
    id_data: typing.Any

    def addon_filter(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def addon_search(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def addon_support(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def addon_tags(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def asset_path_dummy(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    @classmethod
    def draw_cursor_add(cls) -> typing.Any:
        """Add a new draw cursor handler to this space type.
        It will be called every time the cursor for the specified region in the space type will be drawn.
        Note: All arguments are positional only for now.

                :return: Handler that can be removed later on.
                :rtype: typing.Any
        """

    @classmethod
    def draw_cursor_remove(cls) -> None:
        """Remove a draw cursor handler that was added previously."""

    def extension_search(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def extension_show_panel_available(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def extension_show_panel_installed(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def extension_tags(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def extension_type(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def fileselect_add(self, *args, **kwargs) -> None:
        """WindowManager.fileselect_add(operator)
        Opens a file selector with an operator.

                :param args:
                :param kwargs:
        """

    def gizmo_group_type_ensure(self, *args, **kwargs) -> None:
        """WindowManager.gizmo_group_type_ensure(identifier)
        Activate an existing widget group (when the persistent option isnt set)

                :param args:
                :param kwargs:
        """

    def gizmo_group_type_unlink_delayed(self, *args, **kwargs) -> None:
        """WindowManager.gizmo_group_type_unlink_delayed(identifier)
        Unlink a widget group (when the persistent option is set)

                :param args:
                :param kwargs:
        """

    def invoke_confirm(self, *args, **kwargs) -> None:
        """WindowManager.invoke_confirm(operator, event, title="", message="", confirm_text="", icon=NONE, text_ctxt="", translate=True)
        Operator confirmation popup (only to let user confirm the execution, no operator properties shown)

                :param args:
                :param kwargs:
        """

    def invoke_popup(self, *args, **kwargs) -> None:
        """WindowManager.invoke_popup(operator, width=300)
        Operator popup invoke (only shows operators properties, without executing it)

                :param args:
                :param kwargs:
        """

    def invoke_props_dialog(self, *args, **kwargs) -> None:
        """WindowManager.invoke_props_dialog(operator, width=300, title="", confirm_text="", cancel_default=False, text_ctxt="", translate=True)
        Operator dialog (non-autoexec popup) invoke (show operator properties and only execute it on click on OK button)

                :param args:
                :param kwargs:
        """

    def invoke_props_popup(self, *args, **kwargs) -> None:
        """WindowManager.invoke_props_popup(operator, event)
        Operator popup invoke (show operator properties and execute it automatically on changes)

                :param args:
                :param kwargs:
        """

    def invoke_search_popup(self, *args, **kwargs) -> None:
        """WindowManager.invoke_search_popup(operator)
        Operator search popup invoke which searches values of the operators `bpy.types.Operator.bl_property` (which must be an EnumProperty), executing it on confirmation

                :param args:
                :param kwargs:
        """

    def modal_handler_add(self, *args, **kwargs) -> None:
        """WindowManager.modal_handler_add(operator)
        Add a modal handler to the window manager, for the given modal operator (called by invoke() with self, just before returning {RUNNING_MODAL})

                :param args:
                :param kwargs:
        """

    def operator_properties_last(self, *args, **kwargs) -> None:
        """WindowManager.operator_properties_last(operator)
        operator_properties_last

                :param args:
                :param kwargs:
        """

    def piemenu_begin__internal(self, *args, **kwargs) -> None:
        """WindowManager.piemenu_begin__internal(title, icon=NONE, event=event)
        piemenu_begin__internal

                :param args:
                :param kwargs:
        """

    def piemenu_end__internal(self, *args, **kwargs) -> None:
        """WindowManager.piemenu_end__internal(menu)
        piemenu_end__internal

                :param args:
                :param kwargs:
        """

    def popmenu_begin__internal(self, *args, **kwargs) -> None:
        """WindowManager.popmenu_begin__internal(title, icon=NONE)
        popmenu_begin__internal

                :param args:
                :param kwargs:
        """

    def popmenu_end__internal(self, *args, **kwargs) -> None:
        """WindowManager.popmenu_end__internal(menu)
        popmenu_end__internal

                :param args:
                :param kwargs:
        """

    def popover(
        self, draw_func, *, ui_units_x=0, keymap=None, from_active_button=False
    ) -> None:
        """

        :param draw_func:
        :param ui_units_x:
        :param keymap:
        :param from_active_button:
        """

    def popover_begin__internal(self, *args, **kwargs) -> None:
        """WindowManager.popover_begin__internal(ui_units_x=0, from_active_button=False)
        popover_begin__internal

                :param args:
                :param kwargs:
        """

    def popover_end__internal(self, *args, **kwargs) -> None:
        """WindowManager.popover_end__internal(menu, keymap=None)
        popover_end__internal

                :param args:
                :param kwargs:
        """

    def popup_menu(self, draw_func, *, title="", icon="NONE") -> None:
        """

        :param draw_func:
        :param title:
        :param icon:
        """

    def popup_menu_pie(self, event, draw_func, *, title="", icon="NONE") -> None:
        """

        :param event:
        :param draw_func:
        :param title:
        :param icon:
        """

    def poselib_previous_action(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def preset_name(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def tag_script_reload(self, *args, **kwargs) -> None:
        """WindowManager.tag_script_reload()
        Tag for refreshing the interface after scripts have been reloaded

                :param args:
                :param kwargs:
        """

class WorkSpace(bpy.types.ID):
    bl_rna: typing.Any
    id_data: typing.Any

    def active_addon(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def status_text_set(self, text) -> None:
        """Set the status text or None to clear,
        When text is a function, this will be called with the (header, context) arguments.

                :param text:
        """

    def status_text_set_internal(self, *args, **kwargs) -> None:
        """WorkSpace.status_text_set_internal(text)
        Set the status bar text, typically key shortcuts for modal operators

                :param args:
                :param kwargs:
        """

class World(bpy.types.ID):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def cycles(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def cycles_visibility(self, *args, **kwargs) -> None:
        """Intermediate storage for properties before registration.

        :param args:
        :param kwargs:
        """

    def inline_shader_nodes(self) -> None:
        """Get the inlined shader nodes of this world. This preprocesses the node tree
        to remove nested groups, repeat zones and more.

                :return: The inlined shader nodes.
        """

class _RNAMeta:
    is_registered: typing.Any

class Bone(_GenericBone):
    """functions for bones, common between Armature/Pose/Edit bones.
    internal subclassing use only.
    """

    basename: typing.Any
    bl_rna: typing.Any
    center: typing.Any
    children_recursive: typing.Any
    children_recursive_basename: typing.Any
    id_data: typing.Any
    parent_recursive: typing.Any
    vector: typing.Any
    x_axis: typing.Any
    y_axis: typing.Any
    z_axis: typing.Any

    def AxisRollFromMatrix(self, *args, **kwargs) -> None:
        """Bone.AxisRollFromMatrix(matrix, axis=(0, 0, 0))
        Convert a rotational matrix to the axis + roll representation. Note that the resulting value of the roll may not be as expected if the matrix has shear or negative determinant.

                :param args:
                :param kwargs:
        """

    def MatrixFromAxisRoll(self, *args, **kwargs) -> None:
        """Bone.MatrixFromAxisRoll(axis, roll)
        Convert the axis + roll representation to a matrix

                :param args:
                :param kwargs:
        """

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class EditBone(_GenericBone):
    """functions for bones, common between Armature/Pose/Edit bones.
    internal subclassing use only.
    """

    basename: typing.Any
    bl_rna: typing.Any
    center: typing.Any
    children: typing.Any
    children_recursive: typing.Any
    children_recursive_basename: typing.Any
    id_data: typing.Any
    parent_recursive: typing.Any
    vector: typing.Any
    x_axis: typing.Any
    y_axis: typing.Any
    z_axis: typing.Any

    def align_orientation(self, other) -> None:
        """Align this bone to another by moving its tail and settings its roll
        the length of the other bone is not used.

                :param other:
        """

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def transform(
        self,
        matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
        | mathutils.Matrix,
        *,
        scale: bool = True,
        roll: bool = True,
    ) -> None:
        """Transform the bones head, tail, roll and envelope
        (when the matrix has a scale component).

                :param matrix: 3x3 or 4x4 transformation matrix.
                :type matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix
                :param scale: Scale the bone envelope by the matrix.
                :type scale: bool
                :param roll: Correct the roll to point in the same relative
        direction to the head and tail.
                :type roll: bool
        """

class PoseBone(_GenericBone):
    """functions for bones, common between Armature/Pose/Edit bones.
    internal subclassing use only.
    """

    basename: typing.Any
    bl_rna: typing.Any
    center: typing.Any
    children: typing.Any
    children_recursive: typing.Any
    children_recursive_basename: typing.Any
    id_data: typing.Any
    parent_recursive: typing.Any
    vector: typing.Any
    x_axis: typing.Any
    y_axis: typing.Any
    z_axis: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class Header(_GenericUI):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class Menu(_GenericUI):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    @classmethod
    def draw_collapsible(cls, context, layout) -> None:
        """

        :param context:
        :param layout:
        """

    def draw_preset(self, _context) -> None:
        """Define these on the subclass:
        - preset_operator (string)
        - preset_subdir (string)Optionally:
        - preset_add_operator (string)
        - preset_extensions (set of strings)
        - preset_operator_defaults (dict of keyword args)

                :param _context:
        """

    def path_menu(
        self,
        searchpaths: collections.abc.Sequence[str],
        operator: str,
        *,
        props_default: dict[str, typing.Any] | None = None,
        prop_filepath: str = "filepath",
        filter_ext: None | collections.abc.Callable[str, bool] | None = None,
        filter_path=None,
        display_name: collections.abc.Callable[str, str] | None = None,
        add_operator=None,
        add_operator_props=None,
    ) -> None:
        """Populate a menu from a list of paths.

                :param searchpaths: Paths to scan.
                :type searchpaths: collections.abc.Sequence[str]
                :param operator: The operator id to use with each file.
                :type operator: str
                :param props_default: Properties to assign to each operator.
                :type props_default: dict[str, typing.Any] | None
                :param prop_filepath: Optional operator filepath property (defaults to "filepath").
                :type prop_filepath: str
                :param filter_ext: Optional callback that takes the file extensions.

        Returning false excludes the file from the list.
                :type filter_ext: None | collections.abc.Callable[str, bool] | None
                :param filter_path:
                :param display_name: Optional callback that takes the full path, returns the name to display.
                :type display_name: collections.abc.Callable[str, str] | None
                :param add_operator:
                :param add_operator_props:
        """

class Panel(_GenericUI):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class UIList(_GenericUI):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class HydraRenderEngine(RenderEngine):
    bl_delegate_id: typing.Any
    bl_rna: typing.Any
    bl_use_shading_nodes_custom: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def get_render_settings(self, engine_type) -> None:
        """Provide render settings for HdRenderDelegate.

        :param engine_type:
        """

    def render(self, depsgraph) -> None:
        """

        :param depsgraph:
        """

    def update(self, data, depsgraph) -> None:
        """

        :param data:
        :param depsgraph:
        """

    def view_draw(self, context, depsgraph) -> None:
        """

        :param context:
        :param depsgraph:
        """

    def view_update(self, context, depsgraph) -> None:
        """

        :param context:
        :param depsgraph:
        """

class NodeInternal(Node):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def is_registered_node_type(self, *args, **kwargs) -> None:
        """Node.is_registered_node_type()
        True if a registered node type

                :param args:
                :param kwargs:
        """

    def poll(self, *args, **kwargs) -> None:
        """NodeInternal.poll(node_tree)
        If non-null output is returned, the node type can be added to the tree

                :param args:
                :param kwargs:
        """

class NodeTreeInterfaceSocket(NodeTreeInterfaceItem):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class _RNAMetaPropGroup(_RNAMeta):
    is_registered: typing.Any

class CompositorNode(NodeInternal):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def is_registered_node_type(self, *args, **kwargs) -> None:
        """Node.is_registered_node_type()
        True if a registered node type

                :param args:
                :param kwargs:
        """

    @classmethod
    def poll(cls, ntree) -> None:
        """NodeInternal.poll(node_tree)
        If non-null output is returned, the node type can be added to the tree

                :param ntree:
        """

    def update(self) -> None: ...

class GeometryNode(NodeInternal):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def is_registered_node_type(self, *args, **kwargs) -> None:
        """Node.is_registered_node_type()
        True if a registered node type

                :param args:
                :param kwargs:
        """

    @classmethod
    def poll(cls, ntree) -> None:
        """NodeInternal.poll(node_tree)
        If non-null output is returned, the node type can be added to the tree

                :param ntree:
        """

class ShaderNode(NodeInternal):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def is_registered_node_type(self, *args, **kwargs) -> None:
        """Node.is_registered_node_type()
        True if a registered node type

                :param args:
                :param kwargs:
        """

    @classmethod
    def poll(cls, ntree) -> None:
        """NodeInternal.poll(node_tree)
        If non-null output is returned, the node type can be added to the tree

                :param ntree:
        """

class TextureNode(NodeInternal):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def is_registered_node_type(self, *args, **kwargs) -> None:
        """Node.is_registered_node_type()
        True if a registered node type

                :param args:
                :param kwargs:
        """

    @classmethod
    def poll(cls, ntree) -> None:
        """NodeInternal.poll(node_tree)
        If non-null output is returned, the node type can be added to the tree

                :param ntree:
        """
