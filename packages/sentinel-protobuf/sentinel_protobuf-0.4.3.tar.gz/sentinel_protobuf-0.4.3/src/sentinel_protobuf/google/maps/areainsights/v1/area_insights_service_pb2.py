"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/areainsights/v1/area_insights_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/maps/areainsights/v1/area_insights_service.proto\x12\x1bgoogle.maps.areainsights.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x18google/type/latlng.proto"\x8f\x01\n\x16ComputeInsightsRequest\x12;\n\x08insights\x18\x04 \x03(\x0e2$.google.maps.areainsights.v1.InsightB\x03\xe0A\x02\x128\n\x06filter\x18\x05 \x01(\x0b2#.google.maps.areainsights.v1.FilterB\x03\xe0A\x02"z\n\x17ComputeInsightsResponse\x12\x12\n\x05count\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12A\n\x0eplace_insights\x18\x05 \x03(\x0b2).google.maps.areainsights.v1.PlaceInsightB\x08\n\x06_count"?\n\x0cPlaceInsight\x12/\n\x05place\x18\x01 \x01(\tB \xfaA\x1d\n\x1bplaces.googleapis.com/Place"\xee\x02\n\x06Filter\x12I\n\x0flocation_filter\x18\x01 \x01(\x0b2+.google.maps.areainsights.v1.LocationFilterB\x03\xe0A\x02\x12A\n\x0btype_filter\x18\x02 \x01(\x0b2\'.google.maps.areainsights.v1.TypeFilterB\x03\xe0A\x02\x12K\n\x10operating_status\x18\x03 \x03(\x0e2,.google.maps.areainsights.v1.OperatingStatusB\x03\xe0A\x01\x12B\n\x0cprice_levels\x18\x04 \x03(\x0e2\'.google.maps.areainsights.v1.PriceLevelB\x03\xe0A\x01\x12E\n\rrating_filter\x18\x05 \x01(\x0b2).google.maps.areainsights.v1.RatingFilterB\x03\xe0A\x01"\xde\x04\n\x0eLocationFilter\x12D\n\x06circle\x18\x01 \x01(\x0b22.google.maps.areainsights.v1.LocationFilter.CircleH\x00\x12D\n\x06region\x18\x02 \x01(\x0b22.google.maps.areainsights.v1.LocationFilter.RegionH\x00\x12M\n\x0bcustom_area\x18\x03 \x01(\x0b26.google.maps.areainsights.v1.LocationFilter.CustomAreaH\x00\x1a\x82\x01\n\x06Circle\x12&\n\x07lat_lng\x18\x01 \x01(\x0b2\x13.google.type.LatLngH\x00\x121\n\x05place\x18\x02 \x01(\tB \xfaA\x1d\n\x1bplaces.googleapis.com/PlaceH\x00\x12\x13\n\x06radius\x18\x03 \x01(\x05B\x03\xe0A\x01B\x08\n\x06center\x1aE\n\x06Region\x121\n\x05place\x18\x01 \x01(\tB \xfaA\x1d\n\x1bplaces.googleapis.com/PlaceH\x00B\x08\n\x06region\x1a\x9c\x01\n\nCustomArea\x12T\n\x07polygon\x18\x01 \x01(\x0b2>.google.maps.areainsights.v1.LocationFilter.CustomArea.PolygonB\x03\xe0A\x02\x1a8\n\x07Polygon\x12-\n\x0bcoordinates\x18\x01 \x03(\x0b2\x13.google.type.LatLngB\x03\xe0A\x01B\x06\n\x04area"\x90\x01\n\nTypeFilter\x12\x1b\n\x0eincluded_types\x18\x01 \x03(\tB\x03\xe0A\x01\x12\x1b\n\x0eexcluded_types\x18\x02 \x03(\tB\x03\xe0A\x01\x12#\n\x16included_primary_types\x18\x03 \x03(\tB\x03\xe0A\x01\x12#\n\x16excluded_primary_types\x18\x04 \x03(\tB\x03\xe0A\x01"h\n\x0cRatingFilter\x12\x1c\n\nmin_rating\x18\x05 \x01(\x02B\x03\xe0A\x01H\x00\x88\x01\x01\x12\x1c\n\nmax_rating\x18\x06 \x01(\x02B\x03\xe0A\x01H\x01\x88\x01\x01B\r\n\x0b_min_ratingB\r\n\x0b_max_rating*I\n\x07Insight\x12\x17\n\x13INSIGHT_UNSPECIFIED\x10\x00\x12\x11\n\rINSIGHT_COUNT\x10\x01\x12\x12\n\x0eINSIGHT_PLACES\x10\x02*\xa7\x01\n\x0fOperatingStatus\x12 \n\x1cOPERATING_STATUS_UNSPECIFIED\x10\x00\x12 \n\x1cOPERATING_STATUS_OPERATIONAL\x10\x01\x12\'\n#OPERATING_STATUS_PERMANENTLY_CLOSED\x10\x03\x12\'\n#OPERATING_STATUS_TEMPORARILY_CLOSED\x10\x04*\xb1\x01\n\nPriceLevel\x12\x1b\n\x17PRICE_LEVEL_UNSPECIFIED\x10\x00\x12\x14\n\x10PRICE_LEVEL_FREE\x10\x01\x12\x1b\n\x17PRICE_LEVEL_INEXPENSIVE\x10\x02\x12\x18\n\x14PRICE_LEVEL_MODERATE\x10\x03\x12\x19\n\x15PRICE_LEVEL_EXPENSIVE\x10\x04\x12\x1e\n\x1aPRICE_LEVEL_VERY_EXPENSIVE\x10\x052\xfe\x01\n\x0cAreaInsights\x12\x9c\x01\n\x0fComputeInsights\x123.google.maps.areainsights.v1.ComputeInsightsRequest\x1a4.google.maps.areainsights.v1.ComputeInsightsResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/v1:computeInsights:\x01*\x1aO\xcaA\x1bareainsights.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xfd\x01\n\x1fcom.google.maps.areainsights.v1B\x18AreaInsightsServiceProtoP\x01ZIcloud.google.com/go/maps/areainsights/apiv1/areainsightspb;areainsightspb\xa2\x02\x03MAI\xaa\x02\x1bGoogle.Maps.AreaInsights.V1\xca\x02\x1bGoogle\\Maps\\AreaInsights\\V1\xeaA0\n\x1bplaces.googleapis.com/Place\x12\x11places/{place_id}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.areainsights.v1.area_insights_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.maps.areainsights.v1B\x18AreaInsightsServiceProtoP\x01ZIcloud.google.com/go/maps/areainsights/apiv1/areainsightspb;areainsightspb\xa2\x02\x03MAI\xaa\x02\x1bGoogle.Maps.AreaInsights.V1\xca\x02\x1bGoogle\\Maps\\AreaInsights\\V1\xeaA0\n\x1bplaces.googleapis.com/Place\x12\x11places/{place_id}'
    _globals['_COMPUTEINSIGHTSREQUEST'].fields_by_name['insights']._loaded_options = None
    _globals['_COMPUTEINSIGHTSREQUEST'].fields_by_name['insights']._serialized_options = b'\xe0A\x02'
    _globals['_COMPUTEINSIGHTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_COMPUTEINSIGHTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_PLACEINSIGHT'].fields_by_name['place']._loaded_options = None
    _globals['_PLACEINSIGHT'].fields_by_name['place']._serialized_options = b'\xfaA\x1d\n\x1bplaces.googleapis.com/Place'
    _globals['_FILTER'].fields_by_name['location_filter']._loaded_options = None
    _globals['_FILTER'].fields_by_name['location_filter']._serialized_options = b'\xe0A\x02'
    _globals['_FILTER'].fields_by_name['type_filter']._loaded_options = None
    _globals['_FILTER'].fields_by_name['type_filter']._serialized_options = b'\xe0A\x02'
    _globals['_FILTER'].fields_by_name['operating_status']._loaded_options = None
    _globals['_FILTER'].fields_by_name['operating_status']._serialized_options = b'\xe0A\x01'
    _globals['_FILTER'].fields_by_name['price_levels']._loaded_options = None
    _globals['_FILTER'].fields_by_name['price_levels']._serialized_options = b'\xe0A\x01'
    _globals['_FILTER'].fields_by_name['rating_filter']._loaded_options = None
    _globals['_FILTER'].fields_by_name['rating_filter']._serialized_options = b'\xe0A\x01'
    _globals['_LOCATIONFILTER_CIRCLE'].fields_by_name['place']._loaded_options = None
    _globals['_LOCATIONFILTER_CIRCLE'].fields_by_name['place']._serialized_options = b'\xfaA\x1d\n\x1bplaces.googleapis.com/Place'
    _globals['_LOCATIONFILTER_CIRCLE'].fields_by_name['radius']._loaded_options = None
    _globals['_LOCATIONFILTER_CIRCLE'].fields_by_name['radius']._serialized_options = b'\xe0A\x01'
    _globals['_LOCATIONFILTER_REGION'].fields_by_name['place']._loaded_options = None
    _globals['_LOCATIONFILTER_REGION'].fields_by_name['place']._serialized_options = b'\xfaA\x1d\n\x1bplaces.googleapis.com/Place'
    _globals['_LOCATIONFILTER_CUSTOMAREA_POLYGON'].fields_by_name['coordinates']._loaded_options = None
    _globals['_LOCATIONFILTER_CUSTOMAREA_POLYGON'].fields_by_name['coordinates']._serialized_options = b'\xe0A\x01'
    _globals['_LOCATIONFILTER_CUSTOMAREA'].fields_by_name['polygon']._loaded_options = None
    _globals['_LOCATIONFILTER_CUSTOMAREA'].fields_by_name['polygon']._serialized_options = b'\xe0A\x02'
    _globals['_TYPEFILTER'].fields_by_name['included_types']._loaded_options = None
    _globals['_TYPEFILTER'].fields_by_name['included_types']._serialized_options = b'\xe0A\x01'
    _globals['_TYPEFILTER'].fields_by_name['excluded_types']._loaded_options = None
    _globals['_TYPEFILTER'].fields_by_name['excluded_types']._serialized_options = b'\xe0A\x01'
    _globals['_TYPEFILTER'].fields_by_name['included_primary_types']._loaded_options = None
    _globals['_TYPEFILTER'].fields_by_name['included_primary_types']._serialized_options = b'\xe0A\x01'
    _globals['_TYPEFILTER'].fields_by_name['excluded_primary_types']._loaded_options = None
    _globals['_TYPEFILTER'].fields_by_name['excluded_primary_types']._serialized_options = b'\xe0A\x01'
    _globals['_RATINGFILTER'].fields_by_name['min_rating']._loaded_options = None
    _globals['_RATINGFILTER'].fields_by_name['min_rating']._serialized_options = b'\xe0A\x01'
    _globals['_RATINGFILTER'].fields_by_name['max_rating']._loaded_options = None
    _globals['_RATINGFILTER'].fields_by_name['max_rating']._serialized_options = b'\xe0A\x01'
    _globals['_AREAINSIGHTS']._loaded_options = None
    _globals['_AREAINSIGHTS']._serialized_options = b'\xcaA\x1bareainsights.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_AREAINSIGHTS'].methods_by_name['ComputeInsights']._loaded_options = None
    _globals['_AREAINSIGHTS'].methods_by_name['ComputeInsights']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/v1:computeInsights:\x01*'
    _globals['_INSIGHT']._serialized_start = 1795
    _globals['_INSIGHT']._serialized_end = 1868
    _globals['_OPERATINGSTATUS']._serialized_start = 1871
    _globals['_OPERATINGSTATUS']._serialized_end = 2038
    _globals['_PRICELEVEL']._serialized_start = 2041
    _globals['_PRICELEVEL']._serialized_end = 2218
    _globals['_COMPUTEINSIGHTSREQUEST']._serialized_start = 230
    _globals['_COMPUTEINSIGHTSREQUEST']._serialized_end = 373
    _globals['_COMPUTEINSIGHTSRESPONSE']._serialized_start = 375
    _globals['_COMPUTEINSIGHTSRESPONSE']._serialized_end = 497
    _globals['_PLACEINSIGHT']._serialized_start = 499
    _globals['_PLACEINSIGHT']._serialized_end = 562
    _globals['_FILTER']._serialized_start = 565
    _globals['_FILTER']._serialized_end = 931
    _globals['_LOCATIONFILTER']._serialized_start = 934
    _globals['_LOCATIONFILTER']._serialized_end = 1540
    _globals['_LOCATIONFILTER_CIRCLE']._serialized_start = 1172
    _globals['_LOCATIONFILTER_CIRCLE']._serialized_end = 1302
    _globals['_LOCATIONFILTER_REGION']._serialized_start = 1304
    _globals['_LOCATIONFILTER_REGION']._serialized_end = 1373
    _globals['_LOCATIONFILTER_CUSTOMAREA']._serialized_start = 1376
    _globals['_LOCATIONFILTER_CUSTOMAREA']._serialized_end = 1532
    _globals['_LOCATIONFILTER_CUSTOMAREA_POLYGON']._serialized_start = 1476
    _globals['_LOCATIONFILTER_CUSTOMAREA_POLYGON']._serialized_end = 1532
    _globals['_TYPEFILTER']._serialized_start = 1543
    _globals['_TYPEFILTER']._serialized_end = 1687
    _globals['_RATINGFILTER']._serialized_start = 1689
    _globals['_RATINGFILTER']._serialized_end = 1793
    _globals['_AREAINSIGHTS']._serialized_start = 2221
    _globals['_AREAINSIGHTS']._serialized_end = 2475