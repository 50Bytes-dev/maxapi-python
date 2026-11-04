from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QRGeneratedEvent")


@_attrs_define
class QRGeneratedEvent:
    """A QR login started, or MAX's QR expired and the gateway issued a new one (up to 10 times).

    Attributes:
        type_ (Literal['QRGenerated']):
        qr_link (str): MAX's login link the QR encodes
        qr_code_base_64 (str): The same PNG data URL as `GET /session/qr` Example: data:image/png;base64,iVBORw0KGgo....
        track_id (str): MAX's id of this QR
        expires_at (int): When MAX expires this QR, as MAX gives it
        user_id (str): The account id (`userID` and `instanceID` are the same) Example:
            6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
        instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
            6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
        instance_name (str): The account name; "" when the gateway could not read it Example: Shop bot.
        event_timestamp (int): Unix time in seconds, set when the delivery starts; a retry keeps it Example: 1793001234.
    """

    type_: Literal["QRGenerated"]
    qr_link: str
    qr_code_base_64: str
    track_id: str
    expires_at: int
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        qr_link = self.qr_link

        qr_code_base_64 = self.qr_code_base_64

        track_id = self.track_id

        expires_at = self.expires_at

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "qrLink": qr_link,
                "qrCodeBase64": qr_code_base_64,
                "trackId": track_id,
                "expiresAt": expires_at,
                "userID": user_id,
                "instanceID": instance_id,
                "instanceName": instance_name,
                "eventTimestamp": event_timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["QRGenerated"], d.pop("type"))
        if type_ != "QRGenerated":
            raise ValueError(f"type must match const 'QRGenerated', got '{type_}'")

        qr_link = d.pop("qrLink")

        qr_code_base_64 = d.pop("qrCodeBase64")

        track_id = d.pop("trackId")

        expires_at = d.pop("expiresAt")

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        qr_generated_event = cls(
            type_=type_,
            qr_link=qr_link,
            qr_code_base_64=qr_code_base_64,
            track_id=track_id,
            expires_at=expires_at,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
        )

        qr_generated_event.additional_properties = d
        return qr_generated_event

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
