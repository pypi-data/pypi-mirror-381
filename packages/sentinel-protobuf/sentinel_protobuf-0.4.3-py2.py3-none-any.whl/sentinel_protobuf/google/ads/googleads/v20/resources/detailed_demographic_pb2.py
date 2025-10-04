"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/detailed_demographic.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import criterion_category_availability_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_criterion__category__availability__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/googleads/v20/resources/detailed_demographic.proto\x12"google.ads.googleads.v20.resources\x1aEgoogle/ads/googleads/v20/common/criterion_category_availability.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc2\x03\n\x13DetailedDemographic\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x03\xfaA.\n,googleads.googleapis.com/DetailedDemographic\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x03\x12D\n\x06parent\x18\x04 \x01(\tB4\xe0A\x03\xfaA.\n,googleads.googleapis.com/DetailedDemographic\x12\x1c\n\x0flaunched_to_all\x18\x05 \x01(\x08B\x03\xe0A\x03\x12[\n\x0eavailabilities\x18\x06 \x03(\x0b2>.google.ads.googleads.v20.common.CriterionCategoryAvailabilityB\x03\xe0A\x03:y\xeaAv\n,googleads.googleapis.com/DetailedDemographic\x12Fcustomers/{customer_id}/detailedDemographics/{detailed_demographic_id}B\x8a\x02\n&com.google.ads.googleads.v20.resourcesB\x18DetailedDemographicProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.detailed_demographic_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x18DetailedDemographicProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_DETAILEDDEMOGRAPHIC'].fields_by_name['resource_name']._loaded_options = None
    _globals['_DETAILEDDEMOGRAPHIC'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA.\n,googleads.googleapis.com/DetailedDemographic'
    _globals['_DETAILEDDEMOGRAPHIC'].fields_by_name['id']._loaded_options = None
    _globals['_DETAILEDDEMOGRAPHIC'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_DETAILEDDEMOGRAPHIC'].fields_by_name['name']._loaded_options = None
    _globals['_DETAILEDDEMOGRAPHIC'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_DETAILEDDEMOGRAPHIC'].fields_by_name['parent']._loaded_options = None
    _globals['_DETAILEDDEMOGRAPHIC'].fields_by_name['parent']._serialized_options = b'\xe0A\x03\xfaA.\n,googleads.googleapis.com/DetailedDemographic'
    _globals['_DETAILEDDEMOGRAPHIC'].fields_by_name['launched_to_all']._loaded_options = None
    _globals['_DETAILEDDEMOGRAPHIC'].fields_by_name['launched_to_all']._serialized_options = b'\xe0A\x03'
    _globals['_DETAILEDDEMOGRAPHIC'].fields_by_name['availabilities']._loaded_options = None
    _globals['_DETAILEDDEMOGRAPHIC'].fields_by_name['availabilities']._serialized_options = b'\xe0A\x03'
    _globals['_DETAILEDDEMOGRAPHIC']._loaded_options = None
    _globals['_DETAILEDDEMOGRAPHIC']._serialized_options = b'\xeaAv\n,googleads.googleapis.com/DetailedDemographic\x12Fcustomers/{customer_id}/detailedDemographics/{detailed_demographic_id}'
    _globals['_DETAILEDDEMOGRAPHIC']._serialized_start = 233
    _globals['_DETAILEDDEMOGRAPHIC']._serialized_end = 683