"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/llm_utility_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_content__pb2
from .....google.cloud.aiplatform.v1 import prediction_service_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_prediction__service__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/aiplatform/v1/llm_utility_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/aiplatform/v1/content.proto\x1a3google/cloud/aiplatform/v1/prediction_service.proto\x1a\x1cgoogle/protobuf/struct.proto"\xd4\x01\n\x14ComputeTokensRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12.\n\tinstances\x18\x02 \x03(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x01\x12\x12\n\x05model\x18\x03 \x01(\tB\x03\xe0A\x01\x12:\n\x08contents\x18\x04 \x03(\x0b2#.google.cloud.aiplatform.v1.ContentB\x03\xe0A\x01"B\n\nTokensInfo\x12\x0e\n\x06tokens\x18\x01 \x03(\x0c\x12\x11\n\ttoken_ids\x18\x02 \x03(\x03\x12\x11\n\x04role\x18\x03 \x01(\tB\x03\xe0A\x01"T\n\x15ComputeTokensResponse\x12;\n\x0btokens_info\x18\x01 \x03(\x0b2&.google.cloud.aiplatform.v1.TokensInfo2\xf8\x06\n\x11LlmUtilityService\x12\x81\x03\n\x0bCountTokens\x12..google.cloud.aiplatform.v1.CountTokensRequest\x1a/.google.cloud.aiplatform.v1.CountTokensResponse"\x90\x02\xdaA\x12endpoint,instances\x82\xd3\xe4\x93\x02\xf4\x01"=/v1/{endpoint=projects/*/locations/*/endpoints/*}:countTokens:\x01*ZL"G/v1/{endpoint=projects/*/locations/*/publishers/*/models/*}:countTokens:\x01*Z+"&/v1/{endpoint=endpoints/*}:countTokens:\x01*Z5"0/v1/{endpoint=publishers/*/models/*}:countTokens:\x01*\x12\x8f\x03\n\rComputeTokens\x120.google.cloud.aiplatform.v1.ComputeTokensRequest\x1a1.google.cloud.aiplatform.v1.ComputeTokensResponse"\x98\x02\xdaA\x12endpoint,instances\x82\xd3\xe4\x93\x02\xfc\x01"?/v1/{endpoint=projects/*/locations/*/endpoints/*}:computeTokens:\x01*ZN"I/v1/{endpoint=projects/*/locations/*/publishers/*/models/*}:computeTokens:\x01*Z-"(/v1/{endpoint=endpoints/*}:computeTokens:\x01*Z7"2/v1/{endpoint=publishers/*/models/*}:computeTokens:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd4\x01\n\x1ecom.google.cloud.aiplatform.v1B\x16LlmUtilityServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.llm_utility_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x16LlmUtilityServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
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
    _globals['_LLMUTILITYSERVICE'].methods_by_name['CountTokens']._loaded_options = None
    _globals['_LLMUTILITYSERVICE'].methods_by_name['CountTokens']._serialized_options = b'\xdaA\x12endpoint,instances\x82\xd3\xe4\x93\x02\xf4\x01"=/v1/{endpoint=projects/*/locations/*/endpoints/*}:countTokens:\x01*ZL"G/v1/{endpoint=projects/*/locations/*/publishers/*/models/*}:countTokens:\x01*Z+"&/v1/{endpoint=endpoints/*}:countTokens:\x01*Z5"0/v1/{endpoint=publishers/*/models/*}:countTokens:\x01*'
    _globals['_LLMUTILITYSERVICE'].methods_by_name['ComputeTokens']._loaded_options = None
    _globals['_LLMUTILITYSERVICE'].methods_by_name['ComputeTokens']._serialized_options = b'\xdaA\x12endpoint,instances\x82\xd3\xe4\x93\x02\xfc\x01"?/v1/{endpoint=projects/*/locations/*/endpoints/*}:computeTokens:\x01*ZN"I/v1/{endpoint=projects/*/locations/*/publishers/*/models/*}:computeTokens:\x01*Z-"(/v1/{endpoint=endpoints/*}:computeTokens:\x01*Z7"2/v1/{endpoint=publishers/*/models/*}:computeTokens:\x01*'
    _globals['_COMPUTETOKENSREQUEST']._serialized_start = 325
    _globals['_COMPUTETOKENSREQUEST']._serialized_end = 537
    _globals['_TOKENSINFO']._serialized_start = 539
    _globals['_TOKENSINFO']._serialized_end = 605
    _globals['_COMPUTETOKENSRESPONSE']._serialized_start = 607
    _globals['_COMPUTETOKENSRESPONSE']._serialized_end = 691
    _globals['_LLMUTILITYSERVICE']._serialized_start = 694
    _globals['_LLMUTILITYSERVICE']._serialized_end = 1582