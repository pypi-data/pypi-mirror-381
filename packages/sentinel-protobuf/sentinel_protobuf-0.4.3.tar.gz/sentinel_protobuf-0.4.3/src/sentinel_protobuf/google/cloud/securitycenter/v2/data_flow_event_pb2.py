"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/securitycenter/v2/data_flow_event.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/securitycenter/v2/data_flow_event.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x1fgoogle/protobuf/timestamp.proto"\x97\x02\n\rDataFlowEvent\x12\x10\n\x08event_id\x18\x01 \x01(\t\x12\x17\n\x0fprincipal_email\x18\x02 \x01(\t\x12J\n\toperation\x18\x03 \x01(\x0e27.google.cloud.securitycenter.v2.DataFlowEvent.Operation\x12\x19\n\x11violated_location\x18\x04 \x01(\t\x12.\n\nevent_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp"D\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\x08\n\x04READ\x10\x01\x12\x08\n\x04MOVE\x10\x02\x12\x08\n\x04COPY\x10\x03B\xec\x01\n"com.google.cloud.securitycenter.v2B\x12DataFlowEventProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.data_flow_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x12DataFlowEventProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_DATAFLOWEVENT']._serialized_start = 122
    _globals['_DATAFLOWEVENT']._serialized_end = 401
    _globals['_DATAFLOWEVENT_OPERATION']._serialized_start = 333
    _globals['_DATAFLOWEVENT_OPERATION']._serialized_end = 401