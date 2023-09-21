from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("src")
except PackageNotFoundError:
    __version__ = "unknown version"