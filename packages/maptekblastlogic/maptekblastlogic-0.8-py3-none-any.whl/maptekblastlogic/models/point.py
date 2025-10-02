from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Point")


@_attrs_define
class Point:
    """
    Attributes:
        x (Union[None, Unset, float]):
        y (Union[None, Unset, float]):
        z (Union[None, Unset, float]):
    """

    x: Union[None, Unset, float] = UNSET
    y: Union[None, Unset, float] = UNSET
    z: Union[None, Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        x: Union[None, Unset, float]
        if isinstance(self.x, Unset):
            x = UNSET
        else:
            x = self.x

        y: Union[None, Unset, float]
        if isinstance(self.y, Unset):
            y = UNSET
        else:
            y = self.y

        z: Union[None, Unset, float]
        if isinstance(self.z, Unset):
            z = UNSET
        else:
            z = self.z

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if z is not UNSET:
            field_dict["z"] = z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_x(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        x = _parse_x(d.pop("x", UNSET))

        def _parse_y(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        y = _parse_y(d.pop("y", UNSET))

        def _parse_z(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        z = _parse_z(d.pop("z", UNSET))

        point = cls(
            x=x,
            y=y,
            z=z,
        )

        return point
