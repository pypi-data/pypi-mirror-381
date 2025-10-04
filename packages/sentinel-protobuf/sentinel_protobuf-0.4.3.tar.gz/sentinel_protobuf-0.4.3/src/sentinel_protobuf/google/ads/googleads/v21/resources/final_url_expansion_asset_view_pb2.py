"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/final_url_expansion_asset_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_asset__field__type__pb2
from ......google.ads.googleads.v21.enums import asset_link_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_asset__link__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/ads/googleads/v21/resources/final_url_expansion_asset_view.proto\x12"google.ads.googleads.v21.resources\x1a5google/ads/googleads/v21/enums/asset_field_type.proto\x1a6google/ads/googleads/v21/enums/asset_link_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc7\x06\n\x1aFinalUrlExpansionAssetView\x12R\n\rresource_name\x18\x01 \x01(\tB;\xe0A\x03\xfaA5\n3googleads.googleapis.com/FinalUrlExpansionAssetView\x12@\n\x08campaign\x18\x02 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/CampaignH\x01\x88\x01\x01\x12:\n\x05asset\x18\x03 \x01(\tB&\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/AssetH\x02\x88\x01\x01\x12Z\n\nfield_type\x18\x04 \x01(\x0e2A.google.ads.googleads.v21.enums.AssetFieldTypeEnum.AssetFieldTypeB\x03\xe0A\x03\x12]\n\x06status\x18\x05 \x01(\x0e2C.google.ads.googleads.v21.enums.AssetLinkStatusEnum.AssetLinkStatusB\x03\xe0A\x03H\x03\x88\x01\x01\x12\x16\n\tfinal_url\x18\x06 \x01(\tB\x03\xe0A\x03\x12<\n\x08ad_group\x18\x07 \x01(\tB(\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroupH\x00\x12B\n\x0basset_group\x18\x08 \x01(\tB+\xe0A\x03\xfaA%\n#googleads.googleapis.com/AssetGroupH\x00:\xd6\x01\xeaA\xd2\x01\n3googleads.googleapis.com/FinalUrlExpansionAssetView\x12bcustomers/{customer_id}/finalUrlExpansionAssetViews/{campaign_id}~{asset_id}~{field_type}~{url_fp}*\x1bfinalUrlExpansionAssetViews2\x1afinalUrlExpansionAssetViewB\x07\n\x05levelB\x0b\n\t_campaignB\x08\n\x06_assetB\t\n\x07_statusB\x91\x02\n&com.google.ads.googleads.v21.resourcesB\x1fFinalUrlExpansionAssetViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.final_url_expansion_asset_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x1fFinalUrlExpansionAssetViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA5\n3googleads.googleapis.com/FinalUrlExpansionAssetView'
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['campaign']._loaded_options = None
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['asset']._loaded_options = None
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['asset']._serialized_options = b'\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Asset'
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['field_type']._loaded_options = None
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['field_type']._serialized_options = b'\xe0A\x03'
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['status']._loaded_options = None
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['final_url']._loaded_options = None
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['final_url']._serialized_options = b'\xe0A\x03'
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['ad_group']._loaded_options = None
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['asset_group']._loaded_options = None
    _globals['_FINALURLEXPANSIONASSETVIEW'].fields_by_name['asset_group']._serialized_options = b'\xe0A\x03\xfaA%\n#googleads.googleapis.com/AssetGroup'
    _globals['_FINALURLEXPANSIONASSETVIEW']._loaded_options = None
    _globals['_FINALURLEXPANSIONASSETVIEW']._serialized_options = b'\xeaA\xd2\x01\n3googleads.googleapis.com/FinalUrlExpansionAssetView\x12bcustomers/{customer_id}/finalUrlExpansionAssetViews/{campaign_id}~{asset_id}~{field_type}~{url_fp}*\x1bfinalUrlExpansionAssetViews2\x1afinalUrlExpansionAssetView'
    _globals['_FINALURLEXPANSIONASSETVIEW']._serialized_start = 283
    _globals['_FINALURLEXPANSIONASSETVIEW']._serialized_end = 1122