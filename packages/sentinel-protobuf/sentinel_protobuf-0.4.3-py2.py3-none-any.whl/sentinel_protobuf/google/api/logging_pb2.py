"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/api/logging.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18google/api/logging.proto\x12\ngoogle.api"\xd7\x01\n\x07Logging\x12E\n\x15producer_destinations\x18\x01 \x03(\x0b2&.google.api.Logging.LoggingDestination\x12E\n\x15consumer_destinations\x18\x02 \x03(\x0b2&.google.api.Logging.LoggingDestination\x1a>\n\x12LoggingDestination\x12\x1a\n\x12monitored_resource\x18\x03 \x01(\t\x12\x0c\n\x04logs\x18\x01 \x03(\tBn\n\x0ecom.google.apiB\x0cLoggingProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.logging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x0cLoggingProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPI'
    _globals['_LOGGING']._serialized_start = 41
    _globals['_LOGGING']._serialized_end = 256
    _globals['_LOGGING_LOGGINGDESTINATION']._serialized_start = 194
    _globals['_LOGGING_LOGGINGDESTINATION']._serialized_end = 256