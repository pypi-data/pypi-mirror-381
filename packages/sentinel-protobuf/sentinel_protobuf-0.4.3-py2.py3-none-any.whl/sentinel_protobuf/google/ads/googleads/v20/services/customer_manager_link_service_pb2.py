"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/customer_manager_link_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.resources import customer_manager_link_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_customer__manager__link__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/ads/googleads/v20/services/customer_manager_link_service.proto\x12!google.ads.googleads.v20.services\x1a>google/ads/googleads/v20/resources/customer_manager_link.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xad\x01\n MutateCustomerManagerLinkRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12X\n\noperations\x18\x02 \x03(\x0b2?.google.ads.googleads.v20.services.CustomerManagerLinkOperationB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"\x90\x01\n\x16MoveManagerLinkRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12+\n\x1eprevious_customer_manager_link\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bnew_manager\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xa7\x01\n\x1cCustomerManagerLinkOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12I\n\x06update\x18\x02 \x01(\x0b27.google.ads.googleads.v20.resources.CustomerManagerLinkH\x00B\x0b\n\toperation"x\n!MutateCustomerManagerLinkResponse\x12S\n\x07results\x18\x01 \x03(\x0b2B.google.ads.googleads.v20.services.MutateCustomerManagerLinkResult"c\n\x17MoveManagerLinkResponse\x12H\n\rresource_name\x18\x01 \x01(\tB1\xfaA.\n,googleads.googleapis.com/CustomerManagerLink"k\n\x1fMutateCustomerManagerLinkResult\x12H\n\rresource_name\x18\x01 \x01(\tB1\xfaA.\n,googleads.googleapis.com/CustomerManagerLink2\x81\x05\n\x1aCustomerManagerLinkService\x12\x86\x02\n\x19MutateCustomerManagerLink\x12C.google.ads.googleads.v20.services.MutateCustomerManagerLinkRequest\x1aD.google.ads.googleads.v20.services.MutateCustomerManagerLinkResponse"^\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02?":/v20/customers/{customer_id=*}/customerManagerLinks:mutate:\x01*\x12\x92\x02\n\x0fMoveManagerLink\x129.google.ads.googleads.v20.services.MoveManagerLinkRequest\x1a:.google.ads.googleads.v20.services.MoveManagerLinkResponse"\x87\x01\xdaA6customer_id,previous_customer_manager_link,new_manager\x82\xd3\xe4\x93\x02H"C/v20/customers/{customer_id=*}/customerManagerLinks:moveManagerLink:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8b\x02\n%com.google.ads.googleads.v20.servicesB\x1fCustomerManagerLinkServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.customer_manager_link_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x1fCustomerManagerLinkServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATECUSTOMERMANAGERLINKREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECUSTOMERMANAGERLINKREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMERMANAGERLINKREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECUSTOMERMANAGERLINKREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_MOVEMANAGERLINKREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MOVEMANAGERLINKREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MOVEMANAGERLINKREQUEST'].fields_by_name['previous_customer_manager_link']._loaded_options = None
    _globals['_MOVEMANAGERLINKREQUEST'].fields_by_name['previous_customer_manager_link']._serialized_options = b'\xe0A\x02'
    _globals['_MOVEMANAGERLINKREQUEST'].fields_by_name['new_manager']._loaded_options = None
    _globals['_MOVEMANAGERLINKREQUEST'].fields_by_name['new_manager']._serialized_options = b'\xe0A\x02'
    _globals['_MOVEMANAGERLINKRESPONSE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MOVEMANAGERLINKRESPONSE'].fields_by_name['resource_name']._serialized_options = b'\xfaA.\n,googleads.googleapis.com/CustomerManagerLink'
    _globals['_MUTATECUSTOMERMANAGERLINKRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMERMANAGERLINKRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA.\n,googleads.googleapis.com/CustomerManagerLink'
    _globals['_CUSTOMERMANAGERLINKSERVICE']._loaded_options = None
    _globals['_CUSTOMERMANAGERLINKSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMERMANAGERLINKSERVICE'].methods_by_name['MutateCustomerManagerLink']._loaded_options = None
    _globals['_CUSTOMERMANAGERLINKSERVICE'].methods_by_name['MutateCustomerManagerLink']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02?":/v20/customers/{customer_id=*}/customerManagerLinks:mutate:\x01*'
    _globals['_CUSTOMERMANAGERLINKSERVICE'].methods_by_name['MoveManagerLink']._loaded_options = None
    _globals['_CUSTOMERMANAGERLINKSERVICE'].methods_by_name['MoveManagerLink']._serialized_options = b'\xdaA6customer_id,previous_customer_manager_link,new_manager\x82\xd3\xe4\x93\x02H"C/v20/customers/{customer_id=*}/customerManagerLinks:moveManagerLink:\x01*'
    _globals['_MUTATECUSTOMERMANAGERLINKREQUEST']._serialized_start = 322
    _globals['_MUTATECUSTOMERMANAGERLINKREQUEST']._serialized_end = 495
    _globals['_MOVEMANAGERLINKREQUEST']._serialized_start = 498
    _globals['_MOVEMANAGERLINKREQUEST']._serialized_end = 642
    _globals['_CUSTOMERMANAGERLINKOPERATION']._serialized_start = 645
    _globals['_CUSTOMERMANAGERLINKOPERATION']._serialized_end = 812
    _globals['_MUTATECUSTOMERMANAGERLINKRESPONSE']._serialized_start = 814
    _globals['_MUTATECUSTOMERMANAGERLINKRESPONSE']._serialized_end = 934
    _globals['_MOVEMANAGERLINKRESPONSE']._serialized_start = 936
    _globals['_MOVEMANAGERLINKRESPONSE']._serialized_end = 1035
    _globals['_MUTATECUSTOMERMANAGERLINKRESULT']._serialized_start = 1037
    _globals['_MUTATECUSTOMERMANAGERLINKRESULT']._serialized_end = 1144
    _globals['_CUSTOMERMANAGERLINKSERVICE']._serialized_start = 1147
    _globals['_CUSTOMERMANAGERLINKSERVICE']._serialized_end = 1788