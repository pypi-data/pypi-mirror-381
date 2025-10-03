import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.stub_internal.rna_enums
import bpy.types

def active_frame_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
) -> None:
    """Delete the active Grease Pencil frame(s)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: Delete all, Delete active keyframes of all layers
    :type all: bool | None
    """

def bake_grease_pencil_animation(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame_start: int | None = 1,
    frame_end: int | None = 250,
    step: int | None = 1,
    only_selected: bool | None = False,
    frame_target: int | None = 1,
    project_type: typing.Literal["KEEP", "FRONT", "SIDE", "TOP", "VIEW", "CURSOR"]
    | None = "KEEP",
) -> None:
    """Bake Grease Pencil object transform to Grease Pencil keyframes

        :type execution_context: int | str | None
        :type undo: bool | None
        :param frame_start: Start Frame, The start frame
        :type frame_start: int | None
        :param frame_end: End Frame, The end frame of animation
        :type frame_end: int | None
        :param step: Step, Step between generated frames
        :type step: int | None
        :param only_selected: Only Selected Keyframes, Convert only selected keyframes
        :type only_selected: bool | None
        :param frame_target: Target Frame, Destination frame
        :type frame_target: int | None
        :param project_type: Projection Type

    KEEP
    No Reproject.

    FRONT
    Front -- Reproject the strokes using the X-Z plane.

    SIDE
    Side -- Reproject the strokes using the Y-Z plane.

    TOP
    Top -- Reproject the strokes using the X-Y plane.

    VIEW
    View -- Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using Cursor Stroke Placement.

    CURSOR
    Cursor -- Reproject the strokes using the orientation of 3D cursor.
        :type project_type: typing.Literal['KEEP','FRONT','SIDE','TOP','VIEW','CURSOR'] | None
    """

def brush_stroke(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
    pen_flip: bool | None = False,
) -> None:
    """Draw a new stroke in the active Grease Pencil object

        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :type mode: typing.Literal['NORMAL','INVERT','SMOOTH','ERASE'] | None
        :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used
        :type pen_flip: bool | None
    """

def caps_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["ROUND", "FLAT", "START", "END"] | None = "ROUND",
) -> None:
    """Change curve caps mode (rounded or flat)

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    ROUND
    Rounded -- Set as default rounded.

    FLAT
    Flat.

    START
    Toggle Start.

    END
    Toggle End.
        :type type: typing.Literal['ROUND','FLAT','START','END'] | None
    """

def clean_loose(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    limit: int | None = 1,
) -> None:
    """Remove loose points

    :type execution_context: int | str | None
    :type undo: bool | None
    :param limit: Limit, Number of points to consider stroke as loose
    :type limit: int | None
    """

def convert_curve_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.CurvesTypeItems | None = "POLY",
    threshold: float | None = 0.01,
) -> None:
    """Convert type of selected curves

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy.stub_internal.rna_enums.CurvesTypeItems | None
    :param threshold: Threshold, The distance that the resulting points are allowed to be within
    :type threshold: float | None
    """

def copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the selected Grease Pencil points or strokes to the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def cyclical_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CLOSE", "OPEN", "TOGGLE"] | None = "TOGGLE",
    subdivide_cyclic_segment: bool | None = True,
) -> None:
    """Close or open the selected stroke adding a segment from last to first point

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['CLOSE','OPEN','TOGGLE'] | None
    :param subdivide_cyclic_segment: Match Point Density, Add point in the new segment to keep the same density
    :type subdivide_cyclic_segment: bool | None
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete selected strokes or points

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete_breakdown(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove breakdown frames generated by interpolating between two Grease Pencil frames

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["ACTIVE_FRAME", "ALL_FRAMES"] | None = "ACTIVE_FRAME",
) -> None:
    """Delete Grease Pencil Frame(s)

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Method used for deleting Grease Pencil frames

    ACTIVE_FRAME
    Active Frame -- Deletes current frame in the active layer.

    ALL_FRAMES
    All Active Frames -- Delete active frames for all layers.
        :type type: typing.Literal['ACTIVE_FRAME','ALL_FRAMES'] | None
    """

def dissolve(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["POINTS", "BETWEEN", "UNSELECT"] | None = "POINTS",
) -> None:
    """Delete selected points without splitting strokes

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Method used for dissolving stroke points

    POINTS
    Dissolve -- Dissolve selected points.

    BETWEEN
    Dissolve Between -- Dissolve points between selected points.

    UNSELECT
    Dissolve Unselect -- Dissolve all unselected points.
        :type type: typing.Literal['POINTS','BETWEEN','UNSELECT'] | None
    """

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Duplicate the selected points

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    GREASE_PENCIL_OT_duplicate: typing.Any | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Make copies of the selected Grease Pencil strokes and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param GREASE_PENCIL_OT_duplicate: Duplicate, Duplicate the selected points
    :type GREASE_PENCIL_OT_duplicate: typing.Any | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def erase_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
) -> None:
    """Erase points in the box region

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    """

def erase_lasso(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
) -> None:
    """Erase points in the lasso region

    :type execution_context: int | str | None
    :type undo: bool | None
    :param path: Path
    :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
    :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
    :type use_smooth_stroke: bool | None
    :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
    :type smooth_stroke_factor: float | None
    :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
    :type smooth_stroke_radius: int | None
    """

def extrude(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Extrude the selected points

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def extrude_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    GREASE_PENCIL_OT_extrude: typing.Any | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Extrude selected points and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param GREASE_PENCIL_OT_extrude: Extrude Stroke Points, Extrude the selected points
    :type GREASE_PENCIL_OT_extrude: typing.Any | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def fill(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    invert: bool | None = False,
    precision: bool | None = False,
) -> None:
    """Fill with color the shape formed by strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param invert: Invert, Find boundary of unfilled instead of filled regions
    :type invert: bool | None
    :param precision: Precision, Use precision movement for extension lines
    :type precision: bool | None
    """

def frame_clean_duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    selected: bool | None = False,
) -> None:
    """Remove any keyframe that is a duplicate of the previous one

    :type execution_context: int | str | None
    :type undo: bool | None
    :param selected: Selected, Only delete selected keyframes
    :type selected: bool | None
    """

def frame_duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
) -> None:
    """Make a copy of the active Grease Pencil frame(s)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: Duplicate all, Duplicate active keyframes of all layer
    :type all: bool | None
    """

def insert_blank_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all_layers: bool | None = False,
    duration: int | None = 0,
) -> None:
    """Insert a blank frame on the current scene frame

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all_layers: All Layers, Insert a blank frame in all editable layers
    :type all_layers: bool | None
    :param duration: Duration
    :type duration: int | None
    """

def interpolate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shift: float | None = 0.0,
    layers: typing.Literal["ACTIVE", "ALL"] | None = "ACTIVE",
    exclude_breakdowns: bool | None = False,
    use_selection: bool | None = False,
    flip: typing.Literal["NONE", "FLIP", "AUTO"] | None = "AUTO",
    smooth_steps: int | None = 1,
    smooth_factor: float | None = 0.0,
) -> None:
    """Interpolate Grease Pencil strokes between frames

    :type execution_context: int | str | None
    :type undo: bool | None
    :param shift: Shift, Bias factor for which frame has more influence on the interpolated strokes
    :type shift: float | None
    :param layers: Layer, Layers included in the interpolation
    :type layers: typing.Literal['ACTIVE','ALL'] | None
    :param exclude_breakdowns: Exclude Breakdowns, Exclude existing Breakdowns keyframes as interpolation extremes
    :type exclude_breakdowns: bool | None
    :param use_selection: Use Selection, Use only selected strokes for interpolating
    :type use_selection: bool | None
    :param flip: Flip Mode, Invert destination stroke to match start and end with source stroke
    :type flip: typing.Literal['NONE','FLIP','AUTO'] | None
    :param smooth_steps: Iterations, Number of times to smooth newly created strokes
    :type smooth_steps: int | None
    :param smooth_factor: Smooth, Amount of smoothing to apply to interpolated strokes, to reduce jitter/noise
    :type smooth_factor: float | None
    """

def interpolate_sequence(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    step: int | None = 1,
    layers: typing.Literal["ACTIVE", "ALL"] | None = "ACTIVE",
    exclude_breakdowns: bool | None = False,
    use_selection: bool | None = False,
    flip: typing.Literal["NONE", "FLIP", "AUTO"] | None = "AUTO",
    smooth_steps: int | None = 1,
    smooth_factor: float | None = 0.0,
    type: typing.Literal[
        "LINEAR",
        "CUSTOM",
        "SINE",
        "QUAD",
        "CUBIC",
        "QUART",
        "QUINT",
        "EXPO",
        "CIRC",
        "BACK",
        "BOUNCE",
        "ELASTIC",
    ]
    | None = "LINEAR",
    easing: bpy.stub_internal.rna_enums.BeztripleInterpolationEasingItems
    | None = "EASE_IN",
    back: float | None = 1.702,
    amplitude: float | None = 0.15,
    period: float | None = 0.15,
) -> None:
    """Generate in-betweens to smoothly interpolate between Grease Pencil frames

        :type execution_context: int | str | None
        :type undo: bool | None
        :param step: Step, Number of frames between generated interpolated frames
        :type step: int | None
        :param layers: Layer, Layers included in the interpolation
        :type layers: typing.Literal['ACTIVE','ALL'] | None
        :param exclude_breakdowns: Exclude Breakdowns, Exclude existing Breakdowns keyframes as interpolation extremes
        :type exclude_breakdowns: bool | None
        :param use_selection: Use Selection, Use only selected strokes for interpolating
        :type use_selection: bool | None
        :param flip: Flip Mode, Invert destination stroke to match start and end with source stroke
        :type flip: typing.Literal['NONE','FLIP','AUTO'] | None
        :param smooth_steps: Iterations, Number of times to smooth newly created strokes
        :type smooth_steps: int | None
        :param smooth_factor: Smooth, Amount of smoothing to apply to interpolated strokes, to reduce jitter/noise
        :type smooth_factor: float | None
        :param type: Type, Interpolation method to use the next time Interpolate Sequence is run

    LINEAR
    Linear -- Straight-line interpolation between A and B (i.e. no ease in/out).

    CUSTOM
    Custom -- Custom interpolation defined using a curve map.

    SINE
    Sinusoidal -- Sinusoidal easing (weakest, almost linear but with a slight curvature).

    QUAD
    Quadratic -- Quadratic easing.

    CUBIC
    Cubic -- Cubic easing.

    QUART
    Quartic -- Quartic easing.

    QUINT
    Quintic -- Quintic easing.

    EXPO
    Exponential -- Exponential easing (dramatic).

    CIRC
    Circular -- Circular easing (strongest and most dynamic).

    BACK
    Back -- Cubic easing with overshoot and settle.

    BOUNCE
    Bounce -- Exponentially decaying parabolic bounce, like when objects collide.

    ELASTIC
    Elastic -- Exponentially decaying sine wave, like an elastic band.
        :type type: typing.Literal['LINEAR','CUSTOM','SINE','QUAD','CUBIC','QUART','QUINT','EXPO','CIRC','BACK','BOUNCE','ELASTIC'] | None
        :param easing: Easing, Which ends of the segment between the preceding and following Grease Pencil frames easing interpolation is applied to
        :type easing: bpy.stub_internal.rna_enums.BeztripleInterpolationEasingItems | None
        :param back: Back, Amount of overshoot for back easing
        :type back: float | None
        :param amplitude: Amplitude, Amount to boost elastic bounces for elastic easing
        :type amplitude: float | None
        :param period: Period, Time between bounces for elastic easing
        :type period: float | None
    """

def join_selection(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["JOINSTROKES", "SPLITCOPY", "SPLIT"] | None = "JOINSTROKES",
) -> None:
    """New stroke from selected points/strokes

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Defines how the operator will behave on the selection in the active layer

    JOINSTROKES
    Join Strokes -- Join the selected strokes into one stroke.

    SPLITCOPY
    Split and Copy -- Copy the selected points to a new stroke.

    SPLIT
    Split -- Split the selected point to a new stroke.
        :type type: typing.Literal['JOINSTROKES','SPLITCOPY','SPLIT'] | None
    """

def layer_active(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    layer: int | None = 0,
) -> None:
    """Set the active Grease Pencil layer

    :type execution_context: int | str | None
    :type undo: bool | None
    :param layer: Grease Pencil Layer
    :type layer: int | None
    """

def layer_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    new_layer_name: str = "Layer",
) -> None:
    """Add a new Grease Pencil layer in the active object

    :type execution_context: int | str | None
    :type undo: bool | None
    :param new_layer_name: Name, Name of the new layer
    :type new_layer_name: str
    """

def layer_duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    empty_keyframes: bool | None = False,
) -> None:
    """Make a copy of the active Grease Pencil layer

    :type execution_context: int | str | None
    :type undo: bool | None
    :param empty_keyframes: Empty Keyframes, Add Empty Keyframes
    :type empty_keyframes: bool | None
    """

def layer_duplicate_object(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_active: bool | None = True,
    mode: typing.Literal["ALL", "ACTIVE"] | None = "ALL",
) -> None:
    """Make a copy of the active Grease Pencil layer to selected object

    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_active: Only Active, Copy only active Layer, uncheck to append all layers
    :type only_active: bool | None
    :param mode: Mode
    :type mode: typing.Literal['ALL','ACTIVE'] | None
    """

def layer_group_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    new_layer_group_name: str = "",
) -> None:
    """Add a new Grease Pencil layer group in the active object

    :type execution_context: int | str | None
    :type undo: bool | None
    :param new_layer_group_name: Name, Name of the new layer group
    :type new_layer_group_name: str
    """

def layer_group_color_tag(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    color_tag: typing.Literal[
        "NONE",
        "COLOR1",
        "COLOR2",
        "COLOR3",
        "COLOR4",
        "COLOR5",
        "COLOR6",
        "COLOR7",
        "COLOR8",
    ]
    | None = "COLOR1",
) -> None:
    """Change layer group icon

    :type execution_context: int | str | None
    :type undo: bool | None
    :param color_tag: Color Tag
    :type color_tag: typing.Literal['NONE','COLOR1','COLOR2','COLOR3','COLOR4','COLOR5','COLOR6','COLOR7','COLOR8'] | None
    """

def layer_group_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_children: bool | None = False,
) -> None:
    """Remove Grease Pencil layer group in the active object

    :type execution_context: int | str | None
    :type undo: bool | None
    :param keep_children: Keep children nodes, Keep the children nodes of the group and only delete the group itself
    :type keep_children: bool | None
    """

def layer_hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Hide selected/unselected Grease Pencil layers

    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected layers
    :type unselected: bool | None
    """

def layer_isolate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    affect_visibility: bool | None = False,
) -> None:
    """Make only active layer visible/editable

    :type execution_context: int | str | None
    :type undo: bool | None
    :param affect_visibility: Affect Visibility, Also affect the visibility
    :type affect_visibility: bool | None
    """

def layer_lock_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    lock: bool | None = True,
) -> None:
    """Lock all Grease Pencil layers to prevent them from being accidentally modified

    :type execution_context: int | str | None
    :type undo: bool | None
    :param lock: Lock Value, Lock/Unlock all layers
    :type lock: bool | None
    """

def layer_mask_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
) -> None:
    """Add new layer as masking

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Layer, Name of the layer
    :type name: str
    """

def layer_mask_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove Layer Mask

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def layer_mask_reorder(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Reorder the active Grease Pencil mask layer up/down in the list

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def layer_merge(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["ACTIVE", "GROUP", "ALL"] | None = "ACTIVE",
) -> None:
    """Combine layers based on the mode into one layer

        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    ACTIVE
    Active -- Combine the active layer with the layer just below (if it exists).

    GROUP
    Group -- Combine layers in the active group into a single layer.

    ALL
    All -- Combine all layers into a single layer.
        :type mode: typing.Literal['ACTIVE','GROUP','ALL'] | None
    """

def layer_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move the active Grease Pencil layer or Group

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def layer_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the active Grease Pencil layer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def layer_reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Show all Grease Pencil layers

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def material_copy_to_object(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_active: bool | None = True,
) -> None:
    """Append Materials of the active Grease Pencil to other object

    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_active: Only Active, Append only active material, uncheck to append all materials
    :type only_active: bool | None
    """

def material_hide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    invert: bool | None = False,
) -> None:
    """Hide active/inactive Grease Pencil material(s)

    :type execution_context: int | str | None
    :type undo: bool | None
    :param invert: Invert, Hide inactive materials instead of the active one
    :type invert: bool | None
    """

def material_isolate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    affect_visibility: bool | None = False,
) -> None:
    """Toggle whether the active material is the only one that is editable and/or visible

    :type execution_context: int | str | None
    :type undo: bool | None
    :param affect_visibility: Affect Visibility, In addition to toggling the editability, also affect the visibility
    :type affect_visibility: bool | None
    """

def material_lock_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Lock all Grease Pencil materials to prevent them from being accidentally modified

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def material_lock_unselected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Lock any material not used in any selected stroke

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def material_lock_unused(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Lock and hide any material not used

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def material_reveal(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unhide all hidden Grease Pencil materials

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def material_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
) -> None:
    """Select/Deselect all Grease Pencil strokes using current material

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect: Deselect, Unselect strokes
    :type deselect: bool | None
    """

def material_unlock_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unlock all Grease Pencil materials so that they can be edited

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def move_to_layer(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    target_layer_name: str = "",
    add_new_layer: bool | None = False,
) -> None:
    """Move selected strokes to another layer

    :type execution_context: int | str | None
    :type undo: bool | None
    :param target_layer_name: Name, Target Grease Pencil Layer
    :type target_layer_name: str
    :param add_new_layer: New Layer, Move selection to a new layer
    :type add_new_layer: bool | None
    """

def outline(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["VIEW", "FRONT", "SIDE", "TOP", "CURSOR", "CAMERA"]
    | None = "VIEW",
    radius: float | None = 0.01,
    offset_factor: float | None = -1.0,
    corner_subdivisions: int | None = 2,
) -> None:
    """Convert selected strokes to perimeter

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Projection Mode
    :type type: typing.Literal['VIEW','FRONT','SIDE','TOP','CURSOR','CAMERA'] | None
    :param radius: Radius
    :type radius: float | None
    :param offset_factor: Offset Factor
    :type offset_factor: float | None
    :param corner_subdivisions: Corner Subdivisions
    :type corner_subdivisions: int | None
    """

def paintmode_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    back: bool | None = False,
) -> None:
    """Enter/Exit paint mode for Grease Pencil strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool | None
    """

def paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["ACTIVE", "LAYER"] | None = "ACTIVE",
    paste_back: bool | None = False,
    keep_world_transform: bool | None = False,
) -> None:
    """Paste Grease Pencil points or strokes from the internal clipboard to the active layer

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['ACTIVE','LAYER'] | None
    :param paste_back: Paste on Back, Add pasted strokes behind all strokes
    :type paste_back: bool | None
    :param keep_world_transform: Keep World Transform, Keep the world transform of strokes from the clipboard unchanged
    :type keep_world_transform: bool | None
    """

def pen(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    deselect_all: bool | None = False,
    select_passthrough: bool | None = False,
    extrude_point: bool | None = False,
    extrude_handle: typing.Literal["AUTO", "VECTOR"] | None = "VECTOR",
    delete_point: bool | None = False,
    insert_point: bool | None = False,
    move_segment: bool | None = False,
    select_point: bool | None = False,
    move_point: bool | None = False,
    cycle_handle_type: bool | None = False,
    radius: float | None = 0.01,
) -> None:
    """Construct and edit splines

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    :param deselect: Deselect, Remove from selection
    :type deselect: bool | None
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | None
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool | None
    :param extrude_point: Extrude Point, Add a point connected to the last selected point
    :type extrude_point: bool | None
    :param extrude_handle: Extrude Handle Type, Type of the extruded handle
    :type extrude_handle: typing.Literal['AUTO','VECTOR'] | None
    :param delete_point: Delete Point, Delete an existing point
    :type delete_point: bool | None
    :param insert_point: Insert Point, Insert Point into a curve segment
    :type insert_point: bool | None
    :param move_segment: Move Segment, Delete an existing point
    :type move_segment: bool | None
    :param select_point: Select Point, Select a point or its handles
    :type select_point: bool | None
    :param move_point: Move Point, Move a point or its handles
    :type move_point: bool | None
    :param cycle_handle_type: Cycle Handle Type, Cycle between all four handle types
    :type cycle_handle_type: bool | None
    :param radius: Radius
    :type radius: float | None
    """

def primitive_arc(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    subdivision: int | None = 62,
    type: typing.Literal["BOX", "LINE", "POLYLINE", "CIRCLE", "ARC", "CURVE"]
    | None = "ARC",
) -> None:
    """Create predefined Grease Pencil stroke arcs

    :type execution_context: int | str | None
    :type undo: bool | None
    :param subdivision: Subdivisions, Number of subdivisions per segment
    :type subdivision: int | None
    :param type: Type, Type of shape
    :type type: typing.Literal['BOX','LINE','POLYLINE','CIRCLE','ARC','CURVE'] | None
    """

def primitive_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    subdivision: int | None = 3,
    type: typing.Literal["BOX", "LINE", "POLYLINE", "CIRCLE", "ARC", "CURVE"]
    | None = "BOX",
) -> None:
    """Create predefined Grease Pencil stroke boxes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param subdivision: Subdivisions, Number of subdivisions per segment
    :type subdivision: int | None
    :param type: Type, Type of shape
    :type type: typing.Literal['BOX','LINE','POLYLINE','CIRCLE','ARC','CURVE'] | None
    """

def primitive_circle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    subdivision: int | None = 94,
    type: typing.Literal["BOX", "LINE", "POLYLINE", "CIRCLE", "ARC", "CURVE"]
    | None = "CIRCLE",
) -> None:
    """Create predefined Grease Pencil stroke circles

    :type execution_context: int | str | None
    :type undo: bool | None
    :param subdivision: Subdivisions, Number of subdivisions per segment
    :type subdivision: int | None
    :param type: Type, Type of shape
    :type type: typing.Literal['BOX','LINE','POLYLINE','CIRCLE','ARC','CURVE'] | None
    """

def primitive_curve(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    subdivision: int | None = 62,
    type: typing.Literal["BOX", "LINE", "POLYLINE", "CIRCLE", "ARC", "CURVE"]
    | None = "CURVE",
) -> None:
    """Create predefined Grease Pencil stroke curve shapes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param subdivision: Subdivisions, Number of subdivisions per segment
    :type subdivision: int | None
    :param type: Type, Type of shape
    :type type: typing.Literal['BOX','LINE','POLYLINE','CIRCLE','ARC','CURVE'] | None
    """

def primitive_line(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    subdivision: int | None = 6,
    type: typing.Literal["BOX", "LINE", "POLYLINE", "CIRCLE", "ARC", "CURVE"]
    | None = "LINE",
) -> None:
    """Create predefined Grease Pencil stroke lines

    :type execution_context: int | str | None
    :type undo: bool | None
    :param subdivision: Subdivisions, Number of subdivisions per segment
    :type subdivision: int | None
    :param type: Type, Type of shape
    :type type: typing.Literal['BOX','LINE','POLYLINE','CIRCLE','ARC','CURVE'] | None
    """

def primitive_polyline(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    subdivision: int | None = 6,
    type: typing.Literal["BOX", "LINE", "POLYLINE", "CIRCLE", "ARC", "CURVE"]
    | None = "POLYLINE",
) -> None:
    """Create predefined Grease Pencil stroke polylines

    :type execution_context: int | str | None
    :type undo: bool | None
    :param subdivision: Subdivisions, Number of subdivisions per segment
    :type subdivision: int | None
    :param type: Type, Type of shape
    :type type: typing.Literal['BOX','LINE','POLYLINE','CIRCLE','ARC','CURVE'] | None
    """

def relative_layer_mask_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["ABOVE", "BELOW"] | None = "ABOVE",
) -> None:
    """Mask active layer with layer above or below

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode, Which relative layer (above or below) to use as a mask
    :type mode: typing.Literal['ABOVE','BELOW'] | None
    """

def remove_fill_guides(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["ACTIVE_FRAME", "ALL_FRAMES"] | None = "ALL_FRAMES",
) -> None:
    """Remove all the strokes that were created from the fill tool as guides

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['ACTIVE_FRAME','ALL_FRAMES'] | None
    """

def reorder(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["TOP", "UP", "DOWN", "BOTTOM"] | None = "TOP",
) -> None:
    """Change the display order of the selected strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction
    :type direction: typing.Literal['TOP','UP','DOWN','BOTTOM'] | None
    """

def reproject(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["FRONT", "SIDE", "TOP", "VIEW", "SURFACE", "CURSOR"]
    | None = "VIEW",
    keep_original: bool | None = False,
    offset: float | None = 0.0,
) -> None:
    """Reproject the selected strokes from the current viewpoint as if they had been newly drawn (e.g. to fix problems from accidental 3D cursor movement or accidental viewport changes, or for matching deforming geometry)

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Projection Type

    FRONT
    Front -- Reproject the strokes using the X-Z plane.

    SIDE
    Side -- Reproject the strokes using the Y-Z plane.

    TOP
    Top -- Reproject the strokes using the X-Y plane.

    VIEW
    View -- Reproject the strokes to end up on the same plane, as if drawn from the current viewpoint using Cursor Stroke Placement.

    SURFACE
    Surface -- Reproject the strokes on to the scene geometry, as if drawn using Surface placement.

    CURSOR
    Cursor -- Reproject the strokes using the orientation of 3D cursor.
        :type type: typing.Literal['FRONT','SIDE','TOP','VIEW','SURFACE','CURSOR'] | None
        :param keep_original: Keep Original, Keep original strokes and create a copy before reprojecting
        :type keep_original: bool | None
        :param offset: Surface Offset
        :type offset: float | None
    """

def reset_uvs(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset UV transformation to default values

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def sculpt_paint(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
    pen_flip: bool | None = False,
) -> None:
    """Sculpt strokes in the active Grease Pencil object

        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :type mode: typing.Literal['NORMAL','INVERT','SMOOTH','ERASE'] | None
        :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used
        :type pen_flip: bool | None
    """

def sculptmode_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    back: bool | None = False,
) -> None:
    """Enter/Exit sculpt mode for Grease Pencil strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool | None
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """(De)select all visible strokes

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
    """

def select_alternate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect_ends: bool | None = False,
) -> None:
    """Select alternated points in strokes with already selected points

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect_ends: Deselect Ends, (De)select the first and last point of each stroke
    :type deselect_ends: bool | None
    """

def select_ends(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    amount_start: int | None = 0,
    amount_end: int | None = 1,
) -> None:
    """Select end points of strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param amount_start: Amount Start, Number of points to select from the start
    :type amount_start: int | None
    :param amount_end: Amount End, Number of points to select from the end
    :type amount_end: int | None
    """

def select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Shrink the selection by one point

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all points in curves with any point selection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Grow the selection by one point

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.5,
    seed: int | None = 0,
    action: typing.Literal["SELECT", "DESELECT"] | None = "SELECT",
) -> None:
    """Selects random points from the current strokes selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param ratio: Ratio, Portion of items to select randomly
        :type ratio: float | None
        :param seed: Random Seed, Seed for the random number generator
        :type seed: int | None
        :param action: Action, Selection action to execute

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.
        :type action: typing.Literal['SELECT','DESELECT'] | None
    """

def select_similar(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["LAYER", "MATERIAL", "VERTEX_COLOR", "RADIUS", "OPACITY"]
    | None = "LAYER",
    threshold: float | None = 0.1,
) -> None:
    """Select all strokes with similar characteristics

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['LAYER','MATERIAL','VERTEX_COLOR','RADIUS','OPACITY'] | None
    :param threshold: Threshold
    :type threshold: float | None
    """

def separate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["SELECTED", "MATERIAL", "LAYER"] | None = "SELECTED",
) -> None:
    """Separate the selected geometry into a new Grease Pencil object

        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    SELECTED
    Selection -- Separate selected geometry.

    MATERIAL
    By Material -- Separate by material.

    LAYER
    By Layer -- Separate by layer.
        :type mode: typing.Literal['SELECTED','MATERIAL','LAYER'] | None
    """

def set_active_material(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set the selected stroke material as the active material

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def set_corner_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    corner_type: typing.Literal["ROUND", "FLAT", "SHARP"] | None = "SHARP",
    miter_angle: float | None = 0.785398,
) -> None:
    """Set the corner type of the selected points

    :type execution_context: int | str | None
    :type undo: bool | None
    :param corner_type: Corner Type
    :type corner_type: typing.Literal['ROUND','FLAT','SHARP'] | None
    :param miter_angle: Miter Cut Angle, All corners sharper than the Miter angle will be cut flat
    :type miter_angle: float | None
    """

def set_curve_resolution(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    resolution: int | None = 12,
) -> None:
    """Set resolution of selected curves

    :type execution_context: int | str | None
    :type undo: bool | None
    :param resolution: Resolution, The resolution to use for each curve segment
    :type resolution: int | None
    """

def set_curve_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.CurvesTypeItems | None = "POLY",
    use_handles: bool | None = False,
) -> None:
    """Set type of selected curves

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Curve type
    :type type: bpy.stub_internal.rna_enums.CurvesTypeItems | None
    :param use_handles: Handles, Take handle information into account in the conversion
    :type use_handles: bool | None
    """

def set_handle_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["AUTO", "VECTOR", "ALIGN", "FREE_ALIGN", "TOGGLE_FREE_ALIGN"]
    | None = "AUTO",
) -> None:
    """Set the handle type for Bézier curves

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    AUTO
    Auto -- The location is automatically calculated to be smooth.

    VECTOR
    Vector -- The location is calculated to point to the next/previous control point.

    ALIGN
    Align -- The location is constrained to point in the opposite direction as the other handle.

    FREE_ALIGN
    Free -- The handle can be moved anywhere, and does not influence the points other handle.

    TOGGLE_FREE_ALIGN
    Toggle Free/Align -- Replace Free handles with Align, and all Align with Free handles.
        :type type: typing.Literal['AUTO','VECTOR','ALIGN','FREE_ALIGN','TOGGLE_FREE_ALIGN'] | None
    """

def set_material(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    slot: str | None = "DEFAULT",
) -> None:
    """Set active material

    :type execution_context: int | str | None
    :type undo: bool | None
    :param slot: Material Slot
    :type slot: str | None
    """

def set_selection_mode(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: bpy.stub_internal.rna_enums.GreasePencilSelectmodeItems | None = "POINT",
) -> None:
    """Change the selection mode for Grease Pencil strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: bpy.stub_internal.rna_enums.GreasePencilSelectmodeItems | None
    """

def set_start_point(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select which point is the beginning of the curve

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def set_uniform_opacity(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    opacity_stroke: float | None = 1.0,
    opacity_fill: float | None = 0.5,
) -> None:
    """Set all stroke points to same opacity

    :type execution_context: int | str | None
    :type undo: bool | None
    :param opacity_stroke: Stroke Opacity
    :type opacity_stroke: float | None
    :param opacity_fill: Fill Opacity
    :type opacity_fill: float | None
    """

def set_uniform_thickness(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    thickness: float | None = 0.1,
) -> None:
    """Set all stroke points to same thickness

    :type execution_context: int | str | None
    :type undo: bool | None
    :param thickness: Thickness, Thickness
    :type thickness: float | None
    """

def snap_cursor_to_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Snap cursor to center of selected points

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def snap_to_cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_offset: bool | None = True,
) -> None:
    """Snap selected points/strokes to the cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_offset: With Offset, Offset the entire stroke instead of selected points only
    :type use_offset: bool | None
    """

def snap_to_grid(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Snap selected points to the nearest grid points

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def stroke_material_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    material: str = "",
) -> None:
    """Assign the active material slot to the selected strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param material: Material, Name of the material
    :type material: str
    """

def stroke_merge_by_distance(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.001,
    use_unselected: bool | None = False,
) -> None:
    """Merge points by distance

    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Threshold
    :type threshold: float | None
    :param use_unselected: Unselected, Use whole stroke, not only selected points
    :type use_unselected: bool | None
    """

def stroke_reset_vertex_color(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["STROKE", "FILL", "BOTH"] | None = "BOTH",
) -> None:
    """Reset vertex color for all or selected strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['STROKE','FILL','BOTH'] | None
    """

def stroke_simplify(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.01,
    length: float | None = 0.05,
    distance: float | None = 0.01,
    steps: int | None = 1,
    mode: typing.Literal["FIXED", "ADAPTIVE", "SAMPLE", "MERGE"] | None = "FIXED",
) -> None:
    """Simplify selected strokes

        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Factor
        :type factor: float | None
        :param length: Length
        :type length: float | None
        :param distance: Distance
        :type distance: float | None
        :param steps: Steps
        :type steps: int | None
        :param mode: Mode, Method used for simplifying stroke points

    FIXED
    Fixed -- Delete alternating vertices in the stroke, except extremes.

    ADAPTIVE
    Adaptive -- Use a Ramer-Douglas-Peucker algorithm to simplify the stroke preserving main shape.

    SAMPLE
    Sample -- Re-sample the stroke with segments of the specified length.

    MERGE
    Merge -- Simplify the stroke by merging vertices closer than a given distance.
        :type mode: typing.Literal['FIXED','ADAPTIVE','SAMPLE','MERGE'] | None
    """

def stroke_smooth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    iterations: int | None = 10,
    factor: float | None = 1.0,
    smooth_ends: bool | None = False,
    keep_shape: bool | None = False,
    smooth_position: bool | None = True,
    smooth_radius: bool | None = True,
    smooth_opacity: bool | None = False,
) -> None:
    """Smooth selected strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param iterations: Iterations
    :type iterations: int | None
    :param factor: Factor
    :type factor: float | None
    :param smooth_ends: Smooth Endpoints
    :type smooth_ends: bool | None
    :param keep_shape: Keep Shape
    :type keep_shape: bool | None
    :param smooth_position: Position
    :type smooth_position: bool | None
    :param smooth_radius: Radius
    :type smooth_radius: bool | None
    :param smooth_opacity: Opacity
    :type smooth_opacity: bool | None
    """

def stroke_split(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Split selected points to a new stroke

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def stroke_subdivide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number_cuts: int | None = 1,
    only_selected: bool | None = True,
) -> None:
    """Subdivide between continuous selected points of the stroke adding a point half way between them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param number_cuts: Number of Cuts
    :type number_cuts: int | None
    :param only_selected: Selected Points, Smooth only selected points in the stroke
    :type only_selected: bool | None
    """

def stroke_subdivide_smooth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    GREASE_PENCIL_OT_stroke_subdivide: typing.Any | None = None,
    GREASE_PENCIL_OT_stroke_smooth: typing.Any | None = None,
) -> None:
    """Subdivide strokes and smooth them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param GREASE_PENCIL_OT_stroke_subdivide: Subdivide Stroke, Subdivide between continuous selected points of the stroke adding a point half way between them
    :type GREASE_PENCIL_OT_stroke_subdivide: typing.Any | None
    :param GREASE_PENCIL_OT_stroke_smooth: Smooth Stroke, Smooth selected strokes
    :type GREASE_PENCIL_OT_stroke_smooth: typing.Any | None
    """

def stroke_switch_direction(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Change direction of the points of the selected strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def stroke_trim(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
) -> None:
    """Delete stroke points in between intersecting strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param path: Path
    :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
    :param use_smooth_stroke: Stabilize Stroke, Selection lags behind mouse and follows a smoother path
    :type use_smooth_stroke: bool | None
    :param smooth_stroke_factor: Smooth Stroke Factor, Higher values gives a smoother stroke
    :type smooth_stroke_factor: float | None
    :param smooth_stroke_radius: Smooth Stroke Radius, Minimum distance from last point before selection continues
    :type smooth_stroke_radius: int | None
    """

def texture_gradient(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xstart: int | None = 0,
    xend: int | None = 0,
    ystart: int | None = 0,
    yend: int | None = 0,
    flip: bool | None = False,
    cursor: int | None = 5,
) -> None:
    """Draw a line to set the fill material gradient for the selected strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xstart: X Start
    :type xstart: int | None
    :param xend: X End
    :type xend: int | None
    :param ystart: Y Start
    :type ystart: int | None
    :param yend: Y End
    :type yend: int | None
    :param flip: Flip
    :type flip: bool | None
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int | None
    """

def trace_image(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    target: typing.Literal["NEW", "SELECTED"] | None = "NEW",
    radius: float | None = 0.01,
    threshold: float | None = 0.5,
    turnpolicy: typing.Literal[
        "FOREGROUND", "BACKGROUND", "LEFT", "RIGHT", "MINORITY", "MAJORITY", "RANDOM"
    ]
    | None = "MINORITY",
    mode: typing.Literal["SINGLE", "SEQUENCE"] | None = "SINGLE",
    use_current_frame: bool | None = True,
    frame_number: int | None = 0,
) -> None:
    """Extract Grease Pencil strokes from image

        :type execution_context: int | str | None
        :type undo: bool | None
        :param target: Target Object, Target Grease Pencil
        :type target: typing.Literal['NEW','SELECTED'] | None
        :param radius: Radius
        :type radius: float | None
        :param threshold: Color Threshold, Determine the lightness threshold above which strokes are generated
        :type threshold: float | None
        :param turnpolicy: Turn Policy, Determines how to resolve ambiguities during decomposition of bitmaps into paths

    FOREGROUND
    Foreground -- Prefers to connect foreground components.

    BACKGROUND
    Background -- Prefers to connect background components.

    LEFT
    Left -- Always take a left turn.

    RIGHT
    Right -- Always take a right turn.

    MINORITY
    Minority -- Prefers to connect the color that occurs least frequently in the local neighborhood of the current position.

    MAJORITY
    Majority -- Prefers to connect the color that occurs most frequently in the local neighborhood of the current position.

    RANDOM
    Random -- Choose pseudo-randomly.
        :type turnpolicy: typing.Literal['FOREGROUND','BACKGROUND','LEFT','RIGHT','MINORITY','MAJORITY','RANDOM'] | None
        :param mode: Mode, Determines if trace simple image or full sequence

    SINGLE
    Single -- Trace the current frame of the image.

    SEQUENCE
    Sequence -- Trace full sequence.
        :type mode: typing.Literal['SINGLE','SEQUENCE'] | None
        :param use_current_frame: Start At Current Frame, Trace Image starting in current image frame
        :type use_current_frame: bool | None
        :param frame_number: Trace Frame, Used to trace only one frame of the image sequence, set to zero to trace all
        :type frame_number: int | None
    """

def vertex_brush_stroke(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
    pen_flip: bool | None = False,
) -> None:
    """Draw on vertex colors in the active Grease Pencil object

        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :type mode: typing.Literal['NORMAL','INVERT','SMOOTH','ERASE'] | None
        :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used
        :type pen_flip: bool | None
    """

def vertex_color_brightness_contrast(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["STROKE", "FILL", "BOTH"] | None = "BOTH",
    brightness: float | None = 0.0,
    contrast: float | None = 0.0,
) -> None:
    """Adjust vertex color brightness/contrast

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['STROKE','FILL','BOTH'] | None
    :param brightness: Brightness
    :type brightness: float | None
    :param contrast: Contrast
    :type contrast: float | None
    """

def vertex_color_hsv(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["STROKE", "FILL", "BOTH"] | None = "BOTH",
    h: float | None = 0.5,
    s: float | None = 1.0,
    v: float | None = 1.0,
) -> None:
    """Adjust vertex color HSV values

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['STROKE','FILL','BOTH'] | None
    :param h: Hue
    :type h: float | None
    :param s: Saturation
    :type s: float | None
    :param v: Value
    :type v: float | None
    """

def vertex_color_invert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["STROKE", "FILL", "BOTH"] | None = "BOTH",
) -> None:
    """Invert RGB values

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['STROKE','FILL','BOTH'] | None
    """

def vertex_color_levels(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["STROKE", "FILL", "BOTH"] | None = "BOTH",
    offset: float | None = 0.0,
    gain: float | None = 1.0,
) -> None:
    """Adjust levels of vertex colors

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['STROKE','FILL','BOTH'] | None
    :param offset: Offset, Value to add to colors
    :type offset: float | None
    :param gain: Gain, Value to multiply colors by
    :type gain: float | None
    """

def vertex_color_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["STROKE", "FILL", "BOTH"] | None = "BOTH",
    factor: float | None = 1.0,
) -> None:
    """Set active color to all selected vertex

    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['STROKE','FILL','BOTH'] | None
    :param factor: Factor, Mix Factor
    :type factor: float | None
    """

def vertex_group_normalize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Normalize weights of the active vertex group

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vertex_group_normalize_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    lock_active: bool | None = True,
) -> None:
    """Normalize the weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0

    :type execution_context: int | str | None
    :type undo: bool | None
    :param lock_active: Lock Active, Keep the values of the active group while normalizing others
    :type lock_active: bool | None
    """

def vertex_group_smooth(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.5,
    repeat: int | None = 1,
) -> None:
    """Smooth the weights of the active vertex group

    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor
    :type factor: float | None
    :param repeat: Iterations
    :type repeat: int | None
    """

def vertexmode_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    back: bool | None = False,
) -> None:
    """Enter/Exit vertex paint mode for Grease Pencil strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool | None
    """

def weight_brush_stroke(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH", "ERASE"] | None = "NORMAL",
    pen_flip: bool | None = False,
) -> None:
    """Draw weight on stroke points in the active Grease Pencil object

        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL
    Regular -- Apply brush normally.

    INVERT
    Invert -- Invert action of brush for duration of stroke.

    SMOOTH
    Smooth -- Switch brush to smooth mode for duration of stroke.

    ERASE
    Erase -- Switch brush to erase mode for duration of stroke.
        :type mode: typing.Literal['NORMAL','INVERT','SMOOTH','ERASE'] | None
        :param pen_flip: Pen Flip, Whether a tablets eraser mode is being used
        :type pen_flip: bool | None
    """

def weight_invert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Invert the weight of active vertex group

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def weight_sample(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set the weight of the Draw tool to the weight of the vertex under the mouse cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def weight_toggle_direction(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle Add/Subtract for the weight paint draw tool

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def weightmode_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    back: bool | None = False,
) -> None:
    """Enter/Exit weight paint mode for Grease Pencil strokes

    :type execution_context: int | str | None
    :type undo: bool | None
    :param back: Return to Previous Mode, Return to previous mode
    :type back: bool | None
    """
