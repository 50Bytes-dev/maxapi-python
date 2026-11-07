from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QRPasswordRequiredEvent")


@_attrs_define
class QRPasswordRequiredEvent:
    """After the scan MAX asks for the account's cloud password (two factor
    authentication); once per login. Ask the owner for it and send it with
    `POST /session/password` within 10 minutes. No new QR is issued.

        Attributes:
            type_ (Literal['QRPasswordRequired']):
            user_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_name (str): The account name; "" when the gateway could not read it Example: Shop bot.
            event_timestamp (int): Unix time in seconds, set when the delivery starts; a retry keeps it Example: 1793001234.
            hint (Union[Unset, str]): The hint the owner set for the password, when MAX gives one
            email (Union[Unset, str]): The recovery email, masked by MAX (`o***@mail.ru`), when MAX gives one
    """

    type_: Literal["QRPasswordRequired"]
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    hint: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

        hint = self.hint

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "userID": user_id,
                "instanceID": instance_id,
                "instanceName": instance_name,
                "eventTimestamp": event_timestamp,
            }
        )
        if hint is not UNSET:
            field_dict["hint"] = hint
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["QRPasswordRequired"], d.pop("type"))
        if type_ != "QRPasswordRequired":
            raise ValueError(f"type must match const 'QRPasswordRequired', got '{type_}'")

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        hint = d.pop("hint", UNSET)

        email = d.pop("email", UNSET)

        qr_password_required_event = cls(
            type_=type_,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
            hint=hint,
            email=email,
        )

        qr_password_required_event.additional_properties = d
        return qr_password_required_event

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
