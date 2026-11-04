from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DownloadMediaResponse")


@_attrs_define
class DownloadMediaResponse:
    """
    Attributes:
        success (bool):  Example: True.
        data (str): The file in base64 Example: /9j/4AAQSkZJRg....
        mime_type (str): Sniffed from the bytes Example: image/jpeg.
    """

    success: bool
    data: str
    mime_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        data = self.data

        mime_type = self.mime_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "data": data,
                "mimeType": mime_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        data = d.pop("data")

        mime_type = d.pop("mimeType")

        download_media_response = cls(
            success=success,
            data=data,
            mime_type=mime_type,
        )

        download_media_response.additional_properties = d
        return download_media_response

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
