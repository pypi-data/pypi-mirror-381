"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/customer.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import brand_safety_suitability_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_brand__safety__suitability__pb2
from ......google.ads.googleads.v20.enums import conversion_tracking_status_enum_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_conversion__tracking__status__enum__pb2
from ......google.ads.googleads.v20.enums import customer_pay_per_conversion_eligibility_failure_reason_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_customer__pay__per__conversion__eligibility__failure__reason__pb2
from ......google.ads.googleads.v20.enums import customer_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_customer__status__pb2
from ......google.ads.googleads.v20.enums import local_services_verification_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_local__services__verification__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ads/googleads/v20/resources/customer.proto\x12"google.ads.googleads.v20.resources\x1a=google/ads/googleads/v20/enums/brand_safety_suitability.proto\x1aDgoogle/ads/googleads/v20/enums/conversion_tracking_status_enum.proto\x1a[google/ads/googleads/v20/enums/customer_pay_per_conversion_eligibility_failure_reason.proto\x1a4google/ads/googleads/v20/enums/customer_status.proto\x1aGgoogle/ads/googleads/v20/enums/local_services_verification_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf2\x0f\n\x08Customer\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/Customer\x12\x14\n\x02id\x18\x13 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1d\n\x10descriptive_name\x18\x14 \x01(\tH\x01\x88\x01\x01\x12\x1f\n\rcurrency_code\x18\x15 \x01(\tB\x03\xe0A\x05H\x02\x88\x01\x01\x12\x1b\n\ttime_zone\x18\x16 \x01(\tB\x03\xe0A\x05H\x03\x88\x01\x01\x12"\n\x15tracking_url_template\x18\x17 \x01(\tH\x04\x88\x01\x01\x12\x1d\n\x10final_url_suffix\x18\x18 \x01(\tH\x05\x88\x01\x01\x12!\n\x14auto_tagging_enabled\x18\x19 \x01(\x08H\x06\x88\x01\x01\x12$\n\x12has_partners_badge\x18\x1a \x01(\x08B\x03\xe0A\x03H\x07\x88\x01\x01\x12\x19\n\x07manager\x18\x1b \x01(\x08B\x03\xe0A\x03H\x08\x88\x01\x01\x12\x1e\n\x0ctest_account\x18\x1c \x01(\x08B\x03\xe0A\x03H\t\x88\x01\x01\x12X\n\x16call_reporting_setting\x18\n \x01(\x0b28.google.ads.googleads.v20.resources.CallReportingSetting\x12b\n\x1bconversion_tracking_setting\x18\x0e \x01(\x0b2=.google.ads.googleads.v20.resources.ConversionTrackingSetting\x12X\n\x13remarketing_setting\x18\x0f \x01(\x0b26.google.ads.googleads.v20.resources.RemarketingSettingB\x03\xe0A\x03\x12\xc3\x01\n.pay_per_conversion_eligibility_failure_reasons\x18\x10 \x03(\x0e2\x85\x01.google.ads.googleads.v20.enums.CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonB\x03\xe0A\x03\x12$\n\x12optimization_score\x18\x1d \x01(\x01B\x03\xe0A\x03H\n\x88\x01\x01\x12&\n\x19optimization_score_weight\x18\x1e \x01(\x01B\x03\xe0A\x03\x12V\n\x06status\x18$ \x01(\x0e2A.google.ads.googleads.v20.enums.CustomerStatusEnum.CustomerStatusB\x03\xe0A\x03\x124\n"location_asset_auto_migration_done\x18& \x01(\x08B\x03\xe0A\x03H\x0b\x88\x01\x01\x121\n\x1fimage_asset_auto_migration_done\x18\' \x01(\x08B\x03\xe0A\x03H\x0c\x88\x01\x01\x12>\n,location_asset_auto_migration_done_date_time\x18( \x01(\tB\x03\xe0A\x03H\r\x88\x01\x01\x12;\n)image_asset_auto_migration_done_date_time\x18) \x01(\tB\x03\xe0A\x03H\x0e\x88\x01\x01\x12e\n\x1acustomer_agreement_setting\x18, \x01(\x0b2<.google.ads.googleads.v20.resources.CustomerAgreementSettingB\x03\xe0A\x03\x12_\n\x17local_services_settings\x18- \x01(\x0b29.google.ads.googleads.v20.resources.LocalServicesSettingsB\x03\xe0A\x03\x12~\n\x1evideo_brand_safety_suitability\x18. \x01(\x0e2Q.google.ads.googleads.v20.enums.BrandSafetySuitabilityEnum.BrandSafetySuitabilityB\x03\xe0A\x03:?\xeaA<\n!googleads.googleapis.com/Customer\x12\x17customers/{customer_id}B\x05\n\x03_idB\x13\n\x11_descriptive_nameB\x10\n\x0e_currency_codeB\x0c\n\n_time_zoneB\x18\n\x16_tracking_url_templateB\x13\n\x11_final_url_suffixB\x17\n\x15_auto_tagging_enabledB\x15\n\x13_has_partners_badgeB\n\n\x08_managerB\x0f\n\r_test_accountB\x15\n\x13_optimization_scoreB%\n#_location_asset_auto_migration_doneB"\n _image_asset_auto_migration_doneB/\n-_location_asset_auto_migration_done_date_timeB,\n*_image_asset_auto_migration_done_date_time"\x9c\x02\n\x14CallReportingSetting\x12#\n\x16call_reporting_enabled\x18\n \x01(\x08H\x00\x88\x01\x01\x12.\n!call_conversion_reporting_enabled\x18\x0b \x01(\x08H\x01\x88\x01\x01\x12S\n\x16call_conversion_action\x18\x0c \x01(\tB.\xfaA+\n)googleads.googleapis.com/ConversionActionH\x02\x88\x01\x01B\x19\n\x17_call_reporting_enabledB$\n"_call_conversion_reporting_enabledB\x19\n\x17_call_conversion_action"\xc9\x03\n\x19ConversionTrackingSetting\x12(\n\x16conversion_tracking_id\x18\x03 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x126\n$cross_account_conversion_tracking_id\x18\x04 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12)\n\x1caccepted_customer_data_terms\x18\x05 \x01(\x08B\x03\xe0A\x03\x12~\n\x1aconversion_tracking_status\x18\x06 \x01(\x0e2U.google.ads.googleads.v20.enums.ConversionTrackingStatusEnum.ConversionTrackingStatusB\x03\xe0A\x03\x123\n&enhanced_conversions_for_leads_enabled\x18\x07 \x01(\x08B\x03\xe0A\x03\x12&\n\x1egoogle_ads_conversion_customer\x18\x08 \x01(\tB\x19\n\x17_conversion_tracking_idB\'\n%_cross_account_conversion_tracking_id"Y\n\x12RemarketingSetting\x12(\n\x16google_global_site_tag\x18\x02 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01B\x19\n\x17_google_global_site_tag"A\n\x18CustomerAgreementSetting\x12%\n\x18accepted_lead_form_terms\x18\x01 \x01(\x08B\x03\xe0A\x03"\xe1\x01\n\x15LocalServicesSettings\x12a\n\x19granular_license_statuses\x18\x01 \x03(\x0b29.google.ads.googleads.v20.resources.GranularLicenseStatusB\x03\xe0A\x03\x12e\n\x1bgranular_insurance_statuses\x18\x02 \x03(\x0b2;.google.ads.googleads.v20.resources.GranularInsuranceStatusB\x03\xe0A\x03"\xa4\x02\n\x15GranularLicenseStatus\x12"\n\x10geo_criterion_id\x18\x01 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1d\n\x0bcategory_id\x18\x02 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x8a\x01\n\x13verification_status\x18\x03 \x01(\x0e2c.google.ads.googleads.v20.enums.LocalServicesVerificationStatusEnum.LocalServicesVerificationStatusB\x03\xe0A\x03H\x02\x88\x01\x01B\x13\n\x11_geo_criterion_idB\x0e\n\x0c_category_idB\x16\n\x14_verification_status"\xa6\x02\n\x17GranularInsuranceStatus\x12"\n\x10geo_criterion_id\x18\x01 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1d\n\x0bcategory_id\x18\x02 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x8a\x01\n\x13verification_status\x18\x03 \x01(\x0e2c.google.ads.googleads.v20.enums.LocalServicesVerificationStatusEnum.LocalServicesVerificationStatusB\x03\xe0A\x03H\x02\x88\x01\x01B\x13\n\x11_geo_criterion_idB\x0e\n\x0c_category_idB\x16\n\x14_verification_statusB\xff\x01\n&com.google.ads.googleads.v20.resourcesB\rCustomerProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.customer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\rCustomerProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_CUSTOMER'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_CUSTOMER'].fields_by_name['id']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['currency_code']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMER'].fields_by_name['time_zone']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x05'
    _globals['_CUSTOMER'].fields_by_name['has_partners_badge']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['has_partners_badge']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['manager']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['manager']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['test_account']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['test_account']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['remarketing_setting']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['remarketing_setting']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['pay_per_conversion_eligibility_failure_reasons']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['pay_per_conversion_eligibility_failure_reasons']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['optimization_score']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['optimization_score']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['optimization_score_weight']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['optimization_score_weight']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['status']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['location_asset_auto_migration_done']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['location_asset_auto_migration_done']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['image_asset_auto_migration_done']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['image_asset_auto_migration_done']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['location_asset_auto_migration_done_date_time']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['location_asset_auto_migration_done_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['image_asset_auto_migration_done_date_time']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['image_asset_auto_migration_done_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['customer_agreement_setting']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['customer_agreement_setting']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['local_services_settings']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['local_services_settings']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER'].fields_by_name['video_brand_safety_suitability']._loaded_options = None
    _globals['_CUSTOMER'].fields_by_name['video_brand_safety_suitability']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER']._loaded_options = None
    _globals['_CUSTOMER']._serialized_options = b'\xeaA<\n!googleads.googleapis.com/Customer\x12\x17customers/{customer_id}'
    _globals['_CALLREPORTINGSETTING'].fields_by_name['call_conversion_action']._loaded_options = None
    _globals['_CALLREPORTINGSETTING'].fields_by_name['call_conversion_action']._serialized_options = b'\xfaA+\n)googleads.googleapis.com/ConversionAction'
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['conversion_tracking_id']._loaded_options = None
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['conversion_tracking_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['cross_account_conversion_tracking_id']._loaded_options = None
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['cross_account_conversion_tracking_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['accepted_customer_data_terms']._loaded_options = None
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['accepted_customer_data_terms']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['conversion_tracking_status']._loaded_options = None
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['conversion_tracking_status']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['enhanced_conversions_for_leads_enabled']._loaded_options = None
    _globals['_CONVERSIONTRACKINGSETTING'].fields_by_name['enhanced_conversions_for_leads_enabled']._serialized_options = b'\xe0A\x03'
    _globals['_REMARKETINGSETTING'].fields_by_name['google_global_site_tag']._loaded_options = None
    _globals['_REMARKETINGSETTING'].fields_by_name['google_global_site_tag']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERAGREEMENTSETTING'].fields_by_name['accepted_lead_form_terms']._loaded_options = None
    _globals['_CUSTOMERAGREEMENTSETTING'].fields_by_name['accepted_lead_form_terms']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESSETTINGS'].fields_by_name['granular_license_statuses']._loaded_options = None
    _globals['_LOCALSERVICESSETTINGS'].fields_by_name['granular_license_statuses']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESSETTINGS'].fields_by_name['granular_insurance_statuses']._loaded_options = None
    _globals['_LOCALSERVICESSETTINGS'].fields_by_name['granular_insurance_statuses']._serialized_options = b'\xe0A\x03'
    _globals['_GRANULARLICENSESTATUS'].fields_by_name['geo_criterion_id']._loaded_options = None
    _globals['_GRANULARLICENSESTATUS'].fields_by_name['geo_criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_GRANULARLICENSESTATUS'].fields_by_name['category_id']._loaded_options = None
    _globals['_GRANULARLICENSESTATUS'].fields_by_name['category_id']._serialized_options = b'\xe0A\x03'
    _globals['_GRANULARLICENSESTATUS'].fields_by_name['verification_status']._loaded_options = None
    _globals['_GRANULARLICENSESTATUS'].fields_by_name['verification_status']._serialized_options = b'\xe0A\x03'
    _globals['_GRANULARINSURANCESTATUS'].fields_by_name['geo_criterion_id']._loaded_options = None
    _globals['_GRANULARINSURANCESTATUS'].fields_by_name['geo_criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_GRANULARINSURANCESTATUS'].fields_by_name['category_id']._loaded_options = None
    _globals['_GRANULARINSURANCESTATUS'].fields_by_name['category_id']._serialized_options = b'\xe0A\x03'
    _globals['_GRANULARINSURANCESTATUS'].fields_by_name['verification_status']._loaded_options = None
    _globals['_GRANULARINSURANCESTATUS'].fields_by_name['verification_status']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMER']._serialized_start = 503
    _globals['_CUSTOMER']._serialized_end = 2537
    _globals['_CALLREPORTINGSETTING']._serialized_start = 2540
    _globals['_CALLREPORTINGSETTING']._serialized_end = 2824
    _globals['_CONVERSIONTRACKINGSETTING']._serialized_start = 2827
    _globals['_CONVERSIONTRACKINGSETTING']._serialized_end = 3284
    _globals['_REMARKETINGSETTING']._serialized_start = 3286
    _globals['_REMARKETINGSETTING']._serialized_end = 3375
    _globals['_CUSTOMERAGREEMENTSETTING']._serialized_start = 3377
    _globals['_CUSTOMERAGREEMENTSETTING']._serialized_end = 3442
    _globals['_LOCALSERVICESSETTINGS']._serialized_start = 3445
    _globals['_LOCALSERVICESSETTINGS']._serialized_end = 3670
    _globals['_GRANULARLICENSESTATUS']._serialized_start = 3673
    _globals['_GRANULARLICENSESTATUS']._serialized_end = 3965
    _globals['_GRANULARINSURANCESTATUS']._serialized_start = 3968
    _globals['_GRANULARINSURANCESTATUS']._serialized_end = 4262