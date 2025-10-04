"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/remarketing_action.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import tag_snippet_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_tag__snippet__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/googleads/v19/resources/remarketing_action.proto\x12"google.ads.googleads.v19.resources\x1a1google/ads/googleads/v19/common/tag_snippet.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd4\x02\n\x11RemarketingAction\x12I\n\rresource_name\x18\x01 \x01(\tB2\xe0A\x05\xfaA,\n*googleads.googleapis.com/RemarketingAction\x12\x14\n\x02id\x18\x05 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x06 \x01(\tH\x01\x88\x01\x01\x12F\n\x0ctag_snippets\x18\x04 \x03(\x0b2+.google.ads.googleads.v19.common.TagSnippetB\x03\xe0A\x03:s\xeaAp\n*googleads.googleapis.com/RemarketingAction\x12Bcustomers/{customer_id}/remarketingActions/{remarketing_action_id}B\x05\n\x03_idB\x07\n\x05_nameB\x88\x02\n&com.google.ads.googleads.v19.resourcesB\x16RemarketingActionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.remarketing_action_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x16RemarketingActionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_REMARKETINGACTION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_REMARKETINGACTION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA,\n*googleads.googleapis.com/RemarketingAction'
    _globals['_REMARKETINGACTION'].fields_by_name['id']._loaded_options = None
    _globals['_REMARKETINGACTION'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_REMARKETINGACTION'].fields_by_name['tag_snippets']._loaded_options = None
    _globals['_REMARKETINGACTION'].fields_by_name['tag_snippets']._serialized_options = b'\xe0A\x03'
    _globals['_REMARKETINGACTION']._loaded_options = None
    _globals['_REMARKETINGACTION']._serialized_options = b'\xeaAp\n*googleads.googleapis.com/RemarketingAction\x12Bcustomers/{customer_id}/remarketingActions/{remarketing_action_id}'
    _globals['_REMARKETINGACTION']._serialized_start = 211
    _globals['_REMARKETINGACTION']._serialized_end = 551