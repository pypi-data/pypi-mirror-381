from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ManagedTableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MANAGED_TABLE_TYPE_UNSPECIFIED: _ClassVar[ManagedTableType]
    NATIVE: _ClassVar[ManagedTableType]
    BIGLAKE: _ClassVar[ManagedTableType]
MANAGED_TABLE_TYPE_UNSPECIFIED: ManagedTableType
NATIVE: ManagedTableType
BIGLAKE: ManagedTableType