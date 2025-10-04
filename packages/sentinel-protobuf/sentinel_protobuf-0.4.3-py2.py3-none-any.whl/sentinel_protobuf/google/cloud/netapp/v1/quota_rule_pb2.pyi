from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListQuotaRulesRequest(_message.Message):
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

class ListQuotaRulesResponse(_message.Message):
    __slots__ = ('quota_rules', 'next_page_token', 'unreachable')
    QUOTA_RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    quota_rules: _containers.RepeatedCompositeFieldContainer[QuotaRule]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, quota_rules: _Optional[_Iterable[_Union[QuotaRule, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetQuotaRuleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateQuotaRuleRequest(_message.Message):
    __slots__ = ('parent', 'quota_rule', 'quota_rule_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUOTA_RULE_FIELD_NUMBER: _ClassVar[int]
    QUOTA_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    quota_rule: QuotaRule
    quota_rule_id: str

    def __init__(self, parent: _Optional[str]=..., quota_rule: _Optional[_Union[QuotaRule, _Mapping]]=..., quota_rule_id: _Optional[str]=...) -> None:
        ...

class UpdateQuotaRuleRequest(_message.Message):
    __slots__ = ('update_mask', 'quota_rule')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    QUOTA_RULE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    quota_rule: QuotaRule

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., quota_rule: _Optional[_Union[QuotaRule, _Mapping]]=...) -> None:
        ...

class DeleteQuotaRuleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class QuotaRule(_message.Message):
    __slots__ = ('name', 'target', 'type', 'disk_limit_mib', 'state', 'state_details', 'create_time', 'description', 'labels')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[QuotaRule.Type]
        INDIVIDUAL_USER_QUOTA: _ClassVar[QuotaRule.Type]
        INDIVIDUAL_GROUP_QUOTA: _ClassVar[QuotaRule.Type]
        DEFAULT_USER_QUOTA: _ClassVar[QuotaRule.Type]
        DEFAULT_GROUP_QUOTA: _ClassVar[QuotaRule.Type]
    TYPE_UNSPECIFIED: QuotaRule.Type
    INDIVIDUAL_USER_QUOTA: QuotaRule.Type
    INDIVIDUAL_GROUP_QUOTA: QuotaRule.Type
    DEFAULT_USER_QUOTA: QuotaRule.Type
    DEFAULT_GROUP_QUOTA: QuotaRule.Type

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[QuotaRule.State]
        CREATING: _ClassVar[QuotaRule.State]
        UPDATING: _ClassVar[QuotaRule.State]
        DELETING: _ClassVar[QuotaRule.State]
        READY: _ClassVar[QuotaRule.State]
        ERROR: _ClassVar[QuotaRule.State]
    STATE_UNSPECIFIED: QuotaRule.State
    CREATING: QuotaRule.State
    UPDATING: QuotaRule.State
    DELETING: QuotaRule.State
    READY: QuotaRule.State
    ERROR: QuotaRule.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_LIMIT_MIB_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    target: str
    type: QuotaRule.Type
    disk_limit_mib: int
    state: QuotaRule.State
    state_details: str
    create_time: _timestamp_pb2.Timestamp
    description: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., target: _Optional[str]=..., type: _Optional[_Union[QuotaRule.Type, str]]=..., disk_limit_mib: _Optional[int]=..., state: _Optional[_Union[QuotaRule.State, str]]=..., state_details: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...