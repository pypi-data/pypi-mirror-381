"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/payments_account_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.resources import payments_account_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_payments__account__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v20/services/payments_account_service.proto\x12!google.ads.googleads.v20.services\x1a9google/ads/googleads/v20/resources/payments_account.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"7\n\x1bListPaymentsAccountsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02"n\n\x1cListPaymentsAccountsResponse\x12N\n\x11payments_accounts\x18\x01 \x03(\x0b23.google.ads.googleads.v20.resources.PaymentsAccount2\xc0\x02\n\x16PaymentsAccountService\x12\xde\x01\n\x14ListPaymentsAccounts\x12>.google.ads.googleads.v20.services.ListPaymentsAccountsRequest\x1a?.google.ads.googleads.v20.services.ListPaymentsAccountsResponse"E\xdaA\x0bcustomer_id\x82\xd3\xe4\x93\x021\x12//v20/customers/{customer_id=*}/paymentsAccounts\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x87\x02\n%com.google.ads.googleads.v20.servicesB\x1bPaymentsAccountServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.payments_account_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x1bPaymentsAccountServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_LISTPAYMENTSACCOUNTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_LISTPAYMENTSACCOUNTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_PAYMENTSACCOUNTSERVICE']._loaded_options = None
    _globals['_PAYMENTSACCOUNTSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_PAYMENTSACCOUNTSERVICE'].methods_by_name['ListPaymentsAccounts']._loaded_options = None
    _globals['_PAYMENTSACCOUNTSERVICE'].methods_by_name['ListPaymentsAccounts']._serialized_options = b'\xdaA\x0bcustomer_id\x82\xd3\xe4\x93\x021\x12//v20/customers/{customer_id=*}/paymentsAccounts'
    _globals['_LISTPAYMENTSACCOUNTSREQUEST']._serialized_start = 250
    _globals['_LISTPAYMENTSACCOUNTSREQUEST']._serialized_end = 305
    _globals['_LISTPAYMENTSACCOUNTSRESPONSE']._serialized_start = 307
    _globals['_LISTPAYMENTSACCOUNTSRESPONSE']._serialized_end = 417
    _globals['_PAYMENTSACCOUNTSERVICE']._serialized_start = 420
    _globals['_PAYMENTSACCOUNTSERVICE']._serialized_end = 740