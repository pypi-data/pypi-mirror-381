from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserNotifyProps")


@_attrs_define
class UserNotifyProps:
    """
    Attributes:
        email (Union[Unset, str]): Set to "true" to enable email notifications, "false" to disable. Defaults to "true".
        push (Union[Unset, str]): Set to "all" to receive push notifications for all activity, "mention" for mentions
            and direct messages only, and "none" to disable. Defaults to "mention".
        desktop (Union[Unset, str]): Set to "all" to receive desktop notifications for all activity, "mention" for
            mentions and direct messages only, and "none" to disable. Defaults to "all".
        desktop_sound (Union[Unset, str]): Set to "true" to enable sound on desktop notifications, "false" to disable.
            Defaults to "true".
        mention_keys (Union[Unset, str]): A comma-separated list of words to count as mentions. Defaults to username and
            @username.
        channel (Union[Unset, str]): Set to "true" to enable channel-wide notifications (@channel, @all, etc.), "false"
            to disable. Defaults to "true".
        first_name (Union[Unset, str]): Set to "true" to enable mentions for first name. Defaults to "true" if a first
            name is set, "false" otherwise.
        auto_responder_message (Union[Unset, str]): The message sent to users when they are auto-responded to. Defaults
            to "".
        push_threads (Union[Unset, str]): Set to "all" to enable mobile push notifications for followed threads and
            "none" to disable. Defaults to "all".
        comments (Union[Unset, str]): Set to "any" to enable notifications for comments to any post you have replied to,
            "root" for comments on your posts, and "never" to disable. Only affects users with collapsed reply threads
            disabled. Defaults to "never".
        desktop_threads (Union[Unset, str]): Set to "all" to enable desktop notifications for followed threads and
            "none" to disable. Defaults to "all".
        email_threads (Union[Unset, str]): Set to "all" to enable email notifications for followed threads and "none" to
            disable. Defaults to "all".
    """

    email: Union[Unset, str] = UNSET
    push: Union[Unset, str] = UNSET
    desktop: Union[Unset, str] = UNSET
    desktop_sound: Union[Unset, str] = UNSET
    mention_keys: Union[Unset, str] = UNSET
    channel: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    auto_responder_message: Union[Unset, str] = UNSET
    push_threads: Union[Unset, str] = UNSET
    comments: Union[Unset, str] = UNSET
    desktop_threads: Union[Unset, str] = UNSET
    email_threads: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        push = self.push

        desktop = self.desktop

        desktop_sound = self.desktop_sound

        mention_keys = self.mention_keys

        channel = self.channel

        first_name = self.first_name

        auto_responder_message = self.auto_responder_message

        push_threads = self.push_threads

        comments = self.comments

        desktop_threads = self.desktop_threads

        email_threads = self.email_threads

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if push is not UNSET:
            field_dict["push"] = push
        if desktop is not UNSET:
            field_dict["desktop"] = desktop
        if desktop_sound is not UNSET:
            field_dict["desktop_sound"] = desktop_sound
        if mention_keys is not UNSET:
            field_dict["mention_keys"] = mention_keys
        if channel is not UNSET:
            field_dict["channel"] = channel
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if auto_responder_message is not UNSET:
            field_dict["auto_responder_message"] = auto_responder_message
        if push_threads is not UNSET:
            field_dict["push_threads"] = push_threads
        if comments is not UNSET:
            field_dict["comments"] = comments
        if desktop_threads is not UNSET:
            field_dict["desktop_threads"] = desktop_threads
        if email_threads is not UNSET:
            field_dict["email_threads"] = email_threads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        push = d.pop("push", UNSET)

        desktop = d.pop("desktop", UNSET)

        desktop_sound = d.pop("desktop_sound", UNSET)

        mention_keys = d.pop("mention_keys", UNSET)

        channel = d.pop("channel", UNSET)

        first_name = d.pop("first_name", UNSET)

        auto_responder_message = d.pop("auto_responder_message", UNSET)

        push_threads = d.pop("push_threads", UNSET)

        comments = d.pop("comments", UNSET)

        desktop_threads = d.pop("desktop_threads", UNSET)

        email_threads = d.pop("email_threads", UNSET)

        user_notify_props = cls(
            email=email,
            push=push,
            desktop=desktop,
            desktop_sound=desktop_sound,
            mention_keys=mention_keys,
            channel=channel,
            first_name=first_name,
            auto_responder_message=auto_responder_message,
            push_threads=push_threads,
            comments=comments,
            desktop_threads=desktop_threads,
            email_threads=email_threads,
        )

        user_notify_props.additional_properties = d
        return user_notify_props

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
