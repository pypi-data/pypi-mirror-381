"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/chronicle/v1/reference_list.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/chronicle/v1/reference_list.proto\x12\x19google.cloud.chronicle.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"]\n\tScopeInfo\x12P\n\x14reference_list_scope\x18\x02 \x01(\x0b2-.google.cloud.chronicle.v1.ReferenceListScopeB\x03\xe0A\x02".\n\x12ReferenceListScope\x12\x18\n\x0bscope_names\x18\x01 \x03(\tB\x03\xe0A\x01"\x93\x01\n\x17GetReferenceListRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&chronicle.googleapis.com/ReferenceList\x12:\n\x04view\x18\x02 \x01(\x0e2,.google.cloud.chronicle.v1.ReferenceListView"\xbe\x01\n\x19ListReferenceListsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&chronicle.googleapis.com/ReferenceList\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12:\n\x04view\x18\x04 \x01(\x0e2,.google.cloud.chronicle.v1.ReferenceListView"x\n\x1aListReferenceListsResponse\x12A\n\x0freference_lists\x18\x01 \x03(\x0b2(.google.cloud.chronicle.v1.ReferenceList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc3\x01\n\x1aCreateReferenceListRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&chronicle.googleapis.com/ReferenceList\x12E\n\x0ereference_list\x18\x02 \x01(\x0b2(.google.cloud.chronicle.v1.ReferenceListB\x03\xe0A\x02\x12\x1e\n\x11reference_list_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x94\x01\n\x1aUpdateReferenceListRequest\x12E\n\x0ereference_list\x18\x01 \x01(\x0b2(.google.cloud.chronicle.v1.ReferenceListB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xaa\x04\n\rReferenceList\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12=\n\x14revision_create_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x02\x12C\n\x07entries\x18\x05 \x03(\x0b2-.google.cloud.chronicle.v1.ReferenceListEntryB\x03\xe0A\x02\x12\x12\n\x05rules\x18\x06 \x03(\tB\x03\xe0A\x03\x12L\n\x0bsyntax_type\x18\x08 \x01(\x0e22.google.cloud.chronicle.v1.ReferenceListSyntaxTypeB\x03\xe0A\x02\x12$\n\x17rule_associations_count\x18\t \x01(\x05B\x03\xe0A\x03\x128\n\nscope_info\x18\x0b \x01(\x0b2$.google.cloud.chronicle.v1.ScopeInfo:\x8a\x01\xeaA\x86\x01\n&chronicle.googleapis.com/ReferenceList\x12\\projects/{project}/locations/{location}/instances/{instance}/referenceLists/{reference_list}"(\n\x12ReferenceListEntry\x12\x12\n\x05value\x18\x01 \x01(\tB\x03\xe0A\x02*\xc2\x01\n\x17ReferenceListSyntaxType\x12*\n&REFERENCE_LIST_SYNTAX_TYPE_UNSPECIFIED\x10\x00\x120\n,REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING\x10\x01\x12$\n REFERENCE_LIST_SYNTAX_TYPE_REGEX\x10\x02\x12#\n\x1fREFERENCE_LIST_SYNTAX_TYPE_CIDR\x10\x03*u\n\x11ReferenceListView\x12#\n\x1fREFERENCE_LIST_VIEW_UNSPECIFIED\x10\x00\x12\x1d\n\x19REFERENCE_LIST_VIEW_BASIC\x10\x01\x12\x1c\n\x18REFERENCE_LIST_VIEW_FULL\x10\x022\xf5\x07\n\x14ReferenceListService\x12\xbf\x01\n\x10GetReferenceList\x122.google.cloud.chronicle.v1.GetReferenceListRequest\x1a(.google.cloud.chronicle.v1.ReferenceList"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/{name=projects/*/locations/*/instances/*/referenceLists/*}\x12\xd2\x01\n\x12ListReferenceLists\x124.google.cloud.chronicle.v1.ListReferenceListsRequest\x1a5.google.cloud.chronicle.v1.ListReferenceListsResponse"O\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1/{parent=projects/*/locations/*/instances/*}/referenceLists\x12\xf9\x01\n\x13CreateReferenceList\x125.google.cloud.chronicle.v1.CreateReferenceListRequest\x1a(.google.cloud.chronicle.v1.ReferenceList"\x80\x01\xdaA\'parent,reference_list,reference_list_id\x82\xd3\xe4\x93\x02P">/v1/{parent=projects/*/locations/*/instances/*}/referenceLists:\x0ereference_list\x12\xfb\x01\n\x13UpdateReferenceList\x125.google.cloud.chronicle.v1.UpdateReferenceListRequest\x1a(.google.cloud.chronicle.v1.ReferenceList"\x82\x01\xdaA\x1areference_list,update_mask\x82\xd3\xe4\x93\x02_2M/v1/{reference_list.name=projects/*/locations/*/instances/*/referenceLists/*}:\x0ereference_list\x1aL\xcaA\x18chronicle.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc9\x01\n\x1dcom.google.cloud.chronicle.v1B\x12ReferenceListProtoP\x01Z;cloud.google.com/go/chronicle/apiv1/chroniclepb;chroniclepb\xaa\x02\x19Google.Cloud.Chronicle.V1\xca\x02\x19Google\\Cloud\\Chronicle\\V1\xea\x02\x1cGoogle::Cloud::Chronicle::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.chronicle.v1.reference_list_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.chronicle.v1B\x12ReferenceListProtoP\x01Z;cloud.google.com/go/chronicle/apiv1/chroniclepb;chroniclepb\xaa\x02\x19Google.Cloud.Chronicle.V1\xca\x02\x19Google\\Cloud\\Chronicle\\V1\xea\x02\x1cGoogle::Cloud::Chronicle::V1'
    _globals['_SCOPEINFO'].fields_by_name['reference_list_scope']._loaded_options = None
    _globals['_SCOPEINFO'].fields_by_name['reference_list_scope']._serialized_options = b'\xe0A\x02'
    _globals['_REFERENCELISTSCOPE'].fields_by_name['scope_names']._loaded_options = None
    _globals['_REFERENCELISTSCOPE'].fields_by_name['scope_names']._serialized_options = b'\xe0A\x01'
    _globals['_GETREFERENCELISTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREFERENCELISTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&chronicle.googleapis.com/ReferenceList'
    _globals['_LISTREFERENCELISTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREFERENCELISTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&chronicle.googleapis.com/ReferenceList'
    _globals['_CREATEREFERENCELISTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREFERENCELISTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&chronicle.googleapis.com/ReferenceList'
    _globals['_CREATEREFERENCELISTREQUEST'].fields_by_name['reference_list']._loaded_options = None
    _globals['_CREATEREFERENCELISTREQUEST'].fields_by_name['reference_list']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEREFERENCELISTREQUEST'].fields_by_name['reference_list_id']._loaded_options = None
    _globals['_CREATEREFERENCELISTREQUEST'].fields_by_name['reference_list_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEREFERENCELISTREQUEST'].fields_by_name['reference_list']._loaded_options = None
    _globals['_UPDATEREFERENCELISTREQUEST'].fields_by_name['reference_list']._serialized_options = b'\xe0A\x02'
    _globals['_REFERENCELIST'].fields_by_name['name']._loaded_options = None
    _globals['_REFERENCELIST'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_REFERENCELIST'].fields_by_name['display_name']._loaded_options = None
    _globals['_REFERENCELIST'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_REFERENCELIST'].fields_by_name['revision_create_time']._loaded_options = None
    _globals['_REFERENCELIST'].fields_by_name['revision_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_REFERENCELIST'].fields_by_name['description']._loaded_options = None
    _globals['_REFERENCELIST'].fields_by_name['description']._serialized_options = b'\xe0A\x02'
    _globals['_REFERENCELIST'].fields_by_name['entries']._loaded_options = None
    _globals['_REFERENCELIST'].fields_by_name['entries']._serialized_options = b'\xe0A\x02'
    _globals['_REFERENCELIST'].fields_by_name['rules']._loaded_options = None
    _globals['_REFERENCELIST'].fields_by_name['rules']._serialized_options = b'\xe0A\x03'
    _globals['_REFERENCELIST'].fields_by_name['syntax_type']._loaded_options = None
    _globals['_REFERENCELIST'].fields_by_name['syntax_type']._serialized_options = b'\xe0A\x02'
    _globals['_REFERENCELIST'].fields_by_name['rule_associations_count']._loaded_options = None
    _globals['_REFERENCELIST'].fields_by_name['rule_associations_count']._serialized_options = b'\xe0A\x03'
    _globals['_REFERENCELIST']._loaded_options = None
    _globals['_REFERENCELIST']._serialized_options = b'\xeaA\x86\x01\n&chronicle.googleapis.com/ReferenceList\x12\\projects/{project}/locations/{location}/instances/{instance}/referenceLists/{reference_list}'
    _globals['_REFERENCELISTENTRY'].fields_by_name['value']._loaded_options = None
    _globals['_REFERENCELISTENTRY'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_REFERENCELISTSERVICE']._loaded_options = None
    _globals['_REFERENCELISTSERVICE']._serialized_options = b'\xcaA\x18chronicle.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_REFERENCELISTSERVICE'].methods_by_name['GetReferenceList']._loaded_options = None
    _globals['_REFERENCELISTSERVICE'].methods_by_name['GetReferenceList']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/{name=projects/*/locations/*/instances/*/referenceLists/*}'
    _globals['_REFERENCELISTSERVICE'].methods_by_name['ListReferenceLists']._loaded_options = None
    _globals['_REFERENCELISTSERVICE'].methods_by_name['ListReferenceLists']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1/{parent=projects/*/locations/*/instances/*}/referenceLists'
    _globals['_REFERENCELISTSERVICE'].methods_by_name['CreateReferenceList']._loaded_options = None
    _globals['_REFERENCELISTSERVICE'].methods_by_name['CreateReferenceList']._serialized_options = b'\xdaA\'parent,reference_list,reference_list_id\x82\xd3\xe4\x93\x02P">/v1/{parent=projects/*/locations/*/instances/*}/referenceLists:\x0ereference_list'
    _globals['_REFERENCELISTSERVICE'].methods_by_name['UpdateReferenceList']._loaded_options = None
    _globals['_REFERENCELISTSERVICE'].methods_by_name['UpdateReferenceList']._serialized_options = b'\xdaA\x1areference_list,update_mask\x82\xd3\xe4\x93\x02_2M/v1/{reference_list.name=projects/*/locations/*/instances/*/referenceLists/*}:\x0ereference_list'
    _globals['_REFERENCELISTSYNTAXTYPE']._serialized_start = 1816
    _globals['_REFERENCELISTSYNTAXTYPE']._serialized_end = 2010
    _globals['_REFERENCELISTVIEW']._serialized_start = 2012
    _globals['_REFERENCELISTVIEW']._serialized_end = 2129
    _globals['_SCOPEINFO']._serialized_start = 259
    _globals['_SCOPEINFO']._serialized_end = 352
    _globals['_REFERENCELISTSCOPE']._serialized_start = 354
    _globals['_REFERENCELISTSCOPE']._serialized_end = 400
    _globals['_GETREFERENCELISTREQUEST']._serialized_start = 403
    _globals['_GETREFERENCELISTREQUEST']._serialized_end = 550
    _globals['_LISTREFERENCELISTSREQUEST']._serialized_start = 553
    _globals['_LISTREFERENCELISTSREQUEST']._serialized_end = 743
    _globals['_LISTREFERENCELISTSRESPONSE']._serialized_start = 745
    _globals['_LISTREFERENCELISTSRESPONSE']._serialized_end = 865
    _globals['_CREATEREFERENCELISTREQUEST']._serialized_start = 868
    _globals['_CREATEREFERENCELISTREQUEST']._serialized_end = 1063
    _globals['_UPDATEREFERENCELISTREQUEST']._serialized_start = 1066
    _globals['_UPDATEREFERENCELISTREQUEST']._serialized_end = 1214
    _globals['_REFERENCELIST']._serialized_start = 1217
    _globals['_REFERENCELIST']._serialized_end = 1771
    _globals['_REFERENCELISTENTRY']._serialized_start = 1773
    _globals['_REFERENCELISTENTRY']._serialized_end = 1813
    _globals['_REFERENCELISTSERVICE']._serialized_start = 2132
    _globals['_REFERENCELISTSERVICE']._serialized_end = 3145