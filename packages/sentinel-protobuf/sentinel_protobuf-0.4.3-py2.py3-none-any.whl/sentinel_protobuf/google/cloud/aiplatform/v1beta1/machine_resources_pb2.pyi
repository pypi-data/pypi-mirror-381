from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.aiplatform.v1beta1 import accelerator_type_pb2 as _accelerator_type_pb2
from google.cloud.aiplatform.v1beta1 import reservation_affinity_pb2 as _reservation_affinity_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MachineSpec(_message.Message):
    __slots__ = ('machine_type', 'accelerator_type', 'accelerator_count', 'gpu_partition_size', 'tpu_topology', 'multihost_gpu_node_count', 'reservation_affinity')
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCELERATOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    GPU_PARTITION_SIZE_FIELD_NUMBER: _ClassVar[int]
    TPU_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    MULTIHOST_GPU_NODE_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_AFFINITY_FIELD_NUMBER: _ClassVar[int]
    machine_type: str
    accelerator_type: _accelerator_type_pb2.AcceleratorType
    accelerator_count: int
    gpu_partition_size: str
    tpu_topology: str
    multihost_gpu_node_count: int
    reservation_affinity: _reservation_affinity_pb2.ReservationAffinity

    def __init__(self, machine_type: _Optional[str]=..., accelerator_type: _Optional[_Union[_accelerator_type_pb2.AcceleratorType, str]]=..., accelerator_count: _Optional[int]=..., gpu_partition_size: _Optional[str]=..., tpu_topology: _Optional[str]=..., multihost_gpu_node_count: _Optional[int]=..., reservation_affinity: _Optional[_Union[_reservation_affinity_pb2.ReservationAffinity, _Mapping]]=...) -> None:
        ...

class DedicatedResources(_message.Message):
    __slots__ = ('machine_spec', 'min_replica_count', 'max_replica_count', 'required_replica_count', 'autoscaling_metric_specs', 'spot', 'flex_start')
    MACHINE_SPEC_FIELD_NUMBER: _ClassVar[int]
    MIN_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUTOSCALING_METRIC_SPECS_FIELD_NUMBER: _ClassVar[int]
    SPOT_FIELD_NUMBER: _ClassVar[int]
    FLEX_START_FIELD_NUMBER: _ClassVar[int]
    machine_spec: MachineSpec
    min_replica_count: int
    max_replica_count: int
    required_replica_count: int
    autoscaling_metric_specs: _containers.RepeatedCompositeFieldContainer[AutoscalingMetricSpec]
    spot: bool
    flex_start: FlexStart

    def __init__(self, machine_spec: _Optional[_Union[MachineSpec, _Mapping]]=..., min_replica_count: _Optional[int]=..., max_replica_count: _Optional[int]=..., required_replica_count: _Optional[int]=..., autoscaling_metric_specs: _Optional[_Iterable[_Union[AutoscalingMetricSpec, _Mapping]]]=..., spot: bool=..., flex_start: _Optional[_Union[FlexStart, _Mapping]]=...) -> None:
        ...

class AutomaticResources(_message.Message):
    __slots__ = ('min_replica_count', 'max_replica_count')
    MIN_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    min_replica_count: int
    max_replica_count: int

    def __init__(self, min_replica_count: _Optional[int]=..., max_replica_count: _Optional[int]=...) -> None:
        ...

class BatchDedicatedResources(_message.Message):
    __slots__ = ('machine_spec', 'starting_replica_count', 'max_replica_count', 'flex_start', 'spot')
    MACHINE_SPEC_FIELD_NUMBER: _ClassVar[int]
    STARTING_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_REPLICA_COUNT_FIELD_NUMBER: _ClassVar[int]
    FLEX_START_FIELD_NUMBER: _ClassVar[int]
    SPOT_FIELD_NUMBER: _ClassVar[int]
    machine_spec: MachineSpec
    starting_replica_count: int
    max_replica_count: int
    flex_start: FlexStart
    spot: bool

    def __init__(self, machine_spec: _Optional[_Union[MachineSpec, _Mapping]]=..., starting_replica_count: _Optional[int]=..., max_replica_count: _Optional[int]=..., flex_start: _Optional[_Union[FlexStart, _Mapping]]=..., spot: bool=...) -> None:
        ...

class ResourcesConsumed(_message.Message):
    __slots__ = ('replica_hours',)
    REPLICA_HOURS_FIELD_NUMBER: _ClassVar[int]
    replica_hours: float

    def __init__(self, replica_hours: _Optional[float]=...) -> None:
        ...

class DiskSpec(_message.Message):
    __slots__ = ('boot_disk_type', 'boot_disk_size_gb')
    BOOT_DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    BOOT_DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    boot_disk_type: str
    boot_disk_size_gb: int

    def __init__(self, boot_disk_type: _Optional[str]=..., boot_disk_size_gb: _Optional[int]=...) -> None:
        ...

class PersistentDiskSpec(_message.Message):
    __slots__ = ('disk_type', 'disk_size_gb')
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISK_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    disk_type: str
    disk_size_gb: int

    def __init__(self, disk_type: _Optional[str]=..., disk_size_gb: _Optional[int]=...) -> None:
        ...

class NfsMount(_message.Message):
    __slots__ = ('server', 'path', 'mount_point')
    SERVER_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    MOUNT_POINT_FIELD_NUMBER: _ClassVar[int]
    server: str
    path: str
    mount_point: str

    def __init__(self, server: _Optional[str]=..., path: _Optional[str]=..., mount_point: _Optional[str]=...) -> None:
        ...

class AutoscalingMetricSpec(_message.Message):
    __slots__ = ('metric_name', 'target', 'monitored_resource_labels')

    class MonitoredResourceLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    METRIC_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    MONITORED_RESOURCE_LABELS_FIELD_NUMBER: _ClassVar[int]
    metric_name: str
    target: int
    monitored_resource_labels: _containers.ScalarMap[str, str]

    def __init__(self, metric_name: _Optional[str]=..., target: _Optional[int]=..., monitored_resource_labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ShieldedVmConfig(_message.Message):
    __slots__ = ('enable_secure_boot',)
    ENABLE_SECURE_BOOT_FIELD_NUMBER: _ClassVar[int]
    enable_secure_boot: bool

    def __init__(self, enable_secure_boot: bool=...) -> None:
        ...

class FlexStart(_message.Message):
    __slots__ = ('max_runtime_duration',)
    MAX_RUNTIME_DURATION_FIELD_NUMBER: _ClassVar[int]
    max_runtime_duration: _duration_pb2.Duration

    def __init__(self, max_runtime_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...