from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_result_status import DeleteResultStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteResult")


@_attrs_define
class DeleteResult:
    """
    Attributes:
        message_id (str): A MAX message id. MAX's ids are above 2^53, so they travel as strings; a JSON number is read
            too. Example: 115478893120847321.
        status (DeleteResultStatus): `deleted`: MAX deleted it for everyone. `not_found`: MAX did not
            delete it (no such message in the chat, as far as MAX says).
            `too_old`, `forbidden`: MAX refused the call with a code of that
            kind (`upstreamCode`).
        upstream_code (Union[Unset, str]): MAX's code, when MAX refused the call
    """

    message_id: str
    status: DeleteResultStatus
    upstream_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        status = self.status.value

        upstream_code = self.upstream_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageId": message_id,
                "status": status,
            }
        )
        if upstream_code is not UNSET:
            field_dict["upstreamCode"] = upstream_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("messageId")

        status = DeleteResultStatus(d.pop("status"))

        upstream_code = d.pop("upstreamCode", UNSET)

        delete_result = cls(
            message_id=message_id,
            status=status,
            upstream_code=upstream_code,
        )

        delete_result.additional_properties = d
        return delete_result

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
