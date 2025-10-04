"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/common/dates.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import month_of_year_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_month__of__year__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/ads/googleads/v21/common/dates.proto\x12\x1fgoogle.ads.googleads.v21.common\x1a2google/ads/googleads/v21/enums/month_of_year.proto"W\n\tDateRange\x12\x17\n\nstart_date\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08end_date\x18\x04 \x01(\tH\x01\x88\x01\x01B\r\n\x0b_start_dateB\x0b\n\t_end_date"\x84\x01\n\x0eYearMonthRange\x129\n\x05start\x18\x01 \x01(\x0b2*.google.ads.googleads.v21.common.YearMonth\x127\n\x03end\x18\x02 \x01(\x0b2*.google.ads.googleads.v21.common.YearMonth"e\n\tYearMonth\x12\x0c\n\x04year\x18\x01 \x01(\x03\x12J\n\x05month\x18\x02 \x01(\x0e2;.google.ads.googleads.v21.enums.MonthOfYearEnum.MonthOfYearB\xea\x01\n#com.google.ads.googleads.v21.commonB\nDatesProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v21/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V21.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V21\\Common\xea\x02#Google::Ads::GoogleAds::V21::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.common.dates_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v21.commonB\nDatesProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v21/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V21.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V21\\Common\xea\x02#Google::Ads::GoogleAds::V21::Common'
    _globals['_DATERANGE']._serialized_start = 132
    _globals['_DATERANGE']._serialized_end = 219
    _globals['_YEARMONTHRANGE']._serialized_start = 222
    _globals['_YEARMONTHRANGE']._serialized_end = 354
    _globals['_YEARMONTH']._serialized_start = 356
    _globals['_YEARMONTH']._serialized_end = 457