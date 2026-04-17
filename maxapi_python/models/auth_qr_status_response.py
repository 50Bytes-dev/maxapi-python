from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_qr_status_response_status import AuthQRStatusResponseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthQRStatusResponse")


@_attrs_define
class AuthQRStatusResponse:
    """QR auth session status

    Attributes:
        auth_token (Union[Unset, str]):  Example: auth_token_value.
        status (Union[Unset, AuthQRStatusResponseStatus]):  Example: pending.
        success (Union[Unset, bool]):  Example: True.
    """

    auth_token: Union[Unset, str] = UNSET
    status: Union[Unset, AuthQRStatusResponseStatus] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_token = self.auth_token

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_token is not UNSET:
            field_dict["authToken"] = auth_token
        if status is not UNSET:
            field_dict["status"] = status
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_token = d.pop("authToken", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AuthQRStatusResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AuthQRStatusResponseStatus(_status)

        success = d.pop("success", UNSET)

        auth_qr_status_response = cls(
            auth_token=auth_token,
            status=status,
            success=success,
        )

        auth_qr_status_response.additional_properties = d
        return auth_qr_status_response

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
