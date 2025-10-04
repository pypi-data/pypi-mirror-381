from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1 import serving_config_pb2 as _serving_config_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UpdateServingConfigRequest(_message.Message):
    __slots__ = ('serving_config', 'update_mask')
    SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    serving_config: _serving_config_pb2.ServingConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, serving_config: _Optional[_Union[_serving_config_pb2.ServingConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...