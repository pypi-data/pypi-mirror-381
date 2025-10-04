"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/ad_group_ad_label_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.resources import ad_group_ad_label_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_ad__group__ad__label__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/googleads/v19/services/ad_group_ad_label_service.proto\x12!google.ads.googleads.v19.services\x1a:google/ads/googleads/v19/resources/ad_group_ad_label.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xbd\x01\n\x1cMutateAdGroupAdLabelsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12S\n\noperations\x18\x02 \x03(\x0b2:.google.ads.googleads.v19.services.AdGroupAdLabelOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xac\x01\n\x17AdGroupAdLabelOperation\x12D\n\x06create\x18\x01 \x01(\x0b22.google.ads.googleads.v19.resources.AdGroupAdLabelH\x00\x12>\n\x06remove\x18\x02 \x01(\tB,\xfaA)\n\'googleads.googleapis.com/AdGroupAdLabelH\x00B\x0b\n\toperation"\xa2\x01\n\x1dMutateAdGroupAdLabelsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12N\n\x07results\x18\x02 \x03(\x0b2=.google.ads.googleads.v19.services.MutateAdGroupAdLabelResult"a\n\x1aMutateAdGroupAdLabelResult\x12C\n\rresource_name\x18\x01 \x01(\tB,\xfaA)\n\'googleads.googleapis.com/AdGroupAdLabel2\xd6\x02\n\x15AdGroupAdLabelService\x12\xf5\x01\n\x15MutateAdGroupAdLabels\x12?.google.ads.googleads.v19.services.MutateAdGroupAdLabelsRequest\x1a@.google.ads.googleads.v19.services.MutateAdGroupAdLabelsResponse"Y\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02:"5/v19/customers/{customer_id=*}/adGroupAdLabels:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x86\x02\n%com.google.ads.googleads.v19.servicesB\x1aAdGroupAdLabelServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.ad_group_ad_label_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB\x1aAdGroupAdLabelServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_MUTATEADGROUPADLABELSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEADGROUPADLABELSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEADGROUPADLABELSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEADGROUPADLABELSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_ADGROUPADLABELOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_ADGROUPADLABELOPERATION'].fields_by_name['remove']._serialized_options = b"\xfaA)\n'googleads.googleapis.com/AdGroupAdLabel"
    _globals['_MUTATEADGROUPADLABELRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEADGROUPADLABELRESULT'].fields_by_name['resource_name']._serialized_options = b"\xfaA)\n'googleads.googleapis.com/AdGroupAdLabel"
    _globals['_ADGROUPADLABELSERVICE']._loaded_options = None
    _globals['_ADGROUPADLABELSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_ADGROUPADLABELSERVICE'].methods_by_name['MutateAdGroupAdLabels']._loaded_options = None
    _globals['_ADGROUPADLABELSERVICE'].methods_by_name['MutateAdGroupAdLabels']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02:"5/v19/customers/{customer_id=*}/adGroupAdLabels:mutate:\x01*'
    _globals['_MUTATEADGROUPADLABELSREQUEST']._serialized_start = 305
    _globals['_MUTATEADGROUPADLABELSREQUEST']._serialized_end = 494
    _globals['_ADGROUPADLABELOPERATION']._serialized_start = 497
    _globals['_ADGROUPADLABELOPERATION']._serialized_end = 669
    _globals['_MUTATEADGROUPADLABELSRESPONSE']._serialized_start = 672
    _globals['_MUTATEADGROUPADLABELSRESPONSE']._serialized_end = 834
    _globals['_MUTATEADGROUPADLABELRESULT']._serialized_start = 836
    _globals['_MUTATEADGROUPADLABELRESULT']._serialized_end = 933
    _globals['_ADGROUPADLABELSERVICE']._serialized_start = 936
    _globals['_ADGROUPADLABELSERVICE']._serialized_end = 1278