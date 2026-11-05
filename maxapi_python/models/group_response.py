from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat_row import ChatRow


T = TypeVar("T", bound="GroupResponse")


@_attrs_define
class GroupResponse:
    """
    Attributes:
        success (bool):  Example: True.
        chat (Union['ChatRow', None]): The chat MAX gave back, as a row of `GET /chat/list`
    """

    success: bool
    chat: Union["ChatRow", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_row import ChatRow

        success = self.success

        chat: Union[None, dict[str, Any]]
        if isinstance(self.chat, ChatRow):
            chat = self.chat.to_dict()
        else:
            chat = self.chat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "chat": chat,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_row import ChatRow

        d = dict(src_dict)
        success = d.pop("success")

        def _parse_chat(data: object) -> Union["ChatRow", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                chat_type_0 = ChatRow.from_dict(data)

                return chat_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ChatRow", None], data)

        chat = _parse_chat(d.pop("chat"))

        group_response = cls(
            success=success,
            chat=chat,
        )

        group_response.additional_properties = d
        return group_response

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
