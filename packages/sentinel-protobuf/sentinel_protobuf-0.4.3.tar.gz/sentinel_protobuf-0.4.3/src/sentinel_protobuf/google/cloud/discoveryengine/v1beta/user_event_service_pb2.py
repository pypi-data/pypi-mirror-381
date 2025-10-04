"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/user_event_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import import_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_import__config__pb2
from .....google.cloud.discoveryengine.v1beta import purge_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_purge__config__pb2
from .....google.cloud.discoveryengine.v1beta import user_event_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_user__event__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/discoveryengine/v1beta/user_event_service.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/httpbody.proto\x1a\x19google/api/resource.proto\x1a7google/cloud/discoveryengine/v1beta/import_config.proto\x1a6google/cloud/discoveryengine/v1beta/purge_config.proto\x1a4google/cloud/discoveryengine/v1beta/user_event.proto\x1a#google/longrunning/operations.proto"\xcb\x01\n\x15WriteUserEventRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12L\n\nuser_event\x18\x02 \x01(\x0b2..google.cloud.discoveryengine.v1beta.UserEventB\x03\xe0A\x02H\x00\x88\x01\x01\x12\x13\n\x0bwrite_async\x18\x03 \x01(\x08B\r\n\x0b_user_event"\xa8\x01\n\x17CollectUserEventRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12\x17\n\nuser_event\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03uri\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03ets\x18\x04 \x01(\x03H\x01\x88\x01\x01B\x06\n\x04_uriB\x06\n\x04_ets2\xfc\x0c\n\x10UserEventService\x12\x84\x03\n\x0eWriteUserEvent\x12:.google.cloud.discoveryengine.v1beta.WriteUserEventRequest\x1a..google.cloud.discoveryengine.v1beta.UserEvent"\x85\x02\x82\xd3\xe4\x93\x02\xfe\x01"E/v1beta/{parent=projects/*/locations/*/dataStores/*}/userEvents:write:\nuser_eventZa"S/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:write:\nuser_eventZF"8/v1beta/{parent=projects/*/locations/*}/userEvents:write:\nuser_event\x12\xd0\x02\n\x10CollectUserEvent\x12<.google.cloud.discoveryengine.v1beta.CollectUserEventRequest\x1a\x14.google.api.HttpBody"\xe7\x01\x82\xd3\xe4\x93\x02\xe0\x01\x12G/v1beta/{parent=projects/*/locations/*/dataStores/*}/userEvents:collectZW\x12U/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:collectZ<\x12:/v1beta/{parent=projects/*/locations/*}/userEvents:collect\x12\x98\x03\n\x0fPurgeUserEvents\x12;.google.cloud.discoveryengine.v1beta.PurgeUserEventsRequest\x1a\x1d.google.longrunning.Operation"\xa8\x02\xcaAz\n;google.cloud.discoveryengine.v1beta.PurgeUserEventsResponse\x12;google.cloud.discoveryengine.v1beta.PurgeUserEventsMetadata\x82\xd3\xe4\x93\x02\xa4\x01"E/v1beta/{parent=projects/*/locations/*/dataStores/*}/userEvents:purge:\x01*ZX"S/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:purge:\x01*\x12\x9e\x03\n\x10ImportUserEvents\x12<.google.cloud.discoveryengine.v1beta.ImportUserEventsRequest\x1a\x1d.google.longrunning.Operation"\xac\x02\xcaA|\n<google.cloud.discoveryengine.v1beta.ImportUserEventsResponse\x12<google.cloud.discoveryengine.v1beta.ImportUserEventsMetadata\x82\xd3\xe4\x93\x02\xa6\x01"F/v1beta/{parent=projects/*/locations/*/dataStores/*}/userEvents:import:\x01*ZY"T/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:import:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9c\x02\n\'com.google.cloud.discoveryengine.v1betaB\x15UserEventServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.user_event_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x15UserEventServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
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
    _globals['_USEREVENTSERVICE'].methods_by_name['WriteUserEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02\xfe\x01"E/v1beta/{parent=projects/*/locations/*/dataStores/*}/userEvents:write:\nuser_eventZa"S/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:write:\nuser_eventZF"8/v1beta/{parent=projects/*/locations/*}/userEvents:write:\nuser_event'
    _globals['_USEREVENTSERVICE'].methods_by_name['CollectUserEvent']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['CollectUserEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02\xe0\x01\x12G/v1beta/{parent=projects/*/locations/*/dataStores/*}/userEvents:collectZW\x12U/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:collectZ<\x12:/v1beta/{parent=projects/*/locations/*}/userEvents:collect'
    _globals['_USEREVENTSERVICE'].methods_by_name['PurgeUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['PurgeUserEvents']._serialized_options = b'\xcaAz\n;google.cloud.discoveryengine.v1beta.PurgeUserEventsResponse\x12;google.cloud.discoveryengine.v1beta.PurgeUserEventsMetadata\x82\xd3\xe4\x93\x02\xa4\x01"E/v1beta/{parent=projects/*/locations/*/dataStores/*}/userEvents:purge:\x01*ZX"S/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:purge:\x01*'
    _globals['_USEREVENTSERVICE'].methods_by_name['ImportUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['ImportUserEvents']._serialized_options = b'\xcaA|\n<google.cloud.discoveryengine.v1beta.ImportUserEventsResponse\x12<google.cloud.discoveryengine.v1beta.ImportUserEventsMetadata\x82\xd3\xe4\x93\x02\xa6\x01"F/v1beta/{parent=projects/*/locations/*/dataStores/*}/userEvents:import:\x01*ZY"T/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:import:\x01*'
    _globals['_WRITEUSEREVENTREQUEST']._serialized_start = 448
    _globals['_WRITEUSEREVENTREQUEST']._serialized_end = 651
    _globals['_COLLECTUSEREVENTREQUEST']._serialized_start = 654
    _globals['_COLLECTUSEREVENTREQUEST']._serialized_end = 822
    _globals['_USEREVENTSERVICE']._serialized_start = 825
    _globals['_USEREVENTSERVICE']._serialized_end = 2485