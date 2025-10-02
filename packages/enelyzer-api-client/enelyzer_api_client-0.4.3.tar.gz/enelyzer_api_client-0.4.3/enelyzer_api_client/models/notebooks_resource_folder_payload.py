from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NotebooksResourceFolderPayload")


@_attrs_define
class NotebooksResourceFolderPayload:
    """
    Example:
        {'folderPath': '/metadata/metadata.json'}

    Attributes:
        folder_path (str):
    """

    folder_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        folder_path = self.folder_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "folderPath": folder_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        folder_path = d.pop("folderPath")

        notebooks_resource_folder_payload = cls(
            folder_path=folder_path,
        )

        notebooks_resource_folder_payload.additional_properties = d
        return notebooks_resource_folder_payload

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
