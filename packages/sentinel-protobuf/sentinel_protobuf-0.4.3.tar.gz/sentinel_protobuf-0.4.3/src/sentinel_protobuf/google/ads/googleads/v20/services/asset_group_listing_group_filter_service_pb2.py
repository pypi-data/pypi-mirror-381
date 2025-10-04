"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/asset_group_listing_group_filter_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v20.resources import asset_group_listing_group_filter_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_asset__group__listing__group__filter__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nPgoogle/ads/googleads/v20/services/asset_group_listing_group_filter_service.proto\x12!google.ads.googleads.v20.services\x1a:google/ads/googleads/v20/enums/response_content_type.proto\x1aIgoogle/ads/googleads/v20/resources/asset_group_listing_group_filter.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xac\x02\n*MutateAssetGroupListingGroupFiltersRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12a\n\noperations\x18\x02 \x03(\x0b2H.google.ads.googleads.v20.services.AssetGroupListingGroupFilterOperationB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08\x12j\n\x15response_content_type\x18\x04 \x01(\x0e2K.google.ads.googleads.v20.enums.ResponseContentTypeEnum.ResponseContentType"\xdb\x02\n%AssetGroupListingGroupFilterOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12R\n\x06create\x18\x01 \x01(\x0b2@.google.ads.googleads.v20.resources.AssetGroupListingGroupFilterH\x00\x12R\n\x06update\x18\x02 \x01(\x0b2@.google.ads.googleads.v20.resources.AssetGroupListingGroupFilterH\x00\x12L\n\x06remove\x18\x03 \x01(\tB:\xfaA7\n5googleads.googleapis.com/AssetGroupListingGroupFilterH\x00B\x0b\n\toperation"\x8b\x01\n+MutateAssetGroupListingGroupFiltersResponse\x12\\\n\x07results\x18\x01 \x03(\x0b2K.google.ads.googleads.v20.services.MutateAssetGroupListingGroupFilterResult"\xe9\x01\n(MutateAssetGroupListingGroupFilterResult\x12Q\n\rresource_name\x18\x01 \x01(\tB:\xfaA7\n5googleads.googleapis.com/AssetGroupListingGroupFilter\x12j\n asset_group_listing_group_filter\x18\x02 \x01(\x0b2@.google.ads.googleads.v20.resources.AssetGroupListingGroupFilter2\x9c\x03\n#AssetGroupListingGroupFilterService\x12\xad\x02\n#MutateAssetGroupListingGroupFilters\x12M.google.ads.googleads.v20.services.MutateAssetGroupListingGroupFiltersRequest\x1aN.google.ads.googleads.v20.services.MutateAssetGroupListingGroupFiltersResponse"g\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02H"C/v20/customers/{customer_id=*}/assetGroupListingGroupFilters:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x94\x02\n%com.google.ads.googleads.v20.servicesB(AssetGroupListingGroupFilterServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.asset_group_listing_group_filter_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB(AssetGroupListingGroupFilterServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATEASSETGROUPLISTINGGROUPFILTERSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEASSETGROUPLISTINGGROUPFILTERSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEASSETGROUPLISTINGGROUPFILTERSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEASSETGROUPLISTINGGROUPFILTERSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_ASSETGROUPLISTINGGROUPFILTEROPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTEROPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA7\n5googleads.googleapis.com/AssetGroupListingGroupFilter'
    _globals['_MUTATEASSETGROUPLISTINGGROUPFILTERRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEASSETGROUPLISTINGGROUPFILTERRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA7\n5googleads.googleapis.com/AssetGroupListingGroupFilter'
    _globals['_ASSETGROUPLISTINGGROUPFILTERSERVICE']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTERSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_ASSETGROUPLISTINGGROUPFILTERSERVICE'].methods_by_name['MutateAssetGroupListingGroupFilters']._loaded_options = None
    _globals['_ASSETGROUPLISTINGGROUPFILTERSERVICE'].methods_by_name['MutateAssetGroupListingGroupFilters']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02H"C/v20/customers/{customer_id=*}/assetGroupListingGroupFilters:mutate:\x01*'
    _globals['_MUTATEASSETGROUPLISTINGGROUPFILTERSREQUEST']._serialized_start = 404
    _globals['_MUTATEASSETGROUPLISTINGGROUPFILTERSREQUEST']._serialized_end = 704
    _globals['_ASSETGROUPLISTINGGROUPFILTEROPERATION']._serialized_start = 707
    _globals['_ASSETGROUPLISTINGGROUPFILTEROPERATION']._serialized_end = 1054
    _globals['_MUTATEASSETGROUPLISTINGGROUPFILTERSRESPONSE']._serialized_start = 1057
    _globals['_MUTATEASSETGROUPLISTINGGROUPFILTERSRESPONSE']._serialized_end = 1196
    _globals['_MUTATEASSETGROUPLISTINGGROUPFILTERRESULT']._serialized_start = 1199
    _globals['_MUTATEASSETGROUPLISTINGGROUPFILTERRESULT']._serialized_end = 1432
    _globals['_ASSETGROUPLISTINGGROUPFILTERSERVICE']._serialized_start = 1435
    _globals['_ASSETGROUPLISTINGGROUPFILTERSERVICE']._serialized_end = 1847