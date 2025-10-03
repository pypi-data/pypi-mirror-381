"""
This module provides access to image buffer types.

[NOTE]
Image buffer is also the structure used by bpy.types.Image
ID type to store and manipulate image data at runtime.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class ImBuf:
    channels: int
    """ Number of bit-planes.

    :type: int
    """

    filepath: str
    """ filepath associated with this image.

    :type: str
    """

    planes: int
    """ Number of bits associated with this image.

    :type: int
    """

    ppm: tuple[float, float]
    """ pixels per meter.

    :type: tuple[float, float]
    """

    size: tuple[int, int]
    """ size of the image in pixels.

    :type: tuple[int, int]
    """

    def copy(self) -> typing_extensions.Self:
        """

        :return: A copy of the image.
        :rtype: typing_extensions.Self
        """

    def crop(self, min: tuple[int, int], max: tuple[int, int]) -> None:
        """Crop the image.

        :param min: X, Y minimum.
        :type min: tuple[int, int]
        :param max: X, Y maximum.
        :type max: tuple[int, int]
        """

    def free(self) -> None:
        """Clear image data immediately (causing an error on re-use)."""

    def resize(self, size: tuple[int, int], *, method: str = "FAST") -> None:
        """Resize the image.

        :param size: New size.
        :type size: tuple[int, int]
        :param method: Method of resizing (FAST, BILINEAR)
        :type method: str
        """
