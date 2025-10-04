"""Database abstraction layer."""

import copy
from abc import ABC, abstractmethod
from typing import Dict, Generic, Type, TypeVar

import pydantic
from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema

T = TypeVar("T", bound="DatabaseItem")


class ForeignKey(Generic[T]):
    """A reference to another DatabaseItem."""

    def __init__(self, target_type: type[T], identifier: str):
        self.target_type = target_type
        self.identifier = identifier

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, ForeignKey)
            and self.target_type == other.target_type
            and self.identifier == other.identifier
        )

    def __hash__(self) -> int:
        return hash((self.target_type, self.identifier))

    def __repr__(self) -> str:
        return f"ForeignKey({self.target_type.__name__}:{self.identifier})"

    #
    # --- Pydantic integration ---
    #
    @classmethod
    def __class_getitem__(cls, item: type[T]):
        target_type = item

        class _ForeignKey(cls):  # type: ignore
            __origin__ = cls
            __args__ = (item,)

            @classmethod
            def __get_pydantic_core_schema__(cls, source_type, handler: GetCoreSchemaHandler):
                def validator(v):
                    if isinstance(v, ForeignKey):
                        return v
                    if isinstance(v, target_type):
                        return ForeignKey(target_type, v.identifier)
                    if isinstance(v, str):
                        return ForeignKey(target_type, v)
                    raise TypeError(f"Cannot convert {v!r} to ForeignKey[{target_type.__name__}]")

                return core_schema.no_info_after_validator_function(
                    validator,
                    core_schema.union_schema(
                        [
                            core_schema.is_instance_schema(target_type),
                            core_schema.str_schema(),
                            core_schema.is_instance_schema(ForeignKey),
                        ]
                    ),
                )

            @classmethod
            def __get_pydantic_json_schema__(cls, _core_schema, handler):
                # Expose as string in OpenAPI
                return handler(core_schema.str_schema())

        return _ForeignKey


class DatabaseItem(ABC, pydantic.BaseModel):
    """Base class for database items."""

    model_config = pydantic.ConfigDict(revalidate_instances="always")

    @property
    @abstractmethod
    def identifier(self) -> str:
        """Database item identifier."""

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DatabaseItem):
            raise NotImplementedError
        return self.identifier == other.identifier

    def __hash__(self) -> int:
        return int.from_bytes(self.identifier.encode("utf-8"), "big")


class DatabaseError(Exception):
    """Errors related to database operations."""


class UnknownEntityError(DatabaseError):
    """Requested entity does not exist."""


class Database(ABC):
    """Database abstraction."""

    @abstractmethod
    def update(self, item: DatabaseItem) -> None:
        """Update entity."""

    @abstractmethod
    def get(self, schema: Type[T], identifier: str) -> T:
        """Return entity, raise UnknownEntityError if entity does not exist."""

    @abstractmethod
    def get_all(self, schema: Type[T]) -> Dict[str, T]:
        """Return all entities of schema."""

    @abstractmethod
    def delete(self, item: DatabaseItem, cascade: bool = False) -> None:
        """Delete entity."""

    @abstractmethod
    def find(self, schema: Type[T], **kwargs: str) -> Dict[str, T]:
        """Return all entities of schema matching the filter criteria."""


class DictDatabase(Database):
    """Simple Database implementation with dictionary."""

    def __init__(self) -> None:
        self.data: Dict[Type[DatabaseItem], Dict[str, DatabaseItem]] = {}

    def update(self, item: DatabaseItem) -> None:
        """Update data."""
        item_type = type(item)
        if item_type not in self.data:
            self.data[item_type] = {}
        self.data[item_type][item.identifier] = copy.deepcopy(item)

    def get(self, schema: Type[T], identifier: str) -> T:
        try:
            return self.data[schema][identifier]  # type: ignore
        except KeyError as exc:
            raise UnknownEntityError(f"Unknown identifier: {identifier}") from exc

    def get_all(self, schema: Type[T]) -> Dict[str, T]:
        try:
            return self.data[schema]  # type: ignore
        except KeyError as exc:
            raise DatabaseError(f"Unkonwn schema: {schema}") from exc

    def delete(self, item: DatabaseItem, cascade: bool = False) -> None:
        item_type = type(item)
        try:
            del self.data[item_type][item.identifier]
        except KeyError as exc:
            raise UnknownEntityError(f"Unknown identifier: {item.identifier}") from exc
        if cascade:
            for schema in self.data:
                for identifier, item in self.data[schema].items():
                    for attribute in item.__class__.model_fields:
                        if isinstance(attribute, ForeignKey) and attribute == item.identifier:
                            del self.data[schema][identifier]

    def find(self, schema: Type[T], **kwargs: str) -> Dict[str, T]:
        try:
            results = []
            for item in self.data[schema].values():  # type: ignore
                if all(getattr(item, k) == v for k, v in kwargs.items()):
                    results.append(item)
            return {item.identifier: item for item in results}  # type: ignore
        except KeyError as exc:
            raise DatabaseError(f"Unkonwn schema: {schema}") from exc
