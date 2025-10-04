from google.api import resource_pb2 as _resource_pb2
from google.type import localized_text_pb2 as _localized_text_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AddressDescriptor(_message.Message):
    __slots__ = ('landmarks', 'areas')

    class Landmark(_message.Message):
        __slots__ = ('name', 'place_id', 'display_name', 'types', 'spatial_relationship', 'straight_line_distance_meters', 'travel_distance_meters')

        class SpatialRelationship(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NEAR: _ClassVar[AddressDescriptor.Landmark.SpatialRelationship]
            WITHIN: _ClassVar[AddressDescriptor.Landmark.SpatialRelationship]
            BESIDE: _ClassVar[AddressDescriptor.Landmark.SpatialRelationship]
            ACROSS_THE_ROAD: _ClassVar[AddressDescriptor.Landmark.SpatialRelationship]
            DOWN_THE_ROAD: _ClassVar[AddressDescriptor.Landmark.SpatialRelationship]
            AROUND_THE_CORNER: _ClassVar[AddressDescriptor.Landmark.SpatialRelationship]
            BEHIND: _ClassVar[AddressDescriptor.Landmark.SpatialRelationship]
        NEAR: AddressDescriptor.Landmark.SpatialRelationship
        WITHIN: AddressDescriptor.Landmark.SpatialRelationship
        BESIDE: AddressDescriptor.Landmark.SpatialRelationship
        ACROSS_THE_ROAD: AddressDescriptor.Landmark.SpatialRelationship
        DOWN_THE_ROAD: AddressDescriptor.Landmark.SpatialRelationship
        AROUND_THE_CORNER: AddressDescriptor.Landmark.SpatialRelationship
        BEHIND: AddressDescriptor.Landmark.SpatialRelationship
        NAME_FIELD_NUMBER: _ClassVar[int]
        PLACE_ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        TYPES_FIELD_NUMBER: _ClassVar[int]
        SPATIAL_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
        STRAIGHT_LINE_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
        TRAVEL_DISTANCE_METERS_FIELD_NUMBER: _ClassVar[int]
        name: str
        place_id: str
        display_name: _localized_text_pb2.LocalizedText
        types: _containers.RepeatedScalarFieldContainer[str]
        spatial_relationship: AddressDescriptor.Landmark.SpatialRelationship
        straight_line_distance_meters: float
        travel_distance_meters: float

        def __init__(self, name: _Optional[str]=..., place_id: _Optional[str]=..., display_name: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]]=..., types: _Optional[_Iterable[str]]=..., spatial_relationship: _Optional[_Union[AddressDescriptor.Landmark.SpatialRelationship, str]]=..., straight_line_distance_meters: _Optional[float]=..., travel_distance_meters: _Optional[float]=...) -> None:
            ...

    class Area(_message.Message):
        __slots__ = ('name', 'place_id', 'display_name', 'containment')

        class Containment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONTAINMENT_UNSPECIFIED: _ClassVar[AddressDescriptor.Area.Containment]
            WITHIN: _ClassVar[AddressDescriptor.Area.Containment]
            OUTSKIRTS: _ClassVar[AddressDescriptor.Area.Containment]
            NEAR: _ClassVar[AddressDescriptor.Area.Containment]
        CONTAINMENT_UNSPECIFIED: AddressDescriptor.Area.Containment
        WITHIN: AddressDescriptor.Area.Containment
        OUTSKIRTS: AddressDescriptor.Area.Containment
        NEAR: AddressDescriptor.Area.Containment
        NAME_FIELD_NUMBER: _ClassVar[int]
        PLACE_ID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        CONTAINMENT_FIELD_NUMBER: _ClassVar[int]
        name: str
        place_id: str
        display_name: _localized_text_pb2.LocalizedText
        containment: AddressDescriptor.Area.Containment

        def __init__(self, name: _Optional[str]=..., place_id: _Optional[str]=..., display_name: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]]=..., containment: _Optional[_Union[AddressDescriptor.Area.Containment, str]]=...) -> None:
            ...
    LANDMARKS_FIELD_NUMBER: _ClassVar[int]
    AREAS_FIELD_NUMBER: _ClassVar[int]
    landmarks: _containers.RepeatedCompositeFieldContainer[AddressDescriptor.Landmark]
    areas: _containers.RepeatedCompositeFieldContainer[AddressDescriptor.Area]

    def __init__(self, landmarks: _Optional[_Iterable[_Union[AddressDescriptor.Landmark, _Mapping]]]=..., areas: _Optional[_Iterable[_Union[AddressDescriptor.Area, _Mapping]]]=...) -> None:
        ...