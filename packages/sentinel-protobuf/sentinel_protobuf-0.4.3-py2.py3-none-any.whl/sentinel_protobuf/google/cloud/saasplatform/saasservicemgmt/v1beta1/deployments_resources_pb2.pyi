from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.saasplatform.saasservicemgmt.v1beta1 import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Location(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class Saas(_message.Message):
    __slots__ = ('name', 'locations', 'labels', 'annotations', 'uid', 'etag', 'create_time', 'update_time')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    locations: _containers.RepeatedCompositeFieldContainer[Location]
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    uid: str
    etag: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., locations: _Optional[_Iterable[_Union[Location, _Mapping]]]=..., labels: _Optional[_Mapping[str, str]]=..., annotations: _Optional[_Mapping[str, str]]=..., uid: _Optional[str]=..., etag: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Tenant(_message.Message):
    __slots__ = ('name', 'consumer_resource', 'saas', 'labels', 'annotations', 'uid', 'etag', 'create_time', 'update_time')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SAAS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    consumer_resource: str
    saas: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    uid: str
    etag: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., consumer_resource: _Optional[str]=..., saas: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., annotations: _Optional[_Mapping[str, str]]=..., uid: _Optional[str]=..., etag: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UnitKind(_message.Message):
    __slots__ = ('name', 'default_release', 'dependencies', 'input_variable_mappings', 'output_variable_mappings', 'saas', 'labels', 'annotations', 'uid', 'etag', 'create_time', 'update_time')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_RELEASE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    INPUT_VARIABLE_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_VARIABLE_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    SAAS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    default_release: str
    dependencies: _containers.RepeatedCompositeFieldContainer[Dependency]
    input_variable_mappings: _containers.RepeatedCompositeFieldContainer[VariableMapping]
    output_variable_mappings: _containers.RepeatedCompositeFieldContainer[VariableMapping]
    saas: str
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    uid: str
    etag: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., default_release: _Optional[str]=..., dependencies: _Optional[_Iterable[_Union[Dependency, _Mapping]]]=..., input_variable_mappings: _Optional[_Iterable[_Union[VariableMapping, _Mapping]]]=..., output_variable_mappings: _Optional[_Iterable[_Union[VariableMapping, _Mapping]]]=..., saas: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., annotations: _Optional[_Mapping[str, str]]=..., uid: _Optional[str]=..., etag: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Unit(_message.Message):
    __slots__ = ('name', 'unit_kind', 'release', 'tenant', 'ongoing_operations', 'pending_operations', 'scheduled_operations', 'dependents', 'dependencies', 'input_variables', 'output_variables', 'maintenance', 'state', 'conditions', 'management_mode', 'system_managed_state', 'system_cleanup_at', 'labels', 'annotations', 'uid', 'etag', 'create_time', 'update_time')

    class UnitState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNIT_STATE_UNSPECIFIED: _ClassVar[Unit.UnitState]
        UNIT_STATE_NOT_PROVISIONED: _ClassVar[Unit.UnitState]
        UNIT_STATE_PROVISIONING: _ClassVar[Unit.UnitState]
        UNIT_STATE_UPDATING: _ClassVar[Unit.UnitState]
        UNIT_STATE_DEPROVISIONING: _ClassVar[Unit.UnitState]
        UNIT_STATE_READY: _ClassVar[Unit.UnitState]
        UNIT_STATE_ERROR: _ClassVar[Unit.UnitState]
    UNIT_STATE_UNSPECIFIED: Unit.UnitState
    UNIT_STATE_NOT_PROVISIONED: Unit.UnitState
    UNIT_STATE_PROVISIONING: Unit.UnitState
    UNIT_STATE_UPDATING: Unit.UnitState
    UNIT_STATE_DEPROVISIONING: Unit.UnitState
    UNIT_STATE_READY: Unit.UnitState
    UNIT_STATE_ERROR: Unit.UnitState

    class ManagementMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MANAGEMENT_MODE_UNSPECIFIED: _ClassVar[Unit.ManagementMode]
        MANAGEMENT_MODE_USER: _ClassVar[Unit.ManagementMode]
        MANAGEMENT_MODE_SYSTEM: _ClassVar[Unit.ManagementMode]
    MANAGEMENT_MODE_UNSPECIFIED: Unit.ManagementMode
    MANAGEMENT_MODE_USER: Unit.ManagementMode
    MANAGEMENT_MODE_SYSTEM: Unit.ManagementMode

    class SystemManagedState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SYSTEM_MANAGED_STATE_UNSPECIFIED: _ClassVar[Unit.SystemManagedState]
        SYSTEM_MANAGED_STATE_ACTIVE: _ClassVar[Unit.SystemManagedState]
        SYSTEM_MANAGED_STATE_INACTIVE: _ClassVar[Unit.SystemManagedState]
        SYSTEM_MANAGED_STATE_DECOMMISSIONED: _ClassVar[Unit.SystemManagedState]
    SYSTEM_MANAGED_STATE_UNSPECIFIED: Unit.SystemManagedState
    SYSTEM_MANAGED_STATE_ACTIVE: Unit.SystemManagedState
    SYSTEM_MANAGED_STATE_INACTIVE: Unit.SystemManagedState
    SYSTEM_MANAGED_STATE_DECOMMISSIONED: Unit.SystemManagedState

    class MaintenanceSettings(_message.Message):
        __slots__ = ('pinned_until_time',)
        PINNED_UNTIL_TIME_FIELD_NUMBER: _ClassVar[int]
        pinned_until_time: _timestamp_pb2.Timestamp

        def __init__(self, pinned_until_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_KIND_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    ONGOING_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PENDING_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    DEPENDENTS_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    INPUT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MANAGED_STATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_CLEANUP_AT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    unit_kind: str
    release: str
    tenant: str
    ongoing_operations: _containers.RepeatedScalarFieldContainer[str]
    pending_operations: _containers.RepeatedScalarFieldContainer[str]
    scheduled_operations: _containers.RepeatedScalarFieldContainer[str]
    dependents: _containers.RepeatedCompositeFieldContainer[UnitDependency]
    dependencies: _containers.RepeatedCompositeFieldContainer[UnitDependency]
    input_variables: _containers.RepeatedCompositeFieldContainer[_common_pb2.UnitVariable]
    output_variables: _containers.RepeatedCompositeFieldContainer[_common_pb2.UnitVariable]
    maintenance: Unit.MaintenanceSettings
    state: Unit.UnitState
    conditions: _containers.RepeatedCompositeFieldContainer[_common_pb2.UnitCondition]
    management_mode: Unit.ManagementMode
    system_managed_state: Unit.SystemManagedState
    system_cleanup_at: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    uid: str
    etag: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., unit_kind: _Optional[str]=..., release: _Optional[str]=..., tenant: _Optional[str]=..., ongoing_operations: _Optional[_Iterable[str]]=..., pending_operations: _Optional[_Iterable[str]]=..., scheduled_operations: _Optional[_Iterable[str]]=..., dependents: _Optional[_Iterable[_Union[UnitDependency, _Mapping]]]=..., dependencies: _Optional[_Iterable[_Union[UnitDependency, _Mapping]]]=..., input_variables: _Optional[_Iterable[_Union[_common_pb2.UnitVariable, _Mapping]]]=..., output_variables: _Optional[_Iterable[_Union[_common_pb2.UnitVariable, _Mapping]]]=..., maintenance: _Optional[_Union[Unit.MaintenanceSettings, _Mapping]]=..., state: _Optional[_Union[Unit.UnitState, str]]=..., conditions: _Optional[_Iterable[_Union[_common_pb2.UnitCondition, _Mapping]]]=..., management_mode: _Optional[_Union[Unit.ManagementMode, str]]=..., system_managed_state: _Optional[_Union[Unit.SystemManagedState, str]]=..., system_cleanup_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., annotations: _Optional[_Mapping[str, str]]=..., uid: _Optional[str]=..., etag: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UnitDependency(_message.Message):
    __slots__ = ('alias', 'unit')
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    alias: str
    unit: str

    def __init__(self, alias: _Optional[str]=..., unit: _Optional[str]=...) -> None:
        ...

class UnitOperation(_message.Message):
    __slots__ = ('provision', 'upgrade', 'deprovision', 'name', 'unit', 'parent_unit_operation', 'rollout', 'cancel', 'state', 'conditions', 'schedule', 'engine_state', 'error_category', 'labels', 'annotations', 'uid', 'etag', 'create_time', 'update_time')

    class UnitOperationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNIT_OPERATION_STATE_UNKNOWN: _ClassVar[UnitOperation.UnitOperationState]
        UNIT_OPERATION_STATE_PENDING: _ClassVar[UnitOperation.UnitOperationState]
        UNIT_OPERATION_STATE_SCHEDULED: _ClassVar[UnitOperation.UnitOperationState]
        UNIT_OPERATION_STATE_RUNNING: _ClassVar[UnitOperation.UnitOperationState]
        UNIT_OPERATION_STATE_SUCCEEDED: _ClassVar[UnitOperation.UnitOperationState]
        UNIT_OPERATION_STATE_FAILED: _ClassVar[UnitOperation.UnitOperationState]
        UNIT_OPERATION_STATE_CANCELLED: _ClassVar[UnitOperation.UnitOperationState]
    UNIT_OPERATION_STATE_UNKNOWN: UnitOperation.UnitOperationState
    UNIT_OPERATION_STATE_PENDING: UnitOperation.UnitOperationState
    UNIT_OPERATION_STATE_SCHEDULED: UnitOperation.UnitOperationState
    UNIT_OPERATION_STATE_RUNNING: UnitOperation.UnitOperationState
    UNIT_OPERATION_STATE_SUCCEEDED: UnitOperation.UnitOperationState
    UNIT_OPERATION_STATE_FAILED: UnitOperation.UnitOperationState
    UNIT_OPERATION_STATE_CANCELLED: UnitOperation.UnitOperationState

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PROVISION_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_FIELD_NUMBER: _ClassVar[int]
    DEPROVISION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    PARENT_UNIT_OPERATION_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ENGINE_STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    provision: Provision
    upgrade: Upgrade
    deprovision: Deprovision
    name: str
    unit: str
    parent_unit_operation: str
    rollout: str
    cancel: bool
    state: UnitOperation.UnitOperationState
    conditions: _containers.RepeatedCompositeFieldContainer[_common_pb2.UnitOperationCondition]
    schedule: Schedule
    engine_state: str
    error_category: _common_pb2.UnitOperationErrorCategory
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    uid: str
    etag: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, provision: _Optional[_Union[Provision, _Mapping]]=..., upgrade: _Optional[_Union[Upgrade, _Mapping]]=..., deprovision: _Optional[_Union[Deprovision, _Mapping]]=..., name: _Optional[str]=..., unit: _Optional[str]=..., parent_unit_operation: _Optional[str]=..., rollout: _Optional[str]=..., cancel: bool=..., state: _Optional[_Union[UnitOperation.UnitOperationState, str]]=..., conditions: _Optional[_Iterable[_Union[_common_pb2.UnitOperationCondition, _Mapping]]]=..., schedule: _Optional[_Union[Schedule, _Mapping]]=..., engine_state: _Optional[str]=..., error_category: _Optional[_Union[_common_pb2.UnitOperationErrorCategory, str]]=..., labels: _Optional[_Mapping[str, str]]=..., annotations: _Optional[_Mapping[str, str]]=..., uid: _Optional[str]=..., etag: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Provision(_message.Message):
    __slots__ = ('release', 'input_variables')
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    INPUT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    release: str
    input_variables: _containers.RepeatedCompositeFieldContainer[_common_pb2.UnitVariable]

    def __init__(self, release: _Optional[str]=..., input_variables: _Optional[_Iterable[_Union[_common_pb2.UnitVariable, _Mapping]]]=...) -> None:
        ...

class Deprovision(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class Upgrade(_message.Message):
    __slots__ = ('release', 'input_variables')
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    INPUT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    release: str
    input_variables: _containers.RepeatedCompositeFieldContainer[_common_pb2.UnitVariable]

    def __init__(self, release: _Optional[str]=..., input_variables: _Optional[_Iterable[_Union[_common_pb2.UnitVariable, _Mapping]]]=...) -> None:
        ...

class Schedule(_message.Message):
    __slots__ = ('start_time',)
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp

    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Release(_message.Message):
    __slots__ = ('name', 'unit_kind', 'blueprint', 'release_requirements', 'input_variables', 'output_variables', 'input_variable_defaults', 'labels', 'annotations', 'uid', 'etag', 'create_time', 'update_time')

    class ReleaseRequirements(_message.Message):
        __slots__ = ('upgradeable_from_releases',)
        UPGRADEABLE_FROM_RELEASES_FIELD_NUMBER: _ClassVar[int]
        upgradeable_from_releases: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, upgradeable_from_releases: _Optional[_Iterable[str]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UNIT_KIND_FIELD_NUMBER: _ClassVar[int]
    BLUEPRINT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    INPUT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    INPUT_VARIABLE_DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    unit_kind: str
    blueprint: _common_pb2.Blueprint
    release_requirements: Release.ReleaseRequirements
    input_variables: _containers.RepeatedCompositeFieldContainer[_common_pb2.UnitVariable]
    output_variables: _containers.RepeatedCompositeFieldContainer[_common_pb2.UnitVariable]
    input_variable_defaults: _containers.RepeatedCompositeFieldContainer[_common_pb2.UnitVariable]
    labels: _containers.ScalarMap[str, str]
    annotations: _containers.ScalarMap[str, str]
    uid: str
    etag: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., unit_kind: _Optional[str]=..., blueprint: _Optional[_Union[_common_pb2.Blueprint, _Mapping]]=..., release_requirements: _Optional[_Union[Release.ReleaseRequirements, _Mapping]]=..., input_variables: _Optional[_Iterable[_Union[_common_pb2.UnitVariable, _Mapping]]]=..., output_variables: _Optional[_Iterable[_Union[_common_pb2.UnitVariable, _Mapping]]]=..., input_variable_defaults: _Optional[_Iterable[_Union[_common_pb2.UnitVariable, _Mapping]]]=..., labels: _Optional[_Mapping[str, str]]=..., annotations: _Optional[_Mapping[str, str]]=..., uid: _Optional[str]=..., etag: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class VariableMapping(_message.Message):
    __slots__ = ('to', 'variable')
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    VARIABLE_FIELD_NUMBER: _ClassVar[int]
    to: ToMapping
    variable: str

    def __init__(self, to: _Optional[_Union[ToMapping, _Mapping]]=..., variable: _Optional[str]=..., **kwargs) -> None:
        ...

class FromMapping(_message.Message):
    __slots__ = ('dependency', 'output_variable')
    DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_VARIABLE_FIELD_NUMBER: _ClassVar[int]
    dependency: str
    output_variable: str

    def __init__(self, dependency: _Optional[str]=..., output_variable: _Optional[str]=...) -> None:
        ...

class ToMapping(_message.Message):
    __slots__ = ('dependency', 'input_variable', 'ignore_for_lookup')
    DEPENDENCY_FIELD_NUMBER: _ClassVar[int]
    INPUT_VARIABLE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_FOR_LOOKUP_FIELD_NUMBER: _ClassVar[int]
    dependency: str
    input_variable: str
    ignore_for_lookup: bool

    def __init__(self, dependency: _Optional[str]=..., input_variable: _Optional[str]=..., ignore_for_lookup: bool=...) -> None:
        ...

class Dependency(_message.Message):
    __slots__ = ('unit_kind', 'alias')
    UNIT_KIND_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    unit_kind: str
    alias: str

    def __init__(self, unit_kind: _Optional[str]=..., alias: _Optional[str]=...) -> None:
        ...