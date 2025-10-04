"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/datamanager/v1/encryption_info.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/ads/datamanager/v1/encryption_info.proto\x12\x19google.ads.datamanager.v1\x1a\x1fgoogle/api/field_behavior.proto"m\n\x0eEncryptionInfo\x12L\n\x14gcp_wrapped_key_info\x18\x01 \x01(\x0b2,.google.ads.datamanager.v1.GcpWrappedKeyInfoH\x00B\r\n\x0bwrapped_key"\xea\x01\n\x11GcpWrappedKeyInfo\x12K\n\x08key_type\x18\x01 \x01(\x0e24.google.ads.datamanager.v1.GcpWrappedKeyInfo.KeyTypeB\x03\xe0A\x02\x12\x19\n\x0cwip_provider\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07kek_uri\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rencrypted_dek\x18\x04 \x01(\tB\x03\xe0A\x02";\n\x07KeyType\x12\x18\n\x14KEY_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12XCHACHA20_POLY1305\x10\x01B\xd3\x01\n\x1dcom.google.ads.datamanager.v1B\x13EncryptionInfoProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.datamanager.v1.encryption_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.ads.datamanager.v1B\x13EncryptionInfoProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1'
    _globals['_GCPWRAPPEDKEYINFO'].fields_by_name['key_type']._loaded_options = None
    _globals['_GCPWRAPPEDKEYINFO'].fields_by_name['key_type']._serialized_options = b'\xe0A\x02'
    _globals['_GCPWRAPPEDKEYINFO'].fields_by_name['wip_provider']._loaded_options = None
    _globals['_GCPWRAPPEDKEYINFO'].fields_by_name['wip_provider']._serialized_options = b'\xe0A\x02'
    _globals['_GCPWRAPPEDKEYINFO'].fields_by_name['kek_uri']._loaded_options = None
    _globals['_GCPWRAPPEDKEYINFO'].fields_by_name['kek_uri']._serialized_options = b'\xe0A\x02'
    _globals['_GCPWRAPPEDKEYINFO'].fields_by_name['encrypted_dek']._loaded_options = None
    _globals['_GCPWRAPPEDKEYINFO'].fields_by_name['encrypted_dek']._serialized_options = b'\xe0A\x02'
    _globals['_ENCRYPTIONINFO']._serialized_start = 111
    _globals['_ENCRYPTIONINFO']._serialized_end = 220
    _globals['_GCPWRAPPEDKEYINFO']._serialized_start = 223
    _globals['_GCPWRAPPEDKEYINFO']._serialized_end = 457
    _globals['_GCPWRAPPEDKEYINFO_KEYTYPE']._serialized_start = 398
    _globals['_GCPWRAPPEDKEYINFO_KEYTYPE']._serialized_end = 457