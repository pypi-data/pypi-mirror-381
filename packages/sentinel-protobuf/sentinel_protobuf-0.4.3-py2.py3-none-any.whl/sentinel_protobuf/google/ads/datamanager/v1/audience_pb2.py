"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/datamanager/v1/audience.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.datamanager.v1 import consent_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_consent__pb2
from .....google.ads.datamanager.v1 import user_data_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_user__data__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/ads/datamanager/v1/audience.proto\x12\x19google.ads.datamanager.v1\x1a\'google/ads/datamanager/v1/consent.proto\x1a)google/ads/datamanager/v1/user_data.proto\x1a\x1fgoogle/api/field_behavior.proto"\x84\x02\n\x0eAudienceMember\x128\n\tuser_data\x18\x02 \x01(\x0b2#.google.ads.datamanager.v1.UserDataH\x00\x128\n\tpair_data\x18\x04 \x01(\x0b2#.google.ads.datamanager.v1.PairDataH\x00\x12<\n\x0bmobile_data\x18\x05 \x01(\x0b2%.google.ads.datamanager.v1.MobileDataH\x00\x128\n\x07consent\x18\x03 \x01(\x0b2".google.ads.datamanager.v1.ConsentB\x03\xe0A\x01B\x06\n\x04data"!\n\x08PairData\x12\x15\n\x08pair_ids\x18\x01 \x03(\tB\x03\xe0A\x02"%\n\nMobileData\x12\x17\n\nmobile_ids\x18\x01 \x03(\tB\x03\xe0A\x02B\xcd\x01\n\x1dcom.google.ads.datamanager.v1B\rAudienceProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.datamanager.v1.audience_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.ads.datamanager.v1B\rAudienceProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1'
    _globals['_AUDIENCEMEMBER'].fields_by_name['consent']._loaded_options = None
    _globals['_AUDIENCEMEMBER'].fields_by_name['consent']._serialized_options = b'\xe0A\x01'
    _globals['_PAIRDATA'].fields_by_name['pair_ids']._loaded_options = None
    _globals['_PAIRDATA'].fields_by_name['pair_ids']._serialized_options = b'\xe0A\x02'
    _globals['_MOBILEDATA'].fields_by_name['mobile_ids']._loaded_options = None
    _globals['_MOBILEDATA'].fields_by_name['mobile_ids']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEMEMBER']._serialized_start = 189
    _globals['_AUDIENCEMEMBER']._serialized_end = 449
    _globals['_PAIRDATA']._serialized_start = 451
    _globals['_PAIRDATA']._serialized_end = 484
    _globals['_MOBILEDATA']._serialized_start = 486
    _globals['_MOBILEDATA']._serialized_end = 523