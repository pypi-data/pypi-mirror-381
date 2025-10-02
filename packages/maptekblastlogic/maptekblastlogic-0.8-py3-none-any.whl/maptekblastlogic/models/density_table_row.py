from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DensityTableRow")


@_attrs_define
class DensityTableRow:
    """
    Attributes:
        depth (Union[Unset, float]):
        average_density (Union[None, Unset, float]):
    """

    depth: Union[Unset, float] = UNSET
    average_density: Union[None, Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        depth = self.depth

        average_density: Union[None, Unset, float]
        if isinstance(self.average_density, Unset):
            average_density = UNSET
        else:
            average_density = self.average_density

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if depth is not UNSET:
            field_dict["depth"] = depth
        if average_density is not UNSET:
            field_dict["averageDensity"] = average_density

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        depth = d.pop("depth", UNSET)

        def _parse_average_density(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        average_density = _parse_average_density(d.pop("averageDensity", UNSET))

        density_table_row = cls(
            depth=depth,
            average_density=average_density,
        )

        return density_table_row
