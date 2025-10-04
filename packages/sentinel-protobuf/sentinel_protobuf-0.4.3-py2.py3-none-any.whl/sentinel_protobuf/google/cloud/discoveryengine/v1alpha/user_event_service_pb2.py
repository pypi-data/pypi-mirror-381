"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1alpha/user_event_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import import_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_import__config__pb2
from .....google.cloud.discoveryengine.v1alpha import purge_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_purge__config__pb2
from .....google.cloud.discoveryengine.v1alpha import user_event_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_user__event__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/discoveryengine/v1alpha/user_event_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/httpbody.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/discoveryengine/v1alpha/import_config.proto\x1a7google/cloud/discoveryengine/v1alpha/purge_config.proto\x1a5google/cloud/discoveryengine/v1alpha/user_event.proto\x1a#google/longrunning/operations.proto"\xcc\x01\n\x15WriteUserEventRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12M\n\nuser_event\x18\x02 \x01(\x0b2/.google.cloud.discoveryengine.v1alpha.UserEventB\x03\xe0A\x02H\x00\x88\x01\x01\x12\x13\n\x0bwrite_async\x18\x03 \x01(\x08B\r\n\x0b_user_event"\xa8\x01\n\x17CollectUserEventRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12\x17\n\nuser_event\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03uri\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03ets\x18\x04 \x01(\x03H\x01\x88\x01\x01B\x06\n\x04_uriB\x06\n\x04_ets2\x8f\r\n\x10UserEventService\x12\x89\x03\n\x0eWriteUserEvent\x12;.google.cloud.discoveryengine.v1alpha.WriteUserEventRequest\x1a/.google.cloud.discoveryengine.v1alpha.UserEvent"\x88\x02\x82\xd3\xe4\x93\x02\x81\x02"F/v1alpha/{parent=projects/*/locations/*/dataStores/*}/userEvents:write:\nuser_eventZb"T/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:write:\nuser_eventZG"9/v1alpha/{parent=projects/*/locations/*}/userEvents:write:\nuser_event\x12\xd4\x02\n\x10CollectUserEvent\x12=.google.cloud.discoveryengine.v1alpha.CollectUserEventRequest\x1a\x14.google.api.HttpBody"\xea\x01\x82\xd3\xe4\x93\x02\xe3\x01\x12H/v1alpha/{parent=projects/*/locations/*/dataStores/*}/userEvents:collectZX\x12V/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:collectZ=\x12;/v1alpha/{parent=projects/*/locations/*}/userEvents:collect\x12\x9d\x03\n\x0fPurgeUserEvents\x12<.google.cloud.discoveryengine.v1alpha.PurgeUserEventsRequest\x1a\x1d.google.longrunning.Operation"\xac\x02\xcaA|\n<google.cloud.discoveryengine.v1alpha.PurgeUserEventsResponse\x12<google.cloud.discoveryengine.v1alpha.PurgeUserEventsMetadata\x82\xd3\xe4\x93\x02\xa6\x01"F/v1alpha/{parent=projects/*/locations/*/dataStores/*}/userEvents:purge:\x01*ZY"T/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:purge:\x01*\x12\xa3\x03\n\x10ImportUserEvents\x12=.google.cloud.discoveryengine.v1alpha.ImportUserEventsRequest\x1a\x1d.google.longrunning.Operation"\xb0\x02\xcaA~\n=google.cloud.discoveryengine.v1alpha.ImportUserEventsResponse\x12=google.cloud.discoveryengine.v1alpha.ImportUserEventsMetadata\x82\xd3\xe4\x93\x02\xa8\x01"G/v1alpha/{parent=projects/*/locations/*/dataStores/*}/userEvents:import:\x01*ZZ"U/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:import:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa1\x02\n(com.google.cloud.discoveryengine.v1alphaB\x15UserEventServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.user_event_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x15UserEventServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
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
    _globals['_USEREVENTSERVICE'].methods_by_name['WriteUserEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02\x81\x02"F/v1alpha/{parent=projects/*/locations/*/dataStores/*}/userEvents:write:\nuser_eventZb"T/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:write:\nuser_eventZG"9/v1alpha/{parent=projects/*/locations/*}/userEvents:write:\nuser_event'
    _globals['_USEREVENTSERVICE'].methods_by_name['CollectUserEvent']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['CollectUserEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02\xe3\x01\x12H/v1alpha/{parent=projects/*/locations/*/dataStores/*}/userEvents:collectZX\x12V/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:collectZ=\x12;/v1alpha/{parent=projects/*/locations/*}/userEvents:collect'
    _globals['_USEREVENTSERVICE'].methods_by_name['PurgeUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['PurgeUserEvents']._serialized_options = b'\xcaA|\n<google.cloud.discoveryengine.v1alpha.PurgeUserEventsResponse\x12<google.cloud.discoveryengine.v1alpha.PurgeUserEventsMetadata\x82\xd3\xe4\x93\x02\xa6\x01"F/v1alpha/{parent=projects/*/locations/*/dataStores/*}/userEvents:purge:\x01*ZY"T/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:purge:\x01*'
    _globals['_USEREVENTSERVICE'].methods_by_name['ImportUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['ImportUserEvents']._serialized_options = b'\xcaA~\n=google.cloud.discoveryengine.v1alpha.ImportUserEventsResponse\x12=google.cloud.discoveryengine.v1alpha.ImportUserEventsMetadata\x82\xd3\xe4\x93\x02\xa8\x01"G/v1alpha/{parent=projects/*/locations/*/dataStores/*}/userEvents:import:\x01*ZZ"U/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/userEvents:import:\x01*'
    _globals['_WRITEUSEREVENTREQUEST']._serialized_start = 453
    _globals['_WRITEUSEREVENTREQUEST']._serialized_end = 657
    _globals['_COLLECTUSEREVENTREQUEST']._serialized_start = 660
    _globals['_COLLECTUSEREVENTREQUEST']._serialized_end = 828
    _globals['_USEREVENTSERVICE']._serialized_start = 831
    _globals['_USEREVENTSERVICE']._serialized_end = 2510