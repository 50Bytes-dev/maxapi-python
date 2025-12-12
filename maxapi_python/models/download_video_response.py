from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadVideoResponse")


@_attrs_define
class DownloadVideoResponse:
    """Response with downloaded video data

    Attributes:
        data (Union[Unset, str]):  Example: base64_encoded_data.
        mime_type (Union[Unset, str]):  Example: video/mp4.
        success (Union[Unset, bool]):  Example: True.
        url (Union[Unset, str]):  Example: https://example.com/video.mp4.
    """

    data: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        mime_type = self.mime_type

        success = self.success

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if success is not UNSET:
            field_dict["success"] = success
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        success = d.pop("success", UNSET)

        url = d.pop("url", UNSET)

        download_video_response = cls(
            data=data,
            mime_type=mime_type,
            success=success,
            url=url,
        )

        download_video_response.additional_properties = d
        return download_video_response

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
