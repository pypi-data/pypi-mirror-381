"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/alloydb/v1/data_model.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/alloydb/v1/data_model.proto\x12\x17google.cloud.alloydb.v1"{\n\tSqlResult\x129\n\x07columns\x18\x01 \x03(\x0b2(.google.cloud.alloydb.v1.SqlResultColumn\x123\n\x04rows\x18\x02 \x03(\x0b2%.google.cloud.alloydb.v1.SqlResultRow"-\n\x0fSqlResultColumn\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t"G\n\x0cSqlResultRow\x127\n\x06values\x18\x01 \x03(\x0b2\'.google.cloud.alloydb.v1.SqlResultValue"V\n\x0eSqlResultValue\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nnull_value\x18\x02 \x01(\x08H\x01\x88\x01\x01B\x08\n\x06_valueB\r\n\x0b_null_valueB\xb7\x01\n\x1bcom.google.cloud.alloydb.v1B\x0eDataModelProtoP\x01Z5cloud.google.com/go/alloydb/apiv1/alloydbpb;alloydbpb\xaa\x02\x17Google.Cloud.AlloyDb.V1\xca\x02\x17Google\\Cloud\\AlloyDb\\V1\xea\x02\x1aGoogle::Cloud::AlloyDB::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.alloydb.v1.data_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.alloydb.v1B\x0eDataModelProtoP\x01Z5cloud.google.com/go/alloydb/apiv1/alloydbpb;alloydbpb\xaa\x02\x17Google.Cloud.AlloyDb.V1\xca\x02\x17Google\\Cloud\\AlloyDb\\V1\xea\x02\x1aGoogle::Cloud::AlloyDB::V1'
    _globals['_SQLRESULT']._serialized_start = 69
    _globals['_SQLRESULT']._serialized_end = 192
    _globals['_SQLRESULTCOLUMN']._serialized_start = 194
    _globals['_SQLRESULTCOLUMN']._serialized_end = 239
    _globals['_SQLRESULTROW']._serialized_start = 241
    _globals['_SQLRESULTROW']._serialized_end = 312
    _globals['_SQLRESULTVALUE']._serialized_start = 314
    _globals['_SQLRESULTVALUE']._serialized_end = 400