"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/common/ad_type_infos.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.common import ad_asset_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_ad__asset__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/ads/searchads360/v0/common/ad_type_infos.proto\x12!google.ads.searchads360.v0.common\x1a0google/ads/searchads360/v0/common/ad_asset.proto"\xa6\x02\n\x16SearchAds360TextAdInfo\x12\x15\n\x08headline\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0cdescription1\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x19\n\x0cdescription2\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0bdisplay_url\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1f\n\x12display_mobile_url\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x1b\n\x0ead_tracking_id\x18\x06 \x01(\x03H\x05\x88\x01\x01B\x0b\n\t_headlineB\x0f\n\r_description1B\x0f\n\r_description2B\x0e\n\x0c_display_urlB\x15\n\x13_display_mobile_urlB\x11\n\x0f_ad_tracking_id"\xd4\x02\n\x1eSearchAds360ExpandedTextAdInfo\x12\x15\n\x08headline\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\theadline2\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\theadline3\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x19\n\x0cdescription1\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x19\n\x0cdescription2\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x12\n\x05path1\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x12\n\x05path2\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x1b\n\x0ead_tracking_id\x18\x08 \x01(\x03H\x07\x88\x01\x01B\x0b\n\t_headlineB\x0c\n\n_headline2B\x0c\n\n_headline3B\x0f\n\r_description1B\x0f\n\r_description2B\x08\n\x06_path1B\x08\n\x06_path2B\x11\n\x0f_ad_tracking_id"\xb1\x01\n\'SearchAds360ExpandedDynamicSearchAdInfo\x12\x19\n\x0cdescription1\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0cdescription2\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1b\n\x0ead_tracking_id\x18\x03 \x01(\x03H\x02\x88\x01\x01B\x0f\n\r_description1B\x0f\n\r_description2B\x11\n\x0f_ad_tracking_id"\x1b\n\x19SearchAds360ProductAdInfo"\x99\x02\n"SearchAds360ResponsiveSearchAdInfo\x12\x12\n\x05path1\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05path2\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1b\n\x0ead_tracking_id\x18\x03 \x01(\x03H\x02\x88\x01\x01\x12A\n\theadlines\x18\x04 \x03(\x0b2..google.ads.searchads360.v0.common.AdTextAsset\x12D\n\x0cdescriptions\x18\x05 \x03(\x0b2..google.ads.searchads360.v0.common.AdTextAssetB\x08\n\x06_path1B\x08\n\x06_path2B\x11\n\x0f_ad_tracking_idB\xfe\x01\n%com.google.ads.searchads360.v0.commonB\x10AdTypeInfosProtoP\x01ZGgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/common;common\xa2\x02\x07GASA360\xaa\x02!Google.Ads.SearchAds360.V0.Common\xca\x02!Google\\Ads\\SearchAds360\\V0\\Common\xea\x02%Google::Ads::SearchAds360::V0::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.common.ad_type_infos_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.searchads360.v0.commonB\x10AdTypeInfosProtoP\x01ZGgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/common;common\xa2\x02\x07GASA360\xaa\x02!Google.Ads.SearchAds360.V0.Common\xca\x02!Google\\Ads\\SearchAds360\\V0\\Common\xea\x02%Google::Ads::SearchAds360::V0::Common'
    _globals['_SEARCHADS360TEXTADINFO']._serialized_start = 143
    _globals['_SEARCHADS360TEXTADINFO']._serialized_end = 437
    _globals['_SEARCHADS360EXPANDEDTEXTADINFO']._serialized_start = 440
    _globals['_SEARCHADS360EXPANDEDTEXTADINFO']._serialized_end = 780
    _globals['_SEARCHADS360EXPANDEDDYNAMICSEARCHADINFO']._serialized_start = 783
    _globals['_SEARCHADS360EXPANDEDDYNAMICSEARCHADINFO']._serialized_end = 960
    _globals['_SEARCHADS360PRODUCTADINFO']._serialized_start = 962
    _globals['_SEARCHADS360PRODUCTADINFO']._serialized_end = 989
    _globals['_SEARCHADS360RESPONSIVESEARCHADINFO']._serialized_start = 992
    _globals['_SEARCHADS360RESPONSIVESEARCHADINFO']._serialized_end = 1273