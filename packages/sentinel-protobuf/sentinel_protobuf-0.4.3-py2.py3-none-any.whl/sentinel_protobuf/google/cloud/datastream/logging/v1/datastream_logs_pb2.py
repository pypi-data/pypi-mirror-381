"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/datastream/logging/v1/datastream_logs.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.cloud.datastream.v1 import datastream_resources_pb2 as google_dot_cloud_dot_datastream_dot_v1_dot_datastream__resources__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/datastream/logging/v1/datastream_logs.proto\x12"google.cloud.datastream.logging.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a5google/cloud/datastream/v1/datastream_resources.proto"\x98\x02\n\x16StreamActivityLogEntry\x12\x12\n\nevent_code\x18\x01 \x01(\t\x12\x15\n\revent_message\x18\x02 \x01(\t\x12k\n\x13stream_state_change\x18d \x01(\x0b2L.google.cloud.datastream.logging.v1.StreamActivityLogEntry.StreamStateChangeH\x00\x1aU\n\x11StreamStateChange\x12@\n\tnew_state\x18\x01 \x01(\x0e2(.google.cloud.datastream.v1.Stream.StateB\x03\xe0A\x03B\x0f\n\revent_payloadB\xf4\x01\n&com.google.cloud.datastream.logging.v1B\x13DatastreamLogsProtoP\x01Z@cloud.google.com/go/datastream/logging/apiv1/loggingpb;loggingpb\xaa\x02"Google.Cloud.Datastream.Logging.V1\xca\x02"Google\\Cloud\\Datastream\\Logging\\V1\xea\x02&Google::Cloud::Datastream::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datastream.logging.v1.datastream_logs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.datastream.logging.v1B\x13DatastreamLogsProtoP\x01Z@cloud.google.com/go/datastream/logging/apiv1/loggingpb;loggingpb\xaa\x02"Google.Cloud.Datastream.Logging.V1\xca\x02"Google\\Cloud\\Datastream\\Logging\\V1\xea\x02&Google::Cloud::Datastream::Logging::V1'
    _globals['_STREAMACTIVITYLOGENTRY_STREAMSTATECHANGE'].fields_by_name['new_state']._loaded_options = None
    _globals['_STREAMACTIVITYLOGENTRY_STREAMSTATECHANGE'].fields_by_name['new_state']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMACTIVITYLOGENTRY']._serialized_start = 185
    _globals['_STREAMACTIVITYLOGENTRY']._serialized_end = 465
    _globals['_STREAMACTIVITYLOGENTRY_STREAMSTATECHANGE']._serialized_start = 363
    _globals['_STREAMACTIVITYLOGENTRY_STREAMSTATECHANGE']._serialized_end = 448