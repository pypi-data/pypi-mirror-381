from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RelocateBucketError(_message.Message):
    __slots__ = ('resource', 'object_id', 'source_location', 'destination_location', 'source_custom_placement_config', 'destination_custom_placement_config', 'relocation_errors', 'validate_only')

    class CustomPlacementConfig(_message.Message):
        __slots__ = ('data_locations',)
        DATA_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        data_locations: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, data_locations: _Optional[_Iterable[str]]=...) -> None:
            ...
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CUSTOM_PLACEMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_CUSTOM_PLACEMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RELOCATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    resource: str
    object_id: str
    source_location: str
    destination_location: str
    source_custom_placement_config: RelocateBucketError.CustomPlacementConfig
    destination_custom_placement_config: RelocateBucketError.CustomPlacementConfig
    relocation_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    validate_only: bool

    def __init__(self, resource: _Optional[str]=..., object_id: _Optional[str]=..., source_location: _Optional[str]=..., destination_location: _Optional[str]=..., source_custom_placement_config: _Optional[_Union[RelocateBucketError.CustomPlacementConfig, _Mapping]]=..., destination_custom_placement_config: _Optional[_Union[RelocateBucketError.CustomPlacementConfig, _Mapping]]=..., relocation_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=..., validate_only: bool=...) -> None:
        ...