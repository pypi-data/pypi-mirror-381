from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LicenseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LICENSE_TYPE_UNSPECIFIED: _ClassVar[LicenseType]
    LICENSE_TYPE_PER_MONTH_PER_USER: _ClassVar[LicenseType]
    LICENSE_TYPE_BRING_YOUR_OWN_LICENSE: _ClassVar[LicenseType]

class ActivationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTIVATION_STATE_UNSPECIFIED: _ClassVar[ActivationState]
    ACTIVATION_STATE_KEY_REQUESTED: _ClassVar[ActivationState]
    ACTIVATION_STATE_ACTIVATING: _ClassVar[ActivationState]
    ACTIVATION_STATE_ACTIVATED: _ClassVar[ActivationState]
    ACTIVATION_STATE_DEACTIVATING: _ClassVar[ActivationState]
    ACTIVATION_STATE_DEACTIVATED: _ClassVar[ActivationState]
    ACTIVATION_STATE_TERMINATED: _ClassVar[ActivationState]
LICENSE_TYPE_UNSPECIFIED: LicenseType
LICENSE_TYPE_PER_MONTH_PER_USER: LicenseType
LICENSE_TYPE_BRING_YOUR_OWN_LICENSE: LicenseType
ACTIVATION_STATE_UNSPECIFIED: ActivationState
ACTIVATION_STATE_KEY_REQUESTED: ActivationState
ACTIVATION_STATE_ACTIVATING: ActivationState
ACTIVATION_STATE_ACTIVATED: ActivationState
ACTIVATION_STATE_DEACTIVATING: ActivationState
ACTIVATION_STATE_DEACTIVATED: ActivationState
ACTIVATION_STATE_TERMINATED: ActivationState

class Configuration(_message.Message):
    __slots__ = ('name', 'display_name', 'product', 'license_type', 'current_billing_info', 'next_billing_info', 'create_time', 'update_time', 'labels', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Configuration.State]
        STATE_ACTIVE: _ClassVar[Configuration.State]
        STATE_SUSPENDED: _ClassVar[Configuration.State]
        STATE_DELETED: _ClassVar[Configuration.State]
    STATE_UNSPECIFIED: Configuration.State
    STATE_ACTIVE: Configuration.State
    STATE_SUSPENDED: Configuration.State
    STATE_DELETED: Configuration.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    NEXT_BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    product: str
    license_type: LicenseType
    current_billing_info: BillingInfo
    next_billing_info: BillingInfo
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: Configuration.State

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., product: _Optional[str]=..., license_type: _Optional[_Union[LicenseType, str]]=..., current_billing_info: _Optional[_Union[BillingInfo, _Mapping]]=..., next_billing_info: _Optional[_Union[BillingInfo, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[Configuration.State, str]]=...) -> None:
        ...

class BillingInfo(_message.Message):
    __slots__ = ('user_count_billing', 'start_time', 'end_time')
    USER_COUNT_BILLING_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    user_count_billing: UserCountBillingInfo
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, user_count_billing: _Optional[_Union[UserCountBillingInfo, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UserCountBillingInfo(_message.Message):
    __slots__ = ('user_count',)
    USER_COUNT_FIELD_NUMBER: _ClassVar[int]
    user_count: int

    def __init__(self, user_count: _Optional[int]=...) -> None:
        ...

class UserCountUsage(_message.Message):
    __slots__ = ('unique_user_count',)
    UNIQUE_USER_COUNT_FIELD_NUMBER: _ClassVar[int]
    unique_user_count: int

    def __init__(self, unique_user_count: _Optional[int]=...) -> None:
        ...

class Product(_message.Message):
    __slots__ = ('name', 'version', 'product_company', 'state', 'sku', 'description', 'display_name')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Product.State]
        STATE_PROVISIONING: _ClassVar[Product.State]
        STATE_RUNNING: _ClassVar[Product.State]
        STATE_TERMINATING: _ClassVar[Product.State]
        STATE_TERMINATED: _ClassVar[Product.State]
    STATE_UNSPECIFIED: Product.State
    STATE_PROVISIONING: Product.State
    STATE_RUNNING: Product.State
    STATE_TERMINATING: Product.State
    STATE_TERMINATED: Product.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_COMPANY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    product_company: str
    state: Product.State
    sku: str
    description: str
    display_name: str

    def __init__(self, name: _Optional[str]=..., version: _Optional[str]=..., product_company: _Optional[str]=..., state: _Optional[_Union[Product.State, str]]=..., sku: _Optional[str]=..., description: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class Instance(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'state', 'region', 'product_activation', 'license_version_id', 'compute_instance')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        PROVISIONING: _ClassVar[Instance.State]
        STAGING: _ClassVar[Instance.State]
        RUNNING: _ClassVar[Instance.State]
        STOPPING: _ClassVar[Instance.State]
        STOPPED: _ClassVar[Instance.State]
        TERMINATED: _ClassVar[Instance.State]
        REPAIRING: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    PROVISIONING: Instance.State
    STAGING: Instance.State
    RUNNING: Instance.State
    STOPPING: Instance.State
    STOPPED: Instance.State
    TERMINATED: Instance.State
    REPAIRING: Instance.State

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class ProductActivationEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ActivationState

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ActivationState, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    LICENSE_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    state: Instance.State
    region: str
    product_activation: _containers.ScalarMap[str, ActivationState]
    license_version_id: str
    compute_instance: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., state: _Optional[_Union[Instance.State, str]]=..., region: _Optional[str]=..., product_activation: _Optional[_Mapping[str, ActivationState]]=..., license_version_id: _Optional[str]=..., compute_instance: _Optional[str]=...) -> None:
        ...

class Usage(_message.Message):
    __slots__ = ('lima_instance', 'users')
    LIMA_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    lima_instance: str
    users: int

    def __init__(self, lima_instance: _Optional[str]=..., users: _Optional[int]=...) -> None:
        ...