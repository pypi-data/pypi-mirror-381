"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/common/extensions.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import custom_parameter_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_custom__parameter__pb2
from ......google.ads.googleads.v20.enums import call_conversion_reporting_state_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_call__conversion__reporting__state__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/ads/googleads/v20/common/extensions.proto\x12\x1fgoogle.ads.googleads.v20.common\x1a6google/ads/googleads/v20/common/custom_parameter.proto\x1aDgoogle/ads/googleads/v20/enums/call_conversion_reporting_state.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc3\x03\n\x0cCallFeedItem\x12\x19\n\x0cphone_number\x18\x07 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0ccountry_code\x18\x08 \x01(\tH\x01\x88\x01\x01\x12"\n\x15call_tracking_enabled\x18\t \x01(\x08H\x02\x88\x01\x01\x12#\n\x16call_conversion_action\x18\n \x01(\tH\x03\x88\x01\x01\x12.\n!call_conversion_tracking_disabled\x18\x0b \x01(\x08H\x04\x88\x01\x01\x12\x86\x01\n\x1fcall_conversion_reporting_state\x18\x06 \x01(\x0e2].google.ads.googleads.v20.enums.CallConversionReportingStateEnum.CallConversionReportingStateB\x0f\n\r_phone_numberB\x0f\n\r_country_codeB\x18\n\x16_call_tracking_enabledB\x19\n\x17_call_conversion_actionB$\n"_call_conversion_tracking_disabled"=\n\x0fCalloutFeedItem\x12\x19\n\x0ccallout_text\x18\x02 \x01(\tH\x00\x88\x01\x01B\x0f\n\r_callout_text"\xe6\x02\n\x10SitelinkFeedItem\x12\x16\n\tlink_text\x18\t \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05line1\x18\n \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05line2\x18\x0b \x01(\tH\x02\x88\x01\x01\x12\x12\n\nfinal_urls\x18\x0c \x03(\t\x12\x19\n\x11final_mobile_urls\x18\r \x03(\t\x12"\n\x15tracking_url_template\x18\x0e \x01(\tH\x03\x88\x01\x01\x12O\n\x15url_custom_parameters\x18\x07 \x03(\x0b20.google.ads.googleads.v20.common.CustomParameter\x12\x1d\n\x10final_url_suffix\x18\x0f \x01(\tH\x04\x88\x01\x01B\x0c\n\n_link_textB\x08\n\x06_line1B\x08\n\x06_line2B\x18\n\x16_tracking_url_templateB\x13\n\x11_final_url_suffixB\xef\x01\n#com.google.ads.googleads.v20.commonB\x0fExtensionsProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v20/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V20.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V20\\Common\xea\x02#Google::Ads::GoogleAds::V20::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.common.extensions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v20.commonB\x0fExtensionsProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v20/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V20.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V20\\Common\xea\x02#Google::Ads::GoogleAds::V20::Common'
    _globals['_CALLFEEDITEM']._serialized_start = 272
    _globals['_CALLFEEDITEM']._serialized_end = 723
    _globals['_CALLOUTFEEDITEM']._serialized_start = 725
    _globals['_CALLOUTFEEDITEM']._serialized_end = 786
    _globals['_SITELINKFEEDITEM']._serialized_start = 789
    _globals['_SITELINKFEEDITEM']._serialized_end = 1147