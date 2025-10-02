from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteModel")


@_attrs_define
class SiteModel:
    """Details of a site.

    Attributes:
        site_code (str): The code of the site.
        name (str): The name of the site.
        is_active (Union[Unset, bool]): Whether this site is active.
    """

    site_code: str
    name: str
    is_active: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        site_code = self.site_code

        name = self.name

        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "siteCode": site_code,
                "name": name,
            }
        )
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        site_code = d.pop("siteCode")

        name = d.pop("name")

        is_active = d.pop("isActive", UNSET)

        site_model = cls(
            site_code=site_code,
            name=name,
            is_active=is_active,
        )

        return site_model
