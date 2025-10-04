"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/user_event_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import import_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_import__config__pb2
from .....google.cloud.discoveryengine.v1 import purge_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_purge__config__pb2
from .....google.cloud.discoveryengine.v1 import user_event_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_user__event__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/discoveryengine/v1/user_event_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/httpbody.proto\x1a\x19google/api/resource.proto\x1a3google/cloud/discoveryengine/v1/import_config.proto\x1a2google/cloud/discoveryengine/v1/purge_config.proto\x1a0google/cloud/discoveryengine/v1/user_event.proto\x1a#google/longrunning/operations.proto"\xc7\x01\n\x15WriteUserEventRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12H\n\nuser_event\x18\x02 \x01(\x0b2*.google.cloud.discoveryengine.v1.UserEventB\x03\xe0A\x02H\x00\x88\x01\x01\x12\x13\n\x0bwrite_async\x18\x03 \x01(\x08B\r\n\x0b_user_event"\xa8\x01\n\x17CollectUserEventRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12\x17\n\nuser_event\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03uri\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03ets\x18\x04 \x01(\x03H\x01\x88\x01\x01B\x06\n\x04_uriB\x06\n\x04_ets2\xec\x0c\n\x10UserEventService\x12\xf0\x02\n\x0eWriteUserEvent\x126.google.cloud.discoveryengine.v1.WriteUserEventRequest\x1a*.google.cloud.discoveryengine.v1.UserEvent"\xf9\x01\x82\xd3\xe4\x93\x02\xf2\x01"A/v1/{parent=projects/*/locations/*/dataStores/*}/userEvents:write:\nuser_eventZ]"O/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:write:\nuser_eventZB"4/v1/{parent=projects/*/locations/*}/userEvents:write:\nuser_event\x12\xc0\x02\n\x10CollectUserEvent\x128.google.cloud.discoveryengine.v1.CollectUserEventRequest\x1a\x14.google.api.HttpBody"\xdb\x01\x82\xd3\xe4\x93\x02\xd4\x01\x12C/v1/{parent=projects/*/locations/*/dataStores/*}/userEvents:collectZS\x12Q/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:collectZ8\x126/v1/{parent=projects/*/locations/*}/userEvents:collect\x12\x84\x03\n\x0fPurgeUserEvents\x127.google.cloud.discoveryengine.v1.PurgeUserEventsRequest\x1a\x1d.google.longrunning.Operation"\x98\x02\xcaAr\n7google.cloud.discoveryengine.v1.PurgeUserEventsResponse\x127google.cloud.discoveryengine.v1.PurgeUserEventsMetadata\x82\xd3\xe4\x93\x02\x9c\x01"A/v1/{parent=projects/*/locations/*/dataStores/*}/userEvents:purge:\x01*ZT"O/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:purge:\x01*\x12\xc6\x03\n\x10ImportUserEvents\x128.google.cloud.discoveryengine.v1.ImportUserEventsRequest\x1a\x1d.google.longrunning.Operation"\xd8\x02\xcaAt\n8google.cloud.discoveryengine.v1.ImportUserEventsResponse\x128google.cloud.discoveryengine.v1.ImportUserEventsMetadata\x82\xd3\xe4\x93\x02\xda\x01"B/v1/{parent=projects/*/locations/*/dataStores/*}/userEvents:import:\x01*ZU"P/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:import:\x01*Z:"5/v1/{parent=projects/*/locations/*}/userEvents:import:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x88\x02\n#com.google.cloud.discoveryengine.v1B\x15UserEventServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.user_event_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x15UserEventServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_WRITEUSEREVENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_WRITEUSEREVENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_WRITEUSEREVENTREQUEST'].fields_by_name['user_event']._loaded_options = None
    _globals['_WRITEUSEREVENTREQUEST'].fields_by_name['user_event']._serialized_options = b'\xe0A\x02'
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['user_event']._loaded_options = None
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['user_event']._serialized_options = b'\xe0A\x02'
    _globals['_USEREVENTSERVICE']._loaded_options = None
    _globals['_USEREVENTSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_USEREVENTSERVICE'].methods_by_name['WriteUserEvent']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['WriteUserEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02\xf2\x01"A/v1/{parent=projects/*/locations/*/dataStores/*}/userEvents:write:\nuser_eventZ]"O/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:write:\nuser_eventZB"4/v1/{parent=projects/*/locations/*}/userEvents:write:\nuser_event'
    _globals['_USEREVENTSERVICE'].methods_by_name['CollectUserEvent']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['CollectUserEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02\xd4\x01\x12C/v1/{parent=projects/*/locations/*/dataStores/*}/userEvents:collectZS\x12Q/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:collectZ8\x126/v1/{parent=projects/*/locations/*}/userEvents:collect'
    _globals['_USEREVENTSERVICE'].methods_by_name['PurgeUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['PurgeUserEvents']._serialized_options = b'\xcaAr\n7google.cloud.discoveryengine.v1.PurgeUserEventsResponse\x127google.cloud.discoveryengine.v1.PurgeUserEventsMetadata\x82\xd3\xe4\x93\x02\x9c\x01"A/v1/{parent=projects/*/locations/*/dataStores/*}/userEvents:purge:\x01*ZT"O/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:purge:\x01*'
    _globals['_USEREVENTSERVICE'].methods_by_name['ImportUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['ImportUserEvents']._serialized_options = b'\xcaAt\n8google.cloud.discoveryengine.v1.ImportUserEventsResponse\x128google.cloud.discoveryengine.v1.ImportUserEventsMetadata\x82\xd3\xe4\x93\x02\xda\x01"B/v1/{parent=projects/*/locations/*/dataStores/*}/userEvents:import:\x01*ZU"P/v1/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:import:\x01*Z:"5/v1/{parent=projects/*/locations/*}/userEvents:import:\x01*'
    _globals['_WRITEUSEREVENTREQUEST']._serialized_start = 428
    _globals['_WRITEUSEREVENTREQUEST']._serialized_end = 627
    _globals['_COLLECTUSEREVENTREQUEST']._serialized_start = 630
    _globals['_COLLECTUSEREVENTREQUEST']._serialized_end = 798
    _globals['_USEREVENTSERVICE']._serialized_start = 801
    _globals['_USEREVENTSERVICE']._serialized_end = 2445