"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/google_ads_field_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.resources import google_ads_field_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_google__ads__field__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v20/services/google_ads_field_service.proto\x12!google.ads.googleads.v20.services\x1a9google/ads/googleads/v20/resources/google_ads_field.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"b\n\x18GetGoogleAdsFieldRequest\x12F\n\rresource_name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'googleads.googleapis.com/GoogleAdsField"Y\n\x1cSearchGoogleAdsFieldsRequest\x12\x12\n\x05query\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"\x9a\x01\n\x1dSearchGoogleAdsFieldsResponse\x12C\n\x07results\x18\x01 \x03(\x0b22.google.ads.googleads.v20.resources.GoogleAdsField\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x1b\n\x13total_results_count\x18\x03 \x01(\x032\xf2\x03\n\x15GoogleAdsFieldService\x12\xc4\x01\n\x11GetGoogleAdsField\x12;.google.ads.googleads.v20.services.GetGoogleAdsFieldRequest\x1a2.google.ads.googleads.v20.resources.GoogleAdsField">\xdaA\rresource_name\x82\xd3\xe4\x93\x02(\x12&/v20/{resource_name=googleAdsFields/*}\x12\xca\x01\n\x15SearchGoogleAdsFields\x12?.google.ads.googleads.v20.services.SearchGoogleAdsFieldsRequest\x1a@.google.ads.googleads.v20.services.SearchGoogleAdsFieldsResponse".\xdaA\x05query\x82\xd3\xe4\x93\x02 "\x1b/v20/googleAdsFields:search:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x86\x02\n%com.google.ads.googleads.v20.servicesB\x1aGoogleAdsFieldServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.google_ads_field_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x1aGoogleAdsFieldServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_GETGOOGLEADSFIELDREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_GETGOOGLEADSFIELDREQUEST'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x02\xfaA)\n'googleads.googleapis.com/GoogleAdsField"
    _globals['_SEARCHGOOGLEADSFIELDSREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHGOOGLEADSFIELDSREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_GOOGLEADSFIELDSERVICE']._loaded_options = None
    _globals['_GOOGLEADSFIELDSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_GOOGLEADSFIELDSERVICE'].methods_by_name['GetGoogleAdsField']._loaded_options = None
    _globals['_GOOGLEADSFIELDSERVICE'].methods_by_name['GetGoogleAdsField']._serialized_options = b'\xdaA\rresource_name\x82\xd3\xe4\x93\x02(\x12&/v20/{resource_name=googleAdsFields/*}'
    _globals['_GOOGLEADSFIELDSERVICE'].methods_by_name['SearchGoogleAdsFields']._loaded_options = None
    _globals['_GOOGLEADSFIELDSERVICE'].methods_by_name['SearchGoogleAdsFields']._serialized_options = b'\xdaA\x05query\x82\xd3\xe4\x93\x02 "\x1b/v20/googleAdsFields:search:\x01*'
    _globals['_GETGOOGLEADSFIELDREQUEST']._serialized_start = 277
    _globals['_GETGOOGLEADSFIELDREQUEST']._serialized_end = 375
    _globals['_SEARCHGOOGLEADSFIELDSREQUEST']._serialized_start = 377
    _globals['_SEARCHGOOGLEADSFIELDSREQUEST']._serialized_end = 466
    _globals['_SEARCHGOOGLEADSFIELDSRESPONSE']._serialized_start = 469
    _globals['_SEARCHGOOGLEADSFIELDSRESPONSE']._serialized_end = 623
    _globals['_GOOGLEADSFIELDSERVICE']._serialized_start = 626
    _globals['_GOOGLEADSFIELDSERVICE']._serialized_end = 1124