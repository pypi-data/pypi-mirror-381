"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/example.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.aiplatform.v1beta1 import content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_content__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/aiplatform/v1beta1/example.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a-google/cloud/aiplatform/v1beta1/content.proto"\x87\x02\n\x0fContentsExample\x12?\n\x08contents\x18\x01 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.ContentB\x03\xe0A\x02\x12`\n\x11expected_contents\x18\x02 \x03(\x0b2@.google.cloud.aiplatform.v1beta1.ContentsExample.ExpectedContentB\x03\xe0A\x02\x1aQ\n\x0fExpectedContent\x12>\n\x07content\x18\x01 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.ContentB\x03\xe0A\x02"\xa5\x03\n\x15StoredContentsExample\x12\x17\n\nsearch_key\x18\x01 \x01(\tB\x03\xe0A\x01\x12O\n\x10contents_example\x18\x02 \x01(\x0b20.google.cloud.aiplatform.v1beta1.ContentsExampleB\x03\xe0A\x02\x12{\n\x1csearch_key_generation_method\x18\x03 \x01(\x0b2P.google.cloud.aiplatform.v1beta1.StoredContentsExample.SearchKeyGenerationMethodB\x03\xe0A\x01\x1a\xa4\x01\n\x19SearchKeyGenerationMethod\x12p\n\nlast_entry\x18\x01 \x01(\x0b2Z.google.cloud.aiplatform.v1beta1.StoredContentsExample.SearchKeyGenerationMethod.LastEntryH\x00\x1a\x0b\n\tLastEntryB\x08\n\x06methodB\xe3\x01\n#com.google.cloud.aiplatform.v1beta1B\x0cExampleProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.example_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x0cExampleProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CONTENTSEXAMPLE_EXPECTEDCONTENT'].fields_by_name['content']._loaded_options = None
    _globals['_CONTENTSEXAMPLE_EXPECTEDCONTENT'].fields_by_name['content']._serialized_options = b'\xe0A\x02'
    _globals['_CONTENTSEXAMPLE'].fields_by_name['contents']._loaded_options = None
    _globals['_CONTENTSEXAMPLE'].fields_by_name['contents']._serialized_options = b'\xe0A\x02'
    _globals['_CONTENTSEXAMPLE'].fields_by_name['expected_contents']._loaded_options = None
    _globals['_CONTENTSEXAMPLE'].fields_by_name['expected_contents']._serialized_options = b'\xe0A\x02'
    _globals['_STOREDCONTENTSEXAMPLE'].fields_by_name['search_key']._loaded_options = None
    _globals['_STOREDCONTENTSEXAMPLE'].fields_by_name['search_key']._serialized_options = b'\xe0A\x01'
    _globals['_STOREDCONTENTSEXAMPLE'].fields_by_name['contents_example']._loaded_options = None
    _globals['_STOREDCONTENTSEXAMPLE'].fields_by_name['contents_example']._serialized_options = b'\xe0A\x02'
    _globals['_STOREDCONTENTSEXAMPLE'].fields_by_name['search_key_generation_method']._loaded_options = None
    _globals['_STOREDCONTENTSEXAMPLE'].fields_by_name['search_key_generation_method']._serialized_options = b'\xe0A\x01'
    _globals['_CONTENTSEXAMPLE']._serialized_start = 163
    _globals['_CONTENTSEXAMPLE']._serialized_end = 426
    _globals['_CONTENTSEXAMPLE_EXPECTEDCONTENT']._serialized_start = 345
    _globals['_CONTENTSEXAMPLE_EXPECTEDCONTENT']._serialized_end = 426
    _globals['_STOREDCONTENTSEXAMPLE']._serialized_start = 429
    _globals['_STOREDCONTENTSEXAMPLE']._serialized_end = 850
    _globals['_STOREDCONTENTSEXAMPLE_SEARCHKEYGENERATIONMETHOD']._serialized_start = 686
    _globals['_STOREDCONTENTSEXAMPLE_SEARCHKEYGENERATIONMETHOD']._serialized_end = 850
    _globals['_STOREDCONTENTSEXAMPLE_SEARCHKEYGENERATIONMETHOD_LASTENTRY']._serialized_start = 829
    _globals['_STOREDCONTENTSEXAMPLE_SEARCHKEYGENERATIONMETHOD_LASTENTRY']._serialized_end = 840