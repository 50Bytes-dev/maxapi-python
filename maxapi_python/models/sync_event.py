from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncEvent")


@_attrs_define
class SyncEvent:
    """The session is logged in: after a connect with a stored login, after
    `QRAuthorized`, after a reconnect. It carries the account, never MAX's
    login answer: the chats are `GET /chat/list`, people `POST /user/info`,
    the profile `GET /session/status`.

        Attributes:
            type_ (Literal['Sync']):
            max_user_id (int): The MAX id of the account's MAX user Example: 123456789.
            reconnect (bool): true after a reconnect
            user_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_id (str): The account id (`userID` and `instanceID` are the same) Example:
                6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
            instance_name (str): The account name; "" when the gateway could not read it Example: Shop bot.
            event_timestamp (int): Unix time in seconds, set when the delivery starts; a retry keeps it Example: 1793001234.
            name (Union[Unset, str]): The MAX account's name Example: Магазин у дома.
            photo (Union[Unset, str]): The MAX account's photo URL; "" when it has none
    """

    type_: Literal["Sync"]
    max_user_id: int
    reconnect: bool
    user_id: str
    instance_id: str
    instance_name: str
    event_timestamp: int
    name: Union[Unset, str] = UNSET
    photo: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        max_user_id = self.max_user_id

        reconnect = self.reconnect

        user_id = self.user_id

        instance_id = self.instance_id

        instance_name = self.instance_name

        event_timestamp = self.event_timestamp

        name = self.name

        photo = self.photo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "maxUserID": max_user_id,
                "reconnect": reconnect,
                "userID": user_id,
                "instanceID": instance_id,
                "instanceName": instance_name,
                "eventTimestamp": event_timestamp,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if photo is not UNSET:
            field_dict["photo"] = photo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["Sync"], d.pop("type"))
        if type_ != "Sync":
            raise ValueError(f"type must match const 'Sync', got '{type_}'")

        max_user_id = d.pop("maxUserID")

        reconnect = d.pop("reconnect")

        user_id = d.pop("userID")

        instance_id = d.pop("instanceID")

        instance_name = d.pop("instanceName")

        event_timestamp = d.pop("eventTimestamp")

        name = d.pop("name", UNSET)

        photo = d.pop("photo", UNSET)

        sync_event = cls(
            type_=type_,
            max_user_id=max_user_id,
            reconnect=reconnect,
            user_id=user_id,
            instance_id=instance_id,
            instance_name=instance_name,
            event_timestamp=event_timestamp,
            name=name,
            photo=photo,
        )

        sync_event.additional_properties = d
        return sync_event

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
