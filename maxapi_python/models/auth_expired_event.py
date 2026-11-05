from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_expired_event_reason import AuthExpiredEventReason

T = TypeVar("T", bound="AuthExpiredEvent")


@_attrs_define
class AuthExpiredEvent:
    """The session stopped and will not reconnect by itself. `reason` says
    whether the stored login is gone (`token_revoked`, `page_blocked`,
    `logged_out`: a new QR login through `POST /session/connect` is needed)
    or kept (`refresh_failed`: `POST /session/connect` tries it again). The
    gateway account stays in every case. MAX's own text goes to the log
    only.

        Attributes:
            type_ (Literal['AuthExpired']):
            reason (AuthExpiredEventReason): `token_revoked`: MAX refused the stored login (login.token and the
                like, or the account is gone); the login is erased.
                `page_blocked`: MAX blocked the account (login.blocked); the login is
                erased. `refresh_failed`: MAX refused 3 logins in a row, or answered
                login.flood; the login is kept. `logged_out`: MAX ended the session
                (from the MAX app, or MAX itself); the login is erased. Example: refresh_failed.
            user_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_name (str): The account name; "" when the gateway could not read it Example: Shop bot.
            event_timestamp (int): Unix time in seconds, set when the delivery starts; a retry keeps it Example: 1793001234.
    """

    type_: Literal["AuthExpired"]
    reason: AuthExpiredEventReason
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        reason = self.reason.value

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["AuthExpired"], d.pop("type"))
        if type_ != "AuthExpired":
            raise ValueError(f"type must match const 'AuthExpired', got '{type_}'")

        reason = AuthExpiredEventReason(d.pop("reason"))

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        auth_expired_event = cls(
            type_=type_,
            reason=reason,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
        )

        auth_expired_event.additional_properties = d
        return auth_expired_event

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
