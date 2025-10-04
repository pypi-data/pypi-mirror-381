"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/firestore/admin/v1/index.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/firestore/admin/v1/index.proto\x12\x19google.firestore.admin.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xed\n\n\x05Index\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x0bquery_scope\x18\x02 \x01(\x0e2+.google.firestore.admin.v1.Index.QueryScope\x12<\n\tapi_scope\x18\x05 \x01(\x0e2).google.firestore.admin.v1.Index.ApiScope\x12;\n\x06fields\x18\x03 \x03(\x0b2+.google.firestore.admin.v1.Index.IndexField\x125\n\x05state\x18\x04 \x01(\x0e2&.google.firestore.admin.v1.Index.State\x12>\n\x07density\x18\x06 \x01(\x0e2(.google.firestore.admin.v1.Index.DensityB\x03\xe0A\x05\x12\x15\n\x08multikey\x18\x07 \x01(\x08B\x03\xe0A\x01\x12\x18\n\x0bshard_count\x18\x08 \x01(\x05B\x03\xe0A\x01\x1a\xa2\x04\n\nIndexField\x12\x12\n\nfield_path\x18\x01 \x01(\t\x12B\n\x05order\x18\x02 \x01(\x0e21.google.firestore.admin.v1.Index.IndexField.OrderH\x00\x12O\n\x0carray_config\x18\x03 \x01(\x0e27.google.firestore.admin.v1.Index.IndexField.ArrayConfigH\x00\x12Q\n\rvector_config\x18\x04 \x01(\x0b28.google.firestore.admin.v1.Index.IndexField.VectorConfigH\x00\x1a\x8f\x01\n\x0cVectorConfig\x12\x16\n\tdimension\x18\x01 \x01(\x05B\x03\xe0A\x02\x12R\n\x04flat\x18\x02 \x01(\x0b2B.google.firestore.admin.v1.Index.IndexField.VectorConfig.FlatIndexH\x00\x1a\x0b\n\tFlatIndexB\x06\n\x04type"=\n\x05Order\x12\x15\n\x11ORDER_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02"9\n\x0bArrayConfig\x12\x1c\n\x18ARRAY_CONFIG_UNSPECIFIED\x10\x00\x12\x0c\n\x08CONTAINS\x10\x01B\x0c\n\nvalue_mode"i\n\nQueryScope\x12\x1b\n\x17QUERY_SCOPE_UNSPECIFIED\x10\x00\x12\x0e\n\nCOLLECTION\x10\x01\x12\x14\n\x10COLLECTION_GROUP\x10\x02\x12\x18\n\x14COLLECTION_RECURSIVE\x10\x03"K\n\x08ApiScope\x12\x0b\n\x07ANY_API\x10\x00\x12\x16\n\x12DATASTORE_MODE_API\x10\x01\x12\x1a\n\x16MONGODB_COMPATIBLE_API\x10\x02"I\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x10\n\x0cNEEDS_REPAIR\x10\x03"M\n\x07Density\x12\x17\n\x13DENSITY_UNSPECIFIED\x10\x00\x12\x0e\n\nSPARSE_ALL\x10\x01\x12\x0e\n\nSPARSE_ANY\x10\x02\x12\t\n\x05DENSE\x10\x03:z\xeaAw\n\x1efirestore.googleapis.com/Index\x12Uprojects/{project}/databases/{database}/collectionGroups/{collection}/indexes/{index}B\xd9\x01\n\x1dcom.google.firestore.admin.v1B\nIndexProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1.index_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.firestore.admin.v1B\nIndexProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1'
    _globals['_INDEX_INDEXFIELD_VECTORCONFIG'].fields_by_name['dimension']._loaded_options = None
    _globals['_INDEX_INDEXFIELD_VECTORCONFIG'].fields_by_name['dimension']._serialized_options = b'\xe0A\x02'
    _globals['_INDEX'].fields_by_name['density']._loaded_options = None
    _globals['_INDEX'].fields_by_name['density']._serialized_options = b'\xe0A\x05'
    _globals['_INDEX'].fields_by_name['multikey']._loaded_options = None
    _globals['_INDEX'].fields_by_name['multikey']._serialized_options = b'\xe0A\x01'
    _globals['_INDEX'].fields_by_name['shard_count']._loaded_options = None
    _globals['_INDEX'].fields_by_name['shard_count']._serialized_options = b'\xe0A\x01'
    _globals['_INDEX']._loaded_options = None
    _globals['_INDEX']._serialized_options = b'\xeaAw\n\x1efirestore.googleapis.com/Index\x12Uprojects/{project}/databases/{database}/collectionGroups/{collection}/indexes/{index}'
    _globals['_INDEX']._serialized_start = 129
    _globals['_INDEX']._serialized_end = 1518
    _globals['_INDEX_INDEXFIELD']._serialized_start = 510
    _globals['_INDEX_INDEXFIELD']._serialized_end = 1056
    _globals['_INDEX_INDEXFIELD_VECTORCONFIG']._serialized_start = 777
    _globals['_INDEX_INDEXFIELD_VECTORCONFIG']._serialized_end = 920
    _globals['_INDEX_INDEXFIELD_VECTORCONFIG_FLATINDEX']._serialized_start = 901
    _globals['_INDEX_INDEXFIELD_VECTORCONFIG_FLATINDEX']._serialized_end = 912
    _globals['_INDEX_INDEXFIELD_ORDER']._serialized_start = 922
    _globals['_INDEX_INDEXFIELD_ORDER']._serialized_end = 983
    _globals['_INDEX_INDEXFIELD_ARRAYCONFIG']._serialized_start = 985
    _globals['_INDEX_INDEXFIELD_ARRAYCONFIG']._serialized_end = 1042
    _globals['_INDEX_QUERYSCOPE']._serialized_start = 1058
    _globals['_INDEX_QUERYSCOPE']._serialized_end = 1163
    _globals['_INDEX_APISCOPE']._serialized_start = 1165
    _globals['_INDEX_APISCOPE']._serialized_end = 1240
    _globals['_INDEX_STATE']._serialized_start = 1242
    _globals['_INDEX_STATE']._serialized_end = 1315
    _globals['_INDEX_DENSITY']._serialized_start = 1317
    _globals['_INDEX_DENSITY']._serialized_end = 1394