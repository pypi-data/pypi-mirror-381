"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/accountservices.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/shopping/merchant/accounts/v1/accountservices.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto"\xc9\x07\n\x0eAccountService\x12W\n\x13products_management\x18d \x01(\x0b28.google.shopping.merchant.accounts.v1.ProductsManagementH\x00\x12Y\n\x14campaigns_management\x18e \x01(\x0b29.google.shopping.merchant.accounts.v1.CampaignsManagementH\x00\x12U\n\x12account_management\x18f \x01(\x0b27.google.shopping.merchant.accounts.v1.AccountManagementH\x00\x12W\n\x13account_aggregation\x18g \x01(\x0b28.google.shopping.merchant.accounts.v1.AccountAggregationH\x00\x12`\n\x18local_listing_management\x18h \x01(\x0b2<.google.shopping.merchant.accounts.v1.LocalListingManagementH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1a\n\x08provider\x18\x02 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12"\n\x15provider_display_name\x18\x03 \x01(\tB\x03\xe0A\x03\x12G\n\thandshake\x18\x04 \x01(\x0b2/.google.shopping.merchant.accounts.v1.HandshakeB\x03\xe0A\x03\x12X\n\nmutability\x18\x05 \x01(\x0e2?.google.shopping.merchant.accounts.v1.AccountService.MutabilityB\x03\xe0A\x03\x12 \n\x13external_account_id\x18\x06 \x01(\tB\x03\xe0A\x05"D\n\nMutability\x12\x1a\n\x16MUTABILITY_UNSPECIFIED\x10\x00\x12\x0b\n\x07MUTABLE\x10\x01\x12\r\n\tIMMUTABLE\x10\x02:v\xeaAs\n)merchantapi.googleapis.com/AccountService\x12%accounts/{account}/services/{service}*\x0faccountServices2\x0eaccountServiceB\x0e\n\x0cservice_typeB\x0b\n\t_provider"[\n\x18GetAccountServiceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/AccountService"\x89\x01\n\x1aListAccountServicesRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x05 \x01(\x05B\x03\xe0A\x01"\x86\x01\n\x1bListAccountServicesResponse\x12N\n\x10account_services\x18\x01 \x03(\x0b24.google.shopping.merchant.accounts.v1.AccountService\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc5\x01\n\x1cProposeAccountServiceRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x15\n\x08provider\x18\x02 \x01(\tB\x03\xe0A\x02\x12R\n\x0faccount_service\x18\x04 \x01(\x0b24.google.shopping.merchant.accounts.v1.AccountServiceB\x03\xe0A\x02"_\n\x1cApproveAccountServiceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/AccountService"^\n\x1bRejectAccountServiceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/AccountService"\x14\n\x12ProductsManagement"\x15\n\x13CampaignsManagement"\x13\n\x11AccountManagement"\x14\n\x12AccountAggregation"\x18\n\x16LocalListingManagement"\xcd\x02\n\tHandshake\x12Z\n\x0eapproval_state\x18\x01 \x01(\x0e2=.google.shopping.merchant.accounts.v1.Handshake.ApprovalStateB\x03\xe0A\x03\x12I\n\x05actor\x18\x02 \x01(\x0e25.google.shopping.merchant.accounts.v1.Handshake.ActorB\x03\xe0A\x03"[\n\rApprovalState\x12\x1e\n\x1aAPPROVAL_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0f\n\x0bESTABLISHED\x10\x02\x12\x0c\n\x08REJECTED\x10\x03"<\n\x05Actor\x12\x15\n\x11ACTOR_UNSPECIFIED\x10\x00\x12\x0b\n\x07ACCOUNT\x10\x01\x12\x0f\n\x0bOTHER_PARTY\x10\x022\x85\t\n\x16AccountServicesService\x12\xc3\x01\n\x11GetAccountService\x12>.google.shopping.merchant.accounts.v1.GetAccountServiceRequest\x1a4.google.shopping.merchant.accounts.v1.AccountService"8\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/accounts/v1/{name=accounts/*/services/*}\x12\xd6\x01\n\x13ListAccountServices\x12@.google.shopping.merchant.accounts.v1.ListAccountServicesRequest\x1aA.google.shopping.merchant.accounts.v1.ListAccountServicesResponse":\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/accounts/v1/{parent=accounts/*}/services\x12\xf1\x01\n\x15ProposeAccountService\x12B.google.shopping.merchant.accounts.v1.ProposeAccountServiceRequest\x1a4.google.shopping.merchant.accounts.v1.AccountService"^\xdaA\x1fparent,provider,account_service\x82\xd3\xe4\x93\x026"1/accounts/v1/{parent=accounts/*}/services:propose:\x01*\x12\xd6\x01\n\x15ApproveAccountService\x12B.google.shopping.merchant.accounts.v1.ApproveAccountServiceRequest\x1a4.google.shopping.merchant.accounts.v1.AccountService"C\xdaA\x04name\x82\xd3\xe4\x93\x026"1/accounts/v1/{name=accounts/*/services/*}:approve:\x01*\x12\xb5\x01\n\x14RejectAccountService\x12A.google.shopping.merchant.accounts.v1.RejectAccountServiceRequest\x1a\x16.google.protobuf.Empty"B\xdaA\x04name\x82\xd3\xe4\x93\x025"0/accounts/v1/{name=accounts/*/services/*}:reject:\x01*\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x87\x02\n(com.google.shopping.merchant.accounts.v1B\x14AccountServicesProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.accountservices_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B\x14AccountServicesProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_ACCOUNTSERVICE'].fields_by_name['name']._loaded_options = None
    _globals['_ACCOUNTSERVICE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ACCOUNTSERVICE'].fields_by_name['provider']._loaded_options = None
    _globals['_ACCOUNTSERVICE'].fields_by_name['provider']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTSERVICE'].fields_by_name['provider_display_name']._loaded_options = None
    _globals['_ACCOUNTSERVICE'].fields_by_name['provider_display_name']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTSERVICE'].fields_by_name['handshake']._loaded_options = None
    _globals['_ACCOUNTSERVICE'].fields_by_name['handshake']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTSERVICE'].fields_by_name['mutability']._loaded_options = None
    _globals['_ACCOUNTSERVICE'].fields_by_name['mutability']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTSERVICE'].fields_by_name['external_account_id']._loaded_options = None
    _globals['_ACCOUNTSERVICE'].fields_by_name['external_account_id']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTSERVICE']._loaded_options = None
    _globals['_ACCOUNTSERVICE']._serialized_options = b'\xeaAs\n)merchantapi.googleapis.com/AccountService\x12%accounts/{account}/services/{service}*\x0faccountServices2\x0eaccountService'
    _globals['_GETACCOUNTSERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETACCOUNTSERVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/AccountService'
    _globals['_LISTACCOUNTSERVICESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACCOUNTSERVICESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_LISTACCOUNTSERVICESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTACCOUNTSERVICESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCOUNTSERVICESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTACCOUNTSERVICESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_PROPOSEACCOUNTSERVICEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_PROPOSEACCOUNTSERVICEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_PROPOSEACCOUNTSERVICEREQUEST'].fields_by_name['provider']._loaded_options = None
    _globals['_PROPOSEACCOUNTSERVICEREQUEST'].fields_by_name['provider']._serialized_options = b'\xe0A\x02'
    _globals['_PROPOSEACCOUNTSERVICEREQUEST'].fields_by_name['account_service']._loaded_options = None
    _globals['_PROPOSEACCOUNTSERVICEREQUEST'].fields_by_name['account_service']._serialized_options = b'\xe0A\x02'
    _globals['_APPROVEACCOUNTSERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_APPROVEACCOUNTSERVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/AccountService'
    _globals['_REJECTACCOUNTSERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REJECTACCOUNTSERVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/AccountService'
    _globals['_HANDSHAKE'].fields_by_name['approval_state']._loaded_options = None
    _globals['_HANDSHAKE'].fields_by_name['approval_state']._serialized_options = b'\xe0A\x03'
    _globals['_HANDSHAKE'].fields_by_name['actor']._loaded_options = None
    _globals['_HANDSHAKE'].fields_by_name['actor']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTSERVICESSERVICE']._loaded_options = None
    _globals['_ACCOUNTSERVICESSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_ACCOUNTSERVICESSERVICE'].methods_by_name['GetAccountService']._loaded_options = None
    _globals['_ACCOUNTSERVICESSERVICE'].methods_by_name['GetAccountService']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/accounts/v1/{name=accounts/*/services/*}'
    _globals['_ACCOUNTSERVICESSERVICE'].methods_by_name['ListAccountServices']._loaded_options = None
    _globals['_ACCOUNTSERVICESSERVICE'].methods_by_name['ListAccountServices']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/accounts/v1/{parent=accounts/*}/services'
    _globals['_ACCOUNTSERVICESSERVICE'].methods_by_name['ProposeAccountService']._loaded_options = None
    _globals['_ACCOUNTSERVICESSERVICE'].methods_by_name['ProposeAccountService']._serialized_options = b'\xdaA\x1fparent,provider,account_service\x82\xd3\xe4\x93\x026"1/accounts/v1/{parent=accounts/*}/services:propose:\x01*'
    _globals['_ACCOUNTSERVICESSERVICE'].methods_by_name['ApproveAccountService']._loaded_options = None
    _globals['_ACCOUNTSERVICESSERVICE'].methods_by_name['ApproveAccountService']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026"1/accounts/v1/{name=accounts/*/services/*}:approve:\x01*'
    _globals['_ACCOUNTSERVICESSERVICE'].methods_by_name['RejectAccountService']._loaded_options = None
    _globals['_ACCOUNTSERVICESSERVICE'].methods_by_name['RejectAccountService']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025"0/accounts/v1/{name=accounts/*/services/*}:reject:\x01*'
    _globals['_ACCOUNTSERVICE']._serialized_start = 245
    _globals['_ACCOUNTSERVICE']._serialized_end = 1214
    _globals['_ACCOUNTSERVICE_MUTABILITY']._serialized_start = 997
    _globals['_ACCOUNTSERVICE_MUTABILITY']._serialized_end = 1065
    _globals['_GETACCOUNTSERVICEREQUEST']._serialized_start = 1216
    _globals['_GETACCOUNTSERVICEREQUEST']._serialized_end = 1307
    _globals['_LISTACCOUNTSERVICESREQUEST']._serialized_start = 1310
    _globals['_LISTACCOUNTSERVICESREQUEST']._serialized_end = 1447
    _globals['_LISTACCOUNTSERVICESRESPONSE']._serialized_start = 1450
    _globals['_LISTACCOUNTSERVICESRESPONSE']._serialized_end = 1584
    _globals['_PROPOSEACCOUNTSERVICEREQUEST']._serialized_start = 1587
    _globals['_PROPOSEACCOUNTSERVICEREQUEST']._serialized_end = 1784
    _globals['_APPROVEACCOUNTSERVICEREQUEST']._serialized_start = 1786
    _globals['_APPROVEACCOUNTSERVICEREQUEST']._serialized_end = 1881
    _globals['_REJECTACCOUNTSERVICEREQUEST']._serialized_start = 1883
    _globals['_REJECTACCOUNTSERVICEREQUEST']._serialized_end = 1977
    _globals['_PRODUCTSMANAGEMENT']._serialized_start = 1979
    _globals['_PRODUCTSMANAGEMENT']._serialized_end = 1999
    _globals['_CAMPAIGNSMANAGEMENT']._serialized_start = 2001
    _globals['_CAMPAIGNSMANAGEMENT']._serialized_end = 2022
    _globals['_ACCOUNTMANAGEMENT']._serialized_start = 2024
    _globals['_ACCOUNTMANAGEMENT']._serialized_end = 2043
    _globals['_ACCOUNTAGGREGATION']._serialized_start = 2045
    _globals['_ACCOUNTAGGREGATION']._serialized_end = 2065
    _globals['_LOCALLISTINGMANAGEMENT']._serialized_start = 2067
    _globals['_LOCALLISTINGMANAGEMENT']._serialized_end = 2091
    _globals['_HANDSHAKE']._serialized_start = 2094
    _globals['_HANDSHAKE']._serialized_end = 2427
    _globals['_HANDSHAKE_APPROVALSTATE']._serialized_start = 2274
    _globals['_HANDSHAKE_APPROVALSTATE']._serialized_end = 2365
    _globals['_HANDSHAKE_ACTOR']._serialized_start = 2367
    _globals['_HANDSHAKE_ACTOR']._serialized_end = 2427
    _globals['_ACCOUNTSERVICESSERVICE']._serialized_start = 2430
    _globals['_ACCOUNTSERVICESSERVICE']._serialized_end = 3587