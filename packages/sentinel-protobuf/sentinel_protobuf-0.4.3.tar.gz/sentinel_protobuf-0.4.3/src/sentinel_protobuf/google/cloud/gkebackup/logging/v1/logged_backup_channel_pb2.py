"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkebackup/logging/v1/logged_backup_channel.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/gkebackup/logging/v1/logged_backup_channel.proto\x12!google.cloud.gkebackup.logging.v1"\xca\x01\n\x13LoggedBackupChannel\x12\x1b\n\x13destination_project\x18\x01 \x01(\t\x12R\n\x06labels\x18\x02 \x03(\x0b2B.google.cloud.gkebackup.logging.v1.LoggedBackupChannel.LabelsEntry\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\xf4\x01\n%com.google.cloud.gkebackup.logging.v1B\x18LoggedBackupChannelProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.logging.v1.logged_backup_channel_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.gkebackup.logging.v1B\x18LoggedBackupChannelProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1'
    _globals['_LOGGEDBACKUPCHANNEL_LABELSENTRY']._loaded_options = None
    _globals['_LOGGEDBACKUPCHANNEL_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_LOGGEDBACKUPCHANNEL']._serialized_start = 101
    _globals['_LOGGEDBACKUPCHANNEL']._serialized_end = 303
    _globals['_LOGGEDBACKUPCHANNEL_LABELSENTRY']._serialized_start = 258
    _globals['_LOGGEDBACKUPCHANNEL_LABELSENTRY']._serialized_end = 303