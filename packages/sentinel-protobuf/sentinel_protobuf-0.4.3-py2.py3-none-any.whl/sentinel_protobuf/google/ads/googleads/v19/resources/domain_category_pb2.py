"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/domain_category.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v19/resources/domain_category.proto\x12"google.ads.googleads.v19.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x9e\x05\n\x0eDomainCategory\x12F\n\rresource_name\x18\x01 \x01(\tB/\xe0A\x03\xfaA)\n\'googleads.googleapis.com/DomainCategory\x12@\n\x08campaign\x18\n \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/CampaignH\x00\x88\x01\x01\x12\x1a\n\x08category\x18\x0b \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1f\n\rlanguage_code\x18\x0c \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12\x18\n\x06domain\x18\r \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12#\n\x11coverage_fraction\x18\x0e \x01(\x01B\x03\xe0A\x03H\x04\x88\x01\x01\x12\x1f\n\rcategory_rank\x18\x0f \x01(\x03B\x03\xe0A\x03H\x05\x88\x01\x01\x12\x1e\n\x0chas_children\x18\x10 \x01(\x08B\x03\xe0A\x03H\x06\x88\x01\x01\x12,\n\x1arecommended_cpc_bid_micros\x18\x11 \x01(\x03B\x03\xe0A\x03H\x07\x88\x01\x01:\x87\x01\xeaA\x83\x01\n\'googleads.googleapis.com/DomainCategory\x12Xcustomers/{customer_id}/domainCategories/{campaign_id}~{base64_category}~{language_code}B\x0b\n\t_campaignB\x0b\n\t_categoryB\x10\n\x0e_language_codeB\t\n\x07_domainB\x14\n\x12_coverage_fractionB\x10\n\x0e_category_rankB\x0f\n\r_has_childrenB\x1d\n\x1b_recommended_cpc_bid_microsB\x85\x02\n&com.google.ads.googleads.v19.resourcesB\x13DomainCategoryProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.domain_category_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x13DomainCategoryProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_DOMAINCATEGORY'].fields_by_name['resource_name']._loaded_options = None
    _globals['_DOMAINCATEGORY'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x03\xfaA)\n'googleads.googleapis.com/DomainCategory"
    _globals['_DOMAINCATEGORY'].fields_by_name['campaign']._loaded_options = None
    _globals['_DOMAINCATEGORY'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_DOMAINCATEGORY'].fields_by_name['category']._loaded_options = None
    _globals['_DOMAINCATEGORY'].fields_by_name['category']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAINCATEGORY'].fields_by_name['language_code']._loaded_options = None
    _globals['_DOMAINCATEGORY'].fields_by_name['language_code']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAINCATEGORY'].fields_by_name['domain']._loaded_options = None
    _globals['_DOMAINCATEGORY'].fields_by_name['domain']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAINCATEGORY'].fields_by_name['coverage_fraction']._loaded_options = None
    _globals['_DOMAINCATEGORY'].fields_by_name['coverage_fraction']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAINCATEGORY'].fields_by_name['category_rank']._loaded_options = None
    _globals['_DOMAINCATEGORY'].fields_by_name['category_rank']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAINCATEGORY'].fields_by_name['has_children']._loaded_options = None
    _globals['_DOMAINCATEGORY'].fields_by_name['has_children']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAINCATEGORY'].fields_by_name['recommended_cpc_bid_micros']._loaded_options = None
    _globals['_DOMAINCATEGORY'].fields_by_name['recommended_cpc_bid_micros']._serialized_options = b'\xe0A\x03'
    _globals['_DOMAINCATEGORY']._loaded_options = None
    _globals['_DOMAINCATEGORY']._serialized_options = b"\xeaA\x83\x01\n'googleads.googleapis.com/DomainCategory\x12Xcustomers/{customer_id}/domainCategories/{campaign_id}~{base64_category}~{language_code}"
    _globals['_DOMAINCATEGORY']._serialized_start = 157
    _globals['_DOMAINCATEGORY']._serialized_end = 827