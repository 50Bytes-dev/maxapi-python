from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AudioBody")


@_attrs_define
class AudioBody:
    """
    Attributes:
        audio (Union[Unset, str]):  Example: data:audio/mp3;base64,....
        chat_id (Union[Unset, int]):  Example: 123456789.
        file_name (Union[Unset, str]):  Example: audio.mp3.
        notify (Union[Unset, bool]):  Example: True.
        phone (Union[Unset, str]):  Example: 79001234567.
    """

    audio: Union[Unset, str] = UNSET
    chat_id: Union[Unset, int] = UNSET
    file_name: Union[Unset, str] = UNSET
    notify: Union[Unset, bool] = UNSET
    phone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio = self.audio

        chat_id = self.chat_id

        file_name = self.file_name

        notify = self.notify

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audio is not UNSET:
            field_dict["audio"] = audio
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if notify is not UNSET:
            field_dict["notify"] = notify
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audio = d.pop("audio", UNSET)

        chat_id = d.pop("chatId", UNSET)

        file_name = d.pop("fileName", UNSET)

        notify = d.pop("notify", UNSET)

        phone = d.pop("phone", UNSET)

        audio_body = cls(
            audio=audio,
            chat_id=chat_id,
            file_name=file_name,
            notify=notify,
            phone=phone,
        )

        audio_body.additional_properties = d
        return audio_body

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
