"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/sql/v1/cloud_sql_backup_runs.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.sql.v1 import cloud_sql_resources_pb2 as google_dot_cloud_dot_sql_dot_v1_dot_cloud__sql__resources__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/sql/v1/cloud_sql_backup_runs.proto\x12\x13google.cloud.sql.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a-google/cloud/sql/v1/cloud_sql_resources.proto\x1a\x1fgoogle/protobuf/timestamp.proto"K\n\x1aSqlBackupRunsDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t"H\n\x17SqlBackupRunsGetRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t"m\n\x1aSqlBackupRunsInsertRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12,\n\x04body\x18d \x01(\x0b2\x1e.google.cloud.sql.v1.BackupRun"f\n\x18SqlBackupRunsListRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t"\x8c\x06\n\tBackupRun\x12\x0c\n\x04kind\x18\x01 \x01(\t\x127\n\x06status\x18\x02 \x01(\x0e2\'.google.cloud.sql.v1.SqlBackupRunStatus\x121\n\renqueued_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\n\n\x02id\x18\x04 \x01(\x03\x12.\n\nstart_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x122\n\x05error\x18\x07 \x01(\x0b2#.google.cloud.sql.v1.OperationError\x123\n\x04type\x18\x08 \x01(\x0e2%.google.cloud.sql.v1.SqlBackupRunType\x12\x13\n\x0bdescription\x18\t \x01(\t\x125\n\x11window_start_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x10\n\x08instance\x18\x0b \x01(\t\x12\x11\n\tself_link\x18\x0c \x01(\t\x12\x10\n\x08location\x18\r \x01(\t\x12W\n\x1ddisk_encryption_configuration\x18\x10 \x01(\x0b20.google.cloud.sql.v1.DiskEncryptionConfiguration\x12I\n\x16disk_encryption_status\x18\x11 \x01(\x0b2).google.cloud.sql.v1.DiskEncryptionStatus\x127\n\x0bbackup_kind\x18\x13 \x01(\x0e2".google.cloud.sql.v1.SqlBackupKind\x12\x11\n\ttime_zone\x18\x17 \x01(\t\x12&\n\x14max_chargeable_bytes\x18\x18 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01B\x17\n\x15_max_chargeable_bytes"n\n\x16BackupRunsListResponse\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12-\n\x05items\x18\x02 \x03(\x0b2\x1e.google.cloud.sql.v1.BackupRun\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t*\xc4\x01\n\x12SqlBackupRunStatus\x12%\n!SQL_BACKUP_RUN_STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08ENQUEUED\x10\x01\x12\x0b\n\x07OVERDUE\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\x0e\n\nSUCCESSFUL\x10\x05\x12\x0b\n\x07SKIPPED\x10\x06\x12\x14\n\x10DELETION_PENDING\x10\x07\x12\x13\n\x0fDELETION_FAILED\x10\x08\x12\x0b\n\x07DELETED\x10\t*L\n\rSqlBackupKind\x12\x1f\n\x1bSQL_BACKUP_KIND_UNSPECIFIED\x10\x00\x12\x0c\n\x08SNAPSHOT\x10\x01\x12\x0c\n\x08PHYSICAL\x10\x02*U\n\x10SqlBackupRunType\x12#\n\x1fSQL_BACKUP_RUN_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tAUTOMATED\x10\x01\x12\r\n\tON_DEMAND\x10\x022\x97\x06\n\x14SqlBackupRunsService\x12\x9e\x01\n\x06Delete\x12/.google.cloud.sql.v1.SqlBackupRunsDeleteRequest\x1a\x1e.google.cloud.sql.v1.Operation"C\x82\xd3\xe4\x93\x02=*;/v1/projects/{project}/instances/{instance}/backupRuns/{id}\x12\x98\x01\n\x03Get\x12,.google.cloud.sql.v1.SqlBackupRunsGetRequest\x1a\x1e.google.cloud.sql.v1.BackupRun"C\x82\xd3\xe4\x93\x02=\x12;/v1/projects/{project}/instances/{instance}/backupRuns/{id}\x12\x9f\x01\n\x06Insert\x12/.google.cloud.sql.v1.SqlBackupRunsInsertRequest\x1a\x1e.google.cloud.sql.v1.Operation"D\x82\xd3\xe4\x93\x02>"6/v1/projects/{project}/instances/{instance}/backupRuns:\x04body\x12\xa2\x01\n\x04List\x12-.google.cloud.sql.v1.SqlBackupRunsListRequest\x1a+.google.cloud.sql.v1.BackupRunsListResponse">\x82\xd3\xe4\x93\x028\x126/v1/projects/{project}/instances/{instance}/backupRuns\x1a|\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.adminB_\n\x17com.google.cloud.sql.v1B\x17CloudSqlBackupRunsProtoP\x01Z)cloud.google.com/go/sql/apiv1/sqlpb;sqlpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.sql.v1.cloud_sql_backup_runs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.sql.v1B\x17CloudSqlBackupRunsProtoP\x01Z)cloud.google.com/go/sql/apiv1/sqlpb;sqlpb'
    _globals['_BACKUPRUN'].fields_by_name['max_chargeable_bytes']._loaded_options = None
    _globals['_BACKUPRUN'].fields_by_name['max_chargeable_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_SQLBACKUPRUNSSERVICE']._loaded_options = None
    _globals['_SQLBACKUPRUNSSERVICE']._serialized_options = b'\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.admin'
    _globals['_SQLBACKUPRUNSSERVICE'].methods_by_name['Delete']._loaded_options = None
    _globals['_SQLBACKUPRUNSSERVICE'].methods_by_name['Delete']._serialized_options = b'\x82\xd3\xe4\x93\x02=*;/v1/projects/{project}/instances/{instance}/backupRuns/{id}'
    _globals['_SQLBACKUPRUNSSERVICE'].methods_by_name['Get']._loaded_options = None
    _globals['_SQLBACKUPRUNSSERVICE'].methods_by_name['Get']._serialized_options = b'\x82\xd3\xe4\x93\x02=\x12;/v1/projects/{project}/instances/{instance}/backupRuns/{id}'
    _globals['_SQLBACKUPRUNSSERVICE'].methods_by_name['Insert']._loaded_options = None
    _globals['_SQLBACKUPRUNSSERVICE'].methods_by_name['Insert']._serialized_options = b'\x82\xd3\xe4\x93\x02>"6/v1/projects/{project}/instances/{instance}/backupRuns:\x04body'
    _globals['_SQLBACKUPRUNSSERVICE'].methods_by_name['List']._loaded_options = None
    _globals['_SQLBACKUPRUNSSERVICE'].methods_by_name['List']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/v1/projects/{project}/instances/{instance}/backupRuns'
    _globals['_SQLBACKUPRUNSTATUS']._serialized_start = 1502
    _globals['_SQLBACKUPRUNSTATUS']._serialized_end = 1698
    _globals['_SQLBACKUPKIND']._serialized_start = 1700
    _globals['_SQLBACKUPKIND']._serialized_end = 1776
    _globals['_SQLBACKUPRUNTYPE']._serialized_start = 1778
    _globals['_SQLBACKUPRUNTYPE']._serialized_end = 1863
    _globals['_SQLBACKUPRUNSDELETEREQUEST']._serialized_start = 240
    _globals['_SQLBACKUPRUNSDELETEREQUEST']._serialized_end = 315
    _globals['_SQLBACKUPRUNSGETREQUEST']._serialized_start = 317
    _globals['_SQLBACKUPRUNSGETREQUEST']._serialized_end = 389
    _globals['_SQLBACKUPRUNSINSERTREQUEST']._serialized_start = 391
    _globals['_SQLBACKUPRUNSINSERTREQUEST']._serialized_end = 500
    _globals['_SQLBACKUPRUNSLISTREQUEST']._serialized_start = 502
    _globals['_SQLBACKUPRUNSLISTREQUEST']._serialized_end = 604
    _globals['_BACKUPRUN']._serialized_start = 607
    _globals['_BACKUPRUN']._serialized_end = 1387
    _globals['_BACKUPRUNSLISTRESPONSE']._serialized_start = 1389
    _globals['_BACKUPRUNSLISTRESPONSE']._serialized_end = 1499
    _globals['_SQLBACKUPRUNSSERVICE']._serialized_start = 1866
    _globals['_SQLBACKUPRUNSSERVICE']._serialized_end = 2657