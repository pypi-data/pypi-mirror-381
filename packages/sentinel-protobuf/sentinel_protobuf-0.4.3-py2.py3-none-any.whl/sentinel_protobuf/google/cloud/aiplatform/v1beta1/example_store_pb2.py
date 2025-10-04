"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/example_store.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_content__pb2
from .....google.cloud.aiplatform.v1beta1 import example_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_example__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/aiplatform/v1beta1/example_store.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/aiplatform/v1beta1/content.proto\x1a-google/cloud/aiplatform/v1beta1/example.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xad\x03\n\x0cExampleStore\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12V\n\x14example_store_config\x18\x06 \x01(\x0b23.google.cloud.aiplatform.v1beta1.ExampleStoreConfigB\x03\xe0A\x02:\x90\x01\xeaA\x8c\x01\n&aiplatform.googleapis.com/ExampleStore\x12Eprojects/{project}/locations/{location}/exampleStores/{example_store}*\rexampleStores2\x0cexampleStore"9\n\x12ExampleStoreConfig\x12#\n\x16vertex_embedding_model\x18\x01 \x01(\tB\x03\xe0A\x02"\x8a\x01\n\x1bStoredContentsExampleFilter\x12\x18\n\x0bsearch_keys\x18\x01 \x03(\tB\x03\xe0A\x01\x12Q\n\x0efunction_names\x18\x02 \x01(\x0b24.google.cloud.aiplatform.v1beta1.ExamplesArrayFilterB\x03\xe0A\x01"\xd7\x03\n\x1fStoredContentsExampleParameters\x12\x14\n\nsearch_key\x18\x01 \x01(\tH\x00\x12o\n\x12content_search_key\x18\x02 \x01(\x0b2Q.google.cloud.aiplatform.v1beta1.StoredContentsExampleParameters.ContentSearchKeyH\x00\x12Q\n\x0efunction_names\x18\x03 \x01(\x0b24.google.cloud.aiplatform.v1beta1.ExamplesArrayFilterB\x03\xe0A\x01\x1a\xd0\x01\n\x10ContentSearchKey\x12?\n\x08contents\x18\x01 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.ContentB\x03\xe0A\x02\x12{\n\x1csearch_key_generation_method\x18\x02 \x01(\x0b2P.google.cloud.aiplatform.v1beta1.StoredContentsExample.SearchKeyGenerationMethodB\x03\xe0A\x02B\x07\n\x05query"\xe0\x01\n\x13ExamplesArrayFilter\x12\x13\n\x06values\x18\x01 \x03(\tB\x03\xe0A\x02\x12_\n\x0earray_operator\x18\x02 \x01(\x0e2B.google.cloud.aiplatform.v1beta1.ExamplesArrayFilter.ArrayOperatorB\x03\xe0A\x02"S\n\rArrayOperator\x12\x1e\n\x1aARRAY_OPERATOR_UNSPECIFIED\x10\x00\x12\x10\n\x0cCONTAINS_ANY\x10\x01\x12\x10\n\x0cCONTAINS_ALL\x10\x02B\xe8\x01\n#com.google.cloud.aiplatform.v1beta1B\x11ExampleStoreProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.example_store_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x11ExampleStoreProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_EXAMPLESTORE'].fields_by_name['name']._loaded_options = None
    _globals['_EXAMPLESTORE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_EXAMPLESTORE'].fields_by_name['display_name']._loaded_options = None
    _globals['_EXAMPLESTORE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_EXAMPLESTORE'].fields_by_name['description']._loaded_options = None
    _globals['_EXAMPLESTORE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_EXAMPLESTORE'].fields_by_name['create_time']._loaded_options = None
    _globals['_EXAMPLESTORE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXAMPLESTORE'].fields_by_name['update_time']._loaded_options = None
    _globals['_EXAMPLESTORE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXAMPLESTORE'].fields_by_name['example_store_config']._loaded_options = None
    _globals['_EXAMPLESTORE'].fields_by_name['example_store_config']._serialized_options = b'\xe0A\x02'
    _globals['_EXAMPLESTORE']._loaded_options = None
    _globals['_EXAMPLESTORE']._serialized_options = b'\xeaA\x8c\x01\n&aiplatform.googleapis.com/ExampleStore\x12Eprojects/{project}/locations/{location}/exampleStores/{example_store}*\rexampleStores2\x0cexampleStore'
    _globals['_EXAMPLESTORECONFIG'].fields_by_name['vertex_embedding_model']._loaded_options = None
    _globals['_EXAMPLESTORECONFIG'].fields_by_name['vertex_embedding_model']._serialized_options = b'\xe0A\x02'
    _globals['_STOREDCONTENTSEXAMPLEFILTER'].fields_by_name['search_keys']._loaded_options = None
    _globals['_STOREDCONTENTSEXAMPLEFILTER'].fields_by_name['search_keys']._serialized_options = b'\xe0A\x01'
    _globals['_STOREDCONTENTSEXAMPLEFILTER'].fields_by_name['function_names']._loaded_options = None
    _globals['_STOREDCONTENTSEXAMPLEFILTER'].fields_by_name['function_names']._serialized_options = b'\xe0A\x01'
    _globals['_STOREDCONTENTSEXAMPLEPARAMETERS_CONTENTSEARCHKEY'].fields_by_name['contents']._loaded_options = None
    _globals['_STOREDCONTENTSEXAMPLEPARAMETERS_CONTENTSEARCHKEY'].fields_by_name['contents']._serialized_options = b'\xe0A\x02'
    _globals['_STOREDCONTENTSEXAMPLEPARAMETERS_CONTENTSEARCHKEY'].fields_by_name['search_key_generation_method']._loaded_options = None
    _globals['_STOREDCONTENTSEXAMPLEPARAMETERS_CONTENTSEARCHKEY'].fields_by_name['search_key_generation_method']._serialized_options = b'\xe0A\x02'
    _globals['_STOREDCONTENTSEXAMPLEPARAMETERS'].fields_by_name['function_names']._loaded_options = None
    _globals['_STOREDCONTENTSEXAMPLEPARAMETERS'].fields_by_name['function_names']._serialized_options = b'\xe0A\x01'
    _globals['_EXAMPLESARRAYFILTER'].fields_by_name['values']._loaded_options = None
    _globals['_EXAMPLESARRAYFILTER'].fields_by_name['values']._serialized_options = b'\xe0A\x02'
    _globals['_EXAMPLESARRAYFILTER'].fields_by_name['array_operator']._loaded_options = None
    _globals['_EXAMPLESARRAYFILTER'].fields_by_name['array_operator']._serialized_options = b'\xe0A\x02'
    _globals['_EXAMPLESTORE']._serialized_start = 276
    _globals['_EXAMPLESTORE']._serialized_end = 705
    _globals['_EXAMPLESTORECONFIG']._serialized_start = 707
    _globals['_EXAMPLESTORECONFIG']._serialized_end = 764
    _globals['_STOREDCONTENTSEXAMPLEFILTER']._serialized_start = 767
    _globals['_STOREDCONTENTSEXAMPLEFILTER']._serialized_end = 905
    _globals['_STOREDCONTENTSEXAMPLEPARAMETERS']._serialized_start = 908
    _globals['_STOREDCONTENTSEXAMPLEPARAMETERS']._serialized_end = 1379
    _globals['_STOREDCONTENTSEXAMPLEPARAMETERS_CONTENTSEARCHKEY']._serialized_start = 1162
    _globals['_STOREDCONTENTSEXAMPLEPARAMETERS_CONTENTSEARCHKEY']._serialized_end = 1370
    _globals['_EXAMPLESARRAYFILTER']._serialized_start = 1382
    _globals['_EXAMPLESARRAYFILTER']._serialized_end = 1606
    _globals['_EXAMPLESARRAYFILTER_ARRAYOPERATOR']._serialized_start = 1523
    _globals['_EXAMPLESARRAYFILTER_ARRAYOPERATOR']._serialized_end = 1606