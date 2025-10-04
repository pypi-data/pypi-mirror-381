"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/datamanager/v1/user_data.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/ads/datamanager/v1/user_data.proto\x12\x19google.ads.datamanager.v1\x1a\x1fgoogle/api/field_behavior.proto"T\n\x08UserData\x12H\n\x10user_identifiers\x18\x01 \x03(\x0b2).google.ads.datamanager.v1.UserIdentifierB\x03\xe0A\x02"\x8a\x01\n\x0eUserIdentifier\x12\x17\n\remail_address\x18\x01 \x01(\tH\x00\x12\x16\n\x0cphone_number\x18\x02 \x01(\tH\x00\x129\n\x07address\x18\x03 \x01(\x0b2&.google.ads.datamanager.v1.AddressInfoH\x00B\x0c\n\nidentifier"t\n\x0bAddressInfo\x12\x17\n\ngiven_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bfamily_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bregion_code\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bpostal_code\x18\x04 \x01(\tB\x03\xe0A\x02B\xcd\x01\n\x1dcom.google.ads.datamanager.v1B\rUserDataProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.datamanager.v1.user_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.ads.datamanager.v1B\rUserDataProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1'
    _globals['_USERDATA'].fields_by_name['user_identifiers']._loaded_options = None
    _globals['_USERDATA'].fields_by_name['user_identifiers']._serialized_options = b'\xe0A\x02'
    _globals['_ADDRESSINFO'].fields_by_name['given_name']._loaded_options = None
    _globals['_ADDRESSINFO'].fields_by_name['given_name']._serialized_options = b'\xe0A\x02'
    _globals['_ADDRESSINFO'].fields_by_name['family_name']._loaded_options = None
    _globals['_ADDRESSINFO'].fields_by_name['family_name']._serialized_options = b'\xe0A\x02'
    _globals['_ADDRESSINFO'].fields_by_name['region_code']._loaded_options = None
    _globals['_ADDRESSINFO'].fields_by_name['region_code']._serialized_options = b'\xe0A\x02'
    _globals['_ADDRESSINFO'].fields_by_name['postal_code']._loaded_options = None
    _globals['_ADDRESSINFO'].fields_by_name['postal_code']._serialized_options = b'\xe0A\x02'
    _globals['_USERDATA']._serialized_start = 105
    _globals['_USERDATA']._serialized_end = 189
    _globals['_USERIDENTIFIER']._serialized_start = 192
    _globals['_USERIDENTIFIER']._serialized_end = 330
    _globals['_ADDRESSINFO']._serialized_start = 332
    _globals['_ADDRESSINFO']._serialized_end = 448