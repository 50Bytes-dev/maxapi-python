from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.max_chat_admin_participants import MaxChatAdminParticipants
    from ..models.max_chat_options import MaxChatOptions
    from ..models.max_chat_participants import MaxChatParticipants
    from ..models.max_message import MaxMessage


T = TypeVar("T", bound="MaxChat")


@_attrs_define
class MaxChat:
    """A chat, as MAX gives it

    Attributes:
        id (int):  Example: -68000000000001.
        type_ (str): `DIALOG`, `CHAT` or `CHANNEL` Example: CHAT.
        cid (Union[Unset, int]):
        title (Union[Unset, str]):  Example: Покупатели.
        description (Union[Unset, str]):
        owner (Union[Unset, int]):
        access (Union[Unset, str]):
        link (Union[Unset, str]):
        participants (Union[Unset, MaxChatParticipants]): MAX user id → MAX's value for the member
        participants_count (Union[Unset, int]):
        admins (Union[Unset, list[int]]):
        admin_participants (Union[Unset, MaxChatAdminParticipants]):
        last_message (Union[Unset, MaxMessage]): A message, as MAX gives it
        options (Union[Unset, MaxChatOptions]):
        created (Union[Unset, int]):
        modified (Union[Unset, int]):
        join_time (Union[Unset, int]):
        messages_count (Union[Unset, int]):
        status (Union[Unset, str]):
        base_icon_url (Union[Unset, str]):
        base_raw_icon_url (Union[Unset, str]):
        last_event_time (Union[Unset, int]):
        last_delayed_update_time (Union[Unset, int]):
        last_fire_delayed_error_time (Union[Unset, int]):
    """

    id: int
    type_: str
    cid: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    owner: Union[Unset, int] = UNSET
    access: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    participants: Union[Unset, "MaxChatParticipants"] = UNSET
    participants_count: Union[Unset, int] = UNSET
    admins: Union[Unset, list[int]] = UNSET
    admin_participants: Union[Unset, "MaxChatAdminParticipants"] = UNSET
    last_message: Union[Unset, "MaxMessage"] = UNSET
    options: Union[Unset, "MaxChatOptions"] = UNSET
    created: Union[Unset, int] = UNSET
    modified: Union[Unset, int] = UNSET
    join_time: Union[Unset, int] = UNSET
    messages_count: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    base_icon_url: Union[Unset, str] = UNSET
    base_raw_icon_url: Union[Unset, str] = UNSET
    last_event_time: Union[Unset, int] = UNSET
    last_delayed_update_time: Union[Unset, int] = UNSET
    last_fire_delayed_error_time: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        cid = self.cid

        title = self.title

        description = self.description

        owner = self.owner

        access = self.access

        link = self.link

        participants: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = self.participants.to_dict()

        participants_count = self.participants_count

        admins: Union[Unset, list[int]] = UNSET
        if not isinstance(self.admins, Unset):
            admins = self.admins

        admin_participants: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.admin_participants, Unset):
            admin_participants = self.admin_participants.to_dict()

        last_message: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_message, Unset):
            last_message = self.last_message.to_dict()

        options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        created = self.created

        modified = self.modified

        join_time = self.join_time

        messages_count = self.messages_count

        status = self.status

        base_icon_url = self.base_icon_url

        base_raw_icon_url = self.base_raw_icon_url

        last_event_time = self.last_event_time

        last_delayed_update_time = self.last_delayed_update_time

        last_fire_delayed_error_time = self.last_fire_delayed_error_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if cid is not UNSET:
            field_dict["cid"] = cid
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if owner is not UNSET:
            field_dict["owner"] = owner
        if access is not UNSET:
            field_dict["access"] = access
        if link is not UNSET:
            field_dict["link"] = link
        if participants is not UNSET:
            field_dict["participants"] = participants
        if participants_count is not UNSET:
            field_dict["participantsCount"] = participants_count
        if admins is not UNSET:
            field_dict["admins"] = admins
        if admin_participants is not UNSET:
            field_dict["adminParticipants"] = admin_participants
        if last_message is not UNSET:
            field_dict["lastMessage"] = last_message
        if options is not UNSET:
            field_dict["options"] = options
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if join_time is not UNSET:
            field_dict["joinTime"] = join_time
        if messages_count is not UNSET:
            field_dict["messagesCount"] = messages_count
        if status is not UNSET:
            field_dict["status"] = status
        if base_icon_url is not UNSET:
            field_dict["baseIconUrl"] = base_icon_url
        if base_raw_icon_url is not UNSET:
            field_dict["baseRawIconUrl"] = base_raw_icon_url
        if last_event_time is not UNSET:
            field_dict["lastEventTime"] = last_event_time
        if last_delayed_update_time is not UNSET:
            field_dict["lastDelayedUpdateTime"] = last_delayed_update_time
        if last_fire_delayed_error_time is not UNSET:
            field_dict["lastFireDelayedErrorTime"] = last_fire_delayed_error_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.max_chat_admin_participants import MaxChatAdminParticipants
        from ..models.max_chat_options import MaxChatOptions
        from ..models.max_chat_participants import MaxChatParticipants
        from ..models.max_message import MaxMessage

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        cid = d.pop("cid", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        owner = d.pop("owner", UNSET)

        access = d.pop("access", UNSET)

        link = d.pop("link", UNSET)

        _participants = d.pop("participants", UNSET)
        participants: Union[Unset, MaxChatParticipants]
        if isinstance(_participants, Unset):
            participants = UNSET
        else:
            participants = MaxChatParticipants.from_dict(_participants)

        participants_count = d.pop("participantsCount", UNSET)

        admins = cast(list[int], d.pop("admins", UNSET))

        _admin_participants = d.pop("adminParticipants", UNSET)
        admin_participants: Union[Unset, MaxChatAdminParticipants]
        if isinstance(_admin_participants, Unset):
            admin_participants = UNSET
        else:
            admin_participants = MaxChatAdminParticipants.from_dict(_admin_participants)

        _last_message = d.pop("lastMessage", UNSET)
        last_message: Union[Unset, MaxMessage]
        if isinstance(_last_message, Unset):
            last_message = UNSET
        else:
            last_message = MaxMessage.from_dict(_last_message)

        _options = d.pop("options", UNSET)
        options: Union[Unset, MaxChatOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = MaxChatOptions.from_dict(_options)

        created = d.pop("created", UNSET)

        modified = d.pop("modified", UNSET)

        join_time = d.pop("joinTime", UNSET)

        messages_count = d.pop("messagesCount", UNSET)

        status = d.pop("status", UNSET)

        base_icon_url = d.pop("baseIconUrl", UNSET)

        base_raw_icon_url = d.pop("baseRawIconUrl", UNSET)

        last_event_time = d.pop("lastEventTime", UNSET)

        last_delayed_update_time = d.pop("lastDelayedUpdateTime", UNSET)

        last_fire_delayed_error_time = d.pop("lastFireDelayedErrorTime", UNSET)

        max_chat = cls(
            id=id,
            type_=type_,
            cid=cid,
            title=title,
            description=description,
            owner=owner,
            access=access,
            link=link,
            participants=participants,
            participants_count=participants_count,
            admins=admins,
            admin_participants=admin_participants,
            last_message=last_message,
            options=options,
            created=created,
            modified=modified,
            join_time=join_time,
            messages_count=messages_count,
            status=status,
            base_icon_url=base_icon_url,
            base_raw_icon_url=base_raw_icon_url,
            last_event_time=last_event_time,
            last_delayed_update_time=last_delayed_update_time,
            last_fire_delayed_error_time=last_fire_delayed_error_time,
        )

        max_chat.additional_properties = d
        return max_chat

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
