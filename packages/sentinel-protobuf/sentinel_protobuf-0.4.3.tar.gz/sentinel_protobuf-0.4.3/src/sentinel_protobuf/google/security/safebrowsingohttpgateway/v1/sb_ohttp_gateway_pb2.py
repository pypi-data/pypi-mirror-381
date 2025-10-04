"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/security/safebrowsingohttpgateway/v1/sb_ohttp_gateway.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/security/safebrowsingohttpgateway/v1/sb_ohttp_gateway.proto\x12+google.security.safebrowsingohttpgateway.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/httpbody.proto2\xb1\x02\n\x18SafeBrowsingOhttpGateway\x12\x84\x01\n\x1eHandleOhttpEncapsulatedRequest\x12\x14.google.api.HttpBody\x1a\x14.google.api.HttpBody"6\xdaA\x00\x82\xd3\xe4\x93\x02-"(/v1/ohttp:handleOhttpEncapsulatedRequest:\x01*\x12b\n\x10GetHpkeKeyConfig\x12\x14.google.api.HttpBody\x1a\x14.google.api.HttpBody""\xdaA\x00\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/ohttp/hpkekeyconfig\x1a*\xcaA\'safebrowsingohttpgateway.googleapis.comB\xad\x01\n/com.google.security.safebrowsingohttpgateway.v1B\x13SbOhttpGatewayProtoP\x01Zcgoogle.golang.org/genproto/googleapis/security/safebrowsingohttpgateway/v1;safebrowsingohttpgatewayb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.security.safebrowsingohttpgateway.v1.sb_ohttp_gateway_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.security.safebrowsingohttpgateway.v1B\x13SbOhttpGatewayProtoP\x01Zcgoogle.golang.org/genproto/googleapis/security/safebrowsingohttpgateway/v1;safebrowsingohttpgateway'
    _globals['_SAFEBROWSINGOHTTPGATEWAY']._loaded_options = None
    _globals['_SAFEBROWSINGOHTTPGATEWAY']._serialized_options = b"\xcaA'safebrowsingohttpgateway.googleapis.com"
    _globals['_SAFEBROWSINGOHTTPGATEWAY'].methods_by_name['HandleOhttpEncapsulatedRequest']._loaded_options = None
    _globals['_SAFEBROWSINGOHTTPGATEWAY'].methods_by_name['HandleOhttpEncapsulatedRequest']._serialized_options = b'\xdaA\x00\x82\xd3\xe4\x93\x02-"(/v1/ohttp:handleOhttpEncapsulatedRequest:\x01*'
    _globals['_SAFEBROWSINGOHTTPGATEWAY'].methods_by_name['GetHpkeKeyConfig']._loaded_options = None
    _globals['_SAFEBROWSINGOHTTPGATEWAY'].methods_by_name['GetHpkeKeyConfig']._serialized_options = b'\xdaA\x00\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/ohttp/hpkekeyconfig'
    _globals['_SAFEBROWSINGOHTTPGATEWAY']._serialized_start = 198
    _globals['_SAFEBROWSINGOHTTPGATEWAY']._serialized_end = 503