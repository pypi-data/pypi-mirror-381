"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/data_link.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import data_link_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_data__link__status__pb2
from ......google.ads.googleads.v21.enums import data_link_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_data__link__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/ads/googleads/v21/resources/data_link.proto\x12"google.ads.googleads.v21.resources\x1a5google/ads/googleads/v21/enums/data_link_status.proto\x1a3google/ads/googleads/v21/enums/data_link_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb8\x04\n\x08DataLink\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/DataLink\x12!\n\x0fproduct_link_id\x18\x02 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1e\n\x0cdata_link_id\x18\x03 \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12P\n\x04type\x18\x04 \x01(\x0e2=.google.ads.googleads.v21.enums.DataLinkTypeEnum.DataLinkTypeB\x03\xe0A\x03\x12V\n\x06status\x18\x05 \x01(\x0e2A.google.ads.googleads.v21.enums.DataLinkStatusEnum.DataLinkStatusB\x03\xe0A\x03\x12X\n\ryoutube_video\x18\x06 \x01(\x0b2:.google.ads.googleads.v21.resources.YoutubeVideoIdentifierB\x03\xe0A\x05H\x00:j\xeaAg\n!googleads.googleapis.com/DataLink\x12Bcustomers/{customer_id}/dataLinks/{product_link_id}~{data_link_id}B\x12\n\x10data_link_entityB\x12\n\x10_product_link_idB\x0f\n\r_data_link_id"n\n\x16YoutubeVideoIdentifier\x12\x1c\n\nchannel_id\x18\x01 \x01(\tB\x03\xe0A\x05H\x00\x88\x01\x01\x12\x1a\n\x08video_id\x18\x02 \x01(\tB\x03\xe0A\x05H\x01\x88\x01\x01B\r\n\x0b_channel_idB\x0b\n\t_video_idB\xff\x01\n&com.google.ads.googleads.v21.resourcesB\rDataLinkProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.data_link_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\rDataLinkProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_DATALINK'].fields_by_name['resource_name']._loaded_options = None
    _globals['_DATALINK'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/DataLink'
    _globals['_DATALINK'].fields_by_name['product_link_id']._loaded_options = None
    _globals['_DATALINK'].fields_by_name['product_link_id']._serialized_options = b'\xe0A\x03'
    _globals['_DATALINK'].fields_by_name['data_link_id']._loaded_options = None
    _globals['_DATALINK'].fields_by_name['data_link_id']._serialized_options = b'\xe0A\x03'
    _globals['_DATALINK'].fields_by_name['type']._loaded_options = None
    _globals['_DATALINK'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_DATALINK'].fields_by_name['status']._loaded_options = None
    _globals['_DATALINK'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_DATALINK'].fields_by_name['youtube_video']._loaded_options = None
    _globals['_DATALINK'].fields_by_name['youtube_video']._serialized_options = b'\xe0A\x05'
    _globals['_DATALINK']._loaded_options = None
    _globals['_DATALINK']._serialized_options = b'\xeaAg\n!googleads.googleapis.com/DataLink\x12Bcustomers/{customer_id}/dataLinks/{product_link_id}~{data_link_id}'
    _globals['_YOUTUBEVIDEOIDENTIFIER'].fields_by_name['channel_id']._loaded_options = None
    _globals['_YOUTUBEVIDEOIDENTIFIER'].fields_by_name['channel_id']._serialized_options = b'\xe0A\x05'
    _globals['_YOUTUBEVIDEOIDENTIFIER'].fields_by_name['video_id']._loaded_options = None
    _globals['_YOUTUBEVIDEOIDENTIFIER'].fields_by_name['video_id']._serialized_options = b'\xe0A\x05'
    _globals['_DATALINK']._serialized_start = 259
    _globals['_DATALINK']._serialized_end = 827
    _globals['_YOUTUBEVIDEOIDENTIFIER']._serialized_start = 829
    _globals['_YOUTUBEVIDEOIDENTIFIER']._serialized_end = 939