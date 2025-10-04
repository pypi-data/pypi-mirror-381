"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/devicestreaming/v1/adb_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/devicestreaming/v1/adb_service.proto\x12\x1fgoogle.cloud.devicestreaming.v1\x1a\x1fgoogle/api/field_behavior.proto"\xef\x01\n\rDeviceMessage\x12F\n\rstatus_update\x18\x01 \x01(\x0b2-.google.cloud.devicestreaming.v1.StatusUpdateH\x00\x12F\n\rstream_status\x18\x02 \x01(\x0b2-.google.cloud.devicestreaming.v1.StreamStatusH\x00\x12B\n\x0bstream_data\x18\x03 \x01(\x0b2+.google.cloud.devicestreaming.v1.StreamDataH\x00B\n\n\x08contents"\x93\x01\n\nAdbMessage\x125\n\x04open\x18\x01 \x01(\x0b2%.google.cloud.devicestreaming.v1.OpenH\x00\x12B\n\x0bstream_data\x18\x02 \x01(\x0b2+.google.cloud.devicestreaming.v1.StreamDataH\x00B\n\n\x08contents"\x9f\x03\n\x0cStatusUpdate\x12H\n\x05state\x18\x01 \x01(\x0e29.google.cloud.devicestreaming.v1.StatusUpdate.DeviceState\x12Q\n\nproperties\x18\x02 \x03(\x0b2=.google.cloud.devicestreaming.v1.StatusUpdate.PropertiesEntry\x12\x10\n\x08features\x18\x03 \x01(\t\x1a1\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xac\x01\n\x0bDeviceState\x12\x1c\n\x18DEVICE_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06DEVICE\x10\x01\x12\x0c\n\x08RECOVERY\x10\x02\x12\n\n\x06RESCUE\x10\x03\x12\x0c\n\x08SIDELOAD\x10\x04\x12\x0b\n\x07MISSING\x10\n\x12\x0b\n\x07OFFLINE\x10\x0b\x12\x10\n\x0cUNAUTHORIZED\x10\x0c\x12\x0f\n\x0bAUTHORIZING\x10\r\x12\x0e\n\nCONNECTING\x10\x0e"\x99\x01\n\x0cStreamStatus\x12\x11\n\tstream_id\x18\x01 \x01(\x05\x125\n\x04okay\x18\x02 \x01(\x0b2%.google.cloud.devicestreaming.v1.OkayH\x00\x125\n\x04fail\x18\x03 \x01(\x0b2%.google.cloud.devicestreaming.v1.FailH\x00B\x08\n\x06status"4\n\x04Open\x12\x16\n\tstream_id\x18\x01 \x01(\x05B\x03\xe0A\x02\x12\x14\n\x07service\x18\x02 \x01(\tB\x03\xe0A\x01"y\n\nStreamData\x12\x16\n\tstream_id\x18\x01 \x01(\x05B\x03\xe0A\x02\x12\x0e\n\x04data\x18\x02 \x01(\x0cH\x00\x127\n\x05close\x18\x03 \x01(\x0b2&.google.cloud.devicestreaming.v1.CloseH\x00B\n\n\x08contents"\x06\n\x04Okay"\x16\n\x04Fail\x12\x0e\n\x06reason\x18\x01 \x01(\t"\x07\n\x05CloseB\xf0\x01\n#com.google.cloud.devicestreaming.v1B\x0fAdbServiceProtoP\x01ZMcloud.google.com/go/devicestreaming/apiv1/devicestreamingpb;devicestreamingpb\xaa\x02\x1fGoogle.Cloud.DeviceStreaming.V1\xca\x02\x1fGoogle\\Cloud\\DeviceStreaming\\V1\xea\x02"Google::Cloud::DeviceStreaming::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.devicestreaming.v1.adb_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.devicestreaming.v1B\x0fAdbServiceProtoP\x01ZMcloud.google.com/go/devicestreaming/apiv1/devicestreamingpb;devicestreamingpb\xaa\x02\x1fGoogle.Cloud.DeviceStreaming.V1\xca\x02\x1fGoogle\\Cloud\\DeviceStreaming\\V1\xea\x02"Google::Cloud::DeviceStreaming::V1'
    _globals['_STATUSUPDATE_PROPERTIESENTRY']._loaded_options = None
    _globals['_STATUSUPDATE_PROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_OPEN'].fields_by_name['stream_id']._loaded_options = None
    _globals['_OPEN'].fields_by_name['stream_id']._serialized_options = b'\xe0A\x02'
    _globals['_OPEN'].fields_by_name['service']._loaded_options = None
    _globals['_OPEN'].fields_by_name['service']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMDATA'].fields_by_name['stream_id']._loaded_options = None
    _globals['_STREAMDATA'].fields_by_name['stream_id']._serialized_options = b'\xe0A\x02'
    _globals['_DEVICEMESSAGE']._serialized_start = 120
    _globals['_DEVICEMESSAGE']._serialized_end = 359
    _globals['_ADBMESSAGE']._serialized_start = 362
    _globals['_ADBMESSAGE']._serialized_end = 509
    _globals['_STATUSUPDATE']._serialized_start = 512
    _globals['_STATUSUPDATE']._serialized_end = 927
    _globals['_STATUSUPDATE_PROPERTIESENTRY']._serialized_start = 703
    _globals['_STATUSUPDATE_PROPERTIESENTRY']._serialized_end = 752
    _globals['_STATUSUPDATE_DEVICESTATE']._serialized_start = 755
    _globals['_STATUSUPDATE_DEVICESTATE']._serialized_end = 927
    _globals['_STREAMSTATUS']._serialized_start = 930
    _globals['_STREAMSTATUS']._serialized_end = 1083
    _globals['_OPEN']._serialized_start = 1085
    _globals['_OPEN']._serialized_end = 1137
    _globals['_STREAMDATA']._serialized_start = 1139
    _globals['_STREAMDATA']._serialized_end = 1260
    _globals['_OKAY']._serialized_start = 1262
    _globals['_OKAY']._serialized_end = 1268
    _globals['_FAIL']._serialized_start = 1270
    _globals['_FAIL']._serialized_end = 1292
    _globals['_CLOSE']._serialized_start = 1294
    _globals['_CLOSE']._serialized_end = 1301