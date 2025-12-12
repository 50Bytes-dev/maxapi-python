from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageBody")


@_attrs_define
class ImageBody:
    """
    Attributes:
        caption (Union[Unset, str]):  Example: Image caption.
        chat_id (Union[Unset, int]):  Example: 123456789.
        image (Union[Unset, str]):  Example: data:image/jpeg;base64,....
        notify (Union[Unset, bool]):  Example: True.
        phone (Union[Unset, str]):  Example: 79001234567.
    """

    caption: Union[Unset, str] = UNSET
    chat_id: Union[Unset, int] = UNSET
    image: Union[Unset, str] = UNSET
    notify: Union[Unset, bool] = UNSET
    phone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        caption = self.caption

        chat_id = self.chat_id

        image = self.image

        notify = self.notify

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if caption is not UNSET:
            field_dict["caption"] = caption
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if image is not UNSET:
            field_dict["image"] = image
        if notify is not UNSET:
            field_dict["notify"] = notify
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        caption = d.pop("caption", UNSET)

        chat_id = d.pop("chatId", UNSET)

        image = d.pop("image", UNSET)

        notify = d.pop("notify", UNSET)

        phone = d.pop("phone", UNSET)

        image_body = cls(
            caption=caption,
            chat_id=chat_id,
            image=image,
            notify=notify,
            phone=phone,
        )

        image_body.additional_properties = d
        return image_body

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
