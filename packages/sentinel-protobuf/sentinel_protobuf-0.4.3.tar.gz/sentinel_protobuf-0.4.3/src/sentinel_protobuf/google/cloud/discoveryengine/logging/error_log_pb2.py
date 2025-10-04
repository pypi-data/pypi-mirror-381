"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/logging/error_log.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/discoveryengine/logging/error_log.proto\x12$google.cloud.discoveryengine.logging\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"!\n\x0eServiceContext\x12\x0f\n\x07service\x18\x01 \x01(\t"2\n\x12HttpRequestContext\x12\x1c\n\x14response_status_code\x18\x01 \x01(\x05"\'\n\x0eSourceLocation\x12\x15\n\rfunction_name\x18\x01 \x01(\t"\xad\x01\n\x0cErrorContext\x12N\n\x0chttp_request\x18\x01 \x01(\x0b28.google.cloud.discoveryengine.logging.HttpRequestContext\x12M\n\x0freport_location\x18\x02 \x01(\x0b24.google.cloud.discoveryengine.logging.SourceLocation"\x88\x01\n\x12ImportErrorContext\x12\x11\n\toperation\x18\x01 \x01(\t\x12\x10\n\x08gcs_path\x18\x02 \x01(\t\x12\x13\n\x0bline_number\x18\x03 \x01(\t\x12\x12\n\x08document\x18\x04 \x01(\tH\x00\x12\x14\n\nuser_event\x18\x05 \x01(\tH\x00B\x0e\n\x0cline_content"\xdd\x01\n\x18ConnectorRunErrorContext\x12\x11\n\toperation\x18\x01 \x01(\t\x12\x16\n\x0edata_connector\x18\x02 \x01(\t\x12\x15\n\rconnector_run\x18\x03 \x01(\t\x12\x0e\n\x06entity\x18\x04 \x01(\t\x12\x11\n\tsync_type\x18\x05 \x01(\t\x12.\n\nstart_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xe9\x03\n\x08ErrorLog\x12M\n\x0fservice_context\x18\x01 \x01(\x0b24.google.cloud.discoveryengine.logging.ServiceContext\x12C\n\x07context\x18\x02 \x01(\x0b22.google.cloud.discoveryengine.logging.ErrorContext\x12\x0f\n\x07message\x18\x03 \x01(\t\x12"\n\x06status\x18\x04 \x01(\x0b2\x12.google.rpc.Status\x120\n\x0frequest_payload\x18\x05 \x01(\x0b2\x17.google.protobuf.Struct\x121\n\x10response_payload\x18\x06 \x01(\x0b2\x17.google.protobuf.Struct\x12P\n\x0eimport_payload\x18\x07 \x01(\x0b28.google.cloud.discoveryengine.logging.ImportErrorContext\x12]\n\x15connector_run_payload\x18\x08 \x01(\x0b2>.google.cloud.discoveryengine.logging.ConnectorRunErrorContextB\x86\x02\n(com.google.cloud.discoveryengine.loggingB\rErrorLogProtoP\x01Z?cloud.google.com/go/discoveryengine/logging/loggingpb;loggingpb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.Logging\xca\x02$Google\\Cloud\\DiscoveryEngine\\Logging\xea\x02\'Google::Cloud::DiscoveryEngine::Loggingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.logging.error_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.loggingB\rErrorLogProtoP\x01Z?cloud.google.com/go/discoveryengine/logging/loggingpb;loggingpb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.Logging\xca\x02$Google\\Cloud\\DiscoveryEngine\\Logging\xea\x02'Google::Cloud::DiscoveryEngine::Logging"
    _globals['_SERVICECONTEXT']._serialized_start = 182
    _globals['_SERVICECONTEXT']._serialized_end = 215
    _globals['_HTTPREQUESTCONTEXT']._serialized_start = 217
    _globals['_HTTPREQUESTCONTEXT']._serialized_end = 267
    _globals['_SOURCELOCATION']._serialized_start = 269
    _globals['_SOURCELOCATION']._serialized_end = 308
    _globals['_ERRORCONTEXT']._serialized_start = 311
    _globals['_ERRORCONTEXT']._serialized_end = 484
    _globals['_IMPORTERRORCONTEXT']._serialized_start = 487
    _globals['_IMPORTERRORCONTEXT']._serialized_end = 623
    _globals['_CONNECTORRUNERRORCONTEXT']._serialized_start = 626
    _globals['_CONNECTORRUNERRORCONTEXT']._serialized_end = 847
    _globals['_ERRORLOG']._serialized_start = 850
    _globals['_ERRORLOG']._serialized_end = 1339