"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/services/search_ads360_field_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.resources import search_ads360_field_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_resources_dot_search__ads360__field__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/ads/searchads360/v0/services/search_ads360_field_service.proto\x12#google.ads.searchads360.v0.services\x1a>google/ads/searchads360/v0/resources/search_ads360_field.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"k\n\x1bGetSearchAds360FieldRequest\x12L\n\rresource_name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-searchads360.googleapis.com/SearchAds360Field"\\\n\x1fSearchSearchAds360FieldsRequest\x12\x12\n\x05query\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"\xa2\x01\n SearchSearchAds360FieldsResponse\x12H\n\x07results\x18\x01 \x03(\x0b27.google.ads.searchads360.v0.resources.SearchAds360Field\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x1b\n\x13total_results_count\x18\x03 \x01(\x032\xa0\x04\n\x18SearchAds360FieldService\x12\xd3\x01\n\x14GetSearchAds360Field\x12@.google.ads.searchads360.v0.services.GetSearchAds360FieldRequest\x1a7.google.ads.searchads360.v0.resources.SearchAds360Field"@\xdaA\rresource_name\x82\xd3\xe4\x93\x02*\x12(/v0/{resource_name=searchAds360Fields/*}\x12\xd9\x01\n\x18SearchSearchAds360Fields\x12D.google.ads.searchads360.v0.services.SearchSearchAds360FieldsRequest\x1aE.google.ads.searchads360.v0.services.SearchSearchAds360FieldsResponse"0\xdaA\x05query\x82\xd3\xe4\x93\x02""\x1d/v0/searchAds360Fields:search:\x01*\x1aR\xcaA\x1bsearchads360.googleapis.com\xd2A1https://www.googleapis.com/auth/doubleclicksearchB\x97\x02\n\'com.google.ads.searchads360.v0.servicesB\x1dSearchAds360FieldServiceProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/services;services\xa2\x02\x07GASA360\xaa\x02#Google.Ads.SearchAds360.V0.Services\xca\x02#Google\\Ads\\SearchAds360\\V0\\Services\xea\x02\'Google::Ads::SearchAds360::V0::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.services.search_ads360_field_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.ads.searchads360.v0.servicesB\x1dSearchAds360FieldServiceProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/services;services\xa2\x02\x07GASA360\xaa\x02#Google.Ads.SearchAds360.V0.Services\xca\x02#Google\\Ads\\SearchAds360\\V0\\Services\xea\x02'Google::Ads::SearchAds360::V0::Services"
    _globals['_GETSEARCHADS360FIELDREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_GETSEARCHADS360FIELDREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA/\n-searchads360.googleapis.com/SearchAds360Field'
    _globals['_SEARCHSEARCHADS360FIELDSREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHSEARCHADS360FIELDSREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHADS360FIELDSERVICE']._loaded_options = None
    _globals['_SEARCHADS360FIELDSERVICE']._serialized_options = b'\xcaA\x1bsearchads360.googleapis.com\xd2A1https://www.googleapis.com/auth/doubleclicksearch'
    _globals['_SEARCHADS360FIELDSERVICE'].methods_by_name['GetSearchAds360Field']._loaded_options = None
    _globals['_SEARCHADS360FIELDSERVICE'].methods_by_name['GetSearchAds360Field']._serialized_options = b'\xdaA\rresource_name\x82\xd3\xe4\x93\x02*\x12(/v0/{resource_name=searchAds360Fields/*}'
    _globals['_SEARCHADS360FIELDSERVICE'].methods_by_name['SearchSearchAds360Fields']._loaded_options = None
    _globals['_SEARCHADS360FIELDSERVICE'].methods_by_name['SearchSearchAds360Fields']._serialized_options = b'\xdaA\x05query\x82\xd3\xe4\x93\x02""\x1d/v0/searchAds360Fields:search:\x01*'
    _globals['_GETSEARCHADS360FIELDREQUEST']._serialized_start = 289
    _globals['_GETSEARCHADS360FIELDREQUEST']._serialized_end = 396
    _globals['_SEARCHSEARCHADS360FIELDSREQUEST']._serialized_start = 398
    _globals['_SEARCHSEARCHADS360FIELDSREQUEST']._serialized_end = 490
    _globals['_SEARCHSEARCHADS360FIELDSRESPONSE']._serialized_start = 493
    _globals['_SEARCHSEARCHADS360FIELDSRESPONSE']._serialized_end = 655
    _globals['_SEARCHADS360FIELDSERVICE']._serialized_start = 658
    _globals['_SEARCHADS360FIELDSERVICE']._serialized_end = 1202