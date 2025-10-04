"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/recommendation_subscription.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import recommendation_subscription_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_recommendation__subscription__status__pb2
from ......google.ads.googleads.v19.enums import recommendation_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_recommendation__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/ads/googleads/v19/resources/recommendation_subscription.proto\x12"google.ads.googleads.v19.resources\x1aGgoogle/ads/googleads/v19/enums/recommendation_subscription_status.proto\x1a8google/ads/googleads/v19/enums/recommendation_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd6\x04\n\x1aRecommendationSubscription\x12R\n\rresource_name\x18\x01 \x01(\tB;\xe0A\x05\xfaA5\n3googleads.googleapis.com/RecommendationSubscription\x12_\n\x04type\x18\x02 \x01(\x0e2I.google.ads.googleads.v19.enums.RecommendationTypeEnum.RecommendationTypeB\x06\xe0A\x02\xe0A\x05\x12"\n\x10create_date_time\x18\x03 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12"\n\x10modify_date_time\x18\x04 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x7f\n\x06status\x18\x05 \x01(\x0e2e.google.ads.googleads.v19.enums.RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatusB\x03\xe0A\x02H\x02\x88\x01\x01:\x84\x01\xeaA\x80\x01\n3googleads.googleapis.com/RecommendationSubscription\x12Icustomers/{customer_id}/recommendationSubscriptions/{recommendation_type}B\x13\n\x11_create_date_timeB\x13\n\x11_modify_date_timeB\t\n\x07_statusB\x91\x02\n&com.google.ads.googleads.v19.resourcesB\x1fRecommendationSubscriptionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.recommendation_subscription_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x1fRecommendationSubscriptionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_RECOMMENDATIONSUBSCRIPTION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_RECOMMENDATIONSUBSCRIPTION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA5\n3googleads.googleapis.com/RecommendationSubscription'
    _globals['_RECOMMENDATIONSUBSCRIPTION'].fields_by_name['type']._loaded_options = None
    _globals['_RECOMMENDATIONSUBSCRIPTION'].fields_by_name['type']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_RECOMMENDATIONSUBSCRIPTION'].fields_by_name['create_date_time']._loaded_options = None
    _globals['_RECOMMENDATIONSUBSCRIPTION'].fields_by_name['create_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_RECOMMENDATIONSUBSCRIPTION'].fields_by_name['modify_date_time']._loaded_options = None
    _globals['_RECOMMENDATIONSUBSCRIPTION'].fields_by_name['modify_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_RECOMMENDATIONSUBSCRIPTION'].fields_by_name['status']._loaded_options = None
    _globals['_RECOMMENDATIONSUBSCRIPTION'].fields_by_name['status']._serialized_options = b'\xe0A\x02'
    _globals['_RECOMMENDATIONSUBSCRIPTION']._loaded_options = None
    _globals['_RECOMMENDATIONSUBSCRIPTION']._serialized_options = b'\xeaA\x80\x01\n3googleads.googleapis.com/RecommendationSubscription\x12Icustomers/{customer_id}/recommendationSubscriptions/{recommendation_type}'
    _globals['_RECOMMENDATIONSUBSCRIPTION']._serialized_start = 300
    _globals['_RECOMMENDATIONSUBSCRIPTION']._serialized_end = 898