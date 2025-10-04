"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/custom_interest_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.resources import custom_interest_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_custom__interest__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/googleads/v20/services/custom_interest_service.proto\x12!google.ads.googleads.v20.services\x1a8google/ads/googleads/v20/resources/custom_interest.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xa4\x01\n\x1cMutateCustomInterestsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12S\n\noperations\x18\x02 \x03(\x0b2:.google.ads.googleads.v20.services.CustomInterestOperationB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xe3\x01\n\x17CustomInterestOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12D\n\x06create\x18\x01 \x01(\x0b22.google.ads.googleads.v20.resources.CustomInterestH\x00\x12D\n\x06update\x18\x02 \x01(\x0b22.google.ads.googleads.v20.resources.CustomInterestH\x00B\x0b\n\toperation"o\n\x1dMutateCustomInterestsResponse\x12N\n\x07results\x18\x02 \x03(\x0b2=.google.ads.googleads.v20.services.MutateCustomInterestResult"a\n\x1aMutateCustomInterestResult\x12C\n\rresource_name\x18\x01 \x01(\tB,\xfaA)\n\'googleads.googleapis.com/CustomInterest2\xd6\x02\n\x15CustomInterestService\x12\xf5\x01\n\x15MutateCustomInterests\x12?.google.ads.googleads.v20.services.MutateCustomInterestsRequest\x1a@.google.ads.googleads.v20.services.MutateCustomInterestsResponse"Y\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02:"5/v20/customers/{customer_id=*}/customInterests:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x86\x02\n%com.google.ads.googleads.v20.servicesB\x1aCustomInterestServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.custom_interest_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x1aCustomInterestServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATECUSTOMINTERESTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECUSTOMINTERESTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMINTERESTSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECUSTOMINTERESTSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMINTERESTRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMINTERESTRESULT'].fields_by_name['resource_name']._serialized_options = b"\xfaA)\n'googleads.googleapis.com/CustomInterest"
    _globals['_CUSTOMINTERESTSERVICE']._loaded_options = None
    _globals['_CUSTOMINTERESTSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMINTERESTSERVICE'].methods_by_name['MutateCustomInterests']._loaded_options = None
    _globals['_CUSTOMINTERESTSERVICE'].methods_by_name['MutateCustomInterests']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02:"5/v20/customers/{customer_id=*}/customInterests:mutate:\x01*'
    _globals['_MUTATECUSTOMINTERESTSREQUEST']._serialized_start = 310
    _globals['_MUTATECUSTOMINTERESTSREQUEST']._serialized_end = 474
    _globals['_CUSTOMINTERESTOPERATION']._serialized_start = 477
    _globals['_CUSTOMINTERESTOPERATION']._serialized_end = 704
    _globals['_MUTATECUSTOMINTERESTSRESPONSE']._serialized_start = 706
    _globals['_MUTATECUSTOMINTERESTSRESPONSE']._serialized_end = 817
    _globals['_MUTATECUSTOMINTERESTRESULT']._serialized_start = 819
    _globals['_MUTATECUSTOMINTERESTRESULT']._serialized_end = 916
    _globals['_CUSTOMINTERESTSERVICE']._serialized_start = 919
    _globals['_CUSTOMINTERESTSERVICE']._serialized_end = 1261