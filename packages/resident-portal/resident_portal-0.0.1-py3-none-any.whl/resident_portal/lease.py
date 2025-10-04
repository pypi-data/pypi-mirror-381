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

from typing import Any

from . import exceptions, models
from .session import HTTP, Route

__all__ = ("Lease",)


class Lease:
    """TODO."""

    def __init__(self, data: dict, session: HTTP):
        self.lease_id: int = data["lease_id"]
        self.lease_status: str = data["lease_status"]
        self.property_unit_id: str = data["property_unit_id"]
        self.unit_number: str = data["unit_number"]
        self.is_smart: bool = data["unit_is_smart"]
        self.building_name: str = data["building_name"]
        self.lease_under_eviction: bool = data["is_lease_under_eviction"]
        self.primary_lease_holder_name: str = data["primary_lease_holder_name"]
        self.lease_term: str = data["lease_term"]
        self._session: HTTP = session

    async def get_ledger(
        self,
        page: int = 0,
        per_page: int = 0,
        with_settings: bool = False,
    ) -> None:
        """TODO."""
        action = "getLedgerWithSettings" if with_settings else "getLedger"
        return await self._session._api_request(
            Route("GET", controller="ledger", action=action, page=page, per_page=per_page),
        )

    async def get_product_permissions(self) -> None:
        """TODO.
        Returns getPropertyProductPermissions & getLeaseProductPermissions
        by just using getProductPermissions.
        """
        return await self._session._api_request(
            Route("GET", controller="permissions", action="getProductPermissions"),
        )

    async def get_lease_balance(self, with_details: bool = False) -> dict:
        """TODO."""
        action = "getLeaseBalanceDetails" if with_details else "getLeaseBalance"
        return await self._session._api_request(
            Route("GET", controller="balance", action=action),
        )

    async def get_scheduled_total(self) -> dict:
        """TODO."""
        return await self._session._api_request(
            Route("GET", controller="balance", action="getScheduledChargeTotal"),
        )

    async def get_property_contact(self, with_settings: bool = False) -> dict:
        """TODO."""
        action = "getContactInfoWithSettings" if with_settings else "getContactInfo"
        return await self._session._api_request(
            Route("GET", controller="property_contact", action=action),
        )

    async def get_documents(self, with_settings: bool = False) -> dict:
        """TODO."""
        action = "listWithSettings" if with_settings else "list"
        return await self._session._api_request(
            Route("GET", controller="documents", action=action),
        )

    async def get_tenant_permissions(self) -> None:
        """TODO."""
        return await self._session._api_request(
            Route("GET", controller="tenant_permissions", action="getProductPermissions"),
        )

    async def get_guest_list(self, with_settings: bool = False) -> dict:
        """TODO."""
        action = "listWithSettings" if with_settings else "list"
        return await self._session._api_request(
            Route("GET", controller="guest_list", action=action),
        )

    async def get_utilities_usage(self) -> dict:
        """TODO."""
        return await self._session._api_request(
            Route("GET", controller="utilities", action="getUsage"),
        )

    async def get_utility_invoices(self) -> list[models.UtilityInvoice]:
        """TODO."""
        invoices = await self._session._api_request(
            Route("GET", controller="utility_invoice", action="getInvoices"),
        )

        return [models.UtilityInvoice(*list(i.values())) for i in invoices["invoices"]]

    async def get_vehicles(
        self,
        with_settings: bool = False,
    ) -> list[models.Vehicle] | dict[models.Vehicle, dict]:
        """TODO."""
        action = "listWithSettings" if with_settings else "list"
        vehicle_data = await self._session._api_request(
            Route("GET", controller="vehicles", action=action),
        )

        if with_settings:
            v_list = [models.Vehicle(*list(v.values())) for v in vehicle_data["list"]]
            return {"list": v_list, "settings": vehicle_data["settings"]}

        return [models.Vehicle(*list(v.values())) for v in vehicle_data]

    async def get_services(self, with_settings: bool = False) -> list[Any]:
        """TODO."""
        action = "listWithSettings" if with_settings else "list"
        return await self._session._api_request(
            Route("GET", controller="services", action=action),
        )

    async def get_services_requests(self) -> list[Any]:
        """TODO."""
        return await self._session._api_request(
            Route("GET", controller="services", action="listRequests"),
        )

    async def get_inspections(self, with_settings: bool = False) -> None:
        """TODO."""
        action = "listWithSettings" if with_settings else "list"
        inspections = await self._session._api_request(
            Route("GET", controller="inspections", action=action),
        )
        if with_settings:
            i_list = [models.Inspection(*list(i.values())) for i in inspections["inspections"]]
            return {"list": i_list, "settings": inspections["settings"]}

        return [models.Inspection(*list(i.values())) for i in inspections["inspections"]]

    async def get_inspection(self, inspection_id: int) -> dict:
        """TODO."""
        inspection = await self._session._api_request(
            Route("GET", controller="inspections", action="getInspection", inspection_id=inspection_id),
        )
        return inspection["inspection"]

    async def get_autopay_status(self) -> None:
        """TODO."""
        status = await self._session._api_request(
            Route("GET", controller="scheduled_payments", action="getAutoPaymentStatus"),
        )
        return not status["status"] == "inactive"

    async def get_amenities(self, with_settings: bool = False) -> list | None:
        """TODO."""
        action = "listWithSettings" if with_settings else "list"

        try:
            return await self._session._api_request(
                Route("GET", controller="amenities", action=action),
            )
        except exceptions.HTTPError:
            return None

    async def get_announcements(self) -> list | None:
        """TODO."""
        return await self._session._api_request(
            Route("GET", controller="announcements", action="list"),
        )
