"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkebackup/v1/backup_channel.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/gkebackup/v1/backup_channel.proto\x12\x19google.cloud.gkebackup.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb0\x04\n\rBackupChannel\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12#\n\x13destination_project\x18\x02 \x01(\tB\x06\xe0A\x05\xe0A\x02\x12\x18\n\x03uid\x18\x03 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12I\n\x06labels\x18\x06 \x03(\x0b24.google.cloud.gkebackup.v1.BackupChannel.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04etag\x18\x08 \x01(\tB\x03\xe0A\x03\x12#\n\x16destination_project_id\x18\t \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x94\x01\xeaA\x90\x01\n&gkebackup.googleapis.com/BackupChannel\x12Gprojects/{project}/locations/{location}/backupChannels/{backup_channel}*\x0ebackupChannels2\rbackupChannelB\xc9\x01\n\x1dcom.google.cloud.gkebackup.v1B\x12BackupChannelProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.v1.backup_channel_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.gkebackup.v1B\x12BackupChannelProtoP\x01Z;cloud.google.com/go/gkebackup/apiv1/gkebackuppb;gkebackuppb\xaa\x02\x19Google.Cloud.GkeBackup.V1\xca\x02\x19Google\\Cloud\\GkeBackup\\V1\xea\x02\x1cGoogle::Cloud::GkeBackup::V1'
    _globals['_BACKUPCHANNEL_LABELSENTRY']._loaded_options = None
    _globals['_BACKUPCHANNEL_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BACKUPCHANNEL'].fields_by_name['name']._loaded_options = None
    _globals['_BACKUPCHANNEL'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_BACKUPCHANNEL'].fields_by_name['destination_project']._loaded_options = None
    _globals['_BACKUPCHANNEL'].fields_by_name['destination_project']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_BACKUPCHANNEL'].fields_by_name['uid']._loaded_options = None
    _globals['_BACKUPCHANNEL'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_BACKUPCHANNEL'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKUPCHANNEL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPCHANNEL'].fields_by_name['update_time']._loaded_options = None
    _globals['_BACKUPCHANNEL'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPCHANNEL'].fields_by_name['labels']._loaded_options = None
    _globals['_BACKUPCHANNEL'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPCHANNEL'].fields_by_name['description']._loaded_options = None
    _globals['_BACKUPCHANNEL'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_BACKUPCHANNEL'].fields_by_name['etag']._loaded_options = None
    _globals['_BACKUPCHANNEL'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPCHANNEL'].fields_by_name['destination_project_id']._loaded_options = None
    _globals['_BACKUPCHANNEL'].fields_by_name['destination_project_id']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPCHANNEL']._loaded_options = None
    _globals['_BACKUPCHANNEL']._serialized_options = b'\xeaA\x90\x01\n&gkebackup.googleapis.com/BackupChannel\x12Gprojects/{project}/locations/{location}/backupChannels/{backup_channel}*\x0ebackupChannels2\rbackupChannel'
    _globals['_BACKUPCHANNEL']._serialized_start = 200
    _globals['_BACKUPCHANNEL']._serialized_end = 760
    _globals['_BACKUPCHANNEL_LABELSENTRY']._serialized_start = 564
    _globals['_BACKUPCHANNEL_LABELSENTRY']._serialized_end = 609