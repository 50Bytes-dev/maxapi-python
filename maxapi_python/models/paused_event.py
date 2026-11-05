from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PausedEvent")


@_attrs_define
class PausedEvent:
    """The MAX account was paused: MAX answered a call of one of its gateway
    accounts with a limit or restriction error. Every gateway account of the
    MAX account subscribed to `Paused` (or `All`) gets it, also one without a
    session. Until `POST /session/resume` no call of any of them reaches MAX.

        Attributes:
            type_ (Literal['Paused']):
            max_user_id (int): The MAX id of the account's MAX user Example: 123456789.
            pause_reason (str): Why the MAX account is paused. maxapi gives only `spam` (a limit or restriction error of
                MAX). Example: spam.
            upstream_code (str): MAX's code that paused the account Example: error.user.restricted.send.
            user_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_name (str): The account name; "" when the gateway could not read it Example: Shop bot.
            event_timestamp (int): Unix time in seconds, set when the delivery starts; a retry keeps it Example: 1793001234.
    """

    type_: Literal["Paused"]
    max_user_id: int
    pause_reason: str
    upstream_code: str
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        max_user_id = self.max_user_id

        pause_reason = self.pause_reason

        upstream_code = self.upstream_code

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "maxUserID": max_user_id,
                "pauseReason": pause_reason,
                "upstreamCode": upstream_code,
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
        type_ = cast(Literal["Paused"], d.pop("type"))
        if type_ != "Paused":
            raise ValueError(f"type must match const 'Paused', got '{type_}'")

        max_user_id = d.pop("maxUserID")

        pause_reason = d.pop("pauseReason")

        upstream_code = d.pop("upstreamCode")

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        paused_event = cls(
            type_=type_,
            max_user_id=max_user_id,
            pause_reason=pause_reason,
            upstream_code=upstream_code,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
        )

        paused_event.additional_properties = d
        return paused_event

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
