from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadFileBody")


@_attrs_define
class DownloadFileBody:
    """
    Attributes:
        chat_id (Union[Unset, int]):  Example: 123456789.
        file_id (Union[Unset, int]):  Example: 111222333.
        message_id (Union[Unset, int]):  Example: 987654321.
        video_id (Union[Unset, int]):  Example: 111222333.
    """

    chat_id: Union[Unset, int] = UNSET
    file_id: Union[Unset, int] = UNSET
    message_id: Union[Unset, int] = UNSET
    video_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        file_id = self.file_id

        message_id = self.message_id

        video_id = self.video_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if video_id is not UNSET:
            field_dict["videoId"] = video_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId", UNSET)

        file_id = d.pop("fileId", UNSET)

        message_id = d.pop("messageId", UNSET)

        video_id = d.pop("videoId", UNSET)

        download_file_body = cls(
            chat_id=chat_id,
            file_id=file_id,
            message_id=message_id,
            video_id=video_id,
        )

        download_file_body.additional_properties = d
        return download_file_body

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
