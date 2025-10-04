"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/ad_group_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v19.resources import ad_group_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_ad__group__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v19/services/ad_group_service.proto\x12!google.ads.googleads.v19.services\x1a:google/ads/googleads/v19/enums/response_content_type.proto\x1a1google/ads/googleads/v19/resources/ad_group.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\x9b\x02\n\x15MutateAdGroupsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12L\n\noperations\x18\x02 \x03(\x0b23.google.ads.googleads.v19.services.AdGroupOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v19.enums.ResponseContentTypeEnum.ResponseContentType"\x87\x02\n\x10AdGroupOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12=\n\x06create\x18\x01 \x01(\x0b2+.google.ads.googleads.v19.resources.AdGroupH\x00\x12=\n\x06update\x18\x02 \x01(\x0b2+.google.ads.googleads.v19.resources.AdGroupH\x00\x127\n\x06remove\x18\x03 \x01(\tB%\xfaA"\n googleads.googleapis.com/AdGroupH\x00B\x0b\n\toperation"\x94\x01\n\x16MutateAdGroupsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12G\n\x07results\x18\x02 \x03(\x0b26.google.ads.googleads.v19.services.MutateAdGroupResult"\x92\x01\n\x13MutateAdGroupResult\x12<\n\rresource_name\x18\x01 \x01(\tB%\xfaA"\n googleads.googleapis.com/AdGroup\x12=\n\x08ad_group\x18\x02 \x01(\x0b2+.google.ads.googleads.v19.resources.AdGroup2\xb3\x02\n\x0eAdGroupService\x12\xd9\x01\n\x0eMutateAdGroups\x128.google.ads.googleads.v19.services.MutateAdGroupsRequest\x1a9.google.ads.googleads.v19.services.MutateAdGroupsResponse"R\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x023"./v19/customers/{customer_id=*}/adGroups:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\xff\x01\n%com.google.ads.googleads.v19.servicesB\x13AdGroupServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.ad_group_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB\x13AdGroupServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_MUTATEADGROUPSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEADGROUPSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEADGROUPSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEADGROUPSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_ADGROUPOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_ADGROUPOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_MUTATEADGROUPRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEADGROUPRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_ADGROUPSERVICE']._loaded_options = None
    _globals['_ADGROUPSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_ADGROUPSERVICE'].methods_by_name['MutateAdGroups']._loaded_options = None
    _globals['_ADGROUPSERVICE'].methods_by_name['MutateAdGroups']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x023"./v19/customers/{customer_id=*}/adGroups:mutate:\x01*'
    _globals['_MUTATEADGROUPSREQUEST']._serialized_start = 381
    _globals['_MUTATEADGROUPSREQUEST']._serialized_end = 664
    _globals['_ADGROUPOPERATION']._serialized_start = 667
    _globals['_ADGROUPOPERATION']._serialized_end = 930
    _globals['_MUTATEADGROUPSRESPONSE']._serialized_start = 933
    _globals['_MUTATEADGROUPSRESPONSE']._serialized_end = 1081
    _globals['_MUTATEADGROUPRESULT']._serialized_start = 1084
    _globals['_MUTATEADGROUPRESULT']._serialized_end = 1230
    _globals['_ADGROUPSERVICE']._serialized_start = 1233
    _globals['_ADGROUPSERVICE']._serialized_end = 1540