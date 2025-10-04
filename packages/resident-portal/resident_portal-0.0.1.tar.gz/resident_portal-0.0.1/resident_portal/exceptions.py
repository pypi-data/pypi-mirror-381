"""The MIT License (MIT)

Copyright (c) 2025-present Gavyn Stanley

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiohttp import ClientResponse

__all__ = (
    "BadRoute",
    "Forbidden",
    "HTTPError",
    "LoginError",
    "NotFound",
    "ResidentPortalError",
)


class ResidentPortalError(Exception):
    """Base exception class for resident_portal."""

    pass


class BadRoute(ResidentPortalError):
    """Exception that's raised when a route or controller is not passed in a route."""

    def __init__(self):
        super().__init__("A 'action' and 'controller' parameter must be passed.")


class HTTPError(ResidentPortalError):
    """Base HTTP Exception."""

    def __init__(self, resp: ClientResponse, body: str | dict):
        error_msg = body.get("message") if body else "Unknown Error"
        super().__init__(f"{resp.status} - {error_msg}")


class Forbidden(HTTPError):
    """Exception that's raised when a HTTP 403 response is received."""

    def __init__(self, resp: ClientResponse, body: str | dict):
        error_msg = body.get("message") if body else "Unknown Error"
        super().__init__(f"{resp.status} - {error_msg}")


class NotFound(HTTPError):
    """Exception that's raised when a HTTP 404 response is received."""

    def __init__(self, resp: ClientResponse, body: str | dict):
        error_msg = body.get("message") if body else "Unknown Error"
        super().__init__(f"{resp.status} - {error_msg}")


class LoginError(ResidentPortalError):
    """Exception that's raised when the :meth:`RPClient.login` function fails due to
    improper credentials or other misc. failures.
    """

    def __init__(self):
        super().__init__("Failed to retrieve token")
