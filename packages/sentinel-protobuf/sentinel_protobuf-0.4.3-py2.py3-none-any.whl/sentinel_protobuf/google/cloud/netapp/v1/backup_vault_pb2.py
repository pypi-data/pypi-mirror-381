"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/netapp/v1/backup_vault.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/netapp/v1/backup_vault.proto\x12\x16google.cloud.netapp.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x91\n\n\x0bBackupVault\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12=\n\x05state\x18\x02 \x01(\x0e2).google.cloud.netapp.v1.BackupVault.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12?\n\x06labels\x18\x05 \x03(\x0b2/.google.cloud.netapp.v1.BackupVault.LabelsEntry\x12S\n\x11backup_vault_type\x18\x06 \x01(\x0e23.google.cloud.netapp.v1.BackupVault.BackupVaultTypeB\x03\xe0A\x01\x12@\n\rsource_region\x18\x07 \x01(\tB)\xe0A\x03\xfaA#\n!locations.googleapis.com/Location\x12@\n\rbackup_region\x18\x08 \x01(\tB)\xe0A\x01\xfaA#\n!locations.googleapis.com/Location\x12F\n\x13source_backup_vault\x18\t \x01(\tB)\xe0A\x03\xfaA#\n!netapp.googleapis.com/BackupVault\x12K\n\x18destination_backup_vault\x18\n \x01(\tB)\xe0A\x03\xfaA#\n!netapp.googleapis.com/BackupVault\x12_\n\x17backup_retention_policy\x18\x0b \x01(\x0b29.google.cloud.netapp.v1.BackupVault.BackupRetentionPolicyB\x03\xe0A\x01\x1a\xe4\x01\n\x15BackupRetentionPolicy\x123\n&backup_minimum_enforced_retention_days\x18\x01 \x01(\x05B\x03\xe0A\x02\x12#\n\x16daily_backup_immutable\x18\x02 \x01(\x08B\x03\xe0A\x01\x12$\n\x17weekly_backup_immutable\x18\x03 \x01(\x08B\x03\xe0A\x01\x12%\n\x18monthly_backup_immutable\x18\x04 \x01(\x08B\x03\xe0A\x01\x12$\n\x17manual_backup_immutable\x18\x05 \x01(\x08B\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"^\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\t\n\x05ERROR\x10\x04\x12\x0c\n\x08UPDATING\x10\x05"U\n\x0fBackupVaultType\x12!\n\x1dBACKUP_VAULT_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tIN_REGION\x10\x01\x12\x10\n\x0cCROSS_REGION\x10\x02:\x87\x01\xeaA\x83\x01\n!netapp.googleapis.com/BackupVault\x12Cprojects/{project}/locations/{location}/backupVaults/{backup_vault}*\x0cbackupVaults2\x0bbackupVault"P\n\x15GetBackupVaultRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/BackupVault"\x9d\x01\n\x17ListBackupVaultsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!netapp.googleapis.com/BackupVault\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t"\x84\x01\n\x18ListBackupVaultsResponse\x12:\n\rbackup_vaults\x18\x01 \x03(\x0b2#.google.cloud.netapp.v1.BackupVault\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\xb3\x01\n\x18CreateBackupVaultRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!netapp.googleapis.com/BackupVault\x12\x1c\n\x0fbackup_vault_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12>\n\x0cbackup_vault\x18\x03 \x01(\x0b2#.google.cloud.netapp.v1.BackupVaultB\x03\xe0A\x02"S\n\x18DeleteBackupVaultRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/BackupVault"\x90\x01\n\x18UpdateBackupVaultRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12>\n\x0cbackup_vault\x18\x02 \x01(\x0b2#.google.cloud.netapp.v1.BackupVaultB\x03\xe0A\x02B\xb2\x01\n\x1acom.google.cloud.netapp.v1B\x10BackupVaultProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.netapp.v1.backup_vault_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.netapp.v1B\x10BackupVaultProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1'
    _globals['_BACKUPVAULT_BACKUPRETENTIONPOLICY'].fields_by_name['backup_minimum_enforced_retention_days']._loaded_options = None
    _globals['_BACKUPVAULT_BACKUPRETENTIONPOLICY'].fields_by_name['backup_minimum_enforced_retention_days']._serialized_options = b'\xe0A\x02'
    _globals['_BACKUPVAULT_BACKUPRETENTIONPOLICY'].fields_by_name['daily_backup_immutable']._loaded_options = None
    _globals['_BACKUPVAULT_BACKUPRETENTIONPOLICY'].fields_by_name['daily_backup_immutable']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPVAULT_BACKUPRETENTIONPOLICY'].fields_by_name['weekly_backup_immutable']._loaded_options = None
    _globals['_BACKUPVAULT_BACKUPRETENTIONPOLICY'].fields_by_name['weekly_backup_immutable']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPVAULT_BACKUPRETENTIONPOLICY'].fields_by_name['monthly_backup_immutable']._loaded_options = None
    _globals['_BACKUPVAULT_BACKUPRETENTIONPOLICY'].fields_by_name['monthly_backup_immutable']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPVAULT_BACKUPRETENTIONPOLICY'].fields_by_name['manual_backup_immutable']._loaded_options = None
    _globals['_BACKUPVAULT_BACKUPRETENTIONPOLICY'].fields_by_name['manual_backup_immutable']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPVAULT_LABELSENTRY']._loaded_options = None
    _globals['_BACKUPVAULT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BACKUPVAULT'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUPVAULT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_BACKUPVAULT'].fields_by_name['state']._loaded_options = None
    _globals['_BACKUPVAULT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPVAULT'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKUPVAULT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPVAULT'].fields_by_name['backup_vault_type']._loaded_options = None
    _globals['_BACKUPVAULT'].fields_by_name['backup_vault_type']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPVAULT'].fields_by_name['source_region']._loaded_options = None
    _globals['_BACKUPVAULT'].fields_by_name['source_region']._serialized_options = b'\xe0A\x03\xfaA#\n!locations.googleapis.com/Location'
    _globals['_BACKUPVAULT'].fields_by_name['backup_region']._loaded_options = None
    _globals['_BACKUPVAULT'].fields_by_name['backup_region']._serialized_options = b'\xe0A\x01\xfaA#\n!locations.googleapis.com/Location'
    _globals['_BACKUPVAULT'].fields_by_name['source_backup_vault']._loaded_options = None
    _globals['_BACKUPVAULT'].fields_by_name['source_backup_vault']._serialized_options = b'\xe0A\x03\xfaA#\n!netapp.googleapis.com/BackupVault'
    _globals['_BACKUPVAULT'].fields_by_name['destination_backup_vault']._loaded_options = None
    _globals['_BACKUPVAULT'].fields_by_name['destination_backup_vault']._serialized_options = b'\xe0A\x03\xfaA#\n!netapp.googleapis.com/BackupVault'
    _globals['_BACKUPVAULT'].fields_by_name['backup_retention_policy']._loaded_options = None
    _globals['_BACKUPVAULT'].fields_by_name['backup_retention_policy']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPVAULT']._loaded_options = None
    _globals['_BACKUPVAULT']._serialized_options = b'\xeaA\x83\x01\n!netapp.googleapis.com/BackupVault\x12Cprojects/{project}/locations/{location}/backupVaults/{backup_vault}*\x0cbackupVaults2\x0bbackupVault'
    _globals['_GETBACKUPVAULTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBACKUPVAULTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/BackupVault'
    _globals['_LISTBACKUPVAULTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBACKUPVAULTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!netapp.googleapis.com/BackupVault'
    _globals['_CREATEBACKUPVAULTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBACKUPVAULTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!netapp.googleapis.com/BackupVault'
    _globals['_CREATEBACKUPVAULTREQUEST'].fields_by_name['backup_vault_id']._loaded_options = None
    _globals['_CREATEBACKUPVAULTREQUEST'].fields_by_name['backup_vault_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPVAULTREQUEST'].fields_by_name['backup_vault']._loaded_options = None
    _globals['_CREATEBACKUPVAULTREQUEST'].fields_by_name['backup_vault']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEBACKUPVAULTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBACKUPVAULTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/BackupVault'
    _globals['_UPDATEBACKUPVAULTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBACKUPVAULTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBACKUPVAULTREQUEST'].fields_by_name['backup_vault']._loaded_options = None
    _globals['_UPDATEBACKUPVAULTREQUEST'].fields_by_name['backup_vault']._serialized_options = b'\xe0A\x02'
    _globals['_BACKUPVAULT']._serialized_start = 197
    _globals['_BACKUPVAULT']._serialized_end = 1494
    _globals['_BACKUPVAULT_BACKUPRETENTIONPOLICY']._serialized_start = 898
    _globals['_BACKUPVAULT_BACKUPRETENTIONPOLICY']._serialized_end = 1126
    _globals['_BACKUPVAULT_LABELSENTRY']._serialized_start = 1128
    _globals['_BACKUPVAULT_LABELSENTRY']._serialized_end = 1173
    _globals['_BACKUPVAULT_STATE']._serialized_start = 1175
    _globals['_BACKUPVAULT_STATE']._serialized_end = 1269
    _globals['_BACKUPVAULT_BACKUPVAULTTYPE']._serialized_start = 1271
    _globals['_BACKUPVAULT_BACKUPVAULTTYPE']._serialized_end = 1356
    _globals['_GETBACKUPVAULTREQUEST']._serialized_start = 1496
    _globals['_GETBACKUPVAULTREQUEST']._serialized_end = 1576
    _globals['_LISTBACKUPVAULTSREQUEST']._serialized_start = 1579
    _globals['_LISTBACKUPVAULTSREQUEST']._serialized_end = 1736
    _globals['_LISTBACKUPVAULTSRESPONSE']._serialized_start = 1739
    _globals['_LISTBACKUPVAULTSRESPONSE']._serialized_end = 1871
    _globals['_CREATEBACKUPVAULTREQUEST']._serialized_start = 1874
    _globals['_CREATEBACKUPVAULTREQUEST']._serialized_end = 2053
    _globals['_DELETEBACKUPVAULTREQUEST']._serialized_start = 2055
    _globals['_DELETEBACKUPVAULTREQUEST']._serialized_end = 2138
    _globals['_UPDATEBACKUPVAULTREQUEST']._serialized_start = 2141
    _globals['_UPDATEBACKUPVAULTREQUEST']._serialized_end = 2285