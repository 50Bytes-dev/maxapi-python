from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QRCodeResponse")


@_attrs_define
class QRCodeResponse:
    """Current QR code for an in-progress auth session.

    Attributes:
        qrcode (Union[Unset, str]):  Example: data:image/png;base64,....
        success (Union[Unset, bool]):  Example: True.
    """

    qrcode: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qrcode = self.qrcode

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qrcode is not UNSET:
            field_dict["qrcode"] = qrcode
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qrcode = d.pop("qrcode", UNSET)

        success = d.pop("success", UNSET)

        qr_code_response = cls(
            qrcode=qrcode,
            success=success,
        )

        qr_code_response.additional_properties = d
        return qr_code_response

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
