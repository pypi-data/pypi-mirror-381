"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/common/criterion_category_availability.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import advertising_channel_sub_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_advertising__channel__sub__type__pb2
from ......google.ads.googleads.v21.enums import advertising_channel_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_advertising__channel__type__pb2
from ......google.ads.googleads.v21.enums import criterion_category_channel_availability_mode_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_criterion__category__channel__availability__mode__pb2
from ......google.ads.googleads.v21.enums import criterion_category_locale_availability_mode_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_criterion__category__locale__availability__mode__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/ads/googleads/v21/common/criterion_category_availability.proto\x12\x1fgoogle.ads.googleads.v21.common\x1aAgoogle/ads/googleads/v21/enums/advertising_channel_sub_type.proto\x1a=google/ads/googleads/v21/enums/advertising_channel_type.proto\x1aQgoogle/ads/googleads/v21/enums/criterion_category_channel_availability_mode.proto\x1aPgoogle/ads/googleads/v21/enums/criterion_category_locale_availability_mode.proto"\xcd\x01\n\x1dCriterionCategoryAvailability\x12V\n\x07channel\x18\x01 \x01(\x0b2E.google.ads.googleads.v21.common.CriterionCategoryChannelAvailability\x12T\n\x06locale\x18\x02 \x03(\x0b2D.google.ads.googleads.v21.common.CriterionCategoryLocaleAvailability"\x81\x04\n$CriterionCategoryChannelAvailability\x12\x90\x01\n\x11availability_mode\x18\x01 \x01(\x0e2u.google.ads.googleads.v21.enums.CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode\x12s\n\x18advertising_channel_type\x18\x02 \x01(\x0e2Q.google.ads.googleads.v21.enums.AdvertisingChannelTypeEnum.AdvertisingChannelType\x12}\n\x1cadvertising_channel_sub_type\x18\x03 \x03(\x0e2W.google.ads.googleads.v21.enums.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType\x12-\n include_default_channel_sub_type\x18\x05 \x01(\x08H\x00\x88\x01\x01B#\n!_include_default_channel_sub_type"\x90\x02\n#CriterionCategoryLocaleAvailability\x12\x8e\x01\n\x11availability_mode\x18\x01 \x01(\x0e2s.google.ads.googleads.v21.enums.CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode\x12\x19\n\x0ccountry_code\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rlanguage_code\x18\x05 \x01(\tH\x01\x88\x01\x01B\x0f\n\r_country_codeB\x10\n\x0e_language_codeB\x82\x02\n#com.google.ads.googleads.v21.commonB"CriterionCategoryAvailabilityProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v21/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V21.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V21\\Common\xea\x02#Google::Ads::GoogleAds::V21::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.common.criterion_category_availability_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v21.commonB"CriterionCategoryAvailabilityProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v21/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V21.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V21\\Common\xea\x02#Google::Ads::GoogleAds::V21::Common'
    _globals['_CRITERIONCATEGORYAVAILABILITY']._serialized_start = 402
    _globals['_CRITERIONCATEGORYAVAILABILITY']._serialized_end = 607
    _globals['_CRITERIONCATEGORYCHANNELAVAILABILITY']._serialized_start = 610
    _globals['_CRITERIONCATEGORYCHANNELAVAILABILITY']._serialized_end = 1123
    _globals['_CRITERIONCATEGORYLOCALEAVAILABILITY']._serialized_start = 1126
    _globals['_CRITERIONCATEGORYLOCALEAVAILABILITY']._serialized_end = 1398