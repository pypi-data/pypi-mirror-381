"""ResidentPortal API Wrapper.

A basic wrapper for the ResidentPortal API.

:copyright: (c) 2025-present Gavyn Stanley
:license: MIT, see LICENSE for more details.

"""

__title__ = "resident_portal"
__author__ = "Gavyn Stanley"
__version__ = "0.0.1"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from .exceptions import *
from .lease import *
from .models import *
from .session import *
from .user import *
