from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateExpressionAgainstRequesterBody")


@_attrs_define
class ValidateExpressionAgainstRequesterBody:
    """
    Attributes:
        expression (str): The CEL expression to validate against the current user.
        channel_id (Union[Unset, str]): The channel ID for channel-specific permission checks (required for channel
            admins).
    """

    expression: str
    channel_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expression = self.expression

        channel_id = self.channel_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expression": expression,
            }
        )
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expression = d.pop("expression")

        channel_id = d.pop("channelId", UNSET)

        validate_expression_against_requester_body = cls(
            expression=expression,
            channel_id=channel_id,
        )

        validate_expression_against_requester_body.additional_properties = d
        return validate_expression_against_requester_body

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
