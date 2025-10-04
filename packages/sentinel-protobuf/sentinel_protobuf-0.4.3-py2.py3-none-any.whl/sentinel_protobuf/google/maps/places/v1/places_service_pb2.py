"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/places/v1/places_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.geo.type import viewport_pb2 as google_dot_geo_dot_type_dot_viewport__pb2
from .....google.maps.places.v1 import contextual_content_pb2 as google_dot_maps_dot_places_dot_v1_dot_contextual__content__pb2
from .....google.maps.places.v1 import ev_charging_pb2 as google_dot_maps_dot_places_dot_v1_dot_ev__charging__pb2
from .....google.maps.places.v1 import geometry_pb2 as google_dot_maps_dot_places_dot_v1_dot_geometry__pb2
from .....google.maps.places.v1 import place_pb2 as google_dot_maps_dot_places_dot_v1_dot_place__pb2
from .....google.maps.places.v1 import polyline_pb2 as google_dot_maps_dot_places_dot_v1_dot_polyline__pb2
from .....google.maps.places.v1 import route_modifiers_pb2 as google_dot_maps_dot_places_dot_v1_dot_route__modifiers__pb2
from .....google.maps.places.v1 import routing_preference_pb2 as google_dot_maps_dot_places_dot_v1_dot_routing__preference__pb2
from .....google.maps.places.v1 import routing_summary_pb2 as google_dot_maps_dot_places_dot_v1_dot_routing__summary__pb2
from .....google.maps.places.v1 import travel_mode_pb2 as google_dot_maps_dot_places_dot_v1_dot_travel__mode__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/maps/places/v1/places_service.proto\x12\x15google.maps.places.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/geo/type/viewport.proto\x1a.google/maps/places/v1/contextual_content.proto\x1a\'google/maps/places/v1/ev_charging.proto\x1a$google/maps/places/v1/geometry.proto\x1a!google/maps/places/v1/place.proto\x1a$google/maps/places/v1/polyline.proto\x1a+google/maps/places/v1/route_modifiers.proto\x1a.google/maps/places/v1/routing_preference.proto\x1a+google/maps/places/v1/routing_summary.proto\x1a\'google/maps/places/v1/travel_mode.proto\x1a\x18google/type/latlng.proto"\x8a\x02\n\x11RoutingParameters\x12(\n\x06origin\x18\x01 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x01\x12;\n\x0btravel_mode\x18\x02 \x01(\x0e2!.google.maps.places.v1.TravelModeB\x03\xe0A\x01\x12C\n\x0froute_modifiers\x18\x03 \x01(\x0b2%.google.maps.places.v1.RouteModifiersB\x03\xe0A\x01\x12I\n\x12routing_preference\x18\x04 \x01(\x0e2(.google.maps.places.v1.RoutingPreferenceB\x03\xe0A\x01"\xee\x04\n\x13SearchNearbyRequest\x12\x15\n\rlanguage_code\x18\x01 \x01(\t\x12\x13\n\x0bregion_code\x18\x02 \x01(\t\x12\x16\n\x0eincluded_types\x18\x03 \x03(\t\x12\x16\n\x0eexcluded_types\x18\x04 \x03(\t\x12\x1e\n\x16included_primary_types\x18\x05 \x03(\t\x12\x1e\n\x16excluded_primary_types\x18\x06 \x03(\t\x12\x18\n\x10max_result_count\x18\x07 \x01(\x05\x12a\n\x14location_restriction\x18\x08 \x01(\x0b2>.google.maps.places.v1.SearchNearbyRequest.LocationRestrictionB\x03\xe0A\x02\x12R\n\x0frank_preference\x18\t \x01(\x0e29.google.maps.places.v1.SearchNearbyRequest.RankPreference\x12I\n\x12routing_parameters\x18\n \x01(\x0b2(.google.maps.places.v1.RoutingParametersB\x03\xe0A\x01\x1aN\n\x13LocationRestriction\x12/\n\x06circle\x18\x02 \x01(\x0b2\x1d.google.maps.places.v1.CircleH\x00B\x06\n\x04type"O\n\x0eRankPreference\x12\x1f\n\x1bRANK_PREFERENCE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DISTANCE\x10\x01\x12\x0e\n\nPOPULARITY\x10\x02"\x86\x01\n\x14SearchNearbyResponse\x12,\n\x06places\x18\x01 \x03(\x0b2\x1c.google.maps.places.v1.Place\x12@\n\x11routing_summaries\x18\x02 \x03(\x0b2%.google.maps.places.v1.RoutingSummary"\xa7\n\n\x11SearchTextRequest\x12\x17\n\ntext_query\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x13\n\x0bregion_code\x18\x03 \x01(\t\x12P\n\x0frank_preference\x18\x04 \x01(\x0e27.google.maps.places.v1.SearchTextRequest.RankPreference\x12\x15\n\rincluded_type\x18\x06 \x01(\t\x12\x10\n\x08open_now\x18\x07 \x01(\x08\x12\x12\n\nmin_rating\x18\t \x01(\x01\x12\x18\n\x10max_result_count\x18\n \x01(\x05\x127\n\x0cprice_levels\x18\x0b \x03(\x0e2!.google.maps.places.v1.PriceLevel\x12\x1d\n\x15strict_type_filtering\x18\x0c \x01(\x08\x12L\n\rlocation_bias\x18\r \x01(\x0b25.google.maps.places.v1.SearchTextRequest.LocationBias\x12Z\n\x14location_restriction\x18\x0e \x01(\x0b2<.google.maps.places.v1.SearchTextRequest.LocationRestriction\x12K\n\nev_options\x18\x0f \x01(\x0b22.google.maps.places.v1.SearchTextRequest.EVOptionsB\x03\xe0A\x01\x12I\n\x12routing_parameters\x18\x10 \x01(\x0b2(.google.maps.places.v1.RoutingParametersB\x03\xe0A\x01\x12o\n\x1dsearch_along_route_parameters\x18\x11 \x01(\x0b2C.google.maps.places.v1.SearchTextRequest.SearchAlongRouteParametersB\x03\xe0A\x01\x121\n$include_pure_service_area_businesses\x18\x14 \x01(\x08B\x03\xe0A\x01\x1aw\n\x0cLocationBias\x12.\n\trectangle\x18\x01 \x01(\x0b2\x19.google.geo.type.ViewportH\x00\x12/\n\x06circle\x18\x02 \x01(\x0b2\x1d.google.maps.places.v1.CircleH\x00B\x06\n\x04type\x1aM\n\x13LocationRestriction\x12.\n\trectangle\x18\x01 \x01(\x0b2\x19.google.geo.type.ViewportH\x00B\x06\n\x04type\x1ax\n\tEVOptions\x12%\n\x18minimum_charging_rate_kw\x18\x01 \x01(\x01B\x03\xe0A\x01\x12D\n\x0fconnector_types\x18\x02 \x03(\x0e2&.google.maps.places.v1.EVConnectorTypeB\x03\xe0A\x01\x1aT\n\x1aSearchAlongRouteParameters\x126\n\x08polyline\x18\x01 \x01(\x0b2\x1f.google.maps.places.v1.PolylineB\x03\xe0A\x02"N\n\x0eRankPreference\x12\x1f\n\x1bRANK_PREFERENCE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DISTANCE\x10\x01\x12\r\n\tRELEVANCE\x10\x02"\xcb\x01\n\x12SearchTextResponse\x12,\n\x06places\x18\x01 \x03(\x0b2\x1c.google.maps.places.v1.Place\x12@\n\x11routing_summaries\x18\x02 \x03(\x0b2%.google.maps.places.v1.RoutingSummary\x12E\n\x13contextual_contents\x18\x03 \x03(\x0b2(.google.maps.places.v1.ContextualContent"\xa6\x01\n\x14GetPhotoMediaRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n places.googleapis.com/PhotoMedia\x12\x19\n\x0cmax_width_px\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x1a\n\rmax_height_px\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x1f\n\x12skip_http_redirect\x18\x04 \x01(\x08B\x03\xe0A\x01"\x9f\x01\n\nPhotoMedia\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tphoto_uri\x18\x02 \x01(\t:p\xeaAm\n places.googleapis.com/PhotoMedia\x120places/{place_id}/photos/{photo_reference}/media*\x0bphotoMedias2\nphotoMedia"\x96\x01\n\x0fGetPlaceRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bplaces.googleapis.com/Place\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bregion_code\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rsession_token\x18\x04 \x01(\tB\x03\xe0A\x01"\xa7\x06\n\x19AutocompletePlacesRequest\x12\x12\n\x05input\x18\x01 \x01(\tB\x03\xe0A\x02\x12Y\n\rlocation_bias\x18\x02 \x01(\x0b2=.google.maps.places.v1.AutocompletePlacesRequest.LocationBiasB\x03\xe0A\x01\x12g\n\x14location_restriction\x18\x03 \x01(\x0b2D.google.maps.places.v1.AutocompletePlacesRequest.LocationRestrictionB\x03\xe0A\x01\x12#\n\x16included_primary_types\x18\x04 \x03(\tB\x03\xe0A\x01\x12"\n\x15included_region_codes\x18\x05 \x03(\tB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bregion_code\x18\x07 \x01(\tB\x03\xe0A\x01\x12(\n\x06origin\x18\x08 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x01\x12\x19\n\x0cinput_offset\x18\t \x01(\x05B\x03\xe0A\x01\x12&\n\x19include_query_predictions\x18\n \x01(\x08B\x03\xe0A\x01\x12\x1a\n\rsession_token\x18\x0b \x01(\tB\x03\xe0A\x01\x121\n$include_pure_service_area_businesses\x18\x0c \x01(\x08B\x03\xe0A\x01\x1aw\n\x0cLocationBias\x12.\n\trectangle\x18\x01 \x01(\x0b2\x19.google.geo.type.ViewportH\x00\x12/\n\x06circle\x18\x02 \x01(\x0b2\x1d.google.maps.places.v1.CircleH\x00B\x06\n\x04type\x1a~\n\x13LocationRestriction\x12.\n\trectangle\x18\x01 \x01(\x0b2\x19.google.geo.type.ViewportH\x00\x12/\n\x06circle\x18\x02 \x01(\x0b2\x1d.google.maps.places.v1.CircleH\x00B\x06\n\x04type"\x8a\n\n\x1aAutocompletePlacesResponse\x12Q\n\x0bsuggestions\x18\x01 \x03(\x0b2<.google.maps.places.v1.AutocompletePlacesResponse.Suggestion\x1a\x98\t\n\nSuggestion\x12h\n\x10place_prediction\x18\x01 \x01(\x0b2L.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.PlacePredictionH\x00\x12h\n\x10query_prediction\x18\x02 \x01(\x0b2L.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.QueryPredictionH\x00\x1a7\n\x0bStringRange\x12\x14\n\x0cstart_offset\x18\x01 \x01(\x05\x12\x12\n\nend_offset\x18\x02 \x01(\x05\x1az\n\x0fFormattableText\x12\x0c\n\x04text\x18\x01 \x01(\t\x12Y\n\x07matches\x18\x02 \x03(\x0b2H.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.StringRange\x1a\xd9\x01\n\x10StructuredFormat\x12_\n\tmain_text\x18\x01 \x01(\x0b2L.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.FormattableText\x12d\n\x0esecondary_text\x18\x02 \x01(\x0b2L.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.FormattableText\x1a\xc2\x02\n\x0fPlacePrediction\x12/\n\x05place\x18\x01 \x01(\tB \xfaA\x1d\n\x1bplaces.googleapis.com/Place\x12\x10\n\x08place_id\x18\x02 \x01(\t\x12Z\n\x04text\x18\x03 \x01(\x0b2L.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.FormattableText\x12h\n\x11structured_format\x18\x04 \x01(\x0b2M.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.StructuredFormat\x12\r\n\x05types\x18\x05 \x03(\t\x12\x17\n\x0fdistance_meters\x18\x06 \x01(\x05\x1a\xd7\x01\n\x0fQueryPrediction\x12Z\n\x04text\x18\x01 \x01(\x0b2L.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.FormattableText\x12h\n\x11structured_format\x18\x02 \x01(\x0b2M.google.maps.places.v1.AutocompletePlacesResponse.Suggestion.StructuredFormatB\x06\n\x04kind2\x92\x06\n\x06Places\x12\x8b\x01\n\x0cSearchNearby\x12*.google.maps.places.v1.SearchNearbyRequest\x1a+.google.maps.places.v1.SearchNearbyResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/v1/places:searchNearby:\x01*\x12\x83\x01\n\nSearchText\x12(.google.maps.places.v1.SearchTextRequest\x1a).google.maps.places.v1.SearchTextResponse" \x82\xd3\xe4\x93\x02\x1a"\x15/v1/places:searchText:\x01*\x12\x92\x01\n\rGetPhotoMedia\x12+.google.maps.places.v1.GetPhotoMediaRequest\x1a!.google.maps.places.v1.PhotoMedia"1\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v1/{name=places/*/photos/*/media}\x12t\n\x08GetPlace\x12&.google.maps.places.v1.GetPlaceRequest\x1a\x1c.google.maps.places.v1.Place""\xdaA\x04name\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/{name=places/*}\x12\x9d\x01\n\x12AutocompletePlaces\x120.google.maps.places.v1.AutocompletePlacesRequest\x1a1.google.maps.places.v1.AutocompletePlacesResponse""\x82\xd3\xe4\x93\x02\x1c"\x17/v1/places:autocomplete:\x01*\x1aI\xcaA\x15places.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa3\x01\n\x19com.google.maps.places.v1B\x12PlacesServiceProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.places.v1.places_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.places.v1B\x12PlacesServiceProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1'
    _globals['_ROUTINGPARAMETERS'].fields_by_name['origin']._loaded_options = None
    _globals['_ROUTINGPARAMETERS'].fields_by_name['origin']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINGPARAMETERS'].fields_by_name['travel_mode']._loaded_options = None
    _globals['_ROUTINGPARAMETERS'].fields_by_name['travel_mode']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINGPARAMETERS'].fields_by_name['route_modifiers']._loaded_options = None
    _globals['_ROUTINGPARAMETERS'].fields_by_name['route_modifiers']._serialized_options = b'\xe0A\x01'
    _globals['_ROUTINGPARAMETERS'].fields_by_name['routing_preference']._loaded_options = None
    _globals['_ROUTINGPARAMETERS'].fields_by_name['routing_preference']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHNEARBYREQUEST'].fields_by_name['location_restriction']._loaded_options = None
    _globals['_SEARCHNEARBYREQUEST'].fields_by_name['location_restriction']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHNEARBYREQUEST'].fields_by_name['routing_parameters']._loaded_options = None
    _globals['_SEARCHNEARBYREQUEST'].fields_by_name['routing_parameters']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHTEXTREQUEST_EVOPTIONS'].fields_by_name['minimum_charging_rate_kw']._loaded_options = None
    _globals['_SEARCHTEXTREQUEST_EVOPTIONS'].fields_by_name['minimum_charging_rate_kw']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHTEXTREQUEST_EVOPTIONS'].fields_by_name['connector_types']._loaded_options = None
    _globals['_SEARCHTEXTREQUEST_EVOPTIONS'].fields_by_name['connector_types']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHTEXTREQUEST_SEARCHALONGROUTEPARAMETERS'].fields_by_name['polyline']._loaded_options = None
    _globals['_SEARCHTEXTREQUEST_SEARCHALONGROUTEPARAMETERS'].fields_by_name['polyline']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHTEXTREQUEST'].fields_by_name['text_query']._loaded_options = None
    _globals['_SEARCHTEXTREQUEST'].fields_by_name['text_query']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHTEXTREQUEST'].fields_by_name['ev_options']._loaded_options = None
    _globals['_SEARCHTEXTREQUEST'].fields_by_name['ev_options']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHTEXTREQUEST'].fields_by_name['routing_parameters']._loaded_options = None
    _globals['_SEARCHTEXTREQUEST'].fields_by_name['routing_parameters']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHTEXTREQUEST'].fields_by_name['search_along_route_parameters']._loaded_options = None
    _globals['_SEARCHTEXTREQUEST'].fields_by_name['search_along_route_parameters']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHTEXTREQUEST'].fields_by_name['include_pure_service_area_businesses']._loaded_options = None
    _globals['_SEARCHTEXTREQUEST'].fields_by_name['include_pure_service_area_businesses']._serialized_options = b'\xe0A\x01'
    _globals['_GETPHOTOMEDIAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPHOTOMEDIAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n places.googleapis.com/PhotoMedia'
    _globals['_GETPHOTOMEDIAREQUEST'].fields_by_name['max_width_px']._loaded_options = None
    _globals['_GETPHOTOMEDIAREQUEST'].fields_by_name['max_width_px']._serialized_options = b'\xe0A\x01'
    _globals['_GETPHOTOMEDIAREQUEST'].fields_by_name['max_height_px']._loaded_options = None
    _globals['_GETPHOTOMEDIAREQUEST'].fields_by_name['max_height_px']._serialized_options = b'\xe0A\x01'
    _globals['_GETPHOTOMEDIAREQUEST'].fields_by_name['skip_http_redirect']._loaded_options = None
    _globals['_GETPHOTOMEDIAREQUEST'].fields_by_name['skip_http_redirect']._serialized_options = b'\xe0A\x01'
    _globals['_PHOTOMEDIA']._loaded_options = None
    _globals['_PHOTOMEDIA']._serialized_options = b'\xeaAm\n places.googleapis.com/PhotoMedia\x120places/{place_id}/photos/{photo_reference}/media*\x0bphotoMedias2\nphotoMedia'
    _globals['_GETPLACEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPLACEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bplaces.googleapis.com/Place'
    _globals['_GETPLACEREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_GETPLACEREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_GETPLACEREQUEST'].fields_by_name['region_code']._loaded_options = None
    _globals['_GETPLACEREQUEST'].fields_by_name['region_code']._serialized_options = b'\xe0A\x01'
    _globals['_GETPLACEREQUEST'].fields_by_name['session_token']._loaded_options = None
    _globals['_GETPLACEREQUEST'].fields_by_name['session_token']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['input']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['input']._serialized_options = b'\xe0A\x02'
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['location_bias']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['location_bias']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['location_restriction']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['location_restriction']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['included_primary_types']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['included_primary_types']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['included_region_codes']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['included_region_codes']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['region_code']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['region_code']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['origin']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['origin']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['input_offset']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['input_offset']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['include_query_predictions']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['include_query_predictions']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['session_token']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['session_token']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['include_pure_service_area_businesses']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESREQUEST'].fields_by_name['include_pure_service_area_businesses']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION_PLACEPREDICTION'].fields_by_name['place']._loaded_options = None
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION_PLACEPREDICTION'].fields_by_name['place']._serialized_options = b'\xfaA\x1d\n\x1bplaces.googleapis.com/Place'
    _globals['_PLACES']._loaded_options = None
    _globals['_PLACES']._serialized_options = b'\xcaA\x15places.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PLACES'].methods_by_name['SearchNearby']._loaded_options = None
    _globals['_PLACES'].methods_by_name['SearchNearby']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/v1/places:searchNearby:\x01*'
    _globals['_PLACES'].methods_by_name['SearchText']._loaded_options = None
    _globals['_PLACES'].methods_by_name['SearchText']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/v1/places:searchText:\x01*'
    _globals['_PLACES'].methods_by_name['GetPhotoMedia']._loaded_options = None
    _globals['_PLACES'].methods_by_name['GetPhotoMedia']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/v1/{name=places/*/photos/*/media}'
    _globals['_PLACES'].methods_by_name['GetPlace']._loaded_options = None
    _globals['_PLACES'].methods_by_name['GetPlace']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/{name=places/*}'
    _globals['_PLACES'].methods_by_name['AutocompletePlaces']._loaded_options = None
    _globals['_PLACES'].methods_by_name['AutocompletePlaces']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1c"\x17/v1/places:autocomplete:\x01*'
    _globals['_ROUTINGPARAMETERS']._serialized_start = 622
    _globals['_ROUTINGPARAMETERS']._serialized_end = 888
    _globals['_SEARCHNEARBYREQUEST']._serialized_start = 891
    _globals['_SEARCHNEARBYREQUEST']._serialized_end = 1513
    _globals['_SEARCHNEARBYREQUEST_LOCATIONRESTRICTION']._serialized_start = 1354
    _globals['_SEARCHNEARBYREQUEST_LOCATIONRESTRICTION']._serialized_end = 1432
    _globals['_SEARCHNEARBYREQUEST_RANKPREFERENCE']._serialized_start = 1434
    _globals['_SEARCHNEARBYREQUEST_RANKPREFERENCE']._serialized_end = 1513
    _globals['_SEARCHNEARBYRESPONSE']._serialized_start = 1516
    _globals['_SEARCHNEARBYRESPONSE']._serialized_end = 1650
    _globals['_SEARCHTEXTREQUEST']._serialized_start = 1653
    _globals['_SEARCHTEXTREQUEST']._serialized_end = 2972
    _globals['_SEARCHTEXTREQUEST_LOCATIONBIAS']._serialized_start = 2486
    _globals['_SEARCHTEXTREQUEST_LOCATIONBIAS']._serialized_end = 2605
    _globals['_SEARCHTEXTREQUEST_LOCATIONRESTRICTION']._serialized_start = 2607
    _globals['_SEARCHTEXTREQUEST_LOCATIONRESTRICTION']._serialized_end = 2684
    _globals['_SEARCHTEXTREQUEST_EVOPTIONS']._serialized_start = 2686
    _globals['_SEARCHTEXTREQUEST_EVOPTIONS']._serialized_end = 2806
    _globals['_SEARCHTEXTREQUEST_SEARCHALONGROUTEPARAMETERS']._serialized_start = 2808
    _globals['_SEARCHTEXTREQUEST_SEARCHALONGROUTEPARAMETERS']._serialized_end = 2892
    _globals['_SEARCHTEXTREQUEST_RANKPREFERENCE']._serialized_start = 2894
    _globals['_SEARCHTEXTREQUEST_RANKPREFERENCE']._serialized_end = 2972
    _globals['_SEARCHTEXTRESPONSE']._serialized_start = 2975
    _globals['_SEARCHTEXTRESPONSE']._serialized_end = 3178
    _globals['_GETPHOTOMEDIAREQUEST']._serialized_start = 3181
    _globals['_GETPHOTOMEDIAREQUEST']._serialized_end = 3347
    _globals['_PHOTOMEDIA']._serialized_start = 3350
    _globals['_PHOTOMEDIA']._serialized_end = 3509
    _globals['_GETPLACEREQUEST']._serialized_start = 3512
    _globals['_GETPLACEREQUEST']._serialized_end = 3662
    _globals['_AUTOCOMPLETEPLACESREQUEST']._serialized_start = 3665
    _globals['_AUTOCOMPLETEPLACESREQUEST']._serialized_end = 4472
    _globals['_AUTOCOMPLETEPLACESREQUEST_LOCATIONBIAS']._serialized_start = 2486
    _globals['_AUTOCOMPLETEPLACESREQUEST_LOCATIONBIAS']._serialized_end = 2605
    _globals['_AUTOCOMPLETEPLACESREQUEST_LOCATIONRESTRICTION']._serialized_start = 4346
    _globals['_AUTOCOMPLETEPLACESREQUEST_LOCATIONRESTRICTION']._serialized_end = 4472
    _globals['_AUTOCOMPLETEPLACESRESPONSE']._serialized_start = 4475
    _globals['_AUTOCOMPLETEPLACESRESPONSE']._serialized_end = 5765
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION']._serialized_start = 4589
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION']._serialized_end = 5765
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION_STRINGRANGE']._serialized_start = 4815
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION_STRINGRANGE']._serialized_end = 4870
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION_FORMATTABLETEXT']._serialized_start = 4872
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION_FORMATTABLETEXT']._serialized_end = 4994
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION_STRUCTUREDFORMAT']._serialized_start = 4997
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION_STRUCTUREDFORMAT']._serialized_end = 5214
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION_PLACEPREDICTION']._serialized_start = 5217
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION_PLACEPREDICTION']._serialized_end = 5539
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION_QUERYPREDICTION']._serialized_start = 5542
    _globals['_AUTOCOMPLETEPLACESRESPONSE_SUGGESTION_QUERYPREDICTION']._serialized_end = 5757
    _globals['_PLACES']._serialized_start = 5768
    _globals['_PLACES']._serialized_end = 6554