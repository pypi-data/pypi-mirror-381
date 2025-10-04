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

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

import jwt

from .session import HTTP, Route

__all__ = (
    "Address",
    "Alert",
    "EmergencyContact",
    "Message",
    "Message",
    "PropertyBranding",
    "Token",
    "Urgent",
    "UtilityInvoice",
    "Vehicle",
)


class Token:
    """TODO."""

    def __init__(self, token: str):
        self.value = token

        raw: dict = jwt.decode(token, options={"verify_signature": False})

        self.created_at = datetime.fromtimestamp(raw["iat"])
        self.expires_at = datetime.fromtimestamp(raw["exp"])

    def __str__(self):
        return self.value


@dataclass
class Address:
    """TODO."""

    street_line_1: str
    street_line_2: str | None
    street_line_3: str | None
    city: str
    county: str
    state_code: str
    province: str
    country_code: str
    postal_code: str


@dataclass
class EmergencyContact:
    """TODO."""

    id: int
    first_name: str
    last_name: str
    relationship: str
    email: str | None
    phone: str | None
    age: int
    has_access: bool
    address: dict
    company_name: str | None
    notes: str | None


@dataclass
class Alert:
    """TODO."""

    id: int
    title: str
    description: str
    action_title: str
    date: str
    alert_type_id: int
    alert_type: str
    reference_id: int
    priority: int
    dismissed: bool
    action_url: str


@dataclass
class PropertyBranding:
    """TODO."""

    primary_color: str
    secondary_color: str
    background_url: str | None
    color_logo_image_url: str | None
    white_logo_image_url: str | None
    property_image_url: str | None


@dataclass
class UtilityInvoice:
    """TODO."""

    id: int
    amount: float
    due_date: str
    download_url: str
    view_url: str

    def __repr__(self):
        return f"UtilityInvoice(id={self.id}, amount={self.amount}, due_date='{self.due_date}'"


@dataclass
class Vehicle:
    """TODO."""

    id: int
    make: str
    model: str
    year: str
    color: str
    state: type
    type: int
    license_plate: str
    fuel_type: str | None


class Urgent(Enum):
    NO = 0
    YES = 1


@dataclass
class Message:
    """TODO."""

    id: int
    subject: str
    read: bool
    _urgent_raw: str = field(init=True, repr=False)
    urgent: Urgent = field(init=False)
    sender: str
    created: str
    _session: HTTP

    def __post_init__(self):
        self.urgent = Urgent(self._urgent_raw)

    async def get_message_content(self) -> dict[str, str]:
        """TODO."""
        return await self._session._api_request(
            Route("GET", controller="messages", action="getContent"),
            params={"id": self.id},
        )


@dataclass
class Inspection:
    """TODO."""

    id: int
    name: str
    due_date: str
    staff_inspection: bool
    reviewed_on: str
    inspected_on: str
    updated_by: str | None
    status: str

class Profile:
    """TODO."""

    def __init__(self, data: dict):
        self.preferred_name: str | None = data["preferred_name"]
        self.pronoun_picklist_id: int | None = data["pronoun_picklist_id"]
        self.first_name: str = data["first_name"]
        self.last_name: str = data["last_name"]
        self.middle_name: str = data["middle_name"]
        self.email_address: str = data["email_address"]
        self.maternal_last_name: str | None = data["maternal_last_name"]
        self.primary_phone_number: str = data["primary_phone_number"]
        self.primary_phone_type: int = data["primary_phone_type"]
        self.primary_phone_sms_opted_in: bool = data["primary_phone_sms_opted_in"]
        self.secondary_phone_number: str = data["secondary_phone_number"]
        self.secondary_phone_type: int | None = data["secondary_phone_type"]
        self.secondary_phone_sms_opted_in: bool = data["secondary_phone_sms_opted_in"]
        self.customer_address: str = data["customer_address"]
        self.image_url: str = data["image_url"]
        self.phone_numbers: list[dict] = data["phone_numbers"]
