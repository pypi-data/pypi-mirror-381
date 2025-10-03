import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform
import bpy.stub_internal.rna_enums
import bpy.types
import mathutils

def add_scene_strip_from_scene_asset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    move_strips: bool | None = True,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    skip_locked_or_muted_channels: bool | None = True,
    asset_library_type: bpy.stub_internal.rna_enums.AssetLibraryTypeItems
    | None = "LOCAL",
    asset_library_identifier: str = "",
    relative_asset_identifier: str = "",
) -> None:
    """Add a scene strip from a scene asset

    :type execution_context: int | str | None
    :type undo: bool | None
    :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline
    :type move_strips: bool | None
    :param frame_start: Start Frame, Start frame of the strip
    :type frame_start: int | None
    :param channel: Channel, Channel to place this strip into
    :type channel: int | None
    :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes
    :type replace_sel: bool | None
    :param overlap: Allow Overlap, Dont correct overlap on new strips
    :type overlap: bool | None
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool | None
    :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
    :type skip_locked_or_muted_channels: bool | None
    :param asset_library_type: Asset Library Type
    :type asset_library_type: bpy.stub_internal.rna_enums.AssetLibraryTypeItems | None
    :param asset_library_identifier: Asset Library Identifier
    :type asset_library_identifier: str
    :param relative_asset_identifier: Relative Asset Identifier
    :type relative_asset_identifier: str
    """

def change_effect_type(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "CROSS",
        "ADD",
        "SUBTRACT",
        "ALPHA_OVER",
        "ALPHA_UNDER",
        "GAMMA_CROSS",
        "MULTIPLY",
        "WIPE",
        "GLOW",
        "COLOR",
        "SPEED",
        "MULTICAM",
        "ADJUSTMENT",
        "GAUSSIAN_BLUR",
        "TEXT",
        "COLORMIX",
    ]
    | None = "CROSS",
) -> None:
    """Replace effect strip with another that takes the same number of inputs

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Strip effect type

    CROSS
    Crossfade -- Fade out of one video, fading into another.

    ADD
    Add -- Add together color channels from two videos.

    SUBTRACT
    Subtract -- Subtract one strips color from another.

    ALPHA_OVER
    Alpha Over -- Blend alpha on top of another video.

    ALPHA_UNDER
    Alpha Under -- Blend alpha below another video.

    GAMMA_CROSS
    Gamma Crossfade -- Crossfade with color correction.

    MULTIPLY
    Multiply -- Multiply color channels from two videos.

    WIPE
    Wipe -- Sweep a transition line across the frame.

    GLOW
    Glow -- Add blur and brightness to light areas.

    COLOR
    Color -- Add a simple color strip.

    SPEED
    Speed -- Timewarp video strips, modifying playback speed.

    MULTICAM
    Multicam Selector -- Control active camera angles.

    ADJUSTMENT
    Adjustment Layer -- Apply nondestructive effects.

    GAUSSIAN_BLUR
    Gaussian Blur -- Soften details along axes.

    TEXT
    Text -- Add a simple text strip.

    COLORMIX
    Color Mix -- Combine two strips using blend modes.
        :type type: typing.Literal['CROSS','ADD','SUBTRACT','ALPHA_OVER','ALPHA_UNDER','GAMMA_CROSS','MULTIPLY','WIPE','GLOW','COLOR','SPEED','MULTICAM','ADJUSTMENT','GAUSSIAN_BLUR','TEXT','COLORMIX'] | None
    """

def change_path(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    hide_props_region: bool | None = True,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    use_placeholders: bool | None = False,
) -> None:
    """Undocumented, consider contributing.

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param use_placeholders: Use Placeholders, Use placeholders for missing frames of the strip
        :type use_placeholders: bool | None
    """

def change_scene(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    scene: str | None = "",
) -> None:
    """Change Scene assigned to Strip

    :type execution_context: int | str | None
    :type undo: bool | None
    :param scene: Scene
    :type scene: str | None
    """

def connect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    toggle: bool | None = True,
) -> None:
    """Link selected strips together for simplified group selection

    :type execution_context: int | str | None
    :type undo: bool | None
    :param toggle: Toggle, Toggle strip connections
    :type toggle: bool | None
    """

def copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy the selected strips to the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def crossfade_sounds(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Do cross-fading volume animation of two selected sound strips

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def cursor_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Sequence[float] | mathutils.Vector | None = (0.0, 0.0),
) -> None:
    """Set 2D cursor location

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Cursor location in normalized preview coordinates
    :type location: collections.abc.Sequence[float] | mathutils.Vector | None
    """

def deinterlace_selected_movies(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deinterlace all selected movie sources

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delete_data: bool | None = False,
) -> None:
    """Delete selected strips from the sequencer

    :type execution_context: int | str | None
    :type undo: bool | None
    :param delete_data: Delete Data, After removing the Strip, delete the associated data also
    :type delete_data: bool | None
    """

def disconnect(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unlink selected strips so that they can be selected individually

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    linked: bool | None = False,
) -> None:
    """Duplicate the selected strips

    :type execution_context: int | str | None
    :type undo: bool | None
    :param linked: Linked, Duplicate strip but not strip data, linking to the original data
    :type linked: bool | None
    """

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    SEQUENCER_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None = None,
) -> None:
    """Duplicate selected strips and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
    :type SEQUENCER_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    :type TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None
    """

def duplicate_move_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    SEQUENCER_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None = None,
) -> None:
    """Duplicate selected strips, but not their data, and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
    :type SEQUENCER_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    :type TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None
    """

def effect_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "CROSS",
        "ADD",
        "SUBTRACT",
        "ALPHA_OVER",
        "ALPHA_UNDER",
        "GAMMA_CROSS",
        "MULTIPLY",
        "WIPE",
        "GLOW",
        "COLOR",
        "SPEED",
        "MULTICAM",
        "ADJUSTMENT",
        "GAUSSIAN_BLUR",
        "TEXT",
        "COLORMIX",
    ]
    | None = "CROSS",
    move_strips: bool | None = True,
    frame_start: int | None = 0,
    length: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    skip_locked_or_muted_channels: bool | None = True,
    color: collections.abc.Sequence[float] | mathutils.Color | None = (0.0, 0.0, 0.0),
) -> None:
    """Add an effect to the sequencer, most are applied on top of existing strips

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Sequencer effect type

    CROSS
    Crossfade -- Fade out of one video, fading into another.

    ADD
    Add -- Add together color channels from two videos.

    SUBTRACT
    Subtract -- Subtract one strips color from another.

    ALPHA_OVER
    Alpha Over -- Blend alpha on top of another video.

    ALPHA_UNDER
    Alpha Under -- Blend alpha below another video.

    GAMMA_CROSS
    Gamma Crossfade -- Crossfade with color correction.

    MULTIPLY
    Multiply -- Multiply color channels from two videos.

    WIPE
    Wipe -- Sweep a transition line across the frame.

    GLOW
    Glow -- Add blur and brightness to light areas.

    COLOR
    Color -- Add a simple color strip.

    SPEED
    Speed -- Timewarp video strips, modifying playback speed.

    MULTICAM
    Multicam Selector -- Control active camera angles.

    ADJUSTMENT
    Adjustment Layer -- Apply nondestructive effects.

    GAUSSIAN_BLUR
    Gaussian Blur -- Soften details along axes.

    TEXT
    Text -- Add a simple text strip.

    COLORMIX
    Color Mix -- Combine two strips using blend modes.
        :type type: typing.Literal['CROSS','ADD','SUBTRACT','ALPHA_OVER','ALPHA_UNDER','GAMMA_CROSS','MULTIPLY','WIPE','GLOW','COLOR','SPEED','MULTICAM','ADJUSTMENT','GAUSSIAN_BLUR','TEXT','COLORMIX'] | None
        :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline
        :type move_strips: bool | None
        :param frame_start: Start Frame, Start frame of the strip
        :type frame_start: int | None
        :param length: Length, Length of the strip in frames, or the length of each strip if multiple are added
        :type length: int | None
        :param channel: Channel, Channel to place this strip into
        :type channel: int | None
        :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes
        :type replace_sel: bool | None
        :param overlap: Allow Overlap, Dont correct overlap on new strips
        :type overlap: bool | None
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :type overlap_shuffle_override: bool | None
        :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
        :type skip_locked_or_muted_channels: bool | None
        :param color: Color, Initialize the strip with this color
        :type color: collections.abc.Sequence[float] | mathutils.Color | None
    """

def enable_proxies(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    proxy_25: bool | None = False,
    proxy_50: bool | None = False,
    proxy_75: bool | None = False,
    proxy_100: bool | None = False,
    overwrite: bool | None = False,
) -> None:
    """Enable selected proxies on all selected Movie and Image strips

    :type execution_context: int | str | None
    :type undo: bool | None
    :param proxy_25: 25%
    :type proxy_25: bool | None
    :param proxy_50: 50%
    :type proxy_50: bool | None
    :param proxy_75: 75%
    :type proxy_75: bool | None
    :param proxy_100: 100%
    :type proxy_100: bool | None
    :param overwrite: Overwrite
    :type overwrite: bool | None
    """

def export_subtitles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    hide_props_region: bool | None = True,
    check_existing: bool | None = True,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 8,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
) -> None:
    """Export .srt file containing text strips

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param hide_props_region: Hide Operator Properties, Collapse the region displaying the operator settings
        :type hide_props_region: bool | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
    """

def fades_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    duration_seconds: float | None = 1.0,
    type: typing.Literal["IN_OUT", "IN", "OUT", "CURSOR_FROM", "CURSOR_TO"]
    | None = "IN_OUT",
) -> None:
    """Adds or updates a fade animation for either visual or audio strips

        :type execution_context: int | str | None
        :type undo: bool | None
        :param duration_seconds: Fade Duration, Duration of the fade in seconds
        :type duration_seconds: float | None
        :param type: Fade Type, Fade in, out, both in and out, to, or from the current frame. Default is both in and out

    IN_OUT
    Fade In and Out -- Fade selected strips in and out.

    IN
    Fade In -- Fade in selected strips.

    OUT
    Fade Out -- Fade out selected strips.

    CURSOR_FROM
    From Current Frame -- Fade from the time cursor to the end of overlapping strips.

    CURSOR_TO
    To Current Frame -- Fade from the start of strips under the time cursor to the current frame.
        :type type: typing.Literal['IN_OUT','IN','OUT','CURSOR_FROM','CURSOR_TO'] | None
    """

def fades_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Removes fade animation from selected strips

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def gap_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frames: int | None = 10,
) -> None:
    """Insert gap at current frame to first strips at the right, independent of selection or locked state of strips

    :type execution_context: int | str | None
    :type undo: bool | None
    :param frames: Frames, Frames to insert after current strip
    :type frames: int | None
    """

def gap_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = False,
) -> None:
    """Remove gap at current frame to first strip at the right, independent of selection or locked state of strips

    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All Gaps, Do all gaps to right of current frame
    :type all: bool | None
    """

def image_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = True,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: typing.Literal[
        "DEFAULT",
        "FILE_SORT_ALPHA",
        "FILE_SORT_EXTENSION",
        "FILE_SORT_TIME",
        "FILE_SORT_SIZE",
        "ASSET_CATALOG",
    ]
    | None = "",
    move_strips: bool | None = True,
    frame_start: int | None = 0,
    length: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    skip_locked_or_muted_channels: bool | None = True,
    fit_method: bpy.stub_internal.rna_enums.StripScaleMethodItems | None = "FIT",
    set_view_transform: bool | None = True,
    use_sequence_detection: bool | None = True,
    use_placeholders: bool | None = False,
) -> None:
    """Add an image or image sequence to the sequencer

        :type execution_context: int | str | None
        :type undo: bool | None
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode

    DEFAULT
    Default -- Automatically determine sort method for files.

    FILE_SORT_ALPHA
    Name -- Sort the file list alphabetically.

    FILE_SORT_EXTENSION
    Extension -- Sort the file list by extension/type.

    FILE_SORT_TIME
    Modified Date -- Sort files by modification time.

    FILE_SORT_SIZE
    Size -- Sort files by size.

    ASSET_CATALOG
    Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
        :type sort_method: typing.Literal['DEFAULT','FILE_SORT_ALPHA','FILE_SORT_EXTENSION','FILE_SORT_TIME','FILE_SORT_SIZE','ASSET_CATALOG'] | None
        :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline
        :type move_strips: bool | None
        :param frame_start: Start Frame, Start frame of the strip
        :type frame_start: int | None
        :param length: Length, Length of the strip in frames, or the length of each strip if multiple are added
        :type length: int | None
        :param channel: Channel, Channel to place this strip into
        :type channel: int | None
        :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes
        :type replace_sel: bool | None
        :param overlap: Allow Overlap, Dont correct overlap on new strips
        :type overlap: bool | None
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :type overlap_shuffle_override: bool | None
        :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
        :type skip_locked_or_muted_channels: bool | None
        :param fit_method: Fit Method, Mode for fitting the image to the canvas
        :type fit_method: bpy.stub_internal.rna_enums.StripScaleMethodItems | None
        :param set_view_transform: Set View Transform, Set appropriate view transform based on media color space
        :type set_view_transform: bool | None
        :param use_sequence_detection: Detect Sequences, Automatically detect animated sequences in selected images (based on file names)
        :type use_sequence_detection: bool | None
        :param use_placeholders: Use Placeholders, Reserve placeholder frames for missing frames of the image sequence
        :type use_placeholders: bool | None
    """

def images_separate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    length: int | None = 1,
) -> None:
    """On image sequence strips, it returns a strip for each image

    :type execution_context: int | str | None
    :type undo: bool | None
    :param length: Length, Length of each frame
    :type length: int | None
    """

def lock(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Lock strips so they cannot be transformed

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def mask_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    move_strips: bool | None = True,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    skip_locked_or_muted_channels: bool | None = True,
    mask: str | None = "",
) -> None:
    """Add a mask strip to the sequencer

    :type execution_context: int | str | None
    :type undo: bool | None
    :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline
    :type move_strips: bool | None
    :param frame_start: Start Frame, Start frame of the strip
    :type frame_start: int | None
    :param channel: Channel, Channel to place this strip into
    :type channel: int | None
    :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes
    :type replace_sel: bool | None
    :param overlap: Allow Overlap, Dont correct overlap on new strips
    :type overlap: bool | None
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool | None
    :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
    :type skip_locked_or_muted_channels: bool | None
    :param mask: Mask
    :type mask: str | None
    """

def meta_make(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Group selected strips into a meta-strip

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def meta_separate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Put the contents of a meta-strip back in the sequencer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def meta_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle a meta-strip (to edit enclosed strips)

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def movie_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = True,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = False,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: typing.Literal[
        "DEFAULT",
        "FILE_SORT_ALPHA",
        "FILE_SORT_EXTENSION",
        "FILE_SORT_TIME",
        "FILE_SORT_SIZE",
        "ASSET_CATALOG",
    ]
    | None = "",
    move_strips: bool | None = True,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    skip_locked_or_muted_channels: bool | None = True,
    fit_method: bpy.stub_internal.rna_enums.StripScaleMethodItems | None = "FIT",
    set_view_transform: bool | None = True,
    adjust_playback_rate: bool | None = True,
    sound: bool | None = True,
    use_framerate: bool | None = True,
) -> None:
    """Add a movie strip to the sequencer

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode

    DEFAULT
    Default -- Automatically determine sort method for files.

    FILE_SORT_ALPHA
    Name -- Sort the file list alphabetically.

    FILE_SORT_EXTENSION
    Extension -- Sort the file list by extension/type.

    FILE_SORT_TIME
    Modified Date -- Sort files by modification time.

    FILE_SORT_SIZE
    Size -- Sort files by size.

    ASSET_CATALOG
    Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
        :type sort_method: typing.Literal['DEFAULT','FILE_SORT_ALPHA','FILE_SORT_EXTENSION','FILE_SORT_TIME','FILE_SORT_SIZE','ASSET_CATALOG'] | None
        :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline
        :type move_strips: bool | None
        :param frame_start: Start Frame, Start frame of the strip
        :type frame_start: int | None
        :param channel: Channel, Channel to place this strip into
        :type channel: int | None
        :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes
        :type replace_sel: bool | None
        :param overlap: Allow Overlap, Dont correct overlap on new strips
        :type overlap: bool | None
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :type overlap_shuffle_override: bool | None
        :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
        :type skip_locked_or_muted_channels: bool | None
        :param fit_method: Fit Method, Mode for fitting the image to the canvas
        :type fit_method: bpy.stub_internal.rna_enums.StripScaleMethodItems | None
        :param set_view_transform: Set View Transform, Set appropriate view transform based on media color space
        :type set_view_transform: bool | None
        :param adjust_playback_rate: Adjust Playback Rate, Play at normal speed regardless of scene FPS
        :type adjust_playback_rate: bool | None
        :param sound: Sound, Load sound with the movie
        :type sound: bool | None
        :param use_framerate: Set Scene Frame Rate, Set frame rate of the current scene to the frame rate of the movie
        :type use_framerate: bool | None
    """

def movieclip_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    move_strips: bool | None = True,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    skip_locked_or_muted_channels: bool | None = True,
    clip: str | None = "",
) -> None:
    """Add a movieclip strip to the sequencer

    :type execution_context: int | str | None
    :type undo: bool | None
    :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline
    :type move_strips: bool | None
    :param frame_start: Start Frame, Start frame of the strip
    :type frame_start: int | None
    :param channel: Channel, Channel to place this strip into
    :type channel: int | None
    :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes
    :type replace_sel: bool | None
    :param overlap: Allow Overlap, Dont correct overlap on new strips
    :type overlap: bool | None
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool | None
    :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
    :type skip_locked_or_muted_channels: bool | None
    :param clip: Clip
    :type clip: str | None
    """

def mute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Mute (un)selected strips

    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Mute unselected rather than selected strips
    :type unselected: bool | None
    """

def offset_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Clear strip in/out offsets from the start and end of content

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    keep_offset: bool | None = False,
    x: int | None = 0,
    y: int | None = 0,
) -> None:
    """Paste strips from the internal clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    :param keep_offset: Keep Offset, Keep strip offset relative to the current frame when pasting
    :type keep_offset: bool | None
    :param x: X
    :type x: int | None
    :param y: Y
    :type y: int | None
    """

def preview_duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    SEQUENCER_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Duplicate selected strips and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
    :type SEQUENCER_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def preview_duplicate_move_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    SEQUENCER_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Duplicate selected strips, but not their data, and move them

    :type execution_context: int | str | None
    :type undo: bool | None
    :param SEQUENCER_OT_duplicate: Duplicate Strips, Duplicate the selected strips
    :type SEQUENCER_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def reassign_inputs(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reassign the inputs for the effect strip

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def rebuild_proxy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Rebuild all selected proxies and timecode indices

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def refresh_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Refresh the sequencer editor

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def reload(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    adjust_length: bool | None = False,
) -> None:
    """Reload strips in the sequencer

    :type execution_context: int | str | None
    :type undo: bool | None
    :param adjust_length: Adjust Length, Adjust length of strips to their data length
    :type adjust_length: bool | None
    """

def rename_channel(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def rendersize(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set render size and aspect from active strip

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def retiming_add_freeze_frame_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    SEQUENCER_OT_retiming_freeze_frame_add: retiming_freeze_frame_add | None = None,
    TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None = None,
) -> None:
    """Add freeze frame and move it

    :type execution_context: int | str | None
    :type undo: bool | None
    :param SEQUENCER_OT_retiming_freeze_frame_add: Add Freeze Frame, Add freeze frame
    :type SEQUENCER_OT_retiming_freeze_frame_add: retiming_freeze_frame_add | None
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    :type TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None
    """

def retiming_add_transition_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    SEQUENCER_OT_retiming_transition_add: retiming_transition_add | None = None,
    TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None = None,
) -> None:
    """Add smooth transition between 2 retimed segments and change its duration

    :type execution_context: int | str | None
    :type undo: bool | None
    :param SEQUENCER_OT_retiming_transition_add: Add Speed Transition, Add smooth transition between 2 retimed segments
    :type SEQUENCER_OT_retiming_transition_add: retiming_transition_add | None
    :param TRANSFORM_OT_seq_slide: Sequence Slide, Slide a sequence strip in time
    :type TRANSFORM_OT_seq_slide: bpy.ops.transform.seq_slide | None
    """

def retiming_freeze_frame_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    duration: int | None = 0,
) -> None:
    """Add freeze frame

    :type execution_context: int | str | None
    :type undo: bool | None
    :param duration: Duration, Duration of freeze frame segment
    :type duration: int | None
    """

def retiming_key_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    timeline_frame: int | None = 0,
) -> None:
    """Add retiming Key

    :type execution_context: int | str | None
    :type undo: bool | None
    :param timeline_frame: Timeline Frame, Frame where key will be added
    :type timeline_frame: int | None
    """

def retiming_key_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete selected retiming keys from the sequencer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def retiming_reset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset strip retiming

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def retiming_segment_speed_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    speed: float | None = 100.0,
    keep_retiming: bool | None = True,
) -> None:
    """Set speed of retimed segment

    :type execution_context: int | str | None
    :type undo: bool | None
    :param speed: Speed, New speed of retimed segment
    :type speed: float | None
    :param keep_retiming: Preserve Current Retiming, Keep speed of other segments unchanged, change strip length instead
    :type keep_retiming: bool | None
    """

def retiming_show(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Show retiming keys in selected strips

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def retiming_transition_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    duration: int | None = 0,
) -> None:
    """Add smooth transition between 2 retimed segments

    :type execution_context: int | str | None
    :type undo: bool | None
    :param duration: Duration, Duration of freeze frame segment
    :type duration: int | None
    """

def sample(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    size: int | None = 1,
) -> None:
    """Use mouse to sample color in current frame

    :type execution_context: int | str | None
    :type undo: bool | None
    :param size: Sample Size
    :type size: int | None
    """

def scene_frame_range_update(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Update frame range of scene strip

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def scene_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    move_strips: bool | None = True,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    skip_locked_or_muted_channels: bool | None = True,
    scene: str | None = "",
) -> None:
    """Add a strip to the sequencer using a Blender scene as a source

    :type execution_context: int | str | None
    :type undo: bool | None
    :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline
    :type move_strips: bool | None
    :param frame_start: Start Frame, Start frame of the strip
    :type frame_start: int | None
    :param channel: Channel, Channel to place this strip into
    :type channel: int | None
    :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes
    :type replace_sel: bool | None
    :param overlap: Allow Overlap, Dont correct overlap on new strips
    :type overlap: bool | None
    :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
    :type overlap_shuffle_override: bool | None
    :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
    :type skip_locked_or_muted_channels: bool | None
    :param scene: Scene
    :type scene: str | None
    """

def scene_strip_add_new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    move_strips: bool | None = True,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    skip_locked_or_muted_channels: bool | None = True,
    type: typing.Literal["NEW", "EMPTY", "LINK_COPY", "FULL_COPY"] | None = "NEW",
) -> None:
    """Create a new Strip and assign a new Scene as source

        :type execution_context: int | str | None
        :type undo: bool | None
        :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline
        :type move_strips: bool | None
        :param frame_start: Start Frame, Start frame of the strip
        :type frame_start: int | None
        :param channel: Channel, Channel to place this strip into
        :type channel: int | None
        :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes
        :type replace_sel: bool | None
        :param overlap: Allow Overlap, Dont correct overlap on new strips
        :type overlap: bool | None
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :type overlap_shuffle_override: bool | None
        :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
        :type skip_locked_or_muted_channels: bool | None
        :param type: Type

    NEW
    New -- Add new Strip with a new empty Scene with default settings.

    EMPTY
    Copy Settings -- Add a new Strip, with an empty scene, and copy settings from the current scene.

    LINK_COPY
    Linked Copy -- Add a Strip and link in the collections from the current scene (shallow copy).

    FULL_COPY
    Full Copy -- Add a Strip and make a full copy of the current scene.
        :type type: typing.Literal['NEW','EMPTY','LINK_COPY','FULL_COPY'] | None
    """

def select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    wait_to_deselect_others: bool | None = False,
    use_select_on_click: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    deselect_all: bool | None = False,
    select_passthrough: bool | None = False,
    center: bool | None = False,
    linked_handle: bool | None = False,
    linked_time: bool | None = False,
    side_of_frame: bool | None = False,
    ignore_connections: bool | None = False,
) -> None:
    """Select a strip (last selected becomes the "active strip")

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
    :param center: Center, Use the object center when selecting, in edit mode used to extend object selection
    :type center: bool | None
    :param linked_handle: Linked Handle, Select handles next to the active strip
    :type linked_handle: bool | None
    :param linked_time: Linked Time, Select other strips or handles at the same time, or all retiming keys after the current in retiming mode
    :type linked_time: bool | None
    :param side_of_frame: Side of Frame, Select all strips on same side of the current frame as the mouse cursor
    :type side_of_frame: bool | None
    :param ignore_connections: Ignore Connections, Select strips individually whether or not they are connected
    :type ignore_connections: bool | None
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Select or deselect all strips

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

def select_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    tweak: bool | None = False,
    include_handles: bool | None = False,
    ignore_connections: bool | None = False,
) -> None:
    """Select strips using box selection

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
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
        :param tweak: Tweak, Make box select pass through to sequence slide when the cursor is hovering on a strip
        :type tweak: bool | None
        :param include_handles: Select Handles, Select the strips and their handles
        :type include_handles: bool | None
        :param ignore_connections: Ignore Connections, Select strips individually whether or not they are connected
        :type ignore_connections: bool | None
    """

def select_circle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x: int | None = 0,
    y: int | None = 0,
    radius: int | None = 25,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    ignore_connections: bool | None = False,
) -> None:
    """Select strips using circle selection

        :type execution_context: int | str | None
        :type undo: bool | None
        :param x: X
        :type x: int | None
        :param y: Y
        :type y: int | None
        :param radius: Radius
        :type radius: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
        :param ignore_connections: Ignore Connections, Select strips individually whether or not they are connected
        :type ignore_connections: bool | None
    """

def select_grouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "TYPE", "TYPE_BASIC", "TYPE_EFFECT", "DATA", "EFFECT", "EFFECT_LINK", "OVERLAP"
    ]
    | None = "TYPE",
    extend: bool | None = False,
    use_active_channel: bool | None = False,
) -> None:
    """Select all strips grouped by various properties

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    TYPE
    Type -- Shared strip type.

    TYPE_BASIC
    Global Type -- All strips of same basic type (graphical or sound).

    TYPE_EFFECT
    Effect Type -- Shared strip effect type (if active strip is not an effect one, select all non-effect strips).

    DATA
    Data -- Shared data (scene, image, sound, etc.).

    EFFECT
    Effect -- Shared effects.

    EFFECT_LINK
    Effect/Linked -- Other strips affected by the active one (sharing some time, and below or effect-assigned).

    OVERLAP
    Overlap -- Overlapping time.
        :type type: typing.Literal['TYPE','TYPE_BASIC','TYPE_EFFECT','DATA','EFFECT','EFFECT_LINK','OVERLAP'] | None
        :param extend: Extend, Extend selection instead of deselecting everything first
        :type extend: bool | None
        :param use_active_channel: Same Channel, Only consider strips on the same channel as the active one
        :type use_active_channel: bool | None
    """

def select_handle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    wait_to_deselect_others: bool | None = False,
    use_select_on_click: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
    ignore_connections: bool | None = False,
) -> None:
    """Select strip handle

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
    :param ignore_connections: Ignore Connections, Select strips individually whether or not they are connected
    :type ignore_connections: bool | None
    """

def select_handles(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    side: typing.Literal[
        "LEFT", "RIGHT", "BOTH", "LEFT_NEIGHBOR", "RIGHT_NEIGHBOR", "BOTH_NEIGHBORS"
    ]
    | None = "BOTH",
) -> None:
    """Select gizmo handles on the sides of the selected strip

    :type execution_context: int | str | None
    :type undo: bool | None
    :param side: Side, The side of the handle that is selected
    :type side: typing.Literal['LEFT','RIGHT','BOTH','LEFT_NEIGHBOR','RIGHT_NEIGHBOR','BOTH_NEIGHBORS'] | None
    """

def select_lasso(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    use_smooth_stroke: bool | None = False,
    smooth_stroke_factor: float | None = 0.75,
    smooth_stroke_radius: int | None = 35,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Select strips using lasso selection

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
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
    """

def select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Shrink the current selection of adjacent selected strips

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all strips adjacent to the current selection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select a chain of linked strips nearest to the mouse pointer

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select more strips adjacent to the current selection

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_side(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    side: typing.Literal["MOUSE", "LEFT", "RIGHT", "BOTH", "NO_CHANGE"] | None = "BOTH",
) -> None:
    """Select strips on the nominated side of the selected strips

    :type execution_context: int | str | None
    :type undo: bool | None
    :param side: Side, The side to which the selection is applied
    :type side: typing.Literal['MOUSE','LEFT','RIGHT','BOTH','NO_CHANGE'] | None
    """

def select_side_of_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    side: typing.Literal["LEFT", "RIGHT", "CURRENT"] | None = "LEFT",
) -> None:
    """Select strips relative to the current frame

        :type execution_context: int | str | None
        :type undo: bool | None
        :param extend: Extend, Extend the selection
        :type extend: bool | None
        :param side: Side

    LEFT
    Left -- Select to the left of the current frame.

    RIGHT
    Right -- Select to the right of the current frame.

    CURRENT
    Current Frame -- Select intersecting with the current frame.
        :type side: typing.Literal['LEFT','RIGHT','CURRENT'] | None
    """

def set_range_to_strips(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    preview: bool | None = False,
) -> None:
    """Set the frame range to the selected strips start and end

    :type execution_context: int | str | None
    :type undo: bool | None
    :param preview: Preview, Set the preview range instead
    :type preview: bool | None
    """

def slip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: float | None = 0.0,
    slip_keyframes: bool | None = False,
    use_cursor_position: bool | None = False,
    ignore_connections: bool | None = False,
) -> None:
    """Slip the contents of selected strips

    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Offset, Offset to the data of the strip
    :type offset: float | None
    :param slip_keyframes: Slip Keyframes, Move the keyframes alongside the media
    :type slip_keyframes: bool | None
    :param use_cursor_position: Use Cursor Position, Slip strips under mouse cursor instead of all selected strips
    :type use_cursor_position: bool | None
    :param ignore_connections: Ignore Connections, Do not slip connected strips if using cursor position
    :type ignore_connections: bool | None
    """

def snap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: int | None = 0,
) -> None:
    """Frame where selected strips will be snapped

    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame, Frame where selected strips will be snapped
    :type frame: int | None
    """

def sound_strip_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    directory: str = "",
    files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement]
    | None = None,
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = False,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = True,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    relative_path: bool | None = True,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: typing.Literal[
        "DEFAULT",
        "FILE_SORT_ALPHA",
        "FILE_SORT_EXTENSION",
        "FILE_SORT_TIME",
        "FILE_SORT_SIZE",
        "ASSET_CATALOG",
    ]
    | None = "",
    move_strips: bool | None = True,
    frame_start: int | None = 0,
    channel: int | None = 1,
    replace_sel: bool | None = True,
    overlap: bool | None = False,
    overlap_shuffle_override: bool | None = False,
    skip_locked_or_muted_channels: bool | None = True,
    cache: bool | None = False,
    mono: bool | None = False,
) -> None:
    """Add a sound strip to the sequencer

        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param directory: Directory, Directory of the file
        :type directory: str
        :param files: Files
        :type files: bpy.types.bpy_prop_collection[bpy.types.OperatorFileListElement] | None
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param relative_path: Relative Path, Select the file relative to the blend file
        :type relative_path: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode

    DEFAULT
    Default -- Automatically determine sort method for files.

    FILE_SORT_ALPHA
    Name -- Sort the file list alphabetically.

    FILE_SORT_EXTENSION
    Extension -- Sort the file list by extension/type.

    FILE_SORT_TIME
    Modified Date -- Sort files by modification time.

    FILE_SORT_SIZE
    Size -- Sort files by size.

    ASSET_CATALOG
    Asset Catalog -- Sort the asset list so that assets in the same catalog are kept together. Within a single catalog, assets are ordered by name. The catalogs are in order of the flattened catalog hierarchy..
        :type sort_method: typing.Literal['DEFAULT','FILE_SORT_ALPHA','FILE_SORT_EXTENSION','FILE_SORT_TIME','FILE_SORT_SIZE','ASSET_CATALOG'] | None
        :param move_strips: Move Strips, Automatically begin translating strips with the mouse after adding them to the timeline
        :type move_strips: bool | None
        :param frame_start: Start Frame, Start frame of the strip
        :type frame_start: int | None
        :param channel: Channel, Channel to place this strip into
        :type channel: int | None
        :param replace_sel: Replace Selection, Deselect previously selected strips after add operation completes
        :type replace_sel: bool | None
        :param overlap: Allow Overlap, Dont correct overlap on new strips
        :type overlap: bool | None
        :param overlap_shuffle_override: Override Overlap Shuffle Behavior, Use the overlap_mode tool settings to determine how to shuffle overlapping strips
        :type overlap_shuffle_override: bool | None
        :param skip_locked_or_muted_channels: Skip Locked or Muted Channels, Add strips to muted or locked channels when adding movie strips
        :type skip_locked_or_muted_channels: bool | None
        :param cache: Cache, Cache the sound in memory
        :type cache: bool | None
        :param mono: Mono, Merge all the sounds channels into one
        :type mono: bool | None
    """

def split(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: int | None = 0,
    channel: int | None = 0,
    type: typing.Literal["SOFT", "HARD"] | None = "SOFT",
    use_cursor_position: bool | None = False,
    side: typing.Literal["MOUSE", "LEFT", "RIGHT", "BOTH", "NO_CHANGE"]
    | None = "MOUSE",
    ignore_selection: bool | None = False,
    ignore_connections: bool | None = False,
) -> None:
    """Split the selected strips in two

    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame, Frame where selected strips will be split
    :type frame: int | None
    :param channel: Channel, Channel in which strip will be cut
    :type channel: int | None
    :param type: Type, The type of split operation to perform on strips
    :type type: typing.Literal['SOFT','HARD'] | None
    :param use_cursor_position: Use Cursor Position, Split at position of the cursor instead of current frame
    :type use_cursor_position: bool | None
    :param side: Side, The side that remains selected after splitting
    :type side: typing.Literal['MOUSE','LEFT','RIGHT','BOTH','NO_CHANGE'] | None
    :param ignore_selection: Ignore Selection, Make cut even if strip is not selected preserving selection state after cut
    :type ignore_selection: bool | None
    :param ignore_connections: Ignore Connections, Dont propagate split to connected strips
    :type ignore_connections: bool | None
    """

def split_multicam(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    camera: int | None = 1,
) -> None:
    """Split multicam strip and select camera

    :type execution_context: int | str | None
    :type undo: bool | None
    :param camera: Camera
    :type camera: int | None
    """

def strip_color_tag_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    color: bpy.stub_internal.rna_enums.StripColorItems | None = "NONE",
) -> None:
    """Set a color tag for the selected strips

    :type execution_context: int | str | None
    :type undo: bool | None
    :param color: Color Tag
    :type color: bpy.stub_internal.rna_enums.StripColorItems | None
    """

def strip_jump(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    next: bool | None = True,
    center: bool | None = True,
) -> None:
    """Move frame to previous edit point

    :type execution_context: int | str | None
    :type undo: bool | None
    :param next: Next Strip
    :type next: bool | None
    :param center: Use Strip Center
    :type center: bool | None
    """

def strip_modifier_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: str | None = "",
) -> None:
    """Add a modifier to the strip

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: str | None
    """

def strip_modifier_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["REPLACE", "APPEND"] | None = "REPLACE",
) -> None:
    """Copy modifiers of the active strip to all selected strips

        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    REPLACE
    Replace -- Replace modifiers in destination.

    APPEND
    Append -- Append active modifiers to selected strips.
        :type type: typing.Literal['REPLACE','APPEND'] | None
    """

def strip_modifier_equalizer_redefine(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    graphs: typing.Literal["SIMPLE", "DOUBLE", "TRIPLE"] | None = "SIMPLE",
    name: str = "Name",
) -> None:
    """Redefine equalizer graphs

        :type execution_context: int | str | None
        :type undo: bool | None
        :param graphs: Graphs, Number of graphs

    SIMPLE
    Unique -- One unique graphical definition.

    DOUBLE
    Double -- Graphical definition in 2 sections.

    TRIPLE
    Triplet -- Graphical definition in 3 sections.
        :type graphs: typing.Literal['SIMPLE','DOUBLE','TRIPLE'] | None
        :param name: Name, Name of modifier to redefine
        :type name: str
    """

def strip_modifier_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "Name",
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
) -> None:
    """Move modifier up and down in the stack

        :type execution_context: int | str | None
        :type undo: bool | None
        :param name: Name, Name of modifier to remove
        :type name: str
        :param direction: Type

    UP
    Up -- Move modifier up in the stack.

    DOWN
    Down -- Move modifier down in the stack.
        :type direction: typing.Literal['UP','DOWN'] | None
    """

def strip_modifier_move_to_index(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
    index: int | None = 0,
) -> None:
    """Change the strip modifiers index in the stack so it evaluates after the set number of others

    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the modifier to edit
    :type modifier: str
    :param index: Index, The index to move the modifier to
    :type index: int | None
    """

def strip_modifier_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "Name",
) -> None:
    """Remove a modifier from the strip

    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of modifier to remove
    :type name: str
    """

def strip_modifier_set_active(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    modifier: str = "",
) -> None:
    """Activate the strip modifier to use as the context

    :type execution_context: int | str | None
    :type undo: bool | None
    :param modifier: Modifier, Name of the strip modifier to edit
    :type modifier: str
    """

def strip_transform_clear(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    property: typing.Literal["POSITION", "SCALE", "ROTATION", "ALL"] | None = "ALL",
) -> None:
    """Reset image transformation to default value

        :type execution_context: int | str | None
        :type undo: bool | None
        :param property: Property, Strip transform property to be reset

    POSITION
    Position -- Reset strip transform location.

    SCALE
    Scale -- Reset strip transform scale.

    ROTATION
    Rotation -- Reset strip transform rotation.

    ALL
    All -- Reset strip transform location, scale and rotation.
        :type property: typing.Literal['POSITION','SCALE','ROTATION','ALL'] | None
    """

def strip_transform_fit(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    fit_method: bpy.stub_internal.rna_enums.StripScaleMethodItems | None = "FIT",
) -> None:
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param fit_method: Fit Method, Mode for fitting the image to the canvas
    :type fit_method: bpy.stub_internal.rna_enums.StripScaleMethodItems | None
    """

def swap(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    side: typing.Literal["LEFT", "RIGHT"] | None = "RIGHT",
) -> None:
    """Swap active strip with strip to the right or left

    :type execution_context: int | str | None
    :type undo: bool | None
    :param side: Side, Side of the strip to swap
    :type side: typing.Literal['LEFT','RIGHT'] | None
    """

def swap_data(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Swap 2 sequencer strips

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def swap_inputs(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Swap the two inputs of the effect strip

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def text_cursor_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "LINE_BEGIN",
        "LINE_END",
        "TEXT_BEGIN",
        "TEXT_END",
        "PREVIOUS_CHARACTER",
        "NEXT_CHARACTER",
        "PREVIOUS_WORD",
        "NEXT_WORD",
        "PREVIOUS_LINE",
        "NEXT_LINE",
    ]
    | None = "LINE_BEGIN",
    select_text: bool | None = False,
) -> None:
    """Move cursor in text

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Where to move cursor to, to make a selection
    :type type: typing.Literal['LINE_BEGIN','LINE_END','TEXT_BEGIN','TEXT_END','PREVIOUS_CHARACTER','NEXT_CHARACTER','PREVIOUS_WORD','NEXT_WORD','PREVIOUS_LINE','NEXT_LINE'] | None
    :param select_text: Select Text, Select text while moving cursor
    :type select_text: bool | None
    """

def text_cursor_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select_text: bool | None = False,
) -> None:
    """Set cursor position in text

    :type execution_context: int | str | None
    :type undo: bool | None
    :param select_text: Select Text, Select text while moving cursor
    :type select_text: bool | None
    """

def text_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["NEXT_OR_SELECTION", "PREVIOUS_OR_SELECTION"]
    | None = "NEXT_OR_SELECTION",
) -> None:
    """Delete text at cursor position

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Which part of the text to delete
    :type type: typing.Literal['NEXT_OR_SELECTION','PREVIOUS_OR_SELECTION'] | None
    """

def text_deselect_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deselect all characters

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def text_edit_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy text to clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def text_edit_cut(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Cut text to clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def text_edit_mode_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Toggle text editing

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def text_edit_paste(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Paste text from clipboard

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def text_insert(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    string: str = "",
) -> None:
    """Insert text at cursor position

    :type execution_context: int | str | None
    :type undo: bool | None
    :param string: String, String to be inserted at cursor position
    :type string: str
    """

def text_line_break(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Insert line break at cursor position

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def text_select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select all characters

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def unlock(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Unlock strips so they can be transformed

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def unmute(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Unmute (un)selected strips

    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Unmute unselected rather than selected strips
    :type unselected: bool | None
    """

def view_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """View all the strips in the sequencer

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_all_preview(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Zoom preview to fit in the area

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_frame(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Move the view to the current frame

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_ghost_border(
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
    """Set the boundaries of the border used for offset view

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

def view_selected(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Zoom the sequencer on the selected strips

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_zoom_ratio(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 1.0,
) -> None:
    """Change zoom ratio of sequencer preview

    :type execution_context: int | str | None
    :type undo: bool | None
    :param ratio: Ratio, Zoom ratio, 1.0 is 1:1, higher is zoomed in, lower is zoomed out
    :type ratio: float | None
    """
