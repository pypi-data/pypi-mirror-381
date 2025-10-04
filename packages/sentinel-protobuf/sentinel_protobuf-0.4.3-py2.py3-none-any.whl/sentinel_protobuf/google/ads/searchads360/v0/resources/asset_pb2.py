"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/asset.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.common import asset_types_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_asset__types__pb2
from ......google.ads.searchads360.v0.enums import asset_engine_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_asset__engine__status__pb2
from ......google.ads.searchads360.v0.enums import asset_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_asset__status__pb2
from ......google.ads.searchads360.v0.enums import asset_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_asset__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/ads/searchads360/v0/resources/asset.proto\x12$google.ads.searchads360.v0.resources\x1a3google/ads/searchads360/v0/common/asset_types.proto\x1a:google/ads/searchads360/v0/enums/asset_engine_status.proto\x1a3google/ads/searchads360/v0/enums/asset_status.proto\x1a1google/ads/searchads360/v0/enums/asset_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd9\x0b\n\x05Asset\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0A\x05\xfaA#\n!searchads360.googleapis.com/Asset\x12\x14\n\x02id\x18\x0b \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x11\n\x04name\x18\x0c \x01(\tH\x02\x88\x01\x01\x12L\n\x04type\x18\x04 \x01(\x0e29.google.ads.searchads360.v0.enums.AssetTypeEnum.AssetTypeB\x03\xe0A\x03\x12\x12\n\nfinal_urls\x18\x0e \x03(\t\x12"\n\x15tracking_url_template\x18\x11 \x01(\tH\x03\x88\x01\x01\x12R\n\x06status\x18* \x01(\x0e2=.google.ads.searchads360.v0.enums.AssetStatusEnum.AssetStatusB\x03\xe0A\x03\x12\x1a\n\rcreation_time\x18+ \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12last_modified_time\x18, \x01(\tB\x03\xe0A\x03\x12j\n\rengine_status\x18= \x01(\x0e2I.google.ads.searchads360.v0.enums.AssetEngineStatusEnum.AssetEngineStatusB\x03\xe0A\x03H\x04\x88\x01\x01\x12X\n\x13youtube_video_asset\x18\x05 \x01(\x0b24.google.ads.searchads360.v0.common.YoutubeVideoAssetB\x03\xe0A\x05H\x00\x12I\n\x0bimage_asset\x18\x07 \x01(\x0b2-.google.ads.searchads360.v0.common.ImageAssetB\x03\xe0A\x03H\x00\x12G\n\ntext_asset\x18\x08 \x01(\x0b2,.google.ads.searchads360.v0.common.TextAssetB\x03\xe0A\x03H\x00\x12T\n\rcallout_asset\x180 \x01(\x0b26.google.ads.searchads360.v0.common.UnifiedCalloutAssetB\x03\xe0A\x03H\x00\x12V\n\x0esitelink_asset\x18- \x01(\x0b27.google.ads.searchads360.v0.common.UnifiedSitelinkAssetB\x03\xe0A\x03H\x00\x12W\n\x0fpage_feed_asset\x18. \x01(\x0b27.google.ads.searchads360.v0.common.UnifiedPageFeedAssetB\x03\xe0A\x03H\x00\x12M\n\x10mobile_app_asset\x18\x19 \x01(\x0b21.google.ads.searchads360.v0.common.MobileAppAssetH\x00\x12N\n\ncall_asset\x18/ \x01(\x0b23.google.ads.searchads360.v0.common.UnifiedCallAssetB\x03\xe0A\x03H\x00\x12Y\n\x14call_to_action_asset\x18\x1d \x01(\x0b24.google.ads.searchads360.v0.common.CallToActionAssetB\x03\xe0A\x05H\x00\x12V\n\x0elocation_asset\x181 \x01(\x0b27.google.ads.searchads360.v0.common.UnifiedLocationAssetB\x03\xe0A\x03H\x00:Q\xeaAN\n!searchads360.googleapis.com/Asset\x12)customers/{customer_id}/assets/{asset_id}B\x0c\n\nasset_dataB\x05\n\x03_idB\x07\n\x05_nameB\x18\n\x16_tracking_url_templateB\x10\n\x0e_engine_statusB\x8a\x02\n(com.google.ads.searchads360.v0.resourcesB\nAssetProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.asset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\nAssetProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_ASSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA#\n!searchads360.googleapis.com/Asset'
    _globals['_ASSET'].fields_by_name['id']._loaded_options = None
    _globals['_ASSET'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['type']._loaded_options = None
    _globals['_ASSET'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['status']._loaded_options = None
    _globals['_ASSET'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['creation_time']._loaded_options = None
    _globals['_ASSET'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_ASSET'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['engine_status']._loaded_options = None
    _globals['_ASSET'].fields_by_name['engine_status']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['youtube_video_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['youtube_video_asset']._serialized_options = b'\xe0A\x05'
    _globals['_ASSET'].fields_by_name['image_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['image_asset']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['text_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['text_asset']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['callout_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['callout_asset']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['sitelink_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['sitelink_asset']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['page_feed_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['page_feed_asset']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['call_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['call_asset']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['call_to_action_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['call_to_action_asset']._serialized_options = b'\xe0A\x05'
    _globals['_ASSET'].fields_by_name['location_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['location_asset']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET']._loaded_options = None
    _globals['_ASSET']._serialized_options = b'\xeaAN\n!searchads360.googleapis.com/Asset\x12)customers/{customer_id}/assets/{asset_id}'
    _globals['_ASSET']._serialized_start = 368
    _globals['_ASSET']._serialized_end = 1865