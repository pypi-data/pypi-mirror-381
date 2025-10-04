"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/campaign_aggregate_asset_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_asset__field__type__pb2
from ......google.ads.googleads.v19.enums import asset_source_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_asset__source__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/ads/googleads/v19/resources/campaign_aggregate_asset_view.proto\x12"google.ads.googleads.v19.resources\x1a5google/ads/googleads/v19/enums/asset_field_type.proto\x1a1google/ads/googleads/v19/enums/asset_source.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x8e\x05\n\x1aCampaignAggregateAssetView\x12R\n\rresource_name\x18\x01 \x01(\tB;\xe0A\x03\xfaA5\n3googleads.googleapis.com/CampaignAggregateAssetView\x12@\n\x08campaign\x18\x02 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/CampaignH\x00\x88\x01\x01\x12:\n\x05asset\x18\x03 \x01(\tB&\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/AssetH\x01\x88\x01\x01\x12[\n\x0casset_source\x18\x04 \x01(\x0e2;.google.ads.googleads.v19.enums.AssetSourceEnum.AssetSourceB\x03\xe0A\x03H\x02\x88\x01\x01\x12_\n\nfield_type\x18\x05 \x01(\x0e2A.google.ads.googleads.v19.enums.AssetFieldTypeEnum.AssetFieldTypeB\x03\xe0A\x03H\x03\x88\x01\x01:\xa8\x01\xeaA\xa4\x01\n3googleads.googleapis.com/CampaignAggregateAssetView\x12mcustomers/{customer_id}/campaignAggregateAssetViews/{campaign_id}~{asset_id}~{asset_link_source}~{field_type}B\x0b\n\t_campaignB\x08\n\x06_assetB\x0f\n\r_asset_sourceB\r\n\x0b_field_typeB\x91\x02\n&com.google.ads.googleads.v19.resourcesB\x1fCampaignAggregateAssetViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.campaign_aggregate_asset_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x1fCampaignAggregateAssetViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_CAMPAIGNAGGREGATEASSETVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNAGGREGATEASSETVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA5\n3googleads.googleapis.com/CampaignAggregateAssetView'
    _globals['_CAMPAIGNAGGREGATEASSETVIEW'].fields_by_name['campaign']._loaded_options = None
    _globals['_CAMPAIGNAGGREGATEASSETVIEW'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CAMPAIGNAGGREGATEASSETVIEW'].fields_by_name['asset']._loaded_options = None
    _globals['_CAMPAIGNAGGREGATEASSETVIEW'].fields_by_name['asset']._serialized_options = b'\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Asset'
    _globals['_CAMPAIGNAGGREGATEASSETVIEW'].fields_by_name['asset_source']._loaded_options = None
    _globals['_CAMPAIGNAGGREGATEASSETVIEW'].fields_by_name['asset_source']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNAGGREGATEASSETVIEW'].fields_by_name['field_type']._loaded_options = None
    _globals['_CAMPAIGNAGGREGATEASSETVIEW'].fields_by_name['field_type']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNAGGREGATEASSETVIEW']._loaded_options = None
    _globals['_CAMPAIGNAGGREGATEASSETVIEW']._serialized_options = b'\xeaA\xa4\x01\n3googleads.googleapis.com/CampaignAggregateAssetView\x12mcustomers/{customer_id}/campaignAggregateAssetViews/{campaign_id}~{asset_id}~{asset_link_source}~{field_type}'
    _globals['_CAMPAIGNAGGREGATEASSETVIEW']._serialized_start = 277
    _globals['_CAMPAIGNAGGREGATEASSETVIEW']._serialized_end = 931