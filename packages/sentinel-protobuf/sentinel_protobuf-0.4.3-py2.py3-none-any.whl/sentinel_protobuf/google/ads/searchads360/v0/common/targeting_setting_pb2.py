"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/common/targeting_setting.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import targeting_dimension_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_targeting__dimension__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/searchads360/v0/common/targeting_setting.proto\x12!google.ads.searchads360.v0.common\x1a:google/ads/searchads360/v0/enums/targeting_dimension.proto"e\n\x10TargetingSetting\x12Q\n\x13target_restrictions\x18\x01 \x03(\x0b24.google.ads.searchads360.v0.common.TargetRestriction"\xa1\x01\n\x11TargetRestriction\x12h\n\x13targeting_dimension\x18\x01 \x01(\x0e2K.google.ads.searchads360.v0.enums.TargetingDimensionEnum.TargetingDimension\x12\x15\n\x08bid_only\x18\x03 \x01(\x08H\x00\x88\x01\x01B\x0b\n\t_bid_onlyB\x83\x02\n%com.google.ads.searchads360.v0.commonB\x15TargetingSettingProtoP\x01ZGgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/common;common\xa2\x02\x07GASA360\xaa\x02!Google.Ads.SearchAds360.V0.Common\xca\x02!Google\\Ads\\SearchAds360\\V0\\Common\xea\x02%Google::Ads::SearchAds360::V0::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.common.targeting_setting_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.searchads360.v0.commonB\x15TargetingSettingProtoP\x01ZGgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/common;common\xa2\x02\x07GASA360\xaa\x02!Google.Ads.SearchAds360.V0.Common\xca\x02!Google\\Ads\\SearchAds360\\V0\\Common\xea\x02%Google::Ads::SearchAds360::V0::Common'
    _globals['_TARGETINGSETTING']._serialized_start = 156
    _globals['_TARGETINGSETTING']._serialized_end = 257
    _globals['_TARGETRESTRICTION']._serialized_start = 260
    _globals['_TARGETRESTRICTION']._serialized_end = 421