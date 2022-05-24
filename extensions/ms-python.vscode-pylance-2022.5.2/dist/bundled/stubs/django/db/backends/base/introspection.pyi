from collections import namedtuple
from typing import Any, Dict, Iterable, List, Optional, Set, Type

from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.utils import CursorWrapper
from django.db.models.base import Model

TableInfo = namedtuple("TableInfo", ["name", "type"])
FieldInfo = namedtuple(
    "FieldInfo",
    ["name", "type_code", "display_size", "internal_size", "precision", "scale", "null_ok", "default", "collation"],
)

class BaseDatabaseIntrospection:
    data_types_reverse: Any = ...
    connection: BaseDatabaseWrapper
    def __init__(self, connection: BaseDatabaseWrapper) -> None: ...
    def get_field_type(self, data_type: str, description: FieldInfo) -> str: ...
    def identifier_converter(self, name: str) -> str: ...
    def table_names(self, cursor: Optional[CursorWrapper] = ..., include_views: bool = ...) -> List[str]: ...
    def get_table_list(self, cursor: Optional[CursorWrapper]) -> Any: ...
    def get_table_description(self, cursor: Optional[CursorWrapper], table_name: str) -> Any: ...
    def get_migratable_models(self) -> Iterable[Type[Model]]: ...
    def django_table_names(self, only_existing: bool = ..., include_views: bool = ...) -> List[str]: ...
    def installed_models(self, tables: List[str]) -> Set[Type[Model]]: ...
    def sequence_list(self) -> List[Dict[str, str]]: ...
    def get_sequences(self, cursor: Optional[CursorWrapper], table_name: str, table_fields: Any = ...) -> Any: ...
    def get_relations(self, cursor: Optional[CursorWrapper], table_name: str) -> Any: ...
    def get_key_columns(self, cursor: Optional[CursorWrapper], table_name: str) -> Any: ...
    def get_primary_key_column(self, cursor: Optional[CursorWrapper], table_name: str) -> Optional[str]: ...
    def get_constraints(self, cursor: Optional[CursorWrapper], table_name: str) -> Any: ...