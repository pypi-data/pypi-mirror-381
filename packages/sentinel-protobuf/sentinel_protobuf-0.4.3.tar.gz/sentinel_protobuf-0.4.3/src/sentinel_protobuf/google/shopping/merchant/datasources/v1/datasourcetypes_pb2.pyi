from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PrimaryProductDataSource(_message.Message):
    __slots__ = ('legacy_local', 'feed_label', 'content_language', 'countries', 'default_rule', 'contains_custom_rules', 'destinations')

    class DefaultRule(_message.Message):
        __slots__ = ('take_from_data_sources',)
        TAKE_FROM_DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
        take_from_data_sources: _containers.RepeatedCompositeFieldContainer[DataSourceReference]

        def __init__(self, take_from_data_sources: _Optional[_Iterable[_Union[DataSourceReference, _Mapping]]]=...) -> None:
            ...

    class Destination(_message.Message):
        __slots__ = ('destination', 'state')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[PrimaryProductDataSource.Destination.State]
            ENABLED: _ClassVar[PrimaryProductDataSource.Destination.State]
            DISABLED: _ClassVar[PrimaryProductDataSource.Destination.State]
        STATE_UNSPECIFIED: PrimaryProductDataSource.Destination.State
        ENABLED: PrimaryProductDataSource.Destination.State
        DISABLED: PrimaryProductDataSource.Destination.State
        DESTINATION_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        destination: _types_pb2.Destination.DestinationEnum
        state: PrimaryProductDataSource.Destination.State

        def __init__(self, destination: _Optional[_Union[_types_pb2.Destination.DestinationEnum, str]]=..., state: _Optional[_Union[PrimaryProductDataSource.Destination.State, str]]=...) -> None:
            ...
    LEGACY_LOCAL_FIELD_NUMBER: _ClassVar[int]
    FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_RULE_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_CUSTOM_RULES_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    legacy_local: bool
    feed_label: str
    content_language: str
    countries: _containers.RepeatedScalarFieldContainer[str]
    default_rule: PrimaryProductDataSource.DefaultRule
    contains_custom_rules: bool
    destinations: _containers.RepeatedCompositeFieldContainer[PrimaryProductDataSource.Destination]

    def __init__(self, legacy_local: bool=..., feed_label: _Optional[str]=..., content_language: _Optional[str]=..., countries: _Optional[_Iterable[str]]=..., default_rule: _Optional[_Union[PrimaryProductDataSource.DefaultRule, _Mapping]]=..., contains_custom_rules: bool=..., destinations: _Optional[_Iterable[_Union[PrimaryProductDataSource.Destination, _Mapping]]]=...) -> None:
        ...

class SupplementalProductDataSource(_message.Message):
    __slots__ = ('feed_label', 'content_language', 'referencing_primary_data_sources')
    FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    REFERENCING_PRIMARY_DATA_SOURCES_FIELD_NUMBER: _ClassVar[int]
    feed_label: str
    content_language: str
    referencing_primary_data_sources: _containers.RepeatedCompositeFieldContainer[DataSourceReference]

    def __init__(self, feed_label: _Optional[str]=..., content_language: _Optional[str]=..., referencing_primary_data_sources: _Optional[_Iterable[_Union[DataSourceReference, _Mapping]]]=...) -> None:
        ...

class LocalInventoryDataSource(_message.Message):
    __slots__ = ('feed_label', 'content_language')
    FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    feed_label: str
    content_language: str

    def __init__(self, feed_label: _Optional[str]=..., content_language: _Optional[str]=...) -> None:
        ...

class RegionalInventoryDataSource(_message.Message):
    __slots__ = ('feed_label', 'content_language')
    FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    feed_label: str
    content_language: str

    def __init__(self, feed_label: _Optional[str]=..., content_language: _Optional[str]=...) -> None:
        ...

class PromotionDataSource(_message.Message):
    __slots__ = ('target_country', 'content_language')
    TARGET_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    target_country: str
    content_language: str

    def __init__(self, target_country: _Optional[str]=..., content_language: _Optional[str]=...) -> None:
        ...

class ProductReviewDataSource(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MerchantReviewDataSource(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DataSourceReference(_message.Message):
    __slots__ = ('self', 'primary_data_source_name', 'supplemental_data_source_name')
    SELF_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_DATA_SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SUPPLEMENTAL_DATA_SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    self: bool
    primary_data_source_name: str
    supplemental_data_source_name: str

    def __init__(self, self_: bool=..., primary_data_source_name: _Optional[str]=..., supplemental_data_source_name: _Optional[str]=...) -> None:
        ...