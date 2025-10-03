from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("nextepoch")
except PackageNotFoundError:
    __version__ = "0.0.0"

from .myco import MycoClient

__all__ = ["MycoClient", "__version__"]
