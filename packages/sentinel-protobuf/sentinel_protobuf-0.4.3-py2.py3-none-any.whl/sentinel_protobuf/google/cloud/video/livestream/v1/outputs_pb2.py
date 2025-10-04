"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/video/livestream/v1/outputs.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from ......google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/video/livestream/v1/outputs.proto\x12 google.cloud.video.livestream.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/rpc/status.proto\x1a\x1agoogle/type/datetime.proto"\x87\x02\n\x10ElementaryStream\x12\x0b\n\x03key\x18\x04 \x01(\t\x12E\n\x0cvideo_stream\x18\x01 \x01(\x0b2-.google.cloud.video.livestream.v1.VideoStreamH\x00\x12E\n\x0caudio_stream\x18\x02 \x01(\x0b2-.google.cloud.video.livestream.v1.AudioStreamH\x00\x12C\n\x0btext_stream\x18\x03 \x01(\x0b2,.google.cloud.video.livestream.v1.TextStreamH\x00B\x13\n\x11elementary_stream"\xab\x01\n\tMuxStream\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x11\n\tcontainer\x18\x03 \x01(\t\x12\x1a\n\x12elementary_streams\x18\x04 \x03(\t\x12K\n\x10segment_settings\x18\x05 \x01(\x0b21.google.cloud.video.livestream.v1.SegmentSettings\x12\x15\n\rencryption_id\x18\x06 \x01(\t"\xce\x02\n\x08Manifest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12J\n\x04type\x18\x02 \x01(\x0e27.google.cloud.video.livestream.v1.Manifest.ManifestTypeB\x03\xe0A\x02\x12\x18\n\x0bmux_streams\x18\x03 \x03(\tB\x03\xe0A\x02\x12\x19\n\x11max_segment_count\x18\x04 \x01(\x05\x128\n\x15segment_keep_duration\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12 \n\x18use_timecode_as_timeline\x18\x06 \x01(\x08\x12\x10\n\x03key\x18\x07 \x01(\tB\x03\xe0A\x01"@\n\x0cManifestType\x12\x1d\n\x19MANIFEST_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03HLS\x10\x01\x12\x08\n\x04DASH\x10\x02"_\n\x12DistributionStream\x12\x10\n\x03key\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tcontainer\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12elementary_streams\x18\x03 \x03(\tB\x03\xe0A\x02"\xc7\x03\n\x0cDistribution\x12\x10\n\x03key\x18\x01 \x01(\tB\x03\xe0A\x02\x12 \n\x13distribution_stream\x18\x02 \x01(\tB\x03\xe0A\x02\x12H\n\x05state\x18\x03 \x01(\x0e24.google.cloud.video.livestream.v1.Distribution.StateB\x03\xe0A\x03\x12&\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12K\n\x08srt_push\x18\x05 \x01(\x0b27.google.cloud.video.livestream.v1.SrtPushOutputEndpointH\x00\x12M\n\trtmp_push\x18\x06 \x01(\x0b28.google.cloud.video.livestream.v1.RtmpPushOutputEndpointH\x00"i\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\t\n\x05ERROR\x10\x05\x12\r\n\tNOT_READY\x10\x06\x12\t\n\x05READY\x10\x07\x12\x12\n\x0eAWAITING_INPUT\x10\x08\x12\x10\n\x0cDISTRIBUTING\x10\tB\n\n\x08endpoint"\x94\x01\n\x15SrtPushOutputEndpoint\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12T\n\x19passphrase_secret_version\x18\x02 \x01(\tB/\xfaA,\n*secretmanager.googleapis.com/SecretVersionH\x00B\x13\n\x11passphrase_source"C\n\x16RtmpPushOutputEndpoint\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nstream_key\x18\x02 \x01(\tB\x03\xe0A\x02"\xe3\x01\n\x0bSpriteSheet\x12\x0e\n\x06format\x18\x01 \x01(\t\x12\x18\n\x0bfile_prefix\x18\x02 \x01(\tB\x03\xe0A\x02\x12 \n\x13sprite_width_pixels\x18\x03 \x01(\x05B\x03\xe0A\x02\x12!\n\x14sprite_height_pixels\x18\x04 \x01(\x05B\x03\xe0A\x02\x12\x14\n\x0ccolumn_count\x18\x05 \x01(\x05\x12\x11\n\trow_count\x18\x06 \x01(\x05\x12+\n\x08interval\x18\x07 \x01(\x0b2\x19.google.protobuf.Duration\x12\x0f\n\x07quality\x18\x08 \x01(\x05"\xc5\x03\n\x13PreprocessingConfig\x12J\n\x05audio\x18\x01 \x01(\x0b2;.google.cloud.video.livestream.v1.PreprocessingConfig.Audio\x12H\n\x04crop\x18\x02 \x01(\x0b2:.google.cloud.video.livestream.v1.PreprocessingConfig.Crop\x12F\n\x03pad\x18\x03 \x01(\x0b29.google.cloud.video.livestream.v1.PreprocessingConfig.Pad\x1a\x15\n\x05Audio\x12\x0c\n\x04lufs\x18\x01 \x01(\x01\x1a\\\n\x04Crop\x12\x12\n\ntop_pixels\x18\x01 \x01(\x05\x12\x15\n\rbottom_pixels\x18\x02 \x01(\x05\x12\x13\n\x0bleft_pixels\x18\x03 \x01(\x05\x12\x14\n\x0cright_pixels\x18\x04 \x01(\x05\x1a[\n\x03Pad\x12\x12\n\ntop_pixels\x18\x01 \x01(\x05\x12\x15\n\rbottom_pixels\x18\x02 \x01(\x05\x12\x13\n\x0bleft_pixels\x18\x03 \x01(\x05\x12\x14\n\x0cright_pixels\x18\x04 \x01(\x05"\xbe\x07\n\x0bVideoStream\x12O\n\x04h264\x18\x14 \x01(\x0b2?.google.cloud.video.livestream.v1.VideoStream.H264CodecSettingsH\x00\x12O\n\x04h265\x18\x15 \x01(\x0b2?.google.cloud.video.livestream.v1.VideoStream.H265CodecSettingsH\x00\x1a\x8c\x03\n\x11H264CodecSettings\x12\x14\n\x0cwidth_pixels\x18\x01 \x01(\x05\x12\x15\n\rheight_pixels\x18\x02 \x01(\x05\x12\x17\n\nframe_rate\x18\x03 \x01(\x01B\x03\xe0A\x02\x12\x18\n\x0bbitrate_bps\x18\x04 \x01(\x05B\x03\xe0A\x02\x12\x16\n\x0eallow_open_gop\x18\x06 \x01(\x08\x12\x19\n\x0fgop_frame_count\x18\x07 \x01(\x05H\x00\x121\n\x0cgop_duration\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x12\x15\n\rvbv_size_bits\x18\t \x01(\x05\x12\x19\n\x11vbv_fullness_bits\x18\n \x01(\x05\x12\x15\n\rentropy_coder\x18\x0b \x01(\t\x12\x11\n\tb_pyramid\x18\x0c \x01(\x08\x12\x15\n\rb_frame_count\x18\r \x01(\x05\x12\x13\n\x0baq_strength\x18\x0e \x01(\x01\x12\x0f\n\x07profile\x18\x0f \x01(\t\x12\x0c\n\x04tune\x18\x10 \x01(\tB\n\n\x08gop_mode\x1a\xeb\x02\n\x11H265CodecSettings\x12\x19\n\x0cwidth_pixels\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x1a\n\rheight_pixels\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\nframe_rate\x18\x03 \x01(\x01B\x03\xe0A\x02\x12\x18\n\x0bbitrate_bps\x18\x04 \x01(\x05B\x03\xe0A\x02\x12\x1e\n\x0fgop_frame_count\x18\x07 \x01(\x05B\x03\xe0A\x01H\x00\x126\n\x0cgop_duration\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01H\x00\x12\x1a\n\rvbv_size_bits\x18\t \x01(\x05B\x03\xe0A\x01\x12\x1e\n\x11vbv_fullness_bits\x18\n \x01(\x05B\x03\xe0A\x01\x12\x16\n\tb_pyramid\x18\x0b \x01(\x08B\x03\xe0A\x01\x12\x1a\n\rb_frame_count\x18\x0c \x01(\x05B\x03\xe0A\x01\x12\x18\n\x0baq_strength\x18\r \x01(\x01B\x03\xe0A\x01B\n\n\x08gop_modeB\x10\n\x0ecodec_settings"\xec\x02\n\x0bAudioStream\x12\x10\n\x08transmux\x18\x08 \x01(\x08\x12\r\n\x05codec\x18\x01 \x01(\t\x12\x18\n\x0bbitrate_bps\x18\x02 \x01(\x05B\x03\xe0A\x02\x12\x15\n\rchannel_count\x18\x03 \x01(\x05\x12\x16\n\x0echannel_layout\x18\x04 \x03(\t\x12K\n\x07mapping\x18\x05 \x03(\x0b2:.google.cloud.video.livestream.v1.AudioStream.AudioMapping\x12\x19\n\x11sample_rate_hertz\x18\x06 \x01(\x05\x1a\x8a\x01\n\x0cAudioMapping\x12\x16\n\tinput_key\x18\x06 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0binput_track\x18\x02 \x01(\x05B\x03\xe0A\x02\x12\x1a\n\rinput_channel\x18\x03 \x01(\x05B\x03\xe0A\x02\x12\x1b\n\x0eoutput_channel\x18\x04 \x01(\x05B\x03\xe0A\x02\x12\x0f\n\x07gain_db\x18\x05 \x01(\x01"\xcb\x02\n\nTextStream\x12\x12\n\x05codec\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1f\n\x12output_cea_channel\x18\x05 \x01(\tB\x03\xe0A\x01\x12N\n\x07mapping\x18\x03 \x03(\x0b28.google.cloud.video.livestream.v1.TextStream.TextMappingB\x03\xe0A\x01\x1a\x80\x01\n\x0bTextMapping\x12\x16\n\tinput_key\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0binput_track\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x1e\n\x11input_cea_channel\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x1f\n\x12from_language_code\x18\x06 \x01(\tB\x03\xe0A\x01"F\n\x0fSegmentSettings\x123\n\x10segment_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration"\xac\x02\n\x0eTimecodeConfig\x12O\n\x06source\x18\x01 \x01(\x0e2?.google.cloud.video.livestream.v1.TimecodeConfig.TimecodeSource\x12/\n\nutc_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x12*\n\ttime_zone\x18\x03 \x01(\x0b2\x15.google.type.TimeZoneH\x00"]\n\x0eTimecodeSource\x12\x1f\n\x1bTIMECODE_SOURCE_UNSPECIFIED\x10\x00\x12\x13\n\x0fMEDIA_TIMESTAMP\x10\x01\x12\x15\n\x11EMBEDDED_TIMECODE\x10\x02B\r\n\x0btime_offsetB\xe9\x01\n$com.google.cloud.video.livestream.v1B\x0cOutputsProtoP\x01ZDcloud.google.com/go/video/livestream/apiv1/livestreampb;livestreampb\xaa\x02 Google.Cloud.Video.LiveStream.V1\xca\x02 Google\\Cloud\\Video\\LiveStream\\V1\xea\x02$Google::Cloud::Video::LiveStream::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.video.livestream.v1.outputs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.video.livestream.v1B\x0cOutputsProtoP\x01ZDcloud.google.com/go/video/livestream/apiv1/livestreampb;livestreampb\xaa\x02 Google.Cloud.Video.LiveStream.V1\xca\x02 Google\\Cloud\\Video\\LiveStream\\V1\xea\x02$Google::Cloud::Video::LiveStream::V1'
    _globals['_MANIFEST'].fields_by_name['type']._loaded_options = None
    _globals['_MANIFEST'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_MANIFEST'].fields_by_name['mux_streams']._loaded_options = None
    _globals['_MANIFEST'].fields_by_name['mux_streams']._serialized_options = b'\xe0A\x02'
    _globals['_MANIFEST'].fields_by_name['key']._loaded_options = None
    _globals['_MANIFEST'].fields_by_name['key']._serialized_options = b'\xe0A\x01'
    _globals['_DISTRIBUTIONSTREAM'].fields_by_name['key']._loaded_options = None
    _globals['_DISTRIBUTIONSTREAM'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_DISTRIBUTIONSTREAM'].fields_by_name['container']._loaded_options = None
    _globals['_DISTRIBUTIONSTREAM'].fields_by_name['container']._serialized_options = b'\xe0A\x02'
    _globals['_DISTRIBUTIONSTREAM'].fields_by_name['elementary_streams']._loaded_options = None
    _globals['_DISTRIBUTIONSTREAM'].fields_by_name['elementary_streams']._serialized_options = b'\xe0A\x02'
    _globals['_DISTRIBUTION'].fields_by_name['key']._loaded_options = None
    _globals['_DISTRIBUTION'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_DISTRIBUTION'].fields_by_name['distribution_stream']._loaded_options = None
    _globals['_DISTRIBUTION'].fields_by_name['distribution_stream']._serialized_options = b'\xe0A\x02'
    _globals['_DISTRIBUTION'].fields_by_name['state']._loaded_options = None
    _globals['_DISTRIBUTION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DISTRIBUTION'].fields_by_name['error']._loaded_options = None
    _globals['_DISTRIBUTION'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_SRTPUSHOUTPUTENDPOINT'].fields_by_name['uri']._loaded_options = None
    _globals['_SRTPUSHOUTPUTENDPOINT'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_SRTPUSHOUTPUTENDPOINT'].fields_by_name['passphrase_secret_version']._loaded_options = None
    _globals['_SRTPUSHOUTPUTENDPOINT'].fields_by_name['passphrase_secret_version']._serialized_options = b'\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_RTMPPUSHOUTPUTENDPOINT'].fields_by_name['uri']._loaded_options = None
    _globals['_RTMPPUSHOUTPUTENDPOINT'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_RTMPPUSHOUTPUTENDPOINT'].fields_by_name['stream_key']._loaded_options = None
    _globals['_RTMPPUSHOUTPUTENDPOINT'].fields_by_name['stream_key']._serialized_options = b'\xe0A\x02'
    _globals['_SPRITESHEET'].fields_by_name['file_prefix']._loaded_options = None
    _globals['_SPRITESHEET'].fields_by_name['file_prefix']._serialized_options = b'\xe0A\x02'
    _globals['_SPRITESHEET'].fields_by_name['sprite_width_pixels']._loaded_options = None
    _globals['_SPRITESHEET'].fields_by_name['sprite_width_pixels']._serialized_options = b'\xe0A\x02'
    _globals['_SPRITESHEET'].fields_by_name['sprite_height_pixels']._loaded_options = None
    _globals['_SPRITESHEET'].fields_by_name['sprite_height_pixels']._serialized_options = b'\xe0A\x02'
    _globals['_VIDEOSTREAM_H264CODECSETTINGS'].fields_by_name['frame_rate']._loaded_options = None
    _globals['_VIDEOSTREAM_H264CODECSETTINGS'].fields_by_name['frame_rate']._serialized_options = b'\xe0A\x02'
    _globals['_VIDEOSTREAM_H264CODECSETTINGS'].fields_by_name['bitrate_bps']._loaded_options = None
    _globals['_VIDEOSTREAM_H264CODECSETTINGS'].fields_by_name['bitrate_bps']._serialized_options = b'\xe0A\x02'
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['width_pixels']._loaded_options = None
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['width_pixels']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['height_pixels']._loaded_options = None
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['height_pixels']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['frame_rate']._loaded_options = None
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['frame_rate']._serialized_options = b'\xe0A\x02'
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['bitrate_bps']._loaded_options = None
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['bitrate_bps']._serialized_options = b'\xe0A\x02'
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['gop_frame_count']._loaded_options = None
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['gop_frame_count']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['gop_duration']._loaded_options = None
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['gop_duration']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['vbv_size_bits']._loaded_options = None
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['vbv_size_bits']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['vbv_fullness_bits']._loaded_options = None
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['vbv_fullness_bits']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['b_pyramid']._loaded_options = None
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['b_pyramid']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['b_frame_count']._loaded_options = None
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['b_frame_count']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['aq_strength']._loaded_options = None
    _globals['_VIDEOSTREAM_H265CODECSETTINGS'].fields_by_name['aq_strength']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['input_key']._loaded_options = None
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['input_key']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['input_track']._loaded_options = None
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['input_track']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['input_channel']._loaded_options = None
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['input_channel']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['output_channel']._loaded_options = None
    _globals['_AUDIOSTREAM_AUDIOMAPPING'].fields_by_name['output_channel']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIOSTREAM'].fields_by_name['bitrate_bps']._loaded_options = None
    _globals['_AUDIOSTREAM'].fields_by_name['bitrate_bps']._serialized_options = b'\xe0A\x02'
    _globals['_TEXTSTREAM_TEXTMAPPING'].fields_by_name['input_key']._loaded_options = None
    _globals['_TEXTSTREAM_TEXTMAPPING'].fields_by_name['input_key']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTSTREAM_TEXTMAPPING'].fields_by_name['input_track']._loaded_options = None
    _globals['_TEXTSTREAM_TEXTMAPPING'].fields_by_name['input_track']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTSTREAM_TEXTMAPPING'].fields_by_name['input_cea_channel']._loaded_options = None
    _globals['_TEXTSTREAM_TEXTMAPPING'].fields_by_name['input_cea_channel']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTSTREAM_TEXTMAPPING'].fields_by_name['from_language_code']._loaded_options = None
    _globals['_TEXTSTREAM_TEXTMAPPING'].fields_by_name['from_language_code']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTSTREAM'].fields_by_name['codec']._loaded_options = None
    _globals['_TEXTSTREAM'].fields_by_name['codec']._serialized_options = b'\xe0A\x02'
    _globals['_TEXTSTREAM'].fields_by_name['language_code']._loaded_options = None
    _globals['_TEXTSTREAM'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTSTREAM'].fields_by_name['display_name']._loaded_options = None
    _globals['_TEXTSTREAM'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTSTREAM'].fields_by_name['output_cea_channel']._loaded_options = None
    _globals['_TEXTSTREAM'].fields_by_name['output_cea_channel']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTSTREAM'].fields_by_name['mapping']._loaded_options = None
    _globals['_TEXTSTREAM'].fields_by_name['mapping']._serialized_options = b'\xe0A\x01'
    _globals['_ELEMENTARYSTREAM']._serialized_start = 230
    _globals['_ELEMENTARYSTREAM']._serialized_end = 493
    _globals['_MUXSTREAM']._serialized_start = 496
    _globals['_MUXSTREAM']._serialized_end = 667
    _globals['_MANIFEST']._serialized_start = 670
    _globals['_MANIFEST']._serialized_end = 1004
    _globals['_MANIFEST_MANIFESTTYPE']._serialized_start = 940
    _globals['_MANIFEST_MANIFESTTYPE']._serialized_end = 1004
    _globals['_DISTRIBUTIONSTREAM']._serialized_start = 1006
    _globals['_DISTRIBUTIONSTREAM']._serialized_end = 1101
    _globals['_DISTRIBUTION']._serialized_start = 1104
    _globals['_DISTRIBUTION']._serialized_end = 1559
    _globals['_DISTRIBUTION_STATE']._serialized_start = 1442
    _globals['_DISTRIBUTION_STATE']._serialized_end = 1547
    _globals['_SRTPUSHOUTPUTENDPOINT']._serialized_start = 1562
    _globals['_SRTPUSHOUTPUTENDPOINT']._serialized_end = 1710
    _globals['_RTMPPUSHOUTPUTENDPOINT']._serialized_start = 1712
    _globals['_RTMPPUSHOUTPUTENDPOINT']._serialized_end = 1779
    _globals['_SPRITESHEET']._serialized_start = 1782
    _globals['_SPRITESHEET']._serialized_end = 2009
    _globals['_PREPROCESSINGCONFIG']._serialized_start = 2012
    _globals['_PREPROCESSINGCONFIG']._serialized_end = 2465
    _globals['_PREPROCESSINGCONFIG_AUDIO']._serialized_start = 2257
    _globals['_PREPROCESSINGCONFIG_AUDIO']._serialized_end = 2278
    _globals['_PREPROCESSINGCONFIG_CROP']._serialized_start = 2280
    _globals['_PREPROCESSINGCONFIG_CROP']._serialized_end = 2372
    _globals['_PREPROCESSINGCONFIG_PAD']._serialized_start = 2374
    _globals['_PREPROCESSINGCONFIG_PAD']._serialized_end = 2465
    _globals['_VIDEOSTREAM']._serialized_start = 2468
    _globals['_VIDEOSTREAM']._serialized_end = 3426
    _globals['_VIDEOSTREAM_H264CODECSETTINGS']._serialized_start = 2646
    _globals['_VIDEOSTREAM_H264CODECSETTINGS']._serialized_end = 3042
    _globals['_VIDEOSTREAM_H265CODECSETTINGS']._serialized_start = 3045
    _globals['_VIDEOSTREAM_H265CODECSETTINGS']._serialized_end = 3408
    _globals['_AUDIOSTREAM']._serialized_start = 3429
    _globals['_AUDIOSTREAM']._serialized_end = 3793
    _globals['_AUDIOSTREAM_AUDIOMAPPING']._serialized_start = 3655
    _globals['_AUDIOSTREAM_AUDIOMAPPING']._serialized_end = 3793
    _globals['_TEXTSTREAM']._serialized_start = 3796
    _globals['_TEXTSTREAM']._serialized_end = 4127
    _globals['_TEXTSTREAM_TEXTMAPPING']._serialized_start = 3999
    _globals['_TEXTSTREAM_TEXTMAPPING']._serialized_end = 4127
    _globals['_SEGMENTSETTINGS']._serialized_start = 4129
    _globals['_SEGMENTSETTINGS']._serialized_end = 4199
    _globals['_TIMECODECONFIG']._serialized_start = 4202
    _globals['_TIMECODECONFIG']._serialized_end = 4502
    _globals['_TIMECODECONFIG_TIMECODESOURCE']._serialized_start = 4394
    _globals['_TIMECODECONFIG_TIMECODESOURCE']._serialized_end = 4487