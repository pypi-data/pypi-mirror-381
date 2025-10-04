"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1alpha/session.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import answer_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_answer__pb2
from .....google.cloud.discoveryengine.v1alpha import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/discoveryengine/v1alpha/session.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/discoveryengine/v1alpha/answer.proto\x1a1google/cloud/discoveryengine/v1alpha/common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd9\x08\n\x07Session\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x07 \x01(\tB\x03\xe0A\x01\x12B\n\x05state\x18\x02 \x01(\x0e23.google.cloud.discoveryengine.v1alpha.Session.State\x12\x16\n\x0euser_pseudo_id\x18\x03 \x01(\t\x12A\n\x05turns\x18\x04 \x03(\x0b22.google.cloud.discoveryengine.v1alpha.Session.Turn\x123\n\nstart_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x16\n\tis_pinned\x18\x08 \x01(\x08B\x03\xe0A\x01\x1a\xe6\x02\n\x04Turn\x12?\n\x05query\x18\x01 \x01(\x0b2+.google.cloud.discoveryengine.v1alpha.QueryB\x03\xe0A\x01\x12=\n\x06answer\x18\x02 \x01(\tB-\xe0A\x01\xfaA\'\n%discoveryengine.googleapis.com/Answer\x12J\n\x0fdetailed_answer\x18\x07 \x01(\x0b2,.google.cloud.discoveryengine.v1alpha.AnswerB\x03\xe0A\x03\x12^\n\x0cquery_config\x18\x10 \x03(\x0b2C.google.cloud.discoveryengine.v1alpha.Session.Turn.QueryConfigEntryB\x03\xe0A\x01\x1a2\n\x10QueryConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"/\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01:\xe6\x02\xeaA\xe2\x02\n&discoveryengine.googleapis.com/Session\x12Rprojects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}\x12kprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}\x12dprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}*\x08sessions2\x07session"9\n\x05Query\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12\x15\n\x08query_id\x18\x01 \x01(\tB\x03\xe0A\x03B\t\n\x07content"\xa5\x02\n\x14ImageCharacteristics\x12\x12\n\x05width\x18\x01 \x01(\x05B\x03\xe0A\x03\x12\x13\n\x06height\x18\x02 \x01(\x05B\x03\xe0A\x03\x12_\n\x0bcolor_space\x18\x03 \x01(\x0e2E.google.cloud.discoveryengine.v1alpha.ImageCharacteristics.ColorSpaceB\x03\xe0A\x03\x12\x16\n\tbit_depth\x18\x04 \x01(\x05B\x03\xe0A\x03"k\n\nColorSpace\x12\x1b\n\x17COLOR_SPACE_UNSPECIFIED\x10\x00\x12\x07\n\x03RGB\x10\x01\x12\x08\n\x04CMYK\x10\x02\x12\r\n\tGRAYSCALE\x10\x03\x12\x07\n\x03YUV\x10\x04\x12\x15\n\x11OTHER_COLOR_SPACE\x10\x05"\x82\x02\n\x14VideoCharacteristics\x12\x12\n\x05width\x18\x01 \x01(\x05B\x03\xe0A\x03\x12\x13\n\x06height\x18\x02 \x01(\x05B\x03\xe0A\x03\x120\n\x08duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x03\x12\x17\n\nframe_rate\x18\x04 \x01(\x01B\x03\xe0A\x03\x12\x19\n\x0caudio_codecs\x18\x05 \x03(\tB\x03\xe0A\x03\x12\x19\n\x0cvideo_codecs\x18\x06 \x03(\tB\x03\xe0A\x03\x12\x1f\n\x12video_bitrate_kbps\x18\x07 \x01(\x05B\x03\xe0A\x03\x12\x1f\n\x12audio_bitrate_kbps\x18\x08 \x01(\x05B\x03\xe0A\x03"\xbb\x01\n\x13FileCharacteristics\x12l\n\x0fcharacteristics\x18\x06 \x03(\x0b2N.google.cloud.discoveryengine.v1alpha.FileCharacteristics.CharacteristicsEntryB\x03\xe0A\x03\x1a6\n\x14CharacteristicsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xcf\x03\n\x08FileView\x12`\n\x15image_characteristics\x18\x06 \x01(\x0b2:.google.cloud.discoveryengine.v1alpha.ImageCharacteristicsB\x03\xe0A\x03H\x00\x12`\n\x15video_characteristics\x18\x07 \x01(\x0b2:.google.cloud.discoveryengine.v1alpha.VideoCharacteristicsB\x03\xe0A\x03H\x00\x12^\n\x14file_characteristics\x18\x08 \x01(\x0b29.google.cloud.discoveryengine.v1alpha.FileCharacteristicsB\x03\xe0A\x03H\x00\x12\x14\n\x07view_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x03uri\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x16\n\tmime_type\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x16\n\tbyte_size\x18\x04 \x01(\x03B\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03B\x11\n\x0fcharacteristics"\xeb\x05\n\x0cFileMetadata\x12\x14\n\x07file_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x11\n\tmime_type\x18\x03 \x01(\t\x12\x16\n\tbyte_size\x18\x04 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0coriginal_uri\x18\t \x01(\tB\x03\xe0A\x01\x12S\n\x14original_source_type\x18\n \x01(\x0e20.google.cloud.discoveryengine.v1alpha.FileSourceB\x03\xe0A\x01\x124\n\x0bupload_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x126\n\rlast_add_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12W\n\x08metadata\x18\x12 \x03(\x0b2@.google.cloud.discoveryengine.v1alpha.FileMetadata.MetadataEntryB\x03\xe0A\x01\x12\x19\n\x0cdownload_uri\x18\x14 \x01(\tB\x03\xe0A\x03\x12S\n\x10file_origin_type\x18\x15 \x01(\x0e24.google.cloud.discoveryengine.v1alpha.FileOriginTypeB\x03\xe0A\x01\x12Q\n\x05views\x18\x16 \x03(\x0b2=.google.cloud.discoveryengine.v1alpha.FileMetadata.ViewsEntryB\x03\xe0A\x03\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a\\\n\nViewsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b2..google.cloud.discoveryengine.v1alpha.FileView:\x028\x01*\xa9\x01\n\nFileSource\x12\x1b\n\x17FILE_SOURCE_UNSPECIFIED\x10\x00\x12\x16\n\x12FILE_SOURCE_INLINE\x10\x01\x12\x15\n\x11FILE_SOURCE_LOCAL\x10\x02\x12\x1d\n\x19FILE_SOURCE_CLOUD_STORAGE\x10\x03\x12\x1b\n\x17FILE_SOURCE_CLOUD_DRIVE\x10\x04\x12\x13\n\x0fFILE_SOURCE_URL\x10\x05B\x98\x02\n(com.google.cloud.discoveryengine.v1alphaB\x0cSessionProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.session_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x0cSessionProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_SESSION_TURN_QUERYCONFIGENTRY']._loaded_options = None
    _globals['_SESSION_TURN_QUERYCONFIGENTRY']._serialized_options = b'8\x01'
    _globals['_SESSION_TURN'].fields_by_name['query']._loaded_options = None
    _globals['_SESSION_TURN'].fields_by_name['query']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION_TURN'].fields_by_name['answer']._loaded_options = None
    _globals['_SESSION_TURN'].fields_by_name['answer']._serialized_options = b"\xe0A\x01\xfaA'\n%discoveryengine.googleapis.com/Answer"
    _globals['_SESSION_TURN'].fields_by_name['detailed_answer']._loaded_options = None
    _globals['_SESSION_TURN'].fields_by_name['detailed_answer']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION_TURN'].fields_by_name['query_config']._loaded_options = None
    _globals['_SESSION_TURN'].fields_by_name['query_config']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['name']._loaded_options = None
    _globals['_SESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_SESSION'].fields_by_name['display_name']._loaded_options = None
    _globals['_SESSION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['start_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['end_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['is_pinned']._loaded_options = None
    _globals['_SESSION'].fields_by_name['is_pinned']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION']._loaded_options = None
    _globals['_SESSION']._serialized_options = b'\xeaA\xe2\x02\n&discoveryengine.googleapis.com/Session\x12Rprojects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}\x12kprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}\x12dprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}*\x08sessions2\x07session'
    _globals['_QUERY'].fields_by_name['query_id']._loaded_options = None
    _globals['_QUERY'].fields_by_name['query_id']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGECHARACTERISTICS'].fields_by_name['width']._loaded_options = None
    _globals['_IMAGECHARACTERISTICS'].fields_by_name['width']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGECHARACTERISTICS'].fields_by_name['height']._loaded_options = None
    _globals['_IMAGECHARACTERISTICS'].fields_by_name['height']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGECHARACTERISTICS'].fields_by_name['color_space']._loaded_options = None
    _globals['_IMAGECHARACTERISTICS'].fields_by_name['color_space']._serialized_options = b'\xe0A\x03'
    _globals['_IMAGECHARACTERISTICS'].fields_by_name['bit_depth']._loaded_options = None
    _globals['_IMAGECHARACTERISTICS'].fields_by_name['bit_depth']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['width']._loaded_options = None
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['width']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['height']._loaded_options = None
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['height']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['duration']._loaded_options = None
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['duration']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['frame_rate']._loaded_options = None
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['frame_rate']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['audio_codecs']._loaded_options = None
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['audio_codecs']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['video_codecs']._loaded_options = None
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['video_codecs']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['video_bitrate_kbps']._loaded_options = None
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['video_bitrate_kbps']._serialized_options = b'\xe0A\x03'
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['audio_bitrate_kbps']._loaded_options = None
    _globals['_VIDEOCHARACTERISTICS'].fields_by_name['audio_bitrate_kbps']._serialized_options = b'\xe0A\x03'
    _globals['_FILECHARACTERISTICS_CHARACTERISTICSENTRY']._loaded_options = None
    _globals['_FILECHARACTERISTICS_CHARACTERISTICSENTRY']._serialized_options = b'8\x01'
    _globals['_FILECHARACTERISTICS'].fields_by_name['characteristics']._loaded_options = None
    _globals['_FILECHARACTERISTICS'].fields_by_name['characteristics']._serialized_options = b'\xe0A\x03'
    _globals['_FILEVIEW'].fields_by_name['image_characteristics']._loaded_options = None
    _globals['_FILEVIEW'].fields_by_name['image_characteristics']._serialized_options = b'\xe0A\x03'
    _globals['_FILEVIEW'].fields_by_name['video_characteristics']._loaded_options = None
    _globals['_FILEVIEW'].fields_by_name['video_characteristics']._serialized_options = b'\xe0A\x03'
    _globals['_FILEVIEW'].fields_by_name['file_characteristics']._loaded_options = None
    _globals['_FILEVIEW'].fields_by_name['file_characteristics']._serialized_options = b'\xe0A\x03'
    _globals['_FILEVIEW'].fields_by_name['view_id']._loaded_options = None
    _globals['_FILEVIEW'].fields_by_name['view_id']._serialized_options = b'\xe0A\x03'
    _globals['_FILEVIEW'].fields_by_name['uri']._loaded_options = None
    _globals['_FILEVIEW'].fields_by_name['uri']._serialized_options = b'\xe0A\x03'
    _globals['_FILEVIEW'].fields_by_name['mime_type']._loaded_options = None
    _globals['_FILEVIEW'].fields_by_name['mime_type']._serialized_options = b'\xe0A\x03'
    _globals['_FILEVIEW'].fields_by_name['byte_size']._loaded_options = None
    _globals['_FILEVIEW'].fields_by_name['byte_size']._serialized_options = b'\xe0A\x03'
    _globals['_FILEVIEW'].fields_by_name['create_time']._loaded_options = None
    _globals['_FILEVIEW'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FILEMETADATA_METADATAENTRY']._loaded_options = None
    _globals['_FILEMETADATA_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_FILEMETADATA_VIEWSENTRY']._loaded_options = None
    _globals['_FILEMETADATA_VIEWSENTRY']._serialized_options = b'8\x01'
    _globals['_FILEMETADATA'].fields_by_name['file_id']._loaded_options = None
    _globals['_FILEMETADATA'].fields_by_name['file_id']._serialized_options = b'\xe0A\x03'
    _globals['_FILEMETADATA'].fields_by_name['name']._loaded_options = None
    _globals['_FILEMETADATA'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_FILEMETADATA'].fields_by_name['byte_size']._loaded_options = None
    _globals['_FILEMETADATA'].fields_by_name['byte_size']._serialized_options = b'\xe0A\x03'
    _globals['_FILEMETADATA'].fields_by_name['original_uri']._loaded_options = None
    _globals['_FILEMETADATA'].fields_by_name['original_uri']._serialized_options = b'\xe0A\x01'
    _globals['_FILEMETADATA'].fields_by_name['original_source_type']._loaded_options = None
    _globals['_FILEMETADATA'].fields_by_name['original_source_type']._serialized_options = b'\xe0A\x01'
    _globals['_FILEMETADATA'].fields_by_name['upload_time']._loaded_options = None
    _globals['_FILEMETADATA'].fields_by_name['upload_time']._serialized_options = b'\xe0A\x03'
    _globals['_FILEMETADATA'].fields_by_name['last_add_time']._loaded_options = None
    _globals['_FILEMETADATA'].fields_by_name['last_add_time']._serialized_options = b'\xe0A\x03'
    _globals['_FILEMETADATA'].fields_by_name['metadata']._loaded_options = None
    _globals['_FILEMETADATA'].fields_by_name['metadata']._serialized_options = b'\xe0A\x01'
    _globals['_FILEMETADATA'].fields_by_name['download_uri']._loaded_options = None
    _globals['_FILEMETADATA'].fields_by_name['download_uri']._serialized_options = b'\xe0A\x03'
    _globals['_FILEMETADATA'].fields_by_name['file_origin_type']._loaded_options = None
    _globals['_FILEMETADATA'].fields_by_name['file_origin_type']._serialized_options = b'\xe0A\x01'
    _globals['_FILEMETADATA'].fields_by_name['views']._loaded_options = None
    _globals['_FILEMETADATA'].fields_by_name['views']._serialized_options = b'\xe0A\x03'
    _globals['_FILESOURCE']._serialized_start = 3458
    _globals['_FILESOURCE']._serialized_end = 3627
    _globals['_SESSION']._serialized_start = 320
    _globals['_SESSION']._serialized_end = 1433
    _globals['_SESSION_TURN']._serialized_start = 665
    _globals['_SESSION_TURN']._serialized_end = 1023
    _globals['_SESSION_TURN_QUERYCONFIGENTRY']._serialized_start = 973
    _globals['_SESSION_TURN_QUERYCONFIGENTRY']._serialized_end = 1023
    _globals['_SESSION_STATE']._serialized_start = 1025
    _globals['_SESSION_STATE']._serialized_end = 1072
    _globals['_QUERY']._serialized_start = 1435
    _globals['_QUERY']._serialized_end = 1492
    _globals['_IMAGECHARACTERISTICS']._serialized_start = 1495
    _globals['_IMAGECHARACTERISTICS']._serialized_end = 1788
    _globals['_IMAGECHARACTERISTICS_COLORSPACE']._serialized_start = 1681
    _globals['_IMAGECHARACTERISTICS_COLORSPACE']._serialized_end = 1788
    _globals['_VIDEOCHARACTERISTICS']._serialized_start = 1791
    _globals['_VIDEOCHARACTERISTICS']._serialized_end = 2049
    _globals['_FILECHARACTERISTICS']._serialized_start = 2052
    _globals['_FILECHARACTERISTICS']._serialized_end = 2239
    _globals['_FILECHARACTERISTICS_CHARACTERISTICSENTRY']._serialized_start = 2185
    _globals['_FILECHARACTERISTICS_CHARACTERISTICSENTRY']._serialized_end = 2239
    _globals['_FILEVIEW']._serialized_start = 2242
    _globals['_FILEVIEW']._serialized_end = 2705
    _globals['_FILEMETADATA']._serialized_start = 2708
    _globals['_FILEMETADATA']._serialized_end = 3455
    _globals['_FILEMETADATA_METADATAENTRY']._serialized_start = 3314
    _globals['_FILEMETADATA_METADATAENTRY']._serialized_end = 3361
    _globals['_FILEMETADATA_VIEWSENTRY']._serialized_start = 3363
    _globals['_FILEMETADATA_VIEWSENTRY']._serialized_end = 3455