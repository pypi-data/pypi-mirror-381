from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ValidateExpressionAgainstRequesterResponse200")


@_attrs_define
class ValidateExpressionAgainstRequesterResponse200:
    """
    Attributes:
        requester_matches (bool): Whether the current user matches the expression.
    """

    requester_matches: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requester_matches = self.requester_matches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requester_matches": requester_matches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requester_matches = d.pop("requester_matches")

        validate_expression_against_requester_response_200 = cls(
            requester_matches=requester_matches,
        )

        validate_expression_against_requester_response_200.additional_properties = d
        return validate_expression_against_requester_response_200

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
