from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.all_chats_response_channels_item import AllChatsResponseChannelsItem
    from ..models.all_chats_response_dialogs_item import AllChatsResponseDialogsItem
    from ..models.all_chats_response_groups_item import AllChatsResponseGroupsItem
    from ..models.chat_counts import ChatCounts


T = TypeVar("T", bound="AllChatsResponse")


@_attrs_define
class AllChatsResponse:
    """Response with all dialogs, groups and channels

    Attributes:
        channels (Union[Unset, list['AllChatsResponseChannelsItem']]):
        counts (Union[Unset, ChatCounts]): Counts of dialogs, groups and channels
        dialogs (Union[Unset, list['AllChatsResponseDialogsItem']]):
        groups (Union[Unset, list['AllChatsResponseGroupsItem']]):
        success (Union[Unset, bool]):  Example: True.
    """

    channels: Union[Unset, list["AllChatsResponseChannelsItem"]] = UNSET
    counts: Union[Unset, "ChatCounts"] = UNSET
    dialogs: Union[Unset, list["AllChatsResponseDialogsItem"]] = UNSET
    groups: Union[Unset, list["AllChatsResponseGroupsItem"]] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)

        counts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        dialogs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.dialogs, Unset):
            dialogs = []
            for dialogs_item_data in self.dialogs:
                dialogs_item = dialogs_item_data.to_dict()
                dialogs.append(dialogs_item)

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if counts is not UNSET:
            field_dict["counts"] = counts
        if dialogs is not UNSET:
            field_dict["dialogs"] = dialogs
        if groups is not UNSET:
            field_dict["groups"] = groups
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.all_chats_response_channels_item import AllChatsResponseChannelsItem
        from ..models.all_chats_response_dialogs_item import AllChatsResponseDialogsItem
        from ..models.all_chats_response_groups_item import AllChatsResponseGroupsItem
        from ..models.chat_counts import ChatCounts

        d = dict(src_dict)
        channels = []
        _channels = d.pop("channels", UNSET)
        for channels_item_data in _channels or []:
            channels_item = AllChatsResponseChannelsItem.from_dict(channels_item_data)

            channels.append(channels_item)

        _counts = d.pop("counts", UNSET)
        counts: Union[Unset, ChatCounts]
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = ChatCounts.from_dict(_counts)

        dialogs = []
        _dialogs = d.pop("dialogs", UNSET)
        for dialogs_item_data in _dialogs or []:
            dialogs_item = AllChatsResponseDialogsItem.from_dict(dialogs_item_data)

            dialogs.append(dialogs_item)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = AllChatsResponseGroupsItem.from_dict(groups_item_data)

            groups.append(groups_item)

        success = d.pop("success", UNSET)

        all_chats_response = cls(
            channels=channels,
            counts=counts,
            dialogs=dialogs,
            groups=groups,
            success=success,
        )

        all_chats_response.additional_properties = d
        return all_chats_response

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
