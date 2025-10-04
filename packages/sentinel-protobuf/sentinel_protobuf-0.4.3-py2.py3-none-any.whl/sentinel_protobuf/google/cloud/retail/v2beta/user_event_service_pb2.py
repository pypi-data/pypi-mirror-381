"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2beta/user_event_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2beta import export_config_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_export__config__pb2
from .....google.cloud.retail.v2beta import import_config_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_import__config__pb2
from .....google.cloud.retail.v2beta import purge_config_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_purge__config__pb2
from .....google.cloud.retail.v2beta import user_event_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_user__event__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/retail/v2beta/user_event_service.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/httpbody.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/retail/v2beta/export_config.proto\x1a.google/cloud/retail/v2beta/import_config.proto\x1a-google/cloud/retail/v2beta/purge_config.proto\x1a+google/cloud/retail/v2beta/user_event.proto\x1a#google/longrunning/operations.proto"\x81\x01\n\x15WriteUserEventRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12>\n\nuser_event\x18\x02 \x01(\x0b2%.google.cloud.retail.v2beta.UserEventB\x03\xe0A\x02\x12\x13\n\x0bwrite_async\x18\x03 \x01(\x08"\x9f\x01\n\x17CollectUserEventRequest\x12\x17\n\rprebuilt_rule\x18\x06 \x01(\tH\x00\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nuser_event\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\x0b\n\x03ets\x18\x04 \x01(\x03\x12\x10\n\x08raw_json\x18\x05 \x01(\tB\x11\n\x0fconversion_rule"\x82\x02\n\x17RejoinUserEventsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12i\n\x17user_event_rejoin_scope\x18\x02 \x01(\x0e2H.google.cloud.retail.v2beta.RejoinUserEventsRequest.UserEventRejoinScope"g\n\x14UserEventRejoinScope\x12\'\n#USER_EVENT_REJOIN_SCOPE_UNSPECIFIED\x10\x00\x12\x11\n\rJOINED_EVENTS\x10\x01\x12\x13\n\x0fUNJOINED_EVENTS\x10\x02">\n\x18RejoinUserEventsResponse\x12"\n\x1arejoined_user_events_count\x18\x01 \x01(\x03"\x1a\n\x18RejoinUserEventsMetadata2\xe7\x0c\n\x10UserEventService\x12\xc3\x01\n\x0eWriteUserEvent\x121.google.cloud.retail.v2beta.WriteUserEventRequest\x1a%.google.cloud.retail.v2beta.UserEvent"W\x82\xd3\xe4\x93\x02Q"C/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:write:\nuser_event\x12\xfa\x01\n\x10CollectUserEvent\x123.google.cloud.retail.v2beta.CollectUserEventRequest\x1a\x14.google.api.HttpBody"\x9a\x01\x82\xd3\xe4\x93\x02\x93\x01\x12E/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:collectZJ"E/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:collect:\x01*\x12\x96\x02\n\x0fPurgeUserEvents\x122.google.cloud.retail.v2beta.PurgeUserEventsRequest\x1a\x1d.google.longrunning.Operation"\xaf\x01\xcaA^\n2google.cloud.retail.v2beta.PurgeUserEventsResponse\x12(google.cloud.retail.v2beta.PurgeMetadata\x82\xd3\xe4\x93\x02H"C/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:purge:\x01*\x12\x9b\x02\n\x10ImportUserEvents\x123.google.cloud.retail.v2beta.ImportUserEventsRequest\x1a\x1d.google.longrunning.Operation"\xb2\x01\xcaA`\n3google.cloud.retail.v2beta.ImportUserEventsResponse\x12)google.cloud.retail.v2beta.ImportMetadata\x82\xd3\xe4\x93\x02I"D/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:import:\x01*\x12\x9b\x02\n\x10ExportUserEvents\x123.google.cloud.retail.v2beta.ExportUserEventsRequest\x1a\x1d.google.longrunning.Operation"\xb2\x01\xcaA`\n3google.cloud.retail.v2beta.ExportUserEventsResponse\x12)google.cloud.retail.v2beta.ExportMetadata\x82\xd3\xe4\x93\x02I"D/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:export:\x01*\x12\xef\x01\n\x10RejoinUserEvents\x123.google.cloud.retail.v2beta.RejoinUserEventsRequest\x1a\x1d.google.longrunning.Operation"\x86\x01\xcaA4\n\x18RejoinUserEventsResponse\x12\x18RejoinUserEventsMetadata\x82\xd3\xe4\x93\x02I"D/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:rejoin:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd4\x01\n\x1ecom.google.cloud.retail.v2betaB\x15UserEventServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.user_event_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x15UserEventServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
    _globals['_WRITEUSEREVENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_WRITEUSEREVENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_WRITEUSEREVENTREQUEST'].fields_by_name['user_event']._loaded_options = None
    _globals['_WRITEUSEREVENTREQUEST'].fields_by_name['user_event']._serialized_options = b'\xe0A\x02'
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['user_event']._loaded_options = None
    _globals['_COLLECTUSEREVENTREQUEST'].fields_by_name['user_event']._serialized_options = b'\xe0A\x02'
    _globals['_REJOINUSEREVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_REJOINUSEREVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_USEREVENTSERVICE']._loaded_options = None
    _globals['_USEREVENTSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_USEREVENTSERVICE'].methods_by_name['WriteUserEvent']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['WriteUserEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02Q"C/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:write:\nuser_event'
    _globals['_USEREVENTSERVICE'].methods_by_name['CollectUserEvent']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['CollectUserEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02\x93\x01\x12E/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:collectZJ"E/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:collect:\x01*'
    _globals['_USEREVENTSERVICE'].methods_by_name['PurgeUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['PurgeUserEvents']._serialized_options = b'\xcaA^\n2google.cloud.retail.v2beta.PurgeUserEventsResponse\x12(google.cloud.retail.v2beta.PurgeMetadata\x82\xd3\xe4\x93\x02H"C/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:purge:\x01*'
    _globals['_USEREVENTSERVICE'].methods_by_name['ImportUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['ImportUserEvents']._serialized_options = b'\xcaA`\n3google.cloud.retail.v2beta.ImportUserEventsResponse\x12)google.cloud.retail.v2beta.ImportMetadata\x82\xd3\xe4\x93\x02I"D/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:import:\x01*'
    _globals['_USEREVENTSERVICE'].methods_by_name['ExportUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['ExportUserEvents']._serialized_options = b'\xcaA`\n3google.cloud.retail.v2beta.ExportUserEventsResponse\x12)google.cloud.retail.v2beta.ExportMetadata\x82\xd3\xe4\x93\x02I"D/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:export:\x01*'
    _globals['_USEREVENTSERVICE'].methods_by_name['RejoinUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['RejoinUserEvents']._serialized_options = b'\xcaA4\n\x18RejoinUserEventsResponse\x12\x18RejoinUserEventsMetadata\x82\xd3\xe4\x93\x02I"D/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:rejoin:\x01*'
    _globals['_WRITEUSEREVENTREQUEST']._serialized_start = 451
    _globals['_WRITEUSEREVENTREQUEST']._serialized_end = 580
    _globals['_COLLECTUSEREVENTREQUEST']._serialized_start = 583
    _globals['_COLLECTUSEREVENTREQUEST']._serialized_end = 742
    _globals['_REJOINUSEREVENTSREQUEST']._serialized_start = 745
    _globals['_REJOINUSEREVENTSREQUEST']._serialized_end = 1003
    _globals['_REJOINUSEREVENTSREQUEST_USEREVENTREJOINSCOPE']._serialized_start = 900
    _globals['_REJOINUSEREVENTSREQUEST_USEREVENTREJOINSCOPE']._serialized_end = 1003
    _globals['_REJOINUSEREVENTSRESPONSE']._serialized_start = 1005
    _globals['_REJOINUSEREVENTSRESPONSE']._serialized_end = 1067
    _globals['_REJOINUSEREVENTSMETADATA']._serialized_start = 1069
    _globals['_REJOINUSEREVENTSMETADATA']._serialized_end = 1095
    _globals['_USEREVENTSERVICE']._serialized_start = 1098
    _globals['_USEREVENTSERVICE']._serialized_end = 2737