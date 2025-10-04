"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkebackup/v1/backup_plan_binding.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkebackup.v1 import common_pb2 as google_dot_cloud_dot_gkebackup_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/gkebackup/v1/backup_plan_binding.proto\x12\x19google.cloud.gkebackup.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/gkebackup/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8e\x0e\n\x11BackupPlanBinding\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x03uid\x18\x02 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12C\n\x0bbackup_plan\x18\x05 \x01(\tB.\xe0A\x05\xe0A\x03\xfaA%\n#gkebackup.googleapis.com/BackupPlan\x12<\n\x07cluster\x18\x06 \x01(\tB+\xe0A\x05\xe0A\x03\xfaA"\n container.googleapis.com/Cluster\x12`\n\x13backup_plan_details\x18\x07 \x01(\x0b2>.google.cloud.gkebackup.v1.BackupPlanBinding.BackupPlanDetailsB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x08 \x01(\tB\x03\xe0A\x03\x1a\x9b\t\n\x11BackupPlanDetails\x12 \n\x13protected_pod_count\x18\x01 \x01(\x05B\x03\xe0A\x03\x12X\n\x05state\x18\x02 \x01(\x0e2D.google.cloud.gkebackup.v1.BackupPlanBinding.BackupPlanDetails.StateB\x03\xe0A\x03\x12D\n\x1blast_successful_backup_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12C\n\x1anext_scheduled_backup_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1b\n\x0erpo_risk_level\x18\x05 \x01(\x05B\x03\xe0A\x03\x12#\n\x16last_successful_backup\x18\x06 \x01(\tB\x03\xe0A\x03\x12v\n\x15backup_config_details\x18\x07 \x01(\x0b2R.google.cloud.gkebackup.v1.BackupPlanBinding.BackupPlanDetails.BackupConfigDetailsB\x03\xe0A\x03\x12|\n\x18retention_policy_details\x18\x08 \x01(\x0b2U.google.cloud.gkebackup.v1.BackupPlanBinding.BackupPlanDetails.RetentionPolicyDetailsB\x03\xe0A\x03\x1a\xe8\x02\n\x13BackupConfigDetails\x12\x1d\n\x0eall_namespaces\x18\x01 \x01(\x08B\x03\xe0A\x03H\x00\x12I\n\x13selected_namespaces\x18\x02 \x01(\x0b2%.google.cloud.gkebackup.v1.NamespacesB\x03\xe0A\x03H\x00\x12P\n\x15selected_applications\x18\x03 \x01(\x0b2*.google.cloud.gkebackup.v1.NamespacedNamesB\x03\xe0A\x03H\x00\x12 \n\x13include_volume_data\x18\x05 \x01(\x08B\x03\xe0A\x03\x12\x1c\n\x0finclude_secrets\x18\x06 \x01(\x08B\x03\xe0A\x03\x12E\n\x0eencryption_key\x18\x07 \x01(\x0b2(.google.cloud.gkebackup.v1.EncryptionKeyB\x03\xe0A\x03B\x0e\n\x0cbackup_scope\x1a_\n\x16RetentionPolicyDetails\x12$\n\x17backup_delete_lock_days\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x1f\n\x12backup_retain_days\x18\x02 \x01(\x05B\x03\xe0A\x01"{\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x13\n\x0fCLUSTER_PENDING\x10\x01\x12\x10\n\x0cPROVISIONING\x10\x02\x12\t\n\x05READY\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\x0f\n\x0bDEACTIVATED\x10\x05\x12\x0c\n\x08DELETING\x10\x06:\xc9\x01\xeaA\xc5\x01\n*gkebackup.googleapis.com/BackupPlanBinding\x12pprojects/{project}/locations/{location}/backupChannels/{backup_channel}/backupPlanBindings/{backup_plan_binding}*\x12backupPlanBindings2\x11backupPlanBindingB\xcd\x01\n\x1dcom.google.cloud.gkebackup.v1B\x16BackupPlanBindingProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.v1.backup_plan_binding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.gkebackup.v1B\x16BackupPlanBindingProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS'].fields_by_name['all_namespaces']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS'].fields_by_name['all_namespaces']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS'].fields_by_name['selected_namespaces']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS'].fields_by_name['selected_namespaces']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS'].fields_by_name['selected_applications']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS'].fields_by_name['selected_applications']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS'].fields_by_name['include_volume_data']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS'].fields_by_name['include_volume_data']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS'].fields_by_name['include_secrets']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS'].fields_by_name['include_secrets']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS'].fields_by_name['encryption_key']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS'].fields_by_name['encryption_key']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_RETENTIONPOLICYDETAILS'].fields_by_name['backup_delete_lock_days']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_RETENTIONPOLICYDETAILS'].fields_by_name['backup_delete_lock_days']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_RETENTIONPOLICYDETAILS'].fields_by_name['backup_retain_days']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_RETENTIONPOLICYDETAILS'].fields_by_name['backup_retain_days']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['protected_pod_count']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['protected_pod_count']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['state']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['last_successful_backup_time']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['last_successful_backup_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['next_scheduled_backup_time']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['next_scheduled_backup_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['rpo_risk_level']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['rpo_risk_level']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['last_successful_backup']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['last_successful_backup']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['backup_config_details']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['backup_config_details']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['retention_policy_details']._loaded_options = None
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS'].fields_by_name['retention_policy_details']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUPPLANBINDING'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_BACKUPPLANBINDING'].fields_by_name['uid']._loaded_options = None
    _globals['_BACKUPPLANBINDING'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_BACKUPPLANBINDING'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKUPPLANBINDING'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING'].fields_by_name['update_time']._loaded_options = None
    _globals['_BACKUPPLANBINDING'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING'].fields_by_name['backup_plan']._loaded_options = None
    _globals['_BACKUPPLANBINDING'].fields_by_name['backup_plan']._serialized_options = b'\xe0A\x05\xe0A\x03\xfaA%\n#gkebackup.googleapis.com/BackupPlan'
    _globals['_BACKUPPLANBINDING'].fields_by_name['cluster']._loaded_options = None
    _globals['_BACKUPPLANBINDING'].fields_by_name['cluster']._serialized_options = b'\xe0A\x05\xe0A\x03\xfaA"\n container.googleapis.com/Cluster'
    _globals['_BACKUPPLANBINDING'].fields_by_name['backup_plan_details']._loaded_options = None
    _globals['_BACKUPPLANBINDING'].fields_by_name['backup_plan_details']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING'].fields_by_name['etag']._loaded_options = None
    _globals['_BACKUPPLANBINDING'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPLANBINDING']._loaded_options = None
    _globals['_BACKUPPLANBINDING']._serialized_options = b'\xeaA\xc5\x01\n*gkebackup.googleapis.com/BackupPlanBinding\x12pprojects/{project}/locations/{location}/backupChannels/{backup_channel}/backupPlanBindings/{backup_plan_binding}*\x12backupPlanBindings2\x11backupPlanBinding'
    _globals['_BACKUPPLANBINDING']._serialized_start = 245
    _globals['_BACKUPPLANBINDING']._serialized_end = 2051
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS']._serialized_start = 668
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS']._serialized_end = 1847
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS']._serialized_start = 1265
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_BACKUPCONFIGDETAILS']._serialized_end = 1625
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_RETENTIONPOLICYDETAILS']._serialized_start = 1627
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_RETENTIONPOLICYDETAILS']._serialized_end = 1722
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_STATE']._serialized_start = 1724
    _globals['_BACKUPPLANBINDING_BACKUPPLANDETAILS_STATE']._serialized_end = 1847