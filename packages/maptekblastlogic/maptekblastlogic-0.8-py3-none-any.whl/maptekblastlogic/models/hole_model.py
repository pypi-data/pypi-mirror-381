from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hole_geometry import HoleGeometry


T = TypeVar("T", bound="HoleModel")


@_attrs_define
class HoleModel:
    """Details of a hole.

    Attributes:
        hole_id (Union[Unset, int]): The unique identifier of this hole.
        blast_id (Union[Unset, int]): The ID of the blast this hole belongs to.
        hole_name (Union[None, Unset, str]): The name of this hole.
        row (Union[None, Unset, str]): The row this hole sits in. Can be null.
        echelon (Union[None, Unset, int]): The echelon this hole sits in. Can be null.
        status (Union[None, Unset, str]): The status of the hole.
        design (Union['HoleGeometry', None, Unset]): The hole geometry as designed.
        last_known (Union['HoleGeometry', None, Unset]): The hole geometry according to most recent data.
    """

    hole_id: Union[Unset, int] = UNSET
    blast_id: Union[Unset, int] = UNSET
    hole_name: Union[None, Unset, str] = UNSET
    row: Union[None, Unset, str] = UNSET
    echelon: Union[None, Unset, int] = UNSET
    status: Union[None, Unset, str] = UNSET
    design: Union["HoleGeometry", None, Unset] = UNSET
    last_known: Union["HoleGeometry", None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.hole_geometry import HoleGeometry

        hole_id = self.hole_id

        blast_id = self.blast_id

        hole_name: Union[None, Unset, str]
        if isinstance(self.hole_name, Unset):
            hole_name = UNSET
        else:
            hole_name = self.hole_name

        row: Union[None, Unset, str]
        if isinstance(self.row, Unset):
            row = UNSET
        else:
            row = self.row

        echelon: Union[None, Unset, int]
        if isinstance(self.echelon, Unset):
            echelon = UNSET
        else:
            echelon = self.echelon

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        design: Union[Dict[str, Any], None, Unset]
        if isinstance(self.design, Unset):
            design = UNSET
        elif isinstance(self.design, HoleGeometry):
            design = self.design.to_dict()
        else:
            design = self.design

        last_known: Union[Dict[str, Any], None, Unset]
        if isinstance(self.last_known, Unset):
            last_known = UNSET
        elif isinstance(self.last_known, HoleGeometry):
            last_known = self.last_known.to_dict()
        else:
            last_known = self.last_known

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if hole_id is not UNSET:
            field_dict["holeId"] = hole_id
        if blast_id is not UNSET:
            field_dict["blastId"] = blast_id
        if hole_name is not UNSET:
            field_dict["holeName"] = hole_name
        if row is not UNSET:
            field_dict["row"] = row
        if echelon is not UNSET:
            field_dict["echelon"] = echelon
        if status is not UNSET:
            field_dict["status"] = status
        if design is not UNSET:
            field_dict["design"] = design
        if last_known is not UNSET:
            field_dict["lastKnown"] = last_known

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hole_geometry import HoleGeometry

        d = src_dict.copy()
        hole_id = d.pop("holeId", UNSET)

        blast_id = d.pop("blastId", UNSET)

        def _parse_hole_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hole_name = _parse_hole_name(d.pop("holeName", UNSET))

        def _parse_row(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        row = _parse_row(d.pop("row", UNSET))

        def _parse_echelon(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        echelon = _parse_echelon(d.pop("echelon", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_design(data: object) -> Union["HoleGeometry", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                design_type_0 = HoleGeometry.from_dict(data)

                return design_type_0
            except:  # noqa: E722
                pass
            return cast(Union["HoleGeometry", None, Unset], data)

        design = _parse_design(d.pop("design", UNSET))

        def _parse_last_known(data: object) -> Union["HoleGeometry", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_known_type_0 = HoleGeometry.from_dict(data)

                return last_known_type_0
            except:  # noqa: E722
                pass
            return cast(Union["HoleGeometry", None, Unset], data)

        last_known = _parse_last_known(d.pop("lastKnown", UNSET))

        hole_model = cls(
            hole_id=hole_id,
            blast_id=blast_id,
            hole_name=hole_name,
            row=row,
            echelon=echelon,
            status=status,
            design=design,
            last_known=last_known,
        )

        return hole_model
