"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkservices/v1/grpc_route.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/networkservices/v1/grpc_route.proto\x12\x1fgoogle.cloud.networkservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x89\x15\n\tGrpcRoute\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x16\n\tself_link\x18\x0c \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12K\n\x06labels\x18\x04 \x03(\x0b26.google.cloud.networkservices.v1.GrpcRoute.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x16\n\thostnames\x18\x06 \x03(\tB\x03\xe0A\x02\x12;\n\x06meshes\x18\t \x03(\tB+\xe0A\x01\xfaA%\n#networkservices.googleapis.com/Mesh\x12@\n\x08gateways\x18\n \x03(\tB.\xe0A\x01\xfaA(\n&networkservices.googleapis.com/Gateway\x12H\n\x05rules\x18\x07 \x03(\x0b24.google.cloud.networkservices.v1.GrpcRoute.RouteRuleB\x03\xe0A\x02\x1a\x88\x02\n\x0bMethodMatch\x12N\n\x04type\x18\x01 \x01(\x0e2;.google.cloud.networkservices.v1.GrpcRoute.MethodMatch.TypeB\x03\xe0A\x01\x12\x19\n\x0cgrpc_service\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bgrpc_method\x18\x03 \x01(\tB\x03\xe0A\x02\x12 \n\x0ecase_sensitive\x18\x04 \x01(\x08B\x03\xe0A\x01H\x00\x88\x01\x01"?\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05EXACT\x10\x01\x12\x16\n\x12REGULAR_EXPRESSION\x10\x02B\x11\n\x0f_case_sensitive\x1a\xc4\x01\n\x0bHeaderMatch\x12N\n\x04type\x18\x01 \x01(\x0e2;.google.cloud.networkservices.v1.GrpcRoute.HeaderMatch.TypeB\x03\xe0A\x01\x12\x10\n\x03key\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05value\x18\x03 \x01(\tB\x03\xe0A\x02"?\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05EXACT\x10\x01\x12\x16\n\x12REGULAR_EXPRESSION\x10\x02\x1a\xb7\x01\n\nRouteMatch\x12P\n\x06method\x18\x01 \x01(\x0b26.google.cloud.networkservices.v1.GrpcRoute.MethodMatchB\x03\xe0A\x01H\x00\x88\x01\x01\x12L\n\x07headers\x18\x02 \x03(\x0b26.google.cloud.networkservices.v1.GrpcRoute.HeaderMatchB\x03\xe0A\x01B\t\n\x07_method\x1a\x8d\x01\n\x0bDestination\x12E\n\x0cservice_name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%compute.googleapis.com/BackendServiceH\x00\x12\x18\n\x06weight\x18\x02 \x01(\x05B\x03\xe0A\x01H\x01\x88\x01\x01B\x12\n\x10destination_typeB\t\n\x07_weight\x1a\xb1\x03\n\x14FaultInjectionPolicy\x12Y\n\x05delay\x18\x01 \x01(\x0b2E.google.cloud.networkservices.v1.GrpcRoute.FaultInjectionPolicy.DelayH\x00\x88\x01\x01\x12Y\n\x05abort\x18\x02 \x01(\x0b2E.google.cloud.networkservices.v1.GrpcRoute.FaultInjectionPolicy.AbortH\x01\x88\x01\x01\x1at\n\x05Delay\x123\n\x0bfixed_delay\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x88\x01\x01\x12\x17\n\npercentage\x18\x02 \x01(\x05H\x01\x88\x01\x01B\x0e\n\x0c_fixed_delayB\r\n\x0b_percentage\x1aY\n\x05Abort\x12\x18\n\x0bhttp_status\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x17\n\npercentage\x18\x02 \x01(\x05H\x01\x88\x01\x01B\x0e\n\x0c_http_statusB\r\n\x0b_percentageB\x08\n\x06_delayB\x08\n\x06_abort\x1aS\n\x1dStatefulSessionAffinityPolicy\x122\n\ncookie_ttl\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02\x1a<\n\x0bRetryPolicy\x12\x18\n\x10retry_conditions\x18\x01 \x03(\t\x12\x13\n\x0bnum_retries\x18\x02 \x01(\r\x1a\xf2\x03\n\x0bRouteAction\x12Q\n\x0cdestinations\x18\x01 \x03(\x0b26.google.cloud.networkservices.v1.GrpcRoute.DestinationB\x03\xe0A\x01\x12d\n\x16fault_injection_policy\x18\x03 \x01(\x0b2?.google.cloud.networkservices.v1.GrpcRoute.FaultInjectionPolicyB\x03\xe0A\x01\x12/\n\x07timeout\x18\x07 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12Q\n\x0cretry_policy\x18\x08 \x01(\x0b26.google.cloud.networkservices.v1.GrpcRoute.RetryPolicyB\x03\xe0A\x01\x12p\n\x19stateful_session_affinity\x18\x0b \x01(\x0b2H.google.cloud.networkservices.v1.GrpcRoute.StatefulSessionAffinityPolicyB\x03\xe0A\x01\x124\n\x0cidle_timeout\x18\x0c \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x1a\xa5\x01\n\tRouteRule\x12K\n\x07matches\x18\x01 \x03(\x0b25.google.cloud.networkservices.v1.GrpcRoute.RouteMatchB\x03\xe0A\x01\x12K\n\x06action\x18\x02 \x01(\x0b26.google.cloud.networkservices.v1.GrpcRoute.RouteActionB\x03\xe0A\x02\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:n\xeaAk\n(networkservices.googleapis.com/GrpcRoute\x12?projects/{project}/locations/{location}/grpcRoutes/{grpc_route}"\xa5\x01\n\x15ListGrpcRoutesRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(networkservices.googleapis.com/GrpcRoute\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12#\n\x16return_partial_success\x18\x04 \x01(\x08B\x03\xe0A\x01"\x87\x01\n\x16ListGrpcRoutesResponse\x12?\n\x0bgrpc_routes\x18\x01 \x03(\x0b2*.google.cloud.networkservices.v1.GrpcRoute\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"U\n\x13GetGrpcRouteRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(networkservices.googleapis.com/GrpcRoute"\xbb\x01\n\x16CreateGrpcRouteRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(networkservices.googleapis.com/GrpcRoute\x12\x1a\n\rgrpc_route_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12C\n\ngrpc_route\x18\x03 \x01(\x0b2*.google.cloud.networkservices.v1.GrpcRouteB\x03\xe0A\x02"\x93\x01\n\x16UpdateGrpcRouteRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12C\n\ngrpc_route\x18\x02 \x01(\x0b2*.google.cloud.networkservices.v1.GrpcRouteB\x03\xe0A\x02"X\n\x16DeleteGrpcRouteRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(networkservices.googleapis.com/GrpcRouteB\xe4\x02\n#com.google.cloud.networkservices.v1B\x0eGrpcRouteProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1\xeaAr\n%compute.googleapis.com/BackendService\x12Iprojects/{project}/locations/{location}/backendServices/{backend_service}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1.grpc_route_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networkservices.v1B\x0eGrpcRouteProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1\xeaAr\n%compute.googleapis.com/BackendService\x12Iprojects/{project}/locations/{location}/backendServices/{backend_service}'
    _globals['_GRPCROUTE_METHODMATCH'].fields_by_name['type']._loaded_options = None
    _globals['_GRPCROUTE_METHODMATCH'].fields_by_name['type']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_METHODMATCH'].fields_by_name['grpc_service']._loaded_options = None
    _globals['_GRPCROUTE_METHODMATCH'].fields_by_name['grpc_service']._serialized_options = b'\xe0A\x02'
    _globals['_GRPCROUTE_METHODMATCH'].fields_by_name['grpc_method']._loaded_options = None
    _globals['_GRPCROUTE_METHODMATCH'].fields_by_name['grpc_method']._serialized_options = b'\xe0A\x02'
    _globals['_GRPCROUTE_METHODMATCH'].fields_by_name['case_sensitive']._loaded_options = None
    _globals['_GRPCROUTE_METHODMATCH'].fields_by_name['case_sensitive']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_HEADERMATCH'].fields_by_name['type']._loaded_options = None
    _globals['_GRPCROUTE_HEADERMATCH'].fields_by_name['type']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_HEADERMATCH'].fields_by_name['key']._loaded_options = None
    _globals['_GRPCROUTE_HEADERMATCH'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_GRPCROUTE_HEADERMATCH'].fields_by_name['value']._loaded_options = None
    _globals['_GRPCROUTE_HEADERMATCH'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_GRPCROUTE_ROUTEMATCH'].fields_by_name['method']._loaded_options = None
    _globals['_GRPCROUTE_ROUTEMATCH'].fields_by_name['method']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_ROUTEMATCH'].fields_by_name['headers']._loaded_options = None
    _globals['_GRPCROUTE_ROUTEMATCH'].fields_by_name['headers']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_DESTINATION'].fields_by_name['service_name']._loaded_options = None
    _globals['_GRPCROUTE_DESTINATION'].fields_by_name['service_name']._serialized_options = b"\xe0A\x02\xfaA'\n%compute.googleapis.com/BackendService"
    _globals['_GRPCROUTE_DESTINATION'].fields_by_name['weight']._loaded_options = None
    _globals['_GRPCROUTE_DESTINATION'].fields_by_name['weight']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_STATEFULSESSIONAFFINITYPOLICY'].fields_by_name['cookie_ttl']._loaded_options = None
    _globals['_GRPCROUTE_STATEFULSESSIONAFFINITYPOLICY'].fields_by_name['cookie_ttl']._serialized_options = b'\xe0A\x02'
    _globals['_GRPCROUTE_ROUTEACTION'].fields_by_name['destinations']._loaded_options = None
    _globals['_GRPCROUTE_ROUTEACTION'].fields_by_name['destinations']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_ROUTEACTION'].fields_by_name['fault_injection_policy']._loaded_options = None
    _globals['_GRPCROUTE_ROUTEACTION'].fields_by_name['fault_injection_policy']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_ROUTEACTION'].fields_by_name['timeout']._loaded_options = None
    _globals['_GRPCROUTE_ROUTEACTION'].fields_by_name['timeout']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_ROUTEACTION'].fields_by_name['retry_policy']._loaded_options = None
    _globals['_GRPCROUTE_ROUTEACTION'].fields_by_name['retry_policy']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_ROUTEACTION'].fields_by_name['stateful_session_affinity']._loaded_options = None
    _globals['_GRPCROUTE_ROUTEACTION'].fields_by_name['stateful_session_affinity']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_ROUTEACTION'].fields_by_name['idle_timeout']._loaded_options = None
    _globals['_GRPCROUTE_ROUTEACTION'].fields_by_name['idle_timeout']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_ROUTERULE'].fields_by_name['matches']._loaded_options = None
    _globals['_GRPCROUTE_ROUTERULE'].fields_by_name['matches']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE_ROUTERULE'].fields_by_name['action']._loaded_options = None
    _globals['_GRPCROUTE_ROUTERULE'].fields_by_name['action']._serialized_options = b'\xe0A\x02'
    _globals['_GRPCROUTE_LABELSENTRY']._loaded_options = None
    _globals['_GRPCROUTE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_GRPCROUTE'].fields_by_name['name']._loaded_options = None
    _globals['_GRPCROUTE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_GRPCROUTE'].fields_by_name['self_link']._loaded_options = None
    _globals['_GRPCROUTE'].fields_by_name['self_link']._serialized_options = b'\xe0A\x03'
    _globals['_GRPCROUTE'].fields_by_name['create_time']._loaded_options = None
    _globals['_GRPCROUTE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_GRPCROUTE'].fields_by_name['update_time']._loaded_options = None
    _globals['_GRPCROUTE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_GRPCROUTE'].fields_by_name['labels']._loaded_options = None
    _globals['_GRPCROUTE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE'].fields_by_name['description']._loaded_options = None
    _globals['_GRPCROUTE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_GRPCROUTE'].fields_by_name['hostnames']._loaded_options = None
    _globals['_GRPCROUTE'].fields_by_name['hostnames']._serialized_options = b'\xe0A\x02'
    _globals['_GRPCROUTE'].fields_by_name['meshes']._loaded_options = None
    _globals['_GRPCROUTE'].fields_by_name['meshes']._serialized_options = b'\xe0A\x01\xfaA%\n#networkservices.googleapis.com/Mesh'
    _globals['_GRPCROUTE'].fields_by_name['gateways']._loaded_options = None
    _globals['_GRPCROUTE'].fields_by_name['gateways']._serialized_options = b'\xe0A\x01\xfaA(\n&networkservices.googleapis.com/Gateway'
    _globals['_GRPCROUTE'].fields_by_name['rules']._loaded_options = None
    _globals['_GRPCROUTE'].fields_by_name['rules']._serialized_options = b'\xe0A\x02'
    _globals['_GRPCROUTE']._loaded_options = None
    _globals['_GRPCROUTE']._serialized_options = b'\xeaAk\n(networkservices.googleapis.com/GrpcRoute\x12?projects/{project}/locations/{location}/grpcRoutes/{grpc_route}'
    _globals['_LISTGRPCROUTESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTGRPCROUTESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(networkservices.googleapis.com/GrpcRoute'
    _globals['_LISTGRPCROUTESREQUEST'].fields_by_name['return_partial_success']._loaded_options = None
    _globals['_LISTGRPCROUTESREQUEST'].fields_by_name['return_partial_success']._serialized_options = b'\xe0A\x01'
    _globals['_GETGRPCROUTEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETGRPCROUTEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(networkservices.googleapis.com/GrpcRoute'
    _globals['_CREATEGRPCROUTEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEGRPCROUTEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(networkservices.googleapis.com/GrpcRoute'
    _globals['_CREATEGRPCROUTEREQUEST'].fields_by_name['grpc_route_id']._loaded_options = None
    _globals['_CREATEGRPCROUTEREQUEST'].fields_by_name['grpc_route_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEGRPCROUTEREQUEST'].fields_by_name['grpc_route']._loaded_options = None
    _globals['_CREATEGRPCROUTEREQUEST'].fields_by_name['grpc_route']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGRPCROUTEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEGRPCROUTEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEGRPCROUTEREQUEST'].fields_by_name['grpc_route']._loaded_options = None
    _globals['_UPDATEGRPCROUTEREQUEST'].fields_by_name['grpc_route']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEGRPCROUTEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEGRPCROUTEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(networkservices.googleapis.com/GrpcRoute'
    _globals['_GRPCROUTE']._serialized_start = 245
    _globals['_GRPCROUTE']._serialized_end = 2942
    _globals['_GRPCROUTE_METHODMATCH']._serialized_start = 738
    _globals['_GRPCROUTE_METHODMATCH']._serialized_end = 1002
    _globals['_GRPCROUTE_METHODMATCH_TYPE']._serialized_start = 920
    _globals['_GRPCROUTE_METHODMATCH_TYPE']._serialized_end = 983
    _globals['_GRPCROUTE_HEADERMATCH']._serialized_start = 1005
    _globals['_GRPCROUTE_HEADERMATCH']._serialized_end = 1201
    _globals['_GRPCROUTE_HEADERMATCH_TYPE']._serialized_start = 920
    _globals['_GRPCROUTE_HEADERMATCH_TYPE']._serialized_end = 983
    _globals['_GRPCROUTE_ROUTEMATCH']._serialized_start = 1204
    _globals['_GRPCROUTE_ROUTEMATCH']._serialized_end = 1387
    _globals['_GRPCROUTE_DESTINATION']._serialized_start = 1390
    _globals['_GRPCROUTE_DESTINATION']._serialized_end = 1531
    _globals['_GRPCROUTE_FAULTINJECTIONPOLICY']._serialized_start = 1534
    _globals['_GRPCROUTE_FAULTINJECTIONPOLICY']._serialized_end = 1967
    _globals['_GRPCROUTE_FAULTINJECTIONPOLICY_DELAY']._serialized_start = 1740
    _globals['_GRPCROUTE_FAULTINJECTIONPOLICY_DELAY']._serialized_end = 1856
    _globals['_GRPCROUTE_FAULTINJECTIONPOLICY_ABORT']._serialized_start = 1858
    _globals['_GRPCROUTE_FAULTINJECTIONPOLICY_ABORT']._serialized_end = 1947
    _globals['_GRPCROUTE_STATEFULSESSIONAFFINITYPOLICY']._serialized_start = 1969
    _globals['_GRPCROUTE_STATEFULSESSIONAFFINITYPOLICY']._serialized_end = 2052
    _globals['_GRPCROUTE_RETRYPOLICY']._serialized_start = 2054
    _globals['_GRPCROUTE_RETRYPOLICY']._serialized_end = 2114
    _globals['_GRPCROUTE_ROUTEACTION']._serialized_start = 2117
    _globals['_GRPCROUTE_ROUTEACTION']._serialized_end = 2615
    _globals['_GRPCROUTE_ROUTERULE']._serialized_start = 2618
    _globals['_GRPCROUTE_ROUTERULE']._serialized_end = 2783
    _globals['_GRPCROUTE_LABELSENTRY']._serialized_start = 2785
    _globals['_GRPCROUTE_LABELSENTRY']._serialized_end = 2830
    _globals['_LISTGRPCROUTESREQUEST']._serialized_start = 2945
    _globals['_LISTGRPCROUTESREQUEST']._serialized_end = 3110
    _globals['_LISTGRPCROUTESRESPONSE']._serialized_start = 3113
    _globals['_LISTGRPCROUTESRESPONSE']._serialized_end = 3248
    _globals['_GETGRPCROUTEREQUEST']._serialized_start = 3250
    _globals['_GETGRPCROUTEREQUEST']._serialized_end = 3335
    _globals['_CREATEGRPCROUTEREQUEST']._serialized_start = 3338
    _globals['_CREATEGRPCROUTEREQUEST']._serialized_end = 3525
    _globals['_UPDATEGRPCROUTEREQUEST']._serialized_start = 3528
    _globals['_UPDATEGRPCROUTEREQUEST']._serialized_end = 3675
    _globals['_DELETEGRPCROUTEREQUEST']._serialized_start = 3677
    _globals['_DELETEGRPCROUTEREQUEST']._serialized_end = 3765