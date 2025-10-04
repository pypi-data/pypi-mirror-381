from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BigQueryDestination(_message.Message):
    __slots__ = ('table_uri', 'write_disposition')

    class WriteDisposition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WRITE_DISPOSITION_UNSPECIFIED: _ClassVar[BigQueryDestination.WriteDisposition]
        WRITE_EMPTY: _ClassVar[BigQueryDestination.WriteDisposition]
        WRITE_TRUNCATE: _ClassVar[BigQueryDestination.WriteDisposition]
    WRITE_DISPOSITION_UNSPECIFIED: BigQueryDestination.WriteDisposition
    WRITE_EMPTY: BigQueryDestination.WriteDisposition
    WRITE_TRUNCATE: BigQueryDestination.WriteDisposition
    TABLE_URI_FIELD_NUMBER: _ClassVar[int]
    WRITE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    table_uri: str
    write_disposition: BigQueryDestination.WriteDisposition

    def __init__(self, table_uri: _Optional[str]=..., write_disposition: _Optional[_Union[BigQueryDestination.WriteDisposition, str]]=...) -> None:
        ...