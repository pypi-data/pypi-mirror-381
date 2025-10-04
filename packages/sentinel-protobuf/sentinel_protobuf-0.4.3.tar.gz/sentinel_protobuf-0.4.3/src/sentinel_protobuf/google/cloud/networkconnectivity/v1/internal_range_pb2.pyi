from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.networkconnectivity.v1 import common_pb2 as _common_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InternalRange(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'ip_cidr_range', 'network', 'usage', 'peering', 'prefix_length', 'target_cidr_range', 'users', 'overlaps', 'migration', 'immutable', 'allocation_options', 'exclude_cidr_ranges')

    class Usage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USAGE_UNSPECIFIED: _ClassVar[InternalRange.Usage]
        FOR_VPC: _ClassVar[InternalRange.Usage]
        EXTERNAL_TO_VPC: _ClassVar[InternalRange.Usage]
        FOR_MIGRATION: _ClassVar[InternalRange.Usage]
    USAGE_UNSPECIFIED: InternalRange.Usage
    FOR_VPC: InternalRange.Usage
    EXTERNAL_TO_VPC: InternalRange.Usage
    FOR_MIGRATION: InternalRange.Usage

    class Peering(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PEERING_UNSPECIFIED: _ClassVar[InternalRange.Peering]
        FOR_SELF: _ClassVar[InternalRange.Peering]
        FOR_PEER: _ClassVar[InternalRange.Peering]
        NOT_SHARED: _ClassVar[InternalRange.Peering]
    PEERING_UNSPECIFIED: InternalRange.Peering
    FOR_SELF: InternalRange.Peering
    FOR_PEER: InternalRange.Peering
    NOT_SHARED: InternalRange.Peering

    class Overlap(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OVERLAP_UNSPECIFIED: _ClassVar[InternalRange.Overlap]
        OVERLAP_ROUTE_RANGE: _ClassVar[InternalRange.Overlap]
        OVERLAP_EXISTING_SUBNET_RANGE: _ClassVar[InternalRange.Overlap]
    OVERLAP_UNSPECIFIED: InternalRange.Overlap
    OVERLAP_ROUTE_RANGE: InternalRange.Overlap
    OVERLAP_EXISTING_SUBNET_RANGE: InternalRange.Overlap

    class AllocationStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALLOCATION_STRATEGY_UNSPECIFIED: _ClassVar[InternalRange.AllocationStrategy]
        RANDOM: _ClassVar[InternalRange.AllocationStrategy]
        FIRST_AVAILABLE: _ClassVar[InternalRange.AllocationStrategy]
        RANDOM_FIRST_N_AVAILABLE: _ClassVar[InternalRange.AllocationStrategy]
        FIRST_SMALLEST_FITTING: _ClassVar[InternalRange.AllocationStrategy]
    ALLOCATION_STRATEGY_UNSPECIFIED: InternalRange.AllocationStrategy
    RANDOM: InternalRange.AllocationStrategy
    FIRST_AVAILABLE: InternalRange.AllocationStrategy
    RANDOM_FIRST_N_AVAILABLE: InternalRange.AllocationStrategy
    FIRST_SMALLEST_FITTING: InternalRange.AllocationStrategy

    class Migration(_message.Message):
        __slots__ = ('source', 'target')
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        TARGET_FIELD_NUMBER: _ClassVar[int]
        source: str
        target: str

        def __init__(self, source: _Optional[str]=..., target: _Optional[str]=...) -> None:
            ...

    class AllocationOptions(_message.Message):
        __slots__ = ('allocation_strategy', 'first_available_ranges_lookup_size')
        ALLOCATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
        FIRST_AVAILABLE_RANGES_LOOKUP_SIZE_FIELD_NUMBER: _ClassVar[int]
        allocation_strategy: InternalRange.AllocationStrategy
        first_available_ranges_lookup_size: int

        def __init__(self, allocation_strategy: _Optional[_Union[InternalRange.AllocationStrategy, str]]=..., first_available_ranges_lookup_size: _Optional[int]=...) -> None:
            ...

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
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IP_CIDR_RANGE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    PEERING_FIELD_NUMBER: _ClassVar[int]
    PREFIX_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TARGET_CIDR_RANGE_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    OVERLAPS_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_FIELD_NUMBER: _ClassVar[int]
    IMMUTABLE_FIELD_NUMBER: _ClassVar[int]
    ALLOCATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_CIDR_RANGES_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    ip_cidr_range: str
    network: str
    usage: InternalRange.Usage
    peering: InternalRange.Peering
    prefix_length: int
    target_cidr_range: _containers.RepeatedScalarFieldContainer[str]
    users: _containers.RepeatedScalarFieldContainer[str]
    overlaps: _containers.RepeatedScalarFieldContainer[InternalRange.Overlap]
    migration: InternalRange.Migration
    immutable: bool
    allocation_options: InternalRange.AllocationOptions
    exclude_cidr_ranges: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., ip_cidr_range: _Optional[str]=..., network: _Optional[str]=..., usage: _Optional[_Union[InternalRange.Usage, str]]=..., peering: _Optional[_Union[InternalRange.Peering, str]]=..., prefix_length: _Optional[int]=..., target_cidr_range: _Optional[_Iterable[str]]=..., users: _Optional[_Iterable[str]]=..., overlaps: _Optional[_Iterable[_Union[InternalRange.Overlap, str]]]=..., migration: _Optional[_Union[InternalRange.Migration, _Mapping]]=..., immutable: bool=..., allocation_options: _Optional[_Union[InternalRange.AllocationOptions, _Mapping]]=..., exclude_cidr_ranges: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListInternalRangesRequest(_message.Message):
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

class ListInternalRangesResponse(_message.Message):
    __slots__ = ('internal_ranges', 'next_page_token', 'unreachable')
    INTERNAL_RANGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    internal_ranges: _containers.RepeatedCompositeFieldContainer[InternalRange]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, internal_ranges: _Optional[_Iterable[_Union[InternalRange, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetInternalRangeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInternalRangeRequest(_message.Message):
    __slots__ = ('parent', 'internal_range_id', 'internal_range', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_RANGE_ID_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_RANGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    internal_range_id: str
    internal_range: InternalRange
    request_id: str

    def __init__(self, parent: _Optional[str]=..., internal_range_id: _Optional[str]=..., internal_range: _Optional[_Union[InternalRange, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateInternalRangeRequest(_message.Message):
    __slots__ = ('update_mask', 'internal_range', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_RANGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    internal_range: InternalRange
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., internal_range: _Optional[_Union[InternalRange, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteInternalRangeRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...