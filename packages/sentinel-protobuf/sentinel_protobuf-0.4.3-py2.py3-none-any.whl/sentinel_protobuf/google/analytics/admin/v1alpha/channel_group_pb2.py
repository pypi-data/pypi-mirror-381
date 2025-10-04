"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/analytics/admin/v1alpha/channel_group.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/analytics/admin/v1alpha/channel_group.proto\x12\x1egoogle.analytics.admin.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xab\x04\n\x12ChannelGroupFilter\x12X\n\rstring_filter\x18\x02 \x01(\x0b2?.google.analytics.admin.v1alpha.ChannelGroupFilter.StringFilterH\x00\x12Y\n\x0ein_list_filter\x18\x03 \x01(\x0b2?.google.analytics.admin.v1alpha.ChannelGroupFilter.InListFilterH\x00\x12\x1a\n\nfield_name\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x1a\x8e\x02\n\x0cStringFilter\x12b\n\nmatch_type\x18\x01 \x01(\x0e2I.google.analytics.admin.v1alpha.ChannelGroupFilter.StringFilter.MatchTypeB\x03\xe0A\x02\x12\x12\n\x05value\x18\x02 \x01(\tB\x03\xe0A\x02"\x85\x01\n\tMatchType\x12\x1a\n\x16MATCH_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05EXACT\x10\x01\x12\x0f\n\x0bBEGINS_WITH\x10\x02\x12\r\n\tENDS_WITH\x10\x03\x12\x0c\n\x08CONTAINS\x10\x04\x12\x0f\n\x0bFULL_REGEXP\x10\x05\x12\x12\n\x0ePARTIAL_REGEXP\x10\x06\x1a#\n\x0cInListFilter\x12\x13\n\x06values\x18\x01 \x03(\tB\x03\xe0A\x02B\x0e\n\x0cvalue_filter"\xf1\x02\n\x1cChannelGroupFilterExpression\x12U\n\tand_group\x18\x01 \x01(\x0b2@.google.analytics.admin.v1alpha.ChannelGroupFilterExpressionListH\x00\x12T\n\x08or_group\x18\x02 \x01(\x0b2@.google.analytics.admin.v1alpha.ChannelGroupFilterExpressionListH\x00\x12V\n\x0enot_expression\x18\x03 \x01(\x0b2<.google.analytics.admin.v1alpha.ChannelGroupFilterExpressionH\x00\x12D\n\x06filter\x18\x04 \x01(\x0b22.google.analytics.admin.v1alpha.ChannelGroupFilterH\x00B\x06\n\x04expr"|\n ChannelGroupFilterExpressionList\x12X\n\x12filter_expressions\x18\x01 \x03(\x0b2<.google.analytics.admin.v1alpha.ChannelGroupFilterExpression"\x80\x01\n\x0cGroupingRule\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12U\n\nexpression\x18\x02 \x01(\x0b2<.google.analytics.admin.v1alpha.ChannelGroupFilterExpressionB\x03\xe0A\x02"\xb4\x02\n\x0cChannelGroup\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12H\n\rgrouping_rule\x18\x04 \x03(\x0b2,.google.analytics.admin.v1alpha.GroupingRuleB\x03\xe0A\x02\x12\x1b\n\x0esystem_defined\x18\x05 \x01(\x08B\x03\xe0A\x03\x12\x14\n\x07primary\x18\x06 \x01(\x08B\x03\xe0A\x01:d\xeaAa\n*analyticsadmin.googleapis.com/ChannelGroup\x123properties/{property}/channelGroups/{channel_group}By\n"com.google.analytics.admin.v1alphaB\x11ChannelGroupProtoP\x01Z>cloud.google.com/go/analytics/admin/apiv1alpha/adminpb;adminpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.analytics.admin.v1alpha.channel_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.analytics.admin.v1alphaB\x11ChannelGroupProtoP\x01Z>cloud.google.com/go/analytics/admin/apiv1alpha/adminpb;adminpb'
    _globals['_CHANNELGROUPFILTER_STRINGFILTER'].fields_by_name['match_type']._loaded_options = None
    _globals['_CHANNELGROUPFILTER_STRINGFILTER'].fields_by_name['match_type']._serialized_options = b'\xe0A\x02'
    _globals['_CHANNELGROUPFILTER_STRINGFILTER'].fields_by_name['value']._loaded_options = None
    _globals['_CHANNELGROUPFILTER_STRINGFILTER'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_CHANNELGROUPFILTER_INLISTFILTER'].fields_by_name['values']._loaded_options = None
    _globals['_CHANNELGROUPFILTER_INLISTFILTER'].fields_by_name['values']._serialized_options = b'\xe0A\x02'
    _globals['_CHANNELGROUPFILTER'].fields_by_name['field_name']._loaded_options = None
    _globals['_CHANNELGROUPFILTER'].fields_by_name['field_name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_GROUPINGRULE'].fields_by_name['display_name']._loaded_options = None
    _globals['_GROUPINGRULE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_GROUPINGRULE'].fields_by_name['expression']._loaded_options = None
    _globals['_GROUPINGRULE'].fields_by_name['expression']._serialized_options = b'\xe0A\x02'
    _globals['_CHANNELGROUP'].fields_by_name['name']._loaded_options = None
    _globals['_CHANNELGROUP'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELGROUP'].fields_by_name['display_name']._loaded_options = None
    _globals['_CHANNELGROUP'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CHANNELGROUP'].fields_by_name['grouping_rule']._loaded_options = None
    _globals['_CHANNELGROUP'].fields_by_name['grouping_rule']._serialized_options = b'\xe0A\x02'
    _globals['_CHANNELGROUP'].fields_by_name['system_defined']._loaded_options = None
    _globals['_CHANNELGROUP'].fields_by_name['system_defined']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNELGROUP'].fields_by_name['primary']._loaded_options = None
    _globals['_CHANNELGROUP'].fields_by_name['primary']._serialized_options = b'\xe0A\x01'
    _globals['_CHANNELGROUP']._loaded_options = None
    _globals['_CHANNELGROUP']._serialized_options = b'\xeaAa\n*analyticsadmin.googleapis.com/ChannelGroup\x123properties/{property}/channelGroups/{channel_group}'
    _globals['_CHANNELGROUPFILTER']._serialized_start = 147
    _globals['_CHANNELGROUPFILTER']._serialized_end = 702
    _globals['_CHANNELGROUPFILTER_STRINGFILTER']._serialized_start = 379
    _globals['_CHANNELGROUPFILTER_STRINGFILTER']._serialized_end = 649
    _globals['_CHANNELGROUPFILTER_STRINGFILTER_MATCHTYPE']._serialized_start = 516
    _globals['_CHANNELGROUPFILTER_STRINGFILTER_MATCHTYPE']._serialized_end = 649
    _globals['_CHANNELGROUPFILTER_INLISTFILTER']._serialized_start = 651
    _globals['_CHANNELGROUPFILTER_INLISTFILTER']._serialized_end = 686
    _globals['_CHANNELGROUPFILTEREXPRESSION']._serialized_start = 705
    _globals['_CHANNELGROUPFILTEREXPRESSION']._serialized_end = 1074
    _globals['_CHANNELGROUPFILTEREXPRESSIONLIST']._serialized_start = 1076
    _globals['_CHANNELGROUPFILTEREXPRESSIONLIST']._serialized_end = 1200
    _globals['_GROUPINGRULE']._serialized_start = 1203
    _globals['_GROUPINGRULE']._serialized_end = 1331
    _globals['_CHANNELGROUP']._serialized_start = 1334
    _globals['_CHANNELGROUP']._serialized_end = 1642