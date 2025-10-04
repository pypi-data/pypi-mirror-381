"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/performance_max_placement_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import placement_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_placement__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/ads/googleads/v20/resources/performance_max_placement_view.proto\x12"google.ads.googleads.v20.resources\x1a3google/ads/googleads/v20/enums/placement_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x9b\x04\n\x1bPerformanceMaxPlacementView\x12S\n\rresource_name\x18\x01 \x01(\tB<\xe0A\x03\xfaA6\n4googleads.googleapis.com/PerformanceMaxPlacementView\x12\x1b\n\tplacement\x18\x02 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1e\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1c\n\ntarget_url\x18\x04 \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12\\\n\x0eplacement_type\x18\x05 \x01(\x0e2?.google.ads.googleads.v20.enums.PlacementTypeEnum.PlacementTypeB\x03\xe0A\x03:\xbf\x01\xeaA\xbb\x01\n4googleads.googleapis.com/PerformanceMaxPlacementView\x12Hcustomers/{customer_id}/performanceMaxPlacementViews/{base_64_placement}*\x1cperformanceMaxPlacementViews2\x1bperformanceMaxPlacementViewB\x0c\n\n_placementB\x0f\n\r_display_nameB\r\n\x0b_target_urlB\x92\x02\n&com.google.ads.googleads.v20.resourcesB PerformanceMaxPlacementViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.performance_max_placement_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB PerformanceMaxPlacementViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_PERFORMANCEMAXPLACEMENTVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_PERFORMANCEMAXPLACEMENTVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA6\n4googleads.googleapis.com/PerformanceMaxPlacementView'
    _globals['_PERFORMANCEMAXPLACEMENTVIEW'].fields_by_name['placement']._loaded_options = None
    _globals['_PERFORMANCEMAXPLACEMENTVIEW'].fields_by_name['placement']._serialized_options = b'\xe0A\x03'
    _globals['_PERFORMANCEMAXPLACEMENTVIEW'].fields_by_name['display_name']._loaded_options = None
    _globals['_PERFORMANCEMAXPLACEMENTVIEW'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_PERFORMANCEMAXPLACEMENTVIEW'].fields_by_name['target_url']._loaded_options = None
    _globals['_PERFORMANCEMAXPLACEMENTVIEW'].fields_by_name['target_url']._serialized_options = b'\xe0A\x03'
    _globals['_PERFORMANCEMAXPLACEMENTVIEW'].fields_by_name['placement_type']._loaded_options = None
    _globals['_PERFORMANCEMAXPLACEMENTVIEW'].fields_by_name['placement_type']._serialized_options = b'\xe0A\x03'
    _globals['_PERFORMANCEMAXPLACEMENTVIEW']._loaded_options = None
    _globals['_PERFORMANCEMAXPLACEMENTVIEW']._serialized_options = b'\xeaA\xbb\x01\n4googleads.googleapis.com/PerformanceMaxPlacementView\x12Hcustomers/{customer_id}/performanceMaxPlacementViews/{base_64_placement}*\x1cperformanceMaxPlacementViews2\x1bperformanceMaxPlacementView'
    _globals['_PERFORMANCEMAXPLACEMENTVIEW']._serialized_start = 225
    _globals['_PERFORMANCEMAXPLACEMENTVIEW']._serialized_end = 764