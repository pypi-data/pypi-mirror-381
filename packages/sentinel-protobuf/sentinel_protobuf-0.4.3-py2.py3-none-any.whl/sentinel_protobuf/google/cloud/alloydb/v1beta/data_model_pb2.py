"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/alloydb/v1beta/data_model.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/alloydb/v1beta/data_model.proto\x12\x1bgoogle.cloud.alloydb.v1beta"\x83\x01\n\tSqlResult\x12=\n\x07columns\x18\x01 \x03(\x0b2,.google.cloud.alloydb.v1beta.SqlResultColumn\x127\n\x04rows\x18\x02 \x03(\x0b2).google.cloud.alloydb.v1beta.SqlResultRow"-\n\x0fSqlResultColumn\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t"K\n\x0cSqlResultRow\x12;\n\x06values\x18\x01 \x03(\x0b2+.google.cloud.alloydb.v1beta.SqlResultValue"V\n\x0eSqlResultValue\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nnull_value\x18\x02 \x01(\x08H\x01\x88\x01\x01B\x08\n\x06_valueB\r\n\x0b_null_valueB\xcb\x01\n\x1fcom.google.cloud.alloydb.v1betaB\x0eDataModelProtoP\x01Z9cloud.google.com/go/alloydb/apiv1beta/alloydbpb;alloydbpb\xaa\x02\x1bGoogle.Cloud.AlloyDb.V1Beta\xca\x02\x1bGoogle\\Cloud\\AlloyDb\\V1beta\xea\x02\x1eGoogle::Cloud::AlloyDB::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.alloydb.v1beta.data_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.alloydb.v1betaB\x0eDataModelProtoP\x01Z9cloud.google.com/go/alloydb/apiv1beta/alloydbpb;alloydbpb\xaa\x02\x1bGoogle.Cloud.AlloyDb.V1Beta\xca\x02\x1bGoogle\\Cloud\\AlloyDb\\V1beta\xea\x02\x1eGoogle::Cloud::AlloyDB::V1beta'
    _globals['_SQLRESULT']._serialized_start = 78
    _globals['_SQLRESULT']._serialized_end = 209
    _globals['_SQLRESULTCOLUMN']._serialized_start = 211
    _globals['_SQLRESULTCOLUMN']._serialized_end = 256
    _globals['_SQLRESULTROW']._serialized_start = 258
    _globals['_SQLRESULTROW']._serialized_end = 333
    _globals['_SQLRESULTVALUE']._serialized_start = 335
    _globals['_SQLRESULTVALUE']._serialized_end = 421