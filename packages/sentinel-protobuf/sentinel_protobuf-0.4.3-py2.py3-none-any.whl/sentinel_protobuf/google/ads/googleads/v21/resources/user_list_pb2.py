"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/user_list.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import user_lists_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_user__lists__pb2
from ......google.ads.googleads.v21.enums import access_reason_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_access__reason__pb2
from ......google.ads.googleads.v21.enums import user_list_access_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_user__list__access__status__pb2
from ......google.ads.googleads.v21.enums import user_list_closing_reason_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_user__list__closing__reason__pb2
from ......google.ads.googleads.v21.enums import user_list_membership_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_user__list__membership__status__pb2
from ......google.ads.googleads.v21.enums import user_list_size_range_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_user__list__size__range__pb2
from ......google.ads.googleads.v21.enums import user_list_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_user__list__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/ads/googleads/v21/resources/user_list.proto\x12"google.ads.googleads.v21.resources\x1a0google/ads/googleads/v21/common/user_lists.proto\x1a2google/ads/googleads/v21/enums/access_reason.proto\x1a<google/ads/googleads/v21/enums/user_list_access_status.proto\x1a=google/ads/googleads/v21/enums/user_list_closing_reason.proto\x1a@google/ads/googleads/v21/enums/user_list_membership_status.proto\x1a9google/ads/googleads/v21/enums/user_list_size_range.proto\x1a3google/ads/googleads/v21/enums/user_list_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb7\x0f\n\x08UserList\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/UserList\x12\x14\n\x02id\x18\x19 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1b\n\tread_only\x18\x1a \x01(\x08B\x03\xe0A\x03H\x02\x88\x01\x01\x12\x11\n\x04name\x18\x1b \x01(\tH\x03\x88\x01\x01\x12\x18\n\x0bdescription\x18\x1c \x01(\tH\x04\x88\x01\x01\x12p\n\x11membership_status\x18\x06 \x01(\x0e2U.google.ads.googleads.v21.enums.UserListMembershipStatusEnum.UserListMembershipStatus\x12\x1d\n\x10integration_code\x18\x1d \x01(\tH\x05\x88\x01\x01\x12!\n\x14membership_life_span\x18\x1e \x01(\x03H\x06\x88\x01\x01\x12"\n\x10size_for_display\x18\x1f \x01(\x03B\x03\xe0A\x03H\x07\x88\x01\x01\x12l\n\x16size_range_for_display\x18\n \x01(\x0e2G.google.ads.googleads.v21.enums.UserListSizeRangeEnum.UserListSizeRangeB\x03\xe0A\x03\x12!\n\x0fsize_for_search\x18  \x01(\x03B\x03\xe0A\x03H\x08\x88\x01\x01\x12k\n\x15size_range_for_search\x18\x0c \x01(\x0e2G.google.ads.googleads.v21.enums.UserListSizeRangeEnum.UserListSizeRangeB\x03\xe0A\x03\x12P\n\x04type\x18\r \x01(\x0e2=.google.ads.googleads.v21.enums.UserListTypeEnum.UserListTypeB\x03\xe0A\x03\x12g\n\x0eclosing_reason\x18\x0e \x01(\x0e2O.google.ads.googleads.v21.enums.UserListClosingReasonEnum.UserListClosingReason\x12Y\n\raccess_reason\x18\x0f \x01(\x0e2=.google.ads.googleads.v21.enums.AccessReasonEnum.AccessReasonB\x03\xe0A\x03\x12o\n\x18account_user_list_status\x18\x10 \x01(\x0e2M.google.ads.googleads.v21.enums.UserListAccessStatusEnum.UserListAccessStatus\x12 \n\x13eligible_for_search\x18! \x01(\x08H\t\x88\x01\x01\x12&\n\x14eligible_for_display\x18" \x01(\x08B\x03\xe0A\x03H\n\x88\x01\x01\x12\'\n\x15match_rate_percentage\x18\x18 \x01(\x05B\x03\xe0A\x03H\x0b\x88\x01\x01\x12T\n\x13crm_based_user_list\x18\x13 \x01(\x0b25.google.ads.googleads.v21.common.CrmBasedUserListInfoH\x00\x12V\n\x11similar_user_list\x18\x14 \x01(\x0b24.google.ads.googleads.v21.common.SimilarUserListInfoB\x03\xe0A\x03H\x00\x12V\n\x14rule_based_user_list\x18\x15 \x01(\x0b26.google.ads.googleads.v21.common.RuleBasedUserListInfoH\x00\x12Q\n\x11logical_user_list\x18\x16 \x01(\x0b24.google.ads.googleads.v21.common.LogicalUserListInfoH\x00\x12M\n\x0fbasic_user_list\x18\x17 \x01(\x0b22.google.ads.googleads.v21.common.BasicUserListInfoH\x00\x12Z\n\x13lookalike_user_list\x18$ \x01(\x0b26.google.ads.googleads.v21.common.LookalikeUserListInfoB\x03\xe0A\x05H\x00:X\xeaAU\n!googleads.googleapis.com/UserList\x120customers/{customer_id}/userLists/{user_list_id}B\x0b\n\tuser_listB\x05\n\x03_idB\x0c\n\n_read_onlyB\x07\n\x05_nameB\x0e\n\x0c_descriptionB\x13\n\x11_integration_codeB\x17\n\x15_membership_life_spanB\x13\n\x11_size_for_displayB\x12\n\x10_size_for_searchB\x16\n\x14_eligible_for_searchB\x17\n\x15_eligible_for_displayB\x18\n\x16_match_rate_percentageB\xff\x01\n&com.google.ads.googleads.v21.resourcesB\rUserListProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.user_list_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\rUserListProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_USERLIST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/UserList'
    _globals['_USERLIST'].fields_by_name['id']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST'].fields_by_name['read_only']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['read_only']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST'].fields_by_name['size_for_display']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['size_for_display']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST'].fields_by_name['size_range_for_display']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['size_range_for_display']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST'].fields_by_name['size_for_search']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['size_for_search']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST'].fields_by_name['size_range_for_search']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['size_range_for_search']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST'].fields_by_name['type']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST'].fields_by_name['access_reason']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['access_reason']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST'].fields_by_name['eligible_for_display']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['eligible_for_display']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST'].fields_by_name['match_rate_percentage']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['match_rate_percentage']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST'].fields_by_name['similar_user_list']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['similar_user_list']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST'].fields_by_name['lookalike_user_list']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['lookalike_user_list']._serialized_options = b'\xe0A\x05'
    _globals['_USERLIST']._loaded_options = None
    _globals['_USERLIST']._serialized_options = b'\xeaAU\n!googleads.googleapis.com/UserList\x120customers/{customer_id}/userLists/{user_list_id}'
    _globals['_USERLIST']._serialized_start = 556
    _globals['_USERLIST']._serialized_end = 2531