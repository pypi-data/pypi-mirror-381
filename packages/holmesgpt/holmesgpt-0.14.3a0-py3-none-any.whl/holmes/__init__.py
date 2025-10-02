# This is patched by github actions during release
__version__ = "0.14.3-alpha"

# Re-export version functions from version module for backward compatibility
from .version import (
    get_version as get_version,
    is_official_release as is_official_release,
)
