from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CUSTOMER_TYPE_UNSPECIFIED: _ClassVar[CustomerType]
    NEW: _ClassVar[CustomerType]
    RETURNING: _ClassVar[CustomerType]
    REENGAGED: _ClassVar[CustomerType]

class CustomerValueBucket(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CUSTOMER_VALUE_BUCKET_UNSPECIFIED: _ClassVar[CustomerValueBucket]
    LOW: _ClassVar[CustomerValueBucket]
    MEDIUM: _ClassVar[CustomerValueBucket]
    HIGH: _ClassVar[CustomerValueBucket]
CUSTOMER_TYPE_UNSPECIFIED: CustomerType
NEW: CustomerType
RETURNING: CustomerType
REENGAGED: CustomerType
CUSTOMER_VALUE_BUCKET_UNSPECIFIED: CustomerValueBucket
LOW: CustomerValueBucket
MEDIUM: CustomerValueBucket
HIGH: CustomerValueBucket

class UserProperties(_message.Message):
    __slots__ = ('customer_type', 'customer_value_bucket')
    CUSTOMER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_VALUE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    customer_type: CustomerType
    customer_value_bucket: CustomerValueBucket

    def __init__(self, customer_type: _Optional[_Union[CustomerType, str]]=..., customer_value_bucket: _Optional[_Union[CustomerValueBucket, str]]=...) -> None:
        ...