"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/conversion_action.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import attribution_model_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_attribution__model__pb2
from ......google.ads.searchads360.v0.enums import conversion_action_category_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_conversion__action__category__pb2
from ......google.ads.searchads360.v0.enums import conversion_action_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_conversion__action__status__pb2
from ......google.ads.searchads360.v0.enums import conversion_action_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_conversion__action__type__pb2
from ......google.ads.searchads360.v0.enums import data_driven_model_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_data__driven__model__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/searchads360/v0/resources/conversion_action.proto\x12$google.ads.searchads360.v0.resources\x1a8google/ads/searchads360/v0/enums/attribution_model.proto\x1aAgoogle/ads/searchads360/v0/enums/conversion_action_category.proto\x1a?google/ads/searchads360/v0/enums/conversion_action_status.proto\x1a=google/ads/searchads360/v0/enums/conversion_action_type.proto\x1a?google/ads/searchads360/v0/enums/data_driven_model_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x8d\x0f\n\x10ConversionAction\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x05\xfaA.\n,searchads360.googleapis.com/ConversionAction\x12\x14\n\x02id\x18\x15 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x16 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\rcreation_time\x18! \x01(\tB\x03\xe0A\x03\x12c\n\x06status\x18\x04 \x01(\x0e2S.google.ads.searchads360.v0.enums.ConversionActionStatusEnum.ConversionActionStatus\x12b\n\x04type\x18\x05 \x01(\x0e2O.google.ads.searchads360.v0.enums.ConversionActionTypeEnum.ConversionActionTypeB\x03\xe0A\x05\x12\x1d\n\x10primary_for_goal\x18\x1f \x01(\x08H\x02\x88\x01\x01\x12i\n\x08category\x18\x06 \x01(\x0e2W.google.ads.searchads360.v0.enums.ConversionActionCategoryEnum.ConversionActionCategory\x12I\n\x0eowner_customer\x18\x17 \x01(\tB,\xe0A\x03\xfaA&\n$searchads360.googleapis.com/CustomerH\x03\x88\x01\x01\x129\n,include_in_client_account_conversions_metric\x18\x18 \x01(\x08H\x04\x88\x01\x01\x12/\n\x1dinclude_in_conversions_metric\x18  \x01(\x08B\x03\xe0A\x03H\x05\x88\x01\x01\x12/\n"click_through_lookback_window_days\x18\x19 \x01(\x03H\x06\x88\x01\x01\x12\\\n\x0evalue_settings\x18\x0b \x01(\x0b2D.google.ads.searchads360.v0.resources.ConversionAction.ValueSettings\x12s\n\x1aattribution_model_settings\x18\r \x01(\x0b2O.google.ads.searchads360.v0.resources.ConversionAction.AttributionModelSettings\x12\x13\n\x06app_id\x18\x1c \x01(\tH\x07\x88\x01\x01\x12k\n\x13floodlight_settings\x18\x1d \x01(\x0b2I.google.ads.searchads360.v0.resources.ConversionAction.FloodlightSettingsB\x03\xe0A\x03\x1a\xf8\x01\n\x18AttributionModelSettings\x12b\n\x11attribution_model\x18\x01 \x01(\x0e2G.google.ads.searchads360.v0.enums.AttributionModelEnum.AttributionModel\x12x\n\x18data_driven_model_status\x18\x02 \x01(\x0e2Q.google.ads.searchads360.v0.enums.DataDrivenModelStatusEnum.DataDrivenModelStatusB\x03\xe0A\x03\x1a\xbf\x01\n\rValueSettings\x12\x1a\n\rdefault_value\x18\x04 \x01(\x01H\x00\x88\x01\x01\x12"\n\x15default_currency_code\x18\x05 \x01(\tH\x01\x88\x01\x01\x12%\n\x18always_use_default_value\x18\x06 \x01(\x08H\x02\x88\x01\x01B\x10\n\x0e_default_valueB\x18\n\x16_default_currency_codeB\x1b\n\x19_always_use_default_value\x1aj\n\x12FloodlightSettings\x12\x1f\n\x12activity_group_tag\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cactivity_tag\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bactivity_id\x18\x03 \x01(\x03B\x03\xe0A\x03:q\xeaAn\n,searchads360.googleapis.com/ConversionAction\x12>customers/{customer_id}/conversionActions/{conversion_type_id}B\x05\n\x03_idB\x07\n\x05_nameB\x13\n\x11_primary_for_goalB\x11\n\x0f_owner_customerB/\n-_include_in_client_account_conversions_metricB \n\x1e_include_in_conversions_metricB%\n#_click_through_lookback_window_daysB\t\n\x07_app_idB\x95\x02\n(com.google.ads.searchads360.v0.resourcesB\x15ConversionActionProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.conversion_action_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x15ConversionActionProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS'].fields_by_name['data_driven_model_status']._loaded_options = None
    _globals['_CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS'].fields_by_name['data_driven_model_status']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION_FLOODLIGHTSETTINGS'].fields_by_name['activity_group_tag']._loaded_options = None
    _globals['_CONVERSIONACTION_FLOODLIGHTSETTINGS'].fields_by_name['activity_group_tag']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION_FLOODLIGHTSETTINGS'].fields_by_name['activity_tag']._loaded_options = None
    _globals['_CONVERSIONACTION_FLOODLIGHTSETTINGS'].fields_by_name['activity_tag']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION_FLOODLIGHTSETTINGS'].fields_by_name['activity_id']._loaded_options = None
    _globals['_CONVERSIONACTION_FLOODLIGHTSETTINGS'].fields_by_name['activity_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA.\n,searchads360.googleapis.com/ConversionAction'
    _globals['_CONVERSIONACTION'].fields_by_name['id']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION'].fields_by_name['creation_time']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION'].fields_by_name['type']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_CONVERSIONACTION'].fields_by_name['owner_customer']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['owner_customer']._serialized_options = b'\xe0A\x03\xfaA&\n$searchads360.googleapis.com/Customer'
    _globals['_CONVERSIONACTION'].fields_by_name['include_in_conversions_metric']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['include_in_conversions_metric']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION'].fields_by_name['floodlight_settings']._loaded_options = None
    _globals['_CONVERSIONACTION'].fields_by_name['floodlight_settings']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONACTION']._loaded_options = None
    _globals['_CONVERSIONACTION']._serialized_options = b'\xeaAn\n,searchads360.googleapis.com/ConversionAction\x12>customers/{customer_id}/conversionActions/{conversion_type_id}'
    _globals['_CONVERSIONACTION']._serialized_start = 481
    _globals['_CONVERSIONACTION']._serialized_end = 2414
    _globals['_CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS']._serialized_start = 1560
    _globals['_CONVERSIONACTION_ATTRIBUTIONMODELSETTINGS']._serialized_end = 1808
    _globals['_CONVERSIONACTION_VALUESETTINGS']._serialized_start = 1811
    _globals['_CONVERSIONACTION_VALUESETTINGS']._serialized_end = 2002
    _globals['_CONVERSIONACTION_FLOODLIGHTSETTINGS']._serialized_start = 2004
    _globals['_CONVERSIONACTION_FLOODLIGHTSETTINGS']._serialized_end = 2110