"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/geographic_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import geo_targeting_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_geo__targeting__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v20/resources/geographic_view.proto\x12"google.ads.googleads.v20.resources\x1a7google/ads/googleads/v20/enums/geo_targeting_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xfa\x02\n\x0eGeographicView\x12F\n\rresource_name\x18\x01 \x01(\tB/\xe0A\x03\xfaA)\n\'googleads.googleapis.com/GeographicView\x12a\n\rlocation_type\x18\x03 \x01(\x0e2E.google.ads.googleads.v20.enums.GeoTargetingTypeEnum.GeoTargetingTypeB\x03\xe0A\x03\x12&\n\x14country_criterion_id\x18\x05 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01:|\xeaAy\n\'googleads.googleapis.com/GeographicView\x12Ncustomers/{customer_id}/geographicViews/{country_criterion_id}~{location_type}B\x17\n\x15_country_criterion_idB\x85\x02\n&com.google.ads.googleads.v20.resourcesB\x13GeographicViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.geographic_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x13GeographicViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_GEOGRAPHICVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_GEOGRAPHICVIEW'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x03\xfaA)\n'googleads.googleapis.com/GeographicView"
    _globals['_GEOGRAPHICVIEW'].fields_by_name['location_type']._loaded_options = None
    _globals['_GEOGRAPHICVIEW'].fields_by_name['location_type']._serialized_options = b'\xe0A\x03'
    _globals['_GEOGRAPHICVIEW'].fields_by_name['country_criterion_id']._loaded_options = None
    _globals['_GEOGRAPHICVIEW'].fields_by_name['country_criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_GEOGRAPHICVIEW']._loaded_options = None
    _globals['_GEOGRAPHICVIEW']._serialized_options = b"\xeaAy\n'googleads.googleapis.com/GeographicView\x12Ncustomers/{customer_id}/geographicViews/{country_criterion_id}~{location_type}"
    _globals['_GEOGRAPHICVIEW']._serialized_start = 214
    _globals['_GEOGRAPHICVIEW']._serialized_end = 592