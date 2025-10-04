"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/backupdr/v1/backupvault_ba.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/backupdr/v1/backupvault_ba.proto\x12\x18google.cloud.backupdr.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xed\x02\n\x1fBackupApplianceBackupProperties\x12\x1f\n\rgeneration_id\x18\x01 \x01(\x05B\x03\xe0A\x03H\x00\x88\x01\x01\x12;\n\rfinalize_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03H\x01\x88\x01\x01\x12G\n\x19recovery_range_start_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01H\x02\x88\x01\x01\x12E\n\x17recovery_range_end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01H\x03\x88\x01\x01B\x10\n\x0e_generation_idB\x10\n\x0e_finalize_timeB\x1c\n\x1a_recovery_range_start_timeB\x1a\n\x18_recovery_range_end_timeB\xc2\x01\n\x1ccom.google.cloud.backupdr.v1B\x12BackupvaultBaProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.backupdr.v1.backupvault_ba_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.backupdr.v1B\x12BackupvaultBaProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1'
    _globals['_BACKUPAPPLIANCEBACKUPPROPERTIES'].fields_by_name['generation_id']._loaded_options = None
    _globals['_BACKUPAPPLIANCEBACKUPPROPERTIES'].fields_by_name['generation_id']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPAPPLIANCEBACKUPPROPERTIES'].fields_by_name['finalize_time']._loaded_options = None
    _globals['_BACKUPAPPLIANCEBACKUPPROPERTIES'].fields_by_name['finalize_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPAPPLIANCEBACKUPPROPERTIES'].fields_by_name['recovery_range_start_time']._loaded_options = None
    _globals['_BACKUPAPPLIANCEBACKUPPROPERTIES'].fields_by_name['recovery_range_start_time']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPAPPLIANCEBACKUPPROPERTIES'].fields_by_name['recovery_range_end_time']._loaded_options = None
    _globals['_BACKUPAPPLIANCEBACKUPPROPERTIES'].fields_by_name['recovery_range_end_time']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPAPPLIANCEBACKUPPROPERTIES']._serialized_start = 142
    _globals['_BACKUPAPPLIANCEBACKUPPROPERTIES']._serialized_end = 507