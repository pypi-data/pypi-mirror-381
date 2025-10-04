"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/currency_constant.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v19/resources/currency_constant.proto\x12"google.ads.googleads.v19.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xce\x02\n\x10CurrencyConstant\x12H\n\rresource_name\x18\x01 \x01(\tB1\xe0A\x03\xfaA+\n)googleads.googleapis.com/CurrencyConstant\x12\x16\n\x04code\x18\x06 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x16\n\x04name\x18\x07 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x18\n\x06symbol\x18\x08 \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12&\n\x14billable_unit_micros\x18\t \x01(\x03B\x03\xe0A\x03H\x03\x88\x01\x01:H\xeaAE\n)googleads.googleapis.com/CurrencyConstant\x12\x18currencyConstants/{code}B\x07\n\x05_codeB\x07\n\x05_nameB\t\n\x07_symbolB\x17\n\x15_billable_unit_microsB\x87\x02\n&com.google.ads.googleads.v19.resourcesB\x15CurrencyConstantProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.currency_constant_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x15CurrencyConstantProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_CURRENCYCONSTANT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CURRENCYCONSTANT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA+\n)googleads.googleapis.com/CurrencyConstant'
    _globals['_CURRENCYCONSTANT'].fields_by_name['code']._loaded_options = None
    _globals['_CURRENCYCONSTANT'].fields_by_name['code']._serialized_options = b'\xe0A\x03'
    _globals['_CURRENCYCONSTANT'].fields_by_name['name']._loaded_options = None
    _globals['_CURRENCYCONSTANT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CURRENCYCONSTANT'].fields_by_name['symbol']._loaded_options = None
    _globals['_CURRENCYCONSTANT'].fields_by_name['symbol']._serialized_options = b'\xe0A\x03'
    _globals['_CURRENCYCONSTANT'].fields_by_name['billable_unit_micros']._loaded_options = None
    _globals['_CURRENCYCONSTANT'].fields_by_name['billable_unit_micros']._serialized_options = b'\xe0A\x03'
    _globals['_CURRENCYCONSTANT']._loaded_options = None
    _globals['_CURRENCYCONSTANT']._serialized_options = b'\xeaAE\n)googleads.googleapis.com/CurrencyConstant\x12\x18currencyConstants/{code}'
    _globals['_CURRENCYCONSTANT']._serialized_start = 159
    _globals['_CURRENCYCONSTANT']._serialized_end = 493