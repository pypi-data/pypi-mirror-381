"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/user_event_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import export_config_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_export__config__pb2
from .....google.cloud.retail.v2alpha import import_config_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_import__config__pb2
from .....google.cloud.retail.v2alpha import purge_config_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_purge__config__pb2
from .....google.cloud.retail.v2alpha import user_event_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_user__event__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/retail/v2alpha/user_event_service.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/httpbody.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/retail/v2alpha/export_config.proto\x1a/google/cloud/retail/v2alpha/import_config.proto\x1a.google/cloud/retail/v2alpha/purge_config.proto\x1a,google/cloud/retail/v2alpha/user_event.proto\x1a#google/longrunning/operations.proto"\x82\x01\n\x15WriteUserEventRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12?\n\nuser_event\x18\x02 \x01(\x0b2&.google.cloud.retail.v2alpha.UserEventB\x03\xe0A\x02\x12\x13\n\x0bwrite_async\x18\x03 \x01(\x08"\x9f\x01\n\x17CollectUserEventRequest\x12\x17\n\rprebuilt_rule\x18\x06 \x01(\tH\x00\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nuser_event\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\x0b\n\x03ets\x18\x04 \x01(\x03\x12\x10\n\x08raw_json\x18\x05 \x01(\tB\x11\n\x0fconversion_rule"\x83\x02\n\x17RejoinUserEventsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12j\n\x17user_event_rejoin_scope\x18\x02 \x01(\x0e2I.google.cloud.retail.v2alpha.RejoinUserEventsRequest.UserEventRejoinScope"g\n\x14UserEventRejoinScope\x12\'\n#USER_EVENT_REJOIN_SCOPE_UNSPECIFIED\x10\x00\x12\x11\n\rJOINED_EVENTS\x10\x01\x12\x13\n\x0fUNJOINED_EVENTS\x10\x02">\n\x18RejoinUserEventsResponse\x12"\n\x1arejoined_user_events_count\x18\x01 \x01(\x03"\x1a\n\x18RejoinUserEventsMetadata2\xfb\x0c\n\x10UserEventService\x12\xc6\x01\n\x0eWriteUserEvent\x122.google.cloud.retail.v2alpha.WriteUserEventRequest\x1a&.google.cloud.retail.v2alpha.UserEvent"X\x82\xd3\xe4\x93\x02R"D/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:write:\nuser_event\x12\xfd\x01\n\x10CollectUserEvent\x124.google.cloud.retail.v2alpha.CollectUserEventRequest\x1a\x14.google.api.HttpBody"\x9c\x01\x82\xd3\xe4\x93\x02\x95\x01\x12F/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:collectZK"F/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:collect:\x01*\x12\x9a\x02\n\x0fPurgeUserEvents\x123.google.cloud.retail.v2alpha.PurgeUserEventsRequest\x1a\x1d.google.longrunning.Operation"\xb2\x01\xcaA`\n3google.cloud.retail.v2alpha.PurgeUserEventsResponse\x12)google.cloud.retail.v2alpha.PurgeMetadata\x82\xd3\xe4\x93\x02I"D/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:purge:\x01*\x12\x9f\x02\n\x10ImportUserEvents\x124.google.cloud.retail.v2alpha.ImportUserEventsRequest\x1a\x1d.google.longrunning.Operation"\xb5\x01\xcaAb\n4google.cloud.retail.v2alpha.ImportUserEventsResponse\x12*google.cloud.retail.v2alpha.ImportMetadata\x82\xd3\xe4\x93\x02J"E/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:import:\x01*\x12\x9f\x02\n\x10ExportUserEvents\x124.google.cloud.retail.v2alpha.ExportUserEventsRequest\x1a\x1d.google.longrunning.Operation"\xb5\x01\xcaAb\n4google.cloud.retail.v2alpha.ExportUserEventsResponse\x12*google.cloud.retail.v2alpha.ExportMetadata\x82\xd3\xe4\x93\x02J"E/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:export:\x01*\x12\xf1\x01\n\x10RejoinUserEvents\x124.google.cloud.retail.v2alpha.RejoinUserEventsRequest\x1a\x1d.google.longrunning.Operation"\x87\x01\xcaA4\n\x18RejoinUserEventsResponse\x12\x18RejoinUserEventsMetadata\x82\xd3\xe4\x93\x02J"E/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:rejoin:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd9\x01\n\x1fcom.google.cloud.retail.v2alphaB\x15UserEventServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.user_event_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x15UserEventServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
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
    _globals['_USEREVENTSERVICE'].methods_by_name['WriteUserEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02R"D/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:write:\nuser_event'
    _globals['_USEREVENTSERVICE'].methods_by_name['CollectUserEvent']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['CollectUserEvent']._serialized_options = b'\x82\xd3\xe4\x93\x02\x95\x01\x12F/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:collectZK"F/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:collect:\x01*'
    _globals['_USEREVENTSERVICE'].methods_by_name['PurgeUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['PurgeUserEvents']._serialized_options = b'\xcaA`\n3google.cloud.retail.v2alpha.PurgeUserEventsResponse\x12)google.cloud.retail.v2alpha.PurgeMetadata\x82\xd3\xe4\x93\x02I"D/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:purge:\x01*'
    _globals['_USEREVENTSERVICE'].methods_by_name['ImportUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['ImportUserEvents']._serialized_options = b'\xcaAb\n4google.cloud.retail.v2alpha.ImportUserEventsResponse\x12*google.cloud.retail.v2alpha.ImportMetadata\x82\xd3\xe4\x93\x02J"E/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:import:\x01*'
    _globals['_USEREVENTSERVICE'].methods_by_name['ExportUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['ExportUserEvents']._serialized_options = b'\xcaAb\n4google.cloud.retail.v2alpha.ExportUserEventsResponse\x12*google.cloud.retail.v2alpha.ExportMetadata\x82\xd3\xe4\x93\x02J"E/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:export:\x01*'
    _globals['_USEREVENTSERVICE'].methods_by_name['RejoinUserEvents']._loaded_options = None
    _globals['_USEREVENTSERVICE'].methods_by_name['RejoinUserEvents']._serialized_options = b'\xcaA4\n\x18RejoinUserEventsResponse\x12\x18RejoinUserEventsMetadata\x82\xd3\xe4\x93\x02J"E/v2alpha/{parent=projects/*/locations/*/catalogs/*}/userEvents:rejoin:\x01*'
    _globals['_WRITEUSEREVENTREQUEST']._serialized_start = 457
    _globals['_WRITEUSEREVENTREQUEST']._serialized_end = 587
    _globals['_COLLECTUSEREVENTREQUEST']._serialized_start = 590
    _globals['_COLLECTUSEREVENTREQUEST']._serialized_end = 749
    _globals['_REJOINUSEREVENTSREQUEST']._serialized_start = 752
    _globals['_REJOINUSEREVENTSREQUEST']._serialized_end = 1011
    _globals['_REJOINUSEREVENTSREQUEST_USEREVENTREJOINSCOPE']._serialized_start = 908
    _globals['_REJOINUSEREVENTSREQUEST_USEREVENTREJOINSCOPE']._serialized_end = 1011
    _globals['_REJOINUSEREVENTSRESPONSE']._serialized_start = 1013
    _globals['_REJOINUSEREVENTSRESPONSE']._serialized_end = 1075
    _globals['_REJOINUSEREVENTSMETADATA']._serialized_start = 1077
    _globals['_REJOINUSEREVENTSMETADATA']._serialized_end = 1103
    _globals['_USEREVENTSERVICE']._serialized_start = 1106
    _globals['_USEREVENTSERVICE']._serialized_end = 2765