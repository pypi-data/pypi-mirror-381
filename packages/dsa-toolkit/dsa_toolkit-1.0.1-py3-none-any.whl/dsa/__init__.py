"""
DSA Toolkit - Data Structures and Algorithms

A collection of essential algorithms and data structures for learning and practice.
"""

__version__ = "1.0.1"

# Core modules
from . import sorting
from . import searching
from . import graph
from . import recursion
from . import utils
from . import structures
from . import algorithms

# Import commonly used functions for convenience
from .sorting import bubble_sort, merge_sort, quick_sort

__all__ = [
    # Core modules
    'sorting',
    'searching',
    'graph',
    'recursion', 
    'utils',
    'structures', 
    'algorithms',
    # Common functions
    'bubble_sort',
    'merge_sort', 
    'quick_sort'
]
