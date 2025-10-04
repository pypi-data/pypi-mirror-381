"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/routing/v2/speed_reading_interval.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/maps/routing/v2/speed_reading_interval.proto\x12\x16google.maps.routing.v2"\xbc\x02\n\x14SpeedReadingInterval\x12\'\n\x1astart_polyline_point_index\x18\x01 \x01(\x05H\x01\x88\x01\x01\x12%\n\x18end_polyline_point_index\x18\x02 \x01(\x05H\x02\x88\x01\x01\x12C\n\x05speed\x18\x03 \x01(\x0e22.google.maps.routing.v2.SpeedReadingInterval.SpeedH\x00"E\n\x05Speed\x12\x15\n\x11SPEED_UNSPECIFIED\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x08\n\x04SLOW\x10\x02\x12\x0f\n\x0bTRAFFIC_JAM\x10\x03B\x0c\n\nspeed_typeB\x1d\n\x1b_start_polyline_point_indexB\x1b\n\x19_end_polyline_point_indexB\xcb\x01\n\x1acom.google.maps.routing.v2B\x19SpeedReadingIntervalProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.speed_reading_interval_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\x19SpeedReadingIntervalProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_SPEEDREADINGINTERVAL']._serialized_start = 80
    _globals['_SPEEDREADINGINTERVAL']._serialized_end = 396
    _globals['_SPEEDREADINGINTERVAL_SPEED']._serialized_start = 253
    _globals['_SPEEDREADINGINTERVAL_SPEED']._serialized_end = 322