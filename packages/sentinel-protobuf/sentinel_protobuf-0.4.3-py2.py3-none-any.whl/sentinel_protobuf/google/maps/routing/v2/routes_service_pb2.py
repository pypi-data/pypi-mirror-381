"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/routing/v2/routes_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.maps.routing.v2 import fallback_info_pb2 as google_dot_maps_dot_routing_dot_v2_dot_fallback__info__pb2
from .....google.maps.routing.v2 import geocoding_results_pb2 as google_dot_maps_dot_routing_dot_v2_dot_geocoding__results__pb2
from .....google.maps.routing.v2 import polyline_pb2 as google_dot_maps_dot_routing_dot_v2_dot_polyline__pb2
from .....google.maps.routing.v2 import route_pb2 as google_dot_maps_dot_routing_dot_v2_dot_route__pb2
from .....google.maps.routing.v2 import route_modifiers_pb2 as google_dot_maps_dot_routing_dot_v2_dot_route__modifiers__pb2
from .....google.maps.routing.v2 import route_travel_mode_pb2 as google_dot_maps_dot_routing_dot_v2_dot_route__travel__mode__pb2
from .....google.maps.routing.v2 import routing_preference_pb2 as google_dot_maps_dot_routing_dot_v2_dot_routing__preference__pb2
from .....google.maps.routing.v2 import traffic_model_pb2 as google_dot_maps_dot_routing_dot_v2_dot_traffic__model__pb2
from .....google.maps.routing.v2 import transit_preferences_pb2 as google_dot_maps_dot_routing_dot_v2_dot_transit__preferences__pb2
from .....google.maps.routing.v2 import units_pb2 as google_dot_maps_dot_routing_dot_v2_dot_units__pb2
from .....google.maps.routing.v2 import waypoint_pb2 as google_dot_maps_dot_routing_dot_v2_dot_waypoint__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import localized_text_pb2 as google_dot_type_dot_localized__text__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/maps/routing/v2/routes_service.proto\x12\x16google.maps.routing.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a*google/maps/routing/v2/fallback_info.proto\x1a.google/maps/routing/v2/geocoding_results.proto\x1a%google/maps/routing/v2/polyline.proto\x1a"google/maps/routing/v2/route.proto\x1a,google/maps/routing/v2/route_modifiers.proto\x1a.google/maps/routing/v2/route_travel_mode.proto\x1a/google/maps/routing/v2/routing_preference.proto\x1a*google/maps/routing/v2/traffic_model.proto\x1a0google/maps/routing/v2/transit_preferences.proto\x1a"google/maps/routing/v2/units.proto\x1a%google/maps/routing/v2/waypoint.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a google/type/localized_text.proto"\xe7\x0b\n\x14ComputeRoutesRequest\x125\n\x06origin\x18\x01 \x01(\x0b2 .google.maps.routing.v2.WaypointB\x03\xe0A\x02\x12:\n\x0bdestination\x18\x02 \x01(\x0b2 .google.maps.routing.v2.WaypointB\x03\xe0A\x02\x12<\n\rintermediates\x18\x03 \x03(\x0b2 .google.maps.routing.v2.WaypointB\x03\xe0A\x01\x12A\n\x0btravel_mode\x18\x04 \x01(\x0e2\'.google.maps.routing.v2.RouteTravelModeB\x03\xe0A\x01\x12J\n\x12routing_preference\x18\x05 \x01(\x0e2).google.maps.routing.v2.RoutingPreferenceB\x03\xe0A\x01\x12F\n\x10polyline_quality\x18\x06 \x01(\x0e2\'.google.maps.routing.v2.PolylineQualityB\x03\xe0A\x01\x12H\n\x11polyline_encoding\x18\x0c \x01(\x0e2(.google.maps.routing.v2.PolylineEncodingB\x03\xe0A\x01\x127\n\x0edeparture_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x125\n\x0carrival_time\x18\x13 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12\'\n\x1acompute_alternative_routes\x18\x08 \x01(\x08B\x03\xe0A\x01\x12D\n\x0froute_modifiers\x18\t \x01(\x0b2&.google.maps.routing.v2.RouteModifiersB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18\n \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bregion_code\x18\x10 \x01(\tB\x03\xe0A\x01\x121\n\x05units\x18\x0b \x01(\x0e2\x1d.google.maps.routing.v2.UnitsB\x03\xe0A\x01\x12$\n\x17optimize_waypoint_order\x18\r \x01(\x08B\x03\xe0A\x01\x12d\n\x1arequested_reference_routes\x18\x0e \x03(\x0e2;.google.maps.routing.v2.ComputeRoutesRequest.ReferenceRouteB\x03\xe0A\x01\x12^\n\x12extra_computations\x18\x0f \x03(\x0e2=.google.maps.routing.v2.ComputeRoutesRequest.ExtraComputationB\x03\xe0A\x01\x12@\n\rtraffic_model\x18\x12 \x01(\x0e2$.google.maps.routing.v2.TrafficModelB\x03\xe0A\x01\x12L\n\x13transit_preferences\x18\x14 \x01(\x0b2*.google.maps.routing.v2.TransitPreferencesB\x03\xe0A\x01"[\n\x0eReferenceRoute\x12\x1f\n\x1bREFERENCE_ROUTE_UNSPECIFIED\x10\x00\x12\x12\n\x0eFUEL_EFFICIENT\x10\x01\x12\x14\n\x10SHORTER_DISTANCE\x10\x02"\xdb\x01\n\x10ExtraComputation\x12!\n\x1dEXTRA_COMPUTATION_UNSPECIFIED\x10\x00\x12\t\n\x05TOLLS\x10\x01\x12\x14\n\x10FUEL_CONSUMPTION\x10\x02\x12\x17\n\x13TRAFFIC_ON_POLYLINE\x10\x03\x12*\n&HTML_FORMATTED_NAVIGATION_INSTRUCTIONS\x10\x04\x12\x1c\n\x18FLYOVER_INFO_ON_POLYLINE\x10\x07\x12 \n\x1cNARROW_ROAD_INFO_ON_POLYLINE\x10\x08"\xc8\x01\n\x15ComputeRoutesResponse\x12-\n\x06routes\x18\x01 \x03(\x0b2\x1d.google.maps.routing.v2.Route\x12;\n\rfallback_info\x18\x02 \x01(\x0b2$.google.maps.routing.v2.FallbackInfo\x12C\n\x11geocoding_results\x18\x03 \x01(\x0b2(.google.maps.routing.v2.GeocodingResults"\xc6\x06\n\x19ComputeRouteMatrixRequest\x12?\n\x07origins\x18\x01 \x03(\x0b2).google.maps.routing.v2.RouteMatrixOriginB\x03\xe0A\x02\x12I\n\x0cdestinations\x18\x02 \x03(\x0b2..google.maps.routing.v2.RouteMatrixDestinationB\x03\xe0A\x02\x12A\n\x0btravel_mode\x18\x03 \x01(\x0e2\'.google.maps.routing.v2.RouteTravelModeB\x03\xe0A\x01\x12J\n\x12routing_preference\x18\x04 \x01(\x0e2).google.maps.routing.v2.RoutingPreferenceB\x03\xe0A\x01\x127\n\x0edeparture_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x125\n\x0carrival_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bregion_code\x18\t \x01(\tB\x03\xe0A\x01\x121\n\x05units\x18\x07 \x01(\x0e2\x1d.google.maps.routing.v2.UnitsB\x03\xe0A\x01\x12c\n\x12extra_computations\x18\x08 \x03(\x0e2B.google.maps.routing.v2.ComputeRouteMatrixRequest.ExtraComputationB\x03\xe0A\x01\x12@\n\rtraffic_model\x18\n \x01(\x0e2$.google.maps.routing.v2.TrafficModelB\x03\xe0A\x01\x12L\n\x13transit_preferences\x18\x0c \x01(\x0b2*.google.maps.routing.v2.TransitPreferencesB\x03\xe0A\x01"@\n\x10ExtraComputation\x12!\n\x1dEXTRA_COMPUTATION_UNSPECIFIED\x10\x00\x12\t\n\x05TOLLS\x10\x01"\x92\x01\n\x11RouteMatrixOrigin\x127\n\x08waypoint\x18\x01 \x01(\x0b2 .google.maps.routing.v2.WaypointB\x03\xe0A\x02\x12D\n\x0froute_modifiers\x18\x02 \x01(\x0b2&.google.maps.routing.v2.RouteModifiersB\x03\xe0A\x01"Q\n\x16RouteMatrixDestination\x127\n\x08waypoint\x18\x01 \x01(\x0b2 .google.maps.routing.v2.WaypointB\x03\xe0A\x02"\x8c\x06\n\x12RouteMatrixElement\x12\x19\n\x0corigin_index\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x1e\n\x11destination_index\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12"\n\x06status\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12F\n\tcondition\x18\t \x01(\x0e23.google.maps.routing.v2.RouteMatrixElementCondition\x12\x17\n\x0fdistance_meters\x18\x04 \x01(\x05\x12+\n\x08duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fstatic_duration\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12D\n\x0ftravel_advisory\x18\x07 \x01(\x0b2+.google.maps.routing.v2.RouteTravelAdvisory\x12;\n\rfallback_info\x18\x08 \x01(\x0b2$.google.maps.routing.v2.FallbackInfo\x12T\n\x10localized_values\x18\n \x01(\x0b2:.google.maps.routing.v2.RouteMatrixElement.LocalizedValues\x1a\xd4\x01\n\x0fLocalizedValues\x12,\n\x08distance\x18\x01 \x01(\x0b2\x1a.google.type.LocalizedText\x12,\n\x08duration\x18\x02 \x01(\x0b2\x1a.google.type.LocalizedText\x123\n\x0fstatic_duration\x18\x03 \x01(\x0b2\x1a.google.type.LocalizedText\x120\n\x0ctransit_fare\x18\x04 \x01(\x0b2\x1a.google.type.LocalizedTextB\x0f\n\r_origin_indexB\x14\n\x12_destination_index*t\n\x1bRouteMatrixElementCondition\x12.\n*ROUTE_MATRIX_ELEMENT_CONDITION_UNSPECIFIED\x10\x00\x12\x10\n\x0cROUTE_EXISTS\x10\x01\x12\x13\n\x0fROUTE_NOT_FOUND\x10\x022\xe4\x02\n\x06Routes\x12\x95\x01\n\rComputeRoutes\x12,.google.maps.routing.v2.ComputeRoutesRequest\x1a-.google.maps.routing.v2.ComputeRoutesResponse"\'\x82\xd3\xe4\x93\x02!"\x1c/directions/v2:computeRoutes:\x01*\x12\xa7\x01\n\x12ComputeRouteMatrix\x121.google.maps.routing.v2.ComputeRouteMatrixRequest\x1a*.google.maps.routing.v2.RouteMatrixElement"0\x82\xd3\xe4\x93\x02*"%/distanceMatrix/v2:computeRouteMatrix:\x01*0\x01\x1a\x18\xcaA\x15routes.googleapis.comB\xc4\x01\n\x1acom.google.maps.routing.v2B\x12RoutesServiceProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.routes_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\x12RoutesServiceProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['origin']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['origin']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['destination']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['destination']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['intermediates']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['intermediates']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['travel_mode']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['travel_mode']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['routing_preference']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['routing_preference']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['polyline_quality']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['polyline_quality']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['polyline_encoding']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['polyline_encoding']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['departure_time']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['departure_time']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['arrival_time']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['arrival_time']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['compute_alternative_routes']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['compute_alternative_routes']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['route_modifiers']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['route_modifiers']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['region_code']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['region_code']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['units']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['units']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['optimize_waypoint_order']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['optimize_waypoint_order']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['requested_reference_routes']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['requested_reference_routes']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['extra_computations']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['extra_computations']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['traffic_model']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['traffic_model']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['transit_preferences']._loaded_options = None
    _globals['_COMPUTEROUTESREQUEST'].fields_by_name['transit_preferences']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['origins']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['origins']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['destinations']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['destinations']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['travel_mode']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['travel_mode']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['routing_preference']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['routing_preference']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['departure_time']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['departure_time']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['arrival_time']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['arrival_time']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['region_code']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['region_code']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['units']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['units']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['extra_computations']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['extra_computations']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['traffic_model']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['traffic_model']._serialized_options = b'\xe0A\x01'
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['transit_preferences']._loaded_options = None
    _globals['_COMPUTEROUTEMATRIXREQUEST'].fields_by_name['transit_preferences']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTEMATRIXORIGIN'].fields_by_name['waypoint']._loaded_options = None
    _globals['_ROUTEMATRIXORIGIN'].fields_by_name['waypoint']._serialized_options = b'\xe0A\x02'
    _globals['_ROUTEMATRIXORIGIN'].fields_by_name['route_modifiers']._loaded_options = None
    _globals['_ROUTEMATRIXORIGIN'].fields_by_name['route_modifiers']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTEMATRIXDESTINATION'].fields_by_name['waypoint']._loaded_options = None
    _globals['_ROUTEMATRIXDESTINATION'].fields_by_name['waypoint']._serialized_options = b'\xe0A\x02'
    _globals['_ROUTES']._loaded_options = None
    _globals['_ROUTES']._serialized_options = b'\xcaA\x15routes.googleapis.com'
    _globals['_ROUTES'].methods_by_name['ComputeRoutes']._loaded_options = None
    _globals['_ROUTES'].methods_by_name['ComputeRoutes']._serialized_options = b'\x82\xd3\xe4\x93\x02!"\x1c/directions/v2:computeRoutes:\x01*'
    _globals['_ROUTES'].methods_by_name['ComputeRouteMatrix']._loaded_options = None
    _globals['_ROUTES'].methods_by_name['ComputeRouteMatrix']._serialized_options = b'\x82\xd3\xe4\x93\x02*"%/distanceMatrix/v2:computeRouteMatrix:\x01*'
    _globals['_ROUTEMATRIXELEMENTCONDITION']._serialized_start = 4335
    _globals['_ROUTEMATRIXELEMENTCONDITION']._serialized_end = 4451
    _globals['_COMPUTEROUTESREQUEST']._serialized_start = 763
    _globals['_COMPUTEROUTESREQUEST']._serialized_end = 2274
    _globals['_COMPUTEROUTESREQUEST_REFERENCEROUTE']._serialized_start = 1961
    _globals['_COMPUTEROUTESREQUEST_REFERENCEROUTE']._serialized_end = 2052
    _globals['_COMPUTEROUTESREQUEST_EXTRACOMPUTATION']._serialized_start = 2055
    _globals['_COMPUTEROUTESREQUEST_EXTRACOMPUTATION']._serialized_end = 2274
    _globals['_COMPUTEROUTESRESPONSE']._serialized_start = 2277
    _globals['_COMPUTEROUTESRESPONSE']._serialized_end = 2477
    _globals['_COMPUTEROUTEMATRIXREQUEST']._serialized_start = 2480
    _globals['_COMPUTEROUTEMATRIXREQUEST']._serialized_end = 3318
    _globals['_COMPUTEROUTEMATRIXREQUEST_EXTRACOMPUTATION']._serialized_start = 2055
    _globals['_COMPUTEROUTEMATRIXREQUEST_EXTRACOMPUTATION']._serialized_end = 2119
    _globals['_ROUTEMATRIXORIGIN']._serialized_start = 3321
    _globals['_ROUTEMATRIXORIGIN']._serialized_end = 3467
    _globals['_ROUTEMATRIXDESTINATION']._serialized_start = 3469
    _globals['_ROUTEMATRIXDESTINATION']._serialized_end = 3550
    _globals['_ROUTEMATRIXELEMENT']._serialized_start = 3553
    _globals['_ROUTEMATRIXELEMENT']._serialized_end = 4333
    _globals['_ROUTEMATRIXELEMENT_LOCALIZEDVALUES']._serialized_start = 4082
    _globals['_ROUTEMATRIXELEMENT_LOCALIZEDVALUES']._serialized_end = 4294
    _globals['_ROUTES']._serialized_start = 4454
    _globals['_ROUTES']._serialized_end = 4810