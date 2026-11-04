from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_payload import EventPayload
    from ..models.message_event_s3 import MessageEventS3


T = TypeVar("T", bound="MessageEvent")


@_attrs_define
class MessageEvent:
    """A new message in one of the account's chats, the account's own included.
    The media fields come from the message's attachments (the last one of a
    kind wins); `base64`, `mimeType` and `s3` only for a photo, by
    `media_delivery`.

        Attributes:
            type_ (Literal['Message']):
            opcode (int): MAX's opcode of the notification Example: 128.
            event (EventPayload): MAX's notification payload, as MAX sent it
            user_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_name (str): The account name; "" when the gateway could not read it Example: Shop bot.
            event_timestamp (int): Unix time in seconds, set when the delivery starts; a retry keeps it Example: 1793001234.
            media_type (Union[Unset, str]): `image`, `video`, `file` or `audio` Example: image.
            media_url (Union[Unset, str]): A photo's URL
            base64 (Union[Unset, str]): A photo's bytes in base64
            mime_type (Union[Unset, str]): With `base64`; `image/jpeg`
            s3 (Union[Unset, MessageEventS3]): Where the photo was uploaded to S3
            video_id (Union[Unset, int]):
            video_token (Union[Unset, str]):
            file_id (Union[Unset, int]):
            file_name (Union[Unset, str]):
            file_size (Union[Unset, int]):
            audio_id (Union[Unset, int]):
            audio_url (Union[Unset, str]):
    """

    type_: Literal["Message"]
    opcode: int
    event: "EventPayload"
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    media_type: Union[Unset, str] = UNSET
    media_url: Union[Unset, str] = UNSET
    base64: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    s3: Union[Unset, "MessageEventS3"] = UNSET
    video_id: Union[Unset, int] = UNSET
    video_token: Union[Unset, str] = UNSET
    file_id: Union[Unset, int] = UNSET
    file_name: Union[Unset, str] = UNSET
    file_size: Union[Unset, int] = UNSET
    audio_id: Union[Unset, int] = UNSET
    audio_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        opcode = self.opcode

        event = self.event.to_dict()

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

        media_type = self.media_type

        media_url = self.media_url

        base64 = self.base64

        mime_type = self.mime_type

        s3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.s3, Unset):
            s3 = self.s3.to_dict()

        video_id = self.video_id

        video_token = self.video_token

        file_id = self.file_id

        file_name = self.file_name

        file_size = self.file_size

        audio_id = self.audio_id

        audio_url = self.audio_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "opcode": opcode,
                "event": event,
                "userID": user_id,
                "instanceID": instance_id,
                "instanceName": instance_name,
                "eventTimestamp": event_timestamp,
            }
        )
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if media_url is not UNSET:
            field_dict["mediaUrl"] = media_url
        if base64 is not UNSET:
            field_dict["base64"] = base64
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if s3 is not UNSET:
            field_dict["s3"] = s3
        if video_id is not UNSET:
            field_dict["videoId"] = video_id
        if video_token is not UNSET:
            field_dict["videoToken"] = video_token
        if file_id is not UNSET:
            field_dict["fileId"] = file_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if audio_id is not UNSET:
            field_dict["audioId"] = audio_id
        if audio_url is not UNSET:
            field_dict["audioUrl"] = audio_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_payload import EventPayload
        from ..models.message_event_s3 import MessageEventS3

        d = dict(src_dict)
        type_ = cast(Literal["Message"], d.pop("type"))
        if type_ != "Message":
            raise ValueError(f"type must match const 'Message', got '{type_}'")

        opcode = d.pop("opcode")

        event = EventPayload.from_dict(d.pop("event"))

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        media_type = d.pop("mediaType", UNSET)

        media_url = d.pop("mediaUrl", UNSET)

        base64 = d.pop("base64", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        _s3 = d.pop("s3", UNSET)
        s3: Union[Unset, MessageEventS3]
        if isinstance(_s3, Unset):
            s3 = UNSET
        else:
            s3 = MessageEventS3.from_dict(_s3)

        video_id = d.pop("videoId", UNSET)

        video_token = d.pop("videoToken", UNSET)

        file_id = d.pop("fileId", UNSET)

        file_name = d.pop("fileName", UNSET)

        file_size = d.pop("fileSize", UNSET)

        audio_id = d.pop("audioId", UNSET)

        audio_url = d.pop("audioUrl", UNSET)

        message_event = cls(
            type_=type_,
            opcode=opcode,
            event=event,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
            media_type=media_type,
            media_url=media_url,
            base64=base64,
            mime_type=mime_type,
            s3=s3,
            video_id=video_id,
            video_token=video_token,
            file_id=file_id,
            file_name=file_name,
            file_size=file_size,
            audio_id=audio_id,
            audio_url=audio_url,
        )

        message_event.additional_properties = d
        return message_event

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
