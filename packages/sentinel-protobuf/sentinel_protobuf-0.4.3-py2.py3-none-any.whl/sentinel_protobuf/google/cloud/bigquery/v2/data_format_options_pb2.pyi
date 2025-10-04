from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataFormatOptions(_message.Message):
    __slots__ = ('use_int64_timestamp', 'timestamp_output_format')

    class TimestampOutputFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIMESTAMP_OUTPUT_FORMAT_UNSPECIFIED: _ClassVar[DataFormatOptions.TimestampOutputFormat]
        FLOAT64: _ClassVar[DataFormatOptions.TimestampOutputFormat]
        INT64: _ClassVar[DataFormatOptions.TimestampOutputFormat]
        ISO8601_STRING: _ClassVar[DataFormatOptions.TimestampOutputFormat]
    TIMESTAMP_OUTPUT_FORMAT_UNSPECIFIED: DataFormatOptions.TimestampOutputFormat
    FLOAT64: DataFormatOptions.TimestampOutputFormat
    INT64: DataFormatOptions.TimestampOutputFormat
    ISO8601_STRING: DataFormatOptions.TimestampOutputFormat
    USE_INT64_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_OUTPUT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    use_int64_timestamp: bool
    timestamp_output_format: DataFormatOptions.TimestampOutputFormat

    def __init__(self, use_int64_timestamp: bool=..., timestamp_output_format: _Optional[_Union[DataFormatOptions.TimestampOutputFormat, str]]=...) -> None:
        ...