"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/analytics/admin/v1alpha/subproperty_event_filter.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/analytics/admin/v1alpha/subproperty_event_filter.proto\x12\x1egoogle.analytics.admin.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x81\x04\n\x1fSubpropertyEventFilterCondition\x12\x15\n\x0bnull_filter\x18\x02 \x01(\x08H\x00\x12e\n\rstring_filter\x18\x03 \x01(\x0b2L.google.analytics.admin.v1alpha.SubpropertyEventFilterCondition.StringFilterH\x00\x12\x17\n\nfield_name\x18\x01 \x01(\tB\x03\xe0A\x02\x1a\xb8\x02\n\x0cStringFilter\x12o\n\nmatch_type\x18\x01 \x01(\x0e2V.google.analytics.admin.v1alpha.SubpropertyEventFilterCondition.StringFilter.MatchTypeB\x03\xe0A\x02\x12\x12\n\x05value\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0ecase_sensitive\x18\x03 \x01(\x08B\x03\xe0A\x01"\x85\x01\n\tMatchType\x12\x1a\n\x16MATCH_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05EXACT\x10\x01\x12\x0f\n\x0bBEGINS_WITH\x10\x02\x12\r\n\tENDS_WITH\x10\x03\x12\x0c\n\x08CONTAINS\x10\x04\x12\x0f\n\x0bFULL_REGEXP\x10\x05\x12\x12\n\x0ePARTIAL_REGEXP\x10\x06B\x0c\n\none_filter"\xbd\x02\n SubpropertyEventFilterExpression\x12X\n\x08or_group\x18\x01 \x01(\x0b2D.google.analytics.admin.v1alpha.SubpropertyEventFilterExpressionListH\x00\x12Z\n\x0enot_expression\x18\x02 \x01(\x0b2@.google.analytics.admin.v1alpha.SubpropertyEventFilterExpressionH\x00\x12[\n\x10filter_condition\x18\x03 \x01(\x0b2?.google.analytics.admin.v1alpha.SubpropertyEventFilterConditionH\x00B\x06\n\x04expr"\x8c\x01\n$SubpropertyEventFilterExpressionList\x12d\n\x12filter_expressions\x18\x01 \x03(\x0b2@.google.analytics.admin.v1alpha.SubpropertyEventFilterExpressionB\x06\xe0A\x02\xe0A\x06"\xc2\x02\n\x1cSubpropertyEventFilterClause\x12n\n\x12filter_clause_type\x18\x01 \x01(\x0e2M.google.analytics.admin.v1alpha.SubpropertyEventFilterClause.FilterClauseTypeB\x03\xe0A\x02\x12`\n\x11filter_expression\x18\x02 \x01(\x0b2@.google.analytics.admin.v1alpha.SubpropertyEventFilterExpressionB\x03\xe0A\x02"P\n\x10FilterClauseType\x12"\n\x1eFILTER_CLAUSE_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07INCLUDE\x10\x01\x12\x0b\n\x07EXCLUDE\x10\x02"\xfd\x02\n\x16SubpropertyEventFilter\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12#\n\x11apply_to_property\x18\x02 \x01(\tB\x03\xe0A\x05H\x00\x88\x01\x01\x12\\\n\x0efilter_clauses\x18\x03 \x03(\x0b2<.google.analytics.admin.v1alpha.SubpropertyEventFilterClauseB\x06\xe0A\x02\xe0A\x06:\xb6\x01\xeaA\xb2\x01\n4analyticsadmin.googleapis.com/SubpropertyEventFilter\x12Iproperties/{property}/subpropertyEventFilters/{sub_property_event_filter}*\x17subpropertyEventFilters2\x16subpropertyEventFilterB\x14\n\x12_apply_to_propertyB\x83\x01\n"com.google.analytics.admin.v1alphaB\x1bSubpropertyEventFilterProtoP\x01Z>cloud.google.com/go/analytics/admin/apiv1alpha/adminpb;adminpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.analytics.admin.v1alpha.subproperty_event_filter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.analytics.admin.v1alphaB\x1bSubpropertyEventFilterProtoP\x01Z>cloud.google.com/go/analytics/admin/apiv1alpha/adminpb;adminpb'
    _globals['_SUBPROPERTYEVENTFILTERCONDITION_STRINGFILTER'].fields_by_name['match_type']._loaded_options = None
    _globals['_SUBPROPERTYEVENTFILTERCONDITION_STRINGFILTER'].fields_by_name['match_type']._serialized_options = b'\xe0A\x02'
    _globals['_SUBPROPERTYEVENTFILTERCONDITION_STRINGFILTER'].fields_by_name['value']._loaded_options = None
    _globals['_SUBPROPERTYEVENTFILTERCONDITION_STRINGFILTER'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_SUBPROPERTYEVENTFILTERCONDITION_STRINGFILTER'].fields_by_name['case_sensitive']._loaded_options = None
    _globals['_SUBPROPERTYEVENTFILTERCONDITION_STRINGFILTER'].fields_by_name['case_sensitive']._serialized_options = b'\xe0A\x01'
    _globals['_SUBPROPERTYEVENTFILTERCONDITION'].fields_by_name['field_name']._loaded_options = None
    _globals['_SUBPROPERTYEVENTFILTERCONDITION'].fields_by_name['field_name']._serialized_options = b'\xe0A\x02'
    _globals['_SUBPROPERTYEVENTFILTEREXPRESSIONLIST'].fields_by_name['filter_expressions']._loaded_options = None
    _globals['_SUBPROPERTYEVENTFILTEREXPRESSIONLIST'].fields_by_name['filter_expressions']._serialized_options = b'\xe0A\x02\xe0A\x06'
    _globals['_SUBPROPERTYEVENTFILTERCLAUSE'].fields_by_name['filter_clause_type']._loaded_options = None
    _globals['_SUBPROPERTYEVENTFILTERCLAUSE'].fields_by_name['filter_clause_type']._serialized_options = b'\xe0A\x02'
    _globals['_SUBPROPERTYEVENTFILTERCLAUSE'].fields_by_name['filter_expression']._loaded_options = None
    _globals['_SUBPROPERTYEVENTFILTERCLAUSE'].fields_by_name['filter_expression']._serialized_options = b'\xe0A\x02'
    _globals['_SUBPROPERTYEVENTFILTER'].fields_by_name['name']._loaded_options = None
    _globals['_SUBPROPERTYEVENTFILTER'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SUBPROPERTYEVENTFILTER'].fields_by_name['apply_to_property']._loaded_options = None
    _globals['_SUBPROPERTYEVENTFILTER'].fields_by_name['apply_to_property']._serialized_options = b'\xe0A\x05'
    _globals['_SUBPROPERTYEVENTFILTER'].fields_by_name['filter_clauses']._loaded_options = None
    _globals['_SUBPROPERTYEVENTFILTER'].fields_by_name['filter_clauses']._serialized_options = b'\xe0A\x02\xe0A\x06'
    _globals['_SUBPROPERTYEVENTFILTER']._loaded_options = None
    _globals['_SUBPROPERTYEVENTFILTER']._serialized_options = b'\xeaA\xb2\x01\n4analyticsadmin.googleapis.com/SubpropertyEventFilter\x12Iproperties/{property}/subpropertyEventFilters/{sub_property_event_filter}*\x17subpropertyEventFilters2\x16subpropertyEventFilter'
    _globals['_SUBPROPERTYEVENTFILTERCONDITION']._serialized_start = 158
    _globals['_SUBPROPERTYEVENTFILTERCONDITION']._serialized_end = 671
    _globals['_SUBPROPERTYEVENTFILTERCONDITION_STRINGFILTER']._serialized_start = 345
    _globals['_SUBPROPERTYEVENTFILTERCONDITION_STRINGFILTER']._serialized_end = 657
    _globals['_SUBPROPERTYEVENTFILTERCONDITION_STRINGFILTER_MATCHTYPE']._serialized_start = 524
    _globals['_SUBPROPERTYEVENTFILTERCONDITION_STRINGFILTER_MATCHTYPE']._serialized_end = 657
    _globals['_SUBPROPERTYEVENTFILTEREXPRESSION']._serialized_start = 674
    _globals['_SUBPROPERTYEVENTFILTEREXPRESSION']._serialized_end = 991
    _globals['_SUBPROPERTYEVENTFILTEREXPRESSIONLIST']._serialized_start = 994
    _globals['_SUBPROPERTYEVENTFILTEREXPRESSIONLIST']._serialized_end = 1134
    _globals['_SUBPROPERTYEVENTFILTERCLAUSE']._serialized_start = 1137
    _globals['_SUBPROPERTYEVENTFILTERCLAUSE']._serialized_end = 1459
    _globals['_SUBPROPERTYEVENTFILTERCLAUSE_FILTERCLAUSETYPE']._serialized_start = 1379
    _globals['_SUBPROPERTYEVENTFILTERCLAUSE_FILTERCLAUSETYPE']._serialized_end = 1459
    _globals['_SUBPROPERTYEVENTFILTER']._serialized_start = 1462
    _globals['_SUBPROPERTYEVENTFILTER']._serialized_end = 1843