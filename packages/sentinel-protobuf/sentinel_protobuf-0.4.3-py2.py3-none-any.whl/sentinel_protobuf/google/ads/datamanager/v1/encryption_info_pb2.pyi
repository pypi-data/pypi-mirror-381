from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EncryptionInfo(_message.Message):
    __slots__ = ('gcp_wrapped_key_info',)
    GCP_WRAPPED_KEY_INFO_FIELD_NUMBER: _ClassVar[int]
    gcp_wrapped_key_info: GcpWrappedKeyInfo

    def __init__(self, gcp_wrapped_key_info: _Optional[_Union[GcpWrappedKeyInfo, _Mapping]]=...) -> None:
        ...

class GcpWrappedKeyInfo(_message.Message):
    __slots__ = ('key_type', 'wip_provider', 'kek_uri', 'encrypted_dek')

    class KeyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEY_TYPE_UNSPECIFIED: _ClassVar[GcpWrappedKeyInfo.KeyType]
        XCHACHA20_POLY1305: _ClassVar[GcpWrappedKeyInfo.KeyType]
    KEY_TYPE_UNSPECIFIED: GcpWrappedKeyInfo.KeyType
    XCHACHA20_POLY1305: GcpWrappedKeyInfo.KeyType
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    WIP_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    KEK_URI_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_DEK_FIELD_NUMBER: _ClassVar[int]
    key_type: GcpWrappedKeyInfo.KeyType
    wip_provider: str
    kek_uri: str
    encrypted_dek: str

    def __init__(self, key_type: _Optional[_Union[GcpWrappedKeyInfo.KeyType, str]]=..., wip_provider: _Optional[str]=..., kek_uri: _Optional[str]=..., encrypted_dek: _Optional[str]=...) -> None:
        ...