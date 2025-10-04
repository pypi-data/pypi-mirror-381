from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GCAEntitlementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GCA_ENTITLEMENT_TYPE_UNSPECIFIED: _ClassVar[GCAEntitlementType]
    GCA_STANDARD: _ClassVar[GCAEntitlementType]
GCA_ENTITLEMENT_TYPE_UNSPECIFIED: GCAEntitlementType
GCA_STANDARD: GCAEntitlementType

class GeminiClusterConfig(_message.Message):
    __slots__ = ('entitled',)
    ENTITLED_FIELD_NUMBER: _ClassVar[int]
    entitled: bool

    def __init__(self, entitled: bool=...) -> None:
        ...

class GeminiInstanceConfig(_message.Message):
    __slots__ = ('entitled',)
    ENTITLED_FIELD_NUMBER: _ClassVar[int]
    entitled: bool

    def __init__(self, entitled: bool=...) -> None:
        ...

class GCAInstanceConfig(_message.Message):
    __slots__ = ('gca_entitlement',)
    GCA_ENTITLEMENT_FIELD_NUMBER: _ClassVar[int]
    gca_entitlement: GCAEntitlementType

    def __init__(self, gca_entitlement: _Optional[_Union[GCAEntitlementType, str]]=...) -> None:
        ...