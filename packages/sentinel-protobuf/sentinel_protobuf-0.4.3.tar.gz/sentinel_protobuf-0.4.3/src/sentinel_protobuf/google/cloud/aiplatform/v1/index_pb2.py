"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/index.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import deployed_index_ref_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_deployed__index__ref__pb2
from .....google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/aiplatform/v1/index.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a3google/cloud/aiplatform/v1/deployed_index_ref.proto\x1a0google/cloud/aiplatform/v1/encryption_spec.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa4\x07\n\x05Index\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12 \n\x13metadata_schema_uri\x18\x04 \x01(\tB\x03\xe0A\x05\x12(\n\x08metadata\x18\x06 \x01(\x0b2\x16.google.protobuf.Value\x12K\n\x10deployed_indexes\x18\x07 \x03(\x0b2,.google.cloud.aiplatform.v1.DeployedIndexRefB\x03\xe0A\x03\x12\x0c\n\x04etag\x18\x08 \x01(\t\x12=\n\x06labels\x18\t \x03(\x0b2-.google.cloud.aiplatform.v1.Index.LabelsEntry\x124\n\x0bcreate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12@\n\x0bindex_stats\x18\x0e \x01(\x0b2&.google.cloud.aiplatform.v1.IndexStatsB\x03\xe0A\x03\x12U\n\x13index_update_method\x18\x10 \x01(\x0e23.google.cloud.aiplatform.v1.Index.IndexUpdateMethodB\x03\xe0A\x05\x12H\n\x0fencryption_spec\x18\x11 \x01(\x0b2*.google.cloud.aiplatform.v1.EncryptionSpecB\x03\xe0A\x05\x12\x1a\n\rsatisfies_pzs\x18\x12 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x13 \x01(\x08B\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"]\n\x11IndexUpdateMethod\x12#\n\x1fINDEX_UPDATE_METHOD_UNSPECIFIED\x10\x00\x12\x10\n\x0cBATCH_UPDATE\x10\x01\x12\x11\n\rSTREAM_UPDATE\x10\x02:]\xeaAZ\n\x1faiplatform.googleapis.com/Index\x127projects/{project}/locations/{location}/indexes/{index}"\xd9\x07\n\x0eIndexDatapoint\x12\x19\n\x0cdatapoint_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0efeature_vector\x18\x02 \x03(\x02B\x03\xe0A\x02\x12Y\n\x10sparse_embedding\x18\x07 \x01(\x0b2:.google.cloud.aiplatform.v1.IndexDatapoint.SparseEmbeddingB\x03\xe0A\x01\x12N\n\trestricts\x18\x04 \x03(\x0b26.google.cloud.aiplatform.v1.IndexDatapoint.RestrictionB\x03\xe0A\x01\x12]\n\x11numeric_restricts\x18\x06 \x03(\x0b2=.google.cloud.aiplatform.v1.IndexDatapoint.NumericRestrictionB\x03\xe0A\x01\x12Q\n\x0ccrowding_tag\x18\x05 \x01(\x0b26.google.cloud.aiplatform.v1.IndexDatapoint.CrowdingTagB\x03\xe0A\x01\x128\n\x12embedding_metadata\x18\x08 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x1a?\n\x0fSparseEmbedding\x12\x13\n\x06values\x18\x01 \x03(\x02B\x03\xe0A\x02\x12\x17\n\ndimensions\x18\x02 \x03(\x03B\x03\xe0A\x02\x1aG\n\x0bRestriction\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x12\n\nallow_list\x18\x02 \x03(\t\x12\x11\n\tdeny_list\x18\x03 \x03(\t\x1a\xc2\x02\n\x12NumericRestriction\x12\x13\n\tvalue_int\x18\x02 \x01(\x03H\x00\x12\x15\n\x0bvalue_float\x18\x03 \x01(\x02H\x00\x12\x16\n\x0cvalue_double\x18\x04 \x01(\x01H\x00\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12R\n\x02op\x18\x05 \x01(\x0e2F.google.cloud.aiplatform.v1.IndexDatapoint.NumericRestriction.Operator"x\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x08\n\x04LESS\x10\x01\x12\x0e\n\nLESS_EQUAL\x10\x02\x12\t\n\x05EQUAL\x10\x03\x12\x11\n\rGREATER_EQUAL\x10\x04\x12\x0b\n\x07GREATER\x10\x05\x12\r\n\tNOT_EQUAL\x10\x06B\x07\n\x05Value\x1a)\n\x0bCrowdingTag\x12\x1a\n\x12crowding_attribute\x18\x01 \x01(\t"f\n\nIndexStats\x12\x1a\n\rvectors_count\x18\x01 \x01(\x03B\x03\xe0A\x03\x12!\n\x14sparse_vectors_count\x18\x03 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cshards_count\x18\x02 \x01(\x05B\x03\xe0A\x03B\xc8\x01\n\x1ecom.google.cloud.aiplatform.v1B\nIndexProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.index_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\nIndexProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_INDEX_LABELSENTRY']._loaded_options = None
    _globals['_INDEX_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INDEX'].fields_by_name['name']._loaded_options = None
    _globals['_INDEX'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_INDEX'].fields_by_name['display_name']._loaded_options = None
    _globals['_INDEX'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_INDEX'].fields_by_name['metadata_schema_uri']._loaded_options = None
    _globals['_INDEX'].fields_by_name['metadata_schema_uri']._serialized_options = b'\xe0A\x05'
    _globals['_INDEX'].fields_by_name['deployed_indexes']._loaded_options = None
    _globals['_INDEX'].fields_by_name['deployed_indexes']._serialized_options = b'\xe0A\x03'
    _globals['_INDEX'].fields_by_name['create_time']._loaded_options = None
    _globals['_INDEX'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INDEX'].fields_by_name['update_time']._loaded_options = None
    _globals['_INDEX'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INDEX'].fields_by_name['index_stats']._loaded_options = None
    _globals['_INDEX'].fields_by_name['index_stats']._serialized_options = b'\xe0A\x03'
    _globals['_INDEX'].fields_by_name['index_update_method']._loaded_options = None
    _globals['_INDEX'].fields_by_name['index_update_method']._serialized_options = b'\xe0A\x05'
    _globals['_INDEX'].fields_by_name['encryption_spec']._loaded_options = None
    _globals['_INDEX'].fields_by_name['encryption_spec']._serialized_options = b'\xe0A\x05'
    _globals['_INDEX'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_INDEX'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_INDEX'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_INDEX'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_INDEX']._loaded_options = None
    _globals['_INDEX']._serialized_options = b'\xeaAZ\n\x1faiplatform.googleapis.com/Index\x127projects/{project}/locations/{location}/indexes/{index}'
    _globals['_INDEXDATAPOINT_SPARSEEMBEDDING'].fields_by_name['values']._loaded_options = None
    _globals['_INDEXDATAPOINT_SPARSEEMBEDDING'].fields_by_name['values']._serialized_options = b'\xe0A\x02'
    _globals['_INDEXDATAPOINT_SPARSEEMBEDDING'].fields_by_name['dimensions']._loaded_options = None
    _globals['_INDEXDATAPOINT_SPARSEEMBEDDING'].fields_by_name['dimensions']._serialized_options = b'\xe0A\x02'
    _globals['_INDEXDATAPOINT'].fields_by_name['datapoint_id']._loaded_options = None
    _globals['_INDEXDATAPOINT'].fields_by_name['datapoint_id']._serialized_options = b'\xe0A\x02'
    _globals['_INDEXDATAPOINT'].fields_by_name['feature_vector']._loaded_options = None
    _globals['_INDEXDATAPOINT'].fields_by_name['feature_vector']._serialized_options = b'\xe0A\x02'
    _globals['_INDEXDATAPOINT'].fields_by_name['sparse_embedding']._loaded_options = None
    _globals['_INDEXDATAPOINT'].fields_by_name['sparse_embedding']._serialized_options = b'\xe0A\x01'
    _globals['_INDEXDATAPOINT'].fields_by_name['restricts']._loaded_options = None
    _globals['_INDEXDATAPOINT'].fields_by_name['restricts']._serialized_options = b'\xe0A\x01'
    _globals['_INDEXDATAPOINT'].fields_by_name['numeric_restricts']._loaded_options = None
    _globals['_INDEXDATAPOINT'].fields_by_name['numeric_restricts']._serialized_options = b'\xe0A\x01'
    _globals['_INDEXDATAPOINT'].fields_by_name['crowding_tag']._loaded_options = None
    _globals['_INDEXDATAPOINT'].fields_by_name['crowding_tag']._serialized_options = b'\xe0A\x01'
    _globals['_INDEXDATAPOINT'].fields_by_name['embedding_metadata']._loaded_options = None
    _globals['_INDEXDATAPOINT'].fields_by_name['embedding_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_INDEXSTATS'].fields_by_name['vectors_count']._loaded_options = None
    _globals['_INDEXSTATS'].fields_by_name['vectors_count']._serialized_options = b'\xe0A\x03'
    _globals['_INDEXSTATS'].fields_by_name['sparse_vectors_count']._loaded_options = None
    _globals['_INDEXSTATS'].fields_by_name['sparse_vectors_count']._serialized_options = b'\xe0A\x03'
    _globals['_INDEXSTATS'].fields_by_name['shards_count']._loaded_options = None
    _globals['_INDEXSTATS'].fields_by_name['shards_count']._serialized_options = b'\xe0A\x03'
    _globals['_INDEX']._serialized_start = 297
    _globals['_INDEX']._serialized_end = 1229
    _globals['_INDEX_LABELSENTRY']._serialized_start = 994
    _globals['_INDEX_LABELSENTRY']._serialized_end = 1039
    _globals['_INDEX_INDEXUPDATEMETHOD']._serialized_start = 1041
    _globals['_INDEX_INDEXUPDATEMETHOD']._serialized_end = 1134
    _globals['_INDEXDATAPOINT']._serialized_start = 1232
    _globals['_INDEXDATAPOINT']._serialized_end = 2217
    _globals['_INDEXDATAPOINT_SPARSEEMBEDDING']._serialized_start = 1713
    _globals['_INDEXDATAPOINT_SPARSEEMBEDDING']._serialized_end = 1776
    _globals['_INDEXDATAPOINT_RESTRICTION']._serialized_start = 1778
    _globals['_INDEXDATAPOINT_RESTRICTION']._serialized_end = 1849
    _globals['_INDEXDATAPOINT_NUMERICRESTRICTION']._serialized_start = 1852
    _globals['_INDEXDATAPOINT_NUMERICRESTRICTION']._serialized_end = 2174
    _globals['_INDEXDATAPOINT_NUMERICRESTRICTION_OPERATOR']._serialized_start = 2045
    _globals['_INDEXDATAPOINT_NUMERICRESTRICTION_OPERATOR']._serialized_end = 2165
    _globals['_INDEXDATAPOINT_CROWDINGTAG']._serialized_start = 2176
    _globals['_INDEXDATAPOINT_CROWDINGTAG']._serialized_end = 2217
    _globals['_INDEXSTATS']._serialized_start = 2219
    _globals['_INDEXSTATS']._serialized_end = 2321