from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserDetail")


@_attrs_define
class UserDetail:
    """
    Attributes:
        id (str):  Example: 6f1c2d4e-8b3e-4035-ba87-3f96a0e3f5c0.
        name (str):  Example: Shop bot.
        token (str): The account token Example: 0b7a9e31-5d2c-4f6a-9e8b-1c2d3e4f5a6b.
        webhook (str):  Example: https://example.com/webhook.
        max_user_id (int): The MAX id stored at the last login; 0 before the first Example: 123456789.
        device_id (str): The device id the gateway logs into MAX with Example: 6e8ed92f-1c2d-4e5f-8a9b-0c1d2e3f4a5b.
        connected (bool): The MAX connection is up now Example: True.
        connected_flag (bool): The stored connected flag Example: True.
        auth_configured (bool): A MAX login (auth token) is stored; the token itself is never shown Example: True.
        events (list[str]): The stored subscription Example: ['Sync', 'QRAuthorized'].
        proxy_configured (bool):
        proxy_url (str): The proxy URL with its password replaced by `***` Example: http://user:***@proxy.internal:3128.
        history (int): How many messages per chat the gateway keeps in its history; 0 keeps none
        s3_enabled (bool):
        s3_endpoint (str):
        s3_region (str):
        s3_bucket (str):
        media_delivery (str): `base64`, `s3` or `both`: how photos of incoming messages reach the webhook Example:
            base64.
    """

    id: str
    name: str
    token: str
    webhook: str
    max_user_id: int
    device_id: str
    connected: bool
    connected_flag: bool
    auth_configured: bool
    events: list[str]
    proxy_configured: bool
    proxy_url: str
    history: int
    s3_enabled: bool
    s3_endpoint: str
    s3_region: str
    s3_bucket: str
    media_delivery: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        token = self.token

        webhook = self.webhook

        max_user_id = self.max_user_id

        device_id = self.device_id

        connected = self.connected

        connected_flag = self.connected_flag

        auth_configured = self.auth_configured

        events = self.events

        proxy_configured = self.proxy_configured

        proxy_url = self.proxy_url

        history = self.history

        s3_enabled = self.s3_enabled

        s3_endpoint = self.s3_endpoint

        s3_region = self.s3_region

        s3_bucket = self.s3_bucket

        media_delivery = self.media_delivery

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "token": token,
                "webhook": webhook,
                "max_user_id": max_user_id,
                "device_id": device_id,
                "connected": connected,
                "connected_flag": connected_flag,
                "auth_configured": auth_configured,
                "events": events,
                "proxy_configured": proxy_configured,
                "proxy_url": proxy_url,
                "history": history,
                "s3_enabled": s3_enabled,
                "s3_endpoint": s3_endpoint,
                "s3_region": s3_region,
                "s3_bucket": s3_bucket,
                "media_delivery": media_delivery,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        token = d.pop("token")

        webhook = d.pop("webhook")

        max_user_id = d.pop("max_user_id")

        device_id = d.pop("device_id")

        connected = d.pop("connected")

        connected_flag = d.pop("connected_flag")

        auth_configured = d.pop("auth_configured")

        events = cast(list[str], d.pop("events"))

        proxy_configured = d.pop("proxy_configured")

        proxy_url = d.pop("proxy_url")

        history = d.pop("history")

        s3_enabled = d.pop("s3_enabled")

        s3_endpoint = d.pop("s3_endpoint")

        s3_region = d.pop("s3_region")

        s3_bucket = d.pop("s3_bucket")

        media_delivery = d.pop("media_delivery")

        user_detail = cls(
            id=id,
            name=name,
            token=token,
            webhook=webhook,
            max_user_id=max_user_id,
            device_id=device_id,
            connected=connected,
            connected_flag=connected_flag,
            auth_configured=auth_configured,
            events=events,
            proxy_configured=proxy_configured,
            proxy_url=proxy_url,
            history=history,
            s3_enabled=s3_enabled,
            s3_endpoint=s3_endpoint,
            s3_region=s3_region,
            s3_bucket=s3_bucket,
            media_delivery=media_delivery,
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
