"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/conversion_action.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import tag_snippet_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_tag__snippet__pb2
from ......google.ads.googleads.v21.enums import attribution_model_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_attribution__model__pb2
from ......google.ads.googleads.v21.enums import conversion_action_category_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_conversion__action__category__pb2
from ......google.ads.googleads.v21.enums import conversion_action_counting_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_conversion__action__counting__type__pb2
from ......google.ads.googleads.v21.enums import conversion_action_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_conversion__action__status__pb2
from ......google.ads.googleads.v21.enums import conversion_action_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_conversion__action__type__pb2
from ......google.ads.googleads.v21.enums import conversion_origin_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_conversion__origin__pb2
from ......google.ads.googleads.v21.enums import data_driven_model_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_data__driven__model__status__pb2
from ......google.ads.googleads.v21.enums import mobile_app_vendor_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_mobile__app__vendor__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v21/resources/conversion_action.proto\x12"google.ads.googleads.v21.resources\x1a1google/ads/googleads/v21/common/tag_snippet.proto\x1a6google/ads/googleads/v21/enums/attribution_model.proto\x1a?google/ads/googleads/v21/enums/conversion_action_category.proto\x1aDgoogle/ads/googleads/v21/enums/conversion_action_counting_type.proto\x1a=google/ads/googleads/v21/enums/conversion_action_status.proto\x1a;google/ads/googleads/v21/enums/conversion_action_type.proto\x1a6google/ads/googleads/v21/enums/conversion_origin.proto\x1a=google/ads/googleads/v21/enums/data_driven_model_status.proto\x1a6google/ads/googleads/v21/enums/mobile_app_vendor.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x93\x16\n\x10ConversionAction\x12H\n\rresource_name\x18\x01 \x01(\tB1\xe0A\x05\xfaA+\n)googleads.googleapis.com/ConversionAction\x12\x14\n\x02id\x18\x15 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x16 \x01(\tH\x01\x88\x01\x01\x12a\n\x06status\x18\x04 \x01(\x0e2Q.google.ads.googleads.v21.enums.ConversionActionStatusEnum.ConversionActionStatus\x12`\n\x04type\x18\x05 \x01(\x0e2M.google.ads.googleads.v21.enums.ConversionActionTypeEnum.ConversionActionTypeB\x03\xe0A\x05\x12Z\n\x06origin\x18\x1e \x01(\x0e2E.google.ads.googleads.v21.enums.ConversionOriginEnum.ConversionOriginB\x03\xe0A\x03\x12\x1d\n\x10primary_for_goal\x18\x1f \x01(\x08H\x02\x88\x01\x01\x12g\n\x08category\x18\x06 \x01(\x0e2U.google.ads.googleads.v21.enums.ConversionActionCategoryEnum.ConversionActionCategory\x12F\n\x0eowner_customer\x18\x17 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/CustomerH\x03\x88\x01\x01\x12*\n\x1dinclude_in_conversions_metric\x18\x18 \x01(\x08H\x04\x88\x01\x01\x12/\n"click_through_lookback_window_days\x18\x19 \x01(\x03H\x05\x88\x01\x01\x12.\n!view_through_lookback_window_days\x18\x1a \x01(\x03H\x06\x88\x01\x01\x12Z\n\x0evalue_settings\x18\x0b \x01(\x0b2B.google.ads.googleads.v21.resources.ConversionAction.ValueSettings\x12t\n\rcounting_type\x18\x0c \x01(\x0e2].google.ads.googleads.v21.enums.ConversionActionCountingTypeEnum.ConversionActionCountingType\x12q\n\x1aattribution_model_settings\x18\r \x01(\x0b2M.google.ads.googleads.v21.resources.ConversionAction.AttributionModelSettings\x12F\n\x0ctag_snippets\x18\x0e \x03(\x0b2+.google.ads.googleads.v21.common.TagSnippetB\x03\xe0A\x03\x12(\n\x1bphone_call_duration_seconds\x18\x1b \x01(\x03H\x07\x88\x01\x01\x12\x13\n\x06app_id\x18\x1c \x01(\tH\x08\x88\x01\x01\x12c\n\x11mobile_app_vendor\x18\x11 \x01(\x0e2C.google.ads.googleads.v21.enums.MobileAppVendorEnum.MobileAppVendorB\x03\xe0A\x03\x12e\n\x11firebase_settings\x18\x12 \x01(\x0b2E.google.ads.googleads.v21.resources.ConversionAction.FirebaseSettingsB\x03\xe0A\x03\x12\x84\x01\n"third_party_app_analytics_settings\x18\x13 \x01(\x0b2S.google.ads.googleads.v21.resources.ConversionAction.ThirdPartyAppAnalyticsSettingsB\x03\xe0A\x03\x12w\n\x1bgoogle_analytics_4_settings\x18" \x01(\x0b2M.google.ads.googleads.v21.resources.ConversionAction.GoogleAnalytics4SettingsB\x03\xe0A\x03\x1a\xf4\x01\n\x18AttributionModelSettings\x12`\n\x11attribution_model\x18\x01 \x01(\x0e2E.google.ads.googleads.v21.enums.AttributionModelEnum.AttributionModel\x12v\n\x18data_driven_model_status\x18\x02 \x01(\x0e2O.google.ads.googleads.v21.enums.DataDrivenModelStatusEnum.DataDrivenModelStatusB\x03\xe0A\x03\x1a\xbf\x01\n\rValueSettings\x12\x1a\n\rdefault_value\x18\x04 \x01(\x01H\x00\x88\x01\x01\x12"\n\x15default_currency_code\x18\x05 \x01(\tH\x01\x88\x01\x01\x12%\n\x18always_use_default_value\x18\x06 \x01(\x08H\x02\x88\x01\x01B\x10\n\x0e_default_valueB\x18\n\x16_default_currency_codeB\x1b\n\x19_always_use_default_value\x1ai\n\x1eThirdPartyAppAnalyticsSettings\x12\x1c\n\nevent_name\x18\x02 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1a\n\rprovider_name\x18\x03 \x01(\tB\x03\xe0A\x03B\r\n\x0b_event_name\x1a\xa2\x01\n\x10FirebaseSettings\x12\x1c\n\nevent_name\x18\x03 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1c\n\nproject_id\x18\x04 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x18\n\x0bproperty_id\x18\x05 \x01(\x03B\x03\xe0A\x03\x12\x1a\n\rproperty_name\x18\x06 \x01(\tB\x03\xe0A\x03B\r\n\x0b_event_nameB\r\n\x0b_project_id\x1ai\n\x18GoogleAnalytics4Settings\x12\x17\n\nevent_name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rproperty_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bproperty_id\x18\x03 \x01(\x03B\x03\xe0A\x03:p\xeaAm\n)googleads.googleapis.com/ConversionAction\x12@customers/{customer_id}/conversionActions/{conversion_action_id}B\x05\n\x03_idB\x07\n\x05_nameB\x13\n\x11_primary_for_goalB\x11\n\x0f_owner_customerB \n\x1e_include_in_conversions_metricB%\n#_click_through_lookback_window_daysB$\n"_view_through_lookback_window_daysB\x1e\n\x1c_phone_call_duration_secondsB\t\n\x07_app_idB\x87\x02\n&com.google.ads.googleads.v21.resourcesB\x15ConversionActionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.conversion_action_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x15ConversionActionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS'].fields_by_name['data_driven_model_status']._loaded_options = None
    _globals['_CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS'].fields_by_name['data_driven_model_status']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS'].fields_by_name['event_name']._loaded_options = None
    _globals['_CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS'].fields_by_name['event_name']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS'].fields_by_name['provider_name']._loaded_options = None
    _globals['_CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS'].fields_by_name['provider_name']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION_FIREBASESETTINGS'].fields_by_name['event_name']._loaded_options = None
    _globals['_CONVERSIONACTION_FIREBASESETTINGS'].fields_by_name['event_name']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION_FIREBASESETTINGS'].fields_by_name['project_id']._loaded_options = None
    _globals['_CONVERSIONACTION_FIREBASESETTINGS'].fields_by_name['project_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION_FIREBASESETTINGS'].fields_by_name['property_id']._loaded_options = None
    _globals['_CONVERSIONACTION_FIREBASESETTINGS'].fields_by_name['property_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION_FIREBASESETTINGS'].fields_by_name['property_name']._loaded_options = None
    _globals['_CONVERSIONACTION_FIREBASESETTINGS'].fields_by_name['property_name']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION_GOOGLEANALYTICS4SETTINGS'].fields_by_name['event_name']._loaded_options = None
    _globals['_CONVERSIONACTION_GOOGLEANALYTICS4SETTINGS'].fields_by_name['event_name']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION_GOOGLEANALYTICS4SETTINGS'].fields_by_name['property_name']._loaded_options = None
    _globals['_CONVERSIONACTION_GOOGLEANALYTICS4SETTINGS'].fields_by_name['property_name']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION_GOOGLEANALYTICS4SETTINGS'].fields_by_name['property_id']._loaded_options = None
    _globals['_CONVERSIONACTION_GOOGLEANALYTICS4SETTINGS'].fields_by_name['property_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA+\n)googleads.googleapis.com/ConversionAction'
    _globals['_CONVERSIONACTION'].fields_by_name['id']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION'].fields_by_name['type']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_CONVERSIONACTION'].fields_by_name['origin']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['origin']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION'].fields_by_name['owner_customer']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['owner_customer']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_CONVERSIONACTION'].fields_by_name['tag_snippets']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['tag_snippets']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION'].fields_by_name['mobile_app_vendor']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['mobile_app_vendor']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION'].fields_by_name['firebase_settings']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['firebase_settings']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION'].fields_by_name['third_party_app_analytics_settings']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['third_party_app_analytics_settings']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION'].fields_by_name['google_analytics_4_settings']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['google_analytics_4_settings']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION']._loaded_options = None
    _globals['_CONVERSIONACTION']._serialized_options = b'\xeaAm\n)googleads.googleapis.com/ConversionAction\x12@customers/{customer_id}/conversionActions/{conversion_action_id}'
    _globals['_CONVERSIONACTION']._serialized_start = 700
    _globals['_CONVERSIONACTION']._serialized_end = 3535
    _globals['_CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS']._serialized_start = 2394
    _globals['_CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS']._serialized_end = 2638
    _globals['_CONVERSIONACTION_VALUESETTINGS']._serialized_start = 2641
    _globals['_CONVERSIONACTION_VALUESETTINGS']._serialized_end = 2832
    _globals['_CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS']._serialized_start = 2834
    _globals['_CONVERSIONACTION_THIRDPARTYAPPANALYTICSSETTINGS']._serialized_end = 2939
    _globals['_CONVERSIONACTION_FIREBASESETTINGS']._serialized_start = 2942
    _globals['_CONVERSIONACTION_FIREBASESETTINGS']._serialized_end = 3104
    _globals['_CONVERSIONACTION_GOOGLEANALYTICS4SETTINGS']._serialized_start = 3106
    _globals['_CONVERSIONACTION_GOOGLEANALYTICS4SETTINGS']._serialized_end = 3211