from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_kind import ChatKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_row_last_message import ChatRowLastMessage


T = TypeVar("T", bound="ChatRow")


@_attrs_define
class ChatRow:
    """One chat of the account, as `GET /chat/list` and `GET /chat/info` give it.

    Attributes:
        chat_id (int): The chat; `POST /chat/send/text` takes it as it is Example: -70000000000000.
        type_ (ChatKind): `user` a dialog with a person or a bot, `chat` a group chat, `channel` a channel
        title (str): The chat's title, or the person's name; "" when unknown Example: Покупатели.
        can_write (bool): Whether the account may write there, by the rules of the MAX web client
        unread_count (int): Unread messages, as MAX counts them
        user_id (Union[Unset, int]): The person (or bot) of a dialog Example: 123456789.
        members_count (Union[Unset, int]): Members of a group chat or channel Example: 17.
        photo (Union[Unset, str]): The chat's or the person's photo URL, when there is one
        cant_write_reason (Union[Unset, str]): Why not, when `canWrite` is false: `restricted` (MAX does not let the
            account write there: a service chat, a restricted chat),
            `not_member`, `chat_closed` (removed, blocked, left or closed),
            `not_admin` (a channel the account may not post in),
            `user_blocked` or `user_removed` (the person's MAX account). Example: not_admin.
        last_message_id (Union[Unset, str]): The last message's id
        last_message_date (Union[Unset, int]): The last message's unix time, seconds
        last_message (Union[Unset, ChatRowLastMessage]): With `include=lastMessage` only. The last message as MAX gives
            it, its text included.
        participants (Union[Unset, list[int]]): With `include=participants` only. The members' MAX ids, as MAX lists
            them.
    """

    chat_id: int
    type_: ChatKind
    title: str
    can_write: bool
    unread_count: int
    user_id: Union[Unset, int] = UNSET
    members_count: Union[Unset, int] = UNSET
    photo: Union[Unset, str] = UNSET
    cant_write_reason: Union[Unset, str] = UNSET
    last_message_id: Union[Unset, str] = UNSET
    last_message_date: Union[Unset, int] = UNSET
    last_message: Union[Unset, "ChatRowLastMessage"] = UNSET
    participants: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        type_ = self.type_.value

        title = self.title

        can_write = self.can_write

        unread_count = self.unread_count

        user_id = self.user_id

        members_count = self.members_count

        photo = self.photo

        cant_write_reason = self.cant_write_reason

        last_message_id = self.last_message_id

        last_message_date = self.last_message_date

        last_message: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_message, Unset):
            last_message = self.last_message.to_dict()

        participants: Union[Unset, list[int]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = self.participants

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chatId": chat_id,
                "type": type_,
                "title": title,
                "canWrite": can_write,
                "unreadCount": unread_count,
            }
        )
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if members_count is not UNSET:
            field_dict["membersCount"] = members_count
        if photo is not UNSET:
            field_dict["photo"] = photo
        if cant_write_reason is not UNSET:
            field_dict["cantWriteReason"] = cant_write_reason
        if last_message_id is not UNSET:
            field_dict["lastMessageId"] = last_message_id
        if last_message_date is not UNSET:
            field_dict["lastMessageDate"] = last_message_date
        if last_message is not UNSET:
            field_dict["lastMessage"] = last_message
        if participants is not UNSET:
            field_dict["participants"] = participants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_row_last_message import ChatRowLastMessage

        d = dict(src_dict)
        chat_id = d.pop("chatId")

        type_ = ChatKind(d.pop("type"))

        title = d.pop("title")

        can_write = d.pop("canWrite")

        unread_count = d.pop("unreadCount")

        user_id = d.pop("userId", UNSET)

        members_count = d.pop("membersCount", UNSET)

        photo = d.pop("photo", UNSET)

        cant_write_reason = d.pop("cantWriteReason", UNSET)

        last_message_id = d.pop("lastMessageId", UNSET)

        last_message_date = d.pop("lastMessageDate", UNSET)

        _last_message = d.pop("lastMessage", UNSET)
        last_message: Union[Unset, ChatRowLastMessage]
        if isinstance(_last_message, Unset):
            last_message = UNSET
        else:
            last_message = ChatRowLastMessage.from_dict(_last_message)

        participants = cast(list[int], d.pop("participants", UNSET))

        chat_row = cls(
            chat_id=chat_id,
            type_=type_,
            title=title,
            can_write=can_write,
            unread_count=unread_count,
            user_id=user_id,
            members_count=members_count,
            photo=photo,
            cant_write_reason=cant_write_reason,
            last_message_id=last_message_id,
            last_message_date=last_message_date,
            last_message=last_message,
            participants=participants,
        )

        chat_row.additional_properties = d
        return chat_row

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
