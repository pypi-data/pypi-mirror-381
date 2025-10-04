"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/account_link_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.resources import account_link_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_account__link__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/googleads/v21/services/account_link_service.proto\x12!google.ads.googleads.v21.services\x1a5google/ads/googleads/v21/resources/account_link.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\x80\x01\n\x18CreateAccountLinkRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12J\n\x0caccount_link\x18\x02 \x01(\x0b2/.google.ads.googleads.v21.resources.AccountLinkB\x03\xe0A\x02"]\n\x19CreateAccountLinkResponse\x12@\n\rresource_name\x18\x01 \x01(\tB)\xfaA&\n$googleads.googleapis.com/AccountLink"\xb5\x01\n\x18MutateAccountLinkRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12O\n\toperation\x18\x02 \x01(\x0b27.google.ads.googleads.v21.services.AccountLinkOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xd4\x01\n\x14AccountLinkOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12A\n\x06update\x18\x02 \x01(\x0b2/.google.ads.googleads.v21.resources.AccountLinkH\x00\x12;\n\x06remove\x18\x03 \x01(\tB)\xfaA&\n$googleads.googleapis.com/AccountLinkH\x00B\x0b\n\toperation"\x9a\x01\n\x19MutateAccountLinkResponse\x12J\n\x06result\x18\x01 \x01(\x0b2:.google.ads.googleads.v21.services.MutateAccountLinkResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"[\n\x17MutateAccountLinkResult\x12@\n\rresource_name\x18\x01 \x01(\tB)\xfaA&\n$googleads.googleapis.com/AccountLink2\xae\x04\n\x12AccountLinkService\x12\xe8\x01\n\x11CreateAccountLink\x12;.google.ads.googleads.v21.services.CreateAccountLinkRequest\x1a<.google.ads.googleads.v21.services.CreateAccountLinkResponse"X\xdaA\x18customer_id,account_link\x82\xd3\xe4\x93\x027"2/v21/customers/{customer_id=*}/accountLinks:create:\x01*\x12\xe5\x01\n\x11MutateAccountLink\x12;.google.ads.googleads.v21.services.MutateAccountLinkRequest\x1a<.google.ads.googleads.v21.services.MutateAccountLinkResponse"U\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x027"2/v21/customers/{customer_id=*}/accountLinks:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x83\x02\n%com.google.ads.googleads.v21.servicesB\x17AccountLinkServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.account_link_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x17AccountLinkServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_CREATEACCOUNTLINKREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_CREATEACCOUNTLINKREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEACCOUNTLINKREQUEST'].fields_by_name['account_link']._loaded_options = None
    _globals['_CREATEACCOUNTLINKREQUEST'].fields_by_name['account_link']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEACCOUNTLINKRESPONSE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CREATEACCOUNTLINKRESPONSE'].fields_by_name['resource_name']._serialized_options = b'\xfaA&\n$googleads.googleapis.com/AccountLink'
    _globals['_MUTATEACCOUNTLINKREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEACCOUNTLINKREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEACCOUNTLINKREQUEST'].fields_by_name['operation']._loaded_options = None
    _globals['_MUTATEACCOUNTLINKREQUEST'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_ACCOUNTLINKOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_ACCOUNTLINKOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA&\n$googleads.googleapis.com/AccountLink'
    _globals['_MUTATEACCOUNTLINKRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEACCOUNTLINKRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA&\n$googleads.googleapis.com/AccountLink'
    _globals['_ACCOUNTLINKSERVICE']._loaded_options = None
    _globals['_ACCOUNTLINKSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_ACCOUNTLINKSERVICE'].methods_by_name['CreateAccountLink']._loaded_options = None
    _globals['_ACCOUNTLINKSERVICE'].methods_by_name['CreateAccountLink']._serialized_options = b'\xdaA\x18customer_id,account_link\x82\xd3\xe4\x93\x027"2/v21/customers/{customer_id=*}/accountLinks:create:\x01*'
    _globals['_ACCOUNTLINKSERVICE'].methods_by_name['MutateAccountLink']._loaded_options = None
    _globals['_ACCOUNTLINKSERVICE'].methods_by_name['MutateAccountLink']._serialized_options = b'\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x027"2/v21/customers/{customer_id=*}/accountLinks:mutate:\x01*'
    _globals['_CREATEACCOUNTLINKREQUEST']._serialized_start = 329
    _globals['_CREATEACCOUNTLINKREQUEST']._serialized_end = 457
    _globals['_CREATEACCOUNTLINKRESPONSE']._serialized_start = 459
    _globals['_CREATEACCOUNTLINKRESPONSE']._serialized_end = 552
    _globals['_MUTATEACCOUNTLINKREQUEST']._serialized_start = 555
    _globals['_MUTATEACCOUNTLINKREQUEST']._serialized_end = 736
    _globals['_ACCOUNTLINKOPERATION']._serialized_start = 739
    _globals['_ACCOUNTLINKOPERATION']._serialized_end = 951
    _globals['_MUTATEACCOUNTLINKRESPONSE']._serialized_start = 954
    _globals['_MUTATEACCOUNTLINKRESPONSE']._serialized_end = 1108
    _globals['_MUTATEACCOUNTLINKRESULT']._serialized_start = 1110
    _globals['_MUTATEACCOUNTLINKRESULT']._serialized_end = 1201
    _globals['_ACCOUNTLINKSERVICE']._serialized_start = 1204
    _globals['_ACCOUNTLINKSERVICE']._serialized_end = 1762