"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/visionai/v1/streams_resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/visionai/v1/streams_resources.proto\x12\x18google.cloud.visionai.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xaf\x04\n\x06Stream\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12<\n\x06labels\x18\x04 \x03(\x0b2,.google.cloud.visionai.v1.Stream.LabelsEntry\x12F\n\x0bannotations\x18\x05 \x03(\x0b21.google.cloud.visionai.v1.Stream.AnnotationsEntry\x12\x14\n\x0cdisplay_name\x18\x06 \x01(\t\x12\x1b\n\x13enable_hls_playback\x18\x07 \x01(\x08\x12\x1d\n\x15media_warehouse_asset\x18\x08 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:p\xeaAm\n\x1evisionai.googleapis.com/Stream\x12Kprojects/{project}/locations/{location}/clusters/{cluster}/streams/{stream}"\x81\x05\n\x05Event\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12;\n\x06labels\x18\x04 \x03(\x0b2+.google.cloud.visionai.v1.Event.LabelsEntry\x12E\n\x0bannotations\x18\x05 \x03(\x0b20.google.cloud.visionai.v1.Event.AnnotationsEntry\x12>\n\x0falignment_clock\x18\x06 \x01(\x0e2%.google.cloud.visionai.v1.Event.Clock\x12/\n\x0cgrace_period\x18\x07 \x01(\x0b2\x19.google.protobuf.Duration\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"7\n\x05Clock\x12\x15\n\x11CLOCK_UNSPECIFIED\x10\x00\x12\x0b\n\x07CAPTURE\x10\x01\x12\n\n\x06INGEST\x10\x02:m\xeaAj\n\x1dvisionai.googleapis.com/Event\x12Iprojects/{project}/locations/{location}/clusters/{cluster}/events/{event}"\xca\x04\n\x06Series\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12<\n\x06labels\x18\x04 \x03(\x0b2,.google.cloud.visionai.v1.Series.LabelsEntry\x12F\n\x0bannotations\x18\x05 \x03(\x0b21.google.cloud.visionai.v1.Series.AnnotationsEntry\x126\n\x06stream\x18\x06 \x01(\tB&\xe0A\x02\xfaA \n\x1evisionai.googleapis.com/Stream\x124\n\x05event\x18\x07 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dvisionai.googleapis.com/Event\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:o\xeaAl\n\x1evisionai.googleapis.com/Series\x12Jprojects/{project}/locations/{location}/clusters/{cluster}/series/{series}"\xd1\x04\n\x07Channel\x12\x0c\n\x04name\x18\x01 \x01(\t\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\x06labels\x18\x04 \x03(\x0b2-.google.cloud.visionai.v1.Channel.LabelsEntry\x12G\n\x0bannotations\x18\x05 \x03(\x0b22.google.cloud.visionai.v1.Channel.AnnotationsEntry\x126\n\x06stream\x18\x06 \x01(\tB&\xe0A\x02\xfaA \n\x1evisionai.googleapis.com/Stream\x124\n\x05event\x18\x07 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dvisionai.googleapis.com/Event\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:s\xeaAp\n\x1fvisionai.googleapis.com/Channel\x12Mprojects/{project}/locations/{location}/clusters/{cluster}/channels/{channel}B\xc5\x01\n\x1ccom.google.cloud.visionai.v1B\x15StreamsResourcesProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1.streams_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.visionai.v1B\x15StreamsResourcesProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1'
    _globals['_STREAM_LABELSENTRY']._loaded_options = None
    _globals['_STREAM_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_STREAM_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_STREAM_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_STREAM'].fields_by_name['create_time']._loaded_options = None
    _globals['_STREAM'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_STREAM'].fields_by_name['update_time']._loaded_options = None
    _globals['_STREAM'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_STREAM']._loaded_options = None
    _globals['_STREAM']._serialized_options = b'\xeaAm\n\x1evisionai.googleapis.com/Stream\x12Kprojects/{project}/locations/{location}/clusters/{cluster}/streams/{stream}'
    _globals['_EVENT_LABELSENTRY']._loaded_options = None
    _globals['_EVENT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_EVENT_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_EVENT_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_EVENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_EVENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_EVENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_EVENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_EVENT']._loaded_options = None
    _globals['_EVENT']._serialized_options = b'\xeaAj\n\x1dvisionai.googleapis.com/Event\x12Iprojects/{project}/locations/{location}/clusters/{cluster}/events/{event}'
    _globals['_SERIES_LABELSENTRY']._loaded_options = None
    _globals['_SERIES_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SERIES_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_SERIES_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_SERIES'].fields_by_name['create_time']._loaded_options = None
    _globals['_SERIES'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SERIES'].fields_by_name['update_time']._loaded_options = None
    _globals['_SERIES'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SERIES'].fields_by_name['stream']._loaded_options = None
    _globals['_SERIES'].fields_by_name['stream']._serialized_options = b'\xe0A\x02\xfaA \n\x1evisionai.googleapis.com/Stream'
    _globals['_SERIES'].fields_by_name['event']._loaded_options = None
    _globals['_SERIES'].fields_by_name['event']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dvisionai.googleapis.com/Event'
    _globals['_SERIES']._loaded_options = None
    _globals['_SERIES']._serialized_options = b'\xeaAl\n\x1evisionai.googleapis.com/Series\x12Jprojects/{project}/locations/{location}/clusters/{cluster}/series/{series}'
    _globals['_CHANNEL_LABELSENTRY']._loaded_options = None
    _globals['_CHANNEL_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CHANNEL_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_CHANNEL_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_CHANNEL'].fields_by_name['create_time']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNEL'].fields_by_name['update_time']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHANNEL'].fields_by_name['stream']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['stream']._serialized_options = b'\xe0A\x02\xfaA \n\x1evisionai.googleapis.com/Stream'
    _globals['_CHANNEL'].fields_by_name['event']._loaded_options = None
    _globals['_CHANNEL'].fields_by_name['event']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dvisionai.googleapis.com/Event'
    _globals['_CHANNEL']._loaded_options = None
    _globals['_CHANNEL']._serialized_options = b'\xeaAp\n\x1fvisionai.googleapis.com/Channel\x12Mprojects/{project}/locations/{location}/clusters/{cluster}/channels/{channel}'
    _globals['_STREAM']._serialized_start = 204
    _globals['_STREAM']._serialized_end = 763
    _globals['_STREAM_LABELSENTRY']._serialized_start = 552
    _globals['_STREAM_LABELSENTRY']._serialized_end = 597
    _globals['_STREAM_ANNOTATIONSENTRY']._serialized_start = 599
    _globals['_STREAM_ANNOTATIONSENTRY']._serialized_end = 649
    _globals['_EVENT']._serialized_start = 766
    _globals['_EVENT']._serialized_end = 1407
    _globals['_EVENT_LABELSENTRY']._serialized_start = 552
    _globals['_EVENT_LABELSENTRY']._serialized_end = 597
    _globals['_EVENT_ANNOTATIONSENTRY']._serialized_start = 599
    _globals['_EVENT_ANNOTATIONSENTRY']._serialized_end = 649
    _globals['_EVENT_CLOCK']._serialized_start = 1241
    _globals['_EVENT_CLOCK']._serialized_end = 1296
    _globals['_SERIES']._serialized_start = 1410
    _globals['_SERIES']._serialized_end = 1996
    _globals['_SERIES_LABELSENTRY']._serialized_start = 552
    _globals['_SERIES_LABELSENTRY']._serialized_end = 597
    _globals['_SERIES_ANNOTATIONSENTRY']._serialized_start = 599
    _globals['_SERIES_ANNOTATIONSENTRY']._serialized_end = 649
    _globals['_CHANNEL']._serialized_start = 1999
    _globals['_CHANNEL']._serialized_end = 2592
    _globals['_CHANNEL_LABELSENTRY']._serialized_start = 552
    _globals['_CHANNEL_LABELSENTRY']._serialized_end = 597
    _globals['_CHANNEL_ANNOTATIONSENTRY']._serialized_start = 599
    _globals['_CHANNEL_ANNOTATIONSENTRY']._serialized_end = 649