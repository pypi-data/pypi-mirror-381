"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/common/targeting_setting.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import targeting_dimension_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_targeting__dimension__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/googleads/v19/common/targeting_setting.proto\x12\x1fgoogle.ads.googleads.v19.common\x1a8google/ads/googleads/v19/enums/targeting_dimension.proto"\xc7\x01\n\x10TargetingSetting\x12O\n\x13target_restrictions\x18\x01 \x03(\x0b22.google.ads.googleads.v19.common.TargetRestriction\x12b\n\x1dtarget_restriction_operations\x18\x02 \x03(\x0b2;.google.ads.googleads.v19.common.TargetRestrictionOperation"\x9f\x01\n\x11TargetRestriction\x12f\n\x13targeting_dimension\x18\x01 \x01(\x0e2I.google.ads.googleads.v19.enums.TargetingDimensionEnum.TargetingDimension\x12\x15\n\x08bid_only\x18\x03 \x01(\x08H\x00\x88\x01\x01B\x0b\n\t_bid_only"\xf6\x01\n\x1aTargetRestrictionOperation\x12V\n\x08operator\x18\x01 \x01(\x0e2D.google.ads.googleads.v19.common.TargetRestrictionOperation.Operator\x12A\n\x05value\x18\x02 \x01(\x0b22.google.ads.googleads.v19.common.TargetRestriction"=\n\x08Operator\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x07\n\x03ADD\x10\x02\x12\n\n\x06REMOVE\x10\x03B\xf5\x01\n#com.google.ads.googleads.v19.commonB\x15TargetingSettingProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.common.targeting_setting_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v19.commonB\x15TargetingSettingProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Common'
    _globals['_TARGETINGSETTING']._serialized_start = 151
    _globals['_TARGETINGSETTING']._serialized_end = 350
    _globals['_TARGETRESTRICTION']._serialized_start = 353
    _globals['_TARGETRESTRICTION']._serialized_end = 512
    _globals['_TARGETRESTRICTIONOPERATION']._serialized_start = 515
    _globals['_TARGETRESTRICTIONOPERATION']._serialized_end = 761
    _globals['_TARGETRESTRICTIONOPERATION_OPERATOR']._serialized_start = 700
    _globals['_TARGETRESTRICTIONOPERATION_OPERATOR']._serialized_end = 761