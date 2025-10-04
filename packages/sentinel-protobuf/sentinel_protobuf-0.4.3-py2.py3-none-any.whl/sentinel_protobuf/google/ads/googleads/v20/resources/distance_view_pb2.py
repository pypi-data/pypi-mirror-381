"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/distance_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import distance_bucket_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_distance__bucket__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/googleads/v20/resources/distance_view.proto\x12"google.ads.googleads.v20.resources\x1a4google/ads/googleads/v20/enums/distance_bucket.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe4\x02\n\x0cDistanceView\x12D\n\rresource_name\x18\x01 \x01(\tB-\xe0A\x03\xfaA\'\n%googleads.googleapis.com/DistanceView\x12_\n\x0fdistance_bucket\x18\x02 \x01(\x0e2A.google.ads.googleads.v20.enums.DistanceBucketEnum.DistanceBucketB\x03\xe0A\x03\x12\x1f\n\rmetric_system\x18\x04 \x01(\x08B\x03\xe0A\x03H\x00\x88\x01\x01:z\xeaAw\n%googleads.googleapis.com/DistanceView\x12Ncustomers/{customer_id}/distanceViews/{placeholder_chain_id}~{distance_bucket}B\x10\n\x0e_metric_systemB\x83\x02\n&com.google.ads.googleads.v20.resourcesB\x11DistanceViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.distance_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x11DistanceViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_DISTANCEVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_DISTANCEVIEW'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x03\xfaA'\n%googleads.googleapis.com/DistanceView"
    _globals['_DISTANCEVIEW'].fields_by_name['distance_bucket']._loaded_options = None
    _globals['_DISTANCEVIEW'].fields_by_name['distance_bucket']._serialized_options = b'\xe0A\x03'
    _globals['_DISTANCEVIEW'].fields_by_name['metric_system']._loaded_options = None
    _globals['_DISTANCEVIEW'].fields_by_name['metric_system']._serialized_options = b'\xe0A\x03'
    _globals['_DISTANCEVIEW']._loaded_options = None
    _globals['_DISTANCEVIEW']._serialized_options = b'\xeaAw\n%googleads.googleapis.com/DistanceView\x12Ncustomers/{customer_id}/distanceViews/{placeholder_chain_id}~{distance_bucket}'
    _globals['_DISTANCEVIEW']._serialized_start = 209
    _globals['_DISTANCEVIEW']._serialized_end = 565