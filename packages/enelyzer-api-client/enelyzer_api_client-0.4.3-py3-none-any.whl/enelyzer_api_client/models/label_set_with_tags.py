from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.minimal_tag import MinimalTag


T = TypeVar("T", bound="LabelSetWithTags")


@_attrs_define
class LabelSetWithTags:
    """
    Example:
        {'labelSet': ['HVAC', 'Main Building'], 'tags': [{'id': '550e8400-e29b-41d4-a716-446655440000', 'name': 'Main
            Building Electricity', 'technicalName': 'main_building_electricity'}]}

    Attributes:
        label_set (list[str]):
        tags (list['MinimalTag']):
    """

    label_set: list[str]
    tags: list["MinimalTag"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label_set = self.label_set

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labelSet": label_set,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.minimal_tag import MinimalTag

        d = dict(src_dict)
        label_set = cast(list[str], d.pop("labelSet"))

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = MinimalTag.from_dict(tags_item_data)

            tags.append(tags_item)

        label_set_with_tags = cls(
            label_set=label_set,
            tags=tags,
        )

        label_set_with_tags.additional_properties = d
        return label_set_with_tags

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
