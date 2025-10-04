"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dialogflow/v2beta1/phone_number.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/dialogflow/v2beta1/phone_number.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xb1\x03\n\x0bPhoneNumber\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cphone_number\x18\x02 \x01(\tB\x03\xe0A\x03\x12!\n\x14conversation_profile\x18\x03 \x01(\tB\x03\xe0A\x01\x12Y\n\x0flifecycle_state\x18\x04 \x01(\x0e2;.google.cloud.dialogflow.v2beta1.PhoneNumber.LifecycleStateB\x03\xe0A\x03"S\n\x0eLifecycleState\x12\x1f\n\x1bLIFECYCLE_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x14\n\x10DELETE_REQUESTED\x10\x02:\xa0\x01\xeaA\x9c\x01\n%dialogflow.googleapis.com/PhoneNumber\x12.projects/{project}/phoneNumbers/{phone_number}\x12Cprojects/{project}/locations/{location}/phoneNumbers/{phone_number}"W\n\x18DeletePhoneNumberRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/PhoneNumber"Y\n\x1aUndeletePhoneNumberRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/PhoneNumber"\xa4\x01\n\x17ListPhoneNumbersRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%dialogflow.googleapis.com/PhoneNumber\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cshow_deleted\x18\x04 \x01(\x08B\x03\xe0A\x01"x\n\x18ListPhoneNumbersResponse\x12C\n\rphone_numbers\x18\x01 \x03(\x0b2,.google.cloud.dialogflow.v2beta1.PhoneNumber\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x99\x01\n\x18UpdatePhoneNumberRequest\x12G\n\x0cphone_number\x18\x01 \x01(\x0b2,.google.cloud.dialogflow.v2beta1.PhoneNumberB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x012\xc6\t\n\x0cPhoneNumbers\x12\xfc\x01\n\x10ListPhoneNumbers\x128.google.cloud.dialogflow.v2beta1.ListPhoneNumbersRequest\x1a9.google.cloud.dialogflow.v2beta1.ListPhoneNumbersResponse"s\xdaA\x06parent\x82\xd3\xe4\x93\x02d\x12)/v2beta1/{parent=projects/*}/phoneNumbersZ7\x125/v2beta1/{parent=projects/*/locations/*}/phoneNumbers\x12\xbb\x02\n\x11UpdatePhoneNumber\x129.google.cloud.dialogflow.v2beta1.UpdatePhoneNumberRequest\x1a,.google.cloud.dialogflow.v2beta1.PhoneNumber"\xbc\x01\xdaA\x18phone_number,update_mask\x82\xd3\xe4\x93\x02\x9a\x0126/v2beta1/{phone_number.name=projects/*/phoneNumbers/*}:\x0cphone_numberZR2B/v2beta1/{phone_number.name=projects/*/locations/*/phoneNumbers/*}:\x0cphone_number\x12\xef\x01\n\x11DeletePhoneNumber\x129.google.cloud.dialogflow.v2beta1.DeletePhoneNumberRequest\x1a,.google.cloud.dialogflow.v2beta1.PhoneNumber"q\xdaA\x04name\x82\xd3\xe4\x93\x02d*)/v2beta1/{name=projects/*/phoneNumbers/*}Z7*5/v2beta1/{name=projects/*/locations/*/phoneNumbers/*}\x12\x8c\x02\n\x13UndeletePhoneNumber\x12;.google.cloud.dialogflow.v2beta1.UndeletePhoneNumberRequest\x1a,.google.cloud.dialogflow.v2beta1.PhoneNumber"\x89\x01\xdaA\x04name\x82\xd3\xe4\x93\x02|"2/v2beta1/{name=projects/*/phoneNumbers/*}:undelete:\x01*ZC">/v2beta1/{name=projects/*/locations/*/phoneNumbers/*}:undelete:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa5\x01\n#com.google.cloud.dialogflow.v2beta1B\x10PhoneNumberProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.phone_number_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\x10PhoneNumberProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_PHONENUMBER'].fields_by_name['name']._loaded_options = None
    _globals['_PHONENUMBER'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_PHONENUMBER'].fields_by_name['phone_number']._loaded_options = None
    _globals['_PHONENUMBER'].fields_by_name['phone_number']._serialized_options = b'\xe0A\x03'
    _globals['_PHONENUMBER'].fields_by_name['conversation_profile']._loaded_options = None
    _globals['_PHONENUMBER'].fields_by_name['conversation_profile']._serialized_options = b'\xe0A\x01'
    _globals['_PHONENUMBER'].fields_by_name['lifecycle_state']._loaded_options = None
    _globals['_PHONENUMBER'].fields_by_name['lifecycle_state']._serialized_options = b'\xe0A\x03'
    _globals['_PHONENUMBER']._loaded_options = None
    _globals['_PHONENUMBER']._serialized_options = b'\xeaA\x9c\x01\n%dialogflow.googleapis.com/PhoneNumber\x12.projects/{project}/phoneNumbers/{phone_number}\x12Cprojects/{project}/locations/{location}/phoneNumbers/{phone_number}'
    _globals['_DELETEPHONENUMBERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPHONENUMBERREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/PhoneNumber"
    _globals['_UNDELETEPHONENUMBERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNDELETEPHONENUMBERREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/PhoneNumber"
    _globals['_LISTPHONENUMBERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPHONENUMBERSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%dialogflow.googleapis.com/PhoneNumber"
    _globals['_LISTPHONENUMBERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPHONENUMBERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPHONENUMBERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPHONENUMBERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPHONENUMBERSREQUEST'].fields_by_name['show_deleted']._loaded_options = None
    _globals['_LISTPHONENUMBERSREQUEST'].fields_by_name['show_deleted']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEPHONENUMBERREQUEST'].fields_by_name['phone_number']._loaded_options = None
    _globals['_UPDATEPHONENUMBERREQUEST'].fields_by_name['phone_number']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPHONENUMBERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPHONENUMBERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_PHONENUMBERS']._loaded_options = None
    _globals['_PHONENUMBERS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_PHONENUMBERS'].methods_by_name['ListPhoneNumbers']._loaded_options = None
    _globals['_PHONENUMBERS'].methods_by_name['ListPhoneNumbers']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02d\x12)/v2beta1/{parent=projects/*}/phoneNumbersZ7\x125/v2beta1/{parent=projects/*/locations/*}/phoneNumbers'
    _globals['_PHONENUMBERS'].methods_by_name['UpdatePhoneNumber']._loaded_options = None
    _globals['_PHONENUMBERS'].methods_by_name['UpdatePhoneNumber']._serialized_options = b'\xdaA\x18phone_number,update_mask\x82\xd3\xe4\x93\x02\x9a\x0126/v2beta1/{phone_number.name=projects/*/phoneNumbers/*}:\x0cphone_numberZR2B/v2beta1/{phone_number.name=projects/*/locations/*/phoneNumbers/*}:\x0cphone_number'
    _globals['_PHONENUMBERS'].methods_by_name['DeletePhoneNumber']._loaded_options = None
    _globals['_PHONENUMBERS'].methods_by_name['DeletePhoneNumber']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02d*)/v2beta1/{name=projects/*/phoneNumbers/*}Z7*5/v2beta1/{name=projects/*/locations/*/phoneNumbers/*}'
    _globals['_PHONENUMBERS'].methods_by_name['UndeletePhoneNumber']._loaded_options = None
    _globals['_PHONENUMBERS'].methods_by_name['UndeletePhoneNumber']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02|"2/v2beta1/{name=projects/*/phoneNumbers/*}:undelete:\x01*ZC">/v2beta1/{name=projects/*/locations/*/phoneNumbers/*}:undelete:\x01*'
    _globals['_PHONENUMBER']._serialized_start = 237
    _globals['_PHONENUMBER']._serialized_end = 670
    _globals['_PHONENUMBER_LIFECYCLESTATE']._serialized_start = 424
    _globals['_PHONENUMBER_LIFECYCLESTATE']._serialized_end = 507
    _globals['_DELETEPHONENUMBERREQUEST']._serialized_start = 672
    _globals['_DELETEPHONENUMBERREQUEST']._serialized_end = 759
    _globals['_UNDELETEPHONENUMBERREQUEST']._serialized_start = 761
    _globals['_UNDELETEPHONENUMBERREQUEST']._serialized_end = 850
    _globals['_LISTPHONENUMBERSREQUEST']._serialized_start = 853
    _globals['_LISTPHONENUMBERSREQUEST']._serialized_end = 1017
    _globals['_LISTPHONENUMBERSRESPONSE']._serialized_start = 1019
    _globals['_LISTPHONENUMBERSRESPONSE']._serialized_end = 1139
    _globals['_UPDATEPHONENUMBERREQUEST']._serialized_start = 1142
    _globals['_UPDATEPHONENUMBERREQUEST']._serialized_end = 1295
    _globals['_PHONENUMBERS']._serialized_start = 1298
    _globals['_PHONENUMBERS']._serialized_end = 2520