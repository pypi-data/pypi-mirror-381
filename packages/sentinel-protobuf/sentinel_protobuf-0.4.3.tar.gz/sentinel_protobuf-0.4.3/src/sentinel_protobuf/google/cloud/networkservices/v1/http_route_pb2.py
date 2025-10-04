"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkservices/v1/http_route.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/networkservices/v1/http_route.proto\x12\x1fgoogle.cloud.networkservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8f$\n\tHttpRoute\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x16\n\tself_link\x18\x0b \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x16\n\thostnames\x18\x05 \x03(\tB\x03\xe0A\x02\x12;\n\x06meshes\x18\x08 \x03(\tB+\xe0A\x01\xfaA%\n#networkservices.googleapis.com/Mesh\x12@\n\x08gateways\x18\t \x03(\tB.\xe0A\x01\xfaA(\n&networkservices.googleapis.com/Gateway\x12K\n\x06labels\x18\n \x03(\x0b26.google.cloud.networkservices.v1.HttpRoute.LabelsEntryB\x03\xe0A\x01\x12H\n\x05rules\x18\x06 \x03(\x0b24.google.cloud.networkservices.v1.HttpRoute.RouteRuleB\x03\xe0A\x02\x1a\xbf\x02\n\x0bHeaderMatch\x12\x15\n\x0bexact_match\x18\x02 \x01(\tH\x00\x12\x15\n\x0bregex_match\x18\x03 \x01(\tH\x00\x12\x16\n\x0cprefix_match\x18\x04 \x01(\tH\x00\x12\x17\n\rpresent_match\x18\x05 \x01(\x08H\x00\x12\x16\n\x0csuffix_match\x18\x06 \x01(\tH\x00\x12Z\n\x0brange_match\x18\x07 \x01(\x0b2C.google.cloud.networkservices.v1.HttpRoute.HeaderMatch.IntegerRangeH\x00\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x14\n\x0cinvert_match\x18\x08 \x01(\x08\x1a*\n\x0cIntegerRange\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03end\x18\x02 \x01(\x05B\x0b\n\tMatchType\x1a\x82\x01\n\x13QueryParameterMatch\x12\x15\n\x0bexact_match\x18\x02 \x01(\tH\x00\x12\x15\n\x0bregex_match\x18\x03 \x01(\tH\x00\x12\x17\n\rpresent_match\x18\x04 \x01(\x08H\x00\x12\x17\n\x0fquery_parameter\x18\x01 \x01(\tB\x0b\n\tMatchType\x1a\x9b\x02\n\nRouteMatch\x12\x19\n\x0ffull_path_match\x18\x01 \x01(\tH\x00\x12\x16\n\x0cprefix_match\x18\x02 \x01(\tH\x00\x12\x15\n\x0bregex_match\x18\x03 \x01(\tH\x00\x12\x13\n\x0bignore_case\x18\x04 \x01(\x08\x12G\n\x07headers\x18\x05 \x03(\x0b26.google.cloud.networkservices.v1.HttpRoute.HeaderMatch\x12X\n\x10query_parameters\x18\x06 \x03(\x0b2>.google.cloud.networkservices.v1.HttpRoute.QueryParameterMatchB\x0b\n\tPathMatch\x1a\xa2\x02\n\x0bDestination\x12@\n\x0cservice_name\x18\x01 \x01(\tB*\xfaA\'\n%compute.googleapis.com/BackendService\x12\x0e\n\x06weight\x18\x02 \x01(\x05\x12_\n\x17request_header_modifier\x18\x03 \x01(\x0b29.google.cloud.networkservices.v1.HttpRoute.HeaderModifierB\x03\xe0A\x01\x12`\n\x18response_header_modifier\x18\x04 \x01(\x0b29.google.cloud.networkservices.v1.HttpRoute.HeaderModifierB\x03\xe0A\x01\x1a\x86\x03\n\x08Redirect\x12\x15\n\rhost_redirect\x18\x01 \x01(\t\x12\x15\n\rpath_redirect\x18\x02 \x01(\t\x12\x16\n\x0eprefix_rewrite\x18\x03 \x01(\t\x12W\n\rresponse_code\x18\x04 \x01(\x0e2@.google.cloud.networkservices.v1.HttpRoute.Redirect.ResponseCode\x12\x16\n\x0ehttps_redirect\x18\x05 \x01(\x08\x12\x13\n\x0bstrip_query\x18\x06 \x01(\x08\x12\x15\n\rport_redirect\x18\x07 \x01(\x05"\x96\x01\n\x0cResponseCode\x12\x1d\n\x19RESPONSE_CODE_UNSPECIFIED\x10\x00\x12\x1d\n\x19MOVED_PERMANENTLY_DEFAULT\x10\x01\x12\t\n\x05FOUND\x10\x02\x12\r\n\tSEE_OTHER\x10\x03\x12\x16\n\x12TEMPORARY_REDIRECT\x10\x04\x12\x16\n\x12PERMANENT_REDIRECT\x10\x05\x1a\xc1\x02\n\x14FaultInjectionPolicy\x12T\n\x05delay\x18\x01 \x01(\x0b2E.google.cloud.networkservices.v1.HttpRoute.FaultInjectionPolicy.Delay\x12T\n\x05abort\x18\x02 \x01(\x0b2E.google.cloud.networkservices.v1.HttpRoute.FaultInjectionPolicy.Abort\x1aK\n\x05Delay\x12.\n\x0bfixed_delay\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\x12\n\npercentage\x18\x02 \x01(\x05\x1a0\n\x05Abort\x12\x13\n\x0bhttp_status\x18\x01 \x01(\x05\x12\x12\n\npercentage\x18\x02 \x01(\x05\x1aS\n\x1dStatefulSessionAffinityPolicy\x122\n\ncookie_ttl\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02\x1a\x9a\x02\n\x0eHeaderModifier\x12O\n\x03set\x18\x01 \x03(\x0b2B.google.cloud.networkservices.v1.HttpRoute.HeaderModifier.SetEntry\x12O\n\x03add\x18\x02 \x03(\x0b2B.google.cloud.networkservices.v1.HttpRoute.HeaderModifier.AddEntry\x12\x0e\n\x06remove\x18\x03 \x03(\t\x1a*\n\x08SetEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a*\n\x08AddEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a?\n\nURLRewrite\x12\x1b\n\x13path_prefix_rewrite\x18\x01 \x01(\t\x12\x14\n\x0chost_rewrite\x18\x02 \x01(\t\x1ap\n\x0bRetryPolicy\x12\x18\n\x10retry_conditions\x18\x01 \x03(\t\x12\x13\n\x0bnum_retries\x18\x02 \x01(\x05\x122\n\x0fper_try_timeout\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x1a\x7f\n\x13RequestMirrorPolicy\x12K\n\x0bdestination\x18\x01 \x01(\x0b26.google.cloud.networkservices.v1.HttpRoute.Destination\x12\x1b\n\x0emirror_percent\x18\x02 \x01(\x02B\x03\xe0A\x01\x1a\xc5\x01\n\nCorsPolicy\x12\x15\n\rallow_origins\x18\x01 \x03(\t\x12\x1c\n\x14allow_origin_regexes\x18\x02 \x03(\t\x12\x15\n\rallow_methods\x18\x03 \x03(\t\x12\x15\n\rallow_headers\x18\x04 \x03(\t\x12\x16\n\x0eexpose_headers\x18\x05 \x03(\t\x12\x0f\n\x07max_age\x18\x06 \x01(\t\x12\x19\n\x11allow_credentials\x18\x07 \x01(\x08\x12\x10\n\x08disabled\x18\x08 \x01(\x08\x1al\n\x12HttpDirectResponse\x12\x1a\n\x0bstring_body\x18\x02 \x01(\tB\x03\xe0A\x01H\x00\x12\x19\n\nbytes_body\x18\x03 \x01(\x0cB\x03\xe0A\x01H\x00\x12\x13\n\x06status\x18\x01 \x01(\x05B\x03\xe0A\x02B\n\n\x08HttpBody\x1a\xb2\x08\n\x0bRouteAction\x12L\n\x0cdestinations\x18\x01 \x03(\x0b26.google.cloud.networkservices.v1.HttpRoute.Destination\x12E\n\x08redirect\x18\x02 \x01(\x0b23.google.cloud.networkservices.v1.HttpRoute.Redirect\x12_\n\x16fault_injection_policy\x18\x04 \x01(\x0b2?.google.cloud.networkservices.v1.HttpRoute.FaultInjectionPolicy\x12Z\n\x17request_header_modifier\x18\x05 \x01(\x0b29.google.cloud.networkservices.v1.HttpRoute.HeaderModifier\x12[\n\x18response_header_modifier\x18\x06 \x01(\x0b29.google.cloud.networkservices.v1.HttpRoute.HeaderModifier\x12J\n\x0burl_rewrite\x18\x07 \x01(\x0b25.google.cloud.networkservices.v1.HttpRoute.URLRewrite\x12*\n\x07timeout\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x12L\n\x0cretry_policy\x18\t \x01(\x0b26.google.cloud.networkservices.v1.HttpRoute.RetryPolicy\x12]\n\x15request_mirror_policy\x18\n \x01(\x0b2>.google.cloud.networkservices.v1.HttpRoute.RequestMirrorPolicy\x12J\n\x0bcors_policy\x18\x0b \x01(\x0b25.google.cloud.networkservices.v1.HttpRoute.CorsPolicy\x12p\n\x19stateful_session_affinity\x18\x0c \x01(\x0b2H.google.cloud.networkservices.v1.HttpRoute.StatefulSessionAffinityPolicyB\x03\xe0A\x01\x12[\n\x0fdirect_response\x18\r \x01(\x0b2=.google.cloud.networkservices.v1.HttpRoute.HttpDirectResponseB\x03\xe0A\x01\x124\n\x0cidle_timeout\x18\x0e \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x1a\x9b\x01\n\tRouteRule\x12F\n\x07matches\x18\x01 \x03(\x0b25.google.cloud.networkservices.v1.HttpRoute.RouteMatch\x12F\n\x06action\x18\x02 \x01(\x0b26.google.cloud.networkservices.v1.HttpRoute.RouteAction\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:n\xeaAk\n(networkservices.googleapis.com/HttpRoute\x12?projects/{project}/locations/{location}/httpRoutes/{http_route}"\xa5\x01\n\x15ListHttpRoutesRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(networkservices.googleapis.com/HttpRoute\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12#\n\x16return_partial_success\x18\x04 \x01(\x08B\x03\xe0A\x01"\x87\x01\n\x16ListHttpRoutesResponse\x12?\n\x0bhttp_routes\x18\x01 \x03(\x0b2*.google.cloud.networkservices.v1.HttpRoute\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"U\n\x13GetHttpRouteRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(networkservices.googleapis.com/HttpRoute"\xbb\x01\n\x16CreateHttpRouteRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(networkservices.googleapis.com/HttpRoute\x12\x1a\n\rhttp_route_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12C\n\nhttp_route\x18\x03 \x01(\x0b2*.google.cloud.networkservices.v1.HttpRouteB\x03\xe0A\x02"\x93\x01\n\x16UpdateHttpRouteRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12C\n\nhttp_route\x18\x02 \x01(\x0b2*.google.cloud.networkservices.v1.HttpRouteB\x03\xe0A\x02"X\n\x16DeleteHttpRouteRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(networkservices.googleapis.com/HttpRouteB\xef\x01\n#com.google.cloud.networkservices.v1B\x0eHttpRouteProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1.http_route_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networkservices.v1B\x0eHttpRouteProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1'
    _globals['_HTTPROUTE_DESTINATION'].fields_by_name['service_name']._loaded_options = None
    _globals['_HTTPROUTE_DESTINATION'].fields_by_name['service_name']._serialized_options = b"\xfaA'\n%compute.googleapis.com/BackendService"
    _globals['_HTTPROUTE_DESTINATION'].fields_by_name['request_header_modifier']._loaded_options = None
    _globals['_HTTPROUTE_DESTINATION'].fields_by_name['request_header_modifier']._serialized_options = b'\xe0A\x01'
    _globals['_HTTPROUTE_DESTINATION'].fields_by_name['response_header_modifier']._loaded_options = None
    _globals['_HTTPROUTE_DESTINATION'].fields_by_name['response_header_modifier']._serialized_options = b'\xe0A\x01'
    _globals['_HTTPROUTE_STATEFULSESSIONAFFINITYPOLICY'].fields_by_name['cookie_ttl']._loaded_options = None
    _globals['_HTTPROUTE_STATEFULSESSIONAFFINITYPOLICY'].fields_by_name['cookie_ttl']._serialized_options = b'\xe0A\x02'
    _globals['_HTTPROUTE_HEADERMODIFIER_SETENTRY']._loaded_options = None
    _globals['_HTTPROUTE_HEADERMODIFIER_SETENTRY']._serialized_options = b'8\x01'
    _globals['_HTTPROUTE_HEADERMODIFIER_ADDENTRY']._loaded_options = None
    _globals['_HTTPROUTE_HEADERMODIFIER_ADDENTRY']._serialized_options = b'8\x01'
    _globals['_HTTPROUTE_REQUESTMIRRORPOLICY'].fields_by_name['mirror_percent']._loaded_options = None
    _globals['_HTTPROUTE_REQUESTMIRRORPOLICY'].fields_by_name['mirror_percent']._serialized_options = b'\xe0A\x01'
    _globals['_HTTPROUTE_HTTPDIRECTRESPONSE'].fields_by_name['string_body']._loaded_options = None
    _globals['_HTTPROUTE_HTTPDIRECTRESPONSE'].fields_by_name['string_body']._serialized_options = b'\xe0A\x01'
    _globals['_HTTPROUTE_HTTPDIRECTRESPONSE'].fields_by_name['bytes_body']._loaded_options = None
    _globals['_HTTPROUTE_HTTPDIRECTRESPONSE'].fields_by_name['bytes_body']._serialized_options = b'\xe0A\x01'
    _globals['_HTTPROUTE_HTTPDIRECTRESPONSE'].fields_by_name['status']._loaded_options = None
    _globals['_HTTPROUTE_HTTPDIRECTRESPONSE'].fields_by_name['status']._serialized_options = b'\xe0A\x02'
    _globals['_HTTPROUTE_ROUTEACTION'].fields_by_name['stateful_session_affinity']._loaded_options = None
    _globals['_HTTPROUTE_ROUTEACTION'].fields_by_name['stateful_session_affinity']._serialized_options = b'\xe0A\x01'
    _globals['_HTTPROUTE_ROUTEACTION'].fields_by_name['direct_response']._loaded_options = None
    _globals['_HTTPROUTE_ROUTEACTION'].fields_by_name['direct_response']._serialized_options = b'\xe0A\x01'
    _globals['_HTTPROUTE_ROUTEACTION'].fields_by_name['idle_timeout']._loaded_options = None
    _globals['_HTTPROUTE_ROUTEACTION'].fields_by_name['idle_timeout']._serialized_options = b'\xe0A\x01'
    _globals['_HTTPROUTE_LABELSENTRY']._loaded_options = None
    _globals['_HTTPROUTE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_HTTPROUTE'].fields_by_name['name']._loaded_options = None
    _globals['_HTTPROUTE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_HTTPROUTE'].fields_by_name['self_link']._loaded_options = None
    _globals['_HTTPROUTE'].fields_by_name['self_link']._serialized_options = b'\xe0A\x03'
    _globals['_HTTPROUTE'].fields_by_name['description']._loaded_options = None
    _globals['_HTTPROUTE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_HTTPROUTE'].fields_by_name['create_time']._loaded_options = None
    _globals['_HTTPROUTE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_HTTPROUTE'].fields_by_name['update_time']._loaded_options = None
    _globals['_HTTPROUTE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_HTTPROUTE'].fields_by_name['hostnames']._loaded_options = None
    _globals['_HTTPROUTE'].fields_by_name['hostnames']._serialized_options = b'\xe0A\x02'
    _globals['_HTTPROUTE'].fields_by_name['meshes']._loaded_options = None
    _globals['_HTTPROUTE'].fields_by_name['meshes']._serialized_options = b'\xe0A\x01\xfaA%\n#networkservices.googleapis.com/Mesh'
    _globals['_HTTPROUTE'].fields_by_name['gateways']._loaded_options = None
    _globals['_HTTPROUTE'].fields_by_name['gateways']._serialized_options = b'\xe0A\x01\xfaA(\n&networkservices.googleapis.com/Gateway'
    _globals['_HTTPROUTE'].fields_by_name['labels']._loaded_options = None
    _globals['_HTTPROUTE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_HTTPROUTE'].fields_by_name['rules']._loaded_options = None
    _globals['_HTTPROUTE'].fields_by_name['rules']._serialized_options = b'\xe0A\x02'
    _globals['_HTTPROUTE']._loaded_options = None
    _globals['_HTTPROUTE']._serialized_options = b'\xeaAk\n(networkservices.googleapis.com/HttpRoute\x12?projects/{project}/locations/{location}/httpRoutes/{http_route}'
    _globals['_LISTHTTPROUTESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTHTTPROUTESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(networkservices.googleapis.com/HttpRoute'
    _globals['_LISTHTTPROUTESREQUEST'].fields_by_name['return_partial_success']._loaded_options = None
    _globals['_LISTHTTPROUTESREQUEST'].fields_by_name['return_partial_success']._serialized_options = b'\xe0A\x01'
    _globals['_GETHTTPROUTEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETHTTPROUTEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(networkservices.googleapis.com/HttpRoute'
    _globals['_CREATEHTTPROUTEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEHTTPROUTEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(networkservices.googleapis.com/HttpRoute'
    _globals['_CREATEHTTPROUTEREQUEST'].fields_by_name['http_route_id']._loaded_options = None
    _globals['_CREATEHTTPROUTEREQUEST'].fields_by_name['http_route_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEHTTPROUTEREQUEST'].fields_by_name['http_route']._loaded_options = None
    _globals['_CREATEHTTPROUTEREQUEST'].fields_by_name['http_route']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEHTTPROUTEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEHTTPROUTEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEHTTPROUTEREQUEST'].fields_by_name['http_route']._loaded_options = None
    _globals['_UPDATEHTTPROUTEREQUEST'].fields_by_name['http_route']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEHTTPROUTEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEHTTPROUTEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(networkservices.googleapis.com/HttpRoute'
    _globals['_HTTPROUTE']._serialized_start = 245
    _globals['_HTTPROUTE']._serialized_end = 4868
    _globals['_HTTPROUTE_HEADERMATCH']._serialized_start = 738
    _globals['_HTTPROUTE_HEADERMATCH']._serialized_end = 1057
    _globals['_HTTPROUTE_HEADERMATCH_INTEGERRANGE']._serialized_start = 1002
    _globals['_HTTPROUTE_HEADERMATCH_INTEGERRANGE']._serialized_end = 1044
    _globals['_HTTPROUTE_QUERYPARAMETERMATCH']._serialized_start = 1060
    _globals['_HTTPROUTE_QUERYPARAMETERMATCH']._serialized_end = 1190
    _globals['_HTTPROUTE_ROUTEMATCH']._serialized_start = 1193
    _globals['_HTTPROUTE_ROUTEMATCH']._serialized_end = 1476
    _globals['_HTTPROUTE_DESTINATION']._serialized_start = 1479
    _globals['_HTTPROUTE_DESTINATION']._serialized_end = 1769
    _globals['_HTTPROUTE_REDIRECT']._serialized_start = 1772
    _globals['_HTTPROUTE_REDIRECT']._serialized_end = 2162
    _globals['_HTTPROUTE_REDIRECT_RESPONSECODE']._serialized_start = 2012
    _globals['_HTTPROUTE_REDIRECT_RESPONSECODE']._serialized_end = 2162
    _globals['_HTTPROUTE_FAULTINJECTIONPOLICY']._serialized_start = 2165
    _globals['_HTTPROUTE_FAULTINJECTIONPOLICY']._serialized_end = 2486
    _globals['_HTTPROUTE_FAULTINJECTIONPOLICY_DELAY']._serialized_start = 2361
    _globals['_HTTPROUTE_FAULTINJECTIONPOLICY_DELAY']._serialized_end = 2436
    _globals['_HTTPROUTE_FAULTINJECTIONPOLICY_ABORT']._serialized_start = 2438
    _globals['_HTTPROUTE_FAULTINJECTIONPOLICY_ABORT']._serialized_end = 2486
    _globals['_HTTPROUTE_STATEFULSESSIONAFFINITYPOLICY']._serialized_start = 2488
    _globals['_HTTPROUTE_STATEFULSESSIONAFFINITYPOLICY']._serialized_end = 2571
    _globals['_HTTPROUTE_HEADERMODIFIER']._serialized_start = 2574
    _globals['_HTTPROUTE_HEADERMODIFIER']._serialized_end = 2856
    _globals['_HTTPROUTE_HEADERMODIFIER_SETENTRY']._serialized_start = 2770
    _globals['_HTTPROUTE_HEADERMODIFIER_SETENTRY']._serialized_end = 2812
    _globals['_HTTPROUTE_HEADERMODIFIER_ADDENTRY']._serialized_start = 2814
    _globals['_HTTPROUTE_HEADERMODIFIER_ADDENTRY']._serialized_end = 2856
    _globals['_HTTPROUTE_URLREWRITE']._serialized_start = 2858
    _globals['_HTTPROUTE_URLREWRITE']._serialized_end = 2921
    _globals['_HTTPROUTE_RETRYPOLICY']._serialized_start = 2923
    _globals['_HTTPROUTE_RETRYPOLICY']._serialized_end = 3035
    _globals['_HTTPROUTE_REQUESTMIRRORPOLICY']._serialized_start = 3037
    _globals['_HTTPROUTE_REQUESTMIRRORPOLICY']._serialized_end = 3164
    _globals['_HTTPROUTE_CORSPOLICY']._serialized_start = 3167
    _globals['_HTTPROUTE_CORSPOLICY']._serialized_end = 3364
    _globals['_HTTPROUTE_HTTPDIRECTRESPONSE']._serialized_start = 3366
    _globals['_HTTPROUTE_HTTPDIRECTRESPONSE']._serialized_end = 3474
    _globals['_HTTPROUTE_ROUTEACTION']._serialized_start = 3477
    _globals['_HTTPROUTE_ROUTEACTION']._serialized_end = 4551
    _globals['_HTTPROUTE_ROUTERULE']._serialized_start = 4554
    _globals['_HTTPROUTE_ROUTERULE']._serialized_end = 4709
    _globals['_HTTPROUTE_LABELSENTRY']._serialized_start = 4711
    _globals['_HTTPROUTE_LABELSENTRY']._serialized_end = 4756
    _globals['_LISTHTTPROUTESREQUEST']._serialized_start = 4871
    _globals['_LISTHTTPROUTESREQUEST']._serialized_end = 5036
    _globals['_LISTHTTPROUTESRESPONSE']._serialized_start = 5039
    _globals['_LISTHTTPROUTESRESPONSE']._serialized_end = 5174
    _globals['_GETHTTPROUTEREQUEST']._serialized_start = 5176
    _globals['_GETHTTPROUTEREQUEST']._serialized_end = 5261
    _globals['_CREATEHTTPROUTEREQUEST']._serialized_start = 5264
    _globals['_CREATEHTTPROUTEREQUEST']._serialized_end = 5451
    _globals['_UPDATEHTTPROUTEREQUEST']._serialized_start = 5454
    _globals['_UPDATEHTTPROUTEREQUEST']._serialized_end = 5601
    _globals['_DELETEHTTPROUTEREQUEST']._serialized_start = 5603
    _globals['_DELETEHTTPROUTEREQUEST']._serialized_end = 5691