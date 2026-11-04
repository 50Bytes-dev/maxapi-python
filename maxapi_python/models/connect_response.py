from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectResponse")


@_attrs_define
class ConnectResponse:
    """
    Attributes:
        success (bool):  Example: True.
        details (str): "Awaiting QR scan", "Connected to MAX" or "Already connected to MAX" Example: Already connected
            to MAX.
        events (str): The stored subscription, comma-separated Example: Sync,QRAuthorized,AuthExpired,LoggedOut.
        already_connected (Union[Unset, bool]): Present (true) only when the session was already up
        paused (Union[Unset, bool]): Whether sending from the MAX account is paused; only with `alreadyConnected`
        pause_reason (Union[Unset, str]): Why sending from the MAX account is paused. maxapi gives only `spam` (a limit
            or restriction error of MAX). Example: spam.
        upstream_code (Union[Unset, str]): Only while paused (and `alreadyConnected`); the MAX error code that paused
            the account Example: error.user.restricted.send.
    """

    success: bool
    details: str
    events: str
    already_connected: Union[Unset, bool] = UNSET
    paused: Union[Unset, bool] = UNSET
    pause_reason: Union[Unset, str] = UNSET
    upstream_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        details = self.details

        events = self.events

        already_connected = self.already_connected

        paused = self.paused

        pause_reason = self.pause_reason

        upstream_code = self.upstream_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "details": details,
                "events": events,
            }
        )
        if already_connected is not UNSET:
            field_dict["alreadyConnected"] = already_connected
        if paused is not UNSET:
            field_dict["paused"] = paused
        if pause_reason is not UNSET:
            field_dict["pauseReason"] = pause_reason
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        details = d.pop("details")

        events = d.pop("events")

        already_connected = d.pop("alreadyConnected", UNSET)

        paused = d.pop("paused", UNSET)

        pause_reason = d.pop("pauseReason", UNSET)

        upstream_code = d.pop("upstreamCode", UNSET)

        connect_response = cls(
            success=success,
            details=details,
            events=events,
            already_connected=already_connected,
            paused=paused,
            pause_reason=pause_reason,
            upstream_code=upstream_code,
        )

        connect_response.additional_properties = d
        return connect_response

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
