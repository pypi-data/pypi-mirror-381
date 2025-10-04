"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/netapp/v1/quota_rule.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/netapp/v1/quota_rule.proto\x12\x16google.cloud.netapp.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xad\x01\n\x15ListQuotaRulesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fnetapp.googleapis.com/QuotaRule\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"~\n\x16ListQuotaRulesResponse\x126\n\x0bquota_rules\x18\x01 \x03(\x0b2!.google.cloud.netapp.v1.QuotaRule\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"L\n\x13GetQuotaRuleRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fnetapp.googleapis.com/QuotaRule"\xa9\x01\n\x16CreateQuotaRuleRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fnetapp.googleapis.com/QuotaRule\x12:\n\nquota_rule\x18\x02 \x01(\x0b2!.google.cloud.netapp.v1.QuotaRuleB\x03\xe0A\x02\x12\x1a\n\rquota_rule_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x8a\x01\n\x16UpdateQuotaRuleRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12:\n\nquota_rule\x18\x02 \x01(\x0b2!.google.cloud.netapp.v1.QuotaRuleB\x03\xe0A\x02"O\n\x16DeleteQuotaRuleRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fnetapp.googleapis.com/QuotaRule"\x9f\x06\n\tQuotaRule\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x13\n\x06target\x18\x02 \x01(\tB\x03\xe0A\x01\x129\n\x04type\x18\x03 \x01(\x0e2&.google.cloud.netapp.v1.QuotaRule.TypeB\x03\xe0A\x02\x12\x1b\n\x0edisk_limit_mib\x18\x04 \x01(\x05B\x03\xe0A\x02\x12;\n\x05state\x18\x06 \x01(\x0e2\'.google.cloud.netapp.v1.QuotaRule.StateB\x03\xe0A\x03\x12\x1a\n\rstate_details\x18\x07 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\t \x01(\tB\x03\xe0A\x01\x12B\n\x06labels\x18\n \x03(\x0b2-.google.cloud.netapp.v1.QuotaRule.LabelsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x84\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15INDIVIDUAL_USER_QUOTA\x10\x01\x12\x1a\n\x16INDIVIDUAL_GROUP_QUOTA\x10\x02\x12\x16\n\x12DEFAULT_USER_QUOTA\x10\x03\x12\x17\n\x13DEFAULT_GROUP_QUOTA\x10\x04"^\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x0c\n\x08UPDATING\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\t\n\x05READY\x10\x04\x12\t\n\x05ERROR\x10\x05:\x8e\x01\xeaA\x8a\x01\n\x1fnetapp.googleapis.com/QuotaRule\x12Pprojects/{project}/locations/{location}/volumes/{volume}/quotaRules/{quota_rule}*\nquotaRules2\tquotaRuleB\xb0\x01\n\x1acom.google.cloud.netapp.v1B\x0eQuotaRuleProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.netapp.v1.quota_rule_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.netapp.v1B\x0eQuotaRuleProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1'
    _globals['_LISTQUOTARULESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTQUOTARULESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fnetapp.googleapis.com/QuotaRule'
    _globals['_LISTQUOTARULESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTQUOTARULESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTQUOTARULESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTQUOTARULESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTQUOTARULESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTQUOTARULESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTQUOTARULESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTQUOTARULESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETQUOTARULEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETQUOTARULEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fnetapp.googleapis.com/QuotaRule'
    _globals['_CREATEQUOTARULEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEQUOTARULEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fnetapp.googleapis.com/QuotaRule'
    _globals['_CREATEQUOTARULEREQUEST'].fields_by_name['quota_rule']._loaded_options = None
    _globals['_CREATEQUOTARULEREQUEST'].fields_by_name['quota_rule']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEQUOTARULEREQUEST'].fields_by_name['quota_rule_id']._loaded_options = None
    _globals['_CREATEQUOTARULEREQUEST'].fields_by_name['quota_rule_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEQUOTARULEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEQUOTARULEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEQUOTARULEREQUEST'].fields_by_name['quota_rule']._loaded_options = None
    _globals['_UPDATEQUOTARULEREQUEST'].fields_by_name['quota_rule']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEQUOTARULEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEQUOTARULEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fnetapp.googleapis.com/QuotaRule'
    _globals['_QUOTARULE_LABELSENTRY']._loaded_options = None
    _globals['_QUOTARULE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_QUOTARULE'].fields_by_name['name']._loaded_options = None
    _globals['_QUOTARULE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_QUOTARULE'].fields_by_name['target']._loaded_options = None
    _globals['_QUOTARULE'].fields_by_name['target']._serialized_options = b'\xe0A\x01'
    _globals['_QUOTARULE'].fields_by_name['type']._loaded_options = None
    _globals['_QUOTARULE'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_QUOTARULE'].fields_by_name['disk_limit_mib']._loaded_options = None
    _globals['_QUOTARULE'].fields_by_name['disk_limit_mib']._serialized_options = b'\xe0A\x02'
    _globals['_QUOTARULE'].fields_by_name['state']._loaded_options = None
    _globals['_QUOTARULE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTARULE'].fields_by_name['state_details']._loaded_options = None
    _globals['_QUOTARULE'].fields_by_name['state_details']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTARULE'].fields_by_name['create_time']._loaded_options = None
    _globals['_QUOTARULE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTARULE'].fields_by_name['description']._loaded_options = None
    _globals['_QUOTARULE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_QUOTARULE'].fields_by_name['labels']._loaded_options = None
    _globals['_QUOTARULE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_QUOTARULE']._loaded_options = None
    _globals['_QUOTARULE']._serialized_options = b'\xeaA\x8a\x01\n\x1fnetapp.googleapis.com/QuotaRule\x12Pprojects/{project}/locations/{location}/volumes/{volume}/quotaRules/{quota_rule}*\nquotaRules2\tquotaRule'
    _globals['_LISTQUOTARULESREQUEST']._serialized_start = 195
    _globals['_LISTQUOTARULESREQUEST']._serialized_end = 368
    _globals['_LISTQUOTARULESRESPONSE']._serialized_start = 370
    _globals['_LISTQUOTARULESRESPONSE']._serialized_end = 496
    _globals['_GETQUOTARULEREQUEST']._serialized_start = 498
    _globals['_GETQUOTARULEREQUEST']._serialized_end = 574
    _globals['_CREATEQUOTARULEREQUEST']._serialized_start = 577
    _globals['_CREATEQUOTARULEREQUEST']._serialized_end = 746
    _globals['_UPDATEQUOTARULEREQUEST']._serialized_start = 749
    _globals['_UPDATEQUOTARULEREQUEST']._serialized_end = 887
    _globals['_DELETEQUOTARULEREQUEST']._serialized_start = 889
    _globals['_DELETEQUOTARULEREQUEST']._serialized_end = 968
    _globals['_QUOTARULE']._serialized_start = 971
    _globals['_QUOTARULE']._serialized_end = 1770
    _globals['_QUOTARULE_LABELSENTRY']._serialized_start = 1349
    _globals['_QUOTARULE_LABELSENTRY']._serialized_end = 1394
    _globals['_QUOTARULE_TYPE']._serialized_start = 1397
    _globals['_QUOTARULE_TYPE']._serialized_end = 1529
    _globals['_QUOTARULE_STATE']._serialized_start = 1531
    _globals['_QUOTARULE_STATE']._serialized_end = 1625