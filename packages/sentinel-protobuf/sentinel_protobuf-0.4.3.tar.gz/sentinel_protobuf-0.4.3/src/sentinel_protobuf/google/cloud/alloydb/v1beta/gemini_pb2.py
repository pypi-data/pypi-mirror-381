"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/alloydb/v1beta/gemini.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/alloydb/v1beta/gemini.proto\x12\x1bgoogle.cloud.alloydb.v1beta\x1a\x1fgoogle/api/field_behavior.proto".\n\x13GeminiClusterConfig\x12\x17\n\x08entitled\x18\x01 \x01(\x08B\x05\x18\x01\xe0A\x03"/\n\x14GeminiInstanceConfig\x12\x17\n\x08entitled\x18\x01 \x01(\x08B\x05\x18\x01\xe0A\x03"b\n\x11GCAInstanceConfig\x12M\n\x0fgca_entitlement\x18\x01 \x01(\x0e2/.google.cloud.alloydb.v1beta.GCAEntitlementTypeB\x03\xe0A\x03*L\n\x12GCAEntitlementType\x12$\n GCA_ENTITLEMENT_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cGCA_STANDARD\x10\x01B\xc8\x01\n\x1fcom.google.cloud.alloydb.v1betaB\x0bGeminiProtoP\x01Z9cloud.google.com/go/alloydb/apiv1beta/alloydbpb;alloydbpb\xaa\x02\x1bGoogle.Cloud.AlloyDb.V1Beta\xca\x02\x1bGoogle\\Cloud\\AlloyDb\\V1beta\xea\x02\x1eGoogle::Cloud::AlloyDB::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.alloydb.v1beta.gemini_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.alloydb.v1betaB\x0bGeminiProtoP\x01Z9cloud.google.com/go/alloydb/apiv1beta/alloydbpb;alloydbpb\xaa\x02\x1bGoogle.Cloud.AlloyDb.V1Beta\xca\x02\x1bGoogle\\Cloud\\AlloyDb\\V1beta\xea\x02\x1eGoogle::Cloud::AlloyDB::V1beta'
    _globals['_GEMINICLUSTERCONFIG'].fields_by_name['entitled']._loaded_options = None
    _globals['_GEMINICLUSTERCONFIG'].fields_by_name['entitled']._serialized_options = b'\x18\x01\xe0A\x03'
    _globals['_GEMINIINSTANCECONFIG'].fields_by_name['entitled']._loaded_options = None
    _globals['_GEMINIINSTANCECONFIG'].fields_by_name['entitled']._serialized_options = b'\x18\x01\xe0A\x03'
    _globals['_GCAINSTANCECONFIG'].fields_by_name['gca_entitlement']._loaded_options = None
    _globals['_GCAINSTANCECONFIG'].fields_by_name['gca_entitlement']._serialized_options = b'\xe0A\x03'
    _globals['_GCAENTITLEMENTTYPE']._serialized_start = 303
    _globals['_GCAENTITLEMENTTYPE']._serialized_end = 379
    _globals['_GEMINICLUSTERCONFIG']._serialized_start = 106
    _globals['_GEMINICLUSTERCONFIG']._serialized_end = 152
    _globals['_GEMINIINSTANCECONFIG']._serialized_start = 154
    _globals['_GEMINIINSTANCECONFIG']._serialized_end = 201
    _globals['_GCAINSTANCECONFIG']._serialized_start = 203
    _globals['_GCAINSTANCECONFIG']._serialized_end = 301