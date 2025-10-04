"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/apihub/v1/discovery_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.apihub.v1 import common_fields_pb2 as google_dot_cloud_dot_apihub_dot_v1_dot_common__fields__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/apihub/v1/discovery_service.proto\x12\x16google.cloud.apihub.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/apihub/v1/common_fields.proto"\x9f\x01\n$ListDiscoveredApiObservationsRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.apihub.googleapis.com/DiscoveredApiObservation\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x97\x01\n%ListDiscoveredApiObservationsResponse\x12U\n\x1bdiscovered_api_observations\x18\x01 \x03(\x0b20.google.cloud.apihub.v1.DiscoveredApiObservation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9b\x01\n"ListDiscoveredApiOperationsRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,apihub.googleapis.com/DiscoveredApiOperation\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x91\x01\n#ListDiscoveredApiOperationsResponse\x12Q\n\x19discovered_api_operations\x18\x01 \x03(\x0b2..google.cloud.apihub.v1.DiscoveredApiOperation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"j\n"GetDiscoveredApiObservationRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.apihub.googleapis.com/DiscoveredApiObservation"f\n GetDiscoveredApiOperationRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,apihub.googleapis.com/DiscoveredApiOperation2\x9a\x08\n\x0fApiHubDiscovery\x12\xec\x01\n\x1dListDiscoveredApiObservations\x12<.google.cloud.apihub.v1.ListDiscoveredApiObservationsRequest\x1a=.google.cloud.apihub.v1.ListDiscoveredApiObservationsResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/locations/*}/discoveredApiObservations\x12\xd9\x01\n\x1bGetDiscoveredApiObservation\x12:.google.cloud.apihub.v1.GetDiscoveredApiObservationRequest\x1a0.google.cloud.apihub.v1.DiscoveredApiObservation"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/{name=projects/*/locations/*/discoveredApiObservations/*}\x12\x80\x02\n\x1bListDiscoveredApiOperations\x12:.google.cloud.apihub.v1.ListDiscoveredApiOperationsRequest\x1a;.google.cloud.apihub.v1.ListDiscoveredApiOperationsResponse"h\xdaA\x06parent\x82\xd3\xe4\x93\x02Y\x12W/v1/{parent=projects/*/locations/*/discoveredApiObservations/*}/discoveredApiOperations\x12\xed\x01\n\x19GetDiscoveredApiOperation\x128.google.cloud.apihub.v1.GetDiscoveredApiOperationRequest\x1a..google.cloud.apihub.v1.DiscoveredApiOperation"f\xdaA\x04name\x82\xd3\xe4\x93\x02Y\x12W/v1/{name=projects/*/locations/*/discoveredApiObservations/*/discoveredApiOperations/*}\x1aI\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb7\x01\n\x1acom.google.cloud.apihub.v1B\x15DiscoveryServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apihub.v1.discovery_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.apihub.v1B\x15DiscoveryServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1'
    _globals['_LISTDISCOVEREDAPIOBSERVATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDISCOVEREDAPIOBSERVATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.apihub.googleapis.com/DiscoveredApiObservation'
    _globals['_LISTDISCOVEREDAPIOBSERVATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDISCOVEREDAPIOBSERVATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDISCOVEREDAPIOBSERVATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDISCOVEREDAPIOBSERVATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDISCOVEREDAPIOPERATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDISCOVEREDAPIOPERATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,apihub.googleapis.com/DiscoveredApiOperation'
    _globals['_LISTDISCOVEREDAPIOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDISCOVEREDAPIOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDISCOVEREDAPIOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDISCOVEREDAPIOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETDISCOVEREDAPIOBSERVATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDISCOVEREDAPIOBSERVATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.apihub.googleapis.com/DiscoveredApiObservation'
    _globals['_GETDISCOVEREDAPIOPERATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDISCOVEREDAPIOPERATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,apihub.googleapis.com/DiscoveredApiOperation'
    _globals['_APIHUBDISCOVERY']._loaded_options = None
    _globals['_APIHUBDISCOVERY']._serialized_options = b'\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_APIHUBDISCOVERY'].methods_by_name['ListDiscoveredApiObservations']._loaded_options = None
    _globals['_APIHUBDISCOVERY'].methods_by_name['ListDiscoveredApiObservations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/locations/*}/discoveredApiObservations'
    _globals['_APIHUBDISCOVERY'].methods_by_name['GetDiscoveredApiObservation']._loaded_options = None
    _globals['_APIHUBDISCOVERY'].methods_by_name['GetDiscoveredApiObservation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/{name=projects/*/locations/*/discoveredApiObservations/*}'
    _globals['_APIHUBDISCOVERY'].methods_by_name['ListDiscoveredApiOperations']._loaded_options = None
    _globals['_APIHUBDISCOVERY'].methods_by_name['ListDiscoveredApiOperations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02Y\x12W/v1/{parent=projects/*/locations/*/discoveredApiObservations/*}/discoveredApiOperations'
    _globals['_APIHUBDISCOVERY'].methods_by_name['GetDiscoveredApiOperation']._loaded_options = None
    _globals['_APIHUBDISCOVERY'].methods_by_name['GetDiscoveredApiOperation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02Y\x12W/v1/{name=projects/*/locations/*/discoveredApiObservations/*/discoveredApiOperations/*}'
    _globals['_LISTDISCOVEREDAPIOBSERVATIONSREQUEST']._serialized_start = 234
    _globals['_LISTDISCOVEREDAPIOBSERVATIONSREQUEST']._serialized_end = 393
    _globals['_LISTDISCOVEREDAPIOBSERVATIONSRESPONSE']._serialized_start = 396
    _globals['_LISTDISCOVEREDAPIOBSERVATIONSRESPONSE']._serialized_end = 547
    _globals['_LISTDISCOVEREDAPIOPERATIONSREQUEST']._serialized_start = 550
    _globals['_LISTDISCOVEREDAPIOPERATIONSREQUEST']._serialized_end = 705
    _globals['_LISTDISCOVEREDAPIOPERATIONSRESPONSE']._serialized_start = 708
    _globals['_LISTDISCOVEREDAPIOPERATIONSRESPONSE']._serialized_end = 853
    _globals['_GETDISCOVEREDAPIOBSERVATIONREQUEST']._serialized_start = 855
    _globals['_GETDISCOVEREDAPIOBSERVATIONREQUEST']._serialized_end = 961
    _globals['_GETDISCOVEREDAPIOPERATIONREQUEST']._serialized_start = 963
    _globals['_GETDISCOVEREDAPIOPERATIONREQUEST']._serialized_end = 1065
    _globals['_APIHUBDISCOVERY']._serialized_start = 1068
    _globals['_APIHUBDISCOVERY']._serialized_end = 2118