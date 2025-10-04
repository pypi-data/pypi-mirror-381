"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/detail_content_suitability_placement_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import placement_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_placement__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nRgoogle/ads/googleads/v21/resources/detail_content_suitability_placement_view.proto\x12"google.ads.googleads.v21.resources\x1a3google/ads/googleads/v21/enums/placement_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x9e\x04\n%DetailContentSuitabilityPlacementView\x12]\n\rresource_name\x18\x01 \x01(\tBF\xe0A\x03\xfaA@\n>googleads.googleapis.com/DetailContentSuitabilityPlacementView\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x16\n\tplacement\x18\x03 \x01(\tB\x03\xe0A\x03\x12\\\n\x0eplacement_type\x18\x04 \x01(\x0e2?.google.ads.googleads.v21.enums.PlacementTypeEnum.PlacementTypeB\x03\xe0A\x03\x12\x17\n\ntarget_url\x18\x05 \x01(\tB\x03\xe0A\x03:\xeb\x01\xeaA\xe7\x01\n>googleads.googleapis.com/DetailContentSuitabilityPlacementView\x12Vcustomers/{customer_id}/detailContentSuitabilityPlacementViews/{placement_fingerprint}*&detailContentSuitabilityPlacementViews2%detailContentSuitabilityPlacementViewB\x9c\x02\n&com.google.ads.googleads.v21.resourcesB*DetailContentSuitabilityPlacementViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.detail_content_suitability_placement_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB*DetailContentSuitabilityPlacementViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA@\n>googleads.googleapis.com/DetailContentSuitabilityPlacementView'
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW'].fields_by_name['display_name']._loaded_options = None
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW'].fields_by_name['placement']._loaded_options = None
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW'].fields_by_name['placement']._serialized_options = b'\xe0A\x03'
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW'].fields_by_name['placement_type']._loaded_options = None
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW'].fields_by_name['placement_type']._serialized_options = b'\xe0A\x03'
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW'].fields_by_name['target_url']._loaded_options = None
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW'].fields_by_name['target_url']._serialized_options = b'\xe0A\x03'
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW']._loaded_options = None
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW']._serialized_options = b'\xeaA\xe7\x01\n>googleads.googleapis.com/DetailContentSuitabilityPlacementView\x12Vcustomers/{customer_id}/detailContentSuitabilityPlacementViews/{placement_fingerprint}*&detailContentSuitabilityPlacementViews2%detailContentSuitabilityPlacementView'
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW']._serialized_start = 236
    _globals['_DETAILCONTENTSUITABILITYPLACEMENTVIEW']._serialized_end = 778