from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LocationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOCATION_LEVEL_UNSPECIFIED: _ClassVar[LocationLevel]
    REGION: _ClassVar[LocationLevel]
    ZONE: _ClassVar[LocationLevel]
    GLOBAL: _ClassVar[LocationLevel]
    METRO: _ClassVar[LocationLevel]
    DUAL_REGION: _ClassVar[LocationLevel]
    MULTI_REGION: _ClassVar[LocationLevel]
LOCATION_LEVEL_UNSPECIFIED: LocationLevel
REGION: LocationLevel
ZONE: LocationLevel
GLOBAL: LocationLevel
METRO: LocationLevel
DUAL_REGION: LocationLevel
MULTI_REGION: LocationLevel

class LocationIdentifier(_message.Message):
    __slots__ = ('location_level', 'source', 'linked_locations')

    class LinkedLocation(_message.Message):
        __slots__ = ('location_level', 'location', 'label')
        LOCATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        location_level: LocationLevel
        location: str
        label: str

        def __init__(self, location_level: _Optional[_Union[LocationLevel, str]]=..., location: _Optional[str]=..., label: _Optional[str]=...) -> None:
            ...
    LOCATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LINKED_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    location_level: LocationLevel
    source: str
    linked_locations: _containers.RepeatedCompositeFieldContainer[LocationIdentifier.LinkedLocation]

    def __init__(self, location_level: _Optional[_Union[LocationLevel, str]]=..., source: _Optional[str]=..., linked_locations: _Optional[_Iterable[_Union[LocationIdentifier.LinkedLocation, _Mapping]]]=...) -> None:
        ...