"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/visionai/v1/streaming_resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/visionai/v1/streaming_resources.proto\x12\x18google.cloud.visionai.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcf\x01\n\x19GstreamerBufferDescriptor\x12\x13\n\x0bcaps_string\x18\x01 \x01(\t\x12\x14\n\x0cis_key_frame\x18\x02 \x01(\x08\x12,\n\x08pts_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08dts_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12+\n\x08duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration"C\n\x12RawImageDescriptor\x12\x0e\n\x06format\x18\x01 \x01(\t\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05"\xc9\x02\n\nPacketType\x12\x12\n\ntype_class\x18\x01 \x01(\t\x12L\n\x0ftype_descriptor\x18\x02 \x01(\x0b23.google.cloud.visionai.v1.PacketType.TypeDescriptor\x1a\xd8\x01\n\x0eTypeDescriptor\x12Z\n\x1bgstreamer_buffer_descriptor\x18\x02 \x01(\x0b23.google.cloud.visionai.v1.GstreamerBufferDescriptorH\x00\x12L\n\x14raw_image_descriptor\x18\x03 \x01(\x0b2,.google.cloud.visionai.v1.RawImageDescriptorH\x00\x12\x0c\n\x04type\x18\x01 \x01(\tB\x0e\n\x0ctype_details"Q\n\x0eServerMetadata\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12/\n\x0bingest_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"E\n\x0eSeriesMetadata\x123\n\x06series\x18\x01 \x01(\tB#\xfaA \n\x1evisionai.googleapis.com/Series"\xf4\x02\n\x0cPacketHeader\x125\n\x0ccapture_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x04\x12:\n\x04type\x18\x02 \x01(\x0b2$.google.cloud.visionai.v1.PacketTypeB\x06\xe0A\x04\xe0A\x05\x12.\n\x08metadata\x18\x03 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x04\x12F\n\x0fserver_metadata\x18\x04 \x01(\x0b2(.google.cloud.visionai.v1.ServerMetadataB\x03\xe0A\x03\x12I\n\x0fseries_metadata\x18\x05 \x01(\x0b2(.google.cloud.visionai.v1.SeriesMetadataB\x06\xe0A\x04\xe0A\x05\x12\x12\n\x05flags\x18\x06 \x01(\x05B\x03\xe0A\x05\x12\x1a\n\rtrace_context\x18\x07 \x01(\tB\x03\xe0A\x05"Q\n\x06Packet\x126\n\x06header\x18\x01 \x01(\x0b2&.google.cloud.visionai.v1.PacketHeader\x12\x0f\n\x07payload\x18\x02 \x01(\x0cB\xc7\x01\n\x1ccom.google.cloud.visionai.v1B\x17StreamingResourcesProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1.streaming_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.visionai.v1B\x17StreamingResourcesProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1'
    _globals['_SERIESMETADATA'].fields_by_name['series']._loaded_options = None
    _globals['_SERIESMETADATA'].fields_by_name['series']._serialized_options = b'\xfaA \n\x1evisionai.googleapis.com/Series'
    _globals['_PACKETHEADER'].fields_by_name['capture_time']._loaded_options = None
    _globals['_PACKETHEADER'].fields_by_name['capture_time']._serialized_options = b'\xe0A\x04'
    _globals['_PACKETHEADER'].fields_by_name['type']._loaded_options = None
    _globals['_PACKETHEADER'].fields_by_name['type']._serialized_options = b'\xe0A\x04\xe0A\x05'
    _globals['_PACKETHEADER'].fields_by_name['metadata']._loaded_options = None
    _globals['_PACKETHEADER'].fields_by_name['metadata']._serialized_options = b'\xe0A\x04'
    _globals['_PACKETHEADER'].fields_by_name['server_metadata']._loaded_options = None
    _globals['_PACKETHEADER'].fields_by_name['server_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_PACKETHEADER'].fields_by_name['series_metadata']._loaded_options = None
    _globals['_PACKETHEADER'].fields_by_name['series_metadata']._serialized_options = b'\xe0A\x04\xe0A\x05'
    _globals['_PACKETHEADER'].fields_by_name['flags']._loaded_options = None
    _globals['_PACKETHEADER'].fields_by_name['flags']._serialized_options = b'\xe0A\x05'
    _globals['_PACKETHEADER'].fields_by_name['trace_context']._loaded_options = None
    _globals['_PACKETHEADER'].fields_by_name['trace_context']._serialized_options = b'\xe0A\x05'
    _globals['_GSTREAMERBUFFERDESCRIPTOR']._serialized_start = 236
    _globals['_GSTREAMERBUFFERDESCRIPTOR']._serialized_end = 443
    _globals['_RAWIMAGEDESCRIPTOR']._serialized_start = 445
    _globals['_RAWIMAGEDESCRIPTOR']._serialized_end = 512
    _globals['_PACKETTYPE']._serialized_start = 515
    _globals['_PACKETTYPE']._serialized_end = 844
    _globals['_PACKETTYPE_TYPEDESCRIPTOR']._serialized_start = 628
    _globals['_PACKETTYPE_TYPEDESCRIPTOR']._serialized_end = 844
    _globals['_SERVERMETADATA']._serialized_start = 846
    _globals['_SERVERMETADATA']._serialized_end = 927
    _globals['_SERIESMETADATA']._serialized_start = 929
    _globals['_SERIESMETADATA']._serialized_end = 998
    _globals['_PACKETHEADER']._serialized_start = 1001
    _globals['_PACKETHEADER']._serialized_end = 1373
    _globals['_PACKET']._serialized_start = 1375
    _globals['_PACKET']._serialized_end = 1456