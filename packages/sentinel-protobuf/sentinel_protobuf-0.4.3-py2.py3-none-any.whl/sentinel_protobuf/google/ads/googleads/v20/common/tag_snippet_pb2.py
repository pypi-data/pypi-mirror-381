"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/common/tag_snippet.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import tracking_code_page_format_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_tracking__code__page__format__pb2
from ......google.ads.googleads.v20.enums import tracking_code_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_tracking__code__type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ads/googleads/v20/common/tag_snippet.proto\x12\x1fgoogle.ads.googleads.v20.common\x1a>google/ads/googleads/v20/enums/tracking_code_page_format.proto\x1a7google/ads/googleads/v20/enums/tracking_code_type.proto"\xa9\x02\n\nTagSnippet\x12S\n\x04type\x18\x01 \x01(\x0e2E.google.ads.googleads.v20.enums.TrackingCodeTypeEnum.TrackingCodeType\x12f\n\x0bpage_format\x18\x02 \x01(\x0e2Q.google.ads.googleads.v20.enums.TrackingCodePageFormatEnum.TrackingCodePageFormat\x12\x1c\n\x0fglobal_site_tag\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\revent_snippet\x18\x06 \x01(\tH\x01\x88\x01\x01B\x12\n\x10_global_site_tagB\x10\n\x0e_event_snippetB\xef\x01\n#com.google.ads.googleads.v20.commonB\x0fTagSnippetProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v20/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V20.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V20\\Common\xea\x02#Google::Ads::GoogleAds::V20::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.common.tag_snippet_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v20.commonB\x0fTagSnippetProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v20/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V20.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V20\\Common\xea\x02#Google::Ads::GoogleAds::V20::Common'
    _globals['_TAGSNIPPET']._serialized_start = 208
    _globals['_TAGSNIPPET']._serialized_end = 505