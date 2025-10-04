from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1 import cmek_config_service_pb2 as _cmek_config_service_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IdentityMappingStore(_message.Message):
    __slots__ = ('name', 'kms_key_name', 'cmek_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    CMEK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    kms_key_name: str
    cmek_config: _cmek_config_service_pb2.CmekConfig

    def __init__(self, name: _Optional[str]=..., kms_key_name: _Optional[str]=..., cmek_config: _Optional[_Union[_cmek_config_service_pb2.CmekConfig, _Mapping]]=...) -> None:
        ...

class IdentityMappingEntry(_message.Message):
    __slots__ = ('user_id', 'group_id', 'external_identity')
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    group_id: str
    external_identity: str

    def __init__(self, user_id: _Optional[str]=..., group_id: _Optional[str]=..., external_identity: _Optional[str]=...) -> None:
        ...