"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/cached_content.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_content__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import tool_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_tool__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/aiplatform/v1beta1/cached_content.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/aiplatform/v1beta1/content.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a*google/cloud/aiplatform/v1beta1/tool.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb4\x08\n\rCachedContent\x121\n\x0bexpire_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12-\n\x03ttl\x18\n \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x04H\x00\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x08\xe0A\x05\x12\x1c\n\x0cdisplay_name\x18\x0b \x01(\tB\x06\xe0A\x01\xe0A\x05\x12\x12\n\x05model\x18\x02 \x01(\tB\x03\xe0A\x05\x12O\n\x12system_instruction\x18\x03 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.ContentB\t\xe0A\x01\xe0A\x05\xe0A\x04\x12E\n\x08contents\x18\x04 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.ContentB\t\xe0A\x01\xe0A\x05\xe0A\x04\x12?\n\x05tools\x18\x05 \x03(\x0b2%.google.cloud.aiplatform.v1beta1.ToolB\t\xe0A\x01\xe0A\x05\xe0A\x04\x12K\n\x0btool_config\x18\x06 \x01(\x0b2+.google.cloud.aiplatform.v1beta1.ToolConfigB\t\xe0A\x01\xe0A\x05\xe0A\x04\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Y\n\x0eusage_metadata\x18\x0c \x01(\x0b2<.google.cloud.aiplatform.v1beta1.CachedContent.UsageMetadataB\x03\xe0A\x03\x12P\n\x0fencryption_spec\x18\r \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpecB\x06\xe0A\x04\xe0A\x05\x1a\x93\x01\n\rUsageMetadata\x12\x19\n\x11total_token_count\x18\x01 \x01(\x05\x12\x12\n\ntext_count\x18\x02 \x01(\x05\x12\x13\n\x0bimage_count\x18\x03 \x01(\x05\x12\x1e\n\x16video_duration_seconds\x18\x04 \x01(\x05\x12\x1e\n\x16audio_duration_seconds\x18\x05 \x01(\x05:\x95\x01\xeaA\x91\x01\n\'aiplatform.googleapis.com/CachedContent\x12Gprojects/{project}/locations/{location}/cachedContents/{cached_content}*\x0ecachedContents2\rcachedContentB\x0c\n\nexpirationB\xe9\x01\n#com.google.cloud.aiplatform.v1beta1B\x12CachedContentProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.cached_content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x12CachedContentProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CACHEDCONTENT'].fields_by_name['ttl']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['ttl']._serialized_options = b'\xe0A\x04'
    _globals['_CACHEDCONTENT'].fields_by_name['name']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xe0A\x05'
    _globals['_CACHEDCONTENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_CACHEDCONTENT'].fields_by_name['model']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['model']._serialized_options = b'\xe0A\x05'
    _globals['_CACHEDCONTENT'].fields_by_name['system_instruction']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['system_instruction']._serialized_options = b'\xe0A\x01\xe0A\x05\xe0A\x04'
    _globals['_CACHEDCONTENT'].fields_by_name['contents']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['contents']._serialized_options = b'\xe0A\x01\xe0A\x05\xe0A\x04'
    _globals['_CACHEDCONTENT'].fields_by_name['tools']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['tools']._serialized_options = b'\xe0A\x01\xe0A\x05\xe0A\x04'
    _globals['_CACHEDCONTENT'].fields_by_name['tool_config']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['tool_config']._serialized_options = b'\xe0A\x01\xe0A\x05\xe0A\x04'
    _globals['_CACHEDCONTENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CACHEDCONTENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CACHEDCONTENT'].fields_by_name['usage_metadata']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['usage_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_CACHEDCONTENT'].fields_by_name['encryption_spec']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['encryption_spec']._serialized_options = b'\xe0A\x04\xe0A\x05'
    _globals['_CACHEDCONTENT']._loaded_options = None
    _globals['_CACHEDCONTENT']._serialized_options = b"\xeaA\x91\x01\n'aiplatform.googleapis.com/CachedContent\x12Gprojects/{project}/locations/{location}/cachedContents/{cached_content}*\x0ecachedContents2\rcachedContent"
    _globals['_CACHEDCONTENT']._serialized_start = 361
    _globals['_CACHEDCONTENT']._serialized_end = 1437
    _globals['_CACHEDCONTENT_USAGEMETADATA']._serialized_start = 1124
    _globals['_CACHEDCONTENT_USAGEMETADATA']._serialized_end = 1271