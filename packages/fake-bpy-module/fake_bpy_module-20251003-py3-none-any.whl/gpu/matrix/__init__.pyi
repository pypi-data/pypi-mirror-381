"""
This module provides access to the matrix stack.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import mathutils

def get_model_view_matrix() -> mathutils.Matrix:
    """Return a copy of the model-view matrix.

    :return: A 4x4 view matrix.
    :rtype: mathutils.Matrix
    """

def get_normal_matrix() -> mathutils.Matrix:
    """Return a copy of the normal matrix.

    :return: A 3x3 normal matrix.
    :rtype: mathutils.Matrix
    """

def get_projection_matrix() -> mathutils.Matrix:
    """Return a copy of the projection matrix.

    :return: A 4x4 projection matrix.
    :rtype: mathutils.Matrix
    """

def load_identity() -> None:
    """Load an identity matrix into the stack."""

def load_matrix(
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix,
) -> None:
    """Load a matrix into the stack.

    :param matrix: A 4x4 matrix.
    :type matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix
    """

def load_projection_matrix(
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix,
) -> None:
    """Load a projection matrix into the stack.

    :param matrix: A 4x4 matrix.
    :type matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix
    """

def multiply_matrix(
    matrix: collections.abc.Sequence[collections.abc.Sequence[float]]
    | mathutils.Matrix,
) -> None:
    """Multiply the current stack matrix.

    :param matrix: A 4x4 matrix.
    :type matrix: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix
    """

def pop() -> None:
    """Remove the last model-view matrix from the stack."""

def pop_projection() -> None:
    """Remove the last projection matrix from the stack."""

def push() -> None:
    """Add to the model-view matrix stack."""

def push_pop() -> None:
    """Context manager to ensure balanced push/pop calls, even in the case of an error."""

def push_pop_projection() -> None:
    """Context manager to ensure balanced push/pop calls, even in the case of an error."""

def push_projection() -> None:
    """Add to the projection matrix stack."""

def reset() -> None:
    """Empty stack and set to identity."""

def scale(scale: collections.abc.Sequence[float]) -> None:
    """Scale the current stack matrix.

    :param scale: Scale the current stack matrix with 2 or 3 floats.
    :type scale: collections.abc.Sequence[float]
    """

def scale_uniform(scale: float) -> None:
    """

    :param scale: Scale the current stack matrix.
    :type scale: float
    """

def translate(offset: collections.abc.Sequence[float]) -> None:
    """Scale the current stack matrix.

    :param offset: Translate the current stack matrix with 2 or 3 floats.
    :type offset: collections.abc.Sequence[float]
    """
