from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LoginSSOCodeExchangeBody")


@_attrs_define
class LoginSSOCodeExchangeBody:
    """
    Attributes:
        login_code (str): Short-lived one-time code from SSO callback
        code_verifier (str): SAML verifier to prove code possession
        state (str): State parameter to prevent CSRF attacks
    """

    login_code: str
    code_verifier: str
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        login_code = self.login_code

        code_verifier = self.code_verifier

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login_code": login_code,
                "code_verifier": code_verifier,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login_code = d.pop("login_code")

        code_verifier = d.pop("code_verifier")

        state = d.pop("state")

        login_sso_code_exchange_body = cls(
            login_code=login_code,
            code_verifier=code_verifier,
            state=state,
        )

        login_sso_code_exchange_body.additional_properties = d
        return login_sso_code_exchange_body

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
