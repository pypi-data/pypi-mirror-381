"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/language_constant.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v21/resources/language_constant.proto\x12"google.ads.googleads.v21.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xba\x02\n\x10LanguageConstant\x12H\n\rresource_name\x18\x01 \x01(\tB1\xe0A\x03\xfaA+\n)googleads.googleapis.com/LanguageConstant\x12\x14\n\x02id\x18\x06 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x16\n\x04code\x18\x07 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x16\n\x04name\x18\x08 \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12\x1c\n\ntargetable\x18\t \x01(\x08B\x03\xe0A\x03H\x03\x88\x01\x01:P\xeaAM\n)googleads.googleapis.com/LanguageConstant\x12 languageConstants/{criterion_id}B\x05\n\x03_idB\x07\n\x05_codeB\x07\n\x05_nameB\r\n\x0b_targetableB\x87\x02\n&com.google.ads.googleads.v21.resourcesB\x15LanguageConstantProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.language_constant_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x15LanguageConstantProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_LANGUAGECONSTANT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_LANGUAGECONSTANT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA+\n)googleads.googleapis.com/LanguageConstant'
    _globals['_LANGUAGECONSTANT'].fields_by_name['id']._loaded_options = None
    _globals['_LANGUAGECONSTANT'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_LANGUAGECONSTANT'].fields_by_name['code']._loaded_options = None
    _globals['_LANGUAGECONSTANT'].fields_by_name['code']._serialized_options = b'\xe0A\x03'
    _globals['_LANGUAGECONSTANT'].fields_by_name['name']._loaded_options = None
    _globals['_LANGUAGECONSTANT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_LANGUAGECONSTANT'].fields_by_name['targetable']._loaded_options = None
    _globals['_LANGUAGECONSTANT'].fields_by_name['targetable']._serialized_options = b'\xe0A\x03'
    _globals['_LANGUAGECONSTANT']._loaded_options = None
    _globals['_LANGUAGECONSTANT']._serialized_options = b'\xeaAM\n)googleads.googleapis.com/LanguageConstant\x12 languageConstants/{criterion_id}'
    _globals['_LANGUAGECONSTANT']._serialized_start = 159
    _globals['_LANGUAGECONSTANT']._serialized_end = 473