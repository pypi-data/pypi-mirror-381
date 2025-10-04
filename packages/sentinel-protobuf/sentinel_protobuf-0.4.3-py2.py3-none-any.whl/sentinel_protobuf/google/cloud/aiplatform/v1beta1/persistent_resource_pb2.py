"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/persistent_resource.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_machine__resources__pb2
from .....google.cloud.aiplatform.v1beta1 import service_networking_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_service__networking__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/aiplatform/v1beta1/persistent_resource.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a7google/cloud/aiplatform/v1beta1/machine_resources.proto\x1a8google/cloud/aiplatform/v1beta1/service_networking.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\x8c\n\n\x12PersistentResource\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12J\n\x0eresource_pools\x18\x04 \x03(\x0b2-.google.cloud.aiplatform.v1beta1.ResourcePoolB\x03\xe0A\x02\x12M\n\x05state\x18\x05 \x01(\x0e29.google.cloud.aiplatform.v1beta1.PersistentResource.StateB\x03\xe0A\x03\x12&\n\x05error\x18\x06 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\nstart_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12T\n\x06labels\x18\n \x03(\x0b2?.google.cloud.aiplatform.v1beta1.PersistentResource.LabelsEntryB\x03\xe0A\x01\x127\n\x07network\x18\x0b \x01(\tB&\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Network\x12V\n\x14psc_interface_config\x18\x11 \x01(\x0b23.google.cloud.aiplatform.v1beta1.PscInterfaceConfigB\x03\xe0A\x01\x12M\n\x0fencryption_spec\x18\x0c \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpecB\x03\xe0A\x01\x12X\n\x15resource_runtime_spec\x18\r \x01(\x0b24.google.cloud.aiplatform.v1beta1.ResourceRuntimeSpecB\x03\xe0A\x01\x12O\n\x10resource_runtime\x18\x0e \x01(\x0b20.google.cloud.aiplatform.v1beta1.ResourceRuntimeB\x03\xe0A\x03\x12\x1f\n\x12reserved_ip_ranges\x18\x0f \x03(\tB\x03\xe0A\x01\x12\x1a\n\rsatisfies_pzs\x18\x12 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x13 \x01(\x08B\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"s\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0b\n\x07RUNNING\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\t\n\x05ERROR\x10\x05\x12\r\n\tREBOOTING\x10\x06\x12\x0c\n\x08UPDATING\x10\x07:\x85\x01\xeaA\x81\x01\n,aiplatform.googleapis.com/PersistentResource\x12Qprojects/{project}/locations/{location}/persistentResources/{persistent_resource}"\xea\x03\n\x0cResourcePool\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x05\x12J\n\x0cmachine_spec\x18\x02 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.MachineSpecB\x06\xe0A\x02\xe0A\x05\x12\x1f\n\rreplica_count\x18\x03 \x01(\x03B\x03\xe0A\x01H\x00\x88\x01\x01\x12A\n\tdisk_spec\x18\x04 \x01(\x0b2).google.cloud.aiplatform.v1beta1.DiskSpecB\x03\xe0A\x01\x12\x1f\n\x12used_replica_count\x18\x06 \x01(\x03B\x03\xe0A\x03\x12\\\n\x10autoscaling_spec\x18\x07 \x01(\x0b2=.google.cloud.aiplatform.v1beta1.ResourcePool.AutoscalingSpecB\x03\xe0A\x01\x1a\x87\x01\n\x0fAutoscalingSpec\x12#\n\x11min_replica_count\x18\x01 \x01(\x03B\x03\xe0A\x01H\x00\x88\x01\x01\x12#\n\x11max_replica_count\x18\x02 \x01(\x03B\x03\xe0A\x01H\x01\x88\x01\x01B\x14\n\x12_min_replica_countB\x14\n\x12_max_replica_countB\x10\n\x0e_replica_count"\xae\x01\n\x13ResourceRuntimeSpec\x12V\n\x14service_account_spec\x18\x02 \x01(\x0b23.google.cloud.aiplatform.v1beta1.ServiceAccountSpecB\x03\xe0A\x01\x12?\n\x08ray_spec\x18\x01 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.RaySpecB\x03\xe0A\x01"\xc6\x03\n\x07RaySpec\x12\x16\n\timage_uri\x18\x01 \x01(\tB\x03\xe0A\x01\x12B\n\nnfs_mounts\x18\x0b \x03(\x0b2).google.cloud.aiplatform.v1beta1.NfsMountB\x03\xe0A\x01\x12c\n\x14resource_pool_images\x18\x06 \x03(\x0b2@.google.cloud.aiplatform.v1beta1.RaySpec.ResourcePoolImagesEntryB\x03\xe0A\x01\x12\'\n\x1ahead_node_resource_pool_id\x18\x07 \x01(\tB\x03\xe0A\x01\x12L\n\x0fray_metric_spec\x18\x08 \x01(\x0b2..google.cloud.aiplatform.v1beta1.RayMetricSpecB\x03\xe0A\x01\x12H\n\rray_logs_spec\x18\n \x01(\x0b2,.google.cloud.aiplatform.v1beta1.RayLogsSpecB\x03\xe0A\x01\x1a9\n\x17ResourcePoolImagesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x80\x02\n\x0fResourceRuntime\x12Z\n\x0baccess_uris\x18\x01 \x03(\x0b2@.google.cloud.aiplatform.v1beta1.ResourceRuntime.AccessUrisEntryB\x03\xe0A\x03\x12^\n\x19notebook_runtime_template\x18\x02 \x01(\tB;\x18\x01\xe0A\x03\xfaA3\n1aiplatform.googleapis.com/NotebookRuntimeTemplate\x1a1\n\x0fAccessUrisEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"^\n\x12ServiceAccountSpec\x12*\n\x1denable_custom_service_account\x18\x01 \x01(\x08B\x03\xe0A\x02\x12\x1c\n\x0fservice_account\x18\x02 \x01(\tB\x03\xe0A\x01"&\n\rRayMetricSpec\x12\x15\n\x08disabled\x18\x01 \x01(\x08B\x03\xe0A\x01"$\n\x0bRayLogsSpec\x12\x15\n\x08disabled\x18\x01 \x01(\x08B\x03\xe0A\x01B\xee\x01\n#com.google.cloud.aiplatform.v1beta1B\x17PersistentResourceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.persistent_resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x17PersistentResourceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_PERSISTENTRESOURCE_LABELSENTRY']._loaded_options = None
    _globals['_PERSISTENTRESOURCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['name']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['display_name']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['resource_pools']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['resource_pools']._serialized_options = b'\xe0A\x02'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['state']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['error']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['start_time']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['labels']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['network']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['network']._serialized_options = b'\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Network'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['psc_interface_config']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['psc_interface_config']._serialized_options = b'\xe0A\x01'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['encryption_spec']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['encryption_spec']._serialized_options = b'\xe0A\x01'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['resource_runtime_spec']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['resource_runtime_spec']._serialized_options = b'\xe0A\x01'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['resource_runtime']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['resource_runtime']._serialized_options = b'\xe0A\x03'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['reserved_ip_ranges']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['reserved_ip_ranges']._serialized_options = b'\xe0A\x01'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_PERSISTENTRESOURCE'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_PERSISTENTRESOURCE'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_PERSISTENTRESOURCE']._loaded_options = None
    _globals['_PERSISTENTRESOURCE']._serialized_options = b'\xeaA\x81\x01\n,aiplatform.googleapis.com/PersistentResource\x12Qprojects/{project}/locations/{location}/persistentResources/{persistent_resource}'
    _globals['_RESOURCEPOOL_AUTOSCALINGSPEC'].fields_by_name['min_replica_count']._loaded_options = None
    _globals['_RESOURCEPOOL_AUTOSCALINGSPEC'].fields_by_name['min_replica_count']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEPOOL_AUTOSCALINGSPEC'].fields_by_name['max_replica_count']._loaded_options = None
    _globals['_RESOURCEPOOL_AUTOSCALINGSPEC'].fields_by_name['max_replica_count']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEPOOL'].fields_by_name['id']._loaded_options = None
    _globals['_RESOURCEPOOL'].fields_by_name['id']._serialized_options = b'\xe0A\x05'
    _globals['_RESOURCEPOOL'].fields_by_name['machine_spec']._loaded_options = None
    _globals['_RESOURCEPOOL'].fields_by_name['machine_spec']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_RESOURCEPOOL'].fields_by_name['replica_count']._loaded_options = None
    _globals['_RESOURCEPOOL'].fields_by_name['replica_count']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEPOOL'].fields_by_name['disk_spec']._loaded_options = None
    _globals['_RESOURCEPOOL'].fields_by_name['disk_spec']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEPOOL'].fields_by_name['used_replica_count']._loaded_options = None
    _globals['_RESOURCEPOOL'].fields_by_name['used_replica_count']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEPOOL'].fields_by_name['autoscaling_spec']._loaded_options = None
    _globals['_RESOURCEPOOL'].fields_by_name['autoscaling_spec']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCERUNTIMESPEC'].fields_by_name['service_account_spec']._loaded_options = None
    _globals['_RESOURCERUNTIMESPEC'].fields_by_name['service_account_spec']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCERUNTIMESPEC'].fields_by_name['ray_spec']._loaded_options = None
    _globals['_RESOURCERUNTIMESPEC'].fields_by_name['ray_spec']._serialized_options = b'\xe0A\x01'
    _globals['_RAYSPEC_RESOURCEPOOLIMAGESENTRY']._loaded_options = None
    _globals['_RAYSPEC_RESOURCEPOOLIMAGESENTRY']._serialized_options = b'8\x01'
    _globals['_RAYSPEC'].fields_by_name['image_uri']._loaded_options = None
    _globals['_RAYSPEC'].fields_by_name['image_uri']._serialized_options = b'\xe0A\x01'
    _globals['_RAYSPEC'].fields_by_name['nfs_mounts']._loaded_options = None
    _globals['_RAYSPEC'].fields_by_name['nfs_mounts']._serialized_options = b'\xe0A\x01'
    _globals['_RAYSPEC'].fields_by_name['resource_pool_images']._loaded_options = None
    _globals['_RAYSPEC'].fields_by_name['resource_pool_images']._serialized_options = b'\xe0A\x01'
    _globals['_RAYSPEC'].fields_by_name['head_node_resource_pool_id']._loaded_options = None
    _globals['_RAYSPEC'].fields_by_name['head_node_resource_pool_id']._serialized_options = b'\xe0A\x01'
    _globals['_RAYSPEC'].fields_by_name['ray_metric_spec']._loaded_options = None
    _globals['_RAYSPEC'].fields_by_name['ray_metric_spec']._serialized_options = b'\xe0A\x01'
    _globals['_RAYSPEC'].fields_by_name['ray_logs_spec']._loaded_options = None
    _globals['_RAYSPEC'].fields_by_name['ray_logs_spec']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCERUNTIME_ACCESSURISENTRY']._loaded_options = None
    _globals['_RESOURCERUNTIME_ACCESSURISENTRY']._serialized_options = b'8\x01'
    _globals['_RESOURCERUNTIME'].fields_by_name['access_uris']._loaded_options = None
    _globals['_RESOURCERUNTIME'].fields_by_name['access_uris']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCERUNTIME'].fields_by_name['notebook_runtime_template']._loaded_options = None
    _globals['_RESOURCERUNTIME'].fields_by_name['notebook_runtime_template']._serialized_options = b'\x18\x01\xe0A\x03\xfaA3\n1aiplatform.googleapis.com/NotebookRuntimeTemplate'
    _globals['_SERVICEACCOUNTSPEC'].fields_by_name['enable_custom_service_account']._loaded_options = None
    _globals['_SERVICEACCOUNTSPEC'].fields_by_name['enable_custom_service_account']._serialized_options = b'\xe0A\x02'
    _globals['_SERVICEACCOUNTSPEC'].fields_by_name['service_account']._loaded_options = None
    _globals['_SERVICEACCOUNTSPEC'].fields_by_name['service_account']._serialized_options = b'\xe0A\x01'
    _globals['_RAYMETRICSPEC'].fields_by_name['disabled']._loaded_options = None
    _globals['_RAYMETRICSPEC'].fields_by_name['disabled']._serialized_options = b'\xe0A\x01'
    _globals['_RAYLOGSSPEC'].fields_by_name['disabled']._loaded_options = None
    _globals['_RAYLOGSSPEC'].fields_by_name['disabled']._serialized_options = b'\xe0A\x01'
    _globals['_PERSISTENTRESOURCE']._serialized_start = 383
    _globals['_PERSISTENTRESOURCE']._serialized_end = 1675
    _globals['_PERSISTENTRESOURCE_LABELSENTRY']._serialized_start = 1377
    _globals['_PERSISTENTRESOURCE_LABELSENTRY']._serialized_end = 1422
    _globals['_PERSISTENTRESOURCE_STATE']._serialized_start = 1424
    _globals['_PERSISTENTRESOURCE_STATE']._serialized_end = 1539
    _globals['_RESOURCEPOOL']._serialized_start = 1678
    _globals['_RESOURCEPOOL']._serialized_end = 2168
    _globals['_RESOURCEPOOL_AUTOSCALINGSPEC']._serialized_start = 2015
    _globals['_RESOURCEPOOL_AUTOSCALINGSPEC']._serialized_end = 2150
    _globals['_RESOURCERUNTIMESPEC']._serialized_start = 2171
    _globals['_RESOURCERUNTIMESPEC']._serialized_end = 2345
    _globals['_RAYSPEC']._serialized_start = 2348
    _globals['_RAYSPEC']._serialized_end = 2802
    _globals['_RAYSPEC_RESOURCEPOOLIMAGESENTRY']._serialized_start = 2745
    _globals['_RAYSPEC_RESOURCEPOOLIMAGESENTRY']._serialized_end = 2802
    _globals['_RESOURCERUNTIME']._serialized_start = 2805
    _globals['_RESOURCERUNTIME']._serialized_end = 3061
    _globals['_RESOURCERUNTIME_ACCESSURISENTRY']._serialized_start = 3012
    _globals['_RESOURCERUNTIME_ACCESSURISENTRY']._serialized_end = 3061
    _globals['_SERVICEACCOUNTSPEC']._serialized_start = 3063
    _globals['_SERVICEACCOUNTSPEC']._serialized_end = 3157
    _globals['_RAYMETRICSPEC']._serialized_start = 3159
    _globals['_RAYMETRICSPEC']._serialized_end = 3197
    _globals['_RAYLOGSSPEC']._serialized_start = 3199
    _globals['_RAYLOGSSPEC']._serialized_end = 3235