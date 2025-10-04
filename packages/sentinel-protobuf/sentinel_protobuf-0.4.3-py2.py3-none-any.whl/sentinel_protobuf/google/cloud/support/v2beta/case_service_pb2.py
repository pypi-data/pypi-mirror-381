"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/support/v2beta/case_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.support.v2beta import case_pb2 as google_dot_cloud_dot_support_dot_v2beta_dot_case__pb2
from .....google.cloud.support.v2beta import escalation_pb2 as google_dot_cloud_dot_support_dot_v2beta_dot_escalation__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/support/v2beta/case_service.proto\x12\x1bgoogle.cloud.support.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/support/v2beta/case.proto\x1a,google/cloud/support/v2beta/escalation.proto\x1a google/protobuf/field_mask.proto"H\n\x0eGetCaseRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case"\x83\x01\n\x11CreateCaseRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 cloudsupport.googleapis.com/Case\x124\n\x04case\x18\x02 \x01(\x0b2!.google.cloud.support.v2beta.CaseB\x03\xe0A\x02"\xd9\x01\n\x10ListCasesRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 cloudsupport.googleapis.com/Case\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\x12C\n\x0cproduct_line\x18\x08 \x01(\x0e2(.google.cloud.support.v2beta.ProductLineH\x00\x88\x01\x01B\x0f\n\r_product_line"^\n\x11ListCasesResponse\x120\n\x05cases\x18\x01 \x03(\x0b2!.google.cloud.support.v2beta.Case\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Z\n\x12SearchCasesRequest\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12\r\n\x05query\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"`\n\x13SearchCasesResponse\x120\n\x05cases\x18\x01 \x03(\x0b2!.google.cloud.support.v2beta.Case\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8a\x01\n\x13EscalateCaseRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case\x12;\n\nescalation\x18\x02 \x01(\x0b2\'.google.cloud.support.v2beta.Escalation"z\n\x11UpdateCaseRequest\x124\n\x04case\x18\x01 \x01(\x0b2!.google.cloud.support.v2beta.CaseB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"J\n\x10CloseCaseRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case"\x94\x01\n SearchCaseClassificationsRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12:\n\x07product\x18\x07 \x01(\x0b2$.google.cloud.support.v2beta.ProductB\x03\xe0A\x01"\x8b\x01\n!SearchCaseClassificationsResponse\x12M\n\x14case_classifications\x18\x01 \x03(\x0b2/.google.cloud.support.v2beta.CaseClassification\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xcb\r\n\x0bCaseService\x12\xb5\x01\n\x07GetCase\x12+.google.cloud.support.v2beta.GetCaseRequest\x1a!.google.cloud.support.v2beta.Case"Z\xdaA\x04name\x82\xd3\xe4\x93\x02M\x12!/v2beta/{name=projects/*/cases/*}Z(\x12&/v2beta/{name=organizations/*/cases/*}\x12\xc8\x01\n\tListCases\x12-.google.cloud.support.v2beta.ListCasesRequest\x1a..google.cloud.support.v2beta.ListCasesResponse"\\\xdaA\x06parent\x82\xd3\xe4\x93\x02M\x12!/v2beta/{parent=projects/*}/casesZ(\x12&/v2beta/{parent=organizations/*}/cases\x12\xd3\x01\n\x0bSearchCases\x12/.google.cloud.support.v2beta.SearchCasesRequest\x1a0.google.cloud.support.v2beta.SearchCasesResponse"a\x82\xd3\xe4\x93\x02[\x12(/v2beta/{parent=projects/*}/cases:searchZ/\x12-/v2beta/{parent=organizations/*}/cases:search\x12\xce\x01\n\nCreateCase\x12..google.cloud.support.v2beta.CreateCaseRequest\x1a!.google.cloud.support.v2beta.Case"m\xdaA\x0bparent,case\x82\xd3\xe4\x93\x02Y"!/v2beta/{parent=projects/*}/cases:\x04caseZ."&/v2beta/{parent=organizations/*}/cases:\x04case\x12\xdd\x01\n\nUpdateCase\x12..google.cloud.support.v2beta.UpdateCaseRequest\x1a!.google.cloud.support.v2beta.Case"|\xdaA\x10case,update_mask\x82\xd3\xe4\x93\x02c2&/v2beta/{case.name=projects/*/cases/*}:\x04caseZ32+/v2beta/{case.name=organizations/*/cases/*}:\x04case\x12\xd0\x01\n\x0cEscalateCase\x120.google.cloud.support.v2beta.EscalateCaseRequest\x1a!.google.cloud.support.v2beta.Case"k\x82\xd3\xe4\x93\x02e"*/v2beta/{name=projects/*/cases/*}:escalate:\x01*Z4"//v2beta/{name=organizations/*/cases/*}:escalate:\x01*\x12\xc4\x01\n\tCloseCase\x12-.google.cloud.support.v2beta.CloseCaseRequest\x1a!.google.cloud.support.v2beta.Case"e\x82\xd3\xe4\x93\x02_"\'/v2beta/{name=projects/*/cases/*}:close:\x01*Z1",/v2beta/{name=organizations/*/cases/*}:close:\x01*\x12\xc6\x01\n\x19SearchCaseClassifications\x12=.google.cloud.support.v2beta.SearchCaseClassificationsRequest\x1a>.google.cloud.support.v2beta.SearchCaseClassificationsResponse"*\x82\xd3\xe4\x93\x02$\x12"/v2beta/caseClassifications:search\x1aO\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xcd\x01\n\x1fcom.google.cloud.support.v2betaB\x10CaseServiceProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2beta.case_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.support.v2betaB\x10CaseServiceProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2beta'
    _globals['_GETCASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_CREATECASEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECASEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 cloudsupport.googleapis.com/Case'
    _globals['_CREATECASEREQUEST'].fields_by_name['case']._loaded_options = None
    _globals['_CREATECASEREQUEST'].fields_by_name['case']._serialized_options = b'\xe0A\x02'
    _globals['_LISTCASESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCASESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 cloudsupport.googleapis.com/Case'
    _globals['_ESCALATECASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ESCALATECASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_UPDATECASEREQUEST'].fields_by_name['case']._loaded_options = None
    _globals['_UPDATECASEREQUEST'].fields_by_name['case']._serialized_options = b'\xe0A\x02'
    _globals['_CLOSECASEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CLOSECASEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_SEARCHCASECLASSIFICATIONSREQUEST'].fields_by_name['product']._loaded_options = None
    _globals['_SEARCHCASECLASSIFICATIONSREQUEST'].fields_by_name['product']._serialized_options = b'\xe0A\x01'
    _globals['_CASESERVICE']._loaded_options = None
    _globals['_CASESERVICE']._serialized_options = b'\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CASESERVICE'].methods_by_name['GetCase']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['GetCase']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02M\x12!/v2beta/{name=projects/*/cases/*}Z(\x12&/v2beta/{name=organizations/*/cases/*}'
    _globals['_CASESERVICE'].methods_by_name['ListCases']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['ListCases']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02M\x12!/v2beta/{parent=projects/*}/casesZ(\x12&/v2beta/{parent=organizations/*}/cases'
    _globals['_CASESERVICE'].methods_by_name['SearchCases']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['SearchCases']._serialized_options = b'\x82\xd3\xe4\x93\x02[\x12(/v2beta/{parent=projects/*}/cases:searchZ/\x12-/v2beta/{parent=organizations/*}/cases:search'
    _globals['_CASESERVICE'].methods_by_name['CreateCase']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['CreateCase']._serialized_options = b'\xdaA\x0bparent,case\x82\xd3\xe4\x93\x02Y"!/v2beta/{parent=projects/*}/cases:\x04caseZ."&/v2beta/{parent=organizations/*}/cases:\x04case'
    _globals['_CASESERVICE'].methods_by_name['UpdateCase']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['UpdateCase']._serialized_options = b'\xdaA\x10case,update_mask\x82\xd3\xe4\x93\x02c2&/v2beta/{case.name=projects/*/cases/*}:\x04caseZ32+/v2beta/{case.name=organizations/*/cases/*}:\x04case'
    _globals['_CASESERVICE'].methods_by_name['EscalateCase']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['EscalateCase']._serialized_options = b'\x82\xd3\xe4\x93\x02e"*/v2beta/{name=projects/*/cases/*}:escalate:\x01*Z4"//v2beta/{name=organizations/*/cases/*}:escalate:\x01*'
    _globals['_CASESERVICE'].methods_by_name['CloseCase']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['CloseCase']._serialized_options = b'\x82\xd3\xe4\x93\x02_"\'/v2beta/{name=projects/*/cases/*}:close:\x01*Z1",/v2beta/{name=organizations/*/cases/*}:close:\x01*'
    _globals['_CASESERVICE'].methods_by_name['SearchCaseClassifications']._loaded_options = None
    _globals['_CASESERVICE'].methods_by_name['SearchCaseClassifications']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/v2beta/caseClassifications:search'
    _globals['_GETCASEREQUEST']._serialized_start = 314
    _globals['_GETCASEREQUEST']._serialized_end = 386
    _globals['_CREATECASEREQUEST']._serialized_start = 389
    _globals['_CREATECASEREQUEST']._serialized_end = 520
    _globals['_LISTCASESREQUEST']._serialized_start = 523
    _globals['_LISTCASESREQUEST']._serialized_end = 740
    _globals['_LISTCASESRESPONSE']._serialized_start = 742
    _globals['_LISTCASESRESPONSE']._serialized_end = 836
    _globals['_SEARCHCASESREQUEST']._serialized_start = 838
    _globals['_SEARCHCASESREQUEST']._serialized_end = 928
    _globals['_SEARCHCASESRESPONSE']._serialized_start = 930
    _globals['_SEARCHCASESRESPONSE']._serialized_end = 1026
    _globals['_ESCALATECASEREQUEST']._serialized_start = 1029
    _globals['_ESCALATECASEREQUEST']._serialized_end = 1167
    _globals['_UPDATECASEREQUEST']._serialized_start = 1169
    _globals['_UPDATECASEREQUEST']._serialized_end = 1291
    _globals['_CLOSECASEREQUEST']._serialized_start = 1293
    _globals['_CLOSECASEREQUEST']._serialized_end = 1367
    _globals['_SEARCHCASECLASSIFICATIONSREQUEST']._serialized_start = 1370
    _globals['_SEARCHCASECLASSIFICATIONSREQUEST']._serialized_end = 1518
    _globals['_SEARCHCASECLASSIFICATIONSRESPONSE']._serialized_start = 1521
    _globals['_SEARCHCASECLASSIFICATIONSRESPONSE']._serialized_end = 1660
    _globals['_CASESERVICE']._serialized_start = 1663
    _globals['_CASESERVICE']._serialized_end = 3402