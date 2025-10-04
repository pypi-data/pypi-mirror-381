"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/datacatalog/v1/dump_content.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.datacatalog.v1 import datacatalog_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_datacatalog__pb2
from .....google.cloud.datacatalog.v1 import tags_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_tags__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/datacatalog/v1/dump_content.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a-google/cloud/datacatalog/v1/datacatalog.proto\x1a&google/cloud/datacatalog/v1/tags.proto"\xc7\x01\n\x0bTaggedEntry\x126\n\x08v1_entry\x18\x01 \x01(\x0b2".google.cloud.datacatalog.v1.EntryH\x00\x12;\n\x0cpresent_tags\x18\x02 \x03(\x0b2 .google.cloud.datacatalog.v1.TagB\x03\xe0A\x01\x12:\n\x0babsent_tags\x18\x03 \x03(\x0b2 .google.cloud.datacatalog.v1.TagB\x03\xe0A\x01B\x07\n\x05entry"T\n\x08DumpItem\x12@\n\x0ctagged_entry\x18\x01 \x01(\x0b2(.google.cloud.datacatalog.v1.TaggedEntryH\x00B\x06\n\x04itemB\xd5\x01\n\x1fcom.google.cloud.datacatalog.v1B\x10DumpContentProtoP\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1.dump_content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.datacatalog.v1B\x10DumpContentProtoP\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1'
    _globals['_TAGGEDENTRY'].fields_by_name['present_tags']._loaded_options = None
    _globals['_TAGGEDENTRY'].fields_by_name['present_tags']._serialized_options = b'\xe0A\x01'
    _globals['_TAGGEDENTRY'].fields_by_name['absent_tags']._loaded_options = None
    _globals['_TAGGEDENTRY'].fields_by_name['absent_tags']._serialized_options = b'\xe0A\x01'
    _globals['_TAGGEDENTRY']._serialized_start = 200
    _globals['_TAGGEDENTRY']._serialized_end = 399
    _globals['_DUMPITEM']._serialized_start = 401
    _globals['_DUMPITEM']._serialized_end = 485