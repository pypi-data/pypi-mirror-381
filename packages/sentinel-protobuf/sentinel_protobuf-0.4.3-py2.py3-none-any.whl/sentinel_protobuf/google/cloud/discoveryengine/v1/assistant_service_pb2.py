"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/assistant_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import assist_answer_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_assist__answer__pb2
from .....google.cloud.discoveryengine.v1 import search_service_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_search__service__pb2
from .....google.cloud.discoveryengine.v1 import session_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_session__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/discoveryengine/v1/assistant_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a3google/cloud/discoveryengine/v1/assist_answer.proto\x1a4google/cloud/discoveryengine/v1/search_service.proto\x1a-google/cloud/discoveryengine/v1/session.proto"R\n\x12AssistUserMetadata\x12\x16\n\ttime_zone\x18\x01 \x01(\tB\x03\xe0A\x01\x12$\n\x17preferred_language_code\x18\x02 \x01(\tB\x03\xe0A\x01"\xba\t\n\x13StreamAssistRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/Assistant\x12:\n\x05query\x18\x02 \x01(\x0b2&.google.cloud.discoveryengine.v1.QueryB\x03\xe0A\x01\x12?\n\x07session\x18\x03 \x01(\tB.\xe0A\x01\xfaA(\n&discoveryengine.googleapis.com/Session\x12O\n\ruser_metadata\x18\x06 \x01(\x0b23.google.cloud.discoveryengine.v1.AssistUserMetadataB\x03\xe0A\x01\x12W\n\ntools_spec\x18\x12 \x01(\x0b2>.google.cloud.discoveryengine.v1.StreamAssistRequest.ToolsSpecB\x03\xe0A\x01\x12a\n\x0fgeneration_spec\x18\x13 \x01(\x0b2C.google.cloud.discoveryengine.v1.StreamAssistRequest.GenerationSpecB\x03\xe0A\x01\x1a\xaf\x05\n\tToolsSpec\x12u\n\x15vertex_ai_search_spec\x18\x01 \x01(\x0b2Q.google.cloud.discoveryengine.v1.StreamAssistRequest.ToolsSpec.VertexAiSearchSpecB\x03\xe0A\x01\x12p\n\x12web_grounding_spec\x18\x02 \x01(\x0b2O.google.cloud.discoveryengine.v1.StreamAssistRequest.ToolsSpec.WebGroundingSpecB\x03\xe0A\x01\x12v\n\x15image_generation_spec\x18\x03 \x01(\x0b2R.google.cloud.discoveryengine.v1.StreamAssistRequest.ToolsSpec.ImageGenerationSpecB\x03\xe0A\x01\x12v\n\x15video_generation_spec\x18\x04 \x01(\x0b2R.google.cloud.discoveryengine.v1.StreamAssistRequest.ToolsSpec.VideoGenerationSpecB\x03\xe0A\x01\x1a\x86\x01\n\x12VertexAiSearchSpec\x12[\n\x10data_store_specs\x18\x02 \x03(\x0b2<.google.cloud.discoveryengine.v1.SearchRequest.DataStoreSpecB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x1a\x12\n\x10WebGroundingSpec\x1a\x15\n\x13ImageGenerationSpec\x1a\x15\n\x13VideoGenerationSpec\x1a\'\n\x0eGenerationSpec\x12\x15\n\x08model_id\x18\x01 \x01(\tB\x03\xe0A\x01"\x91\x02\n\x14StreamAssistResponse\x12=\n\x06answer\x18\x01 \x01(\x0b2-.google.cloud.discoveryengine.v1.AssistAnswer\x12W\n\x0csession_info\x18\x02 \x01(\x0b2A.google.cloud.discoveryengine.v1.StreamAssistResponse.SessionInfo\x12\x14\n\x0cassist_token\x18\x04 \x01(\t\x1aK\n\x0bSessionInfo\x12<\n\x07session\x18\x01 \x01(\tB+\xfaA(\n&discoveryengine.googleapis.com/Session2\xc6\x02\n\x10AssistantService\x12\xdd\x01\n\x0cStreamAssist\x124.google.cloud.discoveryengine.v1.StreamAssistRequest\x1a5.google.cloud.discoveryengine.v1.StreamAssistResponse"^\x82\xd3\xe4\x93\x02X"S/v1/{name=projects/*/locations/*/collections/*/engines/*/assistants/*}:streamAssist:\x01*0\x01\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x88\x02\n#com.google.cloud.discoveryengine.v1B\x15AssistantServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.assistant_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x15AssistantServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_ASSISTUSERMETADATA'].fields_by_name['time_zone']._loaded_options = None
    _globals['_ASSISTUSERMETADATA'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x01'
    _globals['_ASSISTUSERMETADATA'].fields_by_name['preferred_language_code']._loaded_options = None
    _globals['_ASSISTUSERMETADATA'].fields_by_name['preferred_language_code']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC_VERTEXAISEARCHSPEC'].fields_by_name['data_store_specs']._loaded_options = None
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC_VERTEXAISEARCHSPEC'].fields_by_name['data_store_specs']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC_VERTEXAISEARCHSPEC'].fields_by_name['filter']._loaded_options = None
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC_VERTEXAISEARCHSPEC'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC'].fields_by_name['vertex_ai_search_spec']._loaded_options = None
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC'].fields_by_name['vertex_ai_search_spec']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC'].fields_by_name['web_grounding_spec']._loaded_options = None
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC'].fields_by_name['web_grounding_spec']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC'].fields_by_name['image_generation_spec']._loaded_options = None
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC'].fields_by_name['image_generation_spec']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC'].fields_by_name['video_generation_spec']._loaded_options = None
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC'].fields_by_name['video_generation_spec']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMASSISTREQUEST_GENERATIONSPEC'].fields_by_name['model_id']._loaded_options = None
    _globals['_STREAMASSISTREQUEST_GENERATIONSPEC'].fields_by_name['model_id']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMASSISTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STREAMASSISTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/Assistant'
    _globals['_STREAMASSISTREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_STREAMASSISTREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMASSISTREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_STREAMASSISTREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x01\xfaA(\n&discoveryengine.googleapis.com/Session'
    _globals['_STREAMASSISTREQUEST'].fields_by_name['user_metadata']._loaded_options = None
    _globals['_STREAMASSISTREQUEST'].fields_by_name['user_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMASSISTREQUEST'].fields_by_name['tools_spec']._loaded_options = None
    _globals['_STREAMASSISTREQUEST'].fields_by_name['tools_spec']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMASSISTREQUEST'].fields_by_name['generation_spec']._loaded_options = None
    _globals['_STREAMASSISTREQUEST'].fields_by_name['generation_spec']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMASSISTRESPONSE_SESSIONINFO'].fields_by_name['session']._loaded_options = None
    _globals['_STREAMASSISTRESPONSE_SESSIONINFO'].fields_by_name['session']._serialized_options = b'\xfaA(\n&discoveryengine.googleapis.com/Session'
    _globals['_ASSISTANTSERVICE']._loaded_options = None
    _globals['_ASSISTANTSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ASSISTANTSERVICE'].methods_by_name['StreamAssist']._loaded_options = None
    _globals['_ASSISTANTSERVICE'].methods_by_name['StreamAssist']._serialized_options = b'\x82\xd3\xe4\x93\x02X"S/v1/{name=projects/*/locations/*/collections/*/engines/*/assistants/*}:streamAssist:\x01*'
    _globals['_ASSISTUSERMETADATA']._serialized_start = 361
    _globals['_ASSISTUSERMETADATA']._serialized_end = 443
    _globals['_STREAMASSISTREQUEST']._serialized_start = 446
    _globals['_STREAMASSISTREQUEST']._serialized_end = 1656
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC']._serialized_start = 928
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC']._serialized_end = 1615
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC_VERTEXAISEARCHSPEC']._serialized_start = 1415
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC_VERTEXAISEARCHSPEC']._serialized_end = 1549
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC_WEBGROUNDINGSPEC']._serialized_start = 1551
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC_WEBGROUNDINGSPEC']._serialized_end = 1569
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC_IMAGEGENERATIONSPEC']._serialized_start = 1571
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC_IMAGEGENERATIONSPEC']._serialized_end = 1592
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC_VIDEOGENERATIONSPEC']._serialized_start = 1594
    _globals['_STREAMASSISTREQUEST_TOOLSSPEC_VIDEOGENERATIONSPEC']._serialized_end = 1615
    _globals['_STREAMASSISTREQUEST_GENERATIONSPEC']._serialized_start = 1617
    _globals['_STREAMASSISTREQUEST_GENERATIONSPEC']._serialized_end = 1656
    _globals['_STREAMASSISTRESPONSE']._serialized_start = 1659
    _globals['_STREAMASSISTRESPONSE']._serialized_end = 1932
    _globals['_STREAMASSISTRESPONSE_SESSIONINFO']._serialized_start = 1857
    _globals['_STREAMASSISTRESPONSE_SESSIONINFO']._serialized_end = 1932
    _globals['_ASSISTANTSERVICE']._serialized_start = 1935
    _globals['_ASSISTANTSERVICE']._serialized_end = 2261