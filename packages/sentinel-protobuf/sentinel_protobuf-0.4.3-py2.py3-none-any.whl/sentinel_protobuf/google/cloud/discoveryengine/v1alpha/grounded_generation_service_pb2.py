"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1alpha/grounded_generation_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import grounding_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_grounding__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/cloud/discoveryengine/v1alpha/grounded_generation_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/discoveryengine/v1alpha/grounding.proto"L\n\x12CheckGroundingSpec\x12\x1f\n\x12citation_threshold\x18\x01 \x01(\x01H\x00\x88\x01\x01B\x15\n\x13_citation_threshold"\xae\x03\n\x15CheckGroundingRequest\x12P\n\x10grounding_config\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.discoveryengine.googleapis.com/GroundingConfig\x12\x18\n\x10answer_candidate\x18\x02 \x01(\t\x12B\n\x05facts\x18\x03 \x03(\x0b23.google.cloud.discoveryengine.v1alpha.GroundingFact\x12P\n\x0egrounding_spec\x18\x04 \x01(\x0b28.google.cloud.discoveryengine.v1alpha.CheckGroundingSpec\x12`\n\x0buser_labels\x18\x05 \x03(\x0b2K.google.cloud.discoveryengine.v1alpha.CheckGroundingRequest.UserLabelsEntry\x1a1\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xa5\x03\n\x16CheckGroundingResponse\x12\x1a\n\rsupport_score\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12E\n\x0ccited_chunks\x18\x03 \x03(\x0b2/.google.cloud.discoveryengine.v1alpha.FactChunk\x12R\n\x06claims\x18\x04 \x03(\x0b2B.google.cloud.discoveryengine.v1alpha.CheckGroundingResponse.Claim\x1a\xc1\x01\n\x05Claim\x12\x16\n\tstart_pos\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07end_pos\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x12\n\nclaim_text\x18\x03 \x01(\t\x12\x18\n\x10citation_indices\x18\x04 \x03(\x05\x12%\n\x18grounding_check_required\x18\x06 \x01(\x08H\x02\x88\x01\x01B\x0c\n\n_start_posB\n\n\x08_end_posB\x1b\n\x19_grounding_check_requiredB\x10\n\x0e_support_score2\xd5\x02\n\x19GroundedGenerationService\x12\xe3\x01\n\x0eCheckGrounding\x12;.google.cloud.discoveryengine.v1alpha.CheckGroundingRequest\x1a<.google.cloud.discoveryengine.v1alpha.CheckGroundingResponse"V\x82\xd3\xe4\x93\x02P"K/v1alpha/{grounding_config=projects/*/locations/*/groundingConfigs/*}:check:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xaa\x02\n(com.google.cloud.discoveryengine.v1alphaB\x1eGroundedGenerationServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.grounded_generation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x1eGroundedGenerationServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_CHECKGROUNDINGREQUEST_USERLABELSENTRY']._loaded_options = None
    _globals['_CHECKGROUNDINGREQUEST_USERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CHECKGROUNDINGREQUEST'].fields_by_name['grounding_config']._loaded_options = None
    _globals['_CHECKGROUNDINGREQUEST'].fields_by_name['grounding_config']._serialized_options = b'\xe0A\x02\xfaA0\n.discoveryengine.googleapis.com/GroundingConfig'
    _globals['_GROUNDEDGENERATIONSERVICE']._loaded_options = None
    _globals['_GROUNDEDGENERATIONSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_GROUNDEDGENERATIONSERVICE'].methods_by_name['CheckGrounding']._loaded_options = None
    _globals['_GROUNDEDGENERATIONSERVICE'].methods_by_name['CheckGrounding']._serialized_options = b'\x82\xd3\xe4\x93\x02P"K/v1alpha/{grounding_config=projects/*/locations/*/groundingConfigs/*}:check:\x01*'
    _globals['_CHECKGROUNDINGSPEC']._serialized_start = 281
    _globals['_CHECKGROUNDINGSPEC']._serialized_end = 357
    _globals['_CHECKGROUNDINGREQUEST']._serialized_start = 360
    _globals['_CHECKGROUNDINGREQUEST']._serialized_end = 790
    _globals['_CHECKGROUNDINGREQUEST_USERLABELSENTRY']._serialized_start = 741
    _globals['_CHECKGROUNDINGREQUEST_USERLABELSENTRY']._serialized_end = 790
    _globals['_CHECKGROUNDINGRESPONSE']._serialized_start = 793
    _globals['_CHECKGROUNDINGRESPONSE']._serialized_end = 1214
    _globals['_CHECKGROUNDINGRESPONSE_CLAIM']._serialized_start = 1003
    _globals['_CHECKGROUNDINGRESPONSE_CLAIM']._serialized_end = 1196
    _globals['_GROUNDEDGENERATIONSERVICE']._serialized_start = 1217
    _globals['_GROUNDEDGENERATIONSERVICE']._serialized_end = 1558