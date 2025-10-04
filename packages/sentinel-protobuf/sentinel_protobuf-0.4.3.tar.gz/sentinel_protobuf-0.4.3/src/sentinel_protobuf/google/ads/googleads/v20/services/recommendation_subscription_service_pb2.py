"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/recommendation_subscription_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v20.resources import recommendation_subscription_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_recommendation__subscription__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKgoogle/ads/googleads/v20/services/recommendation_subscription_service.proto\x12!google.ads.googleads.v20.services\x1a:google/ads/googleads/v20/enums/response_content_type.proto\x1aDgoogle/ads/googleads/v20/resources/recommendation_subscription.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xc0\x02\n\'MutateRecommendationSubscriptionRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12_\n\noperations\x18\x02 \x03(\x0b2F.google.ads.googleads.v20.services.RecommendationSubscriptionOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v20.enums.ResponseContentTypeEnum.ResponseContentType"\x8c\x02\n#RecommendationSubscriptionOperation\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12P\n\x06create\x18\x01 \x01(\x0b2>.google.ads.googleads.v20.resources.RecommendationSubscriptionH\x00\x12P\n\x06update\x18\x02 \x01(\x0b2>.google.ads.googleads.v20.resources.RecommendationSubscriptionH\x00B\x0b\n\toperation"\xb9\x01\n(MutateRecommendationSubscriptionResponse\x12Z\n\x07results\x18\x01 \x03(\x0b2I.google.ads.googleads.v20.services.MutateRecommendationSubscriptionResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"\xde\x01\n&MutateRecommendationSubscriptionResult\x12O\n\rresource_name\x18\x01 \x01(\tB8\xfaA5\n3googleads.googleapis.com/RecommendationSubscription\x12c\n\x1brecommendation_subscription\x18\x02 \x01(\x0b2>.google.ads.googleads.v20.resources.RecommendationSubscription2\xa9\x03\n!RecommendationSubscriptionService\x12\xbc\x02\n MutateRecommendationSubscription\x12J.google.ads.googleads.v20.services.MutateRecommendationSubscriptionRequest\x1aK.google.ads.googleads.v20.services.MutateRecommendationSubscriptionResponse"\x7f\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02`"[/v20/customers/{customer_id=*}/recommendationSubscriptions:mutateRecommendationSubscription:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x92\x02\n%com.google.ads.googleads.v20.servicesB&RecommendationSubscriptionServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.recommendation_subscription_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB&RecommendationSubscriptionServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATERECOMMENDATIONSUBSCRIPTIONREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATERECOMMENDATIONSUBSCRIPTIONREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATERECOMMENDATIONSUBSCRIPTIONREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATERECOMMENDATIONSUBSCRIPTIONREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_RECOMMENDATIONSUBSCRIPTIONOPERATION'].fields_by_name['update_mask']._loaded_options = None
    _globals['_RECOMMENDATIONSUBSCRIPTIONOPERATION'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_MUTATERECOMMENDATIONSUBSCRIPTIONRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATERECOMMENDATIONSUBSCRIPTIONRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA5\n3googleads.googleapis.com/RecommendationSubscription'
    _globals['_RECOMMENDATIONSUBSCRIPTIONSERVICE']._loaded_options = None
    _globals['_RECOMMENDATIONSUBSCRIPTIONSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_RECOMMENDATIONSUBSCRIPTIONSERVICE'].methods_by_name['MutateRecommendationSubscription']._loaded_options = None
    _globals['_RECOMMENDATIONSUBSCRIPTIONSERVICE'].methods_by_name['MutateRecommendationSubscription']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02`"[/v20/customers/{customer_id=*}/recommendationSubscriptions:mutateRecommendationSubscription:\x01*'
    _globals['_MUTATERECOMMENDATIONSUBSCRIPTIONREQUEST']._serialized_start = 419
    _globals['_MUTATERECOMMENDATIONSUBSCRIPTIONREQUEST']._serialized_end = 739
    _globals['_RECOMMENDATIONSUBSCRIPTIONOPERATION']._serialized_start = 742
    _globals['_RECOMMENDATIONSUBSCRIPTIONOPERATION']._serialized_end = 1010
    _globals['_MUTATERECOMMENDATIONSUBSCRIPTIONRESPONSE']._serialized_start = 1013
    _globals['_MUTATERECOMMENDATIONSUBSCRIPTIONRESPONSE']._serialized_end = 1198
    _globals['_MUTATERECOMMENDATIONSUBSCRIPTIONRESULT']._serialized_start = 1201
    _globals['_MUTATERECOMMENDATIONSUBSCRIPTIONRESULT']._serialized_end = 1423
    _globals['_RECOMMENDATIONSUBSCRIPTIONSERVICE']._serialized_start = 1426
    _globals['_RECOMMENDATIONSUBSCRIPTIONSERVICE']._serialized_end = 1851