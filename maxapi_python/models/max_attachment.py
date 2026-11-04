from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaxAttachment")


@_attrs_define
class MaxAttachment:
    """An attachment of a message; the fields present depend on `_type`

    Attributes:
        field_type_ (Union[Unset, str]): `PHOTO`, `VIDEO`, `FILE`, `STICKER`, `AUDIO`, `CONTROL`, ... Example: PHOTO.
        photo_id (Union[Unset, int]):
        photo_token (Union[Unset, str]):
        video_id (Union[Unset, int]):
        file_id (Union[Unset, int]):
        audio_id (Union[Unset, int]):
        token (Union[Unset, str]):
        base_url (Union[Unset, str]):
        url (Union[Unset, str]):
        name (Union[Unset, str]):
        size (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        duration (Union[Unset, int]):
        preview_data (Union[Unset, str]):
        event (Union[Unset, str]):
        chat_type (Union[Unset, str]):
        title (Union[Unset, str]):
        user_ids (Union[Unset, list[int]]):
    """

    field_type_: Union[Unset, str] = UNSET
    photo_id: Union[Unset, int] = UNSET
    photo_token: Union[Unset, str] = UNSET
    video_id: Union[Unset, int] = UNSET
    file_id: Union[Unset, int] = UNSET
    audio_id: Union[Unset, int] = UNSET
    token: Union[Unset, str] = UNSET
    base_url: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    preview_data: Union[Unset, str] = UNSET
    event: Union[Unset, str] = UNSET
    chat_type: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    user_ids: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_type_ = self.field_type_

        photo_id = self.photo_id

        photo_token = self.photo_token

        video_id = self.video_id

        file_id = self.file_id

        audio_id = self.audio_id

        token = self.token

        base_url = self.base_url

        url = self.url

        name = self.name

        size = self.size

        width = self.width

        height = self.height

        duration = self.duration

        preview_data = self.preview_data

        event = self.event

        chat_type = self.chat_type

        title = self.title

        user_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_type_ is not UNSET:
            field_dict["_type"] = field_type_
        if photo_id is not UNSET:
            field_dict["photoId"] = photo_id
        if photo_token is not UNSET:
            field_dict["photoToken"] = photo_token
        if video_id is not UNSET:
            field_dict["videoId"] = video_id
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if audio_id is not UNSET:
            field_dict["audioId"] = audio_id
        if token is not UNSET:
            field_dict["token"] = token
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if url is not UNSET:
            field_dict["url"] = url
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if duration is not UNSET:
            field_dict["duration"] = duration
        if preview_data is not UNSET:
            field_dict["previewData"] = preview_data
        if event is not UNSET:
            field_dict["event"] = event
        if chat_type is not UNSET:
            field_dict["chatType"] = chat_type
        if title is not UNSET:
            field_dict["title"] = title
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_type_ = d.pop("_type", UNSET)

        photo_id = d.pop("photoId", UNSET)

        photo_token = d.pop("photoToken", UNSET)

        video_id = d.pop("videoId", UNSET)

        file_id = d.pop("fileId", UNSET)

        audio_id = d.pop("audioId", UNSET)

        token = d.pop("token", UNSET)

        base_url = d.pop("baseUrl", UNSET)

        url = d.pop("url", UNSET)

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        duration = d.pop("duration", UNSET)

        preview_data = d.pop("previewData", UNSET)

        event = d.pop("event", UNSET)

        chat_type = d.pop("chatType", UNSET)

        title = d.pop("title", UNSET)

        user_ids = cast(list[int], d.pop("userIds", UNSET))

        max_attachment = cls(
            field_type_=field_type_,
            photo_id=photo_id,
            photo_token=photo_token,
            video_id=video_id,
            file_id=file_id,
            audio_id=audio_id,
            token=token,
            base_url=base_url,
            url=url,
            name=name,
            size=size,
            width=width,
            height=height,
            duration=duration,
            preview_data=preview_data,
            event=event,
            chat_type=chat_type,
            title=title,
            user_ids=user_ids,
        )

        max_attachment.additional_properties = d
        return max_attachment

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
