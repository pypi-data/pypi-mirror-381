"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/compute/logging/dr/v1/disaster_recovery_event.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/compute/logging/dr/v1/disaster_recovery_event.proto\x12\x1cgoogle.compute.logging.dr.v1"\xf8\x01\n\x15DisasterRecoveryEvent\x12S\n\x08severity\x18\x01 \x01(\x0e2<.google.compute.logging.dr.v1.DisasterRecoveryEvent.SeverityH\x00\x88\x01\x01\x12\x14\n\x07details\x18\x02 \x01(\tH\x01\x88\x01\x01"[\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x13\n\x0fACTION_REQUIRED\x10\x01\x12\x14\n\x10ACTION_SUGGESTED\x10\x02\x12\n\n\x06NOTICE\x10\x03B\x0b\n\t_severityB\n\n\x08_detailsB\xe1\x01\n com.google.compute.logging.dr.v1B\x1aDisasterRecoveryEventProtoP\x01Z>google.golang.org/genproto/googleapis/compute/logging/dr/v1;dr\xaa\x02\x1cGoogle.Compute.Logging.Dr.V1\xca\x02\x1cGoogle\\Compute\\Logging\\Dr\\V1\xea\x02 Google::Compute::Logging::Dr::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.compute.logging.dr.v1.disaster_recovery_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.compute.logging.dr.v1B\x1aDisasterRecoveryEventProtoP\x01Z>google.golang.org/genproto/googleapis/compute/logging/dr/v1;dr\xaa\x02\x1cGoogle.Compute.Logging.Dr.V1\xca\x02\x1cGoogle\\Compute\\Logging\\Dr\\V1\xea\x02 Google::Compute::Logging::Dr::V1'
    _globals['_DISASTERRECOVERYEVENT']._serialized_start = 93
    _globals['_DISASTERRECOVERYEVENT']._serialized_end = 341
    _globals['_DISASTERRECOVERYEVENT_SEVERITY']._serialized_start = 225
    _globals['_DISASTERRECOVERYEVENT_SEVERITY']._serialized_end = 316