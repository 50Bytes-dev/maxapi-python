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
        expires_at (Union[Unset, int]):  Example: 1776435251750.
        polling_interval (Union[Unset, int]):  Example: 5000.
        qr_code_base_64 (Union[Unset, str]):  Example: data:image/png;base64,....
        qr_link (Union[Unset, str]):  Example: https://max.ru/:auth/6bc2adb2-6b23-4a7d-a96c-320bee4ed0d7.
        success (Union[Unset, bool]):  Example: True.
        track_id (Union[Unset, str]):  Example: 6bc2adb2-6b23-4a7d-a96c-320bee4ed0d7.
        ttl (Union[Unset, int]):  Example: 120000.
    """

    expires_at: Union[Unset, int] = UNSET
    polling_interval: Union[Unset, int] = UNSET
    qr_code_base_64: Union[Unset, str] = UNSET
    qr_link: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    track_id: Union[Unset, str] = UNSET
    ttl: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at

        polling_interval = self.polling_interval

        qr_code_base_64 = self.qr_code_base_64

        qr_link = self.qr_link

        success = self.success

        track_id = self.track_id

        ttl = self.ttl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if polling_interval is not UNSET:
            field_dict["pollingInterval"] = polling_interval
        if qr_code_base_64 is not UNSET:
            field_dict["qrCodeBase64"] = qr_code_base_64
        if qr_link is not UNSET:
            field_dict["qrLink"] = qr_link
        if success is not UNSET:
            field_dict["success"] = success
        if track_id is not UNSET:
            field_dict["trackId"] = track_id
        if ttl is not UNSET:
            field_dict["ttl"] = ttl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expires_at = d.pop("expiresAt", UNSET)

        polling_interval = d.pop("pollingInterval", UNSET)

        qr_code_base_64 = d.pop("qrCodeBase64", UNSET)

        qr_link = d.pop("qrLink", UNSET)

        success = d.pop("success", UNSET)

        track_id = d.pop("trackId", UNSET)

        ttl = d.pop("ttl", UNSET)

        auth_qr_start_response = cls(
            expires_at=expires_at,
            polling_interval=polling_interval,
            qr_code_base_64=qr_code_base_64,
            qr_link=qr_link,
            success=success,
            track_id=track_id,
            ttl=ttl,
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
