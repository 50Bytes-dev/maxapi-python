from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadDocumentBody")


@_attrs_define
class DownloadDocumentBody:
    """
    Attributes:
        chat_id (Union[Unset, int]):  Example: 123456789.
        message_id (Union[Unset, str]): A MAX message id. MAX's ids are above 2^53, so they travel as strings; a JSON
            number is read too. Example: 115478893120847321.
        file_id (Union[Unset, int]): The attachment's `fileId` Example: 111222333.
    """

    chat_id: Union[Unset, int] = UNSET
    message_id: Union[Unset, str] = UNSET
    file_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        message_id = self.message_id

        file_id = self.file_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if file_id is not UNSET:
            field_dict["fileId"] = file_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId", UNSET)

        message_id = d.pop("messageId", UNSET)

        file_id = d.pop("fileId", UNSET)

        download_document_body = cls(
            chat_id=chat_id,
            message_id=message_id,
            file_id=file_id,
        )

        download_document_body.additional_properties = d
        return download_document_body

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
