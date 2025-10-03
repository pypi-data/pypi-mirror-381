import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def assign_default_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set this propertys current value as the new default

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def button_execute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    skip_depressed: bool | None = False,
) -> None:
    """Presses active button

    :type execution_context: int | str | None
    :type undo: bool | None
    :param skip_depressed: Skip Depressed
    :type skip_depressed: bool | None
    """

def button_string_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unsets the text of the active button

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def copy_as_driver_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a new driver with this property as input, and copy it to the internal clipboard. Use Paste Driver to add it to the target property, or Paste Driver Variables to extend an existing driver

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def copy_data_path_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    full_path: bool | None = False,
) -> None:
    """Copy the RNA data path for this property to the clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    :param full_path: full_path, Copy full data path
    :type full_path: bool | None
    """

def copy_driver_to_selected_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
) -> None:
    """Copy the propertys driver from the active item to the same property of all selected items, if the same property exists

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Copy to selected the drivers of all elements of the array
    :type all: bool | None
    """

def copy_python_command_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the Python command matching this button

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def copy_to_selected_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
) -> None:
    """Copy the propertys value from the active item to the same property of all selected items if the same property exists

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Copy to selected all elements of the array
    :type all: bool | None
    """

def drop_color(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    color: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0, 0.0),
    gamma: bool | None = False,
    has_alpha: bool | None = False,
) -> None:
    """Drop colors to buttons

    :type execution_context: int | str | None
    :type undo: bool | None
    :param color: Color, Source color
    :type color: collections.abc.Iterable[float] | None
    :param gamma: Gamma Corrected, The source color is gamma corrected
    :type gamma: bool | None
    :param has_alpha: Has Alpha, The source color contains an Alpha component
    :type has_alpha: bool | None
    """

def drop_material(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    session_uid: int | None = 0,
) -> None:
    """Drag material to Material slots in Properties

    :type execution_context: int | str | None
    :type undo: bool | None
    :param session_uid: Session UID, Session UID of the data-block to use by the operator
    :type session_uid: int | None
    """

def drop_name(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    string: str = "",
) -> None:
    """Drop name to button

    :type execution_context: int | str | None
    :type undo: bool | None
    :param string: String, The string value to drop into the button
    :type string: str
    """

def editsource(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Edit UI source code of the active button

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def eyedropper_bone(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Sample a bone from the 3D View or the Outliner to store in a property

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def eyedropper_color(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    prop_data_path: str = "",
) -> None:
    """Sample a color from the Blender window to store in a property

    :type execution_context: int | str | None
    :type undo: bool | None
    :param prop_data_path: Data Path, Path of property to be set with the depth
    :type prop_data_path: str
    """

def eyedropper_colorramp(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Sample a color band

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def eyedropper_colorramp_point(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Point-sample a color band

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def eyedropper_depth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    prop_data_path: str = "",
) -> None:
    """Sample depth from the 3D view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param prop_data_path: Data Path, Path of property to be set with the depth
    :type prop_data_path: str
    """

def eyedropper_driver(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mapping_type: typing.Literal[
        "SINGLE_MANY", "DIRECT", "MATCH", "NONE_ALL", "NONE_SINGLE"
    ]
    | None = "SINGLE_MANY",
) -> None:
    """Pick a property to use as a driver target

        :type execution_context: int | str | None
        :type undo: bool | None
        :param mapping_type: Mapping Type, Method used to match target and driven properties

    SINGLE_MANY
    All from Target -- Drive all components of this property using the target picked.

    DIRECT
    Single from Target -- Drive this component of this property using the target picked.

    MATCH
    Match Indices -- Create drivers for each pair of corresponding elements.

    NONE_ALL
    Manually Create Later -- Create drivers for all properties without assigning any targets yet.

    NONE_SINGLE
    Manually Create Later (Single) -- Create driver for this property only and without assigning any targets yet.
        :type mapping_type: typing.Literal['SINGLE_MANY','DIRECT','MATCH','NONE_ALL','NONE_SINGLE'] | None
    """

def eyedropper_grease_pencil_color(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["MATERIAL", "PALETTE", "BRUSH"] | None = "MATERIAL",
    material_mode: typing.Literal["STROKE", "FILL", "BOTH"] | None = "STROKE",
) -> None:
    """Sample a color from the Blender Window and create Grease Pencil material

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['MATERIAL','PALETTE','BRUSH'] | None
    :param material_mode: Material Mode
    :type material_mode: typing.Literal['STROKE','FILL','BOTH'] | None
    """

def eyedropper_id(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Sample a data-block from the 3D View to store in a property

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def jump_to_target_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Switch to the target object or bone

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def list_start_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Start entering filter text for the list in focus

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def override_add_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
) -> None:
    """Create an override operation

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Add overrides for all elements of the array
    :type all: bool | None
    """

def override_idtemplate_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete the selected local override and relink its usages to the linked data-block if possible, else reset it and mark it as non editable

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def override_idtemplate_make(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Create a local override of the selected linked data-block, and its hierarchy of dependencies

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def override_idtemplate_reset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset the selected local override to its linked reference values

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def override_remove_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
) -> None:
    """Remove an override operation

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Reset to default values all elements of the array
    :type all: bool | None
    """

def reloadtranslation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Force a full reload of UI translation

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def reset_default_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
) -> None:
    """Reset this propertys value to its default value

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Reset to default values all elements of the array
    :type all: bool | None
    """

def unset_property_button(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear the property and use default or generated value in operators

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_drop(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Drag and drop onto a data-set or item within the data-set

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_item_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete selected list item

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_item_rename(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Rename the active item in the data-set view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_item_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    wait_to_deselect_others: bool | None = False,
    use_select_on_click: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
    extend: bool | None = False,
    range_select: bool | None = False,
) -> None:
    """Activate selected view item

    :type execution_context: int | str | None
    :type undo: bool | None
    :param wait_to_deselect_others: Wait to Deselect Others
    :type wait_to_deselect_others: bool | None
    :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if theres drag event. Otherwise select on mouse release
    :type use_select_on_click: bool | None
    :param mouse_x: Mouse X
    :type mouse_x: int | None
    :param mouse_y: Mouse Y
    :type mouse_y: int | None
    :param extend: extend, Extend Selection
    :type extend: bool | None
    :param range_select: Range Select, Select all between clicked and active items
    :type range_select: bool | None
    """

def view_scroll(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_start_filter(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Start entering filter text for the data-set in focus

    :type execution_context: int | str | None
    :type undo: bool | None
    """
