"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/common/frequency_cap.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import frequency_cap_event_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_frequency__cap__event__type__pb2
from ......google.ads.googleads.v21.enums import frequency_cap_level_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_frequency__cap__level__pb2
from ......google.ads.googleads.v21.enums import frequency_cap_time_unit_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_frequency__cap__time__unit__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/googleads/v21/common/frequency_cap.proto\x12\x1fgoogle.ads.googleads.v21.common\x1a=google/ads/googleads/v21/enums/frequency_cap_event_type.proto\x1a8google/ads/googleads/v21/enums/frequency_cap_level.proto\x1a<google/ads/googleads/v21/enums/frequency_cap_time_unit.proto"l\n\x11FrequencyCapEntry\x12=\n\x03key\x18\x01 \x01(\x0b20.google.ads.googleads.v21.common.FrequencyCapKey\x12\x10\n\x03cap\x18\x03 \x01(\x05H\x00\x88\x01\x01B\x06\n\x04_cap"\xda\x02\n\x0fFrequencyCapKey\x12V\n\x05level\x18\x01 \x01(\x0e2G.google.ads.googleads.v21.enums.FrequencyCapLevelEnum.FrequencyCapLevel\x12c\n\nevent_type\x18\x03 \x01(\x0e2O.google.ads.googleads.v21.enums.FrequencyCapEventTypeEnum.FrequencyCapEventType\x12`\n\ttime_unit\x18\x02 \x01(\x0e2M.google.ads.googleads.v21.enums.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit\x12\x18\n\x0btime_length\x18\x05 \x01(\x05H\x00\x88\x01\x01B\x0e\n\x0c_time_lengthB\xf1\x01\n#com.google.ads.googleads.v21.commonB\x11FrequencyCapProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v21/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V21.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V21\\Common\xea\x02#Google::Ads::GoogleAds::V21::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.common.frequency_cap_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v21.commonB\x11FrequencyCapProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v21/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V21.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V21\\Common\xea\x02#Google::Ads::GoogleAds::V21::Common'
    _globals['_FREQUENCYCAPENTRY']._serialized_start = 271
    _globals['_FREQUENCYCAPENTRY']._serialized_end = 379
    _globals['_FREQUENCYCAPKEY']._serialized_start = 382
    _globals['_FREQUENCYCAPKEY']._serialized_end = 728