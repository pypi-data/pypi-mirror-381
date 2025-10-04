"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/smart_campaign_setting.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/googleads/v20/resources/smart_campaign_setting.proto\x12"google.ads.googleads.v20.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd8\x06\n\x14SmartCampaignSetting\x12L\n\rresource_name\x18\x01 \x01(\tB5\xe0A\x05\xfaA/\n-googleads.googleapis.com/SmartCampaignSetting\x12;\n\x08campaign\x18\x02 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign\x12Z\n\x0cphone_number\x18\x03 \x01(\x0b2D.google.ads.googleads.v20.resources.SmartCampaignSetting.PhoneNumber\x12!\n\x19advertising_language_code\x18\x07 \x01(\t\x12\x13\n\tfinal_url\x18\x08 \x01(\tH\x00\x12\x8b\x01\n%ad_optimized_business_profile_setting\x18\t \x01(\x0b2Z.google.ads.googleads.v20.resources.SmartCampaignSetting.AdOptimizedBusinessProfileSettingH\x00\x12\x17\n\rbusiness_name\x18\x05 \x01(\tH\x01\x12#\n\x19business_profile_location\x18\n \x01(\tH\x01\x1ae\n\x0bPhoneNumber\x12\x19\n\x0cphone_number\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0ccountry_code\x18\x02 \x01(\tH\x01\x88\x01\x01B\x0f\n\r_phone_numberB\x0f\n\r_country_code\x1aY\n!AdOptimizedBusinessProfileSetting\x12\x1e\n\x11include_lead_form\x18\x01 \x01(\x08H\x00\x88\x01\x01B\x14\n\x12_include_lead_form:o\xeaAl\n-googleads.googleapis.com/SmartCampaignSetting\x12;customers/{customer_id}/smartCampaignSettings/{campaign_id}B\x0e\n\x0clanding_pageB\x12\n\x10business_settingB\x8b\x02\n&com.google.ads.googleads.v20.resourcesB\x19SmartCampaignSettingProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.smart_campaign_setting_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x19SmartCampaignSettingProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_SMARTCAMPAIGNSETTING'].fields_by_name['resource_name']._loaded_options = None
    _globals['_SMARTCAMPAIGNSETTING'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA/\n-googleads.googleapis.com/SmartCampaignSetting'
    _globals['_SMARTCAMPAIGNSETTING'].fields_by_name['campaign']._loaded_options = None
    _globals['_SMARTCAMPAIGNSETTING'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_SMARTCAMPAIGNSETTING']._loaded_options = None
    _globals['_SMARTCAMPAIGNSETTING']._serialized_options = b'\xeaAl\n-googleads.googleapis.com/SmartCampaignSetting\x12;customers/{customer_id}/smartCampaignSettings/{campaign_id}'
    _globals['_SMARTCAMPAIGNSETTING']._serialized_start = 164
    _globals['_SMARTCAMPAIGNSETTING']._serialized_end = 1020
    _globals['_SMARTCAMPAIGNSETTING_PHONENUMBER']._serialized_start = 679
    _globals['_SMARTCAMPAIGNSETTING_PHONENUMBER']._serialized_end = 780
    _globals['_SMARTCAMPAIGNSETTING_ADOPTIMIZEDBUSINESSPROFILESETTING']._serialized_start = 782
    _globals['_SMARTCAMPAIGNSETTING_ADOPTIMIZEDBUSINESSPROFILESETTING']._serialized_end = 871