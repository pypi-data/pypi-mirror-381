"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1alpha/session_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import conversational_search_service_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_conversational__search__service__pb2
from .....google.cloud.discoveryengine.v1alpha import session_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_session__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/discoveryengine/v1alpha/session_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aHgoogle/cloud/discoveryengine/v1alpha/conversational_search_service.proto\x1a2google/cloud/discoveryengine/v1alpha/session.proto\x1a\x1bgoogle/protobuf/empty.proto"\x98\x01\n\x10ListFilesRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Session\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"o\n\x11ListFilesResponse\x12A\n\x05files\x18\x01 \x03(\x0b22.google.cloud.discoveryengine.v1alpha.FileMetadata\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t2\xb5\x11\n\x0eSessionService\x12\x8d\x03\n\rCreateSession\x12:.google.cloud.discoveryengine.v1alpha.CreateSessionRequest\x1a-.google.cloud.discoveryengine.v1alpha.Session"\x90\x02\xdaA\x0eparent,session\x82\xd3\xe4\x93\x02\xf8\x01">/v1alpha/{parent=projects/*/locations/*/dataStores/*}/sessions:\x07sessionZW"L/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/sessions:\x07sessionZT"I/v1alpha/{parent=projects/*/locations/*/collections/*/engines/*}/sessions:\x07session\x12\xd1\x02\n\rDeleteSession\x12:.google.cloud.discoveryengine.v1alpha.DeleteSessionRequest\x1a\x16.google.protobuf.Empty"\xeb\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xdd\x01*>/v1alpha/{name=projects/*/locations/*/dataStores/*/sessions/*}ZN*L/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/sessions/*}ZK*I/v1alpha/{name=projects/*/locations/*/collections/*/engines/*/sessions/*}\x12\xaa\x03\n\rUpdateSession\x12:.google.cloud.discoveryengine.v1alpha.UpdateSessionRequest\x1a-.google.cloud.discoveryengine.v1alpha.Session"\xad\x02\xdaA\x13session,update_mask\x82\xd3\xe4\x93\x02\x90\x022F/v1alpha/{session.name=projects/*/locations/*/dataStores/*/sessions/*}:\x07sessionZ_2T/v1alpha/{session.name=projects/*/locations/*/collections/*/dataStores/*/sessions/*}:\x07sessionZ\\2Q/v1alpha/{session.name=projects/*/locations/*/collections/*/engines/*/sessions/*}:\x07session\x12\xe2\x02\n\nGetSession\x127.google.cloud.discoveryengine.v1alpha.GetSessionRequest\x1a-.google.cloud.discoveryengine.v1alpha.Session"\xeb\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xdd\x01\x12>/v1alpha/{name=projects/*/locations/*/dataStores/*/sessions/*}ZN\x12L/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/sessions/*}ZK\x12I/v1alpha/{name=projects/*/locations/*/collections/*/engines/*/sessions/*}\x12\xf5\x02\n\x0cListSessions\x129.google.cloud.discoveryengine.v1alpha.ListSessionsRequest\x1a:.google.cloud.discoveryengine.v1alpha.ListSessionsResponse"\xed\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xdd\x01\x12>/v1alpha/{parent=projects/*/locations/*/dataStores/*}/sessionsZN\x12L/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/sessionsZK\x12I/v1alpha/{parent=projects/*/locations/*/collections/*/engines/*}/sessions\x12\xe0\x01\n\tListFiles\x126.google.cloud.discoveryengine.v1alpha.ListFilesRequest\x1a7.google.cloud.discoveryengine.v1alpha.ListFilesResponse"b\xdaA\x06parent\x82\xd3\xe4\x93\x02S\x12Q/v1alpha/{parent=projects/*/locations/*/collections/*/engines/*/sessions/*}/files\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9f\x02\n(com.google.cloud.discoveryengine.v1alphaB\x13SessionServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.session_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x13SessionServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_LISTFILESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFILESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\n&discoveryengine.googleapis.com/Session'
    _globals['_LISTFILESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTFILESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFILESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTFILESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFILESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTFILESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONSERVICE']._loaded_options = None
    _globals['_SESSIONSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SESSIONSERVICE'].methods_by_name['CreateSession']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['CreateSession']._serialized_options = b'\xdaA\x0eparent,session\x82\xd3\xe4\x93\x02\xf8\x01">/v1alpha/{parent=projects/*/locations/*/dataStores/*}/sessions:\x07sessionZW"L/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/sessions:\x07sessionZT"I/v1alpha/{parent=projects/*/locations/*/collections/*/engines/*}/sessions:\x07session'
    _globals['_SESSIONSERVICE'].methods_by_name['DeleteSession']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['DeleteSession']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xdd\x01*>/v1alpha/{name=projects/*/locations/*/dataStores/*/sessions/*}ZN*L/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/sessions/*}ZK*I/v1alpha/{name=projects/*/locations/*/collections/*/engines/*/sessions/*}'
    _globals['_SESSIONSERVICE'].methods_by_name['UpdateSession']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['UpdateSession']._serialized_options = b'\xdaA\x13session,update_mask\x82\xd3\xe4\x93\x02\x90\x022F/v1alpha/{session.name=projects/*/locations/*/dataStores/*/sessions/*}:\x07sessionZ_2T/v1alpha/{session.name=projects/*/locations/*/collections/*/dataStores/*/sessions/*}:\x07sessionZ\\2Q/v1alpha/{session.name=projects/*/locations/*/collections/*/engines/*/sessions/*}:\x07session'
    _globals['_SESSIONSERVICE'].methods_by_name['GetSession']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['GetSession']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xdd\x01\x12>/v1alpha/{name=projects/*/locations/*/dataStores/*/sessions/*}ZN\x12L/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/sessions/*}ZK\x12I/v1alpha/{name=projects/*/locations/*/collections/*/engines/*/sessions/*}'
    _globals['_SESSIONSERVICE'].methods_by_name['ListSessions']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['ListSessions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xdd\x01\x12>/v1alpha/{parent=projects/*/locations/*/dataStores/*}/sessionsZN\x12L/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/sessionsZK\x12I/v1alpha/{parent=projects/*/locations/*/collections/*/engines/*}/sessions'
    _globals['_SESSIONSERVICE'].methods_by_name['ListFiles']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['ListFiles']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02S\x12Q/v1alpha/{parent=projects/*/locations/*/collections/*/engines/*/sessions/*}/files'
    _globals['_LISTFILESREQUEST']._serialized_start = 371
    _globals['_LISTFILESREQUEST']._serialized_end = 523
    _globals['_LISTFILESRESPONSE']._serialized_start = 525
    _globals['_LISTFILESRESPONSE']._serialized_end = 636
    _globals['_SESSIONSERVICE']._serialized_start = 639
    _globals['_SESSIONSERVICE']._serialized_end = 2868