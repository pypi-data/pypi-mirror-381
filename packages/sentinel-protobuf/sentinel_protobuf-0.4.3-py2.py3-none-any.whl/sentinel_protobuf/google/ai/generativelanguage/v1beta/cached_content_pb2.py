"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1beta/cached_content.proto')
_sym_db = _symbol_database.Default()
from .....google.ai.generativelanguage.v1beta import content_pb2 as google_dot_ai_dot_generativelanguage_dot_v1beta_dot_content__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ai/generativelanguage/v1beta/cached_content.proto\x12#google.ai.generativelanguage.v1beta\x1a1google/ai/generativelanguage/v1beta/content.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf1\x07\n\rCachedContent\x121\n\x0bexpire_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12-\n\x03ttl\x18\n \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x04H\x00\x12\x19\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x08\xe0A\x03H\x01\x88\x01\x01\x12!\n\x0cdisplay_name\x18\x0b \x01(\tB\x06\xe0A\x01\xe0A\x05H\x02\x88\x01\x01\x12F\n\x05model\x18\x02 \x01(\tB2\xe0A\x05\xe0A\x02\xfaA)\n\'generativelanguage.googleapis.com/ModelH\x03\x88\x01\x01\x12X\n\x12system_instruction\x18\x03 \x01(\x0b2,.google.ai.generativelanguage.v1beta.ContentB\t\xe0A\x01\xe0A\x05\xe0A\x04H\x04\x88\x01\x01\x12I\n\x08contents\x18\x04 \x03(\x0b2,.google.ai.generativelanguage.v1beta.ContentB\t\xe0A\x01\xe0A\x05\xe0A\x04\x12C\n\x05tools\x18\x05 \x03(\x0b2).google.ai.generativelanguage.v1beta.ToolB\t\xe0A\x01\xe0A\x05\xe0A\x04\x12T\n\x0btool_config\x18\x06 \x01(\x0b2/.google.ai.generativelanguage.v1beta.ToolConfigB\t\xe0A\x01\xe0A\x05\xe0A\x04H\x05\x88\x01\x01\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12]\n\x0eusage_metadata\x18\x0c \x01(\x0b2@.google.ai.generativelanguage.v1beta.CachedContent.UsageMetadataB\x03\xe0A\x03\x1a*\n\rUsageMetadata\x12\x19\n\x11total_token_count\x18\x01 \x01(\x05:h\xeaAe\n/generativelanguage.googleapis.com/CachedContent\x12\x13cachedContents/{id}*\x0ecachedContents2\rcachedContentB\x0c\n\nexpirationB\x07\n\x05_nameB\x0f\n\r_display_nameB\x08\n\x06_modelB\x15\n\x13_system_instructionB\x0e\n\x0c_tool_configB\x9e\x01\n\'com.google.ai.generativelanguage.v1betaB\x12CachedContentProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta.cached_content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.ai.generativelanguage.v1betaB\x12CachedContentProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepb"
    _globals['_CACHEDCONTENT'].fields_by_name['ttl']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['ttl']._serialized_options = b'\xe0A\x04'
    _globals['_CACHEDCONTENT'].fields_by_name['name']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xe0A\x03'
    _globals['_CACHEDCONTENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_CACHEDCONTENT'].fields_by_name['model']._loaded_options = None
    _globals['_CACHEDCONTENT'].fields_by_name['model']._serialized_options = b"\xe0A\x05\xe0A\x02\xfaA)\n'generativelanguage.googleapis.com/Model"
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
    _globals['_CACHEDCONTENT']._loaded_options = None
    _globals['_CACHEDCONTENT']._serialized_options = b'\xeaAe\n/generativelanguage.googleapis.com/CachedContent\x12\x13cachedContents/{id}*\x0ecachedContents2\rcachedContent'
    _globals['_CACHEDCONTENT']._serialized_start = 274
    _globals['_CACHEDCONTENT']._serialized_end = 1283
    _globals['_CACHEDCONTENT_USAGEMETADATA']._serialized_start = 1046
    _globals['_CACHEDCONTENT_USAGEMETADATA']._serialized_end = 1088