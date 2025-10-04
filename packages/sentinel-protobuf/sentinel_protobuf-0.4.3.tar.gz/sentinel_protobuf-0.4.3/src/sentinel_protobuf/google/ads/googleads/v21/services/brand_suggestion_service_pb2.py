"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/brand_suggestion_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import brand_state_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_brand__state__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v21/services/brand_suggestion_service.proto\x12!google.ads.googleads.v21.services\x1a0google/ads/googleads/v21/enums/brand_state.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"\x7f\n\x14SuggestBrandsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x0cbrand_prefix\x18\x02 \x01(\tB\x03\xe0A\x02H\x00\x88\x01\x01\x12\x1c\n\x0fselected_brands\x18\x03 \x03(\tB\x03\xe0A\x01B\x0f\n\r_brand_prefix"[\n\x15SuggestBrandsResponse\x12B\n\x06brands\x18\x01 \x03(\x0b22.google.ads.googleads.v21.services.BrandSuggestion"\x83\x01\n\x0fBrandSuggestion\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04urls\x18\x03 \x03(\t\x12H\n\x05state\x18\x04 \x01(\x0e29.google.ads.googleads.v21.enums.BrandStateEnum.BrandState2\xb8\x02\n\x16BrandSuggestionService\x12\xd6\x01\n\rSuggestBrands\x127.google.ads.googleads.v21.services.SuggestBrandsRequest\x1a8.google.ads.googleads.v21.services.SuggestBrandsResponse"R\xdaA\x18customer_id,brand_prefix\x82\xd3\xe4\x93\x021",/v21/customers/{customer_id=*}:suggestBrands:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x87\x02\n%com.google.ads.googleads.v21.servicesB\x1bBrandSuggestionServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.brand_suggestion_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x1bBrandSuggestionServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_SUGGESTBRANDSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_SUGGESTBRANDSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_SUGGESTBRANDSREQUEST'].fields_by_name['brand_prefix']._loaded_options = None
    _globals['_SUGGESTBRANDSREQUEST'].fields_by_name['brand_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_SUGGESTBRANDSREQUEST'].fields_by_name['selected_brands']._loaded_options = None
    _globals['_SUGGESTBRANDSREQUEST'].fields_by_name['selected_brands']._serialized_options = b'\xe0A\x01'
    _globals['_BRANDSUGGESTIONSERVICE']._loaded_options = None
    _globals['_BRANDSUGGESTIONSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_BRANDSUGGESTIONSERVICE'].methods_by_name['SuggestBrands']._loaded_options = None
    _globals['_BRANDSUGGESTIONSERVICE'].methods_by_name['SuggestBrands']._serialized_options = b'\xdaA\x18customer_id,brand_prefix\x82\xd3\xe4\x93\x021",/v21/customers/{customer_id=*}:suggestBrands:\x01*'
    _globals['_SUGGESTBRANDSREQUEST']._serialized_start = 241
    _globals['_SUGGESTBRANDSREQUEST']._serialized_end = 368
    _globals['_SUGGESTBRANDSRESPONSE']._serialized_start = 370
    _globals['_SUGGESTBRANDSRESPONSE']._serialized_end = 461
    _globals['_BRANDSUGGESTION']._serialized_start = 464
    _globals['_BRANDSUGGESTION']._serialized_end = 595
    _globals['_BRANDSUGGESTIONSERVICE']._serialized_start = 598
    _globals['_BRANDSUGGESTIONSERVICE']._serialized_end = 910