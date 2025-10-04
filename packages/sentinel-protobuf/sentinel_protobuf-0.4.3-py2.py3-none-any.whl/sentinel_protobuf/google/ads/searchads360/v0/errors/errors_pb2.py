"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/errors/errors.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.common import value_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_value__pb2
from ......google.ads.searchads360.v0.errors import authentication_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_authentication__error__pb2
from ......google.ads.searchads360.v0.errors import authorization_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_authorization__error__pb2
from ......google.ads.searchads360.v0.errors import custom_column_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_custom__column__error__pb2
from ......google.ads.searchads360.v0.errors import date_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_date__error__pb2
from ......google.ads.searchads360.v0.errors import date_range_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_date__range__error__pb2
from ......google.ads.searchads360.v0.errors import distinct_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_distinct__error__pb2
from ......google.ads.searchads360.v0.errors import header_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_header__error__pb2
from ......google.ads.searchads360.v0.errors import internal_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_internal__error__pb2
from ......google.ads.searchads360.v0.errors import invalid_parameter_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_invalid__parameter__error__pb2
from ......google.ads.searchads360.v0.errors import query_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_query__error__pb2
from ......google.ads.searchads360.v0.errors import quota_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_quota__error__pb2
from ......google.ads.searchads360.v0.errors import request_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_request__error__pb2
from ......google.ads.searchads360.v0.errors import size_limit_error_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_errors_dot_size__limit__error__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/ads/searchads360/v0/errors/errors.proto\x12!google.ads.searchads360.v0.errors\x1a-google/ads/searchads360/v0/common/value.proto\x1a<google/ads/searchads360/v0/errors/authentication_error.proto\x1a;google/ads/searchads360/v0/errors/authorization_error.proto\x1a;google/ads/searchads360/v0/errors/custom_column_error.proto\x1a2google/ads/searchads360/v0/errors/date_error.proto\x1a8google/ads/searchads360/v0/errors/date_range_error.proto\x1a6google/ads/searchads360/v0/errors/distinct_error.proto\x1a4google/ads/searchads360/v0/errors/header_error.proto\x1a6google/ads/searchads360/v0/errors/internal_error.proto\x1a?google/ads/searchads360/v0/errors/invalid_parameter_error.proto\x1a3google/ads/searchads360/v0/errors/query_error.proto\x1a3google/ads/searchads360/v0/errors/quota_error.proto\x1a5google/ads/searchads360/v0/errors/request_error.proto\x1a8google/ads/searchads360/v0/errors/size_limit_error.proto\x1a\x1egoogle/protobuf/duration.proto"o\n\x13SearchAds360Failure\x12D\n\x06errors\x18\x01 \x03(\x0b24.google.ads.searchads360.v0.errors.SearchAds360Error\x12\x12\n\nrequest_id\x18\x02 \x01(\t"\xa7\x02\n\x11SearchAds360Error\x12@\n\nerror_code\x18\x01 \x01(\x0b2,.google.ads.searchads360.v0.errors.ErrorCode\x12\x0f\n\x07message\x18\x02 \x01(\t\x129\n\x07trigger\x18\x03 \x01(\x0b2(.google.ads.searchads360.v0.common.Value\x12B\n\x08location\x18\x04 \x01(\x0b20.google.ads.searchads360.v0.errors.ErrorLocation\x12@\n\x07details\x18\x05 \x01(\x0b2/.google.ads.searchads360.v0.errors.ErrorDetails"\x89\n\n\tErrorCode\x12Y\n\rrequest_error\x18\x01 \x01(\x0e2@.google.ads.searchads360.v0.errors.RequestErrorEnum.RequestErrorH\x00\x12S\n\x0bquery_error\x18\x05 \x01(\x0e2<.google.ads.searchads360.v0.errors.QueryErrorEnum.QueryErrorH\x00\x12k\n\x13authorization_error\x18\t \x01(\x0e2L.google.ads.searchads360.v0.errors.AuthorizationErrorEnum.AuthorizationErrorH\x00\x12\\\n\x0einternal_error\x18\n \x01(\x0e2B.google.ads.searchads360.v0.errors.InternalErrorEnum.InternalErrorH\x00\x12S\n\x0bquota_error\x18\x0b \x01(\x0e2<.google.ads.searchads360.v0.errors.QuotaErrorEnum.QuotaErrorH\x00\x12n\n\x14authentication_error\x18\x11 \x01(\x0e2N.google.ads.searchads360.v0.errors.AuthenticationErrorEnum.AuthenticationErrorH\x00\x12P\n\ndate_error\x18! \x01(\x0e2:.google.ads.searchads360.v0.errors.DateErrorEnum.DateErrorH\x00\x12`\n\x10date_range_error\x18" \x01(\x0e2D.google.ads.searchads360.v0.errors.DateRangeErrorEnum.DateRangeErrorH\x00\x12\\\n\x0edistinct_error\x18# \x01(\x0e2B.google.ads.searchads360.v0.errors.DistinctErrorEnum.DistinctErrorH\x00\x12V\n\x0cheader_error\x18B \x01(\x0e2>.google.ads.searchads360.v0.errors.HeaderErrorEnum.HeaderErrorH\x00\x12`\n\x10size_limit_error\x18v \x01(\x0e2D.google.ads.searchads360.v0.errors.SizeLimitErrorEnum.SizeLimitErrorH\x00\x12j\n\x13custom_column_error\x18\x90\x01 \x01(\x0e2J.google.ads.searchads360.v0.errors.CustomColumnErrorEnum.CustomColumnErrorH\x00\x12v\n\x17invalid_parameter_error\x18\xaf\x01 \x01(\x0e2R.google.ads.searchads360.v0.errors.InvalidParameterErrorEnum.InvalidParameterErrorH\x00B\x0c\n\nerror_code"\xb5\x01\n\rErrorLocation\x12^\n\x13field_path_elements\x18\x02 \x03(\x0b2A.google.ads.searchads360.v0.errors.ErrorLocation.FieldPathElement\x1aD\n\x10FieldPathElement\x12\x12\n\nfield_name\x18\x01 \x01(\t\x12\x12\n\x05index\x18\x03 \x01(\x05H\x00\x88\x01\x01B\x08\n\x06_index"\x81\x01\n\x0cErrorDetails\x12\x1e\n\x16unpublished_error_code\x18\x01 \x01(\t\x12Q\n\x13quota_error_details\x18\x04 \x01(\x0b24.google.ads.searchads360.v0.errors.QuotaErrorDetails"\xfb\x01\n\x11QuotaErrorDetails\x12W\n\nrate_scope\x18\x01 \x01(\x0e2C.google.ads.searchads360.v0.errors.QuotaErrorDetails.QuotaRateScope\x12\x11\n\trate_name\x18\x02 \x01(\t\x12.\n\x0bretry_delay\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration"J\n\x0eQuotaRateScope\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07ACCOUNT\x10\x02\x12\r\n\tDEVELOPER\x10\x03B\xf9\x01\n%com.google.ads.searchads360.v0.errorsB\x0bErrorsProtoP\x01ZGgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/errors;errors\xa2\x02\x07GASA360\xaa\x02!Google.Ads.SearchAds360.V0.Errors\xca\x02!Google\\Ads\\SearchAds360\\V0\\Errors\xea\x02%Google::Ads::SearchAds360::V0::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.errors.errors_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.searchads360.v0.errorsB\x0bErrorsProtoP\x01ZGgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/errors;errors\xa2\x02\x07GASA360\xaa\x02!Google.Ads.SearchAds360.V0.Errors\xca\x02!Google\\Ads\\SearchAds360\\V0\\Errors\xea\x02%Google::Ads::SearchAds360::V0::Errors'
    _globals['_SEARCHADS360FAILURE']._serialized_start = 908
    _globals['_SEARCHADS360FAILURE']._serialized_end = 1019
    _globals['_SEARCHADS360ERROR']._serialized_start = 1022
    _globals['_SEARCHADS360ERROR']._serialized_end = 1317
    _globals['_ERRORCODE']._serialized_start = 1320
    _globals['_ERRORCODE']._serialized_end = 2609
    _globals['_ERRORLOCATION']._serialized_start = 2612
    _globals['_ERRORLOCATION']._serialized_end = 2793
    _globals['_ERRORLOCATION_FIELDPATHELEMENT']._serialized_start = 2725
    _globals['_ERRORLOCATION_FIELDPATHELEMENT']._serialized_end = 2793
    _globals['_ERRORDETAILS']._serialized_start = 2796
    _globals['_ERRORDETAILS']._serialized_end = 2925
    _globals['_QUOTAERRORDETAILS']._serialized_start = 2928
    _globals['_QUOTAERRORDETAILS']._serialized_end = 3179
    _globals['_QUOTAERRORDETAILS_QUOTARATESCOPE']._serialized_start = 3105
    _globals['_QUOTAERRORDETAILS_QUOTARATESCOPE']._serialized_end = 3179