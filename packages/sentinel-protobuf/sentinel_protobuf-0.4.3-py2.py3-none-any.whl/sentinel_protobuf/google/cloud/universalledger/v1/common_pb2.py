"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/universalledger/v1/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/universalledger/v1/common.proto\x12\x1fgoogle.cloud.universalledger.v1\x1a\x1fgoogle/api/field_behavior.proto"\x19\n\x06Entity\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x03"#\n\rCurrencyValue\x12\x12\n\x05value\x18\x01 \x01(\x03B\x03\xe0A\x02" \n\nStringList\x12\x12\n\x05value\x18\x01 \x03(\tB\x03\xe0A\x01"\x1f\n\tInt64List\x12\x12\n\x05value\x18\x01 \x03(\x03B\x03\xe0A\x01"\x1e\n\x08BoolList\x12\x12\n\x05value\x18\x01 \x03(\x08B\x03\xe0A\x01"J\n\x08DictList\x12>\n\x05value\x18\x01 \x03(\x0b2*.google.cloud.universalledger.v1.DictValueB\x03\xe0A\x01"\x94\x04\n\tDictValue\x12C\n\tbool_keys\x18\x01 \x01(\x0b2).google.cloud.universalledger.v1.BoolListB\x03\xe0A\x01H\x00\x12G\n\x0bstring_keys\x18\x02 \x01(\x0b2+.google.cloud.universalledger.v1.StringListB\x03\xe0A\x01H\x00\x12E\n\nint64_keys\x18\x03 \x01(\x0b2*.google.cloud.universalledger.v1.Int64ListB\x03\xe0A\x01H\x00\x12E\n\x0bbool_values\x18\x04 \x01(\x0b2).google.cloud.universalledger.v1.BoolListB\x03\xe0A\x01H\x01\x12I\n\rstring_values\x18\x05 \x01(\x0b2+.google.cloud.universalledger.v1.StringListB\x03\xe0A\x01H\x01\x12G\n\x0cint64_values\x18\x06 \x01(\x0b2*.google.cloud.universalledger.v1.Int64ListB\x03\xe0A\x01H\x01\x12E\n\x0bdict_values\x18\x07 \x01(\x0b2).google.cloud.universalledger.v1.DictListB\x03\xe0A\x01H\x01B\x06\n\x04keysB\x08\n\x06values"\x8d\x02\n\x05Value\x12E\n\nnone_value\x18\x01 \x01(\x0e2*.google.cloud.universalledger.v1.NoneValueB\x03\xe0A\x01H\x00\x12\x19\n\nbool_value\x18\x02 \x01(\x08B\x03\xe0A\x01H\x00\x12\x1a\n\x0bint64_value\x18\x03 \x01(\x03B\x03\xe0A\x01H\x00\x12\x1b\n\x0cstring_value\x18\x04 \x01(\tB\x03\xe0A\x01H\x00\x12\x19\n\naccount_id\x18\x05 \x01(\tB\x03\xe0A\x01H\x00\x12E\n\ndict_value\x18\x06 \x01(\x0b2*.google.cloud.universalledger.v1.DictValueB\x03\xe0A\x01H\x00B\x07\n\x05value*\'\n\tNoneValue\x12\x1a\n\x16NONE_VALUE_UNSPECIFIED\x10\x00B\xec\x01\n#com.google.cloud.universalledger.v1B\x0bCommonProtoP\x01ZMcloud.google.com/go/universalledger/apiv1/universalledgerpb;universalledgerpb\xaa\x02\x1fGoogle.Cloud.UniversalLedger.V1\xca\x02\x1fGoogle\\Cloud\\UniversalLedger\\V1\xea\x02"Google::Cloud::UniversalLedger::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.universalledger.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.universalledger.v1B\x0bCommonProtoP\x01ZMcloud.google.com/go/universalledger/apiv1/universalledgerpb;universalledgerpb\xaa\x02\x1fGoogle.Cloud.UniversalLedger.V1\xca\x02\x1fGoogle\\Cloud\\UniversalLedger\\V1\xea\x02"Google::Cloud::UniversalLedger::V1'
    _globals['_ENTITY'].fields_by_name['id']._loaded_options = None
    _globals['_ENTITY'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CURRENCYVALUE'].fields_by_name['value']._loaded_options = None
    _globals['_CURRENCYVALUE'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_STRINGLIST'].fields_by_name['value']._loaded_options = None
    _globals['_STRINGLIST'].fields_by_name['value']._serialized_options = b'\xe0A\x01'
    _globals['_INT64LIST'].fields_by_name['value']._loaded_options = None
    _globals['_INT64LIST'].fields_by_name['value']._serialized_options = b'\xe0A\x01'
    _globals['_BOOLLIST'].fields_by_name['value']._loaded_options = None
    _globals['_BOOLLIST'].fields_by_name['value']._serialized_options = b'\xe0A\x01'
    _globals['_DICTLIST'].fields_by_name['value']._loaded_options = None
    _globals['_DICTLIST'].fields_by_name['value']._serialized_options = b'\xe0A\x01'
    _globals['_DICTVALUE'].fields_by_name['bool_keys']._loaded_options = None
    _globals['_DICTVALUE'].fields_by_name['bool_keys']._serialized_options = b'\xe0A\x01'
    _globals['_DICTVALUE'].fields_by_name['string_keys']._loaded_options = None
    _globals['_DICTVALUE'].fields_by_name['string_keys']._serialized_options = b'\xe0A\x01'
    _globals['_DICTVALUE'].fields_by_name['int64_keys']._loaded_options = None
    _globals['_DICTVALUE'].fields_by_name['int64_keys']._serialized_options = b'\xe0A\x01'
    _globals['_DICTVALUE'].fields_by_name['bool_values']._loaded_options = None
    _globals['_DICTVALUE'].fields_by_name['bool_values']._serialized_options = b'\xe0A\x01'
    _globals['_DICTVALUE'].fields_by_name['string_values']._loaded_options = None
    _globals['_DICTVALUE'].fields_by_name['string_values']._serialized_options = b'\xe0A\x01'
    _globals['_DICTVALUE'].fields_by_name['int64_values']._loaded_options = None
    _globals['_DICTVALUE'].fields_by_name['int64_values']._serialized_options = b'\xe0A\x01'
    _globals['_DICTVALUE'].fields_by_name['dict_values']._loaded_options = None
    _globals['_DICTVALUE'].fields_by_name['dict_values']._serialized_options = b'\xe0A\x01'
    _globals['_VALUE'].fields_by_name['none_value']._loaded_options = None
    _globals['_VALUE'].fields_by_name['none_value']._serialized_options = b'\xe0A\x01'
    _globals['_VALUE'].fields_by_name['bool_value']._loaded_options = None
    _globals['_VALUE'].fields_by_name['bool_value']._serialized_options = b'\xe0A\x01'
    _globals['_VALUE'].fields_by_name['int64_value']._loaded_options = None
    _globals['_VALUE'].fields_by_name['int64_value']._serialized_options = b'\xe0A\x01'
    _globals['_VALUE'].fields_by_name['string_value']._loaded_options = None
    _globals['_VALUE'].fields_by_name['string_value']._serialized_options = b'\xe0A\x01'
    _globals['_VALUE'].fields_by_name['account_id']._loaded_options = None
    _globals['_VALUE'].fields_by_name['account_id']._serialized_options = b'\xe0A\x01'
    _globals['_VALUE'].fields_by_name['dict_value']._loaded_options = None
    _globals['_VALUE'].fields_by_name['dict_value']._serialized_options = b'\xe0A\x01'
    _globals['_NONEVALUE']._serialized_start = 1160
    _globals['_NONEVALUE']._serialized_end = 1199
    _globals['_ENTITY']._serialized_start = 114
    _globals['_ENTITY']._serialized_end = 139
    _globals['_CURRENCYVALUE']._serialized_start = 141
    _globals['_CURRENCYVALUE']._serialized_end = 176
    _globals['_STRINGLIST']._serialized_start = 178
    _globals['_STRINGLIST']._serialized_end = 210
    _globals['_INT64LIST']._serialized_start = 212
    _globals['_INT64LIST']._serialized_end = 243
    _globals['_BOOLLIST']._serialized_start = 245
    _globals['_BOOLLIST']._serialized_end = 275
    _globals['_DICTLIST']._serialized_start = 277
    _globals['_DICTLIST']._serialized_end = 351
    _globals['_DICTVALUE']._serialized_start = 354
    _globals['_DICTVALUE']._serialized_end = 886
    _globals['_VALUE']._serialized_start = 889
    _globals['_VALUE']._serialized_end = 1158