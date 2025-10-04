from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.backupdr.v1 import backupvault_gce_pb2 as _backupvault_gce_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DiskTargetEnvironment(_message.Message):
    __slots__ = ('project', 'zone')
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    project: str
    zone: str

    def __init__(self, project: _Optional[str]=..., zone: _Optional[str]=...) -> None:
        ...

class RegionDiskTargetEnvironment(_message.Message):
    __slots__ = ('project', 'region', 'replica_zones')
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ZONES_FIELD_NUMBER: _ClassVar[int]
    project: str
    region: str
    replica_zones: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, project: _Optional[str]=..., region: _Optional[str]=..., replica_zones: _Optional[_Iterable[str]]=...) -> None:
        ...

class DiskRestoreProperties(_message.Message):
    __slots__ = ('name', 'description', 'size_gb', 'licenses', 'guest_os_feature', 'disk_encryption_key', 'physical_block_size_bytes', 'provisioned_iops', 'provisioned_throughput', 'enable_confidential_compute', 'storage_pool', 'access_mode', 'architecture', 'resource_policy', 'type', 'labels', 'resource_manager_tags')

    class AccessMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        READ_WRITE_SINGLE: _ClassVar[DiskRestoreProperties.AccessMode]
        READ_WRITE_MANY: _ClassVar[DiskRestoreProperties.AccessMode]
        READ_ONLY_MANY: _ClassVar[DiskRestoreProperties.AccessMode]
    READ_WRITE_SINGLE: DiskRestoreProperties.AccessMode
    READ_WRITE_MANY: DiskRestoreProperties.AccessMode
    READ_ONLY_MANY: DiskRestoreProperties.AccessMode

    class Architecture(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARCHITECTURE_UNSPECIFIED: _ClassVar[DiskRestoreProperties.Architecture]
        X86_64: _ClassVar[DiskRestoreProperties.Architecture]
        ARM64: _ClassVar[DiskRestoreProperties.Architecture]
    ARCHITECTURE_UNSPECIFIED: DiskRestoreProperties.Architecture
    X86_64: DiskRestoreProperties.Architecture
    ARM64: DiskRestoreProperties.Architecture

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class ResourceManagerTagsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    LICENSES_FIELD_NUMBER: _ClassVar[int]
    GUEST_OS_FEATURE_FIELD_NUMBER: _ClassVar[int]
    DISK_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_BLOCK_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    PROVISIONED_IOPS_FIELD_NUMBER: _ClassVar[int]
    PROVISIONED_THROUGHPUT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CONFIDENTIAL_COMPUTE_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POOL_FIELD_NUMBER: _ClassVar[int]
    ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_POLICY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_MANAGER_TAGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    size_gb: int
    licenses: _containers.RepeatedScalarFieldContainer[str]
    guest_os_feature: _containers.RepeatedCompositeFieldContainer[_backupvault_gce_pb2.GuestOsFeature]
    disk_encryption_key: _backupvault_gce_pb2.CustomerEncryptionKey
    physical_block_size_bytes: int
    provisioned_iops: int
    provisioned_throughput: int
    enable_confidential_compute: bool
    storage_pool: str
    access_mode: DiskRestoreProperties.AccessMode
    architecture: DiskRestoreProperties.Architecture
    resource_policy: _containers.RepeatedScalarFieldContainer[str]
    type: str
    labels: _containers.ScalarMap[str, str]
    resource_manager_tags: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., size_gb: _Optional[int]=..., licenses: _Optional[_Iterable[str]]=..., guest_os_feature: _Optional[_Iterable[_Union[_backupvault_gce_pb2.GuestOsFeature, _Mapping]]]=..., disk_encryption_key: _Optional[_Union[_backupvault_gce_pb2.CustomerEncryptionKey, _Mapping]]=..., physical_block_size_bytes: _Optional[int]=..., provisioned_iops: _Optional[int]=..., provisioned_throughput: _Optional[int]=..., enable_confidential_compute: bool=..., storage_pool: _Optional[str]=..., access_mode: _Optional[_Union[DiskRestoreProperties.AccessMode, str]]=..., architecture: _Optional[_Union[DiskRestoreProperties.Architecture, str]]=..., resource_policy: _Optional[_Iterable[str]]=..., type: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., resource_manager_tags: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class DiskBackupProperties(_message.Message):
    __slots__ = ('description', 'licenses', 'guest_os_feature', 'architecture', 'type', 'size_gb', 'region', 'zone', 'replica_zones', 'source_disk')

    class Architecture(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARCHITECTURE_UNSPECIFIED: _ClassVar[DiskBackupProperties.Architecture]
        X86_64: _ClassVar[DiskBackupProperties.Architecture]
        ARM64: _ClassVar[DiskBackupProperties.Architecture]
    ARCHITECTURE_UNSPECIFIED: DiskBackupProperties.Architecture
    X86_64: DiskBackupProperties.Architecture
    ARM64: DiskBackupProperties.Architecture
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LICENSES_FIELD_NUMBER: _ClassVar[int]
    GUEST_OS_FEATURE_FIELD_NUMBER: _ClassVar[int]
    ARCHITECTURE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    REPLICA_ZONES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DISK_FIELD_NUMBER: _ClassVar[int]
    description: str
    licenses: _containers.RepeatedScalarFieldContainer[str]
    guest_os_feature: _containers.RepeatedCompositeFieldContainer[_backupvault_gce_pb2.GuestOsFeature]
    architecture: DiskBackupProperties.Architecture
    type: str
    size_gb: int
    region: str
    zone: str
    replica_zones: _containers.RepeatedScalarFieldContainer[str]
    source_disk: str

    def __init__(self, description: _Optional[str]=..., licenses: _Optional[_Iterable[str]]=..., guest_os_feature: _Optional[_Iterable[_Union[_backupvault_gce_pb2.GuestOsFeature, _Mapping]]]=..., architecture: _Optional[_Union[DiskBackupProperties.Architecture, str]]=..., type: _Optional[str]=..., size_gb: _Optional[int]=..., region: _Optional[str]=..., zone: _Optional[str]=..., replica_zones: _Optional[_Iterable[str]]=..., source_disk: _Optional[str]=...) -> None:
        ...

class DiskDataSourceProperties(_message.Message):
    __slots__ = ('name', 'description', 'type', 'size_gb')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    type: str
    size_gb: int

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., type: _Optional[str]=..., size_gb: _Optional[int]=...) -> None:
        ...