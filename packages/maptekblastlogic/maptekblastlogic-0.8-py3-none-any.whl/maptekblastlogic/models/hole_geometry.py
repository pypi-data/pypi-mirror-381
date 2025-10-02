from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.point import Point


T = TypeVar("T", bound="HoleGeometry")


@_attrs_define
class HoleGeometry:
    """
    Attributes:
        collar (Union['Point', None, Unset]): The position of the hole.
        angle (Union[None, Unset, float]): The hole angle from vertical towards the direction of the bearing (Degrees).
        bearing (Union[None, Unset, float]): The compass bearing the hole is pointing. Clockwise from north (Degrees).
        depth (Union[None, Unset, float]): The depth of the hole (Meters).
        diameter (Union[None, Unset, float]): The diameter of the hole (Meters).
    """

    collar: Union["Point", None, Unset] = UNSET
    angle: Union[None, Unset, float] = UNSET
    bearing: Union[None, Unset, float] = UNSET
    depth: Union[None, Unset, float] = UNSET
    diameter: Union[None, Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.point import Point

        collar: Union[Dict[str, Any], None, Unset]
        if isinstance(self.collar, Unset):
            collar = UNSET
        elif isinstance(self.collar, Point):
            collar = self.collar.to_dict()
        else:
            collar = self.collar

        angle: Union[None, Unset, float]
        if isinstance(self.angle, Unset):
            angle = UNSET
        else:
            angle = self.angle

        bearing: Union[None, Unset, float]
        if isinstance(self.bearing, Unset):
            bearing = UNSET
        else:
            bearing = self.bearing

        depth: Union[None, Unset, float]
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

        diameter: Union[None, Unset, float]
        if isinstance(self.diameter, Unset):
            diameter = UNSET
        else:
            diameter = self.diameter

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if collar is not UNSET:
            field_dict["collar"] = collar
        if angle is not UNSET:
            field_dict["angle"] = angle
        if bearing is not UNSET:
            field_dict["bearing"] = bearing
        if depth is not UNSET:
            field_dict["depth"] = depth
        if diameter is not UNSET:
            field_dict["diameter"] = diameter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.point import Point

        d = src_dict.copy()

        def _parse_collar(data: object) -> Union["Point", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                collar_type_0 = Point.from_dict(data)

                return collar_type_0
            except:  # noqa: E722
                pass
            return cast(Union["Point", None, Unset], data)

        collar = _parse_collar(d.pop("collar", UNSET))

        def _parse_angle(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        angle = _parse_angle(d.pop("angle", UNSET))

        def _parse_bearing(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bearing = _parse_bearing(d.pop("bearing", UNSET))

        def _parse_depth(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        depth = _parse_depth(d.pop("depth", UNSET))

        def _parse_diameter(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        diameter = _parse_diameter(d.pop("diameter", UNSET))

        hole_geometry = cls(
            collar=collar,
            angle=angle,
            bearing=bearing,
            depth=depth,
            diameter=diameter,
        )

        return hole_geometry
