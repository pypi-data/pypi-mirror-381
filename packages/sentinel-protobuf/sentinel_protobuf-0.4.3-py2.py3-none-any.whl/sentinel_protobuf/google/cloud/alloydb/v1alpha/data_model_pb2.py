"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/alloydb/v1alpha/data_model.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/alloydb/v1alpha/data_model.proto\x12\x1cgoogle.cloud.alloydb.v1alpha"\x85\x01\n\tSqlResult\x12>\n\x07columns\x18\x01 \x03(\x0b2-.google.cloud.alloydb.v1alpha.SqlResultColumn\x128\n\x04rows\x18\x02 \x03(\x0b2*.google.cloud.alloydb.v1alpha.SqlResultRow"-\n\x0fSqlResultColumn\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t"L\n\x0cSqlResultRow\x12<\n\x06values\x18\x01 \x03(\x0b2,.google.cloud.alloydb.v1alpha.SqlResultValue"V\n\x0eSqlResultValue\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\nnull_value\x18\x02 \x01(\x08H\x01\x88\x01\x01B\x08\n\x06_valueB\r\n\x0b_null_valueB\xd0\x01\n com.google.cloud.alloydb.v1alphaB\x0eDataModelProtoP\x01Z:cloud.google.com/go/alloydb/apiv1alpha/alloydbpb;alloydbpb\xaa\x02\x1cGoogle.Cloud.AlloyDb.V1Alpha\xca\x02\x1cGoogle\\Cloud\\AlloyDb\\V1alpha\xea\x02\x1fGoogle::Cloud::AlloyDB::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.alloydb.v1alpha.data_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.alloydb.v1alphaB\x0eDataModelProtoP\x01Z:cloud.google.com/go/alloydb/apiv1alpha/alloydbpb;alloydbpb\xaa\x02\x1cGoogle.Cloud.AlloyDb.V1Alpha\xca\x02\x1cGoogle\\Cloud\\AlloyDb\\V1alpha\xea\x02\x1fGoogle::Cloud::AlloyDB::V1alpha'
    _globals['_SQLRESULT']._serialized_start = 80
    _globals['_SQLRESULT']._serialized_end = 213
    _globals['_SQLRESULTCOLUMN']._serialized_start = 215
    _globals['_SQLRESULTCOLUMN']._serialized_end = 260
    _globals['_SQLRESULTROW']._serialized_start = 262
    _globals['_SQLRESULTROW']._serialized_end = 338
    _globals['_SQLRESULTVALUE']._serialized_start = 340
    _globals['_SQLRESULTVALUE']._serialized_end = 426