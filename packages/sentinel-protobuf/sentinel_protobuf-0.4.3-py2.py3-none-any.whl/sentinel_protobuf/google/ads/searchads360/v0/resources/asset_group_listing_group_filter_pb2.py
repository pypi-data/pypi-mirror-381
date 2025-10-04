"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/asset_group_listing_group_filter.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import listing_group_filter_bidding_category_level_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_listing__group__filter__bidding__category__level__pb2
from ......google.ads.searchads360.v0.enums import listing_group_filter_custom_attribute_index_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_listing__group__filter__custom__attribute__index__pb2
from ......google.ads.searchads360.v0.enums import listing_group_filter_product_channel_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_listing__group__filter__product__channel__pb2
from ......google.ads.searchads360.v0.enums import listing_group_filter_product_condition_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_listing__group__filter__product__condition__pb2
from ......google.ads.searchads360.v0.enums import listing_group_filter_product_type_level_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_listing__group__filter__product__type__level__pb2
from ......google.ads.searchads360.v0.enums import listing_group_filter_type_enum_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_listing__group__filter__type__enum__pb2
from ......google.ads.searchads360.v0.enums import listing_group_filter_vertical_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_listing__group__filter__vertical__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKgoogle/ads/searchads360/v0/resources/asset_group_listing_group_filter.proto\x12$google.ads.searchads360.v0.resources\x1aRgoogle/ads/searchads360/v0/enums/listing_group_filter_bidding_category_level.proto\x1aRgoogle/ads/searchads360/v0/enums/listing_group_filter_custom_attribute_index.proto\x1aKgoogle/ads/searchads360/v0/enums/listing_group_filter_product_channel.proto\x1aMgoogle/ads/searchads360/v0/enums/listing_group_filter_product_condition.proto\x1aNgoogle/ads/searchads360/v0/enums/listing_group_filter_product_type_level.proto\x1aEgoogle/ads/searchads360/v0/enums/listing_group_filter_type_enum.proto\x1aDgoogle/ads/searchads360/v0/enums/listing_group_filter_vertical.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe4\x06\n\x1cAssetGroupListingGroupFilter\x12W\n\rresource_name\x18\x01 \x01(\tB@\xe0A\x05\xfaA:\n8searchads360.googleapis.com/AssetGroupListingGroupFilter\x12C\n\x0basset_group\x18\x02 \x01(\tB.\xe0A\x05\xfaA(\n&searchads360.googleapis.com/AssetGroup\x12\x0f\n\x02id\x18\x03 \x01(\x03B\x03\xe0A\x03\x12f\n\x04type\x18\x04 \x01(\x0e2S.google.ads.searchads360.v0.enums.ListingGroupFilterTypeEnum.ListingGroupFilterTypeB\x03\xe0A\x05\x12r\n\x08vertical\x18\x05 \x01(\x0e2[.google.ads.searchads360.v0.enums.ListingGroupFilterVerticalEnum.ListingGroupFilterVerticalB\x03\xe0A\x05\x12U\n\ncase_value\x18\x06 \x01(\x0b2A.google.ads.searchads360.v0.resources.ListingGroupFilterDimension\x12e\n\x1bparent_listing_group_filter\x18\x07 \x01(\tB@\xe0A\x05\xfaA:\n8searchads360.googleapis.com/AssetGroupListingGroupFilter\x12X\n\x04path\x18\x08 \x01(\x0b2E.google.ads.searchads360.v0.resources.ListingGroupFilterDimensionPathB\x03\xe0A\x03:\xa0\x01\xeaA\x9c\x01\n8searchads360.googleapis.com/AssetGroupListingGroupFilter\x12`customers/{customer_id}/assetGroupListingGroupFilters/{asset_group_id}~{listing_group_filter_id}"}\n\x1fListingGroupFilterDimensionPath\x12Z\n\ndimensions\x18\x01 \x03(\x0b2A.google.ads.searchads360.v0.resources.ListingGroupFilterDimensionB\x03\xe0A\x03"\xdf\r\n\x1bListingGroupFilterDimension\x12|\n\x18product_bidding_category\x18\x01 \x01(\x0b2X.google.ads.searchads360.v0.resources.ListingGroupFilterDimension.ProductBiddingCategoryH\x00\x12g\n\rproduct_brand\x18\x02 \x01(\x0b2N.google.ads.searchads360.v0.resources.ListingGroupFilterDimension.ProductBrandH\x00\x12k\n\x0fproduct_channel\x18\x03 \x01(\x0b2P.google.ads.searchads360.v0.resources.ListingGroupFilterDimension.ProductChannelH\x00\x12o\n\x11product_condition\x18\x04 \x01(\x0b2R.google.ads.searchads360.v0.resources.ListingGroupFilterDimension.ProductConditionH\x00\x12|\n\x18product_custom_attribute\x18\x05 \x01(\x0b2X.google.ads.searchads360.v0.resources.ListingGroupFilterDimension.ProductCustomAttributeH\x00\x12j\n\x0fproduct_item_id\x18\x06 \x01(\x0b2O.google.ads.searchads360.v0.resources.ListingGroupFilterDimension.ProductItemIdH\x00\x12e\n\x0cproduct_type\x18\x07 \x01(\x0b2M.google.ads.searchads360.v0.resources.ListingGroupFilterDimension.ProductTypeH\x00\x1a\xb5\x01\n\x16ProductBiddingCategory\x12\x0f\n\x02id\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x82\x01\n\x05level\x18\x02 \x01(\x0e2s.google.ads.searchads360.v0.enums.ListingGroupFilterBiddingCategoryLevelEnum.ListingGroupFilterBiddingCategoryLevelB\x05\n\x03_id\x1a,\n\x0cProductBrand\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value\x1a\x8a\x01\n\x0eProductChannel\x12x\n\x07channel\x18\x01 \x01(\x0e2g.google.ads.searchads360.v0.enums.ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel\x1a\x92\x01\n\x10ProductCondition\x12~\n\tcondition\x18\x01 \x01(\x0e2k.google.ads.searchads360.v0.enums.ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition\x1a\xbb\x01\n\x16ProductCustomAttribute\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x82\x01\n\x05index\x18\x02 \x01(\x0e2s.google.ads.searchads360.v0.enums.ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndexB\x08\n\x06_value\x1a-\n\rProductItemId\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value\x1a\xa7\x01\n\x0bProductType\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01\x12z\n\x05level\x18\x02 \x01(\x0e2k.google.ads.searchads360.v0.enums.ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevelB\x08\n\x06_valueB\x0b\n\tdimensionB\xa1\x02\n(com.google.ads.searchads360.v0.resourcesB!AssetGroupListingGroupFilterProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.asset_group_listing_group_filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB!AssetGroupListingGroupFilterProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA:\n8searchads360.googleapis.com/AssetGroupListingGroupFilter'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['asset_group']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['asset_group']._serialized_options = b'\xe0A\x05\xfaA(\n&searchads360.googleapis.com/AssetGroup'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['id']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['type']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['vertical']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['vertical']._serialized_options = b'\xe0A\x05'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['parent_listing_group_filter']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['parent_listing_group_filter']._serialized_options = b'\xe0A\x05\xfaA:\n8searchads360.googleapis.com/AssetGroupListingGroupFilter'
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['path']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER'].fields_by_name['path']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPLISTINGGROUPFILTER']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTER']._serialized_options = b'\xeaA\x9c\x01\n8searchads360.googleapis.com/AssetGroupListingGroupFilter\x12`customers/{customer_id}/assetGroupListingGroupFilters/{asset_group_id}~{listing_group_filter_id}'
    _globals['_LISTINGGROUPFILTERDIMENSIONPATH'].fields_by_name['dimensions']._loaded_options = None
    _globals['_LISTINGGROUPFILTERDIMENSIONPATH'].fields_by_name['dimensions']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPLISTINGGROUPFILTER']._serialized_start = 723
    _globals['_ASSETGROUPLISTINGGROUPFILTER']._serialized_end = 1591
    _globals['_LISTINGGROUPFILTERDIMENSIONPATH']._serialized_start = 1593
    _globals['_LISTINGGROUPFILTERDIMENSIONPATH']._serialized_end = 1718
    _globals['_LISTINGGROUPFILTERDIMENSION']._serialized_start = 1721
    _globals['_LISTINGGROUPFILTERDIMENSION']._serialized_end = 3480
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTBIDDINGCATEGORY']._serialized_start = 2543
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTBIDDINGCATEGORY']._serialized_end = 2724
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTBRAND']._serialized_start = 2726
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTBRAND']._serialized_end = 2770
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCHANNEL']._serialized_start = 2773
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCHANNEL']._serialized_end = 2911
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCONDITION']._serialized_start = 2914
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCONDITION']._serialized_end = 3060
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCUSTOMATTRIBUTE']._serialized_start = 3063
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTCUSTOMATTRIBUTE']._serialized_end = 3250
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTITEMID']._serialized_start = 3252
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTITEMID']._serialized_end = 3297
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTTYPE']._serialized_start = 3300
    _globals['_LISTINGGROUPFILTERDIMENSION_PRODUCTTYPE']._serialized_end = 3467