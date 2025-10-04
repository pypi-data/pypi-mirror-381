from google.ads.googleads.v21.enums import placement_type_pb2 as _placement_type_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GroupContentSuitabilityPlacementView(_message.Message):
    __slots__ = ('resource_name', 'display_name', 'placement', 'placement_type', 'target_url')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_URL_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    display_name: str
    placement: str
    placement_type: _placement_type_pb2.PlacementTypeEnum.PlacementType
    target_url: str

    def __init__(self, resource_name: _Optional[str]=..., display_name: _Optional[str]=..., placement: _Optional[str]=..., placement_type: _Optional[_Union[_placement_type_pb2.PlacementTypeEnum.PlacementType, str]]=..., target_url: _Optional[str]=...) -> None:
        ...