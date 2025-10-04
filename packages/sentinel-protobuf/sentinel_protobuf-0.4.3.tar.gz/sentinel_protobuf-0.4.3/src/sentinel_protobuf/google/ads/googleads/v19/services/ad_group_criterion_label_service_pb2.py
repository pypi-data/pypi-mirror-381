"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/ad_group_criterion_label_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.resources import ad_group_criterion_label_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_ad__group__criterion__label__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/ads/googleads/v19/services/ad_group_criterion_label_service.proto\x12!google.ads.googleads.v19.services\x1aAgoogle/ads/googleads/v19/resources/ad_group_criterion_label.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xcb\x01\n#MutateAdGroupCriterionLabelsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12Z\n\noperations\x18\x02 \x03(\x0b2A.google.ads.googleads.v19.services.AdGroupCriterionLabelOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xc1\x01\n\x1eAdGroupCriterionLabelOperation\x12K\n\x06create\x18\x01 \x01(\x0b29.google.ads.googleads.v19.resources.AdGroupCriterionLabelH\x00\x12E\n\x06remove\x18\x02 \x01(\tB3\xfaA0\n.googleads.googleapis.com/AdGroupCriterionLabelH\x00B\x0b\n\toperation"\xb0\x01\n$MutateAdGroupCriterionLabelsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12U\n\x07results\x18\x02 \x03(\x0b2D.google.ads.googleads.v19.services.MutateAdGroupCriterionLabelResult"o\n!MutateAdGroupCriterionLabelResult\x12J\n\rresource_name\x18\x01 \x01(\tB3\xfaA0\n.googleads.googleapis.com/AdGroupCriterionLabel2\xf9\x02\n\x1cAdGroupCriterionLabelService\x12\x91\x02\n\x1cMutateAdGroupCriterionLabels\x12F.google.ads.googleads.v19.services.MutateAdGroupCriterionLabelsRequest\x1aG.google.ads.googleads.v19.services.MutateAdGroupCriterionLabelsResponse"`\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02A"</v19/customers/{customer_id=*}/adGroupCriterionLabels:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8d\x02\n%com.google.ads.googleads.v19.servicesB!AdGroupCriterionLabelServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.ad_group_criterion_label_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB!AdGroupCriterionLabelServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_MUTATEADGROUPCRITERIONLABELSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEADGROUPCRITERIONLABELSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEADGROUPCRITERIONLABELSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEADGROUPCRITERIONLABELSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_ADGROUPCRITERIONLABELOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_ADGROUPCRITERIONLABELOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA0\n.googleads.googleapis.com/AdGroupCriterionLabel'
    _globals['_MUTATEADGROUPCRITERIONLABELRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEADGROUPCRITERIONLABELRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA0\n.googleads.googleapis.com/AdGroupCriterionLabel'
    _globals['_ADGROUPCRITERIONLABELSERVICE']._loaded_options = None
    _globals['_ADGROUPCRITERIONLABELSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_ADGROUPCRITERIONLABELSERVICE'].methods_by_name['MutateAdGroupCriterionLabels']._loaded_options = None
    _globals['_ADGROUPCRITERIONLABELSERVICE'].methods_by_name['MutateAdGroupCriterionLabels']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02A"</v19/customers/{customer_id=*}/adGroupCriterionLabels:mutate:\x01*'
    _globals['_MUTATEADGROUPCRITERIONLABELSREQUEST']._serialized_start = 319
    _globals['_MUTATEADGROUPCRITERIONLABELSREQUEST']._serialized_end = 522
    _globals['_ADGROUPCRITERIONLABELOPERATION']._serialized_start = 525
    _globals['_ADGROUPCRITERIONLABELOPERATION']._serialized_end = 718
    _globals['_MUTATEADGROUPCRITERIONLABELSRESPONSE']._serialized_start = 721
    _globals['_MUTATEADGROUPCRITERIONLABELSRESPONSE']._serialized_end = 897
    _globals['_MUTATEADGROUPCRITERIONLABELRESULT']._serialized_start = 899
    _globals['_MUTATEADGROUPCRITERIONLABELRESULT']._serialized_end = 1010
    _globals['_ADGROUPCRITERIONLABELSERVICE']._serialized_start = 1013
    _globals['_ADGROUPCRITERIONLABELSERVICE']._serialized_end = 1390