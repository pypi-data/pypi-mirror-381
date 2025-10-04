"""fbx-tool package.

Utilities for filtering FBX meshes and generating PCD point clouds.
"""

from importlib.metadata import version, PackageNotFoundError

try:  # pragma: no cover
    __version__ = version("fbx-tool")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0+dev"

from .cli import cli  # noqa: F401

__all__ = ["cli", "__version__"]