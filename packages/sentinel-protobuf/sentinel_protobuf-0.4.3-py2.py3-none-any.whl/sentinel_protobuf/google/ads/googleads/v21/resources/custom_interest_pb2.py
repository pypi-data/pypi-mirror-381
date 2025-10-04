"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/custom_interest.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import custom_interest_member_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_custom__interest__member__type__pb2
from ......google.ads.googleads.v21.enums import custom_interest_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_custom__interest__status__pb2
from ......google.ads.googleads.v21.enums import custom_interest_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_custom__interest__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v21/resources/custom_interest.proto\x12"google.ads.googleads.v21.resources\x1a@google/ads/googleads/v21/enums/custom_interest_member_type.proto\x1a;google/ads/googleads/v21/enums/custom_interest_status.proto\x1a9google/ads/googleads/v21/enums/custom_interest_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xaa\x04\n\x0eCustomInterest\x12F\n\rresource_name\x18\x01 \x01(\tB/\xe0A\x05\xfaA)\n\'googleads.googleapis.com/CustomInterest\x12\x14\n\x02id\x18\x08 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12]\n\x06status\x18\x03 \x01(\x0e2M.google.ads.googleads.v21.enums.CustomInterestStatusEnum.CustomInterestStatus\x12\x11\n\x04name\x18\t \x01(\tH\x01\x88\x01\x01\x12W\n\x04type\x18\x05 \x01(\x0e2I.google.ads.googleads.v21.enums.CustomInterestTypeEnum.CustomInterestType\x12\x18\n\x0bdescription\x18\n \x01(\tH\x02\x88\x01\x01\x12I\n\x07members\x18\x07 \x03(\x0b28.google.ads.googleads.v21.resources.CustomInterestMember:j\xeaAg\n\'googleads.googleapis.com/CustomInterest\x12<customers/{customer_id}/customInterests/{custom_interest_id}B\x05\n\x03_idB\x07\n\x05_nameB\x0e\n\x0c_description"\xa8\x01\n\x14CustomInterestMember\x12j\n\x0bmember_type\x18\x01 \x01(\x0e2U.google.ads.googleads.v21.enums.CustomInterestMemberTypeEnum.CustomInterestMemberType\x12\x16\n\tparameter\x18\x03 \x01(\tH\x00\x88\x01\x01B\x0c\n\n_parameterB\x85\x02\n&com.google.ads.googleads.v21.resourcesB\x13CustomInterestProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.custom_interest_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x13CustomInterestProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_CUSTOMINTEREST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMINTEREST'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x05\xfaA)\n'googleads.googleapis.com/CustomInterest"
    _globals['_CUSTOMINTEREST'].fields_by_name['id']._loaded_options = None
    _globals['_CUSTOMINTEREST'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMINTEREST']._loaded_options = None
    _globals['_CUSTOMINTEREST']._serialized_options = b"\xeaAg\n'googleads.googleapis.com/CustomInterest\x12<customers/{customer_id}/customInterests/{custom_interest_id}"
    _globals['_CUSTOMINTEREST']._serialized_start = 343
    _globals['_CUSTOMINTEREST']._serialized_end = 897
    _globals['_CUSTOMINTERESTMEMBER']._serialized_start = 900
    _globals['_CUSTOMINTERESTMEMBER']._serialized_end = 1068