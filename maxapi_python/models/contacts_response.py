from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.max_contact import MaxContact


T = TypeVar("T", bound="ContactsResponse")


@_attrs_define
class ContactsResponse:
    """
    Attributes:
        success (bool):  Example: True.
        contacts (Union[None, list['MaxContact']]): The contacts; null when there are none
        count (int):  Example: 42.
    """

    success: bool
    contacts: Union[None, list["MaxContact"]]
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        contacts: Union[None, list[dict[str, Any]]]
        if isinstance(self.contacts, list):
            contacts = []
            for contacts_type_0_item_data in self.contacts:
                contacts_type_0_item = contacts_type_0_item_data.to_dict()
                contacts.append(contacts_type_0_item)

        else:
            contacts = self.contacts

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "contacts": contacts,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.max_contact import MaxContact

        d = dict(src_dict)
        success = d.pop("success")

        def _parse_contacts(data: object) -> Union[None, list["MaxContact"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contacts_type_0 = []
                _contacts_type_0 = data
                for contacts_type_0_item_data in _contacts_type_0:
                    contacts_type_0_item = MaxContact.from_dict(contacts_type_0_item_data)

                    contacts_type_0.append(contacts_type_0_item)

                return contacts_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["MaxContact"]], data)

        contacts = _parse_contacts(d.pop("contacts"))

        count = d.pop("count")

        contacts_response = cls(
            success=success,
            contacts=contacts,
            count=count,
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
