"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/texttospeech/v1/cloud_tts_lrs.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.texttospeech.v1 import cloud_tts_pb2 as google_dot_cloud_dot_texttospeech_dot_v1_dot_cloud__tts__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/texttospeech/v1/cloud_tts_lrs.proto\x12\x1cgoogle.cloud.texttospeech.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/cloud/texttospeech/v1/cloud_tts.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x99\x02\n\x1aSynthesizeLongAudioRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12@\n\x05input\x18\x02 \x01(\x0b2,.google.cloud.texttospeech.v1.SynthesisInputB\x03\xe0A\x02\x12D\n\x0caudio_config\x18\x03 \x01(\x0b2).google.cloud.texttospeech.v1.AudioConfigB\x03\xe0A\x02\x12\x1b\n\x0eoutput_gcs_uri\x18\x04 \x01(\tB\x03\xe0A\x02\x12F\n\x05voice\x18\x05 \x01(\x0b22.google.cloud.texttospeech.v1.VoiceSelectionParamsB\x03\xe0A\x02"\x1d\n\x1bSynthesizeLongAudioResponse"\xa4\x01\n\x1bSynthesizeLongAudioMetadata\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x128\n\x10last_update_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x02\x18\x01\x12\x1b\n\x13progress_percentage\x18\x03 \x01(\x012\x9f\x03\n\x1fTextToSpeechLongAudioSynthesize\x12\xaa\x02\n\x13SynthesizeLongAudio\x128.google.cloud.texttospeech.v1.SynthesizeLongAudioRequest\x1a\x1d.google.longrunning.Operation"\xb9\x01\xcaAt\n8google.cloud.texttospeech.v1.SynthesizeLongAudioResponse\x128google.cloud.texttospeech.v1.SynthesizeLongAudioMetadata\x82\xd3\xe4\x93\x02<"7/v1/{parent=projects/*/locations/*}:synthesizeLongAudio:\x01*\x1aO\xcaA\x1btexttospeech.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xef\x01\n com.google.cloud.texttospeech.v1B#TextToSpeechLongAudioSynthesisProtoP\x01ZDcloud.google.com/go/texttospeech/apiv1/texttospeechpb;texttospeechpb\xaa\x02\x1cGoogle.Cloud.TextToSpeech.V1\xca\x02\x1cGoogle\\Cloud\\TextToSpeech\\V1\xea\x02\x1fGoogle::Cloud::TextToSpeech::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.texttospeech.v1.cloud_tts_lrs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.texttospeech.v1B#TextToSpeechLongAudioSynthesisProtoP\x01ZDcloud.google.com/go/texttospeech/apiv1/texttospeechpb;texttospeechpb\xaa\x02\x1cGoogle.Cloud.TextToSpeech.V1\xca\x02\x1cGoogle\\Cloud\\TextToSpeech\\V1\xea\x02\x1fGoogle::Cloud::TextToSpeech::V1'
    _globals['_SYNTHESIZELONGAUDIOREQUEST'].fields_by_name['input']._loaded_options = None
    _globals['_SYNTHESIZELONGAUDIOREQUEST'].fields_by_name['input']._serialized_options = b'\xe0A\x02'
    _globals['_SYNTHESIZELONGAUDIOREQUEST'].fields_by_name['audio_config']._loaded_options = None
    _globals['_SYNTHESIZELONGAUDIOREQUEST'].fields_by_name['audio_config']._serialized_options = b'\xe0A\x02'
    _globals['_SYNTHESIZELONGAUDIOREQUEST'].fields_by_name['output_gcs_uri']._loaded_options = None
    _globals['_SYNTHESIZELONGAUDIOREQUEST'].fields_by_name['output_gcs_uri']._serialized_options = b'\xe0A\x02'
    _globals['_SYNTHESIZELONGAUDIOREQUEST'].fields_by_name['voice']._loaded_options = None
    _globals['_SYNTHESIZELONGAUDIOREQUEST'].fields_by_name['voice']._serialized_options = b'\xe0A\x02'
    _globals['_SYNTHESIZELONGAUDIOMETADATA'].fields_by_name['last_update_time']._loaded_options = None
    _globals['_SYNTHESIZELONGAUDIOMETADATA'].fields_by_name['last_update_time']._serialized_options = b'\x18\x01'
    _globals['_TEXTTOSPEECHLONGAUDIOSYNTHESIZE']._loaded_options = None
    _globals['_TEXTTOSPEECHLONGAUDIOSYNTHESIZE']._serialized_options = b'\xcaA\x1btexttospeech.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_TEXTTOSPEECHLONGAUDIOSYNTHESIZE'].methods_by_name['SynthesizeLongAudio']._loaded_options = None
    _globals['_TEXTTOSPEECHLONGAUDIOSYNTHESIZE'].methods_by_name['SynthesizeLongAudio']._serialized_options = b'\xcaAt\n8google.cloud.texttospeech.v1.SynthesizeLongAudioResponse\x128google.cloud.texttospeech.v1.SynthesizeLongAudioMetadata\x82\xd3\xe4\x93\x02<"7/v1/{parent=projects/*/locations/*}:synthesizeLongAudio:\x01*'
    _globals['_SYNTHESIZELONGAUDIOREQUEST']._serialized_start = 287
    _globals['_SYNTHESIZELONGAUDIOREQUEST']._serialized_end = 568
    _globals['_SYNTHESIZELONGAUDIORESPONSE']._serialized_start = 570
    _globals['_SYNTHESIZELONGAUDIORESPONSE']._serialized_end = 599
    _globals['_SYNTHESIZELONGAUDIOMETADATA']._serialized_start = 602
    _globals['_SYNTHESIZELONGAUDIOMETADATA']._serialized_end = 766
    _globals['_TEXTTOSPEECHLONGAUDIOSYNTHESIZE']._serialized_start = 769
    _globals['_TEXTTOSPEECHLONGAUDIOSYNTHESIZE']._serialized_end = 1184