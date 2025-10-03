from abc import ABC
from datetime import date
from os import PathLike
from typing import ClassVar

from pycommence.pycmc_types import RowInfo
from pydantic import BaseModel, ConfigDict, Field, field_validator

from amherst.models.commence_adaptors import (
    AM_DATE,
    CategoryName,
    HireStatus,
    SaleStatus,
    customer_alias_generator,
    hire_alias_generator,
    replace_noncompliant_apostrophes,
    sale_alias_generator,
    split_addr_str2,
    trial_alias_generator,
)
from amherst.models.meta import register_table
from amherst.models.shipment import AmherstShipment
from shipaw.models.address import Address as AddressAgnost, Contact, FullContact
from shipaw.models.ship_types import ShipDirection


class AmherstShipableBase(BaseModel, ABC):
    category: ClassVar[CategoryName]
    model_config = ConfigDict(
        populate_by_name=True,
        use_enum_values=True,
    )

    def alias_lookup(self, field_name: str) -> str:
        try:
            return self.model_fields[field_name].alias
        except Exception:
            return field_name

    @field_validator('*', mode='before')
    def preprocess_strings(cls, value):
        return replace_noncompliant_apostrophes(value)

    row_info: RowInfo
    # amherst common fieldnames fields
    name: str = Field(..., alias='Name')
    tracking_numbers: str = Field('', alias='Tracking Numbers')
    track_out: str | None = None
    track_in: str | None = None

    # mandatory fields
    customer_name: str
    delivery_contact_name: str
    delivery_contact_business: str
    delivery_contact_phone: str
    delivery_contact_email: str
    delivery_address_str: str
    delivery_address_pc: str

    # optional fields with default
    send_date: AM_DATE = date.today()
    boxes: int = 1


    @field_validator('send_date', mode='after')
    def validate_send_date(cls, v: AM_DATE) -> date:
        if v is None or v < date.today():
            return date.today()
        return v

    @property
    def full_contact(self) -> FullContact:
        addrlines, town = split_addr_str2(self.delivery_address_str)
        return FullContact(
            contact=Contact(
                contact_name=self.delivery_contact_name,
                mobile_phone=self.delivery_contact_phone,
                email_address=self.delivery_contact_email,
            ),
            address=AddressAgnost(
                address_lines=addrlines,
                town=town,
                postcode=self.delivery_address_pc,
                business_name=self.delivery_contact_business,
            ),
        )

    def shipment(self, direction: ShipDirection = ShipDirection.OUTBOUND) -> 'AmherstShipment':
        return AmherstShipment(
            recipient=self.full_contact,
            boxes=self.boxes,
            shipping_date=self.send_date,
            direction=direction,
            reference=self.customer_name,
            context={'record': self},
        )

    # def shipment1(self, direction: ShipDirection = ShipDirection.OUTBOUND) -> Shipment:
    #     return Shipment(
    #         recipient=self.full_contact,
    #         boxes=self.boxes,
    #         shipping_date=self.send_date,
    #         direction=direction,
    #         reference=self.customer_name,
    #     )


class AmherstOrderBase(AmherstShipableBase, ABC):
    # order fields common
    status: str
    arranged_in: str | None = None
    arranged_out: str | None = None
    invoice: PathLike | None = None

    # order fields optional
    date_sent: AM_DATE | None = None
    booking_date: AM_DATE | None = None


@register_table
class AmherstCustomer(AmherstShipableBase):
    model_config = ConfigDict(
        alias_generator=customer_alias_generator,
        # alias_generator=lambda field_name: CustomerAliases[field_name.upper()].value,
    )
    category: ClassVar[CategoryName] = 'Customer'

    # customer fields
    invoice_email: str
    accounts_email: str
    hires: str = ''
    sales: str = ''


@register_table
class AmherstHire(AmherstOrderBase):
    # optional overrides master
    # aliases: ClassVar[StrEnum] = HireAliases
    model_config = ConfigDict(
        alias_generator=hire_alias_generator,
    )
    category: ClassVar[CategoryName] = 'Hire'

    boxes: int = 1
    delivery_contact_phone: str
    send_date: AM_DATE = date.today()

    delivery_method: str | None = None

    # optional overrides order
    status: HireStatus
    date_sent: AM_DATE | None = None
    booking_date: AM_DATE | None = None

    # hire fields
    missing_kit_str: str | None = None
    due_back_date: AM_DATE
    return_notes: str | None = None


@register_table
class AmherstSale(AmherstOrderBase):
    model_config = ConfigDict(
        alias_generator=sale_alias_generator,
    )
    category: ClassVar[CategoryName] = 'Sale'

    delivery_method: str | None = None

    # optional overrides order
    status: SaleStatus
    booking_date: AM_DATE = date.today()
    date_sent: AM_DATE | None = None

    # sale fields
    lost_equipment: str | None = None
    invoice_terms: str | None = None
    purchase_order: str | None = None
    items_ordered: str | None = None
    serial_numbers: str | None = None
    delivery_notes: str | None = None
    notes: str | None = None


@register_table
class AmherstTrial(AmherstOrderBase):
    # aliases: ClassVar[StrEnum] = TrialAliases
    model_config = ConfigDict(
        alias_generator=trial_alias_generator,
    )
    category: ClassVar[CategoryName] = 'Trial'


#
# class AmherstRepairs(AmherstOrderBase):
#     # category:CategoryName = CategoryName.Trial
#     customer_name: str = Field(..., alias='For Customer')
#     delivery_contact_name: str = Field(..., alias='Trial Contact')
#     delivery_contact_business: str = Field(..., alias='Trial Name')
#     delivery_contact_phone: str = Field(..., alias='Trial Telephone')
#     delivery_contact_email: str = Field(..., alias='Trial Email')
#     delivery_address_str: str = Field(..., alias='Trial Address')
#     delivery_address_pc: str = Field(..., alias='Trial Postcode')
#     tracking_numbers: str = Field('', alias='Tracking Numbers')
#
#     invoice: str = Field('', alias='Our Invoice')


AMHERST_ORDER_MODELS = AmherstHire | AmherstSale | AmherstTrial


