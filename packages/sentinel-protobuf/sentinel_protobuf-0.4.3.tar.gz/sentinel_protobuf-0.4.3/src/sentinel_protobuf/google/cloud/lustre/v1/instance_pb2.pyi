from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Instance(_message.Message):
    __slots__ = ('name', 'filesystem', 'capacity_gib', 'network', 'state', 'mount_point', 'create_time', 'update_time', 'description', 'labels', 'per_unit_storage_throughput', 'gke_support_enabled')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        ACTIVE: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        DELETING: _ClassVar[Instance.State]
        UPGRADING: _ClassVar[Instance.State]
        REPAIRING: _ClassVar[Instance.State]
        STOPPED: _ClassVar[Instance.State]
        UPDATING: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    ACTIVE: Instance.State
    CREATING: Instance.State
    DELETING: Instance.State
    UPGRADING: Instance.State
    REPAIRING: Instance.State
    STOPPED: Instance.State
    UPDATING: Instance.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_GIB_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PER_UNIT_STORAGE_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    GKE_SUPPORT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    filesystem: str
    capacity_gib: int
    network: str
    state: Instance.State
    mount_point: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    labels: _containers.ScalarMap[str, str]
    per_unit_storage_throughput: int
    gke_support_enabled: bool

    def __init__(self, name: _Optional[str]=..., filesystem: _Optional[str]=..., capacity_gib: _Optional[int]=..., network: _Optional[str]=..., state: _Optional[_Union[Instance.State, str]]=..., mount_point: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., per_unit_storage_throughput: _Optional[int]=..., gke_support_enabled: bool=...) -> None:
        ...

class ListInstancesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListInstancesResponse(_message.Message):
    __slots__ = ('instances', 'next_page_token', 'unreachable')
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, instances: _Optional[_Iterable[_Union[Instance, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ('parent', 'instance_id', 'instance', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: Instance
    request_id: str

    def __init__(self, parent: _Optional[str]=..., instance_id: _Optional[str]=..., instance: _Optional[_Union[Instance, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateInstanceRequest(_message.Message):
    __slots__ = ('update_mask', 'instance', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    instance: Instance
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., instance: _Optional[_Union[Instance, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...