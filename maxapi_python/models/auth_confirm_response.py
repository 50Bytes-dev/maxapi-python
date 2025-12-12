from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthConfirmResponse")


@_attrs_define
class AuthConfirmResponse:
    """Response after confirming SMS verification code

    Attributes:
        auth_token (Union[Unset, str]):  Example: auth_token_value.
        message (Union[Unset, str]):  Example: Login successful.
        register_token (Union[Unset, str]):  Example: register_token_value.
        requires_registration (Union[Unset, bool]):
        success (Union[Unset, bool]):  Example: True.
    """

    auth_token: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    register_token: Union[Unset, str] = UNSET
    requires_registration: Union[Unset, bool] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_token = self.auth_token

        message = self.message

        register_token = self.register_token

        requires_registration = self.requires_registration

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_token is not UNSET:
            field_dict["authToken"] = auth_token
        if message is not UNSET:
            field_dict["message"] = message
        if register_token is not UNSET:
            field_dict["registerToken"] = register_token
        if requires_registration is not UNSET:
            field_dict["requiresRegistration"] = requires_registration
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_token = d.pop("authToken", UNSET)

        message = d.pop("message", UNSET)

        register_token = d.pop("registerToken", UNSET)

        requires_registration = d.pop("requiresRegistration", UNSET)

        success = d.pop("success", UNSET)

        auth_confirm_response = cls(
            auth_token=auth_token,
            message=message,
            register_token=register_token,
            requires_registration=requires_registration,
            success=success,
        )

        auth_confirm_response.additional_properties = d
        return auth_confirm_response

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
