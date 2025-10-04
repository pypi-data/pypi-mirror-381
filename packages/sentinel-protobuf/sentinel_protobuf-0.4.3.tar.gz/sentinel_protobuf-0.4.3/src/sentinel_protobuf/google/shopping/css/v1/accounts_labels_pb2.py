"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/css/v1/accounts_labels.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/shopping/css/v1/accounts_labels.proto\x12\x16google.shopping.css.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto"\x95\x03\n\x0cAccountLabel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\x08label_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x17\n\naccount_id\x18\x03 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0bdescription\x18\x05 \x01(\tH\x01\x88\x01\x01\x12G\n\nlabel_type\x18\x06 \x01(\x0e2..google.shopping.css.v1.AccountLabel.LabelTypeB\x03\xe0A\x03"B\n\tLabelType\x12\x1a\n\x16LABEL_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06MANUAL\x10\x01\x12\r\n\tAUTOMATIC\x10\x02:d\xeaAa\n\x1fcss.googleapis.com/AccountLabel\x12!accounts/{account}/labels/{label}*\raccountLabels2\x0caccountLabelB\x0f\n\r_display_nameB\x0e\n\x0c_description"z\n\x18ListAccountLabelsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fcss.googleapis.com/AccountLabel\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"r\n\x19ListAccountLabelsResponse\x12<\n\x0eaccount_labels\x18\x01 \x03(\x0b2$.google.shopping.css.v1.AccountLabel\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x96\x01\n\x19CreateAccountLabelRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fcss.googleapis.com/AccountLabel\x12@\n\raccount_label\x18\x02 \x01(\x0b2$.google.shopping.css.v1.AccountLabelB\x03\xe0A\x02"]\n\x19UpdateAccountLabelRequest\x12@\n\raccount_label\x18\x01 \x01(\x0b2$.google.shopping.css.v1.AccountLabelB\x03\xe0A\x02"R\n\x19DeleteAccountLabelRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fcss.googleapis.com/AccountLabel2\x97\x06\n\x14AccountLabelsService\x12\xa9\x01\n\x11ListAccountLabels\x120.google.shopping.css.v1.ListAccountLabelsRequest\x1a1.google.shopping.css.v1.ListAccountLabelsResponse"/\xdaA\x06parent\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{parent=accounts/*}/labels\x12\xbb\x01\n\x12CreateAccountLabel\x121.google.shopping.css.v1.CreateAccountLabelRequest\x1a$.google.shopping.css.v1.AccountLabel"L\xdaA\x14parent,account_label\x82\xd3\xe4\x93\x02/"\x1e/v1/{parent=accounts/*}/labels:\raccount_label\x12\xc2\x01\n\x12UpdateAccountLabel\x121.google.shopping.css.v1.UpdateAccountLabelRequest\x1a$.google.shopping.css.v1.AccountLabel"S\xdaA\raccount_label\x82\xd3\xe4\x93\x02=2,/v1/{account_label.name=accounts/*/labels/*}:\raccount_label\x12\x8e\x01\n\x12DeleteAccountLabel\x121.google.shopping.css.v1.DeleteAccountLabelRequest\x1a\x16.google.protobuf.Empty"-\xdaA\x04name\x82\xd3\xe4\x93\x02 *\x1e/v1/{name=accounts/*/labels/*}\x1a?\xcaA\x12css.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xb5\x01\n\x1acom.google.shopping.css.v1B\x13AccountsLabelsProtoP\x01Z2cloud.google.com/go/shopping/css/apiv1/csspb;csspb\xaa\x02\x16Google.Shopping.Css.V1\xca\x02\x16Google\\Shopping\\Css\\V1\xea\x02\x19Google::Shopping::Css::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.css.v1.accounts_labels_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.shopping.css.v1B\x13AccountsLabelsProtoP\x01Z2cloud.google.com/go/shopping/css/apiv1/csspb;csspb\xaa\x02\x16Google.Shopping.Css.V1\xca\x02\x16Google\\Shopping\\Css\\V1\xea\x02\x19Google::Shopping::Css::V1'
    _globals['_ACCOUNTLABEL'].fields_by_name['label_id']._loaded_options = None
    _globals['_ACCOUNTLABEL'].fields_by_name['label_id']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTLABEL'].fields_by_name['account_id']._loaded_options = None
    _globals['_ACCOUNTLABEL'].fields_by_name['account_id']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTLABEL'].fields_by_name['label_type']._loaded_options = None
    _globals['_ACCOUNTLABEL'].fields_by_name['label_type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTLABEL']._loaded_options = None
    _globals['_ACCOUNTLABEL']._serialized_options = b'\xeaAa\n\x1fcss.googleapis.com/AccountLabel\x12!accounts/{account}/labels/{label}*\raccountLabels2\x0caccountLabel'
    _globals['_LISTACCOUNTLABELSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACCOUNTLABELSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fcss.googleapis.com/AccountLabel'
    _globals['_CREATEACCOUNTLABELREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEACCOUNTLABELREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fcss.googleapis.com/AccountLabel'
    _globals['_CREATEACCOUNTLABELREQUEST'].fields_by_name['account_label']._loaded_options = None
    _globals['_CREATEACCOUNTLABELREQUEST'].fields_by_name['account_label']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEACCOUNTLABELREQUEST'].fields_by_name['account_label']._loaded_options = None
    _globals['_UPDATEACCOUNTLABELREQUEST'].fields_by_name['account_label']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEACCOUNTLABELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEACCOUNTLABELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fcss.googleapis.com/AccountLabel'
    _globals['_ACCOUNTLABELSSERVICE']._loaded_options = None
    _globals['_ACCOUNTLABELSSERVICE']._serialized_options = b"\xcaA\x12css.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_ACCOUNTLABELSSERVICE'].methods_by_name['ListAccountLabels']._loaded_options = None
    _globals['_ACCOUNTLABELSSERVICE'].methods_by_name['ListAccountLabels']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{parent=accounts/*}/labels'
    _globals['_ACCOUNTLABELSSERVICE'].methods_by_name['CreateAccountLabel']._loaded_options = None
    _globals['_ACCOUNTLABELSSERVICE'].methods_by_name['CreateAccountLabel']._serialized_options = b'\xdaA\x14parent,account_label\x82\xd3\xe4\x93\x02/"\x1e/v1/{parent=accounts/*}/labels:\raccount_label'
    _globals['_ACCOUNTLABELSSERVICE'].methods_by_name['UpdateAccountLabel']._loaded_options = None
    _globals['_ACCOUNTLABELSSERVICE'].methods_by_name['UpdateAccountLabel']._serialized_options = b'\xdaA\raccount_label\x82\xd3\xe4\x93\x02=2,/v1/{account_label.name=accounts/*/labels/*}:\raccount_label'
    _globals['_ACCOUNTLABELSSERVICE'].methods_by_name['DeleteAccountLabel']._loaded_options = None
    _globals['_ACCOUNTLABELSSERVICE'].methods_by_name['DeleteAccountLabel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02 *\x1e/v1/{name=accounts/*/labels/*}'
    _globals['_ACCOUNTLABEL']._serialized_start = 217
    _globals['_ACCOUNTLABEL']._serialized_end = 622
    _globals['_ACCOUNTLABEL_LABELTYPE']._serialized_start = 421
    _globals['_ACCOUNTLABEL_LABELTYPE']._serialized_end = 487
    _globals['_LISTACCOUNTLABELSREQUEST']._serialized_start = 624
    _globals['_LISTACCOUNTLABELSREQUEST']._serialized_end = 746
    _globals['_LISTACCOUNTLABELSRESPONSE']._serialized_start = 748
    _globals['_LISTACCOUNTLABELSRESPONSE']._serialized_end = 862
    _globals['_CREATEACCOUNTLABELREQUEST']._serialized_start = 865
    _globals['_CREATEACCOUNTLABELREQUEST']._serialized_end = 1015
    _globals['_UPDATEACCOUNTLABELREQUEST']._serialized_start = 1017
    _globals['_UPDATEACCOUNTLABELREQUEST']._serialized_end = 1110
    _globals['_DELETEACCOUNTLABELREQUEST']._serialized_start = 1112
    _globals['_DELETEACCOUNTLABELREQUEST']._serialized_end = 1194
    _globals['_ACCOUNTLABELSSERVICE']._serialized_start = 1197
    _globals['_ACCOUNTLABELSSERVICE']._serialized_end = 1988