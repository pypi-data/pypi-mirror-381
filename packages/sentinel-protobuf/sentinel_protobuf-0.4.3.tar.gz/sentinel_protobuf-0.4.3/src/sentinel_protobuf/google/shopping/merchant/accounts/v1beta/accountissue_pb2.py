"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1beta/accountissue.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/shopping/merchant/accounts/v1beta/accountissue.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/shopping/type/types.proto"\xb7\x06\n\x0cAccountIssue\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\r\n\x05title\x18\x02 \x01(\t\x12Q\n\x08severity\x18\x03 \x01(\x0e2?.google.shopping.merchant.accounts.v1beta.AccountIssue.Severity\x12i\n\x15impacted_destinations\x18\x04 \x03(\x0b2J.google.shopping.merchant.accounts.v1beta.AccountIssue.ImpactedDestination\x12\x0e\n\x06detail\x18\x05 \x01(\t\x12\x19\n\x11documentation_uri\x18\x06 \x01(\t\x1a\xde\x02\n\x13ImpactedDestination\x12[\n\x11reporting_context\x18\x01 \x01(\x0e2;.google.shopping.type.ReportingContext.ReportingContextEnumH\x00\x88\x01\x01\x12b\n\x07impacts\x18\x02 \x03(\x0b2Q.google.shopping.merchant.accounts.v1beta.AccountIssue.ImpactedDestination.Impact\x1ap\n\x06Impact\x12\x13\n\x0bregion_code\x18\x01 \x01(\t\x12Q\n\x08severity\x18\x02 \x01(\x0e2?.google.shopping.merchant.accounts.v1beta.AccountIssue.SeverityB\x14\n\x12_reporting_context"M\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08CRITICAL\x10\x01\x12\t\n\x05ERROR\x10\x02\x12\x0e\n\nSUGGESTION\x10\x03:l\xeaAi\n\'merchantapi.googleapis.com/AccountIssue\x12!accounts/{account}/issues/{issue}*\raccountIssues2\x0caccountIssue"\xbb\x01\n\x18ListAccountIssuesRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x16\n\ttime_zone\x18\x05 \x01(\tB\x03\xe0A\x01"\x84\x01\n\x19ListAccountIssuesResponse\x12N\n\x0eaccount_issues\x18\x01 \x03(\x0b26.google.shopping.merchant.accounts.v1beta.AccountIssue\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xbb\x02\n\x13AccountIssueService\x12\xda\x01\n\x11ListAccountIssues\x12B.google.shopping.merchant.accounts.v1beta.ListAccountIssuesRequest\x1aC.google.shopping.merchant.accounts.v1beta.ListAccountIssuesResponse"<\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/accounts/v1beta/{parent=accounts/*}/issues\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x93\x01\n,com.google.shopping.merchant.accounts.v1betaB\x11AccountIssueProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.accountissue_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\x11AccountIssueProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_ACCOUNTISSUE'].fields_by_name['name']._loaded_options = None
    _globals['_ACCOUNTISSUE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ACCOUNTISSUE']._loaded_options = None
    _globals['_ACCOUNTISSUE']._serialized_options = b"\xeaAi\n'merchantapi.googleapis.com/AccountIssue\x12!accounts/{account}/issues/{issue}*\raccountIssues2\x0caccountIssue"
    _globals['_LISTACCOUNTISSUESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACCOUNTISSUESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_LISTACCOUNTISSUESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTACCOUNTISSUESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCOUNTISSUESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTACCOUNTISSUESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCOUNTISSUESREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_LISTACCOUNTISSUESREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCOUNTISSUESREQUEST'].fields_by_name['time_zone']._loaded_options = None
    _globals['_LISTACCOUNTISSUESREQUEST'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x01'
    _globals['_ACCOUNTISSUESERVICE']._loaded_options = None
    _globals['_ACCOUNTISSUESERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_ACCOUNTISSUESERVICE'].methods_by_name['ListAccountIssues']._loaded_options = None
    _globals['_ACCOUNTISSUESERVICE'].methods_by_name['ListAccountIssues']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/accounts/v1beta/{parent=accounts/*}/issues'
    _globals['_ACCOUNTISSUE']._serialized_start = 255
    _globals['_ACCOUNTISSUE']._serialized_end = 1078
    _globals['_ACCOUNTISSUE_IMPACTEDDESTINATION']._serialized_start = 539
    _globals['_ACCOUNTISSUE_IMPACTEDDESTINATION']._serialized_end = 889
    _globals['_ACCOUNTISSUE_IMPACTEDDESTINATION_IMPACT']._serialized_start = 755
    _globals['_ACCOUNTISSUE_IMPACTEDDESTINATION_IMPACT']._serialized_end = 867
    _globals['_ACCOUNTISSUE_SEVERITY']._serialized_start = 891
    _globals['_ACCOUNTISSUE_SEVERITY']._serialized_end = 968
    _globals['_LISTACCOUNTISSUESREQUEST']._serialized_start = 1081
    _globals['_LISTACCOUNTISSUESREQUEST']._serialized_end = 1268
    _globals['_LISTACCOUNTISSUESRESPONSE']._serialized_start = 1271
    _globals['_LISTACCOUNTISSUESRESPONSE']._serialized_end = 1403
    _globals['_ACCOUNTISSUESERVICE']._serialized_start = 1406
    _globals['_ACCOUNTISSUESERVICE']._serialized_end = 1721