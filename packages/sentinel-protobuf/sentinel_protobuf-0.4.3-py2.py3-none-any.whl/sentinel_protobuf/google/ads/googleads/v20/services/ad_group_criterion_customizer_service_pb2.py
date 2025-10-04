"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/ad_group_criterion_customizer_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v20.resources import ad_group_criterion_customizer_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_ad__group__criterion__customizer__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMgoogle/ads/googleads/v20/services/ad_group_criterion_customizer_service.proto\x12!google.ads.googleads.v20.services\x1a:google/ads/googleads/v20/enums/response_content_type.proto\x1aFgoogle/ads/googleads/v20/resources/ad_group_criterion_customizer.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xc1\x02\n(MutateAdGroupCriterionCustomizersRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12_\n\noperations\x18\x02 \x03(\x0b2F.google.ads.googleads.v20.services.AdGroupCriterionCustomizerOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v20.enums.ResponseContentTypeEnum.ResponseContentType"\xd0\x01\n#AdGroupCriterionCustomizerOperation\x12P\n\x06create\x18\x01 \x01(\x0b2>.google.ads.googleads.v20.resources.AdGroupCriterionCustomizerH\x00\x12J\n\x06remove\x18\x02 \x01(\tB8\xfaA5\n3googleads.googleapis.com/AdGroupCriterionCustomizerH\x00B\x0b\n\toperation"\xba\x01\n)MutateAdGroupCriterionCustomizersResponse\x12Z\n\x07results\x18\x01 \x03(\x0b2I.google.ads.googleads.v20.services.MutateAdGroupCriterionCustomizerResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"\xe0\x01\n&MutateAdGroupCriterionCustomizerResult\x12O\n\rresource_name\x18\x01 \x01(\tB8\xfaA5\n3googleads.googleapis.com/AdGroupCriterionCustomizer\x12e\n\x1dad_group_criterion_customizer\x18\x02 \x01(\x0b2>.google.ads.googleads.v20.resources.AdGroupCriterionCustomizer2\x92\x03\n!AdGroupCriterionCustomizerService\x12\xa5\x02\n!MutateAdGroupCriterionCustomizers\x12K.google.ads.googleads.v20.services.MutateAdGroupCriterionCustomizersRequest\x1aL.google.ads.googleads.v20.services.MutateAdGroupCriterionCustomizersResponse"e\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02F"A/v20/customers/{customer_id=*}/AdGroupCriterionCustomizers:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x92\x02\n%com.google.ads.googleads.v20.servicesB&AdGroupCriterionCustomizerServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.ad_group_criterion_customizer_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB&AdGroupCriterionCustomizerServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATEADGROUPCRITERIONCUSTOMIZERSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEADGROUPCRITERIONCUSTOMIZERSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEADGROUPCRITERIONCUSTOMIZERSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEADGROUPCRITERIONCUSTOMIZERSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_ADGROUPCRITERIONCUSTOMIZEROPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_ADGROUPCRITERIONCUSTOMIZEROPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA5\n3googleads.googleapis.com/AdGroupCriterionCustomizer'
    _globals['_MUTATEADGROUPCRITERIONCUSTOMIZERRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEADGROUPCRITERIONCUSTOMIZERRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA5\n3googleads.googleapis.com/AdGroupCriterionCustomizer'
    _globals['_ADGROUPCRITERIONCUSTOMIZERSERVICE']._loaded_options = None
    _globals['_ADGROUPCRITERIONCUSTOMIZERSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_ADGROUPCRITERIONCUSTOMIZERSERVICE'].methods_by_name['MutateAdGroupCriterionCustomizers']._loaded_options = None
    _globals['_ADGROUPCRITERIONCUSTOMIZERSERVICE'].methods_by_name['MutateAdGroupCriterionCustomizers']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02F"A/v20/customers/{customer_id=*}/AdGroupCriterionCustomizers:mutate:\x01*'
    _globals['_MUTATEADGROUPCRITERIONCUSTOMIZERSREQUEST']._serialized_start = 389
    _globals['_MUTATEADGROUPCRITERIONCUSTOMIZERSREQUEST']._serialized_end = 710
    _globals['_ADGROUPCRITERIONCUSTOMIZEROPERATION']._serialized_start = 713
    _globals['_ADGROUPCRITERIONCUSTOMIZEROPERATION']._serialized_end = 921
    _globals['_MUTATEADGROUPCRITERIONCUSTOMIZERSRESPONSE']._serialized_start = 924
    _globals['_MUTATEADGROUPCRITERIONCUSTOMIZERSRESPONSE']._serialized_end = 1110
    _globals['_MUTATEADGROUPCRITERIONCUSTOMIZERRESULT']._serialized_start = 1113
    _globals['_MUTATEADGROUPCRITERIONCUSTOMIZERRESULT']._serialized_end = 1337
    _globals['_ADGROUPCRITERIONCUSTOMIZERSERVICE']._serialized_start = 1340
    _globals['_ADGROUPCRITERIONCUSTOMIZERSERVICE']._serialized_end = 1742