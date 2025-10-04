"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/securitycenter/v2/ai_model.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/securitycenter/v2/ai_model.proto\x12\x1egoogle.cloud.securitycenter.v2"\xbe\x02\n\x07AiModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06domain\x18\x02 \x01(\t\x12\x0f\n\x07library\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x11\n\tpublisher\x18\x05 \x01(\t\x12W\n\x13deployment_platform\x18\x06 \x01(\x0e2:.google.cloud.securitycenter.v2.AiModel.DeploymentPlatform\x12\x14\n\x0cdisplay_name\x18\x07 \x01(\t"p\n\x12DeploymentPlatform\x12#\n\x1fDEPLOYMENT_PLATFORM_UNSPECIFIED\x10\x00\x12\r\n\tVERTEX_AI\x10\x01\x12\x07\n\x03GKE\x10\x02\x12\x07\n\x03GCE\x10\x03\x12\x14\n\x10FINE_TUNED_MODEL\x10\x04B\xe6\x01\n"com.google.cloud.securitycenter.v2B\x0cAiModelProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.ai_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x0cAiModelProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_AIMODEL']._serialized_start = 82
    _globals['_AIMODEL']._serialized_end = 400
    _globals['_AIMODEL_DEPLOYMENTPLATFORM']._serialized_start = 288
    _globals['_AIMODEL_DEPLOYMENTPLATFORM']._serialized_end = 400