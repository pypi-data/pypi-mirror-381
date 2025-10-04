"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/routing/v2/geocoding_results.proto')
_sym_db = _symbol_database.Default()
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/maps/routing/v2/geocoding_results.proto\x12\x16google.maps.routing.v2\x1a\x17google/rpc/status.proto"\xcc\x01\n\x10GeocodingResults\x128\n\x06origin\x18\x01 \x01(\x0b2(.google.maps.routing.v2.GeocodedWaypoint\x12=\n\x0bdestination\x18\x02 \x01(\x0b2(.google.maps.routing.v2.GeocodedWaypoint\x12?\n\rintermediates\x18\x03 \x03(\x0b2(.google.maps.routing.v2.GeocodedWaypoint"\xd0\x01\n\x10GeocodedWaypoint\x12+\n\x0fgeocoder_status\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x120\n#intermediate_waypoint_request_index\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x0c\n\x04type\x18\x03 \x03(\t\x12\x15\n\rpartial_match\x18\x04 \x01(\x08\x12\x10\n\x08place_id\x18\x05 \x01(\tB&\n$_intermediate_waypoint_request_indexB\xc7\x01\n\x1acom.google.maps.routing.v2B\x15GeocodingResultsProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.geocoding_results_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\x15GeocodingResultsProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_GEOCODINGRESULTS']._serialized_start = 100
    _globals['_GEOCODINGRESULTS']._serialized_end = 304
    _globals['_GEOCODEDWAYPOINT']._serialized_start = 307
    _globals['_GEOCODEDWAYPOINT']._serialized_end = 515