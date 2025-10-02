from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LabeledTagsInFacilityPayload")


@_attrs_define
class LabeledTagsInFacilityPayload:
    """
    Example:
        {'facilityId': '56933811-3a54-4138-8181-4470a900412e', 'labelKey': 'notebookLabels', 'labelSets': [['Label1',
            'Label2'], ['Label3', 'Label4']]}

    Attributes:
        facility_id (UUID):
        label_key (str):
        label_sets (list[list[str]]):
    """

    facility_id: UUID
    label_key: str
    label_sets: list[list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facility_id = str(self.facility_id)

        label_key = self.label_key

        label_sets = []
        for label_sets_item_data in self.label_sets:
            label_sets_item = label_sets_item_data

            label_sets.append(label_sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "facilityId": facility_id,
                "labelKey": label_key,
                "labelSets": label_sets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        facility_id = UUID(d.pop("facilityId"))

        label_key = d.pop("labelKey")

        label_sets = []
        _label_sets = d.pop("labelSets")
        for label_sets_item_data in _label_sets:
            label_sets_item = cast(list[str], label_sets_item_data)

            label_sets.append(label_sets_item)

        labeled_tags_in_facility_payload = cls(
            facility_id=facility_id,
            label_key=label_key,
            label_sets=label_sets,
        )

        labeled_tags_in_facility_payload.additional_properties = d
        return labeled_tags_in_facility_payload

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
