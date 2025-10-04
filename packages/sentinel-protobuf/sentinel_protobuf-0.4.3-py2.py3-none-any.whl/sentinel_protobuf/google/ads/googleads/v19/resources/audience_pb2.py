"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/audience.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import audiences_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_audiences__pb2
from ......google.ads.googleads.v19.enums import audience_scope_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_audience__scope__pb2
from ......google.ads.googleads.v19.enums import audience_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_audience__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ads/googleads/v19/resources/audience.proto\x12"google.ads.googleads.v19.resources\x1a/google/ads/googleads/v19/common/audiences.proto\x1a3google/ads/googleads/v19/enums/audience_scope.proto\x1a4google/ads/googleads/v19/enums/audience_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf3\x04\n\x08Audience\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/Audience\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12V\n\x06status\x18\x03 \x01(\x0e2A.google.ads.googleads.v19.enums.AudienceStatusEnum.AudienceStatusB\x03\xe0A\x03\x12\x11\n\x04name\x18\n \x01(\tH\x00\x88\x01\x01\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12F\n\ndimensions\x18\x06 \x03(\x0b22.google.ads.googleads.v19.common.AudienceDimension\x12X\n\x13exclusion_dimension\x18\x07 \x01(\x0b2;.google.ads.googleads.v19.common.AudienceExclusionDimension\x12N\n\x05scope\x18\x08 \x01(\x0e2?.google.ads.googleads.v19.enums.AudienceScopeEnum.AudienceScope\x12@\n\x0basset_group\x18\t \x01(\tB+\xe0A\x05\xfaA%\n#googleads.googleapis.com/AssetGroup:W\xeaAT\n!googleads.googleapis.com/Audience\x12/customers/{customer_id}/audiences/{audience_id}B\x07\n\x05_nameB\xff\x01\n&com.google.ads.googleads.v19.resourcesB\rAudienceProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.audience_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\rAudienceProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_AUDIENCE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Audience'
    _globals['_AUDIENCE'].fields_by_name['id']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCE'].fields_by_name['status']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCE'].fields_by_name['asset_group']._loaded_options = None
    _globals['_AUDIENCE'].fields_by_name['asset_group']._serialized_options = b'\xe0A\x05\xfaA%\n#googleads.googleapis.com/AssetGroup'
    _globals['_AUDIENCE']._loaded_options = None
    _globals['_AUDIENCE']._serialized_options = b'\xeaAT\n!googleads.googleapis.com/Audience\x12/customers/{customer_id}/audiences/{audience_id}'
    _globals['_AUDIENCE']._serialized_start = 306
    _globals['_AUDIENCE']._serialized_end = 933