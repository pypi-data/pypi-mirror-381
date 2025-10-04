"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/google_ads_field.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import google_ads_field_category_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_google__ads__field__category__pb2
from ......google.ads.googleads.v20.enums import google_ads_field_data_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_google__ads__field__data__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/googleads/v20/resources/google_ads_field.proto\x12"google.ads.googleads.v20.resources\x1a>google/ads/googleads/v20/enums/google_ads_field_category.proto\x1a?google/ads/googleads/v20/enums/google_ads_field_data_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x82\x06\n\x0eGoogleAdsField\x12F\n\rresource_name\x18\x01 \x01(\tB/\xe0A\x03\xfaA)\n\'googleads.googleapis.com/GoogleAdsField\x12\x16\n\x04name\x18\x15 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12h\n\x08category\x18\x03 \x01(\x0e2Q.google.ads.googleads.v20.enums.GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategoryB\x03\xe0A\x03\x12\x1c\n\nselectable\x18\x16 \x01(\x08B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1c\n\nfilterable\x18\x17 \x01(\x08B\x03\xe0A\x03H\x02\x88\x01\x01\x12\x1a\n\x08sortable\x18\x18 \x01(\x08B\x03\xe0A\x03H\x03\x88\x01\x01\x12\x1c\n\x0fselectable_with\x18\x19 \x03(\tB\x03\xe0A\x03\x12 \n\x13attribute_resources\x18\x1a \x03(\tB\x03\xe0A\x03\x12\x14\n\x07metrics\x18\x1b \x03(\tB\x03\xe0A\x03\x12\x15\n\x08segments\x18\x1c \x03(\tB\x03\xe0A\x03\x12\x18\n\x0benum_values\x18\x1d \x03(\tB\x03\xe0A\x03\x12i\n\tdata_type\x18\x0c \x01(\x0e2Q.google.ads.googleads.v20.enums.GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataTypeB\x03\xe0A\x03\x12\x1a\n\x08type_url\x18\x1e \x01(\tB\x03\xe0A\x03H\x04\x88\x01\x01\x12\x1d\n\x0bis_repeated\x18\x1f \x01(\x08B\x03\xe0A\x03H\x05\x88\x01\x01:P\xeaAM\n\'googleads.googleapis.com/GoogleAdsField\x12"googleAdsFields/{google_ads_field}B\x07\n\x05_nameB\r\n\x0b_selectableB\r\n\x0b_filterableB\x0b\n\t_sortableB\x0b\n\t_type_urlB\x0e\n\x0c_is_repeatedB\x85\x02\n&com.google.ads.googleads.v20.resourcesB\x13GoogleAdsFieldProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.google_ads_field_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x13GoogleAdsFieldProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_GOOGLEADSFIELD'].fields_by_name['resource_name']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x03\xfaA)\n'googleads.googleapis.com/GoogleAdsField"
    _globals['_GOOGLEADSFIELD'].fields_by_name['name']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD'].fields_by_name['category']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['category']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD'].fields_by_name['selectable']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['selectable']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD'].fields_by_name['filterable']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['filterable']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD'].fields_by_name['sortable']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['sortable']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD'].fields_by_name['selectable_with']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['selectable_with']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD'].fields_by_name['attribute_resources']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['attribute_resources']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD'].fields_by_name['metrics']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['metrics']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD'].fields_by_name['segments']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['segments']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD'].fields_by_name['enum_values']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['enum_values']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD'].fields_by_name['data_type']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['data_type']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD'].fields_by_name['type_url']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['type_url']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD'].fields_by_name['is_repeated']._loaded_options = None
    _globals['_GOOGLEADSFIELD'].fields_by_name['is_repeated']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEADSFIELD']._loaded_options = None
    _globals['_GOOGLEADSFIELD']._serialized_options = b'\xeaAM\n\'googleads.googleapis.com/GoogleAdsField\x12"googleAdsFields/{google_ads_field}'
    _globals['_GOOGLEADSFIELD']._serialized_start = 287
    _globals['_GOOGLEADSFIELD']._serialized_end = 1057