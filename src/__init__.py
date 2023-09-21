from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("src")
except PackageNotFoundError:
    __version__ = "unknown version"
