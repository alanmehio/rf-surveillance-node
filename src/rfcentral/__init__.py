"""

| **RF Central**, a *Python Package* receive high power RF data from different nodes

|

"""

__version__ = "0.0.1"

__all__ = (
    "__version__",
    "main",
)

# bootstrap it
from .rest_api import rest
