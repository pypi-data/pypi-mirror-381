"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/conversion.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import asset_field_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_asset__field__type__pb2
from ......google.ads.searchads360.v0.enums import attribution_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_attribution__type__pb2
from ......google.ads.searchads360.v0.enums import conversion_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_conversion__status__pb2
from ......google.ads.searchads360.v0.enums import product_channel_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_product__channel__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/ads/searchads360/v0/resources/conversion.proto\x12$google.ads.searchads360.v0.resources\x1a7google/ads/searchads360/v0/enums/asset_field_type.proto\x1a7google/ads/searchads360/v0/enums/attribution_type.proto\x1a8google/ads/searchads360/v0/enums/conversion_status.proto\x1a6google/ads/searchads360/v0/enums/product_channel.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x8d\x0e\n\nConversion\x12E\n\rresource_name\x18\x01 \x01(\tB.\xe0A\x03\xfaA(\n&searchads360.googleapis.com/Conversion\x12\x14\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1e\n\x0ccriterion_id\x18\x03 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1d\n\x0bmerchant_id\x18\x04 \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12\x17\n\x05ad_id\x18\x05 \x01(\x03B\x03\xe0A\x03H\x03\x88\x01\x01\x12\x1a\n\x08click_id\x18\x06 \x01(\tB\x03\xe0A\x03H\x04\x88\x01\x01\x12\x1a\n\x08visit_id\x18\x07 \x01(\x03B\x03\xe0A\x03H\x05\x88\x01\x01\x12*\n\x18advertiser_conversion_id\x18\x08 \x01(\tB\x03\xe0A\x03H\x06\x88\x01\x01\x12\x1c\n\nproduct_id\x18\t \x01(\tB\x03\xe0A\x03H\x07\x88\x01\x01\x12f\n\x0fproduct_channel\x18\n \x01(\x0e2C.google.ads.searchads360.v0.enums.ProductChannelEnum.ProductChannelB\x03\xe0A\x03H\x08\x88\x01\x01\x12\'\n\x15product_language_code\x18\x0b \x01(\tB\x03\xe0A\x03H\t\x88\x01\x01\x12"\n\x10product_store_id\x18\x0c \x01(\tB\x03\xe0A\x03H\n\x88\x01\x01\x12&\n\x14product_country_code\x18\r \x01(\tB\x03\xe0A\x03H\x0b\x88\x01\x01\x12i\n\x10attribution_type\x18\x0e \x01(\x0e2E.google.ads.searchads360.v0.enums.AttributionTypeEnum.AttributionTypeB\x03\xe0A\x03H\x0c\x88\x01\x01\x12&\n\x14conversion_date_time\x18\x0f \x01(\tB\x03\xe0A\x03H\r\x88\x01\x01\x124\n"conversion_last_modified_date_time\x18\x10 \x01(\tB\x03\xe0A\x03H\x0e\x88\x01\x01\x12,\n\x1aconversion_visit_date_time\x18\x11 \x01(\tB\x03\xe0A\x03H\x0f\x88\x01\x01\x12%\n\x13conversion_quantity\x18\x12 \x01(\x03B\x03\xe0A\x03H\x10\x88\x01\x01\x12+\n\x19conversion_revenue_micros\x18\x13 \x01(\x03B\x03\xe0A\x03H\x11\x88\x01\x01\x12-\n\x1bfloodlight_original_revenue\x18\x14 \x01(\x03B\x03\xe0A\x03H\x12\x88\x01\x01\x12%\n\x13floodlight_order_id\x18\x15 \x01(\tB\x03\xe0A\x03H\x13\x88\x01\x01\x12a\n\x06status\x18\x16 \x01(\x0e2G.google.ads.searchads360.v0.enums.ConversionStatusEnum.ConversionStatusB\x03\xe0A\x03H\x14\x88\x01\x01\x12\x1a\n\x08asset_id\x18\x17 \x01(\x03B\x03\xe0A\x03H\x15\x88\x01\x01\x12g\n\x10asset_field_type\x18\x18 \x01(\x0e2C.google.ads.searchads360.v0.enums.AssetFieldTypeEnum.AssetFieldTypeB\x03\xe0A\x03H\x16\x88\x01\x01:\x7f\xeaA|\n&searchads360.googleapis.com/Conversion\x12Rcustomers/{customer_id}/conversions/{ad_group_id}~{criteria_id}~{ds_conversion_id}B\x05\n\x03_idB\x0f\n\r_criterion_idB\x0e\n\x0c_merchant_idB\x08\n\x06_ad_idB\x0b\n\t_click_idB\x0b\n\t_visit_idB\x1b\n\x19_advertiser_conversion_idB\r\n\x0b_product_idB\x12\n\x10_product_channelB\x18\n\x16_product_language_codeB\x13\n\x11_product_store_idB\x17\n\x15_product_country_codeB\x13\n\x11_attribution_typeB\x17\n\x15_conversion_date_timeB%\n#_conversion_last_modified_date_timeB\x1d\n\x1b_conversion_visit_date_timeB\x16\n\x14_conversion_quantityB\x1c\n\x1a_conversion_revenue_microsB\x1e\n\x1c_floodlight_original_revenueB\x16\n\x14_floodlight_order_idB\t\n\x07_statusB\x0b\n\t_asset_idB\x13\n\x11_asset_field_typeB\x8f\x02\n(com.google.ads.searchads360.v0.resourcesB\x0fConversionProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.conversion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x0fConversionProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_CONVERSION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA(\n&searchads360.googleapis.com/Conversion'
    _globals['_CONVERSION'].fields_by_name['id']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['criterion_id']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['merchant_id']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['merchant_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['ad_id']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['ad_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['click_id']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['click_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['visit_id']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['visit_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['advertiser_conversion_id']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['advertiser_conversion_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['product_id']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['product_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['product_channel']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['product_channel']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['product_language_code']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['product_language_code']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['product_store_id']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['product_store_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['product_country_code']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['product_country_code']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['attribution_type']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['attribution_type']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['conversion_date_time']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['conversion_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['conversion_last_modified_date_time']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['conversion_last_modified_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['conversion_visit_date_time']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['conversion_visit_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['conversion_quantity']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['conversion_quantity']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['conversion_revenue_micros']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['conversion_revenue_micros']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['floodlight_original_revenue']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['floodlight_original_revenue']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['floodlight_order_id']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['floodlight_order_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['status']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['asset_id']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['asset_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION'].fields_by_name['asset_field_type']._loaded_options = None
    _globals['_CONVERSION'].fields_by_name['asset_field_type']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSION']._loaded_options = None
    _globals['_CONVERSION']._serialized_options = b'\xeaA|\n&searchads360.googleapis.com/Conversion\x12Rcustomers/{customer_id}/conversions/{ad_group_id}~{criteria_id}~{ds_conversion_id}'
    _globals['_CONVERSION']._serialized_start = 384
    _globals['_CONVERSION']._serialized_end = 2189