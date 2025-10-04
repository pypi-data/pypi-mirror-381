"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/common/asset_types.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.common import criteria_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_criteria__pb2
from ......google.ads.searchads360.v0.enums import call_conversion_reporting_state_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_call__conversion__reporting__state__pb2
from ......google.ads.searchads360.v0.enums import call_to_action_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_call__to__action__type__pb2
from ......google.ads.searchads360.v0.enums import location_ownership_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_location__ownership__type__pb2
from ......google.ads.searchads360.v0.enums import mime_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_mime__type__pb2
from ......google.ads.searchads360.v0.enums import mobile_app_vendor_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_mobile__app__vendor__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/searchads360/v0/common/asset_types.proto\x12!google.ads.searchads360.v0.common\x1a0google/ads/searchads360/v0/common/criteria.proto\x1aFgoogle/ads/searchads360/v0/enums/call_conversion_reporting_state.proto\x1a:google/ads/searchads360/v0/enums/call_to_action_type.proto\x1a>google/ads/searchads360/v0/enums/location_ownership_type.proto\x1a0google/ads/searchads360/v0/enums/mime_type.proto\x1a8google/ads/searchads360/v0/enums/mobile_app_vendor.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"d\n\x11YoutubeVideoAsset\x12\x1d\n\x10youtube_video_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x13youtube_video_title\x18\x03 \x01(\tB\x13\n\x11_youtube_video_id"\xc4\x01\n\nImageAsset\x12\x16\n\tfile_size\x18\x06 \x01(\x03H\x00\x88\x01\x01\x12J\n\tmime_type\x18\x03 \x01(\x0e27.google.ads.searchads360.v0.enums.MimeTypeEnum.MimeType\x12D\n\tfull_size\x18\x04 \x01(\x0b21.google.ads.searchads360.v0.common.ImageDimensionB\x0c\n\n_file_size"\x84\x01\n\x0eImageDimension\x12\x1a\n\rheight_pixels\x18\x04 \x01(\x03H\x00\x88\x01\x01\x12\x19\n\x0cwidth_pixels\x18\x05 \x01(\x03H\x01\x88\x01\x01\x12\x10\n\x03url\x18\x06 \x01(\tH\x02\x88\x01\x01B\x10\n\x0e_height_pixelsB\x0f\n\r_width_pixelsB\x06\n\x04_url"\'\n\tTextAsset\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01B\x07\n\x05_text"\xc1\x01\n\x13UnifiedCalloutAsset\x12\x14\n\x0ccallout_text\x18\x01 \x01(\t\x12\x12\n\nstart_date\x18\x02 \x01(\t\x12\x10\n\x08end_date\x18\x03 \x01(\t\x12N\n\x13ad_schedule_targets\x18\x04 \x03(\x0b21.google.ads.searchads360.v0.common.AdScheduleInfo\x12\x1e\n\x16use_searcher_time_zone\x18\x05 \x01(\x08"\x9a\x02\n\x14UnifiedSitelinkAsset\x12\x11\n\tlink_text\x18\x01 \x01(\t\x12\x14\n\x0cdescription1\x18\x02 \x01(\t\x12\x14\n\x0cdescription2\x18\x03 \x01(\t\x12\x12\n\nstart_date\x18\x04 \x01(\t\x12\x10\n\x08end_date\x18\x05 \x01(\t\x12N\n\x13ad_schedule_targets\x18\x06 \x03(\x0b21.google.ads.searchads360.v0.common.AdScheduleInfo\x12\x13\n\x0btracking_id\x18\x07 \x01(\x03\x12\x1e\n\x16use_searcher_time_zone\x18\x08 \x01(\x08\x12\x18\n\x10mobile_preferred\x18\t \x01(\x08"8\n\x14UnifiedPageFeedAsset\x12\x10\n\x08page_url\x18\x01 \x01(\t\x12\x0e\n\x06labels\x18\x02 \x03(\t"\x84\x01\n\x0eMobileAppAsset\x12\x13\n\x06app_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12]\n\tapp_store\x18\x02 \x01(\x0e2E.google.ads.searchads360.v0.enums.MobileAppVendorEnum.MobileAppVendorB\x03\xe0A\x02"\xe9\x03\n\x10UnifiedCallAsset\x12\x14\n\x0ccountry_code\x18\x01 \x01(\t\x12\x14\n\x0cphone_number\x18\x02 \x01(\t\x12\x8d\x01\n\x1fcall_conversion_reporting_state\x18\x03 \x01(\x0e2_.google.ads.searchads360.v0.enums.CallConversionReportingStateEnum.CallConversionReportingStateB\x03\xe0A\x03\x12Q\n\x16call_conversion_action\x18\x04 \x01(\tB1\xfaA.\n,searchads360.googleapis.com/ConversionAction\x12N\n\x13ad_schedule_targets\x18\x05 \x03(\x0b21.google.ads.searchads360.v0.common.AdScheduleInfo\x12\x11\n\tcall_only\x18\x07 \x01(\x08\x12\x1d\n\x15call_tracking_enabled\x18\x08 \x01(\x08\x12\x1e\n\x16use_searcher_time_zone\x18\t \x01(\x08\x12\x12\n\nstart_date\x18\n \x01(\t\x12\x10\n\x08end_date\x18\x0b \x01(\t"t\n\x11CallToActionAsset\x12_\n\x0ecall_to_action\x18\x01 \x01(\x0e2G.google.ads.searchads360.v0.enums.CallToActionTypeEnum.CallToActionType"\xfc\x01\n\x14UnifiedLocationAsset\x12\x10\n\x08place_id\x18\x01 \x01(\t\x12^\n\x1abusiness_profile_locations\x18\x02 \x03(\x0b2:.google.ads.searchads360.v0.common.BusinessProfileLocation\x12r\n\x17location_ownership_type\x18\x03 \x01(\x0e2Q.google.ads.searchads360.v0.enums.LocationOwnershipTypeEnum.LocationOwnershipType"Q\n\x17BusinessProfileLocation\x12\x0e\n\x06labels\x18\x01 \x03(\t\x12\x12\n\nstore_code\x18\x02 \x01(\t\x12\x12\n\nlisting_id\x18\x03 \x01(\x03B\xfd\x01\n%com.google.ads.searchads360.v0.commonB\x0fAssetTypesProtoP\x01ZGgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/common;common\xa2\x02\x07GASA360\xaa\x02!Google.Ads.SearchAds360.V0.Common\xca\x02!Google\\Ads\\SearchAds360\\V0\\Common\xea\x02%Google::Ads::SearchAds360::V0::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.common.asset_types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.searchads360.v0.commonB\x0fAssetTypesProtoP\x01ZGgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/common;common\xa2\x02\x07GASA360\xaa\x02!Google.Ads.SearchAds360.V0.Common\xca\x02!Google\\Ads\\SearchAds360\\V0\\Common\xea\x02%Google::Ads::SearchAds360::V0::Common'
    _globals['_MOBILEAPPASSET'].fields_by_name['app_id']._loaded_options = None
    _globals['_MOBILEAPPASSET'].fields_by_name['app_id']._serialized_options = b'\xe0A\x02'
    _globals['_MOBILEAPPASSET'].fields_by_name['app_store']._loaded_options = None
    _globals['_MOBILEAPPASSET'].fields_by_name['app_store']._serialized_options = b'\xe0A\x02'
    _globals['_UNIFIEDCALLASSET'].fields_by_name['call_conversion_reporting_state']._loaded_options = None
    _globals['_UNIFIEDCALLASSET'].fields_by_name['call_conversion_reporting_state']._serialized_options = b'\xe0A\x03'
    _globals['_UNIFIEDCALLASSET'].fields_by_name['call_conversion_action']._loaded_options = None
    _globals['_UNIFIEDCALLASSET'].fields_by_name['call_conversion_action']._serialized_options = b'\xfaA.\n,searchads360.googleapis.com/ConversionAction'
    _globals['_YOUTUBEVIDEOASSET']._serialized_start = 504
    _globals['_YOUTUBEVIDEOASSET']._serialized_end = 604
    _globals['_IMAGEASSET']._serialized_start = 607
    _globals['_IMAGEASSET']._serialized_end = 803
    _globals['_IMAGEDIMENSION']._serialized_start = 806
    _globals['_IMAGEDIMENSION']._serialized_end = 938
    _globals['_TEXTASSET']._serialized_start = 940
    _globals['_TEXTASSET']._serialized_end = 979
    _globals['_UNIFIEDCALLOUTASSET']._serialized_start = 982
    _globals['_UNIFIEDCALLOUTASSET']._serialized_end = 1175
    _globals['_UNIFIEDSITELINKASSET']._serialized_start = 1178
    _globals['_UNIFIEDSITELINKASSET']._serialized_end = 1460
    _globals['_UNIFIEDPAGEFEEDASSET']._serialized_start = 1462
    _globals['_UNIFIEDPAGEFEEDASSET']._serialized_end = 1518
    _globals['_MOBILEAPPASSET']._serialized_start = 1521
    _globals['_MOBILEAPPASSET']._serialized_end = 1653
    _globals['_UNIFIEDCALLASSET']._serialized_start = 1656
    _globals['_UNIFIEDCALLASSET']._serialized_end = 2145
    _globals['_CALLTOACTIONASSET']._serialized_start = 2147
    _globals['_CALLTOACTIONASSET']._serialized_end = 2263
    _globals['_UNIFIEDLOCATIONASSET']._serialized_start = 2266
    _globals['_UNIFIEDLOCATIONASSET']._serialized_end = 2518
    _globals['_BUSINESSPROFILELOCATION']._serialized_start = 2520
    _globals['_BUSINESSPROFILELOCATION']._serialized_end = 2601