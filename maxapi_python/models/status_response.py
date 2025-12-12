from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusResponse")


@_attrs_define
class StatusResponse:
    """Connection and authentication status

    Attributes:
        authenticated (Union[Unset, bool]):  Example: True.
        connected (Union[Unset, bool]):  Example: True.
        logged_in (Union[Unset, bool]):  Example: True.
        max_user_id (Union[Unset, int]):  Example: 123456789.
        success (Union[Unset, bool]):  Example: True.
    """

    authenticated: Union[Unset, bool] = UNSET
    connected: Union[Unset, bool] = UNSET
    logged_in: Union[Unset, bool] = UNSET
    max_user_id: Union[Unset, int] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authenticated = self.authenticated

        connected = self.connected

        logged_in = self.logged_in

        max_user_id = self.max_user_id

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authenticated is not UNSET:
            field_dict["authenticated"] = authenticated
        if connected is not UNSET:
            field_dict["connected"] = connected
        if logged_in is not UNSET:
            field_dict["loggedIn"] = logged_in
        if max_user_id is not UNSET:
            field_dict["maxUserID"] = max_user_id
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authenticated = d.pop("authenticated", UNSET)

        connected = d.pop("connected", UNSET)

        logged_in = d.pop("loggedIn", UNSET)

        max_user_id = d.pop("maxUserID", UNSET)

        success = d.pop("success", UNSET)

        status_response = cls(
            authenticated=authenticated,
            connected=connected,
            logged_in=logged_in,
            max_user_id=max_user_id,
            success=success,
        )

        status_response.additional_properties = d
        return status_response

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
