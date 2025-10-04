"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/common/user_lists.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import customer_match_upload_key_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_customer__match__upload__key__type__pb2
from ......google.ads.googleads.v19.enums import lookalike_expansion_level_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_lookalike__expansion__level__pb2
from ......google.ads.googleads.v19.enums import user_list_crm_data_source_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_user__list__crm__data__source__type__pb2
from ......google.ads.googleads.v19.enums import user_list_date_rule_item_operator_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_user__list__date__rule__item__operator__pb2
from ......google.ads.googleads.v19.enums import user_list_flexible_rule_operator_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_user__list__flexible__rule__operator__pb2
from ......google.ads.googleads.v19.enums import user_list_logical_rule_operator_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_user__list__logical__rule__operator__pb2
from ......google.ads.googleads.v19.enums import user_list_number_rule_item_operator_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_user__list__number__rule__item__operator__pb2
from ......google.ads.googleads.v19.enums import user_list_prepopulation_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_user__list__prepopulation__status__pb2
from ......google.ads.googleads.v19.enums import user_list_rule_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_user__list__rule__type__pb2
from ......google.ads.googleads.v19.enums import user_list_string_rule_item_operator_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_user__list__string__rule__item__operator__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/ads/googleads/v19/common/user_lists.proto\x12\x1fgoogle.ads.googleads.v19.common\x1aCgoogle/ads/googleads/v19/enums/customer_match_upload_key_type.proto\x1a>google/ads/googleads/v19/enums/lookalike_expansion_level.proto\x1aCgoogle/ads/googleads/v19/enums/user_list_crm_data_source_type.proto\x1aFgoogle/ads/googleads/v19/enums/user_list_date_rule_item_operator.proto\x1aEgoogle/ads/googleads/v19/enums/user_list_flexible_rule_operator.proto\x1aDgoogle/ads/googleads/v19/enums/user_list_logical_rule_operator.proto\x1aHgoogle/ads/googleads/v19/enums/user_list_number_rule_item_operator.proto\x1aCgoogle/ads/googleads/v19/enums/user_list_prepopulation_status.proto\x1a8google/ads/googleads/v19/enums/user_list_rule_type.proto\x1aHgoogle/ads/googleads/v19/enums/user_list_string_rule_item_operator.proto"\xb8\x01\n\x15LookalikeUserListInfo\x12\x1a\n\x12seed_user_list_ids\x18\x01 \x03(\x03\x12l\n\x0fexpansion_level\x18\x02 \x01(\x0e2S.google.ads.googleads.v19.enums.LookalikeExpansionLevelEnum.LookalikeExpansionLevel\x12\x15\n\rcountry_codes\x18\x03 \x03(\t"E\n\x13SimilarUserListInfo\x12\x1b\n\x0eseed_user_list\x18\x02 \x01(\tH\x00\x88\x01\x01B\x11\n\x0f_seed_user_list"\x9d\x02\n\x14CrmBasedUserListInfo\x12\x13\n\x06app_id\x18\x04 \x01(\tH\x00\x88\x01\x01\x12r\n\x0fupload_key_type\x18\x02 \x01(\x0e2Y.google.ads.googleads.v19.enums.CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType\x12q\n\x10data_source_type\x18\x03 \x01(\x0e2W.google.ads.googleads.v19.enums.UserListCrmDataSourceTypeEnum.UserListCrmDataSourceTypeB\t\n\x07_app_id"\xc2\x01\n\x10UserListRuleInfo\x12X\n\trule_type\x18\x01 \x01(\x0e2E.google.ads.googleads.v19.enums.UserListRuleTypeEnum.UserListRuleType\x12T\n\x10rule_item_groups\x18\x02 \x03(\x0b2:.google.ads.googleads.v19.common.UserListRuleItemGroupInfo"f\n\x19UserListRuleItemGroupInfo\x12I\n\nrule_items\x18\x01 \x03(\x0b25.google.ads.googleads.v19.common.UserListRuleItemInfo"\xc6\x02\n\x14UserListRuleItemInfo\x12\x11\n\x04name\x18\x05 \x01(\tH\x01\x88\x01\x01\x12W\n\x10number_rule_item\x18\x02 \x01(\x0b2;.google.ads.googleads.v19.common.UserListNumberRuleItemInfoH\x00\x12W\n\x10string_rule_item\x18\x03 \x01(\x0b2;.google.ads.googleads.v19.common.UserListStringRuleItemInfoH\x00\x12S\n\x0edate_rule_item\x18\x04 \x01(\x0b29.google.ads.googleads.v19.common.UserListDateRuleItemInfoH\x00B\x0b\n\trule_itemB\x07\n\x05_name"\xd9\x01\n\x18UserListDateRuleItemInfo\x12o\n\x08operator\x18\x01 \x01(\x0e2].google.ads.googleads.v19.enums.UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator\x12\x12\n\x05value\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0eoffset_in_days\x18\x05 \x01(\x03H\x01\x88\x01\x01B\x08\n\x06_valueB\x11\n\x0f_offset_in_days"\xaf\x01\n\x1aUserListNumberRuleItemInfo\x12s\n\x08operator\x18\x01 \x01(\x0e2a.google.ads.googleads.v19.enums.UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator\x12\x12\n\x05value\x18\x03 \x01(\x01H\x00\x88\x01\x01B\x08\n\x06_value"\xaf\x01\n\x1aUserListStringRuleItemInfo\x12s\n\x08operator\x18\x01 \x01(\x0e2a.google.ads.googleads.v19.enums.UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator\x12\x12\n\x05value\x18\x03 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value"\x96\x01\n\x17FlexibleRuleOperandInfo\x12?\n\x04rule\x18\x01 \x01(\x0b21.google.ads.googleads.v19.common.UserListRuleInfo\x12!\n\x14lookback_window_days\x18\x02 \x01(\x03H\x00\x88\x01\x01B\x17\n\x15_lookback_window_days"\xc6\x02\n\x18FlexibleRuleUserListInfo\x12~\n\x17inclusive_rule_operator\x18\x01 \x01(\x0e2].google.ads.googleads.v19.enums.UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator\x12T\n\x12inclusive_operands\x18\x02 \x03(\x0b28.google.ads.googleads.v19.common.FlexibleRuleOperandInfo\x12T\n\x12exclusive_operands\x18\x03 \x03(\x0b28.google.ads.googleads.v19.common.FlexibleRuleOperandInfo"\xee\x01\n\x15RuleBasedUserListInfo\x12y\n\x14prepopulation_status\x18\x01 \x01(\x0e2[.google.ads.googleads.v19.enums.UserListPrepopulationStatusEnum.UserListPrepopulationStatus\x12Z\n\x17flexible_rule_user_list\x18\x05 \x01(\x0b29.google.ads.googleads.v19.common.FlexibleRuleUserListInfo"^\n\x13LogicalUserListInfo\x12G\n\x05rules\x18\x01 \x03(\x0b28.google.ads.googleads.v19.common.UserListLogicalRuleInfo"\xdc\x01\n\x17UserListLogicalRuleInfo\x12m\n\x08operator\x18\x01 \x01(\x0e2[.google.ads.googleads.v19.enums.UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator\x12R\n\rrule_operands\x18\x02 \x03(\x0b2;.google.ads.googleads.v19.common.LogicalUserListOperandInfo"B\n\x1aLogicalUserListOperandInfo\x12\x16\n\tuser_list\x18\x02 \x01(\tH\x00\x88\x01\x01B\x0c\n\n_user_list"Y\n\x11BasicUserListInfo\x12D\n\x07actions\x18\x01 \x03(\x0b23.google.ads.googleads.v19.common.UserListActionInfo"c\n\x12UserListActionInfo\x12\x1b\n\x11conversion_action\x18\x03 \x01(\tH\x00\x12\x1c\n\x12remarketing_action\x18\x04 \x01(\tH\x00B\x12\n\x10user_list_actionB\xee\x01\n#com.google.ads.googleads.v19.commonB\x0eUserListsProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.common.user_lists_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v19.commonB\x0eUserListsProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Common'
    _globals['_LOOKALIKEUSERLISTINFO']._serialized_start = 776
    _globals['_LOOKALIKEUSERLISTINFO']._serialized_end = 960
    _globals['_SIMILARUSERLISTINFO']._serialized_start = 962
    _globals['_SIMILARUSERLISTINFO']._serialized_end = 1031
    _globals['_CRMBASEDUSERLISTINFO']._serialized_start = 1034
    _globals['_CRMBASEDUSERLISTINFO']._serialized_end = 1319
    _globals['_USERLISTRULEINFO']._serialized_start = 1322
    _globals['_USERLISTRULEINFO']._serialized_end = 1516
    _globals['_USERLISTRULEITEMGROUPINFO']._serialized_start = 1518
    _globals['_USERLISTRULEITEMGROUPINFO']._serialized_end = 1620
    _globals['_USERLISTRULEITEMINFO']._serialized_start = 1623
    _globals['_USERLISTRULEITEMINFO']._serialized_end = 1949
    _globals['_USERLISTDATERULEITEMINFO']._serialized_start = 1952
    _globals['_USERLISTDATERULEITEMINFO']._serialized_end = 2169
    _globals['_USERLISTNUMBERRULEITEMINFO']._serialized_start = 2172
    _globals['_USERLISTNUMBERRULEITEMINFO']._serialized_end = 2347
    _globals['_USERLISTSTRINGRULEITEMINFO']._serialized_start = 2350
    _globals['_USERLISTSTRINGRULEITEMINFO']._serialized_end = 2525
    _globals['_FLEXIBLERULEOPERANDINFO']._serialized_start = 2528
    _globals['_FLEXIBLERULEOPERANDINFO']._serialized_end = 2678
    _globals['_FLEXIBLERULEUSERLISTINFO']._serialized_start = 2681
    _globals['_FLEXIBLERULEUSERLISTINFO']._serialized_end = 3007
    _globals['_RULEBASEDUSERLISTINFO']._serialized_start = 3010
    _globals['_RULEBASEDUSERLISTINFO']._serialized_end = 3248
    _globals['_LOGICALUSERLISTINFO']._serialized_start = 3250
    _globals['_LOGICALUSERLISTINFO']._serialized_end = 3344
    _globals['_USERLISTLOGICALRULEINFO']._serialized_start = 3347
    _globals['_USERLISTLOGICALRULEINFO']._serialized_end = 3567
    _globals['_LOGICALUSERLISTOPERANDINFO']._serialized_start = 3569
    _globals['_LOGICALUSERLISTOPERANDINFO']._serialized_end = 3635
    _globals['_BASICUSERLISTINFO']._serialized_start = 3637
    _globals['_BASICUSERLISTINFO']._serialized_end = 3726
    _globals['_USERLISTACTIONINFO']._serialized_start = 3728
    _globals['_USERLISTACTIONINFO']._serialized_end = 3827