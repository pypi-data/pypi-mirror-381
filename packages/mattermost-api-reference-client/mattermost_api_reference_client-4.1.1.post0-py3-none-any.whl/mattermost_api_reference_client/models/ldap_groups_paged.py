from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_group import LDAPGroup


T = TypeVar("T", bound="LDAPGroupsPaged")


@_attrs_define
class LDAPGroupsPaged:
    """A paged list of LDAP groups

    Attributes:
        count (Union[Unset, float]): Total number of groups
        groups (Union[Unset, list['LDAPGroup']]):
    """

    count: Union[Unset, float] = UNSET
    groups: Union[Unset, list["LDAPGroup"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ldap_group import LDAPGroup

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = LDAPGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        ldap_groups_paged = cls(
            count=count,
            groups=groups,
        )

        ldap_groups_paged.additional_properties = d
        return ldap_groups_paged

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
