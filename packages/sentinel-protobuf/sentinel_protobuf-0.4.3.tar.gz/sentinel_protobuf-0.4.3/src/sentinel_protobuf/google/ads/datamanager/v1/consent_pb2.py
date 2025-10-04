"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/datamanager/v1/consent.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/ads/datamanager/v1/consent.proto\x12\x19google.ads.datamanager.v1\x1a\x1fgoogle/api/field_behavior.proto"\x99\x01\n\x07Consent\x12C\n\x0cad_user_data\x18\x01 \x01(\x0e2(.google.ads.datamanager.v1.ConsentStatusB\x03\xe0A\x01\x12I\n\x12ad_personalization\x18\x02 \x01(\x0e2(.google.ads.datamanager.v1.ConsentStatusB\x03\xe0A\x01*X\n\rConsentStatus\x12\x1e\n\x1aCONSENT_STATUS_UNSPECIFIED\x10\x00\x12\x13\n\x0fCONSENT_GRANTED\x10\x01\x12\x12\n\x0eCONSENT_DENIED\x10\x02B\xcc\x01\n\x1dcom.google.ads.datamanager.v1B\x0cConsentProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.datamanager.v1.consent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.ads.datamanager.v1B\x0cConsentProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1'
    _globals['_CONSENT'].fields_by_name['ad_user_data']._loaded_options = None
    _globals['_CONSENT'].fields_by_name['ad_user_data']._serialized_options = b'\xe0A\x01'
    _globals['_CONSENT'].fields_by_name['ad_personalization']._loaded_options = None
    _globals['_CONSENT'].fields_by_name['ad_personalization']._serialized_options = b'\xe0A\x01'
    _globals['_CONSENTSTATUS']._serialized_start = 259
    _globals['_CONSENTSTATUS']._serialized_end = 347
    _globals['_CONSENT']._serialized_start = 104
    _globals['_CONSENT']._serialized_end = 257