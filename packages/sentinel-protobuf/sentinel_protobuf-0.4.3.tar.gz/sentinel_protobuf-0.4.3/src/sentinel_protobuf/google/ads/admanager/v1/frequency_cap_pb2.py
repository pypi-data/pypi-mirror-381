"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/frequency_cap.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import time_unit_enum_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_time__unit__enum__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/ads/admanager/v1/frequency_cap.proto\x12\x17google.ads.admanager.v1\x1a,google/ads/admanager/v1/time_unit_enum.proto"\xc0\x01\n\x0cFrequencyCap\x12\x1c\n\x0fmax_impressions\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x18\n\x0btime_amount\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12F\n\ttime_unit\x18\x03 \x01(\x0e2..google.ads.admanager.v1.TimeUnitEnum.TimeUnitH\x02\x88\x01\x01B\x12\n\x10_max_impressionsB\x0e\n\x0c_time_amountB\x0c\n\n_time_unitB\xc5\x01\n\x1bcom.google.ads.admanager.v1B\x11FrequencyCapProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.frequency_cap_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x11FrequencyCapProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_FREQUENCYCAP']._serialized_start = 119
    _globals['_FREQUENCYCAP']._serialized_end = 311