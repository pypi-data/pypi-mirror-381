from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class BuildTarget(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Model(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Milestone(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Build(_message.Message):
    __slots__ = ('name', 'milestone', 'build_version', 'status', 'type', 'branch', 'rw_firmware_version', 'labels')

    class BuildStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BUILD_STATUS_UNSPECIFIED: _ClassVar[Build.BuildStatus]
        PASS: _ClassVar[Build.BuildStatus]
        FAIL: _ClassVar[Build.BuildStatus]
        RUNNING: _ClassVar[Build.BuildStatus]
        ABORTED: _ClassVar[Build.BuildStatus]
    BUILD_STATUS_UNSPECIFIED: Build.BuildStatus
    PASS: Build.BuildStatus
    FAIL: Build.BuildStatus
    RUNNING: Build.BuildStatus
    ABORTED: Build.BuildStatus

    class BuildType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BUILD_TYPE_UNSPECIFIED: _ClassVar[Build.BuildType]
        RELEASE: _ClassVar[Build.BuildType]
        FIRMWARE: _ClassVar[Build.BuildType]
    BUILD_TYPE_UNSPECIFIED: Build.BuildType
    RELEASE: Build.BuildType
    FIRMWARE: Build.BuildType
    NAME_FIELD_NUMBER: _ClassVar[int]
    MILESTONE_FIELD_NUMBER: _ClassVar[int]
    BUILD_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    RW_FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    milestone: str
    build_version: str
    status: Build.BuildStatus
    type: Build.BuildType
    branch: str
    rw_firmware_version: str
    labels: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., milestone: _Optional[str]=..., build_version: _Optional[str]=..., status: _Optional[_Union[Build.BuildStatus, str]]=..., type: _Optional[_Union[Build.BuildType, str]]=..., branch: _Optional[str]=..., rw_firmware_version: _Optional[str]=..., labels: _Optional[_Iterable[str]]=...) -> None:
        ...

class BuildArtifact(_message.Message):
    __slots__ = ('name', 'build', 'bucket', 'path', 'object_count')
    NAME_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    build: str
    bucket: str
    path: str
    object_count: int

    def __init__(self, name: _Optional[str]=..., build: _Optional[str]=..., bucket: _Optional[str]=..., path: _Optional[str]=..., object_count: _Optional[int]=...) -> None:
        ...

class CloudBuild(_message.Message):
    __slots__ = ('id', 'status', 'create_time', 'start_time', 'finish_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CloudBuild.State]
        QUEUED: _ClassVar[CloudBuild.State]
        PENDING: _ClassVar[CloudBuild.State]
        WORKING: _ClassVar[CloudBuild.State]
        SUCCEEDED: _ClassVar[CloudBuild.State]
        FAILED: _ClassVar[CloudBuild.State]
        INTERNAL_ERROR: _ClassVar[CloudBuild.State]
        TIMEOUT: _ClassVar[CloudBuild.State]
        CANCELLED: _ClassVar[CloudBuild.State]
        EXPIRED: _ClassVar[CloudBuild.State]
    STATE_UNSPECIFIED: CloudBuild.State
    QUEUED: CloudBuild.State
    PENDING: CloudBuild.State
    WORKING: CloudBuild.State
    SUCCEEDED: CloudBuild.State
    FAILED: CloudBuild.State
    INTERNAL_ERROR: CloudBuild.State
    TIMEOUT: CloudBuild.State
    CANCELLED: CloudBuild.State
    EXPIRED: CloudBuild.State
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    FINISH_TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: CloudBuild.State
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    finish_time: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., status: _Optional[_Union[CloudBuild.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., finish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...