"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/channel_aggregate_asset_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import advertising_channel_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_advertising__channel__type__pb2
from ......google.ads.googleads.v20.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__field__type__pb2
from ......google.ads.googleads.v20.enums import asset_source_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__source__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/ads/googleads/v20/resources/channel_aggregate_asset_view.proto\x12"google.ads.googleads.v20.resources\x1a=google/ads/googleads/v20/enums/advertising_channel_type.proto\x1a5google/ads/googleads/v20/enums/asset_field_type.proto\x1a1google/ads/googleads/v20/enums/asset_source.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xdf\x05\n\x19ChannelAggregateAssetView\x12Q\n\rresource_name\x18\x01 \x01(\tB:\xe0A\x03\xfaA4\n2googleads.googleapis.com/ChannelAggregateAssetView\x12}\n\x18advertising_channel_type\x18\x02 \x01(\x0e2Q.google.ads.googleads.v20.enums.AdvertisingChannelTypeEnum.AdvertisingChannelTypeB\x03\xe0A\x03H\x00\x88\x01\x01\x12:\n\x05asset\x18\x03 \x01(\tB&\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/AssetH\x01\x88\x01\x01\x12[\n\x0casset_source\x18\x04 \x01(\x0e2;.google.ads.googleads.v20.enums.AssetSourceEnum.AssetSourceB\x03\xe0A\x03H\x02\x88\x01\x01\x12_\n\nfield_type\x18\x05 \x01(\x0e2A.google.ads.googleads.v20.enums.AssetFieldTypeEnum.AssetFieldTypeB\x03\xe0A\x03H\x03\x88\x01\x01:\xae\x01\xeaA\xaa\x01\n2googleads.googleapis.com/ChannelAggregateAssetView\x12tcustomers/{customer_id}/channelAggregateAssetViews/{advertising_channel_type}~{asset_id}~{asset_source}~{field_type}B\x1b\n\x19_advertising_channel_typeB\x08\n\x06_assetB\x0f\n\r_asset_sourceB\r\n\x0b_field_typeB\x90\x02\n&com.google.ads.googleads.v20.resourcesB\x1eChannelAggregateAssetViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.channel_aggregate_asset_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x1eChannelAggregateAssetViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_CHANNELAGGREGATEASSETVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CHANNELAGGREGATEASSETVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA4\n2googleads.googleapis.com/ChannelAggregateAssetView'
    _globals['_CHANNELAGGREGATEASSETVIEW'].fields_by_name['advertising_channel_type']._loaded_options = None
    _globals['_CHANNELAGGREGATEASSETVIEW'].fields_by_name['advertising_channel_type']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELAGGREGATEASSETVIEW'].fields_by_name['asset']._loaded_options = None
    _globals['_CHANNELAGGREGATEASSETVIEW'].fields_by_name['asset']._serialized_options = b'\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Asset'
    _globals['_CHANNELAGGREGATEASSETVIEW'].fields_by_name['asset_source']._loaded_options = None
    _globals['_CHANNELAGGREGATEASSETVIEW'].fields_by_name['asset_source']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELAGGREGATEASSETVIEW'].fields_by_name['field_type']._loaded_options = None
    _globals['_CHANNELAGGREGATEASSETVIEW'].fields_by_name['field_type']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELAGGREGATEASSETVIEW']._loaded_options = None
    _globals['_CHANNELAGGREGATEASSETVIEW']._serialized_options = b'\xeaA\xaa\x01\n2googleads.googleapis.com/ChannelAggregateAssetView\x12tcustomers/{customer_id}/channelAggregateAssetViews/{advertising_channel_type}~{asset_id}~{asset_source}~{field_type}'
    _globals['_CHANNELAGGREGATEASSETVIEW']._serialized_start = 339
    _globals['_CHANNELAGGREGATEASSETVIEW']._serialized_end = 1074