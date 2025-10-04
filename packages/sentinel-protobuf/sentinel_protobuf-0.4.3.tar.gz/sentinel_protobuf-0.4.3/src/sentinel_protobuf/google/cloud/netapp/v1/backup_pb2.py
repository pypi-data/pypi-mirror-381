"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/netapp/v1/backup.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/netapp/v1/backup.proto\x12\x16google.cloud.netapp.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd4\x08\n\x06Backup\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x128\n\x05state\x18\x02 \x01(\x0e2$.google.cloud.netapp.v1.Backup.StateB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x1f\n\x12volume_usage_bytes\x18\x04 \x01(\x03B\x03\xe0A\x03\x12=\n\x0bbackup_type\x18\x05 \x01(\x0e2#.google.cloud.netapp.v1.Backup.TypeB\x03\xe0A\x03\x128\n\rsource_volume\x18\x06 \x01(\tB!\xfaA\x1e\n\x1cnetapp.googleapis.com/Volume\x12A\n\x0fsource_snapshot\x18\x07 \x01(\tB#\xfaA \n\x1enetapp.googleapis.com/SnapshotH\x00\x88\x01\x01\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12:\n\x06labels\x18\t \x03(\x0b2*.google.cloud.netapp.v1.Backup.LabelsEntry\x12 \n\x13chain_storage_bytes\x18\n \x01(\x03B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzs\x18\x0b \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x0c \x01(\x08B\x03\xe0A\x03\x12@\n\rvolume_region\x18\r \x01(\tB)\xe0A\x03\xfaA#\n!locations.googleapis.com/Location\x12@\n\rbackup_region\x18\x0e \x01(\tB)\xe0A\x03\xfaA#\n!locations.googleapis.com/Location\x12D\n\x1benforced_retention_end_time\x18\x0f \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"m\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\r\n\tUPLOADING\x10\x02\x12\t\n\x05READY\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\t\n\x05ERROR\x10\x05\x12\x0c\n\x08UPDATING\x10\x06"7\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06MANUAL\x10\x01\x12\r\n\tSCHEDULED\x10\x02:\x89\x01\xeaA\x85\x01\n\x1cnetapp.googleapis.com/Backup\x12Tprojects/{project}/locations/{location}/backupVaults/{backup_vault}/backups/{backup}*\x07backups2\x06backupB\x12\n\x10_source_snapshot"\x93\x01\n\x12ListBackupsRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\x12\x1cnetapp.googleapis.com/Backup\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t"t\n\x13ListBackupsResponse\x12/\n\x07backups\x18\x01 \x03(\x0b2\x1e.google.cloud.netapp.v1.Backup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"F\n\x10GetBackupRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cnetapp.googleapis.com/Backup"\x98\x01\n\x13CreateBackupRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\x12\x1cnetapp.googleapis.com/Backup\x12\x16\n\tbackup_id\x18\x02 \x01(\tB\x03\xe0A\x02\x123\n\x06backup\x18\x03 \x01(\x0b2\x1e.google.cloud.netapp.v1.BackupB\x03\xe0A\x02"I\n\x13DeleteBackupRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cnetapp.googleapis.com/Backup"\x80\x01\n\x13UpdateBackupRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x123\n\x06backup\x18\x02 \x01(\x0b2\x1e.google.cloud.netapp.v1.BackupB\x03\xe0A\x02B\xad\x01\n\x1acom.google.cloud.netapp.v1B\x0bBackupProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.netapp.v1.backup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.netapp.v1B\x0bBackupProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1'
    _globals['_BACKUP_LABELSENTRY']._loaded_options = None
    _globals['_BACKUP_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BACKUP'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_BACKUP'].fields_by_name['state']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['volume_usage_bytes']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['volume_usage_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['backup_type']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['backup_type']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['source_volume']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['source_volume']._serialized_options = b'\xfaA\x1e\n\x1cnetapp.googleapis.com/Volume'
    _globals['_BACKUP'].fields_by_name['source_snapshot']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['source_snapshot']._serialized_options = b'\xfaA \n\x1enetapp.googleapis.com/Snapshot'
    _globals['_BACKUP'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['chain_storage_bytes']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['chain_storage_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP'].fields_by_name['volume_region']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['volume_region']._serialized_options = b'\xe0A\x03\xfaA#\n!locations.googleapis.com/Location'
    _globals['_BACKUP'].fields_by_name['backup_region']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['backup_region']._serialized_options = b'\xe0A\x03\xfaA#\n!locations.googleapis.com/Location'
    _globals['_BACKUP'].fields_by_name['enforced_retention_end_time']._loaded_options = None
    _globals['_BACKUP'].fields_by_name['enforced_retention_end_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUP']._loaded_options = None
    _globals['_BACKUP']._serialized_options = b'\xeaA\x85\x01\n\x1cnetapp.googleapis.com/Backup\x12Tprojects/{project}/locations/{location}/backupVaults/{backup_vault}/backups/{backup}*\x07backups2\x06backup'
    _globals['_LISTBACKUPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBACKUPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\x12\x1cnetapp.googleapis.com/Backup'
    _globals['_GETBACKUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBACKUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cnetapp.googleapis.com/Backup'
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\x12\x1cnetapp.googleapis.com/Backup'
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['backup_id']._loaded_options = None
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['backup_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['backup']._loaded_options = None
    _globals['_CREATEBACKUPREQUEST'].fields_by_name['backup']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEBACKUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBACKUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cnetapp.googleapis.com/Backup'
    _globals['_UPDATEBACKUPREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBACKUPREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBACKUPREQUEST'].fields_by_name['backup']._loaded_options = None
    _globals['_UPDATEBACKUPREQUEST'].fields_by_name['backup']._serialized_options = b'\xe0A\x02'
    _globals['_BACKUP']._serialized_start = 191
    _globals['_BACKUP']._serialized_end = 1299
    _globals['_BACKUP_LABELSENTRY']._serialized_start = 926
    _globals['_BACKUP_LABELSENTRY']._serialized_end = 971
    _globals['_BACKUP_STATE']._serialized_start = 973
    _globals['_BACKUP_STATE']._serialized_end = 1082
    _globals['_BACKUP_TYPE']._serialized_start = 1084
    _globals['_BACKUP_TYPE']._serialized_end = 1139
    _globals['_LISTBACKUPSREQUEST']._serialized_start = 1302
    _globals['_LISTBACKUPSREQUEST']._serialized_end = 1449
    _globals['_LISTBACKUPSRESPONSE']._serialized_start = 1451
    _globals['_LISTBACKUPSRESPONSE']._serialized_end = 1567
    _globals['_GETBACKUPREQUEST']._serialized_start = 1569
    _globals['_GETBACKUPREQUEST']._serialized_end = 1639
    _globals['_CREATEBACKUPREQUEST']._serialized_start = 1642
    _globals['_CREATEBACKUPREQUEST']._serialized_end = 1794
    _globals['_DELETEBACKUPREQUEST']._serialized_start = 1796
    _globals['_DELETEBACKUPREQUEST']._serialized_end = 1869
    _globals['_UPDATEBACKUPREQUEST']._serialized_start = 1872
    _globals['_UPDATEBACKUPREQUEST']._serialized_end = 2000