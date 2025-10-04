"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/video.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/ads/googleads/v19/resources/video.proto\x12"google.ads.googleads.v19.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xba\x02\n\x05Video\x12=\n\rresource_name\x18\x01 \x01(\tB&\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Video\x12\x14\n\x02id\x18\x06 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1c\n\nchannel_id\x18\x07 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12!\n\x0fduration_millis\x18\x08 \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12\x17\n\x05title\x18\t \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01:N\xeaAK\n\x1egoogleads.googleapis.com/Video\x12)customers/{customer_id}/videos/{video_id}B\x05\n\x03_idB\r\n\x0b_channel_idB\x12\n\x10_duration_millisB\x08\n\x06_titleB\xfc\x01\n&com.google.ads.googleads.v19.resourcesB\nVideoProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.video_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\nVideoProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_VIDEO'].fields_by_name['resource_name']._loaded_options = None
    _globals['_VIDEO'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Video'
    _globals['_VIDEO'].fields_by_name['id']._loaded_options = None
    _globals['_VIDEO'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEO'].fields_by_name['channel_id']._loaded_options = None
    _globals['_VIDEO'].fields_by_name['channel_id']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEO'].fields_by_name['duration_millis']._loaded_options = None
    _globals['_VIDEO'].fields_by_name['duration_millis']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEO'].fields_by_name['title']._loaded_options = None
    _globals['_VIDEO'].fields_by_name['title']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEO']._loaded_options = None
    _globals['_VIDEO']._serialized_options = b'\xeaAK\n\x1egoogleads.googleapis.com/Video\x12)customers/{customer_id}/videos/{video_id}'
    _globals['_VIDEO']._serialized_start = 147
    _globals['_VIDEO']._serialized_end = 461