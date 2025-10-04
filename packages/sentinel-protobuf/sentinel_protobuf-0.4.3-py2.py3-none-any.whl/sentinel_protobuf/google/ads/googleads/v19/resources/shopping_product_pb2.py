"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/shopping_product.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import product_availability_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_product__availability__pb2
from ......google.ads.googleads.v19.enums import product_channel_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_product__channel__pb2
from ......google.ads.googleads.v19.enums import product_channel_exclusivity_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_product__channel__exclusivity__pb2
from ......google.ads.googleads.v19.enums import product_condition_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_product__condition__pb2
from ......google.ads.googleads.v19.enums import product_issue_severity_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_product__issue__severity__pb2
from ......google.ads.googleads.v19.enums import product_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_product__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/googleads/v19/resources/shopping_product.proto\x12"google.ads.googleads.v19.resources\x1a9google/ads/googleads/v19/enums/product_availability.proto\x1a4google/ads/googleads/v19/enums/product_channel.proto\x1a@google/ads/googleads/v19/enums/product_channel_exclusivity.proto\x1a6google/ads/googleads/v19/enums/product_condition.proto\x1a;google/ads/googleads/v19/enums/product_issue_severity.proto\x1a3google/ads/googleads/v19/enums/product_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xbf\x17\n\x0fShoppingProduct\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0A\x03\xfaA*\n(googleads.googleapis.com/ShoppingProduct\x12\x1f\n\x12merchant_center_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12W\n\x07channel\x18\x03 \x01(\x0e2A.google.ads.googleads.v19.enums.ProductChannelEnum.ProductChannelB\x03\xe0A\x03\x12\x1a\n\rlanguage_code\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x17\n\nfeed_label\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07item_id\x18\x06 \x01(\tB\x03\xe0A\x03\x12)\n\x17multi_client_account_id\x18\x07 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x17\n\x05title\x18\x08 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x17\n\x05brand\x18\t \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12\x1e\n\x0cprice_micros\x18\n \x01(\x03B\x03\xe0A\x03H\x03\x88\x01\x01\x12\x1f\n\rcurrency_code\x18\x0b \x01(\tB\x03\xe0A\x03H\x04\x88\x01\x01\x12~\n\x13channel_exclusivity\x18\x0c \x01(\x0e2W.google.ads.googleads.v19.enums.ProductChannelExclusivityEnum.ProductChannelExclusivityB\x03\xe0A\x03H\x05\x88\x01\x01\x12b\n\tcondition\x18\r \x01(\x0e2E.google.ads.googleads.v19.enums.ProductConditionEnum.ProductConditionB\x03\xe0A\x03H\x06\x88\x01\x01\x12k\n\x0cavailability\x18\x0e \x01(\x0e2K.google.ads.googleads.v19.enums.ProductAvailabilityEnum.ProductAvailabilityB\x03\xe0A\x03H\x07\x88\x01\x01\x12\x1d\n\x10target_countries\x18\x0f \x03(\tB\x03\xe0A\x03\x12#\n\x11custom_attribute0\x18\x10 \x01(\tB\x03\xe0A\x03H\x08\x88\x01\x01\x12#\n\x11custom_attribute1\x18\x11 \x01(\tB\x03\xe0A\x03H\t\x88\x01\x01\x12#\n\x11custom_attribute2\x18\x12 \x01(\tB\x03\xe0A\x03H\n\x88\x01\x01\x12#\n\x11custom_attribute3\x18\x13 \x01(\tB\x03\xe0A\x03H\x0b\x88\x01\x01\x12#\n\x11custom_attribute4\x18\x14 \x01(\tB\x03\xe0A\x03H\x0c\x88\x01\x01\x12V\n\x0fcategory_level1\x18\x15 \x01(\tB8\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstantH\r\x88\x01\x01\x12V\n\x0fcategory_level2\x18\x16 \x01(\tB8\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstantH\x0e\x88\x01\x01\x12V\n\x0fcategory_level3\x18\x17 \x01(\tB8\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstantH\x0f\x88\x01\x01\x12V\n\x0fcategory_level4\x18\x18 \x01(\tB8\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstantH\x10\x88\x01\x01\x12V\n\x0fcategory_level5\x18\x19 \x01(\tB8\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstantH\x11\x88\x01\x01\x12%\n\x13product_type_level1\x18\x1a \x01(\tB\x03\xe0A\x03H\x12\x88\x01\x01\x12%\n\x13product_type_level2\x18\x1b \x01(\tB\x03\xe0A\x03H\x13\x88\x01\x01\x12%\n\x13product_type_level3\x18\x1c \x01(\tB\x03\xe0A\x03H\x14\x88\x01\x01\x12%\n\x13product_type_level4\x18\x1d \x01(\tB\x03\xe0A\x03H\x15\x88\x01\x01\x12%\n\x13product_type_level5\x18\x1e \x01(\tB\x03\xe0A\x03H\x16\x88\x01\x01\x12*\n\x18effective_max_cpc_micros\x18\x1f \x01(\x03B\x03\xe0A\x03H\x17\x88\x01\x01\x12T\n\x06status\x18  \x01(\x0e2?.google.ads.googleads.v19.enums.ProductStatusEnum.ProductStatusB\x03\xe0A\x03\x12U\n\x06issues\x18! \x03(\x0b2@.google.ads.googleads.v19.resources.ShoppingProduct.ProductIssueB\x03\xe0A\x03\x12@\n\x08campaign\x18" \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/CampaignH\x18\x88\x01\x01\x12?\n\x08ad_group\x18# \x01(\tB(\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroupH\x19\x88\x01\x01\x1a\xb0\x02\n\x0cProductIssue\x12\x17\n\nerror_code\x18\x01 \x01(\tB\x03\xe0A\x03\x12h\n\x0cads_severity\x18\x02 \x01(\x0e2M.google.ads.googleads.v19.enums.ProductIssueSeverityEnum.ProductIssueSeverityB\x03\xe0A\x03\x12 \n\x0eattribute_name\x18\x03 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06detail\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rdocumentation\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10affected_regions\x18\x07 \x03(\tB\x03\xe0A\x03B\x11\n\x0f_attribute_name:\xc1\x01\xeaA\xbd\x01\n(googleads.googleapis.com/ShoppingProduct\x12ncustomers/{customer_id}/shoppingProducts/{merchant_center_id}~{channel}~{language_code}~{feed_label}~{item_id}*\x10shoppingProducts2\x0fshoppingProductB\x1a\n\x18_multi_client_account_idB\x08\n\x06_titleB\x08\n\x06_brandB\x0f\n\r_price_microsB\x10\n\x0e_currency_codeB\x16\n\x14_channel_exclusivityB\x0c\n\n_conditionB\x0f\n\r_availabilityB\x14\n\x12_custom_attribute0B\x14\n\x12_custom_attribute1B\x14\n\x12_custom_attribute2B\x14\n\x12_custom_attribute3B\x14\n\x12_custom_attribute4B\x12\n\x10_category_level1B\x12\n\x10_category_level2B\x12\n\x10_category_level3B\x12\n\x10_category_level4B\x12\n\x10_category_level5B\x16\n\x14_product_type_level1B\x16\n\x14_product_type_level2B\x16\n\x14_product_type_level3B\x16\n\x14_product_type_level4B\x16\n\x14_product_type_level5B\x1b\n\x19_effective_max_cpc_microsB\x0b\n\t_campaignB\x0b\n\t_ad_groupB\x86\x02\n&com.google.ads.googleads.v19.resourcesB\x14ShoppingProductProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.shopping_product_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x14ShoppingProductProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['error_code']._loaded_options = None
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['error_code']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['ads_severity']._loaded_options = None
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['ads_severity']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['attribute_name']._loaded_options = None
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['attribute_name']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['description']._loaded_options = None
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['detail']._loaded_options = None
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['detail']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['documentation']._loaded_options = None
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['documentation']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['affected_regions']._loaded_options = None
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE'].fields_by_name['affected_regions']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA*\n(googleads.googleapis.com/ShoppingProduct'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['merchant_center_id']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['merchant_center_id']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['channel']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['channel']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['language_code']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['language_code']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['feed_label']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['item_id']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['item_id']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['multi_client_account_id']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['multi_client_account_id']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['title']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['title']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['brand']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['brand']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['price_micros']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['price_micros']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['currency_code']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['channel_exclusivity']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['channel_exclusivity']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['condition']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['condition']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['availability']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['availability']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['target_countries']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['target_countries']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['custom_attribute0']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['custom_attribute0']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['custom_attribute1']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['custom_attribute1']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['custom_attribute2']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['custom_attribute2']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['custom_attribute3']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['custom_attribute3']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['custom_attribute4']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['custom_attribute4']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['category_level1']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['category_level1']._serialized_options = b'\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstant'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['category_level2']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['category_level2']._serialized_options = b'\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstant'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['category_level3']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['category_level3']._serialized_options = b'\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstant'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['category_level4']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['category_level4']._serialized_options = b'\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstant'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['category_level5']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['category_level5']._serialized_options = b'\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstant'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['product_type_level1']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['product_type_level1']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['product_type_level2']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['product_type_level2']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['product_type_level3']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['product_type_level3']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['product_type_level4']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['product_type_level4']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['product_type_level5']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['product_type_level5']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['effective_max_cpc_micros']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['effective_max_cpc_micros']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['status']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['issues']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['issues']._serialized_options = b'\xe0A\x03'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['campaign']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_SHOPPINGPRODUCT'].fields_by_name['ad_group']._loaded_options = None
    _globals['_SHOPPINGPRODUCT'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_SHOPPINGPRODUCT']._loaded_options = None
    _globals['_SHOPPINGPRODUCT']._serialized_options = b'\xeaA\xbd\x01\n(googleads.googleapis.com/ShoppingProduct\x12ncustomers/{customer_id}/shoppingProducts/{merchant_center_id}~{channel}~{language_code}~{feed_label}~{item_id}*\x10shoppingProducts2\x0fshoppingProduct'
    _globals['_SHOPPINGPRODUCT']._serialized_start = 507
    _globals['_SHOPPINGPRODUCT']._serialized_end = 3514
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE']._serialized_start = 2491
    _globals['_SHOPPINGPRODUCT_PRODUCTISSUE']._serialized_end = 2795