from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendVideoBody")


@_attrs_define
class SendVideoBody:
    """
    Attributes:
        chat_id (Union[Unset, int]): The MAX chat id; when 0, `phone` is looked up Example: 123456789.
        phone (Union[Unset, str]):  Example: 79001234567.
        video (Union[Unset, str]): A data URL, an http(s) URL the gateway downloads, or plain base64 Example:
            data:video/mp4;base64,AAAAIGZ0eXA....
        file_name (Union[Unset, str]): Default `video.mp4` Example: video.mp4.
        caption (Union[Unset, str]):  Example: Обзор.
        notify (Union[Unset, bool]):  Example: True.
    """

    chat_id: Union[Unset, int] = UNSET
    phone: Union[Unset, str] = UNSET
    video: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    caption: Union[Unset, str] = UNSET
    notify: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        phone = self.phone

        video = self.video

        file_name = self.file_name

        caption = self.caption

        notify = self.notify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if phone is not UNSET:
            field_dict["phone"] = phone
        if video is not UNSET:
            field_dict["video"] = video
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if caption is not UNSET:
            field_dict["caption"] = caption
        if notify is not UNSET:
            field_dict["notify"] = notify

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId", UNSET)

        phone = d.pop("phone", UNSET)

        video = d.pop("video", UNSET)

        file_name = d.pop("fileName", UNSET)

        caption = d.pop("caption", UNSET)

        notify = d.pop("notify", UNSET)

        send_video_body = cls(
            chat_id=chat_id,
            phone=phone,
            video=video,
            file_name=file_name,
            caption=caption,
            notify=notify,
        )

        send_video_body.additional_properties = d
        return send_video_body

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
