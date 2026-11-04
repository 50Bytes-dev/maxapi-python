from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.max_attachment import MaxAttachment
    from ..models.max_element import MaxElement
    from ..models.max_message_link import MaxMessageLink
    from ..models.max_reaction_info import MaxReactionInfo


T = TypeVar("T", bound="MaxMessage")


@_attrs_define
class MaxMessage:
    """A message, as MAX gives it

    Attributes:
        id (str):  Example: 115478893120847321.
        text (str):
        time (int): Unix time in milliseconds
        type_ (str): `TEXT`, `SYSTEM` or `SERVICE` Example: TEXT.
        chat_id (Union[Unset, int]):
        sender (Union[Unset, int]): The sender's MAX id
        status (Union[Unset, str]): `EDITED` or `REMOVED` when so
        options (Union[Unset, int]):
        elements (Union[Unset, list['MaxElement']]):
        attaches (Union[Unset, list['MaxAttachment']]):
        link (Union[Unset, MaxMessageLink]): A reply or forward link of a message
        reaction_info (Union[Unset, MaxReactionInfo]):
        cid (Union[Unset, int]):
    """

    id: str
    text: str
    time: int
    type_: str
    chat_id: Union[Unset, int] = UNSET
    sender: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    options: Union[Unset, int] = UNSET
    elements: Union[Unset, list["MaxElement"]] = UNSET
    attaches: Union[Unset, list["MaxAttachment"]] = UNSET
    link: Union[Unset, "MaxMessageLink"] = UNSET
    reaction_info: Union[Unset, "MaxReactionInfo"] = UNSET
    cid: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        text = self.text

        time = self.time

        type_ = self.type_

        chat_id = self.chat_id

        sender = self.sender

        status = self.status

        options = self.options

        elements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()
                elements.append(elements_item)

        attaches: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attaches, Unset):
            attaches = []
            for attaches_item_data in self.attaches:
                attaches_item = attaches_item_data.to_dict()
                attaches.append(attaches_item)

        link: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.link, Unset):
            link = self.link.to_dict()

        reaction_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reaction_info, Unset):
            reaction_info = self.reaction_info.to_dict()

        cid = self.cid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "text": text,
                "time": time,
                "type": type_,
            }
        )
        if chat_id is not UNSET:
            field_dict["chatId"] = chat_id
        if sender is not UNSET:
            field_dict["sender"] = sender
        if status is not UNSET:
            field_dict["status"] = status
        if options is not UNSET:
            field_dict["options"] = options
        if elements is not UNSET:
            field_dict["elements"] = elements
        if attaches is not UNSET:
            field_dict["attaches"] = attaches
        if link is not UNSET:
            field_dict["link"] = link
        if reaction_info is not UNSET:
            field_dict["reactionInfo"] = reaction_info
        if cid is not UNSET:
            field_dict["cid"] = cid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.max_attachment import MaxAttachment
        from ..models.max_element import MaxElement
        from ..models.max_message_link import MaxMessageLink
        from ..models.max_reaction_info import MaxReactionInfo

        d = dict(src_dict)
        id = d.pop("id")

        text = d.pop("text")

        time = d.pop("time")

        type_ = d.pop("type")

        chat_id = d.pop("chatId", UNSET)

        sender = d.pop("sender", UNSET)

        status = d.pop("status", UNSET)

        options = d.pop("options", UNSET)

        elements = []
        _elements = d.pop("elements", UNSET)
        for elements_item_data in _elements or []:
            elements_item = MaxElement.from_dict(elements_item_data)

            elements.append(elements_item)

        attaches = []
        _attaches = d.pop("attaches", UNSET)
        for attaches_item_data in _attaches or []:
            attaches_item = MaxAttachment.from_dict(attaches_item_data)

            attaches.append(attaches_item)

        _link = d.pop("link", UNSET)
        link: Union[Unset, MaxMessageLink]
        if isinstance(_link, Unset):
            link = UNSET
        else:
            link = MaxMessageLink.from_dict(_link)

        _reaction_info = d.pop("reactionInfo", UNSET)
        reaction_info: Union[Unset, MaxReactionInfo]
        if isinstance(_reaction_info, Unset):
            reaction_info = UNSET
        else:
            reaction_info = MaxReactionInfo.from_dict(_reaction_info)

        cid = d.pop("cid", UNSET)

        max_message = cls(
            id=id,
            text=text,
            time=time,
            type_=type_,
            chat_id=chat_id,
            sender=sender,
            status=status,
            options=options,
            elements=elements,
            attaches=attaches,
            link=link,
            reaction_info=reaction_info,
            cid=cid,
        )

        max_message.additional_properties = d
        return max_message

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
