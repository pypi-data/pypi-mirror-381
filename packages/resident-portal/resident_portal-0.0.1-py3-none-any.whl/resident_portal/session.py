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

from datetime import datetime
from typing import TYPE_CHECKING, Any

import aiohttp
from loguru import logger

from . import exceptions

if TYPE_CHECKING:
    from user import User

__all__ = ("HTTP", "Route")


class Route:
    """Class to represent a API route.

    Parameters
    ----------
    method: :class:`str`
        The HTTP method to use, i.e. GET or POST.
    parameters: :class:`dict`
        The url parameters to be used.
        AT MINIMUM an `action` and `controller` parameter must be passed.

    """

    def __init__(self, method: str, **parameters: Any) -> None:
        self.method: str = method
        self.parameters: dict = parameters

        if "controller" not in self.parameters or "action" not in self.parameters:
            raise exceptions.BadRoute


class HTTP:
    """Class for completing HTTP requests."""

    __slots__ = (
        "_BASE_API_URL",
        "_DEFAULT_HEADERS",
        "_session",
        "_user",
    )

    def __init__(self, subdomain: str, session: aiohttp.ClientSession | None):
        self._BASE_API_URL = f"https://{subdomain}.residentportal.com/api/"
        self._DEFAULT_HEADERS = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",  # noqa: E501
            "X-Consumer": "rpweb",
            "X-Consumer-Version": "1.0",
        }
        self._session = session if session else aiohttp.ClientSession()
        self._session.headers.update(self._DEFAULT_HEADERS)
        self._user: User | None = None

    async def _api_request(
        self,
        route: Route,
        json: dict | None = None,
    ) -> dict | str:
        """Call an api request

        Parameters
        ----------
        route: :class:`.Route`
            API route information
        json: :class:`dict`
            JSON data to be passed along in the request

        Returns
        -------
        :class:`dict`
            API endpoint response data

        Raises
        ------
        :class:`.Forbidden`
            `Represents a HTTP `403` code. You could either not be logged in,
            or not able to preform the function
        :class:`.NotFound`
            `Represents a HTTP `404` code. You could either not be logged in,
            or you passed a bad :class:`Route`
        :class:`.HTTPError`
            General HTTP Error when HTTP the following status codes aren't raised:
                `404`, `403`, `200-300`

        """
        async with self._session.request(
            method=route.method,
            url=self._BASE_API_URL,
            params=route.parameters,
            json=json,
        ) as response:
            if self._user and datetime.now() >= self._user.token.expires_at:
                self._user.get_token()

            data = await response.json(content_type="text/html")
            code = response.status

            if 300 > code >= 200:
                logger.success(f"{response.method} {response.url} - {code}")
                return data
            if code == 403:
                raise exceptions.Forbidden(response, data)
            if code == 404:
                raise exceptions.NotFound(response, data)

            raise exceptions.HTTPError(response, data)

    def add_session_headers(self, headers: dict) -> None:
        """Add headers to the session.

        ..warning
            All needed headers are automatically added.
            Adding custom headers could possibly have adverse effects.

        """
        self._session.headers.update(headers)

    async def close(self) -> None:
        """Call the :meth:`aiohttp.ClientSession.close()`"""
        await self._session.close()
