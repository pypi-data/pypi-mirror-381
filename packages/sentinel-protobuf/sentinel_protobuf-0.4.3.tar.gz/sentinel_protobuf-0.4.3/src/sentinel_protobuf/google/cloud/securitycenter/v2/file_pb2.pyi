from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ('path', 'size', 'sha256', 'hashed_size', 'partially_hashed', 'contents', 'disk_path', 'operations')

    class DiskPath(_message.Message):
        __slots__ = ('partition_uuid', 'relative_path')
        PARTITION_UUID_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
        partition_uuid: str
        relative_path: str

        def __init__(self, partition_uuid: _Optional[str]=..., relative_path: _Optional[str]=...) -> None:
            ...

    class FileOperation(_message.Message):
        __slots__ = ('type',)

        class OperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OPERATION_TYPE_UNSPECIFIED: _ClassVar[File.FileOperation.OperationType]
            OPEN: _ClassVar[File.FileOperation.OperationType]
            READ: _ClassVar[File.FileOperation.OperationType]
            RENAME: _ClassVar[File.FileOperation.OperationType]
            WRITE: _ClassVar[File.FileOperation.OperationType]
            EXECUTE: _ClassVar[File.FileOperation.OperationType]
        OPERATION_TYPE_UNSPECIFIED: File.FileOperation.OperationType
        OPEN: File.FileOperation.OperationType
        READ: File.FileOperation.OperationType
        RENAME: File.FileOperation.OperationType
        WRITE: File.FileOperation.OperationType
        EXECUTE: File.FileOperation.OperationType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: File.FileOperation.OperationType

        def __init__(self, type: _Optional[_Union[File.FileOperation.OperationType, str]]=...) -> None:
            ...
    PATH_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    HASHED_SIZE_FIELD_NUMBER: _ClassVar[int]
    PARTIALLY_HASHED_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    DISK_PATH_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    path: str
    size: int
    sha256: str
    hashed_size: int
    partially_hashed: bool
    contents: str
    disk_path: File.DiskPath
    operations: _containers.RepeatedCompositeFieldContainer[File.FileOperation]

    def __init__(self, path: _Optional[str]=..., size: _Optional[int]=..., sha256: _Optional[str]=..., hashed_size: _Optional[int]=..., partially_hashed: bool=..., contents: _Optional[str]=..., disk_path: _Optional[_Union[File.DiskPath, _Mapping]]=..., operations: _Optional[_Iterable[_Union[File.FileOperation, _Mapping]]]=...) -> None:
        ...