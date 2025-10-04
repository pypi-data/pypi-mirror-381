"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/customer_client_link_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.resources import customer_client_link_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_customer__client__link__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/ads/googleads/v20/services/customer_client_link_service.proto\x12!google.ads.googleads.v20.services\x1a=google/ads/googleads/v20/resources/customer_client_link.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xaa\x01\n\x1fMutateCustomerClientLinkRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12V\n\toperation\x18\x02 \x01(\x0b2>.google.ads.googleads.v20.services.CustomerClientLinkOperationB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"\xef\x01\n\x1bCustomerClientLinkOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12H\n\x06create\x18\x01 \x01(\x0b26.google.ads.googleads.v20.resources.CustomerClientLinkH\x00\x12H\n\x06update\x18\x02 \x01(\x0b26.google.ads.googleads.v20.resources.CustomerClientLinkH\x00B\x0b\n\toperation"u\n MutateCustomerClientLinkResponse\x12Q\n\x06result\x18\x01 \x01(\x0b2A.google.ads.googleads.v20.services.MutateCustomerClientLinkResult"i\n\x1eMutateCustomerClientLinkResult\x12G\n\rresource_name\x18\x01 \x01(\tB0\xfaA-\n+googleads.googleapis.com/CustomerClientLink2\xe6\x02\n\x19CustomerClientLinkService\x12\x81\x02\n\x18MutateCustomerClientLink\x12B.google.ads.googleads.v20.services.MutateCustomerClientLinkRequest\x1aC.google.ads.googleads.v20.services.MutateCustomerClientLinkResponse"\\\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x02>"9/v20/customers/{customer_id=*}/customerClientLinks:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8a\x02\n%com.google.ads.googleads.v20.servicesB\x1eCustomerClientLinkServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.customer_client_link_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x1eCustomerClientLinkServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATECUSTOMERCLIENTLINKREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECUSTOMERCLIENTLINKREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMERCLIENTLINKREQUEST'].fields_by_name['operation']._loaded_options = None
    _globals['_MUTATECUSTOMERCLIENTLINKREQUEST'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMERCLIENTLINKRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMERCLIENTLINKRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA-\n+googleads.googleapis.com/CustomerClientLink'
    _globals['_CUSTOMERCLIENTLINKSERVICE']._loaded_options = None
    _globals['_CUSTOMERCLIENTLINKSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMERCLIENTLINKSERVICE'].methods_by_name['MutateCustomerClientLink']._loaded_options = None
    _globals['_CUSTOMERCLIENTLINKSERVICE'].methods_by_name['MutateCustomerClientLink']._serialized_options = b'\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x02>"9/v20/customers/{customer_id=*}/customerClientLinks:mutate:\x01*'
    _globals['_MUTATECUSTOMERCLIENTLINKREQUEST']._serialized_start = 320
    _globals['_MUTATECUSTOMERCLIENTLINKREQUEST']._serialized_end = 490
    _globals['_CUSTOMERCLIENTLINKOPERATION']._serialized_start = 493
    _globals['_CUSTOMERCLIENTLINKOPERATION']._serialized_end = 732
    _globals['_MUTATECUSTOMERCLIENTLINKRESPONSE']._serialized_start = 734
    _globals['_MUTATECUSTOMERCLIENTLINKRESPONSE']._serialized_end = 851
    _globals['_MUTATECUSTOMERCLIENTLINKRESULT']._serialized_start = 853
    _globals['_MUTATECUSTOMERCLIENTLINKRESULT']._serialized_end = 958
    _globals['_CUSTOMERCLIENTLINKSERVICE']._serialized_start = 961
    _globals['_CUSTOMERCLIENTLINKSERVICE']._serialized_end = 1319