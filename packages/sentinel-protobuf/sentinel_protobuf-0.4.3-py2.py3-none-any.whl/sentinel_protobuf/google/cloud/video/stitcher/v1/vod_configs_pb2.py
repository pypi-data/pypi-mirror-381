"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/video/stitcher/v1/vod_configs.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.video.stitcher.v1 import fetch_options_pb2 as google_dot_cloud_dot_video_dot_stitcher_dot_v1_dot_fetch__options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/video/stitcher/v1/vod_configs.proto\x12\x1egoogle.cloud.video.stitcher.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/video/stitcher/v1/fetch_options.proto"\xe1\x03\n\tVodConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x17\n\nsource_uri\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\nad_tag_uri\x18\x03 \x01(\tB\x03\xe0A\x02\x12I\n\x0egam_vod_config\x18\x04 \x01(\x0b2,.google.cloud.video.stitcher.v1.GamVodConfigB\x03\xe0A\x01\x12C\n\x05state\x18\x05 \x01(\x0e2/.google.cloud.video.stitcher.v1.VodConfig.StateB\x03\xe0A\x03\x12J\n\x14source_fetch_options\x18\x08 \x01(\x0b2,.google.cloud.video.stitcher.v1.FetchOptions"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08DELETING\x10\x03:l\xeaAi\n&videostitcher.googleapis.com/VodConfig\x12?projects/{project}/locations/{location}/vodConfigs/{vod_config}")\n\x0cGamVodConfig\x12\x19\n\x0cnetwork_code\x18\x01 \x01(\tB\x03\xe0A\x02Bw\n"com.google.cloud.video.stitcher.v1B\x0fVodConfigsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.stitcher.v1.vod_configs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.video.stitcher.v1B\x0fVodConfigsProtoP\x01Z>cloud.google.com/go/video/stitcher/apiv1/stitcherpb;stitcherpb'
    _globals['_VODCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_VODCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_VODCONFIG'].fields_by_name['source_uri']._loaded_options = None
    _globals['_VODCONFIG'].fields_by_name['source_uri']._serialized_options = b'\xe0A\x02'
    _globals['_VODCONFIG'].fields_by_name['ad_tag_uri']._loaded_options = None
    _globals['_VODCONFIG'].fields_by_name['ad_tag_uri']._serialized_options = b'\xe0A\x02'
    _globals['_VODCONFIG'].fields_by_name['gam_vod_config']._loaded_options = None
    _globals['_VODCONFIG'].fields_by_name['gam_vod_config']._serialized_options = b'\xe0A\x01'
    _globals['_VODCONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_VODCONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_VODCONFIG']._loaded_options = None
    _globals['_VODCONFIG']._serialized_options = b'\xeaAi\n&videostitcher.googleapis.com/VodConfig\x12?projects/{project}/locations/{location}/vodConfigs/{vod_config}'
    _globals['_GAMVODCONFIG'].fields_by_name['network_code']._loaded_options = None
    _globals['_GAMVODCONFIG'].fields_by_name['network_code']._serialized_options = b'\xe0A\x02'
    _globals['_VODCONFIG']._serialized_start = 197
    _globals['_VODCONFIG']._serialized_end = 678
    _globals['_VODCONFIG_STATE']._serialized_start = 499
    _globals['_VODCONFIG_STATE']._serialized_end = 568
    _globals['_GAMVODCONFIG']._serialized_start = 680
    _globals['_GAMVODCONFIG']._serialized_end = 721