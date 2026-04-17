from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthQRStartResponse")


@_attrs_define
class AuthQRStartResponse:
    """QR auth session created

    Attributes:
        success (Union[Unset, bool]):  Example: True.
        qr_link (Union[Unset, str]):  Example: https://max.ru/:auth/6bc2adb2-6b23-4a7d-a96c-320bee4ed0d7.
        qr_code_base_64 (Union[Unset, str]):  Example: data:image/png;base64,....
        track_id (Union[Unset, str]):  Example: 6bc2adb2-6b23-4a7d-a96c-320bee4ed0d7.
        polling_interval (Union[Unset, int]):  Example: 5000.
        ttl (Union[Unset, int]):  Example: 120000.
        expires_at (Union[Unset, int]):  Example: 1776435251750.
    """

    success: Union[Unset, bool] = UNSET
    qr_link: Union[Unset, str] = UNSET
    qr_code_base_64: Union[Unset, str] = UNSET
    track_id: Union[Unset, str] = UNSET
    polling_interval: Union[Unset, int] = UNSET
    ttl: Union[Unset, int] = UNSET
    expires_at: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        qr_link = self.qr_link

        qr_code_base_64 = self.qr_code_base_64

        track_id = self.track_id

        polling_interval = self.polling_interval

        ttl = self.ttl

        expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if qr_link is not UNSET:
            field_dict["qrLink"] = qr_link
        if qr_code_base_64 is not UNSET:
            field_dict["qrCodeBase64"] = qr_code_base_64
        if track_id is not UNSET:
            field_dict["trackId"] = track_id
        if polling_interval is not UNSET:
            field_dict["pollingInterval"] = polling_interval
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        qr_link = d.pop("qrLink", UNSET)

        qr_code_base_64 = d.pop("qrCodeBase64", UNSET)

        track_id = d.pop("trackId", UNSET)

        polling_interval = d.pop("pollingInterval", UNSET)

        ttl = d.pop("ttl", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        auth_qr_start_response = cls(
            success=success,
            qr_link=qr_link,
            qr_code_base_64=qr_code_base_64,
            track_id=track_id,
            polling_interval=polling_interval,
            ttl=ttl,
            expires_at=expires_at,
        )

        auth_qr_start_response.additional_properties = d
        return auth_qr_start_response

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
