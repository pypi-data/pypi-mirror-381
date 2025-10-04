"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/user_interest.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import criterion_category_availability_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_criterion__category__availability__pb2
from ......google.ads.googleads.v19.enums import user_interest_taxonomy_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_user__interest__taxonomy__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/googleads/v19/resources/user_interest.proto\x12"google.ads.googleads.v19.resources\x1aEgoogle/ads/googleads/v19/common/criterion_category_availability.proto\x1a@google/ads/googleads/v19/enums/user_interest_taxonomy_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x86\x05\n\x0cUserInterest\x12D\n\rresource_name\x18\x01 \x01(\tB-\xe0A\x03\xfaA\'\n%googleads.googleapis.com/UserInterest\x12q\n\rtaxonomy_type\x18\x02 \x01(\x0e2U.google.ads.googleads.v19.enums.UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeB\x03\xe0A\x03\x12"\n\x10user_interest_id\x18\x08 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x16\n\x04name\x18\t \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12P\n\x14user_interest_parent\x18\n \x01(\tB-\xe0A\x03\xfaA\'\n%googleads.googleapis.com/UserInterestH\x02\x88\x01\x01\x12!\n\x0flaunched_to_all\x18\x0b \x01(\x08B\x03\xe0A\x03H\x03\x88\x01\x01\x12[\n\x0eavailabilities\x18\x07 \x03(\x0b2>.google.ads.googleads.v19.common.CriterionCategoryAvailabilityB\x03\xe0A\x03:d\xeaAa\n%googleads.googleapis.com/UserInterest\x128customers/{customer_id}/userInterests/{user_interest_id}B\x13\n\x11_user_interest_idB\x07\n\x05_nameB\x17\n\x15_user_interest_parentB\x12\n\x10_launched_to_allB\x83\x02\n&com.google.ads.googleads.v19.resourcesB\x11UserInterestProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.user_interest_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x11UserInterestProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_USERINTEREST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_USERINTEREST'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x03\xfaA'\n%googleads.googleapis.com/UserInterest"
    _globals['_USERINTEREST'].fields_by_name['taxonomy_type']._loaded_options = None
    _globals['_USERINTEREST'].fields_by_name['taxonomy_type']._serialized_options = b'\xe0A\x03'
    _globals['_USERINTEREST'].fields_by_name['user_interest_id']._loaded_options = None
    _globals['_USERINTEREST'].fields_by_name['user_interest_id']._serialized_options = b'\xe0A\x03'
    _globals['_USERINTEREST'].fields_by_name['name']._loaded_options = None
    _globals['_USERINTEREST'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_USERINTEREST'].fields_by_name['user_interest_parent']._loaded_options = None
    _globals['_USERINTEREST'].fields_by_name['user_interest_parent']._serialized_options = b"\xe0A\x03\xfaA'\n%googleads.googleapis.com/UserInterest"
    _globals['_USERINTEREST'].fields_by_name['launched_to_all']._loaded_options = None
    _globals['_USERINTEREST'].fields_by_name['launched_to_all']._serialized_options = b'\xe0A\x03'
    _globals['_USERINTEREST'].fields_by_name['availabilities']._loaded_options = None
    _globals['_USERINTEREST'].fields_by_name['availabilities']._serialized_options = b'\xe0A\x03'
    _globals['_USERINTEREST']._loaded_options = None
    _globals['_USERINTEREST']._serialized_options = b'\xeaAa\n%googleads.googleapis.com/UserInterest\x128customers/{customer_id}/userInterests/{user_interest_id}'
    _globals['_USERINTEREST']._serialized_start = 292
    _globals['_USERINTEREST']._serialized_end = 938