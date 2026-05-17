"""Ableton Live integration through the Model Context Protocol."""

__version__ = "0.1.0"

# Expose key classes and functions for easier imports
from .server import AbletonConnection, get_ableton_connection

# Also expose the version as a tuple for easier comparison
VERSION = tuple(int(x) for x in __version__.split("."))
