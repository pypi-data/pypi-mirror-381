"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/customer.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import account_level_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_account__level__pb2
from ......google.ads.searchads360.v0.enums import account_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_account__status__pb2
from ......google.ads.searchads360.v0.enums import account_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_account__type__pb2
from ......google.ads.searchads360.v0.enums import conversion_tracking_status_enum_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_conversion__tracking__status__enum__pb2
from ......google.ads.searchads360.v0.enums import customer_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_customer__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/searchads360/v0/resources/customer.proto\x12$google.ads.searchads360.v0.resources\x1a4google/ads/searchads360/v0/enums/account_level.proto\x1a5google/ads/searchads360/v0/enums/account_status.proto\x1a3google/ads/searchads360/v0/enums/account_type.proto\x1aFgoogle/ads/searchads360/v0/enums/conversion_tracking_status_enum.proto\x1a6google/ads/searchads360/v0/enums/customer_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa9\x0b\n\x08Customer\x12C\n\rresource_name\x18\x01 \x01(\tB,\xe0A\x05\xfaA&\n$searchads360.googleapis.com/Customer\x12\x14\n\x02id\x18\x13 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1d\n\x10descriptive_name\x18\x14 \x01(\tH\x01\x88\x01\x01\x12\x1f\n\rcurrency_code\x18\x15 \x01(\tB\x03\xe0A\x05H\x02\x88\x01\x01\x12\x1b\n\ttime_zone\x18\x16 \x01(\tB\x03\xe0A\x05H\x03\x88\x01\x01\x12"\n\x15tracking_url_template\x18\x17 \x01(\tH\x04\x88\x01\x01\x12\x1d\n\x10final_url_suffix\x18\x18 \x01(\tH\x05\x88\x01\x01\x12!\n\x14auto_tagging_enabled\x18\x19 \x01(\x08H\x06\x88\x01\x01\x12\x19\n\x07manager\x18\x1b \x01(\x08B\x03\xe0A\x03H\x07\x88\x01\x01\x12i\n\x1bconversion_tracking_setting\x18\x0e \x01(\x0b2?.google.ads.searchads360.v0.resources.ConversionTrackingSettingB\x03\xe0A\x03\x12X\n\x0caccount_type\x18\x1f \x01(\x0e2=.google.ads.searchads360.v0.enums.AccountTypeEnum.AccountTypeB\x03\xe0A\x03\x12{\n%double_click_campaign_manager_setting\x18  \x01(\x0b2G.google.ads.searchads360.v0.resources.DoubleClickCampaignManagerSettingB\x03\xe0A\x03\x12^\n\x0eaccount_status\x18! \x01(\x0e2A.google.ads.searchads360.v0.enums.AccountStatusEnum.AccountStatusB\x03\xe0A\x03\x12\x1f\n\x12last_modified_time\x18" \x01(\tB\x03\xe0A\x03\x12\x16\n\tengine_id\x18# \x01(\tB\x03\xe0A\x03\x12X\n\x06status\x18$ \x01(\x0e2C.google.ads.searchads360.v0.enums.CustomerStatusEnum.CustomerStatusB\x03\xe0A\x03\x12\x1a\n\rcreation_time\x18* \x01(\tB\x03\xe0A\x03\x12\x17\n\nmanager_id\x18/ \x01(\x03B\x03\xe0A\x03\x12%\n\x18manager_descriptive_name\x180 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0esub_manager_id\x181 \x01(\x03B\x03\xe0A\x03\x12)\n\x1csub_manager_descriptive_name\x182 \x01(\tB\x03\xe0A\x03\x12!\n\x14associate_manager_id\x183 \x01(\x03B\x03\xe0A\x03\x12/\n"associate_manager_descriptive_name\x184 \x01(\tB\x03\xe0A\x03\x12c\n\raccount_level\x185 \x01(\x0e2G.google.ads.searchads360.v0.enums.AccountLevelTypeEnum.AccountLevelTypeB\x03\xe0A\x03:B\xeaA?\n$searchads360.googleapis.com/Customer\x12\x17customers/{customer_id}B\x05\n\x03_idB\x13\n\x11_descriptive_nameB\x10\n\x0e_currency_codeB\x0c\n\n_time_zoneB\x18\n\x16_tracking_url_templateB\x13\n\x11_final_url_suffixB\x17\n\x15_auto_tagging_enabledB\n\n\x08_manager"\xc8\x04\n\x19ConversionTrackingSetting\x12(\n\x16conversion_tracking_id\x18\x03 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12A\n/google_ads_cross_account_conversion_tracking_id\x18\x04 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x126\n$cross_account_conversion_tracking_id\x18% \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12)\n\x1caccepted_customer_data_terms\x18\x05 \x01(\x08B\x03\xe0A\x03\x12\x80\x01\n\x1aconversion_tracking_status\x18\x06 \x01(\x0e2W.google.ads.searchads360.v0.enums.ConversionTrackingStatusEnum.ConversionTrackingStatusB\x03\xe0A\x03\x123\n&enhanced_conversions_for_leads_enabled\x18\x07 \x01(\x08B\x03\xe0A\x03\x12+\n\x1egoogle_ads_conversion_customer\x18\x08 \x01(\tB\x03\xe0A\x03B\x19\n\x17_conversion_tracking_idB2\n0_google_ads_cross_account_conversion_tracking_idB\'\n%_cross_account_conversion_tracking_id"p\n!DoubleClickCampaignManagerSetting\x12\x1a\n\radvertiser_id\x18\x01 \x01(\x03B\x03\xe0A\x03\x12\x17\n\nnetwork_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x16\n\ttime_zone\x18\x03 \x01(\tB\x03\xe0A\x03B\x8d\x02\n(com.google.ads.searchads360.v0.resourcesB\rCustomerProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.customer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\rCustomerProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_CUSTOMER'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA&\n$searchads360.googleapis.com/Customer'
    _globals['_CUSTOMER'].fields_by_name['id']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['currency_code']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMER'].fields_by_name['time_zone']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMER'].fields_by_name['manager']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['manager']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['conversion_tracking_setting']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['conversion_tracking_setting']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['account_type']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['account_type']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['double_click_campaign_manager_setting']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['double_click_campaign_manager_setting']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['account_status']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['account_status']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['engine_id']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['engine_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['status']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['creation_time']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['manager_id']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['manager_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['manager_descriptive_name']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['manager_descriptive_name']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['sub_manager_id']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['sub_manager_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['sub_manager_descriptive_name']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['sub_manager_descriptive_name']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['associate_manager_id']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['associate_manager_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['associate_manager_descriptive_name']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['associate_manager_descriptive_name']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['account_level']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['account_level']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER']._loaded_options = None
    _globals['_CUSTOMER']._serialized_options = b'\xeaA?\n$searchads360.googleapis.com/Customer\x12\x17customers/{customer_id}'
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['conversion_tracking_id']._loaded_options = None
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['conversion_tracking_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['google_ads_cross_account_conversion_tracking_id']._loaded_options = None
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['google_ads_cross_account_conversion_tracking_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['cross_account_conversion_tracking_id']._loaded_options = None
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['cross_account_conversion_tracking_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['accepted_customer_data_terms']._loaded_options = None
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['accepted_customer_data_terms']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['conversion_tracking_status']._loaded_options = None
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['conversion_tracking_status']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['enhanced_conversions_for_leads_enabled']._loaded_options = None
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['enhanced_conversions_for_leads_enabled']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['google_ads_conversion_customer']._loaded_options = None
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['google_ads_conversion_customer']._serialized_options = b'\xe0A\x03'
    _globals['_DOUBLECLICKCAMPAIGNMANAGERSETTING'].fields_by_name['advertiser_id']._loaded_options = None
    _globals['_DOUBLECLICKCAMPAIGNMANAGERSETTING'].fields_by_name['advertiser_id']._serialized_options = b'\xe0A\x03'
    _globals['_DOUBLECLICKCAMPAIGNMANAGERSETTING'].fields_by_name['network_id']._loaded_options = None
    _globals['_DOUBLECLICKCAMPAIGNMANAGERSETTING'].fields_by_name['network_id']._serialized_options = b'\xe0A\x03'
    _globals['_DOUBLECLICKCAMPAIGNMANAGERSETTING'].fields_by_name['time_zone']._loaded_options = None
    _globals['_DOUBLECLICKCAMPAIGNMANAGERSETTING'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER']._serialized_start = 444
    _globals['_CUSTOMER']._serialized_end = 1893
    _globals['_CONVERSIONTRACKINGSETTING']._serialized_start = 1896
    _globals['_CONVERSIONTRACKINGSETTING']._serialized_end = 2480
    _globals['_DOUBLECLICKCAMPAIGNMANAGERSETTING']._serialized_start = 2482
    _globals['_DOUBLECLICKCAMPAIGNMANAGERSETTING']._serialized_end = 2594