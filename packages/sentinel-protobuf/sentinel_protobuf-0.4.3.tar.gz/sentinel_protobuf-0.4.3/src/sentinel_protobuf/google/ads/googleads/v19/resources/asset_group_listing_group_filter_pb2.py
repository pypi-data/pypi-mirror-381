"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/asset_group_listing_group_filter.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import listing_group_filter_custom_attribute_index_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_listing__group__filter__custom__attribute__index__pb2
from ......google.ads.googleads.v19.enums import listing_group_filter_listing_source_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_listing__group__filter__listing__source__pb2
from ......google.ads.googleads.v19.enums import listing_group_filter_product_category_level_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_listing__group__filter__product__category__level__pb2
from ......google.ads.googleads.v19.enums import listing_group_filter_product_channel_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_listing__group__filter__product__channel__pb2
from ......google.ads.googleads.v19.enums import listing_group_filter_product_condition_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_listing__group__filter__product__condition__pb2
from ......google.ads.googleads.v19.enums import listing_group_filter_product_type_level_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_listing__group__filter__product__type__level__pb2
from ......google.ads.googleads.v19.enums import listing_group_filter_type_enum_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_listing__group__filter__type__enum__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nIgoogle/ads/googleads/v19/resources/asset_group_listing_group_filter.proto\x12"google.ads.googleads.v19.resources\x1aPgoogle/ads/googleads/v19/enums/listing_group_filter_custom_attribute_index.proto\x1aHgoogle/ads/googleads/v19/enums/listing_group_filter_listing_source.proto\x1aPgoogle/ads/googleads/v19/enums/listing_group_filter_product_category_level.proto\x1aIgoogle/ads/googleads/v19/enums/listing_group_filter_product_channel.proto\x1aKgoogle/ads/googleads/v19/enums/listing_group_filter_product_condition.proto\x1aLgoogle/ads/googleads/v19/enums/listing_group_filter_product_type_level.proto\x1aCgoogle/ads/googleads/v19/enums/listing_group_filter_type_enum.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe1\x06\n\x1cAssetGroupListingGroupFilter\x12T\n\rresource_name\x18\x01 \x01(\tB=\xe0A\x05\xfaA7\n5googleads.googleapis.com/AssetGroupListingGroupFilter\x12@\n\x0basset_group\x18\x02 \x01(\tB+\xe0A\x05\xfaA%\n#googleads.googleapis.com/AssetGroup\x12\x0f\n\x02id\x18\x03 \x01(\x03B\x03\xe0A\x03\x12d\n\x04type\x18\x04 \x01(\x0e2Q.google.ads.googleads.v19.enums.ListingGroupFilterTypeEnum.ListingGroupFilterTypeB\x03\xe0A\x05\x12\x80\x01\n\x0elisting_source\x18\t \x01(\x0e2c.google.ads.googleads.v19.enums.ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSourceB\x03\xe0A\x05\x12S\n\ncase_value\x18\x06 \x01(\x0b2?.google.ads.googleads.v19.resources.ListingGroupFilterDimension\x12b\n\x1bparent_listing_group_filter\x18\x07 \x01(\tB=\xe0A\x05\xfaA7\n5googleads.googleapis.com/AssetGroupListingGroupFilter\x12V\n\x04path\x18\x08 \x01(\x0b2C.google.ads.googleads.v19.resources.ListingGroupFilterDimensionPathB\x03\xe0A\x03:\x9d\x01\xeaA\x99\x01\n5googleads.googleapis.com/AssetGroupListingGroupFilter\x12`customers/{customer_id}/assetGroupListingGroupFilters/{asset_group_id}~{listing_group_filter_id}"{\n\x1fListingGroupFilterDimensionPath\x12X\n\ndimensions\x18\x01 \x03(\x0b2?.google.ads.googleads.v19.resources.ListingGroupFilterDimensionB\x03\xe0A\x03"\xe1\x0f\n\x1bListingGroupFilterDimension\x12k\n\x10product_category\x18\n \x01(\x0b2O.google.ads.googleads.v19.resources.ListingGroupFilterDimension.ProductCategoryH\x00\x12e\n\rproduct_brand\x18\x02 \x01(\x0b2L.google.ads.googleads.v19.resources.ListingGroupFilterDimension.ProductBrandH\x00\x12i\n\x0fproduct_channel\x18\x03 \x01(\x0b2N.google.ads.googleads.v19.resources.ListingGroupFilterDimension.ProductChannelH\x00\x12m\n\x11product_condition\x18\x04 \x01(\x0b2P.google.ads.googleads.v19.resources.ListingGroupFilterDimension.ProductConditionH\x00\x12z\n\x18product_custom_attribute\x18\x05 \x01(\x0b2V.google.ads.googleads.v19.resources.ListingGroupFilterDimension.ProductCustomAttributeH\x00\x12h\n\x0fproduct_item_id\x18\x06 \x01(\x0b2M.google.ads.googleads.v19.resources.ListingGroupFilterDimension.ProductItemIdH\x00\x12c\n\x0cproduct_type\x18\x07 \x01(\x0b2K.google.ads.googleads.v19.resources.ListingGroupFilterDimension.ProductTypeH\x00\x12Z\n\x07webpage\x18\t \x01(\x0b2G.google.ads.googleads.v19.resources.ListingGroupFilterDimension.WebpageH\x00\x1a\xbe\x01\n\x0fProductCategory\x12\x18\n\x0bcategory_id\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x80\x01\n\x05level\x18\x02 \x01(\x0e2q.google.ads.googleads.v19.enums.ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevelB\x0e\n\x0c_category_id\x1a,\n\x0cProductBrand\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value\x1a\x88\x01\n\x0eProductChannel\x12v\n\x07channel\x18\x01 \x01(\x0e2e.google.ads.googleads.v19.enums.ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel\x1a\x90\x01\n\x10ProductCondition\x12|\n\tcondition\x18\x01 \x01(\x0e2i.google.ads.googleads.v19.enums.ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition\x1a\xb9\x01\n\x16ProductCustomAttribute\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x80\x01\n\x05index\x18\x02 \x01(\x0e2q.google.ads.googleads.v19.enums.ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndexB\x08\n\x06_value\x1a-\n\rProductItemId\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value\x1a\xa5\x01\n\x0bProductType\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01\x12x\n\x05level\x18\x02 \x01(\x0e2i.google.ads.googleads.v19.enums.ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevelB\x08\n\x06_value\x1ao\n\x07Webpage\x12d\n\nconditions\x18\x01 \x03(\x0b2P.google.ads.googleads.v19.resources.ListingGroupFilterDimension.WebpageCondition\x1aO\n\x10WebpageCondition\x12\x16\n\x0ccustom_label\x18\x01 \x01(\tH\x00\x12\x16\n\x0curl_contains\x18\x02 \x01(\tH\x00B\x0b\n\tconditionB\x0b\n\tdimensionB\x93\x02\n&com.google.ads.googleads.v19.resourcesB!AssetGroupListingGroupFilterProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.asset_group_listing_group_filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB!AssetGroupListingGroupFilterProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA7\n5googleads.googleapis.com/AssetGroupListingGroupFilter'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['asset_group']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['asset_group']._serialized_options = b'\xe0A\x05\xfaA%\n#googleads.googleapis.com/AssetGroup'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['id']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['type']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['listing_source']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['listing_source']._serialized_options = b'\xe0A\x05'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['parent_listing_group_filter']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['parent_listing_group_filter']._serialized_options = b'\xe0A\x05\xfaA7\n5googleads.googleapis.com/AssetGroupListingGroupFilter'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['path']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['path']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPLISTINGGROUPFILTER']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER']._serialized_options = b'\xeaA\x99\x01\n5googleads.googleapis.com/AssetGroupListingGroupFilter\x12`customers/{customer_id}/assetGroupListingGroupFilters/{asset_group_id}~{listing_group_filter_id}'
    _globals['_LISTINGGROUPFILTERDIMENSIONPATH'].fields_by_name['dimensions']._loaded_options = None
    _globals['_LISTINGGROUPFILTERDIMENSIONPATH'].fields_by_name['dimensions']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPLISTINGGROUPFILTER']._serialized_start = 711
    _globals['_ASSETGROUPLISTINGGROUPFILTER']._serialized_end = 1576
    _globals['_LISTINGGROUPFILTERDIMENSIONPATH']._serialized_start = 1578
    _globals['_LISTINGGROUPFILTERDIMENSIONPATH']._serialized_end = 1701
    _globals['_LISTINGGROUPFILTERDIMENSION']._serialized_start = 1704
    _globals['_LISTINGGROUPFILTERDIMENSION']._serialized_end = 3721
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCATEGORY']._serialized_start = 2589
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCATEGORY']._serialized_end = 2779
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTBRAND']._serialized_start = 2781
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTBRAND']._serialized_end = 2825
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCHANNEL']._serialized_start = 2828
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCHANNEL']._serialized_end = 2964
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCONDITION']._serialized_start = 2967
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCONDITION']._serialized_end = 3111
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCUSTOMATTRIBUTE']._serialized_start = 3114
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCUSTOMATTRIBUTE']._serialized_end = 3299
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTITEMID']._serialized_start = 3301
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTITEMID']._serialized_end = 3346
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTTYPE']._serialized_start = 3349
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTTYPE']._serialized_end = 3514
    _globals['_LISTINGGROUPFILTERDIMENSION_WEBPAGE']._serialized_start = 3516
    _globals['_LISTINGGROUPFILTERDIMENSION_WEBPAGE']._serialized_end = 3627
    _globals['_LISTINGGROUPFILTERDIMENSION_WEBPAGECONDITION']._serialized_start = 3629
    _globals['_LISTINGGROUPFILTERDIMENSION_WEBPAGECONDITION']._serialized_end = 3708