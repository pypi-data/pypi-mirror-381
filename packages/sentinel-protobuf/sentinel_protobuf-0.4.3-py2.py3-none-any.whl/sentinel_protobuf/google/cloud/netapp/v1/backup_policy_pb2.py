"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/netapp/v1/backup_policy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/netapp/v1/backup_policy.proto\x12\x16google.cloud.netapp.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb6\x06\n\x0cBackupPolicy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1f\n\x12daily_backup_limit\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12 \n\x13weekly_backup_limit\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12!\n\x14monthly_backup_limit\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12\x18\n\x0bdescription\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x14\n\x07enabled\x18\x06 \x01(\x08H\x04\x88\x01\x01\x12\'\n\x15assigned_volume_count\x18\x07 \x01(\x05B\x03\xe0A\x03H\x05\x88\x01\x01\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12@\n\x06labels\x18\t \x03(\x0b20.google.cloud.netapp.v1.BackupPolicy.LabelsEntry\x12>\n\x05state\x18\n \x01(\x0e2*.google.cloud.netapp.v1.BackupPolicy.StateB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"^\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\t\n\x05ERROR\x10\x04\x12\x0c\n\x08UPDATING\x10\x05:\x8e\x01\xeaA\x8a\x01\n"netapp.googleapis.com/BackupPolicy\x12Fprojects/{project}/locations/{location}/backupPolicies/{backup_policy}*\x0ebackupPolicies2\x0cbackupPolicyB\x15\n\x13_daily_backup_limitB\x16\n\x14_weekly_backup_limitB\x17\n\x15_monthly_backup_limitB\x0e\n\x0c_descriptionB\n\n\x08_enabledB\x18\n\x16_assigned_volume_count"\xb8\x01\n\x19CreateBackupPolicyRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"netapp.googleapis.com/BackupPolicy\x12@\n\rbackup_policy\x18\x02 \x01(\x0b2$.google.cloud.netapp.v1.BackupPolicyB\x03\xe0A\x02\x12\x1d\n\x10backup_policy_id\x18\x03 \x01(\tB\x03\xe0A\x02"R\n\x16GetBackupPolicyRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"netapp.googleapis.com/BackupPolicy"\xa0\x01\n\x19ListBackupPoliciesRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"netapp.googleapis.com/BackupPolicy\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x89\x01\n\x1aListBackupPoliciesResponse\x12=\n\x0fbackup_policies\x18\x01 \x03(\x0b2$.google.cloud.netapp.v1.BackupPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\x93\x01\n\x19UpdateBackupPolicyRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12@\n\rbackup_policy\x18\x02 \x01(\x0b2$.google.cloud.netapp.v1.BackupPolicyB\x03\xe0A\x02"U\n\x19DeleteBackupPolicyRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"netapp.googleapis.com/BackupPolicyB\xb3\x01\n\x1acom.google.cloud.netapp.v1B\x11BackupPolicyProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.netapp.v1.backup_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.netapp.v1B\x11BackupPolicyProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1'
    _globals['_BACKUPPOLICY_LABELSENTRY']._loaded_options = None
    _globals['_BACKUPPOLICY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BACKUPPOLICY'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUPPOLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_BACKUPPOLICY'].fields_by_name['assigned_volume_count']._loaded_options = None
    _globals['_BACKUPPOLICY'].fields_by_name['assigned_volume_count']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPOLICY'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKUPPOLICY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPOLICY'].fields_by_name['state']._loaded_options = None
    _globals['_BACKUPPOLICY'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPPOLICY']._loaded_options = None
    _globals['_BACKUPPOLICY']._serialized_options = b'\xeaA\x8a\x01\n"netapp.googleapis.com/BackupPolicy\x12Fprojects/{project}/locations/{location}/backupPolicies/{backup_policy}*\x0ebackupPolicies2\x0cbackupPolicy'
    _globals['_CREATEBACKUPPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBACKUPPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"netapp.googleapis.com/BackupPolicy'
    _globals['_CREATEBACKUPPOLICYREQUEST'].fields_by_name['backup_policy']._loaded_options = None
    _globals['_CREATEBACKUPPOLICYREQUEST'].fields_by_name['backup_policy']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKUPPOLICYREQUEST'].fields_by_name['backup_policy_id']._loaded_options = None
    _globals['_CREATEBACKUPPOLICYREQUEST'].fields_by_name['backup_policy_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETBACKUPPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBACKUPPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"netapp.googleapis.com/BackupPolicy'
    _globals['_LISTBACKUPPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBACKUPPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"netapp.googleapis.com/BackupPolicy'
    _globals['_UPDATEBACKUPPOLICYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBACKUPPOLICYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBACKUPPOLICYREQUEST'].fields_by_name['backup_policy']._loaded_options = None
    _globals['_UPDATEBACKUPPOLICYREQUEST'].fields_by_name['backup_policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEBACKUPPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBACKUPPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"netapp.googleapis.com/BackupPolicy'
    _globals['_BACKUPPOLICY']._serialized_start = 198
    _globals['_BACKUPPOLICY']._serialized_end = 1020
    _globals['_BACKUPPOLICY_LABELSENTRY']._serialized_start = 608
    _globals['_BACKUPPOLICY_LABELSENTRY']._serialized_end = 653
    _globals['_BACKUPPOLICY_STATE']._serialized_start = 655
    _globals['_BACKUPPOLICY_STATE']._serialized_end = 749
    _globals['_CREATEBACKUPPOLICYREQUEST']._serialized_start = 1023
    _globals['_CREATEBACKUPPOLICYREQUEST']._serialized_end = 1207
    _globals['_GETBACKUPPOLICYREQUEST']._serialized_start = 1209
    _globals['_GETBACKUPPOLICYREQUEST']._serialized_end = 1291
    _globals['_LISTBACKUPPOLICIESREQUEST']._serialized_start = 1294
    _globals['_LISTBACKUPPOLICIESREQUEST']._serialized_end = 1454
    _globals['_LISTBACKUPPOLICIESRESPONSE']._serialized_start = 1457
    _globals['_LISTBACKUPPOLICIESRESPONSE']._serialized_end = 1594
    _globals['_UPDATEBACKUPPOLICYREQUEST']._serialized_start = 1597
    _globals['_UPDATEBACKUPPOLICYREQUEST']._serialized_end = 1744
    _globals['_DELETEBACKUPPOLICYREQUEST']._serialized_start = 1746
    _globals['_DELETEBACKUPPOLICYREQUEST']._serialized_end = 1831