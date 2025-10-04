"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkebackup/logging/v1/logging.proto')
_sym_db = _symbol_database.Default()
from ......google.cloud.gkebackup.logging.v1 import logged_backup_pb2 as google_dot_cloud_dot_gkebackup_dot_logging_dot_v1_dot_logged__backup__pb2
from ......google.cloud.gkebackup.logging.v1 import logged_backup_channel_pb2 as google_dot_cloud_dot_gkebackup_dot_logging_dot_v1_dot_logged__backup__channel__pb2
from ......google.cloud.gkebackup.logging.v1 import logged_backup_plan_pb2 as google_dot_cloud_dot_gkebackup_dot_logging_dot_v1_dot_logged__backup__plan__pb2
from ......google.cloud.gkebackup.logging.v1 import logged_backup_plan_metadata_pb2 as google_dot_cloud_dot_gkebackup_dot_logging_dot_v1_dot_logged__backup__plan__metadata__pb2
from ......google.cloud.gkebackup.logging.v1 import logged_restore_pb2 as google_dot_cloud_dot_gkebackup_dot_logging_dot_v1_dot_logged__restore__pb2
from ......google.cloud.gkebackup.logging.v1 import logged_restore_channel_pb2 as google_dot_cloud_dot_gkebackup_dot_logging_dot_v1_dot_logged__restore__channel__pb2
from ......google.cloud.gkebackup.logging.v1 import logged_restore_plan_pb2 as google_dot_cloud_dot_gkebackup_dot_logging_dot_v1_dot_logged__restore__plan__pb2
from ......google.cloud.gkebackup.logging.v1 import logged_restore_plan_metadata_pb2 as google_dot_cloud_dot_gkebackup_dot_logging_dot_v1_dot_logged__restore__plan__metadata__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/gkebackup/logging/v1/logging.proto\x12!google.cloud.gkebackup.logging.v1\x1a5google/cloud/gkebackup/logging/v1/logged_backup.proto\x1a=google/cloud/gkebackup/logging/v1/logged_backup_channel.proto\x1a:google/cloud/gkebackup/logging/v1/logged_backup_plan.proto\x1aCgoogle/cloud/gkebackup/logging/v1/logged_backup_plan_metadata.proto\x1a6google/cloud/gkebackup/logging/v1/logged_restore.proto\x1a>google/cloud/gkebackup/logging/v1/logged_restore_channel.proto\x1a;google/cloud/gkebackup/logging/v1/logged_restore_plan.proto\x1aDgoogle/cloud/gkebackup/logging/v1/logged_restore_plan_metadata.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xea\x02\n\x10BackupPlanChange\x12\x13\n\x0bbackup_plan\x18\x01 \x01(\t\x12B\n\x0bchange_type\x18\x02 \x01(\x0e2-.google.cloud.gkebackup.logging.v1.ChangeType\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12N\n\x11input_backup_plan\x18\x04 \x01(\x0b23.google.cloud.gkebackup.logging.v1.LoggedBackupPlan\x12!\n\x05error\x18\x05 \x01(\x0b2\x12.google.rpc.Status\x12Y\n\x14backup_plan_metadata\x18\x06 \x01(\x0b2;.google.cloud.gkebackup.logging.v1.LoggedBackupPlanMetadata"\x90\x02\n\x0cBackupChange\x12\x0e\n\x06backup\x18\x01 \x01(\t\x12B\n\x0bchange_type\x18\x02 \x01(\x0e2-.google.cloud.gkebackup.logging.v1.ChangeType\x12\x11\n\tscheduled\x18\x03 \x01(\x08\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12E\n\x0cinput_backup\x18\x05 \x01(\x0b2/.google.cloud.gkebackup.logging.v1.LoggedBackup\x12!\n\x05error\x18\x06 \x01(\x0b2\x12.google.rpc.Status"\xf0\x02\n\x11RestorePlanChange\x12\x14\n\x0crestore_plan\x18\x01 \x01(\t\x12B\n\x0bchange_type\x18\x02 \x01(\x0e2-.google.cloud.gkebackup.logging.v1.ChangeType\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12P\n\x12input_restore_plan\x18\x04 \x01(\x0b24.google.cloud.gkebackup.logging.v1.LoggedRestorePlan\x12!\n\x05error\x18\x05 \x01(\x0b2\x12.google.rpc.Status\x12[\n\x15restore_plan_metadata\x18\x06 \x01(\x0b2<.google.cloud.gkebackup.logging.v1.LoggedRestorePlanMetadata"\x81\x02\n\rRestoreChange\x12\x0f\n\x07restore\x18\x01 \x01(\t\x12B\n\x0bchange_type\x18\x02 \x01(\x0e2-.google.cloud.gkebackup.logging.v1.ChangeType\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12G\n\rinput_restore\x18\x04 \x01(\x0b20.google.cloud.gkebackup.logging.v1.LoggedRestore\x12!\n\x05error\x18\x05 \x01(\x0b2\x12.google.rpc.Status"\x9b\x02\n\x13BackupChannelChange\x12\x16\n\x0ebackup_channel\x18\x01 \x01(\t\x12B\n\x0bchange_type\x18\x02 \x01(\x0e2-.google.cloud.gkebackup.logging.v1.ChangeType\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12T\n\x14input_backup_channel\x18\x04 \x01(\x0b26.google.cloud.gkebackup.logging.v1.LoggedBackupChannel\x12!\n\x05error\x18\x05 \x01(\x0b2\x12.google.rpc.Status"\x9f\x02\n\x14RestoreChannelChange\x12\x17\n\x0frestore_channel\x18\x01 \x01(\t\x12B\n\x0bchange_type\x18\x02 \x01(\x0e2-.google.cloud.gkebackup.logging.v1.ChangeType\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12V\n\x15input_restore_channel\x18\x04 \x01(\x0b27.google.cloud.gkebackup.logging.v1.LoggedRestoreChannel\x12!\n\x05error\x18\x05 \x01(\x0b2\x12.google.rpc.Status*Q\n\nChangeType\x12\x1b\n\x17CHANGE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATION\x10\x01\x12\n\n\x06UPDATE\x10\x02\x12\x0c\n\x08DELETION\x10\x03B\xe4\x01\n!google.cloud.gkebackup.logging.v1B\x0cLoggingProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.logging.v1.logging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!google.cloud.gkebackup.logging.v1B\x0cLoggingProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1'
    _globals['_CHANGETYPE']._serialized_start = 2490
    _globals['_CHANGETYPE']._serialized_end = 2571
    _globals['_BACKUPPLANCHANGE']._serialized_start = 644
    _globals['_BACKUPPLANCHANGE']._serialized_end = 1006
    _globals['_BACKUPCHANGE']._serialized_start = 1009
    _globals['_BACKUPCHANGE']._serialized_end = 1281
    _globals['_RESTOREPLANCHANGE']._serialized_start = 1284
    _globals['_RESTOREPLANCHANGE']._serialized_end = 1652
    _globals['_RESTORECHANGE']._serialized_start = 1655
    _globals['_RESTORECHANGE']._serialized_end = 1912
    _globals['_BACKUPCHANNELCHANGE']._serialized_start = 1915
    _globals['_BACKUPCHANNELCHANGE']._serialized_end = 2198
    _globals['_RESTORECHANNELCHANGE']._serialized_start = 2201
    _globals['_RESTORECHANNELCHANGE']._serialized_end = 2488