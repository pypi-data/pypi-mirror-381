"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/click_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import click_location_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_click__location__pb2
from ......google.ads.googleads.v20.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_criteria__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/googleads/v20/resources/click_view.proto\x12"google.ads.googleads.v20.resources\x1a4google/ads/googleads/v20/common/click_location.proto\x1a.google/ads/googleads/v20/common/criteria.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xca\x06\n\tClickView\x12A\n\rresource_name\x18\x01 \x01(\tB*\xe0A\x03\xfaA$\n"googleads.googleapis.com/ClickView\x12\x17\n\x05gclid\x18\x08 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12M\n\x10area_of_interest\x18\x03 \x01(\x0b2..google.ads.googleads.v20.common.ClickLocationB\x03\xe0A\x03\x12Q\n\x14location_of_presence\x18\x04 \x01(\x0b2..google.ads.googleads.v20.common.ClickLocationB\x03\xe0A\x03\x12\x1d\n\x0bpage_number\x18\t \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12D\n\x0bad_group_ad\x18\n \x01(\tB*\xe0A\x03\xfaA$\n"googleads.googleapis.com/AdGroupAdH\x02\x88\x01\x01\x12Y\n\x18campaign_location_target\x18\x0b \x01(\tB2\xe0A\x03\xfaA,\n*googleads.googleapis.com/GeoTargetConstantH\x03\x88\x01\x01\x12A\n\tuser_list\x18\x0c \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/UserListH\x04\x88\x01\x01\x12B\n\x07keyword\x18\r \x01(\tB1\xe0A\x03\xfaA+\n)googleads.googleapis.com/AdGroupCriterion\x12G\n\x0ckeyword_info\x18\x0e \x01(\x0b2,.google.ads.googleads.v20.common.KeywordInfoB\x03\xe0A\x03:Z\xeaAW\n"googleads.googleapis.com/ClickView\x121customers/{customer_id}/clickViews/{date}~{gclid}B\x08\n\x06_gclidB\x0e\n\x0c_page_numberB\x0e\n\x0c_ad_group_adB\x1b\n\x19_campaign_location_targetB\x0c\n\n_user_listB\x80\x02\n&com.google.ads.googleads.v20.resourcesB\x0eClickViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.click_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x0eClickViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_CLICKVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CLICKVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA$\n"googleads.googleapis.com/ClickView'
    _globals['_CLICKVIEW'].fields_by_name['gclid']._loaded_options = None
    _globals['_CLICKVIEW'].fields_by_name['gclid']._serialized_options = b'\xe0A\x03'
    _globals['_CLICKVIEW'].fields_by_name['area_of_interest']._loaded_options = None
    _globals['_CLICKVIEW'].fields_by_name['area_of_interest']._serialized_options = b'\xe0A\x03'
    _globals['_CLICKVIEW'].fields_by_name['location_of_presence']._loaded_options = None
    _globals['_CLICKVIEW'].fields_by_name['location_of_presence']._serialized_options = b'\xe0A\x03'
    _globals['_CLICKVIEW'].fields_by_name['page_number']._loaded_options = None
    _globals['_CLICKVIEW'].fields_by_name['page_number']._serialized_options = b'\xe0A\x03'
    _globals['_CLICKVIEW'].fields_by_name['ad_group_ad']._loaded_options = None
    _globals['_CLICKVIEW'].fields_by_name['ad_group_ad']._serialized_options = b'\xe0A\x03\xfaA$\n"googleads.googleapis.com/AdGroupAd'
    _globals['_CLICKVIEW'].fields_by_name['campaign_location_target']._loaded_options = None
    _globals['_CLICKVIEW'].fields_by_name['campaign_location_target']._serialized_options = b'\xe0A\x03\xfaA,\n*googleads.googleapis.com/GeoTargetConstant'
    _globals['_CLICKVIEW'].fields_by_name['user_list']._loaded_options = None
    _globals['_CLICKVIEW'].fields_by_name['user_list']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/UserList'
    _globals['_CLICKVIEW'].fields_by_name['keyword']._loaded_options = None
    _globals['_CLICKVIEW'].fields_by_name['keyword']._serialized_options = b'\xe0A\x03\xfaA+\n)googleads.googleapis.com/AdGroupCriterion'
    _globals['_CLICKVIEW'].fields_by_name['keyword_info']._loaded_options = None
    _globals['_CLICKVIEW'].fields_by_name['keyword_info']._serialized_options = b'\xe0A\x03'
    _globals['_CLICKVIEW']._loaded_options = None
    _globals['_CLICKVIEW']._serialized_options = b'\xeaAW\n"googleads.googleapis.com/ClickView\x121customers/{customer_id}/clickViews/{date}~{gclid}'
    _globals['_CLICKVIEW']._serialized_start = 254
    _globals['_CLICKVIEW']._serialized_end = 1096