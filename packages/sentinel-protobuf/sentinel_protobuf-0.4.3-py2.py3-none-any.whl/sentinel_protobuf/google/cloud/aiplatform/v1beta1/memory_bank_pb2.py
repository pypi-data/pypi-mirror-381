"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/memory_bank.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/aiplatform/v1beta1/memory_bank.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd4\x04\n\x06Memory\x126\n\x0bexpire_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01H\x00\x12-\n\x03ttl\x18\x0e \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01H\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04fact\x18\n \x01(\tB\x03\xe0A\x02\x12F\n\x05scope\x18\x0b \x03(\x0b22.google.cloud.aiplatform.v1beta1.Memory.ScopeEntryB\x03\xe0A\x02\x1a,\n\nScopeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x97\x01\xeaA\x93\x01\n aiplatform.googleapis.com/Memory\x12]projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/memories/{memory}*\x08memories2\x06memoryB\x0c\n\nexpirationB\xe6\x01\n#com.google.cloud.aiplatform.v1beta1B\x0fMemoryBankProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.memory_bank_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x0fMemoryBankProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_MEMORY_SCOPEENTRY']._loaded_options = None
    _globals['_MEMORY_SCOPEENTRY']._serialized_options = b'8\x01'
    _globals['_MEMORY'].fields_by_name['expire_time']._loaded_options = None
    _globals['_MEMORY'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x01'
    _globals['_MEMORY'].fields_by_name['ttl']._loaded_options = None
    _globals['_MEMORY'].fields_by_name['ttl']._serialized_options = b'\xe0A\x01'
    _globals['_MEMORY'].fields_by_name['name']._loaded_options = None
    _globals['_MEMORY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_MEMORY'].fields_by_name['display_name']._loaded_options = None
    _globals['_MEMORY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_MEMORY'].fields_by_name['description']._loaded_options = None
    _globals['_MEMORY'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_MEMORY'].fields_by_name['create_time']._loaded_options = None
    _globals['_MEMORY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MEMORY'].fields_by_name['update_time']._loaded_options = None
    _globals['_MEMORY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MEMORY'].fields_by_name['fact']._loaded_options = None
    _globals['_MEMORY'].fields_by_name['fact']._serialized_options = b'\xe0A\x02'
    _globals['_MEMORY'].fields_by_name['scope']._loaded_options = None
    _globals['_MEMORY'].fields_by_name['scope']._serialized_options = b'\xe0A\x02'
    _globals['_MEMORY']._loaded_options = None
    _globals['_MEMORY']._serialized_options = b'\xeaA\x93\x01\n aiplatform.googleapis.com/Memory\x12]projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/memories/{memory}*\x08memories2\x06memory'
    _globals['_MEMORY']._serialized_start = 212
    _globals['_MEMORY']._serialized_end = 808
    _globals['_MEMORY_SCOPEENTRY']._serialized_start = 596
    _globals['_MEMORY_SCOPEENTRY']._serialized_end = 640