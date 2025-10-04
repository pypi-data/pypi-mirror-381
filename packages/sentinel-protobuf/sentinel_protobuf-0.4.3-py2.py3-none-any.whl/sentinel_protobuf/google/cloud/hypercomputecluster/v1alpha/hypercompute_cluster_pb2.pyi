from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.hypercomputecluster.v1alpha import operation_metadata_pb2 as _operation_metadata_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Cluster(_message.Message):
    __slots__ = ('name', 'description', 'labels', 'create_time', 'update_time', 'reconciling', 'network_resources', 'storage_resources', 'compute_resources', 'orchestrator', 'networks', 'storages', 'compute')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class NetworkResourcesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: NetworkResource

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[NetworkResource, _Mapping]]=...) -> None:
            ...

    class StorageResourcesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: StorageResource

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[StorageResource, _Mapping]]=...) -> None:
            ...

    class ComputeResourcesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ComputeResource

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ComputeResource, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    NETWORK_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    STORAGE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ORCHESTRATOR_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    STORAGES_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    reconciling: bool
    network_resources: _containers.MessageMap[str, NetworkResource]
    storage_resources: _containers.MessageMap[str, StorageResource]
    compute_resources: _containers.MessageMap[str, ComputeResource]
    orchestrator: Orchestrator
    networks: _containers.RepeatedCompositeFieldContainer[Network]
    storages: _containers.RepeatedCompositeFieldContainer[Storage]
    compute: Compute

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., reconciling: bool=..., network_resources: _Optional[_Mapping[str, NetworkResource]]=..., storage_resources: _Optional[_Mapping[str, StorageResource]]=..., compute_resources: _Optional[_Mapping[str, ComputeResource]]=..., orchestrator: _Optional[_Union[Orchestrator, _Mapping]]=..., networks: _Optional[_Iterable[_Union[Network, _Mapping]]]=..., storages: _Optional[_Iterable[_Union[Storage, _Mapping]]]=..., compute: _Optional[_Union[Compute, _Mapping]]=...) -> None:
        ...

class ListClustersRequest(_message.Message):
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

class ListClustersResponse(_message.Message):
    __slots__ = ('clusters', 'next_page_token', 'unreachable')
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    clusters: _containers.RepeatedCompositeFieldContainer[Cluster]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, clusters: _Optional[_Iterable[_Union[Cluster, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetClusterRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateClusterRequest(_message.Message):
    __slots__ = ('parent', 'cluster_id', 'cluster', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cluster_id: str
    cluster: Cluster
    request_id: str

    def __init__(self, parent: _Optional[str]=..., cluster_id: _Optional[str]=..., cluster: _Optional[_Union[Cluster, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateClusterRequest(_message.Message):
    __slots__ = ('cluster', 'update_mask', 'request_id')
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    cluster: Cluster
    update_mask: _field_mask_pb2.FieldMask
    request_id: str

    def __init__(self, cluster: _Optional[_Union[Cluster, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteClusterRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class NetworkResource(_message.Message):
    __slots__ = ('network', 'compute_network', 'config')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    network: NetworkReference
    compute_network: ComputeNetworkReference
    config: NetworkResourceConfig

    def __init__(self, network: _Optional[_Union[NetworkReference, _Mapping]]=..., compute_network: _Optional[_Union[ComputeNetworkReference, _Mapping]]=..., config: _Optional[_Union[NetworkResourceConfig, _Mapping]]=...) -> None:
        ...

class NetworkReference(_message.Message):
    __slots__ = ('network', 'subnetwork')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnetwork: str

    def __init__(self, network: _Optional[str]=..., subnetwork: _Optional[str]=...) -> None:
        ...

class NetworkResourceConfig(_message.Message):
    __slots__ = ('new_network', 'existing_network', 'new_compute_network', 'existing_compute_network')
    NEW_NETWORK_FIELD_NUMBER: _ClassVar[int]
    EXISTING_NETWORK_FIELD_NUMBER: _ClassVar[int]
    NEW_COMPUTE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    EXISTING_COMPUTE_NETWORK_FIELD_NUMBER: _ClassVar[int]
    new_network: NewNetworkConfig
    existing_network: ExistingNetworkConfig
    new_compute_network: NewComputeNetworkConfig
    existing_compute_network: ExistingComputeNetworkConfig

    def __init__(self, new_network: _Optional[_Union[NewNetworkConfig, _Mapping]]=..., existing_network: _Optional[_Union[ExistingNetworkConfig, _Mapping]]=..., new_compute_network: _Optional[_Union[NewComputeNetworkConfig, _Mapping]]=..., existing_compute_network: _Optional[_Union[ExistingComputeNetworkConfig, _Mapping]]=...) -> None:
        ...

class NewNetworkConfig(_message.Message):
    __slots__ = ('network', 'description')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    network: str
    description: str

    def __init__(self, network: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class ExistingNetworkConfig(_message.Message):
    __slots__ = ('network', 'subnetwork')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnetwork: str

    def __init__(self, network: _Optional[str]=..., subnetwork: _Optional[str]=...) -> None:
        ...

class StorageResource(_message.Message):
    __slots__ = ('filestore', 'bucket', 'lustre', 'config')
    FILESTORE_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    LUSTRE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    filestore: FilestoreReference
    bucket: BucketReference
    lustre: LustreReference
    config: StorageResourceConfig

    def __init__(self, filestore: _Optional[_Union[FilestoreReference, _Mapping]]=..., bucket: _Optional[_Union[BucketReference, _Mapping]]=..., lustre: _Optional[_Union[LustreReference, _Mapping]]=..., config: _Optional[_Union[StorageResourceConfig, _Mapping]]=...) -> None:
        ...

class FilestoreReference(_message.Message):
    __slots__ = ('filestore',)
    FILESTORE_FIELD_NUMBER: _ClassVar[int]
    filestore: str

    def __init__(self, filestore: _Optional[str]=...) -> None:
        ...

class BucketReference(_message.Message):
    __slots__ = ('bucket',)
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    bucket: str

    def __init__(self, bucket: _Optional[str]=...) -> None:
        ...

class LustreReference(_message.Message):
    __slots__ = ('lustre',)
    LUSTRE_FIELD_NUMBER: _ClassVar[int]
    lustre: str

    def __init__(self, lustre: _Optional[str]=...) -> None:
        ...

class StorageResourceConfig(_message.Message):
    __slots__ = ('new_filestore', 'existing_filestore', 'new_bucket', 'existing_bucket', 'new_lustre', 'existing_lustre')
    NEW_FILESTORE_FIELD_NUMBER: _ClassVar[int]
    EXISTING_FILESTORE_FIELD_NUMBER: _ClassVar[int]
    NEW_BUCKET_FIELD_NUMBER: _ClassVar[int]
    EXISTING_BUCKET_FIELD_NUMBER: _ClassVar[int]
    NEW_LUSTRE_FIELD_NUMBER: _ClassVar[int]
    EXISTING_LUSTRE_FIELD_NUMBER: _ClassVar[int]
    new_filestore: NewFilestoreConfig
    existing_filestore: ExistingFilestoreConfig
    new_bucket: NewBucketConfig
    existing_bucket: ExistingBucketConfig
    new_lustre: NewLustreConfig
    existing_lustre: ExistingLustreConfig

    def __init__(self, new_filestore: _Optional[_Union[NewFilestoreConfig, _Mapping]]=..., existing_filestore: _Optional[_Union[ExistingFilestoreConfig, _Mapping]]=..., new_bucket: _Optional[_Union[NewBucketConfig, _Mapping]]=..., existing_bucket: _Optional[_Union[ExistingBucketConfig, _Mapping]]=..., new_lustre: _Optional[_Union[NewLustreConfig, _Mapping]]=..., existing_lustre: _Optional[_Union[ExistingLustreConfig, _Mapping]]=...) -> None:
        ...

class NewFilestoreConfig(_message.Message):
    __slots__ = ('filestore', 'description', 'file_shares', 'tier', 'protocol')

    class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIER_UNSPECIFIED: _ClassVar[NewFilestoreConfig.Tier]
        ZONAL: _ClassVar[NewFilestoreConfig.Tier]
        REGIONAL: _ClassVar[NewFilestoreConfig.Tier]
        BASIC_HDD: _ClassVar[NewFilestoreConfig.Tier]
        BASIC_SSD: _ClassVar[NewFilestoreConfig.Tier]
        HIGH_SCALE_SSD: _ClassVar[NewFilestoreConfig.Tier]
        ENTERPRISE: _ClassVar[NewFilestoreConfig.Tier]
    TIER_UNSPECIFIED: NewFilestoreConfig.Tier
    ZONAL: NewFilestoreConfig.Tier
    REGIONAL: NewFilestoreConfig.Tier
    BASIC_HDD: NewFilestoreConfig.Tier
    BASIC_SSD: NewFilestoreConfig.Tier
    HIGH_SCALE_SSD: NewFilestoreConfig.Tier
    ENTERPRISE: NewFilestoreConfig.Tier

    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROTOCOL_UNSPECIFIED: _ClassVar[NewFilestoreConfig.Protocol]
        NFSV3: _ClassVar[NewFilestoreConfig.Protocol]
        NFSV41: _ClassVar[NewFilestoreConfig.Protocol]
    PROTOCOL_UNSPECIFIED: NewFilestoreConfig.Protocol
    NFSV3: NewFilestoreConfig.Protocol
    NFSV41: NewFilestoreConfig.Protocol
    FILESTORE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FILE_SHARES_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    filestore: str
    description: str
    file_shares: _containers.RepeatedCompositeFieldContainer[FileShareConfig]
    tier: NewFilestoreConfig.Tier
    protocol: NewFilestoreConfig.Protocol

    def __init__(self, filestore: _Optional[str]=..., description: _Optional[str]=..., file_shares: _Optional[_Iterable[_Union[FileShareConfig, _Mapping]]]=..., tier: _Optional[_Union[NewFilestoreConfig.Tier, str]]=..., protocol: _Optional[_Union[NewFilestoreConfig.Protocol, str]]=...) -> None:
        ...

class FileShareConfig(_message.Message):
    __slots__ = ('capacity_gb', 'file_share')
    CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    FILE_SHARE_FIELD_NUMBER: _ClassVar[int]
    capacity_gb: int
    file_share: str

    def __init__(self, capacity_gb: _Optional[int]=..., file_share: _Optional[str]=...) -> None:
        ...

class ExistingFilestoreConfig(_message.Message):
    __slots__ = ('filestore',)
    FILESTORE_FIELD_NUMBER: _ClassVar[int]
    filestore: str

    def __init__(self, filestore: _Optional[str]=...) -> None:
        ...

class NewBucketConfig(_message.Message):
    __slots__ = ('autoclass', 'storage_class', 'bucket', 'hierarchical_namespace')

    class StorageClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STORAGE_CLASS_UNSPECIFIED: _ClassVar[NewBucketConfig.StorageClass]
        STANDARD: _ClassVar[NewBucketConfig.StorageClass]
        NEARLINE: _ClassVar[NewBucketConfig.StorageClass]
        COLDLINE: _ClassVar[NewBucketConfig.StorageClass]
        ARCHIVE: _ClassVar[NewBucketConfig.StorageClass]
    STORAGE_CLASS_UNSPECIFIED: NewBucketConfig.StorageClass
    STANDARD: NewBucketConfig.StorageClass
    NEARLINE: NewBucketConfig.StorageClass
    COLDLINE: NewBucketConfig.StorageClass
    ARCHIVE: NewBucketConfig.StorageClass
    AUTOCLASS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    HIERARCHICAL_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    autoclass: GcsAutoclassConfig
    storage_class: NewBucketConfig.StorageClass
    bucket: str
    hierarchical_namespace: GcsHierarchicalNamespaceConfig

    def __init__(self, autoclass: _Optional[_Union[GcsAutoclassConfig, _Mapping]]=..., storage_class: _Optional[_Union[NewBucketConfig.StorageClass, str]]=..., bucket: _Optional[str]=..., hierarchical_namespace: _Optional[_Union[GcsHierarchicalNamespaceConfig, _Mapping]]=...) -> None:
        ...

class GcsAutoclassConfig(_message.Message):
    __slots__ = ('enabled', 'terminal_storage_class')

    class TerminalStorageClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TERMINAL_STORAGE_CLASS_UNSPECIFIED: _ClassVar[GcsAutoclassConfig.TerminalStorageClass]
        TERMINAL_STORAGE_CLASS_NEARLINE: _ClassVar[GcsAutoclassConfig.TerminalStorageClass]
        TERMINAL_STORAGE_CLASS_ARCHIVE: _ClassVar[GcsAutoclassConfig.TerminalStorageClass]
    TERMINAL_STORAGE_CLASS_UNSPECIFIED: GcsAutoclassConfig.TerminalStorageClass
    TERMINAL_STORAGE_CLASS_NEARLINE: GcsAutoclassConfig.TerminalStorageClass
    TERMINAL_STORAGE_CLASS_ARCHIVE: GcsAutoclassConfig.TerminalStorageClass
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    TERMINAL_STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    terminal_storage_class: GcsAutoclassConfig.TerminalStorageClass

    def __init__(self, enabled: bool=..., terminal_storage_class: _Optional[_Union[GcsAutoclassConfig.TerminalStorageClass, str]]=...) -> None:
        ...

class GcsHierarchicalNamespaceConfig(_message.Message):
    __slots__ = ('enabled',)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool

    def __init__(self, enabled: bool=...) -> None:
        ...

class ExistingBucketConfig(_message.Message):
    __slots__ = ('bucket',)
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    bucket: str

    def __init__(self, bucket: _Optional[str]=...) -> None:
        ...

class NewLustreConfig(_message.Message):
    __slots__ = ('lustre', 'description', 'filesystem', 'capacity_gb')
    LUSTRE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    lustre: str
    description: str
    filesystem: str
    capacity_gb: int

    def __init__(self, lustre: _Optional[str]=..., description: _Optional[str]=..., filesystem: _Optional[str]=..., capacity_gb: _Optional[int]=...) -> None:
        ...

class ExistingLustreConfig(_message.Message):
    __slots__ = ('lustre',)
    LUSTRE_FIELD_NUMBER: _ClassVar[int]
    lustre: str

    def __init__(self, lustre: _Optional[str]=...) -> None:
        ...

class ComputeResource(_message.Message):
    __slots__ = ('new_on_demand_instances', 'new_spot_instances', 'new_reserved_instances', 'new_dws_flex_instances', 'config')
    NEW_ON_DEMAND_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEW_SPOT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEW_RESERVED_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEW_DWS_FLEX_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    new_on_demand_instances: NewOnDemandInstancesConfig
    new_spot_instances: NewSpotInstancesConfig
    new_reserved_instances: NewReservedInstancesConfig
    new_dws_flex_instances: NewDWSFlexInstancesConfig
    config: ComputeResourceConfig

    def __init__(self, new_on_demand_instances: _Optional[_Union[NewOnDemandInstancesConfig, _Mapping]]=..., new_spot_instances: _Optional[_Union[NewSpotInstancesConfig, _Mapping]]=..., new_reserved_instances: _Optional[_Union[NewReservedInstancesConfig, _Mapping]]=..., new_dws_flex_instances: _Optional[_Union[NewDWSFlexInstancesConfig, _Mapping]]=..., config: _Optional[_Union[ComputeResourceConfig, _Mapping]]=...) -> None:
        ...

class ComputeResourceConfig(_message.Message):
    __slots__ = ('new_on_demand_instances', 'new_spot_instances', 'new_reserved_instances', 'new_dws_flex_instances', 'new_flex_start_instances')
    NEW_ON_DEMAND_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEW_SPOT_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEW_RESERVED_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEW_DWS_FLEX_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEW_FLEX_START_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    new_on_demand_instances: NewOnDemandInstancesConfig
    new_spot_instances: NewSpotInstancesConfig
    new_reserved_instances: NewReservedInstancesConfig
    new_dws_flex_instances: NewDWSFlexInstancesConfig
    new_flex_start_instances: NewFlexStartInstancesConfig

    def __init__(self, new_on_demand_instances: _Optional[_Union[NewOnDemandInstancesConfig, _Mapping]]=..., new_spot_instances: _Optional[_Union[NewSpotInstancesConfig, _Mapping]]=..., new_reserved_instances: _Optional[_Union[NewReservedInstancesConfig, _Mapping]]=..., new_dws_flex_instances: _Optional[_Union[NewDWSFlexInstancesConfig, _Mapping]]=..., new_flex_start_instances: _Optional[_Union[NewFlexStartInstancesConfig, _Mapping]]=...) -> None:
        ...

class NewOnDemandInstancesConfig(_message.Message):
    __slots__ = ('zone', 'machine_type', 'atm_tags', 'boot_disk')

    class AtmTagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATM_TAGS_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
    zone: str
    machine_type: str
    atm_tags: _containers.ScalarMap[str, str]
    boot_disk: Disk

    def __init__(self, zone: _Optional[str]=..., machine_type: _Optional[str]=..., atm_tags: _Optional[_Mapping[str, str]]=..., boot_disk: _Optional[_Union[Disk, _Mapping]]=...) -> None:
        ...

class NewSpotInstancesConfig(_message.Message):
    __slots__ = ('zone', 'machine_type', 'atm_tags', 'boot_disk', 'termination_action')

    class TerminationAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TERMINATION_ACTION_UNSPECIFIED: _ClassVar[NewSpotInstancesConfig.TerminationAction]
        STOP: _ClassVar[NewSpotInstancesConfig.TerminationAction]
        DELETE: _ClassVar[NewSpotInstancesConfig.TerminationAction]
    TERMINATION_ACTION_UNSPECIFIED: NewSpotInstancesConfig.TerminationAction
    STOP: NewSpotInstancesConfig.TerminationAction
    DELETE: NewSpotInstancesConfig.TerminationAction

    class AtmTagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATM_TAGS_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    zone: str
    machine_type: str
    atm_tags: _containers.ScalarMap[str, str]
    boot_disk: Disk
    termination_action: NewSpotInstancesConfig.TerminationAction

    def __init__(self, zone: _Optional[str]=..., machine_type: _Optional[str]=..., atm_tags: _Optional[_Mapping[str, str]]=..., boot_disk: _Optional[_Union[Disk, _Mapping]]=..., termination_action: _Optional[_Union[NewSpotInstancesConfig.TerminationAction, str]]=...) -> None:
        ...

class NewReservedInstancesConfig(_message.Message):
    __slots__ = ('reservation', 'atm_tags', 'zone', 'machine_type', 'type', 'boot_disk')

    class ReservationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESERVATION_TYPE_UNSPECIFIED: _ClassVar[NewReservedInstancesConfig.ReservationType]
        NO_RESERVATION: _ClassVar[NewReservedInstancesConfig.ReservationType]
        ANY_RESERVATION: _ClassVar[NewReservedInstancesConfig.ReservationType]
        SPECIFIC_RESERVATION: _ClassVar[NewReservedInstancesConfig.ReservationType]
    RESERVATION_TYPE_UNSPECIFIED: NewReservedInstancesConfig.ReservationType
    NO_RESERVATION: NewReservedInstancesConfig.ReservationType
    ANY_RESERVATION: NewReservedInstancesConfig.ReservationType
    SPECIFIC_RESERVATION: NewReservedInstancesConfig.ReservationType

    class AtmTagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    RESERVATION_FIELD_NUMBER: _ClassVar[int]
    ATM_TAGS_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
    reservation: str
    atm_tags: _containers.ScalarMap[str, str]
    zone: str
    machine_type: str
    type: NewReservedInstancesConfig.ReservationType
    boot_disk: Disk

    def __init__(self, reservation: _Optional[str]=..., atm_tags: _Optional[_Mapping[str, str]]=..., zone: _Optional[str]=..., machine_type: _Optional[str]=..., type: _Optional[_Union[NewReservedInstancesConfig.ReservationType, str]]=..., boot_disk: _Optional[_Union[Disk, _Mapping]]=...) -> None:
        ...

class NewFlexStartInstancesConfig(_message.Message):
    __slots__ = ('zone', 'machine_type', 'max_duration', 'atm_tags', 'termination_action', 'boot_disk')

    class TerminationAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TERMINATION_ACTION_UNSPECIFIED: _ClassVar[NewFlexStartInstancesConfig.TerminationAction]
        STOP: _ClassVar[NewFlexStartInstancesConfig.TerminationAction]
        DELETE: _ClassVar[NewFlexStartInstancesConfig.TerminationAction]
    TERMINATION_ACTION_UNSPECIFIED: NewFlexStartInstancesConfig.TerminationAction
    STOP: NewFlexStartInstancesConfig.TerminationAction
    DELETE: NewFlexStartInstancesConfig.TerminationAction

    class AtmTagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    ATM_TAGS_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
    zone: str
    machine_type: str
    max_duration: _duration_pb2.Duration
    atm_tags: _containers.ScalarMap[str, str]
    termination_action: NewFlexStartInstancesConfig.TerminationAction
    boot_disk: Disk

    def __init__(self, zone: _Optional[str]=..., machine_type: _Optional[str]=..., max_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., atm_tags: _Optional[_Mapping[str, str]]=..., termination_action: _Optional[_Union[NewFlexStartInstancesConfig.TerminationAction, str]]=..., boot_disk: _Optional[_Union[Disk, _Mapping]]=...) -> None:
        ...

class Disk(_message.Message):
    __slots__ = ('type', 'size_gb', 'boot', 'source_image')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    BOOT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    type: str
    size_gb: int
    boot: bool
    source_image: str

    def __init__(self, type: _Optional[str]=..., size_gb: _Optional[int]=..., boot: bool=..., source_image: _Optional[str]=...) -> None:
        ...

class BootDisk(_message.Message):
    __slots__ = ('type', 'size_gb', 'image', 'effective_image')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    type: str
    size_gb: int
    image: str
    effective_image: str

    def __init__(self, type: _Optional[str]=..., size_gb: _Optional[int]=..., image: _Optional[str]=..., effective_image: _Optional[str]=...) -> None:
        ...

class AtmTag(_message.Message):
    __slots__ = ('key', 'value')
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str

    def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class Orchestrator(_message.Message):
    __slots__ = ('slurm',)
    SLURM_FIELD_NUMBER: _ClassVar[int]
    slurm: SlurmOrchestrator

    def __init__(self, slurm: _Optional[_Union[SlurmOrchestrator, _Mapping]]=...) -> None:
        ...

class SlurmOrchestrator(_message.Message):
    __slots__ = ('login_nodes', 'node_sets', 'partitions', 'default_partition', 'prolog_bash_scripts', 'epilog_bash_scripts', 'config', 'task_prolog_bash_scripts', 'task_epilog_bash_scripts')

    class SlurmConfig(_message.Message):
        __slots__ = ('requeue_exit_codes', 'requeue_hold_exit_codes', 'prolog_flags', 'prolog_epilog_timeout', 'accounting_storage_enforce_flags', 'priority_type', 'priority_weight_age', 'priority_weight_assoc', 'priority_weight_fairshare', 'priority_weight_job_size', 'priority_weight_partition', 'priority_weight_qos', 'priority_weight_tres', 'preempt_mode', 'preempt_type', 'preempt_exempt_time')

        class PrologFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PROLOG_FLAG_UNSPECIFIED: _ClassVar[SlurmOrchestrator.SlurmConfig.PrologFlag]
            ALLOC: _ClassVar[SlurmOrchestrator.SlurmConfig.PrologFlag]
            CONTAIN: _ClassVar[SlurmOrchestrator.SlurmConfig.PrologFlag]
            DEFER_BATCH: _ClassVar[SlurmOrchestrator.SlurmConfig.PrologFlag]
            NO_HOLD: _ClassVar[SlurmOrchestrator.SlurmConfig.PrologFlag]
            FORCE_REQUEUE_ON_FAIL: _ClassVar[SlurmOrchestrator.SlurmConfig.PrologFlag]
            RUN_IN_JOB: _ClassVar[SlurmOrchestrator.SlurmConfig.PrologFlag]
            SERIAL: _ClassVar[SlurmOrchestrator.SlurmConfig.PrologFlag]
            X11: _ClassVar[SlurmOrchestrator.SlurmConfig.PrologFlag]
        PROLOG_FLAG_UNSPECIFIED: SlurmOrchestrator.SlurmConfig.PrologFlag
        ALLOC: SlurmOrchestrator.SlurmConfig.PrologFlag
        CONTAIN: SlurmOrchestrator.SlurmConfig.PrologFlag
        DEFER_BATCH: SlurmOrchestrator.SlurmConfig.PrologFlag
        NO_HOLD: SlurmOrchestrator.SlurmConfig.PrologFlag
        FORCE_REQUEUE_ON_FAIL: SlurmOrchestrator.SlurmConfig.PrologFlag
        RUN_IN_JOB: SlurmOrchestrator.SlurmConfig.PrologFlag
        SERIAL: SlurmOrchestrator.SlurmConfig.PrologFlag
        X11: SlurmOrchestrator.SlurmConfig.PrologFlag

        class AccountingStorageEnforceFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACCOUNTING_STORAGE_ENFORCE_FLAG_UNSPECIFIED: _ClassVar[SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag]
            ALL: _ClassVar[SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag]
            ASSOCIATIONS: _ClassVar[SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag]
            LIMITS: _ClassVar[SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag]
            NOJOBS: _ClassVar[SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag]
            NOSTEPS: _ClassVar[SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag]
            QOS: _ClassVar[SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag]
            SAFE: _ClassVar[SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag]
            WCKEYS: _ClassVar[SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag]
        ACCOUNTING_STORAGE_ENFORCE_FLAG_UNSPECIFIED: SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag
        ALL: SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag
        ASSOCIATIONS: SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag
        LIMITS: SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag
        NOJOBS: SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag
        NOSTEPS: SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag
        QOS: SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag
        SAFE: SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag
        WCKEYS: SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag

        class PriorityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PRIORITY_TYPE_UNSPECIFIED: _ClassVar[SlurmOrchestrator.SlurmConfig.PriorityType]
            PRIORITY_BASIC: _ClassVar[SlurmOrchestrator.SlurmConfig.PriorityType]
            PRIORITY_MULTIFACTOR: _ClassVar[SlurmOrchestrator.SlurmConfig.PriorityType]
        PRIORITY_TYPE_UNSPECIFIED: SlurmOrchestrator.SlurmConfig.PriorityType
        PRIORITY_BASIC: SlurmOrchestrator.SlurmConfig.PriorityType
        PRIORITY_MULTIFACTOR: SlurmOrchestrator.SlurmConfig.PriorityType

        class PreemptMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PREEMPT_MODE_UNSPECIFIED: _ClassVar[SlurmOrchestrator.SlurmConfig.PreemptMode]
            OFF: _ClassVar[SlurmOrchestrator.SlurmConfig.PreemptMode]
            CANCEL: _ClassVar[SlurmOrchestrator.SlurmConfig.PreemptMode]
            GANG: _ClassVar[SlurmOrchestrator.SlurmConfig.PreemptMode]
            REQUEUE: _ClassVar[SlurmOrchestrator.SlurmConfig.PreemptMode]
            SUSPEND: _ClassVar[SlurmOrchestrator.SlurmConfig.PreemptMode]
            PRIORITY: _ClassVar[SlurmOrchestrator.SlurmConfig.PreemptMode]
            WITHIN: _ClassVar[SlurmOrchestrator.SlurmConfig.PreemptMode]
        PREEMPT_MODE_UNSPECIFIED: SlurmOrchestrator.SlurmConfig.PreemptMode
        OFF: SlurmOrchestrator.SlurmConfig.PreemptMode
        CANCEL: SlurmOrchestrator.SlurmConfig.PreemptMode
        GANG: SlurmOrchestrator.SlurmConfig.PreemptMode
        REQUEUE: SlurmOrchestrator.SlurmConfig.PreemptMode
        SUSPEND: SlurmOrchestrator.SlurmConfig.PreemptMode
        PRIORITY: SlurmOrchestrator.SlurmConfig.PreemptMode
        WITHIN: SlurmOrchestrator.SlurmConfig.PreemptMode

        class PreemptType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PREEMPT_TYPE_UNSPECIFIED: _ClassVar[SlurmOrchestrator.SlurmConfig.PreemptType]
            PREEMPT_NONE: _ClassVar[SlurmOrchestrator.SlurmConfig.PreemptType]
            PREEMPT_PARTITION_PRIO: _ClassVar[SlurmOrchestrator.SlurmConfig.PreemptType]
            PREEMPT_QOS: _ClassVar[SlurmOrchestrator.SlurmConfig.PreemptType]
        PREEMPT_TYPE_UNSPECIFIED: SlurmOrchestrator.SlurmConfig.PreemptType
        PREEMPT_NONE: SlurmOrchestrator.SlurmConfig.PreemptType
        PREEMPT_PARTITION_PRIO: SlurmOrchestrator.SlurmConfig.PreemptType
        PREEMPT_QOS: SlurmOrchestrator.SlurmConfig.PreemptType
        REQUEUE_EXIT_CODES_FIELD_NUMBER: _ClassVar[int]
        REQUEUE_HOLD_EXIT_CODES_FIELD_NUMBER: _ClassVar[int]
        PROLOG_FLAGS_FIELD_NUMBER: _ClassVar[int]
        PROLOG_EPILOG_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        ACCOUNTING_STORAGE_ENFORCE_FLAGS_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_TYPE_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_WEIGHT_AGE_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_WEIGHT_ASSOC_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_WEIGHT_FAIRSHARE_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_WEIGHT_JOB_SIZE_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_WEIGHT_PARTITION_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_WEIGHT_QOS_FIELD_NUMBER: _ClassVar[int]
        PRIORITY_WEIGHT_TRES_FIELD_NUMBER: _ClassVar[int]
        PREEMPT_MODE_FIELD_NUMBER: _ClassVar[int]
        PREEMPT_TYPE_FIELD_NUMBER: _ClassVar[int]
        PREEMPT_EXEMPT_TIME_FIELD_NUMBER: _ClassVar[int]
        requeue_exit_codes: _containers.RepeatedScalarFieldContainer[int]
        requeue_hold_exit_codes: _containers.RepeatedScalarFieldContainer[int]
        prolog_flags: _containers.RepeatedScalarFieldContainer[SlurmOrchestrator.SlurmConfig.PrologFlag]
        prolog_epilog_timeout: _duration_pb2.Duration
        accounting_storage_enforce_flags: _containers.RepeatedScalarFieldContainer[SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag]
        priority_type: SlurmOrchestrator.SlurmConfig.PriorityType
        priority_weight_age: int
        priority_weight_assoc: int
        priority_weight_fairshare: int
        priority_weight_job_size: int
        priority_weight_partition: int
        priority_weight_qos: int
        priority_weight_tres: str
        preempt_mode: _containers.RepeatedScalarFieldContainer[SlurmOrchestrator.SlurmConfig.PreemptMode]
        preempt_type: SlurmOrchestrator.SlurmConfig.PreemptType
        preempt_exempt_time: str

        def __init__(self, requeue_exit_codes: _Optional[_Iterable[int]]=..., requeue_hold_exit_codes: _Optional[_Iterable[int]]=..., prolog_flags: _Optional[_Iterable[_Union[SlurmOrchestrator.SlurmConfig.PrologFlag, str]]]=..., prolog_epilog_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., accounting_storage_enforce_flags: _Optional[_Iterable[_Union[SlurmOrchestrator.SlurmConfig.AccountingStorageEnforceFlag, str]]]=..., priority_type: _Optional[_Union[SlurmOrchestrator.SlurmConfig.PriorityType, str]]=..., priority_weight_age: _Optional[int]=..., priority_weight_assoc: _Optional[int]=..., priority_weight_fairshare: _Optional[int]=..., priority_weight_job_size: _Optional[int]=..., priority_weight_partition: _Optional[int]=..., priority_weight_qos: _Optional[int]=..., priority_weight_tres: _Optional[str]=..., preempt_mode: _Optional[_Iterable[_Union[SlurmOrchestrator.SlurmConfig.PreemptMode, str]]]=..., preempt_type: _Optional[_Union[SlurmOrchestrator.SlurmConfig.PreemptType, str]]=..., preempt_exempt_time: _Optional[str]=...) -> None:
            ...
    LOGIN_NODES_FIELD_NUMBER: _ClassVar[int]
    NODE_SETS_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PARTITION_FIELD_NUMBER: _ClassVar[int]
    PROLOG_BASH_SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    EPILOG_BASH_SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    TASK_PROLOG_BASH_SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    TASK_EPILOG_BASH_SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    login_nodes: SlurmLoginNodes
    node_sets: _containers.RepeatedCompositeFieldContainer[SlurmNodeSet]
    partitions: _containers.RepeatedCompositeFieldContainer[SlurmPartition]
    default_partition: str
    prolog_bash_scripts: _containers.RepeatedScalarFieldContainer[str]
    epilog_bash_scripts: _containers.RepeatedScalarFieldContainer[str]
    config: SlurmOrchestrator.SlurmConfig
    task_prolog_bash_scripts: _containers.RepeatedScalarFieldContainer[str]
    task_epilog_bash_scripts: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, login_nodes: _Optional[_Union[SlurmLoginNodes, _Mapping]]=..., node_sets: _Optional[_Iterable[_Union[SlurmNodeSet, _Mapping]]]=..., partitions: _Optional[_Iterable[_Union[SlurmPartition, _Mapping]]]=..., default_partition: _Optional[str]=..., prolog_bash_scripts: _Optional[_Iterable[str]]=..., epilog_bash_scripts: _Optional[_Iterable[str]]=..., config: _Optional[_Union[SlurmOrchestrator.SlurmConfig, _Mapping]]=..., task_prolog_bash_scripts: _Optional[_Iterable[str]]=..., task_epilog_bash_scripts: _Optional[_Iterable[str]]=...) -> None:
        ...

class SlurmNodeSet(_message.Message):
    __slots__ = ('compute_instance', 'container_node_pool', 'id', 'compute_id', 'storage_configs', 'static_node_count', 'max_dynamic_node_count', 'service_account', 'boot_disk', 'startup_script', 'resource_request_id', 'enable_os_login', 'can_ip_forward', 'enable_public_ips', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    COMPUTE_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_NODE_POOL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    STATIC_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_DYNAMIC_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
    STARTUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_OS_LOGIN_FIELD_NUMBER: _ClassVar[int]
    CAN_IP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PUBLIC_IPS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    compute_instance: ComputeInstanceSlurmNodeSet
    container_node_pool: ContainerNodePoolSlurmNodeSet
    id: str
    compute_id: str
    storage_configs: _containers.RepeatedCompositeFieldContainer[StorageConfig]
    static_node_count: int
    max_dynamic_node_count: int
    service_account: ServiceAccount
    boot_disk: Disk
    startup_script: str
    resource_request_id: str
    enable_os_login: bool
    can_ip_forward: bool
    enable_public_ips: bool
    labels: _containers.ScalarMap[str, str]

    def __init__(self, compute_instance: _Optional[_Union[ComputeInstanceSlurmNodeSet, _Mapping]]=..., container_node_pool: _Optional[_Union[ContainerNodePoolSlurmNodeSet, _Mapping]]=..., id: _Optional[str]=..., compute_id: _Optional[str]=..., storage_configs: _Optional[_Iterable[_Union[StorageConfig, _Mapping]]]=..., static_node_count: _Optional[int]=..., max_dynamic_node_count: _Optional[int]=..., service_account: _Optional[_Union[ServiceAccount, _Mapping]]=..., boot_disk: _Optional[_Union[Disk, _Mapping]]=..., startup_script: _Optional[str]=..., resource_request_id: _Optional[str]=..., enable_os_login: bool=..., can_ip_forward: bool=..., enable_public_ips: bool=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ComputeInstanceSlurmNodeSet(_message.Message):
    __slots__ = ('startup_script', 'labels', 'boot_disk')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    STARTUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
    startup_script: str
    labels: _containers.ScalarMap[str, str]
    boot_disk: BootDisk

    def __init__(self, startup_script: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., boot_disk: _Optional[_Union[BootDisk, _Mapping]]=...) -> None:
        ...

class ContainerNodePoolSlurmNodeSet(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class SlurmPartition(_message.Message):
    __slots__ = ('id', 'node_set_ids', 'exclusive')
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    node_set_ids: _containers.RepeatedScalarFieldContainer[str]
    exclusive: bool

    def __init__(self, id: _Optional[str]=..., node_set_ids: _Optional[_Iterable[str]]=..., exclusive: bool=...) -> None:
        ...

class SlurmLoginNodes(_message.Message):
    __slots__ = ('count', 'zone', 'machine_type', 'startup_script', 'enable_os_login', 'enable_public_ips', 'labels', 'storage_configs', 'instances', 'disks', 'service_account', 'boot_disk')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STARTUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_OS_LOGIN_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PUBLIC_IPS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
    count: int
    zone: str
    machine_type: str
    startup_script: str
    enable_os_login: bool
    enable_public_ips: bool
    labels: _containers.ScalarMap[str, str]
    storage_configs: _containers.RepeatedCompositeFieldContainer[StorageConfig]
    instances: _containers.RepeatedCompositeFieldContainer[ComputeInstance]
    disks: _containers.RepeatedCompositeFieldContainer[Disk]
    service_account: ServiceAccount
    boot_disk: BootDisk

    def __init__(self, count: _Optional[int]=..., zone: _Optional[str]=..., machine_type: _Optional[str]=..., startup_script: _Optional[str]=..., enable_os_login: bool=..., enable_public_ips: bool=..., labels: _Optional[_Mapping[str, str]]=..., storage_configs: _Optional[_Iterable[_Union[StorageConfig, _Mapping]]]=..., instances: _Optional[_Iterable[_Union[ComputeInstance, _Mapping]]]=..., disks: _Optional[_Iterable[_Union[Disk, _Mapping]]]=..., service_account: _Optional[_Union[ServiceAccount, _Mapping]]=..., boot_disk: _Optional[_Union[BootDisk, _Mapping]]=...) -> None:
        ...

class ServiceAccount(_message.Message):
    __slots__ = ('email', 'scopes')
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    email: str
    scopes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, email: _Optional[str]=..., scopes: _Optional[_Iterable[str]]=...) -> None:
        ...

class StorageConfig(_message.Message):
    __slots__ = ('id', 'local_mount')
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_MOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    local_mount: str

    def __init__(self, id: _Optional[str]=..., local_mount: _Optional[str]=...) -> None:
        ...

class ComputeInstance(_message.Message):
    __slots__ = ('instance',)
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    instance: str

    def __init__(self, instance: _Optional[str]=...) -> None:
        ...

class Network(_message.Message):
    __slots__ = ('initialize_params', 'network_source', 'network', 'subnetwork')
    INITIALIZE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    initialize_params: NetworkInitializeParams
    network_source: NetworkSource
    network: str
    subnetwork: str

    def __init__(self, initialize_params: _Optional[_Union[NetworkInitializeParams, _Mapping]]=..., network_source: _Optional[_Union[NetworkSource, _Mapping]]=..., network: _Optional[str]=..., subnetwork: _Optional[str]=...) -> None:
        ...

class NetworkInitializeParams(_message.Message):
    __slots__ = ('network', 'description')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    network: str
    description: str

    def __init__(self, network: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class NetworkSource(_message.Message):
    __slots__ = ('network', 'subnetwork')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnetwork: str

    def __init__(self, network: _Optional[str]=..., subnetwork: _Optional[str]=...) -> None:
        ...

class ComputeNetworkReference(_message.Message):
    __slots__ = ('network', 'subnetwork')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnetwork: str

    def __init__(self, network: _Optional[str]=..., subnetwork: _Optional[str]=...) -> None:
        ...

class NewComputeNetworkConfig(_message.Message):
    __slots__ = ('network', 'description')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    network: str
    description: str

    def __init__(self, network: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class ExistingComputeNetworkConfig(_message.Message):
    __slots__ = ('network', 'subnetwork')
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
    network: str
    subnetwork: str

    def __init__(self, network: _Optional[str]=..., subnetwork: _Optional[str]=...) -> None:
        ...

class Storage(_message.Message):
    __slots__ = ('initialize_params', 'storage_source', 'id', 'storage')
    INITIALIZE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    initialize_params: StorageInitializeParams
    storage_source: StorageSource
    id: str
    storage: str

    def __init__(self, initialize_params: _Optional[_Union[StorageInitializeParams, _Mapping]]=..., storage_source: _Optional[_Union[StorageSource, _Mapping]]=..., id: _Optional[str]=..., storage: _Optional[str]=...) -> None:
        ...

class StorageInitializeParams(_message.Message):
    __slots__ = ('filestore', 'gcs', 'lustre')
    FILESTORE_FIELD_NUMBER: _ClassVar[int]
    GCS_FIELD_NUMBER: _ClassVar[int]
    LUSTRE_FIELD_NUMBER: _ClassVar[int]
    filestore: FilestoreInitializeParams
    gcs: GcsInitializeParams
    lustre: LustreInitializeParams

    def __init__(self, filestore: _Optional[_Union[FilestoreInitializeParams, _Mapping]]=..., gcs: _Optional[_Union[GcsInitializeParams, _Mapping]]=..., lustre: _Optional[_Union[LustreInitializeParams, _Mapping]]=...) -> None:
        ...

class FilestoreInitializeParams(_message.Message):
    __slots__ = ('file_shares', 'tier', 'filestore', 'description', 'protocol')

    class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIER_UNSPECIFIED: _ClassVar[FilestoreInitializeParams.Tier]
        TIER_BASIC_HDD: _ClassVar[FilestoreInitializeParams.Tier]
        TIER_BASIC_SSD: _ClassVar[FilestoreInitializeParams.Tier]
        TIER_HIGH_SCALE_SSD: _ClassVar[FilestoreInitializeParams.Tier]
        TIER_ZONAL: _ClassVar[FilestoreInitializeParams.Tier]
        TIER_ENTERPRISE: _ClassVar[FilestoreInitializeParams.Tier]
        TIER_REGIONAL: _ClassVar[FilestoreInitializeParams.Tier]
    TIER_UNSPECIFIED: FilestoreInitializeParams.Tier
    TIER_BASIC_HDD: FilestoreInitializeParams.Tier
    TIER_BASIC_SSD: FilestoreInitializeParams.Tier
    TIER_HIGH_SCALE_SSD: FilestoreInitializeParams.Tier
    TIER_ZONAL: FilestoreInitializeParams.Tier
    TIER_ENTERPRISE: FilestoreInitializeParams.Tier
    TIER_REGIONAL: FilestoreInitializeParams.Tier

    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROTOCOL_UNSPECIFIED: _ClassVar[FilestoreInitializeParams.Protocol]
        PROTOCOL_NFSV3: _ClassVar[FilestoreInitializeParams.Protocol]
        PROTOCOL_NFSV41: _ClassVar[FilestoreInitializeParams.Protocol]
    PROTOCOL_UNSPECIFIED: FilestoreInitializeParams.Protocol
    PROTOCOL_NFSV3: FilestoreInitializeParams.Protocol
    PROTOCOL_NFSV41: FilestoreInitializeParams.Protocol
    FILE_SHARES_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    FILESTORE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    file_shares: _containers.RepeatedCompositeFieldContainer[FileShareConfig]
    tier: FilestoreInitializeParams.Tier
    filestore: str
    description: str
    protocol: FilestoreInitializeParams.Protocol

    def __init__(self, file_shares: _Optional[_Iterable[_Union[FileShareConfig, _Mapping]]]=..., tier: _Optional[_Union[FilestoreInitializeParams.Tier, str]]=..., filestore: _Optional[str]=..., description: _Optional[str]=..., protocol: _Optional[_Union[FilestoreInitializeParams.Protocol, str]]=...) -> None:
        ...

class GcsInitializeParams(_message.Message):
    __slots__ = ('autoclass', 'storage_class', 'bucket', 'hierarchical_namespace')

    class StorageClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STORAGE_CLASS_UNSPECIFIED: _ClassVar[GcsInitializeParams.StorageClass]
        STORAGE_CLASS_STANDARD: _ClassVar[GcsInitializeParams.StorageClass]
        STORAGE_CLASS_NEARLINE: _ClassVar[GcsInitializeParams.StorageClass]
        STORAGE_CLASS_COLDLINE: _ClassVar[GcsInitializeParams.StorageClass]
        STORAGE_CLASS_ARCHIVE: _ClassVar[GcsInitializeParams.StorageClass]
    STORAGE_CLASS_UNSPECIFIED: GcsInitializeParams.StorageClass
    STORAGE_CLASS_STANDARD: GcsInitializeParams.StorageClass
    STORAGE_CLASS_NEARLINE: GcsInitializeParams.StorageClass
    STORAGE_CLASS_COLDLINE: GcsInitializeParams.StorageClass
    STORAGE_CLASS_ARCHIVE: GcsInitializeParams.StorageClass
    AUTOCLASS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    HIERARCHICAL_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    autoclass: GcsAutoclassConfig
    storage_class: GcsInitializeParams.StorageClass
    bucket: str
    hierarchical_namespace: GcsHierarchicalNamespaceConfig

    def __init__(self, autoclass: _Optional[_Union[GcsAutoclassConfig, _Mapping]]=..., storage_class: _Optional[_Union[GcsInitializeParams.StorageClass, str]]=..., bucket: _Optional[str]=..., hierarchical_namespace: _Optional[_Union[GcsHierarchicalNamespaceConfig, _Mapping]]=...) -> None:
        ...

class LustreInitializeParams(_message.Message):
    __slots__ = ('lustre', 'description', 'filesystem', 'capacity_gb')
    LUSTRE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FILESYSTEM_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_GB_FIELD_NUMBER: _ClassVar[int]
    lustre: str
    description: str
    filesystem: str
    capacity_gb: int

    def __init__(self, lustre: _Optional[str]=..., description: _Optional[str]=..., filesystem: _Optional[str]=..., capacity_gb: _Optional[int]=...) -> None:
        ...

class StorageSource(_message.Message):
    __slots__ = ('filestore', 'bucket', 'lustre')
    FILESTORE_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    LUSTRE_FIELD_NUMBER: _ClassVar[int]
    filestore: str
    bucket: str
    lustre: str

    def __init__(self, filestore: _Optional[str]=..., bucket: _Optional[str]=..., lustre: _Optional[str]=...) -> None:
        ...

class Compute(_message.Message):
    __slots__ = ('resource_requests', 'atm_tags')
    RESOURCE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    ATM_TAGS_FIELD_NUMBER: _ClassVar[int]
    resource_requests: _containers.RepeatedCompositeFieldContainer[ResourceRequest]
    atm_tags: _containers.RepeatedCompositeFieldContainer[AtmTag]

    def __init__(self, resource_requests: _Optional[_Iterable[_Union[ResourceRequest, _Mapping]]]=..., atm_tags: _Optional[_Iterable[_Union[AtmTag, _Mapping]]]=...) -> None:
        ...

class ResourceRequest(_message.Message):
    __slots__ = ('id', 'zone', 'machine_type', 'guest_accelerators', 'disks', 'max_run_duration', 'provisioning_model', 'reservation_affinity', 'termination_action')

    class ProvisioningModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PROVISIONING_MODEL_UNSPECIFIED: _ClassVar[ResourceRequest.ProvisioningModel]
        PROVISIONING_MODEL_STANDARD: _ClassVar[ResourceRequest.ProvisioningModel]
        PROVISIONING_MODEL_SPOT: _ClassVar[ResourceRequest.ProvisioningModel]
        PROVISIONING_MODEL_FLEX_START: _ClassVar[ResourceRequest.ProvisioningModel]
        PROVISIONING_MODEL_RESERVATION_BOUND: _ClassVar[ResourceRequest.ProvisioningModel]
    PROVISIONING_MODEL_UNSPECIFIED: ResourceRequest.ProvisioningModel
    PROVISIONING_MODEL_STANDARD: ResourceRequest.ProvisioningModel
    PROVISIONING_MODEL_SPOT: ResourceRequest.ProvisioningModel
    PROVISIONING_MODEL_FLEX_START: ResourceRequest.ProvisioningModel
    PROVISIONING_MODEL_RESERVATION_BOUND: ResourceRequest.ProvisioningModel

    class TerminationAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TERMINATION_ACTION_UNSPECIFIED: _ClassVar[ResourceRequest.TerminationAction]
        TERMINATION_ACTION_STOP: _ClassVar[ResourceRequest.TerminationAction]
        TERMINATION_ACTION_DELETE: _ClassVar[ResourceRequest.TerminationAction]
    TERMINATION_ACTION_UNSPECIFIED: ResourceRequest.TerminationAction
    TERMINATION_ACTION_STOP: ResourceRequest.TerminationAction
    TERMINATION_ACTION_DELETE: ResourceRequest.TerminationAction
    ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GUEST_ACCELERATORS_FIELD_NUMBER: _ClassVar[int]
    DISKS_FIELD_NUMBER: _ClassVar[int]
    MAX_RUN_DURATION_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_MODEL_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    zone: str
    machine_type: str
    guest_accelerators: _containers.RepeatedCompositeFieldContainer[GuestAccelerator]
    disks: _containers.RepeatedCompositeFieldContainer[Disk]
    max_run_duration: int
    provisioning_model: ResourceRequest.ProvisioningModel
    reservation_affinity: ReservationAffinity
    termination_action: ResourceRequest.TerminationAction

    def __init__(self, id: _Optional[str]=..., zone: _Optional[str]=..., machine_type: _Optional[str]=..., guest_accelerators: _Optional[_Iterable[_Union[GuestAccelerator, _Mapping]]]=..., disks: _Optional[_Iterable[_Union[Disk, _Mapping]]]=..., max_run_duration: _Optional[int]=..., provisioning_model: _Optional[_Union[ResourceRequest.ProvisioningModel, str]]=..., reservation_affinity: _Optional[_Union[ReservationAffinity, _Mapping]]=..., termination_action: _Optional[_Union[ResourceRequest.TerminationAction, str]]=...) -> None:
        ...

class GuestAccelerator(_message.Message):
    __slots__ = ('accelerator_type', 'count')
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    accelerator_type: str
    count: int

    def __init__(self, accelerator_type: _Optional[str]=..., count: _Optional[int]=...) -> None:
        ...

class NewDWSFlexInstancesConfig(_message.Message):
    __slots__ = ('zone', 'machine_type', 'max_duration', 'atm_tags', 'termination_action', 'boot_disk')

    class TerminationAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TERMINATION_ACTION_UNSPECIFIED: _ClassVar[NewDWSFlexInstancesConfig.TerminationAction]
        STOP: _ClassVar[NewDWSFlexInstancesConfig.TerminationAction]
        DELETE: _ClassVar[NewDWSFlexInstancesConfig.TerminationAction]
    TERMINATION_ACTION_UNSPECIFIED: NewDWSFlexInstancesConfig.TerminationAction
    STOP: NewDWSFlexInstancesConfig.TerminationAction
    DELETE: NewDWSFlexInstancesConfig.TerminationAction

    class AtmTagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    ZONE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    ATM_TAGS_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_FIELD_NUMBER: _ClassVar[int]
    zone: str
    machine_type: str
    max_duration: _duration_pb2.Duration
    atm_tags: _containers.ScalarMap[str, str]
    termination_action: NewDWSFlexInstancesConfig.TerminationAction
    boot_disk: Disk

    def __init__(self, zone: _Optional[str]=..., machine_type: _Optional[str]=..., max_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., atm_tags: _Optional[_Mapping[str, str]]=..., termination_action: _Optional[_Union[NewDWSFlexInstancesConfig.TerminationAction, str]]=..., boot_disk: _Optional[_Union[Disk, _Mapping]]=...) -> None:
        ...

class ReservationAffinity(_message.Message):
    __slots__ = ('type', 'key', 'values')

    class ReservationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESERVATION_TYPE_UNSPECIFIED: _ClassVar[ReservationAffinity.ReservationType]
        RESERVATION_TYPE_NO_RESERVATION: _ClassVar[ReservationAffinity.ReservationType]
        RESERVATION_TYPE_ANY_RESERVATION: _ClassVar[ReservationAffinity.ReservationType]
        RESERVATION_TYPE_SPECIFIC_RESERVATION: _ClassVar[ReservationAffinity.ReservationType]
    RESERVATION_TYPE_UNSPECIFIED: ReservationAffinity.ReservationType
    RESERVATION_TYPE_NO_RESERVATION: ReservationAffinity.ReservationType
    RESERVATION_TYPE_ANY_RESERVATION: ReservationAffinity.ReservationType
    RESERVATION_TYPE_SPECIFIC_RESERVATION: ReservationAffinity.ReservationType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    type: ReservationAffinity.ReservationType
    key: str
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, type: _Optional[_Union[ReservationAffinity.ReservationType, str]]=..., key: _Optional[str]=..., values: _Optional[_Iterable[str]]=...) -> None:
        ...