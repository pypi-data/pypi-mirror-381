"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/shared_set.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import shared_set_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_shared__set__status__pb2
from ......google.ads.googleads.v21.enums import shared_set_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_shared__set__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/googleads/v21/resources/shared_set.proto\x12"google.ads.googleads.v21.resources\x1a6google/ads/googleads/v21/enums/shared_set_status.proto\x1a4google/ads/googleads/v21/enums/shared_set_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xfa\x03\n\tSharedSet\x12A\n\rresource_name\x18\x01 \x01(\tB*\xe0A\x05\xfaA$\n"googleads.googleapis.com/SharedSet\x12\x14\n\x02id\x18\x08 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12R\n\x04type\x18\x03 \x01(\x0e2?.google.ads.googleads.v21.enums.SharedSetTypeEnum.SharedSetTypeB\x03\xe0A\x05\x12\x11\n\x04name\x18\t \x01(\tH\x01\x88\x01\x01\x12X\n\x06status\x18\x05 \x01(\x0e2C.google.ads.googleads.v21.enums.SharedSetStatusEnum.SharedSetStatusB\x03\xe0A\x03\x12\x1e\n\x0cmember_count\x18\n \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12!\n\x0freference_count\x18\x0b \x01(\x03B\x03\xe0A\x03H\x03\x88\x01\x01:[\xeaAX\n"googleads.googleapis.com/SharedSet\x122customers/{customer_id}/sharedSets/{shared_set_id}B\x05\n\x03_idB\x07\n\x05_nameB\x0f\n\r_member_countB\x12\n\x10_reference_countB\x80\x02\n&com.google.ads.googleads.v21.resourcesB\x0eSharedSetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.shared_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x0eSharedSetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_SHAREDSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_SHAREDSET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA$\n"googleads.googleapis.com/SharedSet'
    _globals['_SHAREDSET'].fields_by_name['id']._loaded_options = None
    _globals['_SHAREDSET'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_SHAREDSET'].fields_by_name['type']._loaded_options = None
    _globals['_SHAREDSET'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_SHAREDSET'].fields_by_name['status']._loaded_options = None
    _globals['_SHAREDSET'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_SHAREDSET'].fields_by_name['member_count']._loaded_options = None
    _globals['_SHAREDSET'].fields_by_name['member_count']._serialized_options = b'\xe0A\x03'
    _globals['_SHAREDSET'].fields_by_name['reference_count']._loaded_options = None
    _globals['_SHAREDSET'].fields_by_name['reference_count']._serialized_options = b'\xe0A\x03'
    _globals['_SHAREDSET']._loaded_options = None
    _globals['_SHAREDSET']._serialized_options = b'\xeaAX\n"googleads.googleapis.com/SharedSet\x122customers/{customer_id}/sharedSets/{shared_set_id}'
    _globals['_SHAREDSET']._serialized_start = 262
    _globals['_SHAREDSET']._serialized_end = 768