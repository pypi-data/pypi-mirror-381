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

from . import exceptions, models
from .lease import Lease
from .session import HTTP, Route

if TYPE_CHECKING:
    from aiohttp import ClientSession

__all__ = ("User",)


class User:
    """Represents an account holder with Resident Portal.
    Class used to interact with the API

    Parameters
    ----------
    username: :class:`str`
        Resident Portal username. Typically your email.
    password: :class:`str`
        Account password
    subdomain: :class:`str`
        Your propertys subdomain with resident portal.
        If the url you visit to login is `atlanta.residentportal.com`,
        then you would pass `atlanta`
    session: Optional[:class:`aiohttp.ClientSession`]
        Pass your own client session instance to avoid using an extra
        if you are using this inside of a program that already has one
        instantiated.

    Attributes
    ----------
    cid :class:`int`
        Not exactly sure the purpose of this on the RP side
    property_id :class:`int`
        Your propertys Resident Portal id
    property_name :class:`str`
        Your propertys name
    first_name :class:`str`
        Your First Name
    last_name :class:`str`
        Your Last Name
    customer_id :class:`int`
        Your Resident Portal customer id
    token :class:`.Token`
        The token class used for interacting with the api
    address :class:`dict`
        Raw address data
    leases List[:class:`Lease`]
        List of your leases at the property
    country_code :class:`str`
        Your country code
    property_address :class:`.Address`
        The propertys address
    is_rename_lease_and_rent_set :class:`bool`
        Given in the name
    property_office_phone_numbers List[:class:`str`]
        Given in the name
    parent_property_id
        Unknown | Unable to confirm

    """

    __slots__ = (
        "_username",
        "_password",
        "_subdomain",
        "_session",
        "cid",
        "property_id",
        "property_name",
        "first_name",
        "last_name",
        "customer_id",
        "token",
        "address",
        "leases",
        "country_code",
        "property_address",
        "is_rename_lease_and_rent_set",
        "property_office_phone_numbers",
        "parent_property_id",
    )

    def __init__(self, username: str, password: str, subdomain: str, session: ClientSession | None = None):
        self._username = username
        self._password = password
        self._subdomain = subdomain
        self._session: HTTP = HTTP(self._subdomain, session)

    def _update(self, data: dict, token: models.Token) -> None:
        self.cid: int = data["cid"]
        self.property_id: int = data["property_id"]
        self.property_name: str = data["property_name"]
        self.first_name: str = data["first_name"]
        self.last_name: str = data["last_name"]
        self.customer_id: int = data["customer_id"]
        self.token: models.Token = token
        self.address: dict = data["address"]
        self.leases: list[Lease] = [Lease(data["leases"][0], self._session)]
        self.country_code: str = data["country_code"]
        self.property_address = models.Address(*list(data["property_address"].values()))
        self.is_rename_lease_and_rent_set: bool = data["isRenameLeaseAndRentSet"]
        self.property_office_phone_numbers: list = data["property_office_phone_numbers"]
        self.parent_property_id: int | None = data["parent_property_id"]

    @property
    def name(self) -> str:
        """Combine first and last name into one string."""
        return f"{self.first_name} {self.last_name}"

    async def login(self) -> None:
        """Shortcut to :meth:`get_token()`"""
        await self.get_token()

    async def get_token(self) -> None:
        """Log the user in with the specified credentials. Obtain token to be used during API calls.
        This is manually called when the class is initialized.
        """
        req = await self._session._api_request(
            Route("POST", controller="user", action="login"),
            json={"username": self._username, "password": self._password},
        )

        try:
            token: models.Token = models.Token(
                req["user_properties"][0]["leases"][0]["token"],
            )
        except KeyError as e:
            raise exceptions.LoginError from e

        self._update(req["user_properties"][0], token)
        self._session._user = self
        self._session.add_session_headers({"Authorization": f"Bearer {token}"})

    async def logout(self) -> None:
        """Log the user out

        .. warning::

            When calling this function, you must in turn use :meth:login() or :meth:get_token() before
            any further requests can be made as the :class:`resident_portal.Token` is no longer valid.
        """
        await self._session._api_request(
            Route("GET", controller="user", action="logout"),
        )

    async def get_alerts(self, days: int = 30) -> list[models.Alert] | None:
        """Fetch alerts. Seems to only return alerts which have not been handled.
        For example, you need to sign your lease renewal

        Parameters
        ----------
        days: :class:`int`
            Days back to fetch alerts

        Returns
        -------
        List[:class:`.Alert`]

        """
        alerts = await self._session._api_request(
            Route("GET", controller="alerts", action="list", days=days),
        )

        return [models.Alert(*list(alert.values())) for alert in alerts]

    async def get_property_branding(self) -> dict:
        """Return your property's branding.

        Returns
        -------
        :class:`.PropertyBranding`

        """
        data = await self._session._api_request(
            Route("GET", controller="property", action="getBranding"),
        )
        return models.PropertyBranding(*list(data.values()))

    async def get_notification_settings(self) -> list[dict]:
        """Return a :class:`list` of various notification settings in a :class:`dict`."""
        return await self._session._api_request(
            Route("GET", controller="notification_settings", action="getSettings"),
        )

    async def get_messages(
        self,
        page: int = 0,
        per_page: int = 0,
    ) -> list[models.Message | None]:
        """Return all messages received. You can limit to the amount per page
        and view individual pages by callthing the method again.

        Example
        -------
        Say there are 25 total messages
        ```
        get_messages() # All 25 messages
        get_messages(page=1, per_page=5) # View the first 5 messages of 25
        get_messages(page=2, per_page=5) # View messages 6-10 of 25
        ```

        Parameters
        ----------
        page: :class:`int`
            Page to view of messages (See example)
        per_page: :class:`int`
            Amount of messages per page (See example)

        Returns
        -------
        List[:class:`.Message`]

        """
        messages = await self._session._api_request(
            Route("GET", controller="messages", action="list", page_number=page, page_size=per_page),
        )

        return [models.Message(*list(m.values()), self._session) for m in messages["messages"]]

    async def get_property_associations(self) -> dict[str, list]:
        """Show raw property information, as well as raw lease information.
        The raw lease information is the same information stored in the :attr:`User.leases`
        lease class.

        ..warning:

            The dict returned will show your token which can be used to access your account
            and perform dangerous functions.

        Returns
        -------
        Dict[:class:`str`, :class:`list`]
            Raw property and lease information

        """
        return await self._session._api_request(
            Route("GET", controller="user", action="getPropertyAssociations"),
        )

    async def get_emergency_contacts(self) -> models.EmergencyContact:
        """View emergency contacts.

        Returns
        -------
        :class:`.EmergencyContact`

        """
        req = await self._session._api_request(
            Route("GET", controller="emergency_contacts", action="list"),
        )

        return [models.EmergencyContact(*list(ec.values())) for ec in req]

    async def get_profile(self, with_settings: bool = False) -> models.Profile | tuple[models.Profile, dict]:
        """View profile information and optionally settings.

        Parameters
        ----------
        with_settings: :class:`bool`
            Wether or not to also return profile_settings

        Returns
        -------
        :class:`.Profile`

        - If `with_settings` is `True`:
            Returns: Tuple[:class:`.Profile`, :class:`dict`]

        """
        action = "getProfileWithSettings" if with_settings else "getProfile"
        data = await self._session._api_request(
            Route("GET", controller="customer_profile", action=action),
        )

        if with_settings:
            return models.Profile(data["customer_profile"]), {
                "pronouns": data["pronouns"],
                "settings": data["settings"],
            }

        return models.Profile(data)

    async def get_account_settings(self) -> list[dict | None]:
        """Get account settings.

        I am unsure what exactly what this returns as for me Resident Portal
        only shows `[]`, but I am assuming there would be a dict inside the list.

        Returns
        -------
        List[:class:`dict` | `None`]

        """
        return await self._session._api_request(
            Route("GET", controller="account_settings", action="getSettings"),
        )
