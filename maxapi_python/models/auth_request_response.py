from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthRequestResponse")


@_attrs_define
class AuthRequestResponse:
    """Response after requesting SMS verification code

    Attributes:
        message (Union[Unset, str]):  Example: Verification code sent.
        success (Union[Unset, bool]):  Example: True.
        temp_token (Union[Unset, str]):  Example: temp_token_value.
    """

    message: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    temp_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        success = self.success

        temp_token = self.temp_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if success is not UNSET:
            field_dict["success"] = success
        if temp_token is not UNSET:
            field_dict["tempToken"] = temp_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        success = d.pop("success", UNSET)

        temp_token = d.pop("tempToken", UNSET)

        auth_request_response = cls(
            message=message,
            success=success,
            temp_token=temp_token,
        )

        auth_request_response.additional_properties = d
        return auth_request_response

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
