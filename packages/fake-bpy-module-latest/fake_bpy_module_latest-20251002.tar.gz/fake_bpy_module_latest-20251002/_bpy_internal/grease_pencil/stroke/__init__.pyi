import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class AttributeGetterSetter:
    """Helper class to get and set attributes at an index for a domain."""

class BezierHandle:
    LEFT: typing.Any
    RIGHT: typing.Any
    name: typing.Any
    value: typing.Any

class GreasePencilStrokePointHandle:
    """Proxy giving read-only/write access to Bézier handle data."""

    position: typing.Any
    select: typing.Any
    type: typing.Any

class SliceHelper:
    """Helper class to handle custom slicing."""

class GreasePencilStroke(AttributeGetterSetter):
    """A helper class to get access to stroke data."""

    aspect_ratio: typing.Any
    curve_type: typing.Any
    cyclic: typing.Any
    end_cap: typing.Any
    fill_color: typing.Any
    fill_opacity: typing.Any
    material_index: typing.Any
    points: typing.Any
    select: typing.Any
    softness: typing.Any
    start_cap: typing.Any
    time_start: typing.Any

    def add_points(self, count) -> None:
        """Add new points at the end of the stroke and returns the new points as a list.

        :param count:
        """

    def remove_points(self, count) -> None:
        """Remove points at the end of the stroke.

        :param count:
        """

class GreasePencilStrokePoint(AttributeGetterSetter):
    """A helper class to get access to stroke point data."""

    delta_time: typing.Any
    handle_left: typing.Any
    handle_right: typing.Any
    opacity: typing.Any
    position: typing.Any
    radius: typing.Any
    rotation: typing.Any
    select: typing.Any
    vertex_color: typing.Any

class GreasePencilStrokePointSlice(SliceHelper):
    """A helper class that represents a slice of GreasePencilStrokePoints."""

class GreasePencilStrokeSlice(SliceHelper):
    """A helper class that represents a slice of GreasePencilStrokes."""

def DefAttributeGetterSetters(attributes_list) -> None:
    """A class decorator that reads a list of attribute information &
    creates properties on the class with getters & setters.

    """

def def_prop_for_attribute(attr_name, type, default, doc) -> None:
    """Creates a property that can read and write an attribute."""
