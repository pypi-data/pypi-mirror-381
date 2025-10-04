"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/keyword_theme_constant_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.resources import keyword_theme_constant_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_keyword__theme__constant__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/ads/googleads/v19/services/keyword_theme_constant_service.proto\x12!google.ads.googleads.v19.services\x1a?google/ads/googleads/v19/resources/keyword_theme_constant.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto"f\n#SuggestKeywordThemeConstantsRequest\x12\x12\n\nquery_text\x18\x01 \x01(\t\x12\x14\n\x0ccountry_code\x18\x02 \x01(\t\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"\x81\x01\n$SuggestKeywordThemeConstantsResponse\x12Y\n\x17keyword_theme_constants\x18\x01 \x03(\x0b28.google.ads.googleads.v19.resources.KeywordThemeConstant2\xc5\x02\n\x1bKeywordThemeConstantService\x12\xde\x01\n\x1cSuggestKeywordThemeConstants\x12F.google.ads.googleads.v19.services.SuggestKeywordThemeConstantsRequest\x1aG.google.ads.googleads.v19.services.SuggestKeywordThemeConstantsResponse"-\x82\xd3\xe4\x93\x02\'""/v19/keywordThemeConstants:suggest:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8c\x02\n%com.google.ads.googleads.v19.servicesB KeywordThemeConstantServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.keyword_theme_constant_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB KeywordThemeConstantServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_KEYWORDTHEMECONSTANTSERVICE']._loaded_options = None
    _globals['_KEYWORDTHEMECONSTANTSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_KEYWORDTHEMECONSTANTSERVICE'].methods_by_name['SuggestKeywordThemeConstants']._loaded_options = None
    _globals['_KEYWORDTHEMECONSTANTSERVICE'].methods_by_name['SuggestKeywordThemeConstants']._serialized_options = b'\x82\xd3\xe4\x93\x02\'""/v19/keywordThemeConstants:suggest:\x01*'
    _globals['_SUGGESTKEYWORDTHEMECONSTANTSREQUEST']._serialized_start = 229
    _globals['_SUGGESTKEYWORDTHEMECONSTANTSREQUEST']._serialized_end = 331
    _globals['_SUGGESTKEYWORDTHEMECONSTANTSRESPONSE']._serialized_start = 334
    _globals['_SUGGESTKEYWORDTHEMECONSTANTSRESPONSE']._serialized_end = 463
    _globals['_KEYWORDTHEMECONSTANTSERVICE']._serialized_start = 466
    _globals['_KEYWORDTHEMECONSTANTSERVICE']._serialized_end = 791