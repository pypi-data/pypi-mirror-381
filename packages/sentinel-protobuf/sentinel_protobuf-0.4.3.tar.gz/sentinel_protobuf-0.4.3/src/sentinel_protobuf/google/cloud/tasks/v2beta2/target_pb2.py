"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/tasks/v2beta2/target.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/tasks/v2beta2/target.proto\x12\x1agoogle.cloud.tasks.v2beta2\x1a\x1fgoogle/api/field_behavior.proto"\x0c\n\nPullTarget"+\n\x0bPullMessage\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12\x0b\n\x03tag\x18\x02 \x01(\t"h\n\x13AppEngineHttpTarget\x12Q\n\x1bapp_engine_routing_override\x18\x01 \x01(\x0b2,.google.cloud.tasks.v2beta2.AppEngineRouting"\xc4\x02\n\x14AppEngineHttpRequest\x12;\n\x0bhttp_method\x18\x01 \x01(\x0e2&.google.cloud.tasks.v2beta2.HttpMethod\x12H\n\x12app_engine_routing\x18\x02 \x01(\x0b2,.google.cloud.tasks.v2beta2.AppEngineRouting\x12\x14\n\x0crelative_url\x18\x03 \x01(\t\x12N\n\x07headers\x18\x04 \x03(\x0b2=.google.cloud.tasks.v2beta2.AppEngineHttpRequest.HeadersEntry\x12\x0f\n\x07payload\x18\x05 \x01(\x0c\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x10AppEngineRouting\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08instance\x18\x03 \x01(\t\x12\x0c\n\x04host\x18\x04 \x01(\t"\xf5\x02\n\x0bHttpRequest\x12\x10\n\x03url\x18\x01 \x01(\tB\x03\xe0A\x02\x12;\n\x0bhttp_method\x18\x02 \x01(\x0e2&.google.cloud.tasks.v2beta2.HttpMethod\x12E\n\x07headers\x18\x03 \x03(\x0b24.google.cloud.tasks.v2beta2.HttpRequest.HeadersEntry\x12\x0c\n\x04body\x18\x04 \x01(\x0c\x12=\n\x0boauth_token\x18\x05 \x01(\x0b2&.google.cloud.tasks.v2beta2.OAuthTokenH\x00\x12;\n\noidc_token\x18\x06 \x01(\x0b2%.google.cloud.tasks.v2beta2.OidcTokenH\x00\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x16\n\x14authorization_header"\x1c\n\x0cPathOverride\x12\x0c\n\x04path\x18\x01 \x01(\t"%\n\rQueryOverride\x12\x14\n\x0cquery_params\x18\x01 \x01(\t"\x97\x04\n\x0bUriOverride\x12C\n\x06scheme\x18\x01 \x01(\x0e2..google.cloud.tasks.v2beta2.UriOverride.SchemeH\x00\x88\x01\x01\x12\x11\n\x04host\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04port\x18\x03 \x01(\x03H\x02\x88\x01\x01\x12?\n\rpath_override\x18\x04 \x01(\x0b2(.google.cloud.tasks.v2beta2.PathOverride\x12A\n\x0equery_override\x18\x05 \x01(\x0b2).google.cloud.tasks.v2beta2.QueryOverride\x12a\n\x19uri_override_enforce_mode\x18\x06 \x01(\x0e2>.google.cloud.tasks.v2beta2.UriOverride.UriOverrideEnforceMode"5\n\x06Scheme\x12\x16\n\x12SCHEME_UNSPECIFIED\x10\x00\x12\x08\n\x04HTTP\x10\x01\x12\t\n\x05HTTPS\x10\x02"b\n\x16UriOverrideEnforceMode\x12)\n%URI_OVERRIDE_ENFORCE_MODE_UNSPECIFIED\x10\x00\x12\x11\n\rIF_NOT_EXISTS\x10\x01\x12\n\n\x06ALWAYS\x10\x02B\t\n\x07_schemeB\x07\n\x05_hostB\x07\n\x05_port"\xe4\x03\n\nHttpTarget\x12=\n\x0curi_override\x18\x01 \x01(\x0b2\'.google.cloud.tasks.v2beta2.UriOverride\x12;\n\x0bhttp_method\x18\x02 \x01(\x0e2&.google.cloud.tasks.v2beta2.HttpMethod\x12O\n\x10header_overrides\x18\x03 \x03(\x0b25.google.cloud.tasks.v2beta2.HttpTarget.HeaderOverride\x12=\n\x0boauth_token\x18\x05 \x01(\x0b2&.google.cloud.tasks.v2beta2.OAuthTokenH\x00\x12;\n\noidc_token\x18\x06 \x01(\x0b2%.google.cloud.tasks.v2beta2.OidcTokenH\x00\x1a$\n\x06Header\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1aO\n\x0eHeaderOverride\x12=\n\x06header\x18\x01 \x01(\x0b2-.google.cloud.tasks.v2beta2.HttpTarget.HeaderB\x16\n\x14authorization_header":\n\nOAuthToken\x12\x1d\n\x15service_account_email\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t"<\n\tOidcToken\x12\x1d\n\x15service_account_email\x18\x01 \x01(\t\x12\x10\n\x08audience\x18\x02 \x01(\t*s\n\nHttpMethod\x12\x1b\n\x17HTTP_METHOD_UNSPECIFIED\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x07\n\x03GET\x10\x02\x12\x08\n\x04HEAD\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06DELETE\x10\x05\x12\t\n\x05PATCH\x10\x06\x12\x0b\n\x07OPTIONS\x10\x07Bt\n\x1ecom.google.cloud.tasks.v2beta2B\x0bTargetProtoP\x01ZCcloud.google.com/go/cloudtasks/apiv2beta2/cloudtaskspb;cloudtaskspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.tasks.v2beta2.target_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.tasks.v2beta2B\x0bTargetProtoP\x01ZCcloud.google.com/go/cloudtasks/apiv2beta2/cloudtaskspb;cloudtaskspb'
    _globals['_APPENGINEHTTPREQUEST_HEADERSENTRY']._loaded_options = None
    _globals['_APPENGINEHTTPREQUEST_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_HTTPREQUEST_HEADERSENTRY']._loaded_options = None
    _globals['_HTTPREQUEST_HEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_HTTPREQUEST'].fields_by_name['url']._loaded_options = None
    _globals['_HTTPREQUEST'].fields_by_name['url']._serialized_options = b'\xe0A\x02'
    _globals['_HTTPMETHOD']._serialized_start = 2274
    _globals['_HTTPMETHOD']._serialized_end = 2389
    _globals['_PULLTARGET']._serialized_start = 104
    _globals['_PULLTARGET']._serialized_end = 116
    _globals['_PULLMESSAGE']._serialized_start = 118
    _globals['_PULLMESSAGE']._serialized_end = 161
    _globals['_APPENGINEHTTPTARGET']._serialized_start = 163
    _globals['_APPENGINEHTTPTARGET']._serialized_end = 267
    _globals['_APPENGINEHTTPREQUEST']._serialized_start = 270
    _globals['_APPENGINEHTTPREQUEST']._serialized_end = 594
    _globals['_APPENGINEHTTPREQUEST_HEADERSENTRY']._serialized_start = 548
    _globals['_APPENGINEHTTPREQUEST_HEADERSENTRY']._serialized_end = 594
    _globals['_APPENGINEROUTING']._serialized_start = 596
    _globals['_APPENGINEROUTING']._serialized_end = 680
    _globals['_HTTPREQUEST']._serialized_start = 683
    _globals['_HTTPREQUEST']._serialized_end = 1056
    _globals['_HTTPREQUEST_HEADERSENTRY']._serialized_start = 548
    _globals['_HTTPREQUEST_HEADERSENTRY']._serialized_end = 594
    _globals['_PATHOVERRIDE']._serialized_start = 1058
    _globals['_PATHOVERRIDE']._serialized_end = 1086
    _globals['_QUERYOVERRIDE']._serialized_start = 1088
    _globals['_QUERYOVERRIDE']._serialized_end = 1125
    _globals['_URIOVERRIDE']._serialized_start = 1128
    _globals['_URIOVERRIDE']._serialized_end = 1663
    _globals['_URIOVERRIDE_SCHEME']._serialized_start = 1481
    _globals['_URIOVERRIDE_SCHEME']._serialized_end = 1534
    _globals['_URIOVERRIDE_URIOVERRIDEENFORCEMODE']._serialized_start = 1536
    _globals['_URIOVERRIDE_URIOVERRIDEENFORCEMODE']._serialized_end = 1634
    _globals['_HTTPTARGET']._serialized_start = 1666
    _globals['_HTTPTARGET']._serialized_end = 2150
    _globals['_HTTPTARGET_HEADER']._serialized_start = 2009
    _globals['_HTTPTARGET_HEADER']._serialized_end = 2045
    _globals['_HTTPTARGET_HEADEROVERRIDE']._serialized_start = 2047
    _globals['_HTTPTARGET_HEADEROVERRIDE']._serialized_end = 2126
    _globals['_OAUTHTOKEN']._serialized_start = 2152
    _globals['_OAUTHTOKEN']._serialized_end = 2210
    _globals['_OIDCTOKEN']._serialized_start = 2212
    _globals['_OIDCTOKEN']._serialized_end = 2272