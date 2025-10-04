"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/product_bidding_category_constant.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import product_bidding_category_level_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_product__bidding__category__level__pb2
from ......google.ads.searchads360.v0.enums import product_bidding_category_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_product__bidding__category__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLgoogle/ads/searchads360/v0/resources/product_bidding_category_constant.proto\x12$google.ads.searchads360.v0.resources\x1aEgoogle/ads/searchads360/v0/enums/product_bidding_category_level.proto\x1aFgoogle/ads/searchads360/v0/enums/product_bidding_category_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xcf\x06\n\x1eProductBiddingCategoryConstant\x12Y\n\rresource_name\x18\x01 \x01(\tBB\xe0A\x03\xfaA<\n:searchads360.googleapis.com/ProductBiddingCategoryConstant\x12\x14\n\x02id\x18\n \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1e\n\x0ccountry_code\x18\x0b \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12y\n(product_bidding_category_constant_parent\x18\x0c \x01(\tBB\xe0A\x03\xfaA<\n:searchads360.googleapis.com/ProductBiddingCategoryConstantH\x02\x88\x01\x01\x12q\n\x05level\x18\x05 \x01(\x0e2].google.ads.searchads360.v0.enums.ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevelB\x03\xe0A\x03\x12t\n\x06status\x18\x06 \x01(\x0e2_.google.ads.searchads360.v0.enums.ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatusB\x03\xe0A\x03\x12\x1f\n\rlanguage_code\x18\r \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12 \n\x0elocalized_name\x18\x0e \x01(\tB\x03\xe0A\x03H\x04\x88\x01\x01:\x8a\x01\xeaA\x86\x01\n:searchads360.googleapis.com/ProductBiddingCategoryConstant\x12HproductBiddingCategoryConstants/{country_code}~{level}~{canonical_value}B\x05\n\x03_idB\x0f\n\r_country_codeB+\n)_product_bidding_category_constant_parentB\x10\n\x0e_language_codeB\x11\n\x0f_localized_nameB\xa3\x02\n(com.google.ads.searchads360.v0.resourcesB#ProductBiddingCategoryConstantProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.product_bidding_category_constant_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB#ProductBiddingCategoryConstantProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA<\n:searchads360.googleapis.com/ProductBiddingCategoryConstant'
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['id']._loaded_options = None
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['country_code']._loaded_options = None
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['country_code']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['product_bidding_category_constant_parent']._loaded_options = None
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['product_bidding_category_constant_parent']._serialized_options = b'\xe0A\x03\xfaA<\n:searchads360.googleapis.com/ProductBiddingCategoryConstant'
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['level']._loaded_options = None
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['level']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['status']._loaded_options = None
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['language_code']._loaded_options = None
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['language_code']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['localized_name']._loaded_options = None
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT'].fields_by_name['localized_name']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT']._loaded_options = None
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT']._serialized_options = b'\xeaA\x86\x01\n:searchads360.googleapis.com/ProductBiddingCategoryConstant\x12HproductBiddingCategoryConstants/{country_code}~{level}~{canonical_value}'
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT']._serialized_start = 322
    _globals['_PRODUCTBIDDINGCATEGORYCONSTANT']._serialized_end = 1169