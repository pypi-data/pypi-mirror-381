"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/chronicle/v1/data_access_control.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/chronicle/v1/data_access_control.proto\x12\x19google.cloud.chronicle.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcf\x01\n\x1cCreateDataAccessLabelRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(chronicle.googleapis.com/DataAccessLabel\x12J\n\x11data_access_label\x18\x02 \x01(\x0b2*.google.cloud.chronicle.v1.DataAccessLabelB\x03\xe0A\x02\x12!\n\x14data_access_label_id\x18\x03 \x01(\tB\x03\xe0A\x02"[\n\x19GetDataAccessLabelRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(chronicle.googleapis.com/DataAccessLabel"\x9b\x01\n\x1bListDataAccessLabelsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(chronicle.googleapis.com/DataAccessLabel\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\x7f\n\x1cListDataAccessLabelsResponse\x12F\n\x12data_access_labels\x18\x01 \x03(\x0b2*.google.cloud.chronicle.v1.DataAccessLabel\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9b\x01\n\x1cUpdateDataAccessLabelRequest\x12J\n\x11data_access_label\x18\x01 \x01(\x0b2*.google.cloud.chronicle.v1.DataAccessLabelB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"^\n\x1cDeleteDataAccessLabelRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(chronicle.googleapis.com/DataAccessLabel"\xcf\x01\n\x1cCreateDataAccessScopeRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(chronicle.googleapis.com/DataAccessScope\x12J\n\x11data_access_scope\x18\x02 \x01(\x0b2*.google.cloud.chronicle.v1.DataAccessScopeB\x03\xe0A\x02\x12!\n\x14data_access_scope_id\x18\x03 \x01(\tB\x03\xe0A\x02"[\n\x19GetDataAccessScopeRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(chronicle.googleapis.com/DataAccessScope"\x9b\x01\n\x1bListDataAccessScopesRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(chronicle.googleapis.com/DataAccessScope\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\xd3\x01\n\x1cListDataAccessScopesResponse\x12F\n\x12data_access_scopes\x18\x01 \x03(\x0b2*.google.cloud.chronicle.v1.DataAccessScope\x12-\n global_data_access_scope_granted\x18\x03 \x01(\x08H\x00\x88\x01\x01\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\tB#\n!_global_data_access_scope_granted"\x9b\x01\n\x1cUpdateDataAccessScopeRequest\x12J\n\x11data_access_scope\x18\x01 \x01(\x0b2*.google.cloud.chronicle.v1.DataAccessScopeB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"^\n\x1cDeleteDataAccessScopeRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(chronicle.googleapis.com/DataAccessScope"\xd5\x03\n\x0fDataAccessLabel\x12\x13\n\tudm_query\x18\x03 \x01(\tH\x00\x12;\n\x04name\x18\x01 \x01(\tB-\xfaA*\n(chronicle.googleapis.com/DataAccessLabel\x12\x19\n\x0cdisplay_name\x18\x08 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06author\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0blast_editor\x18\x07 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01:\x91\x01\xeaA\x8d\x01\n(chronicle.googleapis.com/DataAccessLabel\x12aprojects/{project}/locations/{location}/instances/{instance}/dataAccessLabels/{data_access_label}B\x0c\n\ndefinition"\x88\x05\n\x0fDataAccessScope\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(chronicle.googleapis.com/DataAccessScope\x12\\\n\x1aallowed_data_access_labels\x18\x02 \x03(\x0b23.google.cloud.chronicle.v1.DataAccessLabelReferenceB\x03\xe0A\x01\x12[\n\x19denied_data_access_labels\x18\x03 \x03(\x0b23.google.cloud.chronicle.v1.DataAccessLabelReferenceB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x04 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06author\x18\x07 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0blast_editor\x18\x08 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\t \x01(\tB\x03\xe0A\x01\x12\x16\n\tallow_all\x18\n \x01(\x08B\x03\xe0A\x01:\x91\x01\xeaA\x8d\x01\n(chronicle.googleapis.com/DataAccessScope\x12aprojects/{project}/locations/{location}/instances/{instance}/dataAccessScopes/{data_access_scope}"\xd0\x01\n\x18DataAccessLabelReference\x12\x1b\n\x11data_access_label\x18\x01 \x01(\tH\x00\x12\x12\n\x08log_type\x18\x02 \x01(\tH\x00\x12\x19\n\x0fasset_namespace\x18\x03 \x01(\tH\x00\x12D\n\x0fingestion_label\x18\x04 \x01(\x0b2).google.cloud.chronicle.v1.IngestionLabelH\x00\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x03B\x07\n\x05label"V\n\x0eIngestionLabel\x12 \n\x13ingestion_label_key\x18\x01 \x01(\tB\x03\xe0A\x02\x12"\n\x15ingestion_label_value\x18\x02 \x01(\tB\x03\xe0A\x012\xe6\x12\n\x18DataAccessControlService\x12\x8a\x02\n\x15CreateDataAccessLabel\x127.google.cloud.chronicle.v1.CreateDataAccessLabelRequest\x1a*.google.cloud.chronicle.v1.DataAccessLabel"\x8b\x01\xdaA-parent,data_access_label,data_access_label_id\x82\xd3\xe4\x93\x02U"@/v1/{parent=projects/*/locations/*/instances/*}/dataAccessLabels:\x11data_access_label\x12\xc7\x01\n\x12GetDataAccessLabel\x124.google.cloud.chronicle.v1.GetDataAccessLabelRequest\x1a*.google.cloud.chronicle.v1.DataAccessLabel"O\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1/{name=projects/*/locations/*/instances/*/dataAccessLabels/*}\x12\xda\x01\n\x14ListDataAccessLabels\x126.google.cloud.chronicle.v1.ListDataAccessLabelsRequest\x1a7.google.cloud.chronicle.v1.ListDataAccessLabelsResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1/{parent=projects/*/locations/*/instances/*}/dataAccessLabels\x12\x8c\x02\n\x15UpdateDataAccessLabel\x127.google.cloud.chronicle.v1.UpdateDataAccessLabelRequest\x1a*.google.cloud.chronicle.v1.DataAccessLabel"\x8d\x01\xdaA\x1ddata_access_label,update_mask\x82\xd3\xe4\x93\x02g2R/v1/{data_access_label.name=projects/*/locations/*/instances/*/dataAccessLabels/*}:\x11data_access_label\x12\xb9\x01\n\x15DeleteDataAccessLabel\x127.google.cloud.chronicle.v1.DeleteDataAccessLabelRequest\x1a\x16.google.protobuf.Empty"O\xdaA\x04name\x82\xd3\xe4\x93\x02B*@/v1/{name=projects/*/locations/*/instances/*/dataAccessLabels/*}\x12\x8a\x02\n\x15CreateDataAccessScope\x127.google.cloud.chronicle.v1.CreateDataAccessScopeRequest\x1a*.google.cloud.chronicle.v1.DataAccessScope"\x8b\x01\xdaA-parent,data_access_scope,data_access_scope_id\x82\xd3\xe4\x93\x02U"@/v1/{parent=projects/*/locations/*/instances/*}/dataAccessScopes:\x11data_access_scope\x12\xc7\x01\n\x12GetDataAccessScope\x124.google.cloud.chronicle.v1.GetDataAccessScopeRequest\x1a*.google.cloud.chronicle.v1.DataAccessScope"O\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1/{name=projects/*/locations/*/instances/*/dataAccessScopes/*}\x12\xda\x01\n\x14ListDataAccessScopes\x126.google.cloud.chronicle.v1.ListDataAccessScopesRequest\x1a7.google.cloud.chronicle.v1.ListDataAccessScopesResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1/{parent=projects/*/locations/*/instances/*}/dataAccessScopes\x12\x8c\x02\n\x15UpdateDataAccessScope\x127.google.cloud.chronicle.v1.UpdateDataAccessScopeRequest\x1a*.google.cloud.chronicle.v1.DataAccessScope"\x8d\x01\xdaA\x1ddata_access_scope,update_mask\x82\xd3\xe4\x93\x02g2R/v1/{data_access_scope.name=projects/*/locations/*/instances/*/dataAccessScopes/*}:\x11data_access_scope\x12\xb9\x01\n\x15DeleteDataAccessScope\x127.google.cloud.chronicle.v1.DeleteDataAccessScopeRequest\x1a\x16.google.protobuf.Empty"O\xdaA\x04name\x82\xd3\xe4\x93\x02B*@/v1/{name=projects/*/locations/*/instances/*/dataAccessScopes/*}\x1aL\xcaA\x18chronicle.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc6\x01\n\x1dcom.google.cloud.chronicle.v1B\x0fDataAccessProtoP\x01Z;cloud.google.com/go/chronicle/apiv1/chroniclepb;chroniclepb\xaa\x02\x19Google.Cloud.Chronicle.V1\xca\x02\x19Google\\Cloud\\Chronicle\\V1\xea\x02\x1cGoogle::Cloud::Chronicle::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.chronicle.v1.data_access_control_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.chronicle.v1B\x0fDataAccessProtoP\x01Z;cloud.google.com/go/chronicle/apiv1/chroniclepb;chroniclepb\xaa\x02\x19Google.Cloud.Chronicle.V1\xca\x02\x19Google\\Cloud\\Chronicle\\V1\xea\x02\x1cGoogle::Cloud::Chronicle::V1'
    _globals['_CREATEDATAACCESSLABELREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATAACCESSLABELREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(chronicle.googleapis.com/DataAccessLabel'
    _globals['_CREATEDATAACCESSLABELREQUEST'].fields_by_name['data_access_label']._loaded_options = None
    _globals['_CREATEDATAACCESSLABELREQUEST'].fields_by_name['data_access_label']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATAACCESSLABELREQUEST'].fields_by_name['data_access_label_id']._loaded_options = None
    _globals['_CREATEDATAACCESSLABELREQUEST'].fields_by_name['data_access_label_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATAACCESSLABELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATAACCESSLABELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(chronicle.googleapis.com/DataAccessLabel'
    _globals['_LISTDATAACCESSLABELSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATAACCESSLABELSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(chronicle.googleapis.com/DataAccessLabel'
    _globals['_LISTDATAACCESSLABELSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTDATAACCESSLABELSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEDATAACCESSLABELREQUEST'].fields_by_name['data_access_label']._loaded_options = None
    _globals['_UPDATEDATAACCESSLABELREQUEST'].fields_by_name['data_access_label']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDATAACCESSLABELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATAACCESSLABELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(chronicle.googleapis.com/DataAccessLabel'
    _globals['_CREATEDATAACCESSSCOPEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATAACCESSSCOPEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(chronicle.googleapis.com/DataAccessScope'
    _globals['_CREATEDATAACCESSSCOPEREQUEST'].fields_by_name['data_access_scope']._loaded_options = None
    _globals['_CREATEDATAACCESSSCOPEREQUEST'].fields_by_name['data_access_scope']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATAACCESSSCOPEREQUEST'].fields_by_name['data_access_scope_id']._loaded_options = None
    _globals['_CREATEDATAACCESSSCOPEREQUEST'].fields_by_name['data_access_scope_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATAACCESSSCOPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATAACCESSSCOPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(chronicle.googleapis.com/DataAccessScope'
    _globals['_LISTDATAACCESSSCOPESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATAACCESSSCOPESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(chronicle.googleapis.com/DataAccessScope'
    _globals['_LISTDATAACCESSSCOPESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTDATAACCESSSCOPESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEDATAACCESSSCOPEREQUEST'].fields_by_name['data_access_scope']._loaded_options = None
    _globals['_UPDATEDATAACCESSSCOPEREQUEST'].fields_by_name['data_access_scope']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDATAACCESSSCOPEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATAACCESSSCOPEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(chronicle.googleapis.com/DataAccessScope'
    _globals['_DATAACCESSLABEL'].fields_by_name['name']._loaded_options = None
    _globals['_DATAACCESSLABEL'].fields_by_name['name']._serialized_options = b'\xfaA*\n(chronicle.googleapis.com/DataAccessLabel'
    _globals['_DATAACCESSLABEL'].fields_by_name['display_name']._loaded_options = None
    _globals['_DATAACCESSLABEL'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_DATAACCESSLABEL'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATAACCESSLABEL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATAACCESSLABEL'].fields_by_name['update_time']._loaded_options = None
    _globals['_DATAACCESSLABEL'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATAACCESSLABEL'].fields_by_name['author']._loaded_options = None
    _globals['_DATAACCESSLABEL'].fields_by_name['author']._serialized_options = b'\xe0A\x03'
    _globals['_DATAACCESSLABEL'].fields_by_name['last_editor']._loaded_options = None
    _globals['_DATAACCESSLABEL'].fields_by_name['last_editor']._serialized_options = b'\xe0A\x03'
    _globals['_DATAACCESSLABEL'].fields_by_name['description']._loaded_options = None
    _globals['_DATAACCESSLABEL'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_DATAACCESSLABEL']._loaded_options = None
    _globals['_DATAACCESSLABEL']._serialized_options = b'\xeaA\x8d\x01\n(chronicle.googleapis.com/DataAccessLabel\x12aprojects/{project}/locations/{location}/instances/{instance}/dataAccessLabels/{data_access_label}'
    _globals['_DATAACCESSSCOPE'].fields_by_name['name']._loaded_options = None
    _globals['_DATAACCESSSCOPE'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(chronicle.googleapis.com/DataAccessScope'
    _globals['_DATAACCESSSCOPE'].fields_by_name['allowed_data_access_labels']._loaded_options = None
    _globals['_DATAACCESSSCOPE'].fields_by_name['allowed_data_access_labels']._serialized_options = b'\xe0A\x01'
    _globals['_DATAACCESSSCOPE'].fields_by_name['denied_data_access_labels']._loaded_options = None
    _globals['_DATAACCESSSCOPE'].fields_by_name['denied_data_access_labels']._serialized_options = b'\xe0A\x01'
    _globals['_DATAACCESSSCOPE'].fields_by_name['display_name']._loaded_options = None
    _globals['_DATAACCESSSCOPE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_DATAACCESSSCOPE'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATAACCESSSCOPE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATAACCESSSCOPE'].fields_by_name['update_time']._loaded_options = None
    _globals['_DATAACCESSSCOPE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATAACCESSSCOPE'].fields_by_name['author']._loaded_options = None
    _globals['_DATAACCESSSCOPE'].fields_by_name['author']._serialized_options = b'\xe0A\x03'
    _globals['_DATAACCESSSCOPE'].fields_by_name['last_editor']._loaded_options = None
    _globals['_DATAACCESSSCOPE'].fields_by_name['last_editor']._serialized_options = b'\xe0A\x03'
    _globals['_DATAACCESSSCOPE'].fields_by_name['description']._loaded_options = None
    _globals['_DATAACCESSSCOPE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_DATAACCESSSCOPE'].fields_by_name['allow_all']._loaded_options = None
    _globals['_DATAACCESSSCOPE'].fields_by_name['allow_all']._serialized_options = b'\xe0A\x01'
    _globals['_DATAACCESSSCOPE']._loaded_options = None
    _globals['_DATAACCESSSCOPE']._serialized_options = b'\xeaA\x8d\x01\n(chronicle.googleapis.com/DataAccessScope\x12aprojects/{project}/locations/{location}/instances/{instance}/dataAccessScopes/{data_access_scope}'
    _globals['_DATAACCESSLABELREFERENCE'].fields_by_name['display_name']._loaded_options = None
    _globals['_DATAACCESSLABELREFERENCE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_INGESTIONLABEL'].fields_by_name['ingestion_label_key']._loaded_options = None
    _globals['_INGESTIONLABEL'].fields_by_name['ingestion_label_key']._serialized_options = b'\xe0A\x02'
    _globals['_INGESTIONLABEL'].fields_by_name['ingestion_label_value']._loaded_options = None
    _globals['_INGESTIONLABEL'].fields_by_name['ingestion_label_value']._serialized_options = b'\xe0A\x01'
    _globals['_DATAACCESSCONTROLSERVICE']._loaded_options = None
    _globals['_DATAACCESSCONTROLSERVICE']._serialized_options = b'\xcaA\x18chronicle.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['CreateDataAccessLabel']._loaded_options = None
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['CreateDataAccessLabel']._serialized_options = b'\xdaA-parent,data_access_label,data_access_label_id\x82\xd3\xe4\x93\x02U"@/v1/{parent=projects/*/locations/*/instances/*}/dataAccessLabels:\x11data_access_label'
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['GetDataAccessLabel']._loaded_options = None
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['GetDataAccessLabel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1/{name=projects/*/locations/*/instances/*/dataAccessLabels/*}'
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['ListDataAccessLabels']._loaded_options = None
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['ListDataAccessLabels']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1/{parent=projects/*/locations/*/instances/*}/dataAccessLabels'
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['UpdateDataAccessLabel']._loaded_options = None
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['UpdateDataAccessLabel']._serialized_options = b'\xdaA\x1ddata_access_label,update_mask\x82\xd3\xe4\x93\x02g2R/v1/{data_access_label.name=projects/*/locations/*/instances/*/dataAccessLabels/*}:\x11data_access_label'
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['DeleteDataAccessLabel']._loaded_options = None
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['DeleteDataAccessLabel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B*@/v1/{name=projects/*/locations/*/instances/*/dataAccessLabels/*}'
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['CreateDataAccessScope']._loaded_options = None
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['CreateDataAccessScope']._serialized_options = b'\xdaA-parent,data_access_scope,data_access_scope_id\x82\xd3\xe4\x93\x02U"@/v1/{parent=projects/*/locations/*/instances/*}/dataAccessScopes:\x11data_access_scope'
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['GetDataAccessScope']._loaded_options = None
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['GetDataAccessScope']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1/{name=projects/*/locations/*/instances/*/dataAccessScopes/*}'
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['ListDataAccessScopes']._loaded_options = None
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['ListDataAccessScopes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1/{parent=projects/*/locations/*/instances/*}/dataAccessScopes'
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['UpdateDataAccessScope']._loaded_options = None
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['UpdateDataAccessScope']._serialized_options = b'\xdaA\x1ddata_access_scope,update_mask\x82\xd3\xe4\x93\x02g2R/v1/{data_access_scope.name=projects/*/locations/*/instances/*/dataAccessScopes/*}:\x11data_access_scope'
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['DeleteDataAccessScope']._loaded_options = None
    _globals['_DATAACCESSCONTROLSERVICE'].methods_by_name['DeleteDataAccessScope']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B*@/v1/{name=projects/*/locations/*/instances/*/dataAccessScopes/*}'
    _globals['_CREATEDATAACCESSLABELREQUEST']._serialized_start = 294
    _globals['_CREATEDATAACCESSLABELREQUEST']._serialized_end = 501
    _globals['_GETDATAACCESSLABELREQUEST']._serialized_start = 503
    _globals['_GETDATAACCESSLABELREQUEST']._serialized_end = 594
    _globals['_LISTDATAACCESSLABELSREQUEST']._serialized_start = 597
    _globals['_LISTDATAACCESSLABELSREQUEST']._serialized_end = 752
    _globals['_LISTDATAACCESSLABELSRESPONSE']._serialized_start = 754
    _globals['_LISTDATAACCESSLABELSRESPONSE']._serialized_end = 881
    _globals['_UPDATEDATAACCESSLABELREQUEST']._serialized_start = 884
    _globals['_UPDATEDATAACCESSLABELREQUEST']._serialized_end = 1039
    _globals['_DELETEDATAACCESSLABELREQUEST']._serialized_start = 1041
    _globals['_DELETEDATAACCESSLABELREQUEST']._serialized_end = 1135
    _globals['_CREATEDATAACCESSSCOPEREQUEST']._serialized_start = 1138
    _globals['_CREATEDATAACCESSSCOPEREQUEST']._serialized_end = 1345
    _globals['_GETDATAACCESSSCOPEREQUEST']._serialized_start = 1347
    _globals['_GETDATAACCESSSCOPEREQUEST']._serialized_end = 1438
    _globals['_LISTDATAACCESSSCOPESREQUEST']._serialized_start = 1441
    _globals['_LISTDATAACCESSSCOPESREQUEST']._serialized_end = 1596
    _globals['_LISTDATAACCESSSCOPESRESPONSE']._serialized_start = 1599
    _globals['_LISTDATAACCESSSCOPESRESPONSE']._serialized_end = 1810
    _globals['_UPDATEDATAACCESSSCOPEREQUEST']._serialized_start = 1813
    _globals['_UPDATEDATAACCESSSCOPEREQUEST']._serialized_end = 1968
    _globals['_DELETEDATAACCESSSCOPEREQUEST']._serialized_start = 1970
    _globals['_DELETEDATAACCESSSCOPEREQUEST']._serialized_end = 2064
    _globals['_DATAACCESSLABEL']._serialized_start = 2067
    _globals['_DATAACCESSLABEL']._serialized_end = 2536
    _globals['_DATAACCESSSCOPE']._serialized_start = 2539
    _globals['_DATAACCESSSCOPE']._serialized_end = 3187
    _globals['_DATAACCESSLABELREFERENCE']._serialized_start = 3190
    _globals['_DATAACCESSLABELREFERENCE']._serialized_end = 3398
    _globals['_INGESTIONLABEL']._serialized_start = 3400
    _globals['_INGESTIONLABEL']._serialized_end = 3486
    _globals['_DATAACCESSCONTROLSERVICE']._serialized_start = 3489
    _globals['_DATAACCESSCONTROLSERVICE']._serialized_end = 5895