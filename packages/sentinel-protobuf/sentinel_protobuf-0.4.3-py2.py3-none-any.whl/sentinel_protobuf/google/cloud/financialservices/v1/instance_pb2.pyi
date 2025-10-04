from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.financialservices.v1 import bigquery_destination_pb2 as _bigquery_destination_pb2
from google.cloud.financialservices.v1 import line_of_business_pb2 as _line_of_business_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Instance(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'state', 'labels', 'kms_key')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        ACTIVE: _ClassVar[Instance.State]
        UPDATING: _ClassVar[Instance.State]
        DELETING: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    CREATING: Instance.State
    ACTIVE: Instance.State
    UPDATING: Instance.State
    DELETING: Instance.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    state: Instance.State
    labels: _containers.ScalarMap[str, str]
    kms_key: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[Instance.State, str]]=..., labels: _Optional[_Mapping[str, str]]=..., kms_key: _Optional[str]=...) -> None:
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

class ImportRegisteredPartiesRequest(_message.Message):
    __slots__ = ('name', 'party_tables', 'mode', 'validate_only', 'line_of_business')

    class UpdateMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UPDATE_MODE_UNSPECIFIED: _ClassVar[ImportRegisteredPartiesRequest.UpdateMode]
        REPLACE: _ClassVar[ImportRegisteredPartiesRequest.UpdateMode]
        APPEND: _ClassVar[ImportRegisteredPartiesRequest.UpdateMode]
    UPDATE_MODE_UNSPECIFIED: ImportRegisteredPartiesRequest.UpdateMode
    REPLACE: ImportRegisteredPartiesRequest.UpdateMode
    APPEND: ImportRegisteredPartiesRequest.UpdateMode
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTY_TABLES_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    LINE_OF_BUSINESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    party_tables: _containers.RepeatedScalarFieldContainer[str]
    mode: ImportRegisteredPartiesRequest.UpdateMode
    validate_only: bool
    line_of_business: _line_of_business_pb2.LineOfBusiness

    def __init__(self, name: _Optional[str]=..., party_tables: _Optional[_Iterable[str]]=..., mode: _Optional[_Union[ImportRegisteredPartiesRequest.UpdateMode, str]]=..., validate_only: bool=..., line_of_business: _Optional[_Union[_line_of_business_pb2.LineOfBusiness, str]]=...) -> None:
        ...

class ImportRegisteredPartiesResponse(_message.Message):
    __slots__ = ('parties_added', 'parties_removed', 'parties_total', 'parties_failed_to_remove', 'parties_uptiered', 'parties_downtiered', 'parties_failed_to_downtier')
    PARTIES_ADDED_FIELD_NUMBER: _ClassVar[int]
    PARTIES_REMOVED_FIELD_NUMBER: _ClassVar[int]
    PARTIES_TOTAL_FIELD_NUMBER: _ClassVar[int]
    PARTIES_FAILED_TO_REMOVE_FIELD_NUMBER: _ClassVar[int]
    PARTIES_UPTIERED_FIELD_NUMBER: _ClassVar[int]
    PARTIES_DOWNTIERED_FIELD_NUMBER: _ClassVar[int]
    PARTIES_FAILED_TO_DOWNTIER_FIELD_NUMBER: _ClassVar[int]
    parties_added: int
    parties_removed: int
    parties_total: int
    parties_failed_to_remove: int
    parties_uptiered: int
    parties_downtiered: int
    parties_failed_to_downtier: int

    def __init__(self, parties_added: _Optional[int]=..., parties_removed: _Optional[int]=..., parties_total: _Optional[int]=..., parties_failed_to_remove: _Optional[int]=..., parties_uptiered: _Optional[int]=..., parties_downtiered: _Optional[int]=..., parties_failed_to_downtier: _Optional[int]=...) -> None:
        ...

class ExportRegisteredPartiesRequest(_message.Message):
    __slots__ = ('name', 'dataset', 'line_of_business')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    LINE_OF_BUSINESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    dataset: _bigquery_destination_pb2.BigQueryDestination
    line_of_business: _line_of_business_pb2.LineOfBusiness

    def __init__(self, name: _Optional[str]=..., dataset: _Optional[_Union[_bigquery_destination_pb2.BigQueryDestination, _Mapping]]=..., line_of_business: _Optional[_Union[_line_of_business_pb2.LineOfBusiness, str]]=...) -> None:
        ...

class ExportRegisteredPartiesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...