from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetOnlineReturnPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateOnlineReturnPolicyRequest(_message.Message):
    __slots__ = ('parent', 'online_return_policy')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ONLINE_RETURN_POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    online_return_policy: OnlineReturnPolicy

    def __init__(self, parent: _Optional[str]=..., online_return_policy: _Optional[_Union[OnlineReturnPolicy, _Mapping]]=...) -> None:
        ...

class DeleteOnlineReturnPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListOnlineReturnPoliciesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListOnlineReturnPoliciesResponse(_message.Message):
    __slots__ = ('online_return_policies', 'next_page_token')
    ONLINE_RETURN_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    online_return_policies: _containers.RepeatedCompositeFieldContainer[OnlineReturnPolicy]
    next_page_token: str

    def __init__(self, online_return_policies: _Optional[_Iterable[_Union[OnlineReturnPolicy, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class OnlineReturnPolicy(_message.Message):
    __slots__ = ('name', 'return_policy_id', 'label', 'countries', 'policy', 'seasonal_overrides', 'restocking_fee', 'return_methods', 'item_conditions', 'return_shipping_fee', 'return_policy_uri', 'accept_defective_only', 'process_refund_days', 'accept_exchange', 'return_label_source')

    class ReturnMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RETURN_METHOD_UNSPECIFIED: _ClassVar[OnlineReturnPolicy.ReturnMethod]
        BY_MAIL: _ClassVar[OnlineReturnPolicy.ReturnMethod]
        IN_STORE: _ClassVar[OnlineReturnPolicy.ReturnMethod]
        AT_A_KIOSK: _ClassVar[OnlineReturnPolicy.ReturnMethod]
    RETURN_METHOD_UNSPECIFIED: OnlineReturnPolicy.ReturnMethod
    BY_MAIL: OnlineReturnPolicy.ReturnMethod
    IN_STORE: OnlineReturnPolicy.ReturnMethod
    AT_A_KIOSK: OnlineReturnPolicy.ReturnMethod

    class ItemCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ITEM_CONDITION_UNSPECIFIED: _ClassVar[OnlineReturnPolicy.ItemCondition]
        NEW: _ClassVar[OnlineReturnPolicy.ItemCondition]
        USED: _ClassVar[OnlineReturnPolicy.ItemCondition]
    ITEM_CONDITION_UNSPECIFIED: OnlineReturnPolicy.ItemCondition
    NEW: OnlineReturnPolicy.ItemCondition
    USED: OnlineReturnPolicy.ItemCondition

    class ReturnLabelSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RETURN_LABEL_SOURCE_UNSPECIFIED: _ClassVar[OnlineReturnPolicy.ReturnLabelSource]
        DOWNLOAD_AND_PRINT: _ClassVar[OnlineReturnPolicy.ReturnLabelSource]
        IN_THE_PACKAGE: _ClassVar[OnlineReturnPolicy.ReturnLabelSource]
        CUSTOMER_RESPONSIBILITY: _ClassVar[OnlineReturnPolicy.ReturnLabelSource]
    RETURN_LABEL_SOURCE_UNSPECIFIED: OnlineReturnPolicy.ReturnLabelSource
    DOWNLOAD_AND_PRINT: OnlineReturnPolicy.ReturnLabelSource
    IN_THE_PACKAGE: OnlineReturnPolicy.ReturnLabelSource
    CUSTOMER_RESPONSIBILITY: OnlineReturnPolicy.ReturnLabelSource

    class ReturnShippingFee(_message.Message):
        __slots__ = ('type', 'fixed_fee')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[OnlineReturnPolicy.ReturnShippingFee.Type]
            FIXED: _ClassVar[OnlineReturnPolicy.ReturnShippingFee.Type]
            CUSTOMER_PAYING_ACTUAL_FEE: _ClassVar[OnlineReturnPolicy.ReturnShippingFee.Type]
        TYPE_UNSPECIFIED: OnlineReturnPolicy.ReturnShippingFee.Type
        FIXED: OnlineReturnPolicy.ReturnShippingFee.Type
        CUSTOMER_PAYING_ACTUAL_FEE: OnlineReturnPolicy.ReturnShippingFee.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        FIXED_FEE_FIELD_NUMBER: _ClassVar[int]
        type: OnlineReturnPolicy.ReturnShippingFee.Type
        fixed_fee: _types_pb2.Price

        def __init__(self, type: _Optional[_Union[OnlineReturnPolicy.ReturnShippingFee.Type, str]]=..., fixed_fee: _Optional[_Union[_types_pb2.Price, _Mapping]]=...) -> None:
            ...

    class RestockingFee(_message.Message):
        __slots__ = ('fixed_fee', 'micro_percent')
        FIXED_FEE_FIELD_NUMBER: _ClassVar[int]
        MICRO_PERCENT_FIELD_NUMBER: _ClassVar[int]
        fixed_fee: _types_pb2.Price
        micro_percent: int

        def __init__(self, fixed_fee: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., micro_percent: _Optional[int]=...) -> None:
            ...

    class Policy(_message.Message):
        __slots__ = ('type', 'days')

        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNSPECIFIED: _ClassVar[OnlineReturnPolicy.Policy.Type]
            NUMBER_OF_DAYS_AFTER_DELIVERY: _ClassVar[OnlineReturnPolicy.Policy.Type]
            NO_RETURNS: _ClassVar[OnlineReturnPolicy.Policy.Type]
            LIFETIME_RETURNS: _ClassVar[OnlineReturnPolicy.Policy.Type]
        TYPE_UNSPECIFIED: OnlineReturnPolicy.Policy.Type
        NUMBER_OF_DAYS_AFTER_DELIVERY: OnlineReturnPolicy.Policy.Type
        NO_RETURNS: OnlineReturnPolicy.Policy.Type
        LIFETIME_RETURNS: OnlineReturnPolicy.Policy.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        DAYS_FIELD_NUMBER: _ClassVar[int]
        type: OnlineReturnPolicy.Policy.Type
        days: int

        def __init__(self, type: _Optional[_Union[OnlineReturnPolicy.Policy.Type, str]]=..., days: _Optional[int]=...) -> None:
            ...

    class SeasonalOverride(_message.Message):
        __slots__ = ('return_days', 'return_until_date', 'label', 'start_date', 'end_date')
        RETURN_DAYS_FIELD_NUMBER: _ClassVar[int]
        RETURN_UNTIL_DATE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        START_DATE_FIELD_NUMBER: _ClassVar[int]
        END_DATE_FIELD_NUMBER: _ClassVar[int]
        return_days: int
        return_until_date: _date_pb2.Date
        label: str
        start_date: _date_pb2.Date
        end_date: _date_pb2.Date

        def __init__(self, return_days: _Optional[int]=..., return_until_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., label: _Optional[str]=..., start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    RETURN_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    SEASONAL_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    RESTOCKING_FEE_FIELD_NUMBER: _ClassVar[int]
    RETURN_METHODS_FIELD_NUMBER: _ClassVar[int]
    ITEM_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    RETURN_SHIPPING_FEE_FIELD_NUMBER: _ClassVar[int]
    RETURN_POLICY_URI_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_DEFECTIVE_ONLY_FIELD_NUMBER: _ClassVar[int]
    PROCESS_REFUND_DAYS_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    RETURN_LABEL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    return_policy_id: str
    label: str
    countries: _containers.RepeatedScalarFieldContainer[str]
    policy: OnlineReturnPolicy.Policy
    seasonal_overrides: _containers.RepeatedCompositeFieldContainer[OnlineReturnPolicy.SeasonalOverride]
    restocking_fee: OnlineReturnPolicy.RestockingFee
    return_methods: _containers.RepeatedScalarFieldContainer[OnlineReturnPolicy.ReturnMethod]
    item_conditions: _containers.RepeatedScalarFieldContainer[OnlineReturnPolicy.ItemCondition]
    return_shipping_fee: OnlineReturnPolicy.ReturnShippingFee
    return_policy_uri: str
    accept_defective_only: bool
    process_refund_days: int
    accept_exchange: bool
    return_label_source: OnlineReturnPolicy.ReturnLabelSource

    def __init__(self, name: _Optional[str]=..., return_policy_id: _Optional[str]=..., label: _Optional[str]=..., countries: _Optional[_Iterable[str]]=..., policy: _Optional[_Union[OnlineReturnPolicy.Policy, _Mapping]]=..., seasonal_overrides: _Optional[_Iterable[_Union[OnlineReturnPolicy.SeasonalOverride, _Mapping]]]=..., restocking_fee: _Optional[_Union[OnlineReturnPolicy.RestockingFee, _Mapping]]=..., return_methods: _Optional[_Iterable[_Union[OnlineReturnPolicy.ReturnMethod, str]]]=..., item_conditions: _Optional[_Iterable[_Union[OnlineReturnPolicy.ItemCondition, str]]]=..., return_shipping_fee: _Optional[_Union[OnlineReturnPolicy.ReturnShippingFee, _Mapping]]=..., return_policy_uri: _Optional[str]=..., accept_defective_only: bool=..., process_refund_days: _Optional[int]=..., accept_exchange: bool=..., return_label_source: _Optional[_Union[OnlineReturnPolicy.ReturnLabelSource, str]]=...) -> None:
        ...