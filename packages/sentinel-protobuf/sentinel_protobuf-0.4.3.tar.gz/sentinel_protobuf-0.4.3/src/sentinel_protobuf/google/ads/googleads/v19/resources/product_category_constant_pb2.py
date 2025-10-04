"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/product_category_constant.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import product_category_level_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_product__category__level__pb2
from ......google.ads.googleads.v19.enums import product_category_state_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_product__category__state__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/ads/googleads/v19/resources/product_category_constant.proto\x12"google.ads.googleads.v19.resources\x1a;google/ads/googleads/v19/enums/product_category_level.proto\x1a;google/ads/googleads/v19/enums/product_category_state.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd2\x06\n\x17ProductCategoryConstant\x12O\n\rresource_name\x18\x01 \x01(\tB8\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstant\x12\x18\n\x0bcategory_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12g\n product_category_constant_parent\x18\x03 \x01(\tB8\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstantH\x00\x88\x01\x01\x12a\n\x05level\x18\x04 \x01(\x0e2M.google.ads.googleads.v19.enums.ProductCategoryLevelEnum.ProductCategoryLevelB\x03\xe0A\x03\x12a\n\x05state\x18\x05 \x01(\x0e2M.google.ads.googleads.v19.enums.ProductCategoryStateEnum.ProductCategoryStateB\x03\xe0A\x03\x12s\n\rlocalizations\x18\x06 \x03(\x0b2W.google.ads.googleads.v19.resources.ProductCategoryConstant.ProductCategoryLocalizationB\x03\xe0A\x03\x1ag\n\x1bProductCategoryLocalization\x12\x18\n\x0bregion_code\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x12\n\x05value\x18\x03 \x01(\tB\x03\xe0A\x03:\x99\x01\xeaA\x95\x01\n0googleads.googleapis.com/ProductCategoryConstant\x12.productCategoryConstants/{level}~{category_id}*\x18productCategoryConstants2\x17productCategoryConstantB#\n!_product_category_constant_parentB\x8e\x02\n&com.google.ads.googleads.v19.resourcesB\x1cProductCategoryConstantProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.product_category_constant_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x1cProductCategoryConstantProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_PRODUCTCATEGORYCONSTANT_PRODUCTCATEGORYLOCALIZATION'].fields_by_name['region_code']._loaded_options = None
    _globals['_PRODUCTCATEGORYCONSTANT_PRODUCTCATEGORYLOCALIZATION'].fields_by_name['region_code']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTCATEGORYCONSTANT_PRODUCTCATEGORYLOCALIZATION'].fields_by_name['language_code']._loaded_options = None
    _globals['_PRODUCTCATEGORYCONSTANT_PRODUCTCATEGORYLOCALIZATION'].fields_by_name['language_code']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTCATEGORYCONSTANT_PRODUCTCATEGORYLOCALIZATION'].fields_by_name['value']._loaded_options = None
    _globals['_PRODUCTCATEGORYCONSTANT_PRODUCTCATEGORYLOCALIZATION'].fields_by_name['value']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTCATEGORYCONSTANT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_PRODUCTCATEGORYCONSTANT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstant'
    _globals['_PRODUCTCATEGORYCONSTANT'].fields_by_name['category_id']._loaded_options = None
    _globals['_PRODUCTCATEGORYCONSTANT'].fields_by_name['category_id']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTCATEGORYCONSTANT'].fields_by_name['product_category_constant_parent']._loaded_options = None
    _globals['_PRODUCTCATEGORYCONSTANT'].fields_by_name['product_category_constant_parent']._serialized_options = b'\xe0A\x03\xfaA2\n0googleads.googleapis.com/ProductCategoryConstant'
    _globals['_PRODUCTCATEGORYCONSTANT'].fields_by_name['level']._loaded_options = None
    _globals['_PRODUCTCATEGORYCONSTANT'].fields_by_name['level']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTCATEGORYCONSTANT'].fields_by_name['state']._loaded_options = None
    _globals['_PRODUCTCATEGORYCONSTANT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTCATEGORYCONSTANT'].fields_by_name['localizations']._loaded_options = None
    _globals['_PRODUCTCATEGORYCONSTANT'].fields_by_name['localizations']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTCATEGORYCONSTANT']._loaded_options = None
    _globals['_PRODUCTCATEGORYCONSTANT']._serialized_options = b'\xeaA\x95\x01\n0googleads.googleapis.com/ProductCategoryConstant\x12.productCategoryConstants/{level}~{category_id}*\x18productCategoryConstants2\x17productCategoryConstant'
    _globals['_PRODUCTCATEGORYCONSTANT']._serialized_start = 289
    _globals['_PRODUCTCATEGORYCONSTANT']._serialized_end = 1139
    _globals['_PRODUCTCATEGORYCONSTANT_PRODUCTCATEGORYLOCALIZATION']._serialized_start = 843
    _globals['_PRODUCTCATEGORYCONSTANT_PRODUCTCATEGORYLOCALIZATION']._serialized_end = 946