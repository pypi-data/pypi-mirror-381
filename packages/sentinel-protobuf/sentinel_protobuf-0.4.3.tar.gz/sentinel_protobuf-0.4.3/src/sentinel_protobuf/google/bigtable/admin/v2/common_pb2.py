"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/bigtable/admin/v2/common.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/bigtable/admin/v2/common.proto\x12\x18google.bigtable.admin.v2\x1a\x1fgoogle/protobuf/timestamp.proto"\x8b\x01\n\x11OperationProgress\x12\x18\n\x10progress_percent\x18\x01 \x01(\x05\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp*=\n\x0bStorageType\x12\x1c\n\x18STORAGE_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03SSD\x10\x01\x12\x07\n\x03HDD\x10\x02B\xce\x01\n\x1ccom.google.bigtable.admin.v2B\x0bCommonProtoP\x01Z8cloud.google.com/go/bigtable/admin/apiv2/adminpb;adminpb\xaa\x02\x1eGoogle.Cloud.Bigtable.Admin.V2\xca\x02\x1eGoogle\\Cloud\\Bigtable\\Admin\\V2\xea\x02"Google::Cloud::Bigtable::Admin::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.bigtable.admin.v2.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.bigtable.admin.v2B\x0bCommonProtoP\x01Z8cloud.google.com/go/bigtable/admin/apiv2/adminpb;adminpb\xaa\x02\x1eGoogle.Cloud.Bigtable.Admin.V2\xca\x02\x1eGoogle\\Cloud\\Bigtable\\Admin\\V2\xea\x02"Google::Cloud::Bigtable::Admin::V2'
    _globals['_STORAGETYPE']._serialized_start = 242
    _globals['_STORAGETYPE']._serialized_end = 303
    _globals['_OPERATIONPROGRESS']._serialized_start = 101
    _globals['_OPERATIONPROGRESS']._serialized_end = 240