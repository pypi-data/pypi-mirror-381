"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/customer_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import access_role_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_access__role__pb2
from ......google.ads.googleads.v21.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v21.resources import customer_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_customer__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v21/services/customer_service.proto\x12!google.ads.googleads.v21.services\x1a0google/ads/googleads/v21/enums/access_role.proto\x1a:google/ads/googleads/v21/enums/response_content_type.proto\x1a1google/ads/googleads/v21/resources/customer.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\x82\x02\n\x15MutateCustomerRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12L\n\toperation\x18\x04 \x01(\x0b24.google.ads.googleads.v21.services.CustomerOperationB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x05 \x01(\x08\x12j\n\x15response_content_type\x18\x06 \x01(\x0e2K.google.ads.googleads.v21.enums.ResponseContentTypeEnum.ResponseContentType"\x98\x02\n\x1bCreateCustomerClientRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12J\n\x0fcustomer_client\x18\x02 \x01(\x0b2,.google.ads.googleads.v21.resources.CustomerB\x03\xe0A\x02\x12\x1a\n\remail_address\x18\x05 \x01(\tH\x00\x88\x01\x01\x12N\n\x0baccess_role\x18\x04 \x01(\x0e29.google.ads.googleads.v21.enums.AccessRoleEnum.AccessRole\x12\x15\n\rvalidate_only\x18\x06 \x01(\x08B\x10\n\x0e_email_address"\x82\x01\n\x11CustomerOperation\x12<\n\x06update\x18\x01 \x01(\x0b2,.google.ads.googleads.v21.resources.Customer\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"v\n\x1cCreateCustomerClientResponse\x12=\n\rresource_name\x18\x02 \x01(\tB&\xfaA#\n!googleads.googleapis.com/Customer\x12\x17\n\x0finvitation_link\x18\x03 \x01(\t"a\n\x16MutateCustomerResponse\x12G\n\x06result\x18\x02 \x01(\x0b27.google.ads.googleads.v21.services.MutateCustomerResult"\x95\x01\n\x14MutateCustomerResult\x12=\n\rresource_name\x18\x01 \x01(\tB&\xfaA#\n!googleads.googleapis.com/Customer\x12>\n\x08customer\x18\x02 \x01(\x0b2,.google.ads.googleads.v21.resources.Customer" \n\x1eListAccessibleCustomersRequest"9\n\x1fListAccessibleCustomersResponse\x12\x16\n\x0eresource_names\x18\x01 \x03(\t2\xf5\x05\n\x0fCustomerService\x12\xcf\x01\n\x0eMutateCustomer\x128.google.ads.googleads.v21.services.MutateCustomerRequest\x1a9.google.ads.googleads.v21.services.MutateCustomerResponse"H\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x02*"%/v21/customers/{customer_id=*}:mutate:\x01*\x12\xd0\x01\n\x17ListAccessibleCustomers\x12A.google.ads.googleads.v21.services.ListAccessibleCustomersRequest\x1aB.google.ads.googleads.v21.services.ListAccessibleCustomersResponse".\x82\xd3\xe4\x93\x02(\x12&/v21/customers:listAccessibleCustomers\x12\xf5\x01\n\x14CreateCustomerClient\x12>.google.ads.googleads.v21.services.CreateCustomerClientRequest\x1a?.google.ads.googleads.v21.services.CreateCustomerClientResponse"\\\xdaA\x1bcustomer_id,customer_client\x82\xd3\xe4\x93\x028"3/v21/customers/{customer_id=*}:createCustomerClient:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x80\x02\n%com.google.ads.googleads.v21.servicesB\x14CustomerServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.customer_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x14CustomerServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_MUTATECUSTOMERREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECUSTOMERREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMERREQUEST'].fields_by_name['operation']._loaded_options = None
    _globals['_MUTATECUSTOMERREQUEST'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECUSTOMERCLIENTREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_CREATECUSTOMERCLIENTREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECUSTOMERCLIENTREQUEST'].fields_by_name['customer_client']._loaded_options = None
    _globals['_CREATECUSTOMERCLIENTREQUEST'].fields_by_name['customer_client']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECUSTOMERCLIENTRESPONSE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CREATECUSTOMERCLIENTRESPONSE'].fields_by_name['resource_name']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_MUTATECUSTOMERRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMERRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_CUSTOMERSERVICE']._loaded_options = None
    _globals['_CUSTOMERSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMERSERVICE'].methods_by_name['MutateCustomer']._loaded_options = None
    _globals['_CUSTOMERSERVICE'].methods_by_name['MutateCustomer']._serialized_options = b'\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x02*"%/v21/customers/{customer_id=*}:mutate:\x01*'
    _globals['_CUSTOMERSERVICE'].methods_by_name['ListAccessibleCustomers']._loaded_options = None
    _globals['_CUSTOMERSERVICE'].methods_by_name['ListAccessibleCustomers']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/v21/customers:listAccessibleCustomers'
    _globals['_CUSTOMERSERVICE'].methods_by_name['CreateCustomerClient']._loaded_options = None
    _globals['_CUSTOMERSERVICE'].methods_by_name['CreateCustomerClient']._serialized_options = b'\xdaA\x1bcustomer_id,customer_client\x82\xd3\xe4\x93\x028"3/v21/customers/{customer_id=*}:createCustomerClient:\x01*'
    _globals['_MUTATECUSTOMERREQUEST']._serialized_start = 406
    _globals['_MUTATECUSTOMERREQUEST']._serialized_end = 664
    _globals['_CREATECUSTOMERCLIENTREQUEST']._serialized_start = 667
    _globals['_CREATECUSTOMERCLIENTREQUEST']._serialized_end = 947
    _globals['_CUSTOMEROPERATION']._serialized_start = 950
    _globals['_CUSTOMEROPERATION']._serialized_end = 1080
    _globals['_CREATECUSTOMERCLIENTRESPONSE']._serialized_start = 1082
    _globals['_CREATECUSTOMERCLIENTRESPONSE']._serialized_end = 1200
    _globals['_MUTATECUSTOMERRESPONSE']._serialized_start = 1202
    _globals['_MUTATECUSTOMERRESPONSE']._serialized_end = 1299
    _globals['_MUTATECUSTOMERRESULT']._serialized_start = 1302
    _globals['_MUTATECUSTOMERRESULT']._serialized_end = 1451
    _globals['_LISTACCESSIBLECUSTOMERSREQUEST']._serialized_start = 1453
    _globals['_LISTACCESSIBLECUSTOMERSREQUEST']._serialized_end = 1485
    _globals['_LISTACCESSIBLECUSTOMERSRESPONSE']._serialized_start = 1487
    _globals['_LISTACCESSIBLECUSTOMERSRESPONSE']._serialized_end = 1544
    _globals['_CUSTOMERSERVICE']._serialized_start = 1547
    _globals['_CUSTOMERSERVICE']._serialized_end = 2304