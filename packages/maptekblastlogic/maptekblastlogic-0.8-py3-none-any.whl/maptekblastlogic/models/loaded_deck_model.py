import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadedDeckModel")


@_attrs_define
class LoadedDeckModel:
    """Describes the loading of an individual deck. This is raw data collected from the field that has not been validated
    and reconciled in BlastLogic Desktop. As such, decks may overlap with each other. This data should not be relied
    upon as the current state of the hole.

        Attributes:
            start_time (datetime.datetime): When charging this deck began (UTC).
            end_time (datetime.datetime): When charging this deck completed (UTC). Must be greater than or equal to
                'startTime'.
            product_id (int): The ID of the product used in this deck
            top_depth (float): The depth of the top of this deck (Metres). Can be null if unknown.
            bottom_depth (float): The depth of the bottom of this deck (Metres). Can be null if unknown.
            loaded_deck_id (Union[None, Unset, int]): The unique identifier if this loaded deck. Ignored when creating.
                Cannot be edited.
            etag (Union[None, Unset, str]): The loaded deck's current ETag. Ignored when creating and editing.
            created_by (Union[None, Unset, str]): Username of the person who created this loaded deck. Ignored when creating
                and editing.
            created_time (Union[Unset, datetime.datetime]): When this loaded deck was created (UTC). Ignored when creating
                and editing.
            last_modified_by (Union[None, Unset, str]): Username of the person who last updated this loaded deck. Ignored
                when creating and editing.
            last_modified_time (Union[Unset, datetime.datetime]): When this loaded deck was last updated (UTC). Ignored when
                creating and editing.
            hole_id (Union[None, Unset, int]): The ID of the hole this loaded deck relates to. Cannot be edited.
            is_deleted (Union[Unset, bool]): Whether this loaded deck is deleted. Deleted loaded decks are considered
                erroneous and all details are ignored.
            shot_firer_id (Union[None, Unset, int]): The ID of the person responsible for firing the blast. Can be null if
                unknown.
            crew_id (Union[None, Unset, int]): The ID of the crew that loaded this deck. Can be null if unknown.
            operator_id (Union[None, Unset, int]): The ID of the equipment operator. Can be null if unknown.
            loading_truck_id (Union[None, Unset, int]): The ID of the loading truck used to load this deck. Can be null if
                unknown.
            comment (Union[None, Unset, str]): Comments from the crew or operator about this loaded deck.
            mass (Union[None, Unset, float]): The mass of the product that was loaded into the hole (Kilograms). Cannot be
                negative. Can be null if unknown.
            quantity (Union[None, Unset, int]): The number of product loaded into the hole. Cannot be negative. Can be null
                if unknown.
    """

    start_time: datetime.datetime
    end_time: datetime.datetime
    product_id: int
    top_depth: float
    bottom_depth: float
    loaded_deck_id: Union[None, Unset, int] = UNSET
    etag: Union[None, Unset, str] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    created_time: Union[Unset, datetime.datetime] = UNSET
    last_modified_by: Union[None, Unset, str] = UNSET
    last_modified_time: Union[Unset, datetime.datetime] = UNSET
    hole_id: Union[None, Unset, int] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    shot_firer_id: Union[None, Unset, int] = UNSET
    crew_id: Union[None, Unset, int] = UNSET
    operator_id: Union[None, Unset, int] = UNSET
    loading_truck_id: Union[None, Unset, int] = UNSET
    comment: Union[None, Unset, str] = UNSET
    mass: Union[None, Unset, float] = UNSET
    quantity: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        product_id = self.product_id

        top_depth = self.top_depth

        bottom_depth = self.bottom_depth

        loaded_deck_id: Union[None, Unset, int]
        if isinstance(self.loaded_deck_id, Unset):
            loaded_deck_id = UNSET
        else:
            loaded_deck_id = self.loaded_deck_id

        etag: Union[None, Unset, str]
        if isinstance(self.etag, Unset):
            etag = UNSET
        else:
            etag = self.etag

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        created_time: Union[Unset, str] = UNSET
        if self.created_time and not isinstance(self.created_time, Unset):
            created_time = self.created_time.isoformat()

        last_modified_by: Union[None, Unset, str]
        if isinstance(self.last_modified_by, Unset):
            last_modified_by = UNSET
        else:
            last_modified_by = self.last_modified_by

        last_modified_time: Union[Unset, str] = UNSET
        if self.last_modified_time and not isinstance(self.last_modified_time, Unset):
            last_modified_time = self.last_modified_time.isoformat()

        hole_id: Union[None, Unset, int]
        if isinstance(self.hole_id, Unset):
            hole_id = UNSET
        else:
            hole_id = self.hole_id

        is_deleted = self.is_deleted

        shot_firer_id: Union[None, Unset, int]
        if isinstance(self.shot_firer_id, Unset):
            shot_firer_id = UNSET
        else:
            shot_firer_id = self.shot_firer_id

        crew_id: Union[None, Unset, int]
        if isinstance(self.crew_id, Unset):
            crew_id = UNSET
        else:
            crew_id = self.crew_id

        operator_id: Union[None, Unset, int]
        if isinstance(self.operator_id, Unset):
            operator_id = UNSET
        else:
            operator_id = self.operator_id

        loading_truck_id: Union[None, Unset, int]
        if isinstance(self.loading_truck_id, Unset):
            loading_truck_id = UNSET
        else:
            loading_truck_id = self.loading_truck_id

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        mass: Union[None, Unset, float]
        if isinstance(self.mass, Unset):
            mass = UNSET
        else:
            mass = self.mass

        quantity: Union[None, Unset, int]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "startTime": start_time,
                "endTime": end_time,
                "productId": product_id,
                "topDepth": top_depth,
                "bottomDepth": bottom_depth,
            }
        )
        if loaded_deck_id is not UNSET:
            field_dict["loadedDeckId"] = loaded_deck_id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if last_modified_by is not UNSET:
            field_dict["lastModifiedBy"] = last_modified_by
        if last_modified_time is not UNSET:
            field_dict["lastModifiedTime"] = last_modified_time
        if hole_id is not UNSET:
            field_dict["holeId"] = hole_id
        if is_deleted is not UNSET:
            field_dict["isDeleted"] = is_deleted
        if shot_firer_id is not UNSET:
            field_dict["shotFirerId"] = shot_firer_id
        if crew_id is not UNSET:
            field_dict["crewId"] = crew_id
        if operator_id is not UNSET:
            field_dict["operatorId"] = operator_id
        if loading_truck_id is not UNSET:
            field_dict["loadingTruckId"] = loading_truck_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if mass is not UNSET:
            field_dict["mass"] = mass
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_time = isoparse(d.pop("startTime"))

        end_time = isoparse(d.pop("endTime"))

        product_id = d.pop("productId")

        top_depth = d.pop("topDepth")

        bottom_depth = d.pop("bottomDepth")

        def _parse_loaded_deck_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        loaded_deck_id = _parse_loaded_deck_id(d.pop("loadedDeckId", UNSET))

        def _parse_etag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        etag = _parse_etag(d.pop("etag", UNSET))

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))

        _created_time = d.pop("createdTime", UNSET)
        created_time: Union[Unset, datetime.datetime]
        if isinstance(_created_time, Unset):
            created_time = UNSET
        else:
            created_time = isoparse(_created_time)

        def _parse_last_modified_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_modified_by = _parse_last_modified_by(d.pop("lastModifiedBy", UNSET))

        _last_modified_time = d.pop("lastModifiedTime", UNSET)
        last_modified_time: Union[Unset, datetime.datetime]
        if isinstance(_last_modified_time, Unset):
            last_modified_time = UNSET
        else:
            last_modified_time = isoparse(_last_modified_time)

        def _parse_hole_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        hole_id = _parse_hole_id(d.pop("holeId", UNSET))

        is_deleted = d.pop("isDeleted", UNSET)

        def _parse_shot_firer_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shot_firer_id = _parse_shot_firer_id(d.pop("shotFirerId", UNSET))

        def _parse_crew_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        crew_id = _parse_crew_id(d.pop("crewId", UNSET))

        def _parse_operator_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        operator_id = _parse_operator_id(d.pop("operatorId", UNSET))

        def _parse_loading_truck_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        loading_truck_id = _parse_loading_truck_id(d.pop("loadingTruckId", UNSET))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_mass(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        mass = _parse_mass(d.pop("mass", UNSET))

        def _parse_quantity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        loaded_deck_model = cls(
            start_time=start_time,
            end_time=end_time,
            product_id=product_id,
            top_depth=top_depth,
            bottom_depth=bottom_depth,
            loaded_deck_id=loaded_deck_id,
            etag=etag,
            created_by=created_by,
            created_time=created_time,
            last_modified_by=last_modified_by,
            last_modified_time=last_modified_time,
            hole_id=hole_id,
            is_deleted=is_deleted,
            shot_firer_id=shot_firer_id,
            crew_id=crew_id,
            operator_id=operator_id,
            loading_truck_id=loading_truck_id,
            comment=comment,
            mass=mass,
            quantity=quantity,
        )

        return loaded_deck_model
