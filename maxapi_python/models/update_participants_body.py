from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_participants_body_operation import UpdateParticipantsBodyOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateParticipantsBody")


@_attrs_define
class UpdateParticipantsBody:
    """
    Attributes:
        chat_id (Union[Unset, int]):  Example: 123456789.
        user_ids (Union[Unset, list[int]]):  Example: [987654321].
        operation (Union[Unset, UpdateParticipantsBodyOperation]): `add` adds; anything else removes Example: add.
    """

    chat_id: Union[Unset, int] = UNSET
    user_ids: Union[Unset, list[int]] = UNSET
    operation: Union[Unset, UpdateParticipantsBodyOperation] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = self.chat_id

        user_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if user_ids is not UNSET:
            field_dict["userIds"] = user_ids
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_id = d.pop("chatId", UNSET)

        user_ids = cast(list[int], d.pop("userIds", UNSET))

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, UpdateParticipantsBodyOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = UpdateParticipantsBodyOperation(_operation)

        update_participants_body = cls(
            chat_id=chat_id,
            user_ids=user_ids,
            operation=operation,
        )

        update_participants_body.additional_properties = d
        return update_participants_body

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
