"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/routing/v2/route.proto')
_sym_db = _symbol_database.Default()
from .....google.geo.type import viewport_pb2 as google_dot_geo_dot_type_dot_viewport__pb2
from .....google.maps.routing.v2 import localized_time_pb2 as google_dot_maps_dot_routing_dot_v2_dot_localized__time__pb2
from .....google.maps.routing.v2 import location_pb2 as google_dot_maps_dot_routing_dot_v2_dot_location__pb2
from .....google.maps.routing.v2 import navigation_instruction_pb2 as google_dot_maps_dot_routing_dot_v2_dot_navigation__instruction__pb2
from .....google.maps.routing.v2 import polyline_pb2 as google_dot_maps_dot_routing_dot_v2_dot_polyline__pb2
from .....google.maps.routing.v2 import polyline_details_pb2 as google_dot_maps_dot_routing_dot_v2_dot_polyline__details__pb2
from .....google.maps.routing.v2 import route_label_pb2 as google_dot_maps_dot_routing_dot_v2_dot_route__label__pb2
from .....google.maps.routing.v2 import route_travel_mode_pb2 as google_dot_maps_dot_routing_dot_v2_dot_route__travel__mode__pb2
from .....google.maps.routing.v2 import speed_reading_interval_pb2 as google_dot_maps_dot_routing_dot_v2_dot_speed__reading__interval__pb2
from .....google.maps.routing.v2 import toll_info_pb2 as google_dot_maps_dot_routing_dot_v2_dot_toll__info__pb2
from .....google.maps.routing.v2 import transit_pb2 as google_dot_maps_dot_routing_dot_v2_dot_transit__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import localized_text_pb2 as google_dot_type_dot_localized__text__pb2
from .....google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/maps/routing/v2/route.proto\x12\x16google.maps.routing.v2\x1a\x1egoogle/geo/type/viewport.proto\x1a+google/maps/routing/v2/localized_time.proto\x1a%google/maps/routing/v2/location.proto\x1a3google/maps/routing/v2/navigation_instruction.proto\x1a%google/maps/routing/v2/polyline.proto\x1a-google/maps/routing/v2/polyline_details.proto\x1a(google/maps/routing/v2/route_label.proto\x1a.google/maps/routing/v2/route_travel_mode.proto\x1a3google/maps/routing/v2/speed_reading_interval.proto\x1a&google/maps/routing/v2/toll_info.proto\x1a$google/maps/routing/v2/transit.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/type/localized_text.proto\x1a\x17google/type/money.proto"\xea\x06\n\x05Route\x128\n\x0croute_labels\x18\r \x03(\x0e2".google.maps.routing.v2.RouteLabel\x12.\n\x04legs\x18\x01 \x03(\x0b2 .google.maps.routing.v2.RouteLeg\x12\x17\n\x0fdistance_meters\x18\x02 \x01(\x05\x12+\n\x08duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fstatic_duration\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x08polyline\x18\x05 \x01(\x0b2 .google.maps.routing.v2.Polyline\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12\x10\n\x08warnings\x18\x07 \x03(\t\x12+\n\x08viewport\x18\x08 \x01(\x0b2\x19.google.geo.type.Viewport\x12D\n\x0ftravel_advisory\x18\t \x01(\x0b2+.google.maps.routing.v2.RouteTravelAdvisory\x12-\n%optimized_intermediate_waypoint_index\x18\n \x03(\x05\x12L\n\x10localized_values\x18\x0b \x01(\x0b22.google.maps.routing.v2.Route.RouteLocalizedValues\x12\x13\n\x0broute_token\x18\x0c \x01(\t\x12A\n\x10polyline_details\x18\x0e \x01(\x0b2\'.google.maps.routing.v2.PolylineDetails\x1a\xd9\x01\n\x14RouteLocalizedValues\x12,\n\x08distance\x18\x01 \x01(\x0b2\x1a.google.type.LocalizedText\x12,\n\x08duration\x18\x02 \x01(\x0b2\x1a.google.type.LocalizedText\x123\n\x0fstatic_duration\x18\x03 \x01(\x0b2\x1a.google.type.LocalizedText\x120\n\x0ctransit_fare\x18\x04 \x01(\x0b2\x1a.google.type.LocalizedText"\x97\x02\n\x13RouteTravelAdvisory\x123\n\ttoll_info\x18\x02 \x01(\x0b2 .google.maps.routing.v2.TollInfo\x12M\n\x17speed_reading_intervals\x18\x03 \x03(\x0b2,.google.maps.routing.v2.SpeedReadingInterval\x12$\n\x1cfuel_consumption_microliters\x18\x05 \x01(\x03\x12,\n$route_restrictions_partially_ignored\x18\x06 \x01(\x08\x12(\n\x0ctransit_fare\x18\x07 \x01(\x0b2\x12.google.type.Money"\x9c\x01\n\x16RouteLegTravelAdvisory\x123\n\ttoll_info\x18\x01 \x01(\x0b2 .google.maps.routing.v2.TollInfo\x12M\n\x17speed_reading_intervals\x18\x02 \x03(\x0b2,.google.maps.routing.v2.SpeedReadingInterval"k\n\x1aRouteLegStepTravelAdvisory\x12M\n\x17speed_reading_intervals\x18\x01 \x03(\x0b2,.google.maps.routing.v2.SpeedReadingInterval"\xea\x08\n\x08RouteLeg\x12\x17\n\x0fdistance_meters\x18\x01 \x01(\x05\x12+\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x0fstatic_duration\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x08polyline\x18\x04 \x01(\x0b2 .google.maps.routing.v2.Polyline\x128\n\x0estart_location\x18\x05 \x01(\x0b2 .google.maps.routing.v2.Location\x126\n\x0cend_location\x18\x06 \x01(\x0b2 .google.maps.routing.v2.Location\x123\n\x05steps\x18\x07 \x03(\x0b2$.google.maps.routing.v2.RouteLegStep\x12G\n\x0ftravel_advisory\x18\x08 \x01(\x0b2..google.maps.routing.v2.RouteLegTravelAdvisory\x12R\n\x10localized_values\x18\t \x01(\x0b28.google.maps.routing.v2.RouteLeg.RouteLegLocalizedValues\x12F\n\x0esteps_overview\x18\n \x01(\x0b2..google.maps.routing.v2.RouteLeg.StepsOverview\x1a\xaa\x01\n\x17RouteLegLocalizedValues\x12,\n\x08distance\x18\x01 \x01(\x0b2\x1a.google.type.LocalizedText\x12,\n\x08duration\x18\x02 \x01(\x0b2\x1a.google.type.LocalizedText\x123\n\x0fstatic_duration\x18\x03 \x01(\x0b2\x1a.google.type.LocalizedText\x1a\xf6\x02\n\rStepsOverview\x12^\n\x14multi_modal_segments\x18\x01 \x03(\x0b2@.google.maps.routing.v2.RouteLeg.StepsOverview.MultiModalSegment\x1a\x84\x02\n\x11MultiModalSegment\x12\x1d\n\x10step_start_index\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x1b\n\x0estep_end_index\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12M\n\x16navigation_instruction\x18\x03 \x01(\x0b2-.google.maps.routing.v2.NavigationInstruction\x12<\n\x0btravel_mode\x18\x04 \x01(\x0e2\'.google.maps.routing.v2.RouteTravelModeB\x13\n\x11_step_start_indexB\x11\n\x0f_step_end_index"\x87\x06\n\x0cRouteLegStep\x12\x17\n\x0fdistance_meters\x18\x01 \x01(\x05\x122\n\x0fstatic_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x122\n\x08polyline\x18\x03 \x01(\x0b2 .google.maps.routing.v2.Polyline\x128\n\x0estart_location\x18\x04 \x01(\x0b2 .google.maps.routing.v2.Location\x126\n\x0cend_location\x18\x05 \x01(\x0b2 .google.maps.routing.v2.Location\x12M\n\x16navigation_instruction\x18\x06 \x01(\x0b2-.google.maps.routing.v2.NavigationInstruction\x12K\n\x0ftravel_advisory\x18\x07 \x01(\x0b22.google.maps.routing.v2.RouteLegStepTravelAdvisory\x12Z\n\x10localized_values\x18\x08 \x01(\x0b2@.google.maps.routing.v2.RouteLegStep.RouteLegStepLocalizedValues\x12K\n\x0ftransit_details\x18\t \x01(\x0b22.google.maps.routing.v2.RouteLegStepTransitDetails\x12<\n\x0btravel_mode\x18\n \x01(\x0e2\'.google.maps.routing.v2.RouteTravelMode\x1a\x80\x01\n\x1bRouteLegStepLocalizedValues\x12,\n\x08distance\x18\x01 \x01(\x0b2\x1a.google.type.LocalizedText\x123\n\x0fstatic_duration\x18\x03 \x01(\x0b2\x1a.google.type.LocalizedText"\x9e\x06\n\x1aRouteLegStepTransitDetails\x12[\n\x0cstop_details\x18\x01 \x01(\x0b2E.google.maps.routing.v2.RouteLegStepTransitDetails.TransitStopDetails\x12j\n\x10localized_values\x18\x02 \x01(\x0b2P.google.maps.routing.v2.RouteLegStepTransitDetails.TransitDetailsLocalizedValues\x12\x10\n\x08headsign\x18\x03 \x01(\t\x12*\n\x07headway\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x129\n\x0ctransit_line\x18\x05 \x01(\x0b2#.google.maps.routing.v2.TransitLine\x12\x12\n\nstop_count\x18\x06 \x01(\x05\x12\x17\n\x0ftrip_short_text\x18\x07 \x01(\t\x1a\xf2\x01\n\x12TransitStopDetails\x129\n\x0carrival_stop\x18\x01 \x01(\x0b2#.google.maps.routing.v2.TransitStop\x120\n\x0carrival_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12;\n\x0edeparture_stop\x18\x03 \x01(\x0b2#.google.maps.routing.v2.TransitStop\x122\n\x0edeparture_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x9b\x01\n\x1dTransitDetailsLocalizedValues\x12;\n\x0carrival_time\x18\x01 \x01(\x0b2%.google.maps.routing.v2.LocalizedTime\x12=\n\x0edeparture_time\x18\x02 \x01(\x0b2%.google.maps.routing.v2.LocalizedTimeB\xbc\x01\n\x1acom.google.maps.routing.v2B\nRouteProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.routing.v2.route_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.routing.v2B\nRouteProtoP\x01Z:cloud.google.com/go/maps/routing/apiv2/routingpb;routingpb\xa2\x02\x05GMRV2\xaa\x02\x16Google.Maps.Routing.V2\xca\x02\x16Google\\Maps\\Routing\\V2\xea\x02\x19Google::Maps::Routing::V2'
    _globals['_ROUTE']._serialized_start = 663
    _globals['_ROUTE']._serialized_end = 1537
    _globals['_ROUTE_ROUTELOCALIZEDVALUES']._serialized_start = 1320
    _globals['_ROUTE_ROUTELOCALIZEDVALUES']._serialized_end = 1537
    _globals['_ROUTETRAVELADVISORY']._serialized_start = 1540
    _globals['_ROUTETRAVELADVISORY']._serialized_end = 1819
    _globals['_ROUTELEGTRAVELADVISORY']._serialized_start = 1822
    _globals['_ROUTELEGTRAVELADVISORY']._serialized_end = 1978
    _globals['_ROUTELEGSTEPTRAVELADVISORY']._serialized_start = 1980
    _globals['_ROUTELEGSTEPTRAVELADVISORY']._serialized_end = 2087
    _globals['_ROUTELEG']._serialized_start = 2090
    _globals['_ROUTELEG']._serialized_end = 3220
    _globals['_ROUTELEG_ROUTELEGLOCALIZEDVALUES']._serialized_start = 2673
    _globals['_ROUTELEG_ROUTELEGLOCALIZEDVALUES']._serialized_end = 2843
    _globals['_ROUTELEG_STEPSOVERVIEW']._serialized_start = 2846
    _globals['_ROUTELEG_STEPSOVERVIEW']._serialized_end = 3220
    _globals['_ROUTELEG_STEPSOVERVIEW_MULTIMODALSEGMENT']._serialized_start = 2960
    _globals['_ROUTELEG_STEPSOVERVIEW_MULTIMODALSEGMENT']._serialized_end = 3220
    _globals['_ROUTELEGSTEP']._serialized_start = 3223
    _globals['_ROUTELEGSTEP']._serialized_end = 3998
    _globals['_ROUTELEGSTEP_ROUTELEGSTEPLOCALIZEDVALUES']._serialized_start = 3870
    _globals['_ROUTELEGSTEP_ROUTELEGSTEPLOCALIZEDVALUES']._serialized_end = 3998
    _globals['_ROUTELEGSTEPTRANSITDETAILS']._serialized_start = 4001
    _globals['_ROUTELEGSTEPTRANSITDETAILS']._serialized_end = 4799
    _globals['_ROUTELEGSTEPTRANSITDETAILS_TRANSITSTOPDETAILS']._serialized_start = 4399
    _globals['_ROUTELEGSTEPTRANSITDETAILS_TRANSITSTOPDETAILS']._serialized_end = 4641
    _globals['_ROUTELEGSTEPTRANSITDETAILS_TRANSITDETAILSLOCALIZEDVALUES']._serialized_start = 4644
    _globals['_ROUTELEGSTEPTRANSITDETAILS_TRANSITDETAILSLOCALIZEDVALUES']._serialized_end = 4799