"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/appengine/logging/v1/request_log.proto')
_sym_db = _symbol_database.Default()
from .....google.logging.type import log_severity_pb2 as google_dot_logging_dot_type_dot_log__severity__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/appengine/logging/v1/request_log.proto\x12\x1bgoogle.appengine.logging.v1\x1a&google/logging/type/log_severity.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc2\x01\n\x07LogLine\x12(\n\x04time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x122\n\x08severity\x18\x02 \x01(\x0e2 .google.logging.type.LogSeverity\x12\x13\n\x0blog_message\x18\x03 \x01(\t\x12D\n\x0fsource_location\x18\x04 \x01(\x0b2+.google.appengine.logging.v1.SourceLocation"C\n\x0eSourceLocation\x12\x0c\n\x04file\x18\x01 \x01(\t\x12\x0c\n\x04line\x18\x02 \x01(\x03\x12\x15\n\rfunction_name\x18\x03 \x01(\t":\n\x0fSourceReference\x12\x12\n\nrepository\x18\x01 \x01(\t\x12\x13\n\x0brevision_id\x18\x02 \x01(\t"\xd5\x06\n\nRequestLog\x12\x0e\n\x06app_id\x18\x01 \x01(\t\x12\x11\n\tmodule_id\x18% \x01(\t\x12\x12\n\nversion_id\x18\x02 \x01(\t\x12\x12\n\nrequest_id\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t\x12.\n\nstart_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12*\n\x07latency\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x12\x13\n\x0bmega_cycles\x18\t \x01(\x03\x12\x0e\n\x06method\x18\n \x01(\t\x12\x10\n\x08resource\x18\x0b \x01(\t\x12\x14\n\x0chttp_version\x18\x0c \x01(\t\x12\x0e\n\x06status\x18\r \x01(\x05\x12\x15\n\rresponse_size\x18\x0e \x01(\x03\x12\x10\n\x08referrer\x18\x0f \x01(\t\x12\x12\n\nuser_agent\x18\x10 \x01(\t\x12\x10\n\x08nickname\x18( \x01(\t\x12\x15\n\rurl_map_entry\x18\x11 \x01(\t\x12\x0c\n\x04host\x18\x14 \x01(\t\x12\x0c\n\x04cost\x18\x15 \x01(\x01\x12\x17\n\x0ftask_queue_name\x18\x16 \x01(\t\x12\x11\n\ttask_name\x18\x17 \x01(\t\x12\x1b\n\x13was_loading_request\x18\x18 \x01(\x08\x12/\n\x0cpending_time\x18\x19 \x01(\x0b2\x19.google.protobuf.Duration\x12\x16\n\x0einstance_index\x18\x1a \x01(\x05\x12\x10\n\x08finished\x18\x1b \x01(\x08\x12\r\n\x05first\x18* \x01(\x08\x12\x13\n\x0binstance_id\x18\x1c \x01(\t\x122\n\x04line\x18\x1d \x03(\x0b2$.google.appengine.logging.v1.LogLine\x12\x1a\n\x12app_engine_release\x18& \x01(\t\x12\x10\n\x08trace_id\x18\' \x01(\t\x12\x15\n\rtrace_sampled\x18+ \x01(\x08\x12F\n\x10source_reference\x18) \x03(\x0b2,.google.appengine.logging.v1.SourceReferenceB\xe8\x01\n\x1fcom.google.appengine.logging.v1B\x0fRequestLogProtoP\x01ZBgoogle.golang.org/genproto/googleapis/appengine/logging/v1;logging\xaa\x02!Google.Cloud.AppEngine.Logging.V1\xca\x02!Google\\Cloud\\AppEngine\\Logging\\V1\xea\x02%Google::Cloud::AppEngine::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.logging.v1.request_log_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.appengine.logging.v1B\x0fRequestLogProtoP\x01ZBgoogle.golang.org/genproto/googleapis/appengine/logging/v1;logging\xaa\x02!Google.Cloud.AppEngine.Logging.V1\xca\x02!Google\\Cloud\\AppEngine\\Logging\\V1\xea\x02%Google::Cloud::AppEngine::Logging::V1'
    _globals['_LOGLINE']._serialized_start = 184
    _globals['_LOGLINE']._serialized_end = 378
    _globals['_SOURCELOCATION']._serialized_start = 380
    _globals['_SOURCELOCATION']._serialized_end = 447
    _globals['_SOURCEREFERENCE']._serialized_start = 449
    _globals['_SOURCEREFERENCE']._serialized_end = 507
    _globals['_REQUESTLOG']._serialized_start = 510
    _globals['_REQUESTLOG']._serialized_end = 1363