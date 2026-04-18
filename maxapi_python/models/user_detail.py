from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDetail")


@_attrs_define
class UserDetail:
    """Detailed user record with secrets masked.

    Attributes:
        auth_configured (Union[Unset, bool]):  Example: True.
        connected (Union[Unset, bool]):  Example: True.
        connected_flag (Union[Unset, bool]):  Example: True.
        device_id (Union[Unset, str]):  Example: 6e8ed92f-....
        events (Union[Unset, list[str]]):  Example: ['Message', 'ReadReceipt'].
        history (Union[Unset, int]):  Example: 100.
        id (Union[Unset, str]):  Example: a7e5dd6b-8b3e-4035-ba87-3f96a0e3f5c0.
        max_user_id (Union[Unset, int]):  Example: 123456789.
        media_delivery (Union[Unset, str]):  Example: base64.
        name (Union[Unset, str]):  Example: John Doe.
        proxy_configured (Union[Unset, bool]):
        proxy_url (Union[Unset, str]):  Example: http://user:***@proxy.internal:3128.
        s3_bucket (Union[Unset, str]):
        s3_enabled (Union[Unset, bool]):
        s3_endpoint (Union[Unset, str]):
        s3_region (Union[Unset, str]):
        token (Union[Unset, str]):  Example: abc123def456.
        webhook (Union[Unset, str]):  Example: https://example.com/webhook.
    """

    auth_configured: Union[Unset, bool] = UNSET
    connected: Union[Unset, bool] = UNSET
    connected_flag: Union[Unset, bool] = UNSET
    device_id: Union[Unset, str] = UNSET
    events: Union[Unset, list[str]] = UNSET
    history: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    max_user_id: Union[Unset, int] = UNSET
    media_delivery: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    proxy_configured: Union[Unset, bool] = UNSET
    proxy_url: Union[Unset, str] = UNSET
    s3_bucket: Union[Unset, str] = UNSET
    s3_enabled: Union[Unset, bool] = UNSET
    s3_endpoint: Union[Unset, str] = UNSET
    s3_region: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    webhook: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_configured = self.auth_configured

        connected = self.connected

        connected_flag = self.connected_flag

        device_id = self.device_id

        events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        history = self.history

        id = self.id

        max_user_id = self.max_user_id

        media_delivery = self.media_delivery

        name = self.name

        proxy_configured = self.proxy_configured

        proxy_url = self.proxy_url

        s3_bucket = self.s3_bucket

        s3_enabled = self.s3_enabled

        s3_endpoint = self.s3_endpoint

        s3_region = self.s3_region

        token = self.token

        webhook = self.webhook

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_configured is not UNSET:
            field_dict["auth_configured"] = auth_configured
        if connected is not UNSET:
            field_dict["connected"] = connected
        if connected_flag is not UNSET:
            field_dict["connected_flag"] = connected_flag
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if events is not UNSET:
            field_dict["events"] = events
        if history is not UNSET:
            field_dict["history"] = history
        if id is not UNSET:
            field_dict["id"] = id
        if max_user_id is not UNSET:
            field_dict["max_user_id"] = max_user_id
        if media_delivery is not UNSET:
            field_dict["media_delivery"] = media_delivery
        if name is not UNSET:
            field_dict["name"] = name
        if proxy_configured is not UNSET:
            field_dict["proxy_configured"] = proxy_configured
        if proxy_url is not UNSET:
            field_dict["proxy_url"] = proxy_url
        if s3_bucket is not UNSET:
            field_dict["s3_bucket"] = s3_bucket
        if s3_enabled is not UNSET:
            field_dict["s3_enabled"] = s3_enabled
        if s3_endpoint is not UNSET:
            field_dict["s3_endpoint"] = s3_endpoint
        if s3_region is not UNSET:
            field_dict["s3_region"] = s3_region
        if token is not UNSET:
            field_dict["token"] = token
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_configured = d.pop("auth_configured", UNSET)

        connected = d.pop("connected", UNSET)

        connected_flag = d.pop("connected_flag", UNSET)

        device_id = d.pop("device_id", UNSET)

        events = cast(list[str], d.pop("events", UNSET))

        history = d.pop("history", UNSET)

        id = d.pop("id", UNSET)

        max_user_id = d.pop("max_user_id", UNSET)

        media_delivery = d.pop("media_delivery", UNSET)

        name = d.pop("name", UNSET)

        proxy_configured = d.pop("proxy_configured", UNSET)

        proxy_url = d.pop("proxy_url", UNSET)

        s3_bucket = d.pop("s3_bucket", UNSET)

        s3_enabled = d.pop("s3_enabled", UNSET)

        s3_endpoint = d.pop("s3_endpoint", UNSET)

        s3_region = d.pop("s3_region", UNSET)

        token = d.pop("token", UNSET)

        webhook = d.pop("webhook", UNSET)

        user_detail = cls(
            auth_configured=auth_configured,
            connected=connected,
            connected_flag=connected_flag,
            device_id=device_id,
            events=events,
            history=history,
            id=id,
            max_user_id=max_user_id,
            media_delivery=media_delivery,
            name=name,
            proxy_configured=proxy_configured,
            proxy_url=proxy_url,
            s3_bucket=s3_bucket,
            s3_enabled=s3_enabled,
            s3_endpoint=s3_endpoint,
            s3_region=s3_region,
            token=token,
            webhook=webhook,
        )

        user_detail.additional_properties = d
        return user_detail

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
