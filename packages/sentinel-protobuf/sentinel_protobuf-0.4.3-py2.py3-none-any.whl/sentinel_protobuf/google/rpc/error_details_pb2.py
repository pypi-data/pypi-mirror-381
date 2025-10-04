"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/rpc/error_details.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egoogle/rpc/error_details.proto\x12\ngoogle.rpc\x1a\x1egoogle/protobuf/duration.proto"\x93\x01\n\tErrorInfo\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x0e\n\x06domain\x18\x02 \x01(\t\x125\n\x08metadata\x18\x03 \x03(\x0b2#.google.rpc.ErrorInfo.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01";\n\tRetryInfo\x12.\n\x0bretry_delay\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration"2\n\tDebugInfo\x12\x15\n\rstack_entries\x18\x01 \x03(\t\x12\x0e\n\x06detail\x18\x02 \x01(\t"\x8f\x03\n\x0cQuotaFailure\x126\n\nviolations\x18\x01 \x03(\x0b2".google.rpc.QuotaFailure.Violation\x1a\xc6\x02\n\tViolation\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x13\n\x0bapi_service\x18\x03 \x01(\t\x12\x14\n\x0cquota_metric\x18\x04 \x01(\t\x12\x10\n\x08quota_id\x18\x05 \x01(\t\x12Q\n\x10quota_dimensions\x18\x06 \x03(\x0b27.google.rpc.QuotaFailure.Violation.QuotaDimensionsEntry\x12\x13\n\x0bquota_value\x18\x07 \x01(\x03\x12\x1f\n\x12future_quota_value\x18\x08 \x01(\x03H\x00\x88\x01\x01\x1a6\n\x14QuotaDimensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x15\n\x13_future_quota_value"\x95\x01\n\x13PreconditionFailure\x12=\n\nviolations\x18\x01 \x03(\x0b2).google.rpc.PreconditionFailure.Violation\x1a?\n\tViolation\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t"\xcc\x01\n\nBadRequest\x12?\n\x10field_violations\x18\x01 \x03(\x0b2%.google.rpc.BadRequest.FieldViolation\x1a}\n\x0eFieldViolation\x12\r\n\x05field\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t\x127\n\x11localized_message\x18\x04 \x01(\x0b2\x1c.google.rpc.LocalizedMessage"7\n\x0bRequestInfo\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x14\n\x0cserving_data\x18\x02 \x01(\t"`\n\x0cResourceInfo\x12\x15\n\rresource_type\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t"V\n\x04Help\x12$\n\x05links\x18\x01 \x03(\x0b2\x15.google.rpc.Help.Link\x1a(\n\x04Link\x12\x13\n\x0bdescription\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t"3\n\x10LocalizedMessage\x12\x0e\n\x06locale\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\tBl\n\x0ecom.google.rpcB\x11ErrorDetailsProtoP\x01Z?google.golang.org/genproto/googleapis/rpc/errdetails;errdetails\xa2\x02\x03RPCb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.rpc.error_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.rpcB\x11ErrorDetailsProtoP\x01Z?google.golang.org/genproto/googleapis/rpc/errdetails;errdetails\xa2\x02\x03RPC'
    _globals['_ERRORINFO_METADATAENTRY']._loaded_options = None
    _globals['_ERRORINFO_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_QUOTAFAILURE_VIOLATION_QUOTADIMENSIONSENTRY']._loaded_options = None
    _globals['_QUOTAFAILURE_VIOLATION_QUOTADIMENSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_ERRORINFO']._serialized_start = 79
    _globals['_ERRORINFO']._serialized_end = 226
    _globals['_ERRORINFO_METADATAENTRY']._serialized_start = 179
    _globals['_ERRORINFO_METADATAENTRY']._serialized_end = 226
    _globals['_RETRYINFO']._serialized_start = 228
    _globals['_RETRYINFO']._serialized_end = 287
    _globals['_DEBUGINFO']._serialized_start = 289
    _globals['_DEBUGINFO']._serialized_end = 339
    _globals['_QUOTAFAILURE']._serialized_start = 342
    _globals['_QUOTAFAILURE']._serialized_end = 741
    _globals['_QUOTAFAILURE_VIOLATION']._serialized_start = 415
    _globals['_QUOTAFAILURE_VIOLATION']._serialized_end = 741
    _globals['_QUOTAFAILURE_VIOLATION_QUOTADIMENSIONSENTRY']._serialized_start = 664
    _globals['_QUOTAFAILURE_VIOLATION_QUOTADIMENSIONSENTRY']._serialized_end = 718
    _globals['_PRECONDITIONFAILURE']._serialized_start = 744
    _globals['_PRECONDITIONFAILURE']._serialized_end = 893
    _globals['_PRECONDITIONFAILURE_VIOLATION']._serialized_start = 830
    _globals['_PRECONDITIONFAILURE_VIOLATION']._serialized_end = 893
    _globals['_BADREQUEST']._serialized_start = 896
    _globals['_BADREQUEST']._serialized_end = 1100
    _globals['_BADREQUEST_FIELDVIOLATION']._serialized_start = 975
    _globals['_BADREQUEST_FIELDVIOLATION']._serialized_end = 1100
    _globals['_REQUESTINFO']._serialized_start = 1102
    _globals['_REQUESTINFO']._serialized_end = 1157
    _globals['_RESOURCEINFO']._serialized_start = 1159
    _globals['_RESOURCEINFO']._serialized_end = 1255
    _globals['_HELP']._serialized_start = 1257
    _globals['_HELP']._serialized_end = 1343
    _globals['_HELP_LINK']._serialized_start = 1303
    _globals['_HELP_LINK']._serialized_end = 1343
    _globals['_LOCALIZEDMESSAGE']._serialized_start = 1345
    _globals['_LOCALIZEDMESSAGE']._serialized_end = 1396