"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/lfp/v1/lfpstore.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/shopping/merchant/lfp/v1/lfpstore.proto\x12\x1fgoogle.shopping.merchant.lfp.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto"\xe2\x05\n\x08LfpStore\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12\x1b\n\x0etarget_account\x18\x02 \x01(\x03B\x03\xe0A\x02\x12\x1a\n\nstore_code\x18\x03 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12\x1a\n\rstore_address\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x1c\n\nstore_name\x18\x05 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12\x1e\n\x0cphone_number\x18\x06 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x12\x1d\n\x0bwebsite_uri\x18\x07 \x01(\tB\x03\xe0A\x01H\x02\x88\x01\x01\x12\x1a\n\rgcid_category\x18\x08 \x03(\tB\x03\xe0A\x01\x12\x1a\n\x08place_id\x18\t \x01(\tB\x03\xe0A\x01H\x03\x88\x01\x01\x12\\\n\x0ematching_state\x18\n \x01(\x0e2<.google.shopping.merchant.lfp.v1.LfpStore.StoreMatchingStateB\x06\xe0A\x01\xe0A\x03\x12(\n\x13matching_state_hint\x18\x0b \x01(\tB\x06\xe0A\x01\xe0A\x03H\x04\x88\x01\x01"}\n\x12StoreMatchingState\x12$\n STORE_MATCHING_STATE_UNSPECIFIED\x10\x00\x12 \n\x1cSTORE_MATCHING_STATE_MATCHED\x10\x01\x12\x1f\n\x1bSTORE_MATCHING_STATE_FAILED\x10\x02:z\xeaAw\n#merchantapi.googleapis.com/LfpStore\x12;accounts/{account}/lfpStores/{target_merchant}~{store_code}*\tlfpStores2\x08lfpStoreB\r\n\x0b_store_nameB\x0f\n\r_phone_numberB\x0e\n\x0c_website_uriB\x0b\n\t_place_idB\x16\n\x14_matching_state_hint"O\n\x12GetLfpStoreRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/LfpStore"\x97\x01\n\x15InsertLfpStoreRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#merchantapi.googleapis.com/LfpStore\x12A\n\tlfp_store\x18\x02 \x01(\x0b2).google.shopping.merchant.lfp.v1.LfpStoreB\x03\xe0A\x02"R\n\x15DeleteLfpStoreRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/LfpStore"\xa1\x01\n\x14ListLfpStoresRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#merchantapi.googleapis.com/LfpStore\x12\x1b\n\x0etarget_account\x18\x02 \x01(\x03B\x03\xe0A\x02\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"o\n\x15ListLfpStoresResponse\x12=\n\nlfp_stores\x18\x01 \x03(\x0b2).google.shopping.merchant.lfp.v1.LfpStore\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x9c\x06\n\x0fLfpStoreService\x12\xa3\x01\n\x0bGetLfpStore\x123.google.shopping.merchant.lfp.v1.GetLfpStoreRequest\x1a).google.shopping.merchant.lfp.v1.LfpStore"4\xdaA\x04name\x82\xd3\xe4\x93\x02\'\x12%/lfp/v1/{name=accounts/*/lfpStores/*}\x12\xc7\x01\n\x0eInsertLfpStore\x126.google.shopping.merchant.lfp.v1.InsertLfpStoreRequest\x1a).google.shopping.merchant.lfp.v1.LfpStore"R\xdaA\x10parent,lfp_store\x82\xd3\xe4\x93\x029",/lfp/v1/{parent=accounts/*}/lfpStores:insert:\tlfp_store\x12\x96\x01\n\x0eDeleteLfpStore\x126.google.shopping.merchant.lfp.v1.DeleteLfpStoreRequest\x1a\x16.google.protobuf.Empty"4\xdaA\x04name\x82\xd3\xe4\x93\x02\'*%/lfp/v1/{name=accounts/*/lfpStores/*}\x12\xb6\x01\n\rListLfpStores\x125.google.shopping.merchant.lfp.v1.ListLfpStoresRequest\x1a6.google.shopping.merchant.lfp.v1.ListLfpStoresResponse"6\xdaA\x06parent\x82\xd3\xe4\x93\x02\'\x12%/lfp/v1/{parent=accounts/*}/lfpStores\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xdd\x01\n#com.google.shopping.merchant.lfp.v1B\rLfpStoreProtoP\x01Z;cloud.google.com/go/shopping/merchant/lfp/apiv1/lfppb;lfppb\xaa\x02\x1fGoogle.Shopping.Merchant.Lfp.V1\xca\x02\x1fGoogle\\Shopping\\Merchant\\Lfp\\V1\xea\x02#Google::Shopping::Merchant::Lfp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.lfp.v1.lfpstore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.shopping.merchant.lfp.v1B\rLfpStoreProtoP\x01Z;cloud.google.com/go/shopping/merchant/lfp/apiv1/lfppb;lfppb\xaa\x02\x1fGoogle.Shopping.Merchant.Lfp.V1\xca\x02\x1fGoogle\\Shopping\\Merchant\\Lfp\\V1\xea\x02#Google::Shopping::Merchant::Lfp::V1'
    _globals['_LFPSTORE'].fields_by_name['name']._loaded_options = None
    _globals['_LFPSTORE'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_LFPSTORE'].fields_by_name['target_account']._loaded_options = None
    _globals['_LFPSTORE'].fields_by_name['target_account']._serialized_options = b'\xe0A\x02'
    _globals['_LFPSTORE'].fields_by_name['store_code']._loaded_options = None
    _globals['_LFPSTORE'].fields_by_name['store_code']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_LFPSTORE'].fields_by_name['store_address']._loaded_options = None
    _globals['_LFPSTORE'].fields_by_name['store_address']._serialized_options = b'\xe0A\x02'
    _globals['_LFPSTORE'].fields_by_name['store_name']._loaded_options = None
    _globals['_LFPSTORE'].fields_by_name['store_name']._serialized_options = b'\xe0A\x01'
    _globals['_LFPSTORE'].fields_by_name['phone_number']._loaded_options = None
    _globals['_LFPSTORE'].fields_by_name['phone_number']._serialized_options = b'\xe0A\x01'
    _globals['_LFPSTORE'].fields_by_name['website_uri']._loaded_options = None
    _globals['_LFPSTORE'].fields_by_name['website_uri']._serialized_options = b'\xe0A\x01'
    _globals['_LFPSTORE'].fields_by_name['gcid_category']._loaded_options = None
    _globals['_LFPSTORE'].fields_by_name['gcid_category']._serialized_options = b'\xe0A\x01'
    _globals['_LFPSTORE'].fields_by_name['place_id']._loaded_options = None
    _globals['_LFPSTORE'].fields_by_name['place_id']._serialized_options = b'\xe0A\x01'
    _globals['_LFPSTORE'].fields_by_name['matching_state']._loaded_options = None
    _globals['_LFPSTORE'].fields_by_name['matching_state']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_LFPSTORE'].fields_by_name['matching_state_hint']._loaded_options = None
    _globals['_LFPSTORE'].fields_by_name['matching_state_hint']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_LFPSTORE']._loaded_options = None
    _globals['_LFPSTORE']._serialized_options = b'\xeaAw\n#merchantapi.googleapis.com/LfpStore\x12;accounts/{account}/lfpStores/{target_merchant}~{store_code}*\tlfpStores2\x08lfpStore'
    _globals['_GETLFPSTOREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETLFPSTOREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/LfpStore'
    _globals['_INSERTLFPSTOREREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_INSERTLFPSTOREREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#merchantapi.googleapis.com/LfpStore'
    _globals['_INSERTLFPSTOREREQUEST'].fields_by_name['lfp_store']._loaded_options = None
    _globals['_INSERTLFPSTOREREQUEST'].fields_by_name['lfp_store']._serialized_options = b'\xe0A\x02'
    _globals['_DELETELFPSTOREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETELFPSTOREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/LfpStore'
    _globals['_LISTLFPSTORESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTLFPSTORESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#merchantapi.googleapis.com/LfpStore'
    _globals['_LISTLFPSTORESREQUEST'].fields_by_name['target_account']._loaded_options = None
    _globals['_LISTLFPSTORESREQUEST'].fields_by_name['target_account']._serialized_options = b'\xe0A\x02'
    _globals['_LISTLFPSTORESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTLFPSTORESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTLFPSTORESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTLFPSTORESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LFPSTORESERVICE']._loaded_options = None
    _globals['_LFPSTORESERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_LFPSTORESERVICE'].methods_by_name['GetLfpStore']._loaded_options = None
    _globals['_LFPSTORESERVICE'].methods_by_name['GetLfpStore']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02'\x12%/lfp/v1/{name=accounts/*/lfpStores/*}"
    _globals['_LFPSTORESERVICE'].methods_by_name['InsertLfpStore']._loaded_options = None
    _globals['_LFPSTORESERVICE'].methods_by_name['InsertLfpStore']._serialized_options = b'\xdaA\x10parent,lfp_store\x82\xd3\xe4\x93\x029",/lfp/v1/{parent=accounts/*}/lfpStores:insert:\tlfp_store'
    _globals['_LFPSTORESERVICE'].methods_by_name['DeleteLfpStore']._loaded_options = None
    _globals['_LFPSTORESERVICE'].methods_by_name['DeleteLfpStore']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02'*%/lfp/v1/{name=accounts/*/lfpStores/*}"
    _globals['_LFPSTORESERVICE'].methods_by_name['ListLfpStores']._loaded_options = None
    _globals['_LFPSTORESERVICE'].methods_by_name['ListLfpStores']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02'\x12%/lfp/v1/{parent=accounts/*}/lfpStores"
    _globals['_LFPSTORE']._serialized_start = 228
    _globals['_LFPSTORE']._serialized_end = 966
    _globals['_LFPSTORE_STOREMATCHINGSTATE']._serialized_start = 632
    _globals['_LFPSTORE_STOREMATCHINGSTATE']._serialized_end = 757
    _globals['_GETLFPSTOREREQUEST']._serialized_start = 968
    _globals['_GETLFPSTOREREQUEST']._serialized_end = 1047
    _globals['_INSERTLFPSTOREREQUEST']._serialized_start = 1050
    _globals['_INSERTLFPSTOREREQUEST']._serialized_end = 1201
    _globals['_DELETELFPSTOREREQUEST']._serialized_start = 1203
    _globals['_DELETELFPSTOREREQUEST']._serialized_end = 1285
    _globals['_LISTLFPSTORESREQUEST']._serialized_start = 1288
    _globals['_LISTLFPSTORESREQUEST']._serialized_end = 1449
    _globals['_LISTLFPSTORESRESPONSE']._serialized_start = 1451
    _globals['_LISTLFPSTORESRESPONSE']._serialized_end = 1562
    _globals['_LFPSTORESERVICE']._serialized_start = 1565
    _globals['_LFPSTORESERVICE']._serialized_end = 2361