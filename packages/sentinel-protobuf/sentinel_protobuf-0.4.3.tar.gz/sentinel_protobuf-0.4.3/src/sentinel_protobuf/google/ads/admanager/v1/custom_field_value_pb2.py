"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/custom_field_value.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/ads/admanager/v1/custom_field_value.proto\x12\x17google.ads.admanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x9e\x02\n\x10CustomFieldValue\x12B\n\x0ccustom_field\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$admanager.googleapis.com/CustomField\x12H\n\x05value\x18\x02 \x01(\x0b2/.google.ads.admanager.v1.CustomFieldValue.ValueB\x03\xe0A\x02H\x00\x88\x01\x01\x1ar\n\x05Value\x12\x18\n\x0edropdown_value\x18\x01 \x01(\x03H\x00\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x12\x16\n\x0cnumber_value\x18\x03 \x01(\x01H\x00\x12\x16\n\x0ctoggle_value\x18\x04 \x01(\x08H\x00B\x07\n\x05valueB\x08\n\x06_valueB\xc9\x01\n\x1bcom.google.ads.admanager.v1B\x15CustomFieldValueProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.custom_field_value_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x15CustomFieldValueProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_CUSTOMFIELDVALUE'].fields_by_name['custom_field']._loaded_options = None
    _globals['_CUSTOMFIELDVALUE'].fields_by_name['custom_field']._serialized_options = b'\xe0A\x02\xfaA&\n$admanager.googleapis.com/CustomField'
    _globals['_CUSTOMFIELDVALUE'].fields_by_name['value']._loaded_options = None
    _globals['_CUSTOMFIELDVALUE'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMFIELDVALUE']._serialized_start = 138
    _globals['_CUSTOMFIELDVALUE']._serialized_end = 424
    _globals['_CUSTOMFIELDVALUE_VALUE']._serialized_start = 300
    _globals['_CUSTOMFIELDVALUE_VALUE']._serialized_end = 414