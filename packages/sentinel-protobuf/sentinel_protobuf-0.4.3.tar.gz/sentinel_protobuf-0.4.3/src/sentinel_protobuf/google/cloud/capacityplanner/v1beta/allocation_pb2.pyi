from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Allocation(_message.Message):
    __slots__ = ('specific_allocation', 'id', 'create_time', 'zone', 'description', 'allocation', 'owner_project_id', 'status', 'share_settings', 'auto_delete_time')

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[Allocation.Status]
        INVALID: _ClassVar[Allocation.Status]
        CREATING: _ClassVar[Allocation.Status]
        READY: _ClassVar[Allocation.Status]
        DELETING: _ClassVar[Allocation.Status]
        UPDATING: _ClassVar[Allocation.Status]
    STATUS_UNSPECIFIED: Allocation.Status
    INVALID: Allocation.Status
    CREATING: Allocation.Status
    READY: Allocation.Status
    DELETING: Allocation.Status
    UPDATING: Allocation.Status

    class SpecificSKUAllocation(_message.Message):
        __slots__ = ('instance_properties', 'count', 'used_count', 'assured_count')

        class AllocatedInstanceProperties(_message.Message):
            __slots__ = ('machine_type', 'guest_accelerator', 'min_cpu_platform', 'local_ssd')

            class AcceleratorConfig(_message.Message):
                __slots__ = ('type', 'count')
                TYPE_FIELD_NUMBER: _ClassVar[int]
                COUNT_FIELD_NUMBER: _ClassVar[int]
                type: str
                count: int

                def __init__(self, type: _Optional[str]=..., count: _Optional[int]=...) -> None:
                    ...

            class AllocatedDisk(_message.Message):
                __slots__ = ('disk_size_gb', 'disk_interface')

                class DiskInterface(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    DISK_INTERFACE_UNSPECIFIED: _ClassVar[Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface]
                    SCSI: _ClassVar[Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface]
                    NVME: _ClassVar[Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface]
                    NVDIMM: _ClassVar[Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface]
                    ISCSI: _ClassVar[Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface]
                DISK_INTERFACE_UNSPECIFIED: Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface
                SCSI: Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface
                NVME: Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface
                NVDIMM: Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface
                ISCSI: Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface
                DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
                DISK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
                disk_size_gb: int
                disk_interface: Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface

                def __init__(self, disk_size_gb: _Optional[int]=..., disk_interface: _Optional[_Union[Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface, str]]=...) -> None:
                    ...
            MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
            GUEST_ACCELERATOR_FIELD_NUMBER: _ClassVar[int]
            MIN_CPU_PLATFORM_FIELD_NUMBER: _ClassVar[int]
            LOCAL_SSD_FIELD_NUMBER: _ClassVar[int]
            machine_type: str
            guest_accelerator: _containers.RepeatedCompositeFieldContainer[Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AcceleratorConfig]
            min_cpu_platform: str
            local_ssd: _containers.RepeatedCompositeFieldContainer[Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk]

            def __init__(self, machine_type: _Optional[str]=..., guest_accelerator: _Optional[_Iterable[_Union[Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AcceleratorConfig, _Mapping]]]=..., min_cpu_platform: _Optional[str]=..., local_ssd: _Optional[_Iterable[_Union[Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk, _Mapping]]]=...) -> None:
                ...
        INSTANCE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        USED_COUNT_FIELD_NUMBER: _ClassVar[int]
        ASSURED_COUNT_FIELD_NUMBER: _ClassVar[int]
        instance_properties: Allocation.SpecificSKUAllocation.AllocatedInstanceProperties
        count: int
        used_count: int
        assured_count: int

        def __init__(self, instance_properties: _Optional[_Union[Allocation.SpecificSKUAllocation.AllocatedInstanceProperties, _Mapping]]=..., count: _Optional[int]=..., used_count: _Optional[int]=..., assured_count: _Optional[int]=...) -> None:
            ...

    class ShareSettings(_message.Message):
        __slots__ = ('share_type', 'projects')

        class ShareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SHARE_TYPE_UNSPECIFIED: _ClassVar[Allocation.ShareSettings.ShareType]
            ORGANIZATION: _ClassVar[Allocation.ShareSettings.ShareType]
            SPECIFIC_PROJECTS: _ClassVar[Allocation.ShareSettings.ShareType]
            LOCAL: _ClassVar[Allocation.ShareSettings.ShareType]
            DIRECT_PROJECTS_UNDER_SPECIFIC_FOLDERS: _ClassVar[Allocation.ShareSettings.ShareType]
        SHARE_TYPE_UNSPECIFIED: Allocation.ShareSettings.ShareType
        ORGANIZATION: Allocation.ShareSettings.ShareType
        SPECIFIC_PROJECTS: Allocation.ShareSettings.ShareType
        LOCAL: Allocation.ShareSettings.ShareType
        DIRECT_PROJECTS_UNDER_SPECIFIC_FOLDERS: Allocation.ShareSettings.ShareType
        SHARE_TYPE_FIELD_NUMBER: _ClassVar[int]
        PROJECTS_FIELD_NUMBER: _ClassVar[int]
        share_type: Allocation.ShareSettings.ShareType
        projects: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, share_type: _Optional[_Union[Allocation.ShareSettings.ShareType, str]]=..., projects: _Optional[_Iterable[str]]=...) -> None:
            ...
    SPECIFIC_ALLOCATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALLOCATION_FIELD_NUMBER: _ClassVar[int]
    OWNER_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SHARE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    AUTO_DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    specific_allocation: Allocation.SpecificSKUAllocation
    id: int
    create_time: _timestamp_pb2.Timestamp
    zone: str
    description: str
    allocation: str
    owner_project_id: str
    status: Allocation.Status
    share_settings: Allocation.ShareSettings
    auto_delete_time: _timestamp_pb2.Timestamp

    def __init__(self, specific_allocation: _Optional[_Union[Allocation.SpecificSKUAllocation, _Mapping]]=..., id: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., zone: _Optional[str]=..., description: _Optional[str]=..., allocation: _Optional[str]=..., owner_project_id: _Optional[str]=..., status: _Optional[_Union[Allocation.Status, str]]=..., share_settings: _Optional[_Union[Allocation.ShareSettings, _Mapping]]=..., auto_delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...