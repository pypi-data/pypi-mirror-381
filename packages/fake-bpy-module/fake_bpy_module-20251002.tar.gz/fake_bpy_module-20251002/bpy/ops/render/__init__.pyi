import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def color_management_white_balance_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove a white balance preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def cycles_integrator_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add an Integrator Preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def cycles_performance_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add an Performance Preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def cycles_sampling_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add a Sampling Preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def cycles_viewport_sampling_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add a Viewport Sampling Preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def eevee_raytracing_preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove an EEVEE ray-tracing preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def opengl(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    animation: bool | None = False,
    render_keyed_only: bool | None = False,
    sequencer: bool | None = False,
    write_still: bool | None = False,
    view_context: bool | None = True,
) -> None:
    """Take a snapshot of the active viewport

    :type execution_context: int | str | None
    :type undo: bool | None
    :param animation: Animation, Render files from the animation range of this scene
    :type animation: bool | None
    :param render_keyed_only: Render Keyframes Only, Render only those frames where selected objects have a key in their animation data. Only used when rendering animation
    :type render_keyed_only: bool | None
    :param sequencer: Sequencer, Render using the sequencers OpenGL display
    :type sequencer: bool | None
    :param write_still: Write Image, Save the rendered image to the output path (used only when animation is disabled)
    :type write_still: bool | None
    :param view_context: View Context, Use the current 3D view for rendering, else use scene settings
    :type view_context: bool | None
    """

def play_rendered_anim(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Play back rendered frames/movies using an external player

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def preset_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_name: bool | None = False,
    remove_active: bool | None = False,
) -> None:
    """Add or remove a Render Preset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_name: remove_name
    :type remove_name: bool | None
    :param remove_active: remove_active
    :type remove_active: bool | None
    """

def render(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    animation: bool | None = False,
    write_still: bool | None = False,
    use_viewport: bool | None = False,
    layer: str = "",
    scene: str = "",
    start_frame: int | None = 0,
    end_frame: int | None = 0,
) -> None:
    """Render active scene

    :type execution_context: int | str | None
    :type undo: bool | None
    :param animation: Animation, Render files from the animation range of this scene
    :type animation: bool | None
    :param write_still: Write Image, Save the rendered image to the output path (used only when animation is disabled)
    :type write_still: bool | None
    :param use_viewport: Use 3D Viewport, When inside a 3D viewport, use layers and camera of the viewport
    :type use_viewport: bool | None
    :param layer: Render Layer, Single render layer to re-render (used only when animation is disabled)
    :type layer: str
    :param scene: Scene, Scene to render, current scene if not specified
    :type scene: str
    :param start_frame: Start Frame, Frame to start rendering animation at. If not specified, the scene start frame will be assumed. This should only be specified if doing an animation render
    :type start_frame: int | None
    :param end_frame: End Frame, Frame to end rendering animation at. If not specified, the scene end frame will be assumed. This should only be specified if doing an animation render
    :type end_frame: int | None
    """

def shutter_curve_preset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shape: typing.Literal["SHARP", "SMOOTH", "MAX", "LINE", "ROUND", "ROOT"]
    | None = "SMOOTH",
) -> None:
    """Set shutter curve

    :type execution_context: int | str | None
    :type undo: bool | None
    :param shape: Mode
    :type shape: typing.Literal['SHARP','SMOOTH','MAX','LINE','ROUND','ROOT'] | None
    """

def view_cancel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Cancel show render view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_show(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle show render view

    :type execution_context: int | str | None
    :type undo: bool | None
    """
