"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/llm_utility_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_content__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/aiplatform/v1beta1/llm_utility_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/aiplatform/v1beta1/content.proto\x1a\x1cgoogle/protobuf/struct.proto"\xd9\x01\n\x14ComputeTokensRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12.\n\tinstances\x18\x02 \x03(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x01\x12\x12\n\x05model\x18\x03 \x01(\tB\x03\xe0A\x01\x12?\n\x08contents\x18\x04 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.ContentB\x03\xe0A\x01"B\n\nTokensInfo\x12\x0e\n\x06tokens\x18\x01 \x03(\x0c\x12\x11\n\ttoken_ids\x18\x02 \x03(\x03\x12\x11\n\x04role\x18\x03 \x01(\tB\x03\xe0A\x01"Y\n\x15ComputeTokensResponse\x12@\n\x0btokens_info\x18\x01 \x03(\x0b2+.google.cloud.aiplatform.v1beta1.TokensInfo2\x92\x04\n\x11LlmUtilityService\x12\xad\x03\n\rComputeTokens\x125.google.cloud.aiplatform.v1beta1.ComputeTokensRequest\x1a6.google.cloud.aiplatform.v1beta1.ComputeTokensResponse"\xac\x02\xdaA\x12endpoint,instances\x82\xd3\xe4\x93\x02\x90\x02"D/v1beta1/{endpoint=projects/*/locations/*/endpoints/*}:computeTokens:\x01*ZS"N/v1beta1/{endpoint=projects/*/locations/*/publishers/*/models/*}:computeTokens:\x01*Z2"-/v1beta1/{endpoint=endpoints/*}:computeTokens:\x01*Z<"7/v1beta1/{endpoint=publishers/*/models/*}:computeTokens:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xed\x01\n#com.google.cloud.aiplatform.v1beta1B\x16LlmUtilityServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.llm_utility_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x16LlmUtilityServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_COMPUTETOKENSREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_COMPUTETOKENSREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_COMPUTETOKENSREQUEST'].fields_by_name['instances']._loaded_options = None
    _globals['_COMPUTETOKENSREQUEST'].fields_by_name['instances']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTETOKENSREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_COMPUTETOKENSREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTETOKENSREQUEST'].fields_by_name['contents']._loaded_options = None
    _globals['_COMPUTETOKENSREQUEST'].fields_by_name['contents']._serialized_options = b'\xe0A\x01'
    _globals['_TOKENSINFO'].fields_by_name['role']._loaded_options = None
    _globals['_TOKENSINFO'].fields_by_name['role']._serialized_options = b'\xe0A\x01'
    _globals['_LLMUTILITYSERVICE']._loaded_options = None
    _globals['_LLMUTILITYSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_LLMUTILITYSERVICE'].methods_by_name['ComputeTokens']._loaded_options = None
    _globals['_LLMUTILITYSERVICE'].methods_by_name['ComputeTokens']._serialized_options = b'\xdaA\x12endpoint,instances\x82\xd3\xe4\x93\x02\x90\x02"D/v1beta1/{endpoint=projects/*/locations/*/endpoints/*}:computeTokens:\x01*ZS"N/v1beta1/{endpoint=projects/*/locations/*/publishers/*/models/*}:computeTokens:\x01*Z2"-/v1beta1/{endpoint=endpoints/*}:computeTokens:\x01*Z<"7/v1beta1/{endpoint=publishers/*/models/*}:computeTokens:\x01*'
    _globals['_COMPUTETOKENSREQUEST']._serialized_start = 287
    _globals['_COMPUTETOKENSREQUEST']._serialized_end = 504
    _globals['_TOKENSINFO']._serialized_start = 506
    _globals['_TOKENSINFO']._serialized_end = 572
    _globals['_COMPUTETOKENSRESPONSE']._serialized_start = 574
    _globals['_COMPUTETOKENSRESPONSE']._serialized_end = 663
    _globals['_LLMUTILITYSERVICE']._serialized_start = 666
    _globals['_LLMUTILITYSERVICE']._serialized_end = 1196