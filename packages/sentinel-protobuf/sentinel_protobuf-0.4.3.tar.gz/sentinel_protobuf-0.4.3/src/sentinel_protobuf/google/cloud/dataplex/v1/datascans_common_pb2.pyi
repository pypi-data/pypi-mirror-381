from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataScanCatalogPublishingStatus(_message.Message):
    __slots__ = ('state',)

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[DataScanCatalogPublishingStatus.State]
        SUCCEEDED: _ClassVar[DataScanCatalogPublishingStatus.State]
        FAILED: _ClassVar[DataScanCatalogPublishingStatus.State]
    STATE_UNSPECIFIED: DataScanCatalogPublishingStatus.State
    SUCCEEDED: DataScanCatalogPublishingStatus.State
    FAILED: DataScanCatalogPublishingStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: DataScanCatalogPublishingStatus.State

    def __init__(self, state: _Optional[_Union[DataScanCatalogPublishingStatus.State, str]]=...) -> None:
        ...