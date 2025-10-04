"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/context.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/aiplatform/v1/context.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd3\x04\n\x07Context\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x0c\n\x04etag\x18\x08 \x01(\t\x12?\n\x06labels\x18\t \x03(\x0b2/.google.cloud.aiplatform.v1.Context.LabelsEntry\x124\n\x0bcreate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12B\n\x0fparent_contexts\x18\x0c \x03(\tB)\xe0A\x03\xfaA#\n!aiplatform.googleapis.com/Context\x12\x14\n\x0cschema_title\x18\r \x01(\t\x12\x16\n\x0eschema_version\x18\x0e \x01(\t\x12)\n\x08metadata\x18\x0f \x01(\x0b2\x17.google.protobuf.Struct\x12\x13\n\x0bdescription\x18\x10 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x82\x01\xeaA\x7f\n!aiplatform.googleapis.com/Context\x12Zprojects/{project}/locations/{location}/metadataStores/{metadata_store}/contexts/{context}B\xca\x01\n\x1ecom.google.cloud.aiplatform.v1B\x0cContextProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.context_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x0cContextProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_CONTEXT_LABELSENTRY']._loaded_options = None
    _globals['_CONTEXT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CONTEXT'].fields_by_name['name']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_CONTEXT'].fields_by_name['create_time']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONTEXT'].fields_by_name['update_time']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONTEXT'].fields_by_name['parent_contexts']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['parent_contexts']._serialized_options = b'\xe0A\x03\xfaA#\n!aiplatform.googleapis.com/Context'
    _globals['_CONTEXT']._loaded_options = None
    _globals['_CONTEXT']._serialized_options = b'\xeaA\x7f\n!aiplatform.googleapis.com/Context\x12Zprojects/{project}/locations/{location}/metadataStores/{metadata_store}/contexts/{context}'
    _globals['_CONTEXT']._serialized_start = 196
    _globals['_CONTEXT']._serialized_end = 791
    _globals['_CONTEXT_LABELSENTRY']._serialized_start = 613
    _globals['_CONTEXT_LABELSENTRY']._serialized_end = 658