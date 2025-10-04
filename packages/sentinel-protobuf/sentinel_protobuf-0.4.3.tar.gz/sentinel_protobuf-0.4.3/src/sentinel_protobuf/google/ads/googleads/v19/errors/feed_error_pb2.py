"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/errors/feed_error.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/ads/googleads/v19/errors/feed_error.proto\x12\x1fgoogle.ads.googleads.v19.errors"\xeb\x06\n\rFeedErrorEnum"\xd9\x06\n\tFeedError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1e\n\x1aATTRIBUTE_NAMES_NOT_UNIQUE\x10\x02\x12/\n+ATTRIBUTES_DO_NOT_MATCH_EXISTING_ATTRIBUTES\x10\x03\x12.\n*CANNOT_SPECIFY_USER_ORIGIN_FOR_SYSTEM_FEED\x10\x04\x124\n0CANNOT_SPECIFY_GOOGLE_ORIGIN_FOR_NON_SYSTEM_FEED\x10\x05\x122\n.CANNOT_SPECIFY_FEED_ATTRIBUTES_FOR_SYSTEM_FEED\x10\x06\x124\n0CANNOT_UPDATE_FEED_ATTRIBUTES_WITH_ORIGIN_GOOGLE\x10\x07\x12\x10\n\x0cFEED_REMOVED\x10\x08\x12\x18\n\x14INVALID_ORIGIN_VALUE\x10\t\x12\x1b\n\x17FEED_ORIGIN_IS_NOT_USER\x10\n\x12 \n\x1cINVALID_AUTH_TOKEN_FOR_EMAIL\x10\x0b\x12\x11\n\rINVALID_EMAIL\x10\x0c\x12\x17\n\x13DUPLICATE_FEED_NAME\x10\r\x12\x15\n\x11INVALID_FEED_NAME\x10\x0e\x12\x16\n\x12MISSING_OAUTH_INFO\x10\x0f\x12.\n*NEW_ATTRIBUTE_CANNOT_BE_PART_OF_UNIQUE_KEY\x10\x10\x12\x17\n\x13TOO_MANY_ATTRIBUTES\x10\x11\x12\x1c\n\x18INVALID_BUSINESS_ACCOUNT\x10\x12\x123\n/BUSINESS_ACCOUNT_CANNOT_ACCESS_LOCATION_ACCOUNT\x10\x13\x12\x1e\n\x1aINVALID_AFFILIATE_CHAIN_ID\x10\x14\x12\x19\n\x15DUPLICATE_SYSTEM_FEED\x10\x15\x12\x14\n\x10GMB_ACCESS_ERROR\x10\x16\x125\n1CANNOT_HAVE_LOCATION_AND_AFFILIATE_LOCATION_FEEDS\x10\x17\x12#\n\x1fLEGACY_EXTENSION_TYPE_READ_ONLY\x10\x18B\xee\x01\n#com.google.ads.googleads.v19.errorsB\x0eFeedErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Errors\xea\x02#Google::Ads::GoogleAds::V19::Errorsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.errors.feed_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v19.errorsB\x0eFeedErrorProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/errors;errors\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Errors\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Errors\xea\x02#Google::Ads::GoogleAds::V19::Errors'
    _globals['_FEEDERRORENUM']._serialized_start = 86
    _globals['_FEEDERRORENUM']._serialized_end = 961
    _globals['_FEEDERRORENUM_FEEDERROR']._serialized_start = 104
    _globals['_FEEDERRORENUM_FEEDERROR']._serialized_end = 961