from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
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

class DeletionPropagationPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DELETION_PROPAGATION_POLICY_UNSPECIFIED: _ClassVar[DeletionPropagationPolicy]
    FOREGROUND: _ClassVar[DeletionPropagationPolicy]
    ORPHAN: _ClassVar[DeletionPropagationPolicy]
DELETION_PROPAGATION_POLICY_UNSPECIFIED: DeletionPropagationPolicy
FOREGROUND: DeletionPropagationPolicy
ORPHAN: DeletionPropagationPolicy

class ResourceBundle(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description')

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
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=...) -> None:
        ...

class ListResourceBundlesRequest(_message.Message):
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

class ListResourceBundlesResponse(_message.Message):
    __slots__ = ('resource_bundles', 'next_page_token', 'unreachable')
    RESOURCE_BUNDLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    resource_bundles: _containers.RepeatedCompositeFieldContainer[ResourceBundle]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, resource_bundles: _Optional[_Iterable[_Union[ResourceBundle, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetResourceBundleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateResourceBundleRequest(_message.Message):
    __slots__ = ('parent', 'resource_bundle_id', 'resource_bundle', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    resource_bundle_id: str
    resource_bundle: ResourceBundle
    request_id: str

    def __init__(self, parent: _Optional[str]=..., resource_bundle_id: _Optional[str]=..., resource_bundle: _Optional[_Union[ResourceBundle, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateResourceBundleRequest(_message.Message):
    __slots__ = ('update_mask', 'resource_bundle', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    resource_bundle: ResourceBundle
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., resource_bundle: _Optional[_Union[ResourceBundle, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteResourceBundleRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., force: bool=...) -> None:
        ...

class FleetPackage(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'resource_bundle_selector', 'target', 'rollout_strategy', 'variant_selector', 'info', 'deletion_propagation_policy', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[FleetPackage.State]
        ACTIVE: _ClassVar[FleetPackage.State]
        SUSPENDED: _ClassVar[FleetPackage.State]
    STATE_UNSPECIFIED: FleetPackage.State
    ACTIVE: FleetPackage.State
    SUSPENDED: FleetPackage.State

    class ResourceBundleSelector(_message.Message):
        __slots__ = ('resource_bundle', 'cloud_build_repository')
        RESOURCE_BUNDLE_FIELD_NUMBER: _ClassVar[int]
        CLOUD_BUILD_REPOSITORY_FIELD_NUMBER: _ClassVar[int]
        resource_bundle: FleetPackage.ResourceBundleTag
        cloud_build_repository: FleetPackage.CloudBuildRepository

        def __init__(self, resource_bundle: _Optional[_Union[FleetPackage.ResourceBundleTag, _Mapping]]=..., cloud_build_repository: _Optional[_Union[FleetPackage.CloudBuildRepository, _Mapping]]=...) -> None:
            ...

    class ResourceBundleTag(_message.Message):
        __slots__ = ('name', 'tag')
        NAME_FIELD_NUMBER: _ClassVar[int]
        TAG_FIELD_NUMBER: _ClassVar[int]
        name: str
        tag: str

        def __init__(self, name: _Optional[str]=..., tag: _Optional[str]=...) -> None:
            ...

    class CloudBuildRepository(_message.Message):
        __slots__ = ('variants_pattern', 'name', 'path', 'tag', 'service_account')
        VARIANTS_PATTERN_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        TAG_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        variants_pattern: str
        name: str
        path: str
        tag: str
        service_account: str

        def __init__(self, variants_pattern: _Optional[str]=..., name: _Optional[str]=..., path: _Optional[str]=..., tag: _Optional[str]=..., service_account: _Optional[str]=...) -> None:
            ...

    class Target(_message.Message):
        __slots__ = ('fleet',)
        FLEET_FIELD_NUMBER: _ClassVar[int]
        fleet: Fleet

        def __init__(self, fleet: _Optional[_Union[Fleet, _Mapping]]=...) -> None:
            ...

    class VariantSelector(_message.Message):
        __slots__ = ('variant_name_template',)
        VARIANT_NAME_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        variant_name_template: str

        def __init__(self, variant_name_template: _Optional[str]=...) -> None:
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
    RESOURCE_BUNDLE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    VARIANT_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROPAGATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    resource_bundle_selector: FleetPackage.ResourceBundleSelector
    target: FleetPackage.Target
    rollout_strategy: RolloutStrategy
    variant_selector: FleetPackage.VariantSelector
    info: FleetPackageInfo
    deletion_propagation_policy: DeletionPropagationPolicy
    state: FleetPackage.State

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., resource_bundle_selector: _Optional[_Union[FleetPackage.ResourceBundleSelector, _Mapping]]=..., target: _Optional[_Union[FleetPackage.Target, _Mapping]]=..., rollout_strategy: _Optional[_Union[RolloutStrategy, _Mapping]]=..., variant_selector: _Optional[_Union[FleetPackage.VariantSelector, _Mapping]]=..., info: _Optional[_Union[FleetPackageInfo, _Mapping]]=..., deletion_propagation_policy: _Optional[_Union[DeletionPropagationPolicy, str]]=..., state: _Optional[_Union[FleetPackage.State, str]]=...) -> None:
        ...

class FleetPackageInfo(_message.Message):
    __slots__ = ('active_rollout', 'last_completed_rollout', 'state', 'errors')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[FleetPackageInfo.State]
        ACTIVE: _ClassVar[FleetPackageInfo.State]
        SUSPENDED: _ClassVar[FleetPackageInfo.State]
        FAILED: _ClassVar[FleetPackageInfo.State]
        DELETING: _ClassVar[FleetPackageInfo.State]
    STATE_UNSPECIFIED: FleetPackageInfo.State
    ACTIVE: FleetPackageInfo.State
    SUSPENDED: FleetPackageInfo.State
    FAILED: FleetPackageInfo.State
    DELETING: FleetPackageInfo.State
    ACTIVE_ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    LAST_COMPLETED_ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    active_rollout: str
    last_completed_rollout: str
    state: FleetPackageInfo.State
    errors: _containers.RepeatedCompositeFieldContainer[FleetPackageError]

    def __init__(self, active_rollout: _Optional[str]=..., last_completed_rollout: _Optional[str]=..., state: _Optional[_Union[FleetPackageInfo.State, str]]=..., errors: _Optional[_Iterable[_Union[FleetPackageError, _Mapping]]]=...) -> None:
        ...

class FleetPackageError(_message.Message):
    __slots__ = ('error_message',)
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    error_message: str

    def __init__(self, error_message: _Optional[str]=...) -> None:
        ...

class ClusterInfo(_message.Message):
    __slots__ = ('membership', 'desired', 'initial', 'current', 'state', 'messages', 'start_time', 'end_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ClusterInfo.State]
        WAITING: _ClassVar[ClusterInfo.State]
        IN_PROGRESS: _ClassVar[ClusterInfo.State]
        STALLED: _ClassVar[ClusterInfo.State]
        COMPLETED: _ClassVar[ClusterInfo.State]
        ABORTED: _ClassVar[ClusterInfo.State]
        CANCELLED: _ClassVar[ClusterInfo.State]
        ERROR: _ClassVar[ClusterInfo.State]
        UNCHANGED: _ClassVar[ClusterInfo.State]
        SKIPPED: _ClassVar[ClusterInfo.State]
    STATE_UNSPECIFIED: ClusterInfo.State
    WAITING: ClusterInfo.State
    IN_PROGRESS: ClusterInfo.State
    STALLED: ClusterInfo.State
    COMPLETED: ClusterInfo.State
    ABORTED: ClusterInfo.State
    CANCELLED: ClusterInfo.State
    ERROR: ClusterInfo.State
    UNCHANGED: ClusterInfo.State
    SKIPPED: ClusterInfo.State
    MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FIELD_NUMBER: _ClassVar[int]
    INITIAL_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    membership: str
    desired: ResourceBundleDeploymentInfo
    initial: ResourceBundleDeploymentInfo
    current: ResourceBundleDeploymentInfo
    state: ClusterInfo.State
    messages: _containers.RepeatedScalarFieldContainer[str]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, membership: _Optional[str]=..., desired: _Optional[_Union[ResourceBundleDeploymentInfo, _Mapping]]=..., initial: _Optional[_Union[ResourceBundleDeploymentInfo, _Mapping]]=..., current: _Optional[_Union[ResourceBundleDeploymentInfo, _Mapping]]=..., state: _Optional[_Union[ClusterInfo.State, str]]=..., messages: _Optional[_Iterable[str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ResourceBundleDeploymentInfo(_message.Message):
    __slots__ = ('release', 'version', 'variant', 'sync_state', 'messages')

    class SyncState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SYNC_STATE_UNSPECIFIED: _ClassVar[ResourceBundleDeploymentInfo.SyncState]
        RECONCILING: _ClassVar[ResourceBundleDeploymentInfo.SyncState]
        STALLED: _ClassVar[ResourceBundleDeploymentInfo.SyncState]
        SYNCED: _ClassVar[ResourceBundleDeploymentInfo.SyncState]
        PENDING: _ClassVar[ResourceBundleDeploymentInfo.SyncState]
        ERROR: _ClassVar[ResourceBundleDeploymentInfo.SyncState]
        DELETION_PENDING: _ClassVar[ResourceBundleDeploymentInfo.SyncState]
        DELETING: _ClassVar[ResourceBundleDeploymentInfo.SyncState]
        DELETED: _ClassVar[ResourceBundleDeploymentInfo.SyncState]
    SYNC_STATE_UNSPECIFIED: ResourceBundleDeploymentInfo.SyncState
    RECONCILING: ResourceBundleDeploymentInfo.SyncState
    STALLED: ResourceBundleDeploymentInfo.SyncState
    SYNCED: ResourceBundleDeploymentInfo.SyncState
    PENDING: ResourceBundleDeploymentInfo.SyncState
    ERROR: ResourceBundleDeploymentInfo.SyncState
    DELETION_PENDING: ResourceBundleDeploymentInfo.SyncState
    DELETING: ResourceBundleDeploymentInfo.SyncState
    DELETED: ResourceBundleDeploymentInfo.SyncState
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    SYNC_STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    release: str
    version: str
    variant: str
    sync_state: ResourceBundleDeploymentInfo.SyncState
    messages: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, release: _Optional[str]=..., version: _Optional[str]=..., variant: _Optional[str]=..., sync_state: _Optional[_Union[ResourceBundleDeploymentInfo.SyncState, str]]=..., messages: _Optional[_Iterable[str]]=...) -> None:
        ...

class Fleet(_message.Message):
    __slots__ = ('project', 'selector')

    class LabelSelector(_message.Message):
        __slots__ = ('match_labels',)

        class MatchLabelsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        MATCH_LABELS_FIELD_NUMBER: _ClassVar[int]
        match_labels: _containers.ScalarMap[str, str]

        def __init__(self, match_labels: _Optional[_Mapping[str, str]]=...) -> None:
            ...
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    project: str
    selector: Fleet.LabelSelector

    def __init__(self, project: _Optional[str]=..., selector: _Optional[_Union[Fleet.LabelSelector, _Mapping]]=...) -> None:
        ...

class AllAtOnceStrategy(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RollingStrategy(_message.Message):
    __slots__ = ('max_concurrent',)
    MAX_CONCURRENT_FIELD_NUMBER: _ClassVar[int]
    max_concurrent: int

    def __init__(self, max_concurrent: _Optional[int]=...) -> None:
        ...

class RolloutStrategy(_message.Message):
    __slots__ = ('all_at_once', 'rolling')
    ALL_AT_ONCE_FIELD_NUMBER: _ClassVar[int]
    ROLLING_FIELD_NUMBER: _ClassVar[int]
    all_at_once: AllAtOnceStrategy
    rolling: RollingStrategy

    def __init__(self, all_at_once: _Optional[_Union[AllAtOnceStrategy, _Mapping]]=..., rolling: _Optional[_Union[RollingStrategy, _Mapping]]=...) -> None:
        ...

class RolloutStrategyInfo(_message.Message):
    __slots__ = ('all_at_once_strategy_info', 'rolling_strategy_info')
    ALL_AT_ONCE_STRATEGY_INFO_FIELD_NUMBER: _ClassVar[int]
    ROLLING_STRATEGY_INFO_FIELD_NUMBER: _ClassVar[int]
    all_at_once_strategy_info: AllAtOnceStrategyInfo
    rolling_strategy_info: RollingStrategyInfo

    def __init__(self, all_at_once_strategy_info: _Optional[_Union[AllAtOnceStrategyInfo, _Mapping]]=..., rolling_strategy_info: _Optional[_Union[RollingStrategyInfo, _Mapping]]=...) -> None:
        ...

class AllAtOnceStrategyInfo(_message.Message):
    __slots__ = ('clusters',)
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[ClusterInfo]

    def __init__(self, clusters: _Optional[_Iterable[_Union[ClusterInfo, _Mapping]]]=...) -> None:
        ...

class RollingStrategyInfo(_message.Message):
    __slots__ = ('clusters',)
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[ClusterInfo]

    def __init__(self, clusters: _Optional[_Iterable[_Union[ClusterInfo, _Mapping]]]=...) -> None:
        ...

class ListFleetPackagesRequest(_message.Message):
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

class ListFleetPackagesResponse(_message.Message):
    __slots__ = ('fleet_packages', 'next_page_token', 'unreachable')
    FLEET_PACKAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    fleet_packages: _containers.RepeatedCompositeFieldContainer[FleetPackage]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, fleet_packages: _Optional[_Iterable[_Union[FleetPackage, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetFleetPackageRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateFleetPackageRequest(_message.Message):
    __slots__ = ('parent', 'fleet_package_id', 'fleet_package', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FLEET_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    FLEET_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    fleet_package_id: str
    fleet_package: FleetPackage
    request_id: str

    def __init__(self, parent: _Optional[str]=..., fleet_package_id: _Optional[str]=..., fleet_package: _Optional[_Union[FleetPackage, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateFleetPackageRequest(_message.Message):
    __slots__ = ('update_mask', 'fleet_package', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    FLEET_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    fleet_package: FleetPackage
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., fleet_package: _Optional[_Union[FleetPackage, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteFleetPackageRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'force', 'allow_missing')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool
    allow_missing: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., force: bool=..., allow_missing: bool=...) -> None:
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

class Release(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'lifecycle', 'version', 'publish_time', 'info')

    class Lifecycle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LIFECYCLE_UNSPECIFIED: _ClassVar[Release.Lifecycle]
        DRAFT: _ClassVar[Release.Lifecycle]
        PUBLISHED: _ClassVar[Release.Lifecycle]
    LIFECYCLE_UNSPECIFIED: Release.Lifecycle
    DRAFT: Release.Lifecycle
    PUBLISHED: Release.Lifecycle

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
    LIFECYCLE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_TIME_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    lifecycle: Release.Lifecycle
    version: str
    publish_time: _timestamp_pb2.Timestamp
    info: ReleaseInfo

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., lifecycle: _Optional[_Union[Release.Lifecycle, str]]=..., version: _Optional[str]=..., publish_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., info: _Optional[_Union[ReleaseInfo, _Mapping]]=...) -> None:
        ...

class Variant(_message.Message):
    __slots__ = ('labels', 'resources', 'name', 'create_time', 'update_time')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.ScalarMap[str, str]
    resources: _containers.RepeatedScalarFieldContainer[str]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, labels: _Optional[_Mapping[str, str]]=..., resources: _Optional[_Iterable[str]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListVariantsRequest(_message.Message):
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

class ListVariantsResponse(_message.Message):
    __slots__ = ('variants', 'next_page_token', 'unreachable')
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    variants: _containers.RepeatedCompositeFieldContainer[Variant]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, variants: _Optional[_Iterable[_Union[Variant, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetVariantRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateVariantRequest(_message.Message):
    __slots__ = ('parent', 'variant_id', 'variant', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    variant_id: str
    variant: Variant
    request_id: str

    def __init__(self, parent: _Optional[str]=..., variant_id: _Optional[str]=..., variant: _Optional[_Union[Variant, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateVariantRequest(_message.Message):
    __slots__ = ('update_mask', 'variant', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    variant: Variant
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., variant: _Optional[_Union[Variant, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteVariantRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ReleaseInfo(_message.Message):
    __slots__ = ('oci_image_path', 'variant_oci_image_paths')

    class VariantOciImagePathsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    OCI_IMAGE_PATH_FIELD_NUMBER: _ClassVar[int]
    VARIANT_OCI_IMAGE_PATHS_FIELD_NUMBER: _ClassVar[int]
    oci_image_path: str
    variant_oci_image_paths: _containers.ScalarMap[str, str]

    def __init__(self, oci_image_path: _Optional[str]=..., variant_oci_image_paths: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ListReleasesRequest(_message.Message):
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

class ListReleasesResponse(_message.Message):
    __slots__ = ('releases', 'next_page_token', 'unreachable')
    RELEASES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    releases: _containers.RepeatedCompositeFieldContainer[Release]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, releases: _Optional[_Iterable[_Union[Release, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetReleaseRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateReleaseRequest(_message.Message):
    __slots__ = ('parent', 'release_id', 'release', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    release_id: str
    release: Release
    request_id: str

    def __init__(self, parent: _Optional[str]=..., release_id: _Optional[str]=..., release: _Optional[_Union[Release, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateReleaseRequest(_message.Message):
    __slots__ = ('update_mask', 'release', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    release: Release
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., release: _Optional[_Union[Release, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteReleaseRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    force: bool

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListRolloutsRequest(_message.Message):
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

class ListRolloutsResponse(_message.Message):
    __slots__ = ('rollouts', 'next_page_token', 'unreachable')
    ROLLOUTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    rollouts: _containers.RepeatedCompositeFieldContainer[Rollout]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, rollouts: _Optional[_Iterable[_Union[Rollout, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetRolloutRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RolloutInfo(_message.Message):
    __slots__ = ('state', 'start_time', 'end_time', 'message', 'rollout_strategy_info')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[RolloutInfo.State]
        COMPLETED: _ClassVar[RolloutInfo.State]
        SUSPENDED: _ClassVar[RolloutInfo.State]
        ABORTED: _ClassVar[RolloutInfo.State]
        IN_PROGRESS: _ClassVar[RolloutInfo.State]
        STALLED: _ClassVar[RolloutInfo.State]
        CANCELLED: _ClassVar[RolloutInfo.State]
        ABORTING: _ClassVar[RolloutInfo.State]
    STATE_UNSPECIFIED: RolloutInfo.State
    COMPLETED: RolloutInfo.State
    SUSPENDED: RolloutInfo.State
    ABORTED: RolloutInfo.State
    IN_PROGRESS: RolloutInfo.State
    STALLED: RolloutInfo.State
    CANCELLED: RolloutInfo.State
    ABORTING: RolloutInfo.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_STRATEGY_INFO_FIELD_NUMBER: _ClassVar[int]
    state: RolloutInfo.State
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    message: str
    rollout_strategy_info: RolloutStrategyInfo

    def __init__(self, state: _Optional[_Union[RolloutInfo.State, str]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., message: _Optional[str]=..., rollout_strategy_info: _Optional[_Union[RolloutStrategyInfo, _Mapping]]=...) -> None:
        ...

class Rollout(_message.Message):
    __slots__ = ('name', 'release', 'rollout_strategy', 'info', 'deletion_propagation_policy', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROPAGATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    release: str
    rollout_strategy: RolloutStrategy
    info: RolloutInfo
    deletion_propagation_policy: DeletionPropagationPolicy
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., release: _Optional[str]=..., rollout_strategy: _Optional[_Union[RolloutStrategy, _Mapping]]=..., info: _Optional[_Union[RolloutInfo, _Mapping]]=..., deletion_propagation_policy: _Optional[_Union[DeletionPropagationPolicy, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class SuspendRolloutRequest(_message.Message):
    __slots__ = ('name', 'reason')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    reason: str

    def __init__(self, name: _Optional[str]=..., reason: _Optional[str]=...) -> None:
        ...

class ResumeRolloutRequest(_message.Message):
    __slots__ = ('name', 'reason')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    reason: str

    def __init__(self, name: _Optional[str]=..., reason: _Optional[str]=...) -> None:
        ...

class AbortRolloutRequest(_message.Message):
    __slots__ = ('name', 'reason')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    reason: str

    def __init__(self, name: _Optional[str]=..., reason: _Optional[str]=...) -> None:
        ...