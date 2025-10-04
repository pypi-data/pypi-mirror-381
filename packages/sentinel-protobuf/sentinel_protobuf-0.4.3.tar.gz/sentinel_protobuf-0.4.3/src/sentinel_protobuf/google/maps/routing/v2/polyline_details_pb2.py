"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/routing/v2/polyline_details.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/maps/routing/v2/polyline_details.proto\x12\x16google.maps.routing.v2\x1a\x1fgoogle/api/field_behavior.proto"\xf9\x05\n\x0fPolylineDetails\x12I\n\x0cflyover_info\x18\x0c \x03(\x0b23.google.maps.routing.v2.PolylineDetails.FlyoverInfo\x12P\n\x10narrow_road_info\x18\r \x03(\x0b26.google.maps.routing.v2.PolylineDetails.NarrowRoadInfo\x1ad\n\x12PolylinePointIndex\x12\x18\n\x0bstart_index\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\tend_index\x18\x02 \x01(\x05H\x01\x88\x01\x01B\x0e\n\x0c_start_indexB\x0c\n\n_end_index\x1a\xc0\x01\n\x0bFlyoverInfo\x12W\n\x10flyover_presence\x18\x01 \x01(\x0e28.google.maps.routing.v2.PolylineDetails.RoadFeatureStateB\x03\xe0A\x03\x12X\n\x14polyline_point_index\x18\x02 \x01(\x0b2:.google.maps.routing.v2.PolylineDetails.PolylinePointIndex\x1a\xc7\x01\n\x0eNarrowRoadInfo\x12[\n\x14narrow_road_presence\x18\x01 \x01(\x0e28.google.maps.routing.v2.PolylineDetails.RoadFeatureStateB\x03\xe0A\x03\x12X\n\x14polyline_point_index\x18\x02 \x01(\x0b2:.google.maps.routing.v2.PolylineDetails.PolylinePointIndex"V\n\x10RoadFeatureState\x12"\n\x1eROAD_FEATURE_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06EXISTS\x10\x01\x12\x12\n\x0eDOES_NOT_EXIST\x10\x02B\xc6\x01\n\x1acom.google.maps.routing.v2B\x14PolylineDetailsProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.polyline_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\x14PolylineDetailsProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_POLYLINEDETAILS_FLYOVERINFO'].fields_by_name['flyover_presence']._loaded_options = None
    _globals['_POLYLINEDETAILS_FLYOVERINFO'].fields_by_name['flyover_presence']._serialized_options = b'\xe0A\x03'
    _globals['_POLYLINEDETAILS_NARROWROADINFO'].fields_by_name['narrow_road_presence']._loaded_options = None
    _globals['_POLYLINEDETAILS_NARROWROADINFO'].fields_by_name['narrow_road_presence']._serialized_options = b'\xe0A\x03'
    _globals['_POLYLINEDETAILS']._serialized_start = 107
    _globals['_POLYLINEDETAILS']._serialized_end = 868
    _globals['_POLYLINEDETAILS_POLYLINEPOINTINDEX']._serialized_start = 283
    _globals['_POLYLINEDETAILS_POLYLINEPOINTINDEX']._serialized_end = 383
    _globals['_POLYLINEDETAILS_FLYOVERINFO']._serialized_start = 386
    _globals['_POLYLINEDETAILS_FLYOVERINFO']._serialized_end = 578
    _globals['_POLYLINEDETAILS_NARROWROADINFO']._serialized_start = 581
    _globals['_POLYLINEDETAILS_NARROWROADINFO']._serialized_end = 780
    _globals['_POLYLINEDETAILS_ROADFEATURESTATE']._serialized_start = 782
    _globals['_POLYLINEDETAILS_ROADFEATURESTATE']._serialized_end = 868