"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/online_return_policy.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
from ......google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/shopping/merchant/accounts/v1/online_return_policy.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/shopping/type/types.proto\x1a\x16google/type/date.proto"c\n\x1cGetOnlineReturnPolicyRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-merchantapi.googleapis.com/OnlineReturnPolicy"\xc5\x01\n\x1fCreateOnlineReturnPolicyRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-merchantapi.googleapis.com/OnlineReturnPolicy\x12[\n\x14online_return_policy\x18\x02 \x01(\x0b28.google.shopping.merchant.accounts.v1.OnlineReturnPolicyB\x03\xe0A\x02"f\n\x1fDeleteOnlineReturnPolicyRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-merchantapi.googleapis.com/OnlineReturnPolicy"\x99\x01\n\x1fListOnlineReturnPoliciesRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-merchantapi.googleapis.com/OnlineReturnPolicy\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x95\x01\n ListOnlineReturnPoliciesResponse\x12X\n\x16online_return_policies\x18\x01 \x03(\x0b28.google.shopping.merchant.accounts.v1.OnlineReturnPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xf8\x11\n\x12OnlineReturnPolicy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1d\n\x10return_policy_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x15\n\x05label\x18\x03 \x01(\tB\x06\xe0A\x05\xe0A\x01\x12\x19\n\tcountries\x18\x04 \x03(\tB\x06\xe0A\x02\xe0A\x05\x12T\n\x06policy\x18\x05 \x01(\x0b2?.google.shopping.merchant.accounts.v1.OnlineReturnPolicy.PolicyB\x03\xe0A\x01\x12j\n\x12seasonal_overrides\x18\x0e \x03(\x0b2I.google.shopping.merchant.accounts.v1.OnlineReturnPolicy.SeasonalOverrideB\x03\xe0A\x01\x12c\n\x0erestocking_fee\x18\x06 \x01(\x0b2F.google.shopping.merchant.accounts.v1.OnlineReturnPolicy.RestockingFeeB\x03\xe0A\x01\x12b\n\x0ereturn_methods\x18\x07 \x03(\x0e2E.google.shopping.merchant.accounts.v1.OnlineReturnPolicy.ReturnMethodB\x03\xe0A\x01\x12d\n\x0fitem_conditions\x18\x08 \x03(\x0e2F.google.shopping.merchant.accounts.v1.OnlineReturnPolicy.ItemConditionB\x03\xe0A\x01\x12l\n\x13return_shipping_fee\x18\t \x01(\x0b2J.google.shopping.merchant.accounts.v1.OnlineReturnPolicy.ReturnShippingFeeB\x03\xe0A\x01\x12\x1e\n\x11return_policy_uri\x18\n \x01(\tB\x03\xe0A\x02\x12\'\n\x15accept_defective_only\x18\x0b \x01(\x08B\x03\xe0A\x01H\x00\x88\x01\x01\x12%\n\x13process_refund_days\x18\x0c \x01(\x05B\x03\xe0A\x01H\x01\x88\x01\x01\x12!\n\x0faccept_exchange\x18\r \x01(\x08B\x03\xe0A\x01H\x02\x88\x01\x01\x12q\n\x13return_label_source\x18\x0f \x01(\x0e2J.google.shopping.merchant.accounts.v1.OnlineReturnPolicy.ReturnLabelSourceB\x03\xe0A\x01H\x03\x88\x01\x01\x1a\xf0\x01\n\x11ReturnShippingFee\x12b\n\x04type\x18\x01 \x01(\x0e2O.google.shopping.merchant.accounts.v1.OnlineReturnPolicy.ReturnShippingFee.TypeB\x03\xe0A\x02\x12.\n\tfixed_fee\x18\x02 \x01(\x0b2\x1b.google.shopping.type.Price"G\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05FIXED\x10\x01\x12\x1e\n\x1aCUSTOMER_PAYING_ACTUAL_FEE\x10\x02\x1ab\n\rRestockingFee\x120\n\tfixed_fee\x18\x01 \x01(\x0b2\x1b.google.shopping.type.PriceH\x00\x12\x17\n\rmicro_percent\x18\x02 \x01(\x05H\x00B\x06\n\x04type\x1a\xd1\x01\n\x06Policy\x12R\n\x04type\x18\x01 \x01(\x0e2D.google.shopping.merchant.accounts.v1.OnlineReturnPolicy.Policy.Type\x12\x0c\n\x04days\x18\x02 \x01(\x03"e\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12!\n\x1dNUMBER_OF_DAYS_AFTER_DELIVERY\x10\x01\x12\x0e\n\nNO_RETURNS\x10\x02\x12\x14\n\x10LIFETIME_RETURNS\x10\x03\x1a\xd4\x01\n\x10SeasonalOverride\x12\x15\n\x0breturn_days\x18\x05 \x01(\x05H\x00\x12.\n\x11return_until_date\x18\x06 \x01(\x0b2\x11.google.type.DateH\x00\x12\x12\n\x05label\x18\x01 \x01(\tB\x03\xe0A\x02\x12*\n\nstart_date\x18\x02 \x01(\x0b2\x11.google.type.DateB\x03\xe0A\x02\x12(\n\x08end_date\x18\x03 \x01(\x0b2\x11.google.type.DateB\x03\xe0A\x02B\x0f\n\rreturn_window"X\n\x0cReturnMethod\x12\x1d\n\x19RETURN_METHOD_UNSPECIFIED\x10\x00\x12\x0b\n\x07BY_MAIL\x10\x01\x12\x0c\n\x08IN_STORE\x10\x02\x12\x0e\n\nAT_A_KIOSK\x10\x03"B\n\rItemCondition\x12\x1e\n\x1aITEM_CONDITION_UNSPECIFIED\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\x08\n\x04USED\x10\x02"\x81\x01\n\x11ReturnLabelSource\x12#\n\x1fRETURN_LABEL_SOURCE_UNSPECIFIED\x10\x00\x12\x16\n\x12DOWNLOAD_AND_PRINT\x10\x01\x12\x12\n\x0eIN_THE_PACKAGE\x10\x02\x12\x1b\n\x17CUSTOMER_RESPONSIBILITY\x10\x03:\x96\x01\xeaA\x92\x01\n-merchantapi.googleapis.com/OnlineReturnPolicy\x127accounts/{account}/onlineReturnPolicies/{return_policy}*\x14onlineReturnPolicies2\x12onlineReturnPolicyB\x18\n\x16_accept_defective_onlyB\x16\n\x14_process_refund_daysB\x12\n\x10_accept_exchangeB\x16\n\x14_return_label_source2\x89\x08\n\x19OnlineReturnPolicyService\x12\xdb\x01\n\x15GetOnlineReturnPolicy\x12B.google.shopping.merchant.accounts.v1.GetOnlineReturnPolicyRequest\x1a8.google.shopping.merchant.accounts.v1.OnlineReturnPolicy"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/accounts/v1/{name=accounts/*/onlineReturnPolicies/*}\x12\xf1\x01\n\x18ListOnlineReturnPolicies\x12E.google.shopping.merchant.accounts.v1.ListOnlineReturnPoliciesRequest\x1aF.google.shopping.merchant.accounts.v1.ListOnlineReturnPoliciesResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/accounts/v1/{parent=accounts/*}/onlineReturnPolicies\x12\x8e\x02\n\x18CreateOnlineReturnPolicy\x12E.google.shopping.merchant.accounts.v1.CreateOnlineReturnPolicyRequest\x1a8.google.shopping.merchant.accounts.v1.OnlineReturnPolicy"q\xdaA\x1bparent,online_return_policy\x82\xd3\xe4\x93\x02M"5/accounts/v1/{parent=accounts/*}/onlineReturnPolicies:\x14online_return_policy\x12\xbf\x01\n\x18DeleteOnlineReturnPolicy\x12E.google.shopping.merchant.accounts.v1.DeleteOnlineReturnPolicyRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x04name\x82\xd3\xe4\x93\x027*5/accounts/v1/{name=accounts/*/onlineReturnPolicies/*}\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x8a\x02\n(com.google.shopping.merchant.accounts.v1B\x17OnlineReturnPolicyProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.online_return_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B\x17OnlineReturnPolicyProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_GETONLINERETURNPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETONLINERETURNPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-merchantapi.googleapis.com/OnlineReturnPolicy'
    _globals['_CREATEONLINERETURNPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEONLINERETURNPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-merchantapi.googleapis.com/OnlineReturnPolicy'
    _globals['_CREATEONLINERETURNPOLICYREQUEST'].fields_by_name['online_return_policy']._loaded_options = None
    _globals['_CREATEONLINERETURNPOLICYREQUEST'].fields_by_name['online_return_policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEONLINERETURNPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEONLINERETURNPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-merchantapi.googleapis.com/OnlineReturnPolicy'
    _globals['_LISTONLINERETURNPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTONLINERETURNPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-merchantapi.googleapis.com/OnlineReturnPolicy'
    _globals['_LISTONLINERETURNPOLICIESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTONLINERETURNPOLICIESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTONLINERETURNPOLICIESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTONLINERETURNPOLICIESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_ONLINERETURNPOLICY_RETURNSHIPPINGFEE'].fields_by_name['type']._loaded_options = None
    _globals['_ONLINERETURNPOLICY_RETURNSHIPPINGFEE'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_ONLINERETURNPOLICY_SEASONALOVERRIDE'].fields_by_name['label']._loaded_options = None
    _globals['_ONLINERETURNPOLICY_SEASONALOVERRIDE'].fields_by_name['label']._serialized_options = b'\xe0A\x02'
    _globals['_ONLINERETURNPOLICY_SEASONALOVERRIDE'].fields_by_name['start_date']._loaded_options = None
    _globals['_ONLINERETURNPOLICY_SEASONALOVERRIDE'].fields_by_name['start_date']._serialized_options = b'\xe0A\x02'
    _globals['_ONLINERETURNPOLICY_SEASONALOVERRIDE'].fields_by_name['end_date']._loaded_options = None
    _globals['_ONLINERETURNPOLICY_SEASONALOVERRIDE'].fields_by_name['end_date']._serialized_options = b'\xe0A\x02'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['name']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['return_policy_id']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['return_policy_id']._serialized_options = b'\xe0A\x03'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['label']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['label']._serialized_options = b'\xe0A\x05\xe0A\x01'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['countries']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['countries']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['policy']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['policy']._serialized_options = b'\xe0A\x01'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['seasonal_overrides']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['seasonal_overrides']._serialized_options = b'\xe0A\x01'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['restocking_fee']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['restocking_fee']._serialized_options = b'\xe0A\x01'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['return_methods']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['return_methods']._serialized_options = b'\xe0A\x01'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['item_conditions']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['item_conditions']._serialized_options = b'\xe0A\x01'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['return_shipping_fee']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['return_shipping_fee']._serialized_options = b'\xe0A\x01'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['return_policy_uri']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['return_policy_uri']._serialized_options = b'\xe0A\x02'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['accept_defective_only']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['accept_defective_only']._serialized_options = b'\xe0A\x01'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['process_refund_days']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['process_refund_days']._serialized_options = b'\xe0A\x01'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['accept_exchange']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['accept_exchange']._serialized_options = b'\xe0A\x01'
    _globals['_ONLINERETURNPOLICY'].fields_by_name['return_label_source']._loaded_options = None
    _globals['_ONLINERETURNPOLICY'].fields_by_name['return_label_source']._serialized_options = b'\xe0A\x01'
    _globals['_ONLINERETURNPOLICY']._loaded_options = None
    _globals['_ONLINERETURNPOLICY']._serialized_options = b'\xeaA\x92\x01\n-merchantapi.googleapis.com/OnlineReturnPolicy\x127accounts/{account}/onlineReturnPolicies/{return_policy}*\x14onlineReturnPolicies2\x12onlineReturnPolicy'
    _globals['_ONLINERETURNPOLICYSERVICE']._loaded_options = None
    _globals['_ONLINERETURNPOLICYSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_ONLINERETURNPOLICYSERVICE'].methods_by_name['GetOnlineReturnPolicy']._loaded_options = None
    _globals['_ONLINERETURNPOLICYSERVICE'].methods_by_name['GetOnlineReturnPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/accounts/v1/{name=accounts/*/onlineReturnPolicies/*}'
    _globals['_ONLINERETURNPOLICYSERVICE'].methods_by_name['ListOnlineReturnPolicies']._loaded_options = None
    _globals['_ONLINERETURNPOLICYSERVICE'].methods_by_name['ListOnlineReturnPolicies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/accounts/v1/{parent=accounts/*}/onlineReturnPolicies'
    _globals['_ONLINERETURNPOLICYSERVICE'].methods_by_name['CreateOnlineReturnPolicy']._loaded_options = None
    _globals['_ONLINERETURNPOLICYSERVICE'].methods_by_name['CreateOnlineReturnPolicy']._serialized_options = b'\xdaA\x1bparent,online_return_policy\x82\xd3\xe4\x93\x02M"5/accounts/v1/{parent=accounts/*}/onlineReturnPolicies:\x14online_return_policy'
    _globals['_ONLINERETURNPOLICYSERVICE'].methods_by_name['DeleteOnlineReturnPolicy']._loaded_options = None
    _globals['_ONLINERETURNPOLICYSERVICE'].methods_by_name['DeleteOnlineReturnPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027*5/accounts/v1/{name=accounts/*/onlineReturnPolicies/*}'
    _globals['_GETONLINERETURNPOLICYREQUEST']._serialized_start = 307
    _globals['_GETONLINERETURNPOLICYREQUEST']._serialized_end = 406
    _globals['_CREATEONLINERETURNPOLICYREQUEST']._serialized_start = 409
    _globals['_CREATEONLINERETURNPOLICYREQUEST']._serialized_end = 606
    _globals['_DELETEONLINERETURNPOLICYREQUEST']._serialized_start = 608
    _globals['_DELETEONLINERETURNPOLICYREQUEST']._serialized_end = 710
    _globals['_LISTONLINERETURNPOLICIESREQUEST']._serialized_start = 713
    _globals['_LISTONLINERETURNPOLICIESREQUEST']._serialized_end = 866
    _globals['_LISTONLINERETURNPOLICIESRESPONSE']._serialized_start = 869
    _globals['_LISTONLINERETURNPOLICIESRESPONSE']._serialized_end = 1018
    _globals['_ONLINERETURNPOLICY']._serialized_start = 1021
    _globals['_ONLINERETURNPOLICY']._serialized_end = 3317
    _globals['_ONLINERETURNPOLICY_RETURNSHIPPINGFEE']._serialized_start = 2013
    _globals['_ONLINERETURNPOLICY_RETURNSHIPPINGFEE']._serialized_end = 2253
    _globals['_ONLINERETURNPOLICY_RETURNSHIPPINGFEE_TYPE']._serialized_start = 2182
    _globals['_ONLINERETURNPOLICY_RETURNSHIPPINGFEE_TYPE']._serialized_end = 2253
    _globals['_ONLINERETURNPOLICY_RESTOCKINGFEE']._serialized_start = 2255
    _globals['_ONLINERETURNPOLICY_RESTOCKINGFEE']._serialized_end = 2353
    _globals['_ONLINERETURNPOLICY_POLICY']._serialized_start = 2356
    _globals['_ONLINERETURNPOLICY_POLICY']._serialized_end = 2565
    _globals['_ONLINERETURNPOLICY_POLICY_TYPE']._serialized_start = 2464
    _globals['_ONLINERETURNPOLICY_POLICY_TYPE']._serialized_end = 2565
    _globals['_ONLINERETURNPOLICY_SEASONALOVERRIDE']._serialized_start = 2568
    _globals['_ONLINERETURNPOLICY_SEASONALOVERRIDE']._serialized_end = 2780
    _globals['_ONLINERETURNPOLICY_RETURNMETHOD']._serialized_start = 2782
    _globals['_ONLINERETURNPOLICY_RETURNMETHOD']._serialized_end = 2870
    _globals['_ONLINERETURNPOLICY_ITEMCONDITION']._serialized_start = 2872
    _globals['_ONLINERETURNPOLICY_ITEMCONDITION']._serialized_end = 2938
    _globals['_ONLINERETURNPOLICY_RETURNLABELSOURCE']._serialized_start = 2941
    _globals['_ONLINERETURNPOLICY_RETURNLABELSOURCE']._serialized_end = 3070
    _globals['_ONLINERETURNPOLICYSERVICE']._serialized_start = 3320
    _globals['_ONLINERETURNPOLICYSERVICE']._serialized_end = 4353