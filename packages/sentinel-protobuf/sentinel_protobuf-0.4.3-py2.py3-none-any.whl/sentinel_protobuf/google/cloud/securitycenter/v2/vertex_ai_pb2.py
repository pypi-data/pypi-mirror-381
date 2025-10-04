"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/securitycenter/v2/vertex_ai.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/securitycenter/v2/vertex_ai.proto\x12\x1egoogle.cloud.securitycenter.v2"\x83\x02\n\x08VertexAi\x12B\n\x08datasets\x18\x01 \x03(\x0b20.google.cloud.securitycenter.v2.VertexAi.Dataset\x12D\n\tpipelines\x18\x02 \x03(\x0b21.google.cloud.securitycenter.v2.VertexAi.Pipeline\x1a=\n\x07Dataset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x1a.\n\x08Pipeline\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\tB\xe7\x01\n"com.google.cloud.securitycenter.v2B\rVertexAiProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.vertex_ai_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\rVertexAiProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_VERTEXAI']._serialized_start = 83
    _globals['_VERTEXAI']._serialized_end = 342
    _globals['_VERTEXAI_DATASET']._serialized_start = 233
    _globals['_VERTEXAI_DATASET']._serialized_end = 294
    _globals['_VERTEXAI_PIPELINE']._serialized_start = 296
    _globals['_VERTEXAI_PIPELINE']._serialized_end = 342