"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/customer_user_access_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.resources import customer_user_access_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_customer__user__access__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/ads/googleads/v19/services/customer_user_access_service.proto\x12!google.ads.googleads.v19.services\x1a=google/ads/googleads/v19/resources/customer_user_access.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\x93\x01\n\x1fMutateCustomerUserAccessRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12V\n\toperation\x18\x02 \x01(\x0b2>.google.ads.googleads.v19.services.CustomerUserAccessOperationB\x03\xe0A\x02"\xe9\x01\n\x1bCustomerUserAccessOperation\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12H\n\x06update\x18\x01 \x01(\x0b26.google.ads.googleads.v19.resources.CustomerUserAccessH\x00\x12B\n\x06remove\x18\x02 \x01(\tB0\xfaA-\n+googleads.googleapis.com/CustomerUserAccessH\x00B\x0b\n\toperation"u\n MutateCustomerUserAccessResponse\x12Q\n\x06result\x18\x01 \x01(\x0b2A.google.ads.googleads.v19.services.MutateCustomerUserAccessResult"i\n\x1eMutateCustomerUserAccessResult\x12G\n\rresource_name\x18\x01 \x01(\tB0\xfaA-\n+googleads.googleapis.com/CustomerUserAccess2\xe7\x02\n\x19CustomerUserAccessService\x12\x82\x02\n\x18MutateCustomerUserAccess\x12B.google.ads.googleads.v19.services.MutateCustomerUserAccessRequest\x1aC.google.ads.googleads.v19.services.MutateCustomerUserAccessResponse"]\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x02?":/v19/customers/{customer_id=*}/customerUserAccesses:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8a\x02\n%com.google.ads.googleads.v19.servicesB\x1eCustomerUserAccessServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.customer_user_access_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB\x1eCustomerUserAccessServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_MUTATECUSTOMERUSERACCESSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECUSTOMERUSERACCESSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMERUSERACCESSREQUEST'].fields_by_name['operation']._loaded_options = None
    _globals['_MUTATECUSTOMERUSERACCESSREQUEST'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMERUSERACCESSOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA-\n+googleads.googleapis.com/CustomerUserAccess'
    _globals['_MUTATECUSTOMERUSERACCESSRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMERUSERACCESSRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA-\n+googleads.googleapis.com/CustomerUserAccess'
    _globals['_CUSTOMERUSERACCESSSERVICE']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMERUSERACCESSSERVICE'].methods_by_name['MutateCustomerUserAccess']._loaded_options = None
    _globals['_CUSTOMERUSERACCESSSERVICE'].methods_by_name['MutateCustomerUserAccess']._serialized_options = b'\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x02?":/v19/customers/{customer_id=*}/customerUserAccesses:mutate:\x01*'
    _globals['_MUTATECUSTOMERUSERACCESSREQUEST']._serialized_start = 320
    _globals['_MUTATECUSTOMERUSERACCESSREQUEST']._serialized_end = 467
    _globals['_CUSTOMERUSERACCESSOPERATION']._serialized_start = 470
    _globals['_CUSTOMERUSERACCESSOPERATION']._serialized_end = 703
    _globals['_MUTATECUSTOMERUSERACCESSRESPONSE']._serialized_start = 705
    _globals['_MUTATECUSTOMERUSERACCESSRESPONSE']._serialized_end = 822
    _globals['_MUTATECUSTOMERUSERACCESSRESULT']._serialized_start = 824
    _globals['_MUTATECUSTOMERUSERACCESSRESULT']._serialized_end = 929
    _globals['_CUSTOMERUSERACCESSSERVICE']._serialized_start = 932
    _globals['_CUSTOMERUSERACCESSSERVICE']._serialized_end = 1291