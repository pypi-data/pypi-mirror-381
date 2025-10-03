from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginSSOCodeExchangeResponse200")


@_attrs_define
class LoginSSOCodeExchangeResponse200:
    """
    Attributes:
        token (Union[Unset, str]): Session token for authentication
        csrf (Union[Unset, str]): CSRF token for request validation
    """

    token: Union[Unset, str] = UNSET
    csrf: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        csrf = self.csrf

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if csrf is not UNSET:
            field_dict["csrf"] = csrf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        csrf = d.pop("csrf", UNSET)

        login_sso_code_exchange_response_200 = cls(
            token=token,
            csrf=csrf,
        )

        login_sso_code_exchange_response_200.additional_properties = d
        return login_sso_code_exchange_response_200

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
