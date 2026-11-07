from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.qr_expired_event_reason import QRExpiredEventReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="QRExpiredEvent")


@_attrs_define
class QRExpiredEvent:
    """The QR login ended without logging in. Not sent when a connect, a
    disconnect, a logout or a delete stopped it.

        Attributes:
            type_ (Literal['QRExpired']):
            reason (QRExpiredEventReason): `login_expired`: MAX expired the QR after 10 new ones, the password
                was not entered in 10 minutes, or MAX refused it too often or ended
                the password step. `login_failed`: MAX refused the login, did not
                answer it, or could not be reached again after the connection
                dropped. `login_unsupported`: MAX asked for a step the gateway does
                not support (see `step`).
            user_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_name (str): The account name; "" when the gateway could not read it Example: Shop bot.
            event_timestamp (int): Unix time in seconds, set when the delivery starts; a retry keeps it Example: 1793001234.
            step (Union[Unset, str]): With `login_unsupported`: what MAX asked for, as MAX names it (the
                keys of its answer, e.g. `REGISTER`), or `password:<MAX's code>`
                when MAX would not take the password from the gateway.
    """

    type_: Literal["QRExpired"]
    reason: QRExpiredEventReason
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    step: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        reason = self.reason.value

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

        step = self.step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "reason": reason,
                "userID": user_id,
                "instanceID": instance_id,
                "instanceName": instance_name,
                "eventTimestamp": event_timestamp,
            }
        )
        if step is not UNSET:
            field_dict["step"] = step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["QRExpired"], d.pop("type"))
        if type_ != "QRExpired":
            raise ValueError(f"type must match const 'QRExpired', got '{type_}'")

        reason = QRExpiredEventReason(d.pop("reason"))

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        step = d.pop("step", UNSET)

        qr_expired_event = cls(
            type_=type_,
            reason=reason,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
            step=step,
        )

        qr_expired_event.additional_properties = d
        return qr_expired_event

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
