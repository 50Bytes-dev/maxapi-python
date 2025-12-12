from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contacts_response_contacts_item import ContactsResponseContactsItem


T = TypeVar("T", bound="ContactsResponse")


@_attrs_define
class ContactsResponse:
    """Response with list of contacts

    Attributes:
        contacts (Union[Unset, list['ContactsResponseContactsItem']]):
        count (Union[Unset, int]):  Example: 42.
        success (Union[Unset, bool]):  Example: True.
    """

    contacts: Union[Unset, list["ContactsResponseContactsItem"]] = UNSET
    count: Union[Unset, int] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contacts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        count = self.count

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if count is not UNSET:
            field_dict["count"] = count
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contacts_response_contacts_item import ContactsResponseContactsItem

        d = dict(src_dict)
        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = ContactsResponseContactsItem.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        count = d.pop("count", UNSET)

        success = d.pop("success", UNSET)

        contacts_response = cls(
            contacts=contacts,
            count=count,
            success=success,
        )

        contacts_response.additional_properties = d
        return contacts_response

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
