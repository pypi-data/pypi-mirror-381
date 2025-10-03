"""
dbbasic-pipe: SQL-style query optimization for Unix pipes

Brings bidirectional flow control to Unix pipelines, allowing downstream
commands to signal upstream to optimize data production.
"""

__version__ = "0.1.0"
__author__ = "Dan Quellhorst"
__license__ = "MIT"

from . import coordinator
from . import pcat
from . import pfilter
from . import plimit

__all__ = ["coordinator", "pcat", "pfilter", "plimit"]
