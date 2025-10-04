"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/search_ads360_field.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import search_ads360_field_category_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_search__ads360__field__category__pb2
from ......google.ads.searchads360.v0.enums import search_ads360_field_data_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_search__ads360__field__data__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/searchads360/v0/resources/search_ads360_field.proto\x12$google.ads.searchads360.v0.resources\x1aCgoogle/ads/searchads360/v0/enums/search_ads360_field_category.proto\x1aDgoogle/ads/searchads360/v0/enums/search_ads360_field_data_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa8\x06\n\x11SearchAds360Field\x12L\n\rresource_name\x18\x01 \x01(\tB5\xe0A\x03\xfaA/\n-searchads360.googleapis.com/SearchAds360Field\x12\x16\n\x04name\x18\x15 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12p\n\x08category\x18\x03 \x01(\x0e2Y.google.ads.searchads360.v0.enums.SearchAds360FieldCategoryEnum.SearchAds360FieldCategoryB\x03\xe0A\x03\x12\x1c\n\nselectable\x18\x16 \x01(\x08B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1c\n\nfilterable\x18\x17 \x01(\x08B\x03\xe0A\x03H\x02\x88\x01\x01\x12\x1a\n\x08sortable\x18\x18 \x01(\x08B\x03\xe0A\x03H\x03\x88\x01\x01\x12\x1c\n\x0fselectable_with\x18\x19 \x03(\tB\x03\xe0A\x03\x12 \n\x13attribute_resources\x18\x1a \x03(\tB\x03\xe0A\x03\x12\x14\n\x07metrics\x18\x1b \x03(\tB\x03\xe0A\x03\x12\x15\n\x08segments\x18\x1c \x03(\tB\x03\xe0A\x03\x12\x18\n\x0benum_values\x18\x1d \x03(\tB\x03\xe0A\x03\x12q\n\tdata_type\x18\x0c \x01(\x0e2Y.google.ads.searchads360.v0.enums.SearchAds360FieldDataTypeEnum.SearchAds360FieldDataTypeB\x03\xe0A\x03\x12\x1a\n\x08type_url\x18\x1e \x01(\tB\x03\xe0A\x03H\x04\x88\x01\x01\x12\x1d\n\x0bis_repeated\x18\x1f \x01(\x08B\x03\xe0A\x03H\x05\x88\x01\x01:]\xeaAZ\n-searchads360.googleapis.com/SearchAds360Field\x12)searchAds360Fields/{search_ads_360_field}B\x07\n\x05_nameB\r\n\x0b_selectableB\r\n\x0b_filterableB\x0b\n\t_sortableB\x0b\n\t_type_urlB\x0e\n\x0c_is_repeatedB\x96\x02\n(com.google.ads.searchads360.v0.resourcesB\x16SearchAds360FieldProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.search_ads360_field_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x16SearchAds360FieldProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_SEARCHADS360FIELD'].fields_by_name['resource_name']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA/\n-searchads360.googleapis.com/SearchAds360Field'
    _globals['_SEARCHADS360FIELD'].fields_by_name['name']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD'].fields_by_name['category']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['category']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD'].fields_by_name['selectable']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['selectable']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD'].fields_by_name['filterable']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['filterable']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD'].fields_by_name['sortable']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['sortable']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD'].fields_by_name['selectable_with']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['selectable_with']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD'].fields_by_name['attribute_resources']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['attribute_resources']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD'].fields_by_name['metrics']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['metrics']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD'].fields_by_name['segments']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['segments']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD'].fields_by_name['enum_values']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['enum_values']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD'].fields_by_name['data_type']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['data_type']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD'].fields_by_name['type_url']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['type_url']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD'].fields_by_name['is_repeated']._loaded_options = None
    _globals['_SEARCHADS360FIELD'].fields_by_name['is_repeated']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHADS360FIELD']._loaded_options = None
    _globals['_SEARCHADS360FIELD']._serialized_options = b'\xeaAZ\n-searchads360.googleapis.com/SearchAds360Field\x12)searchAds360Fields/{search_ads_360_field}'
    _globals['_SEARCHADS360FIELD']._serialized_start = 304
    _globals['_SEARCHADS360FIELD']._serialized_end = 1112