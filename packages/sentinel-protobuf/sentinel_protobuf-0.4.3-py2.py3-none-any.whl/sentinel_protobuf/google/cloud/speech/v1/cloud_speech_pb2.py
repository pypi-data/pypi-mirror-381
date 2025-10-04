"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/speech/v1/cloud_speech.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.speech.v1 import resource_pb2 as google_dot_cloud_dot_speech_dot_v1_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/speech/v1/cloud_speech.proto\x12\x16google.cloud.speech.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a%google/cloud/speech/v1/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto"\x90\x01\n\x10RecognizeRequest\x12>\n\x06config\x18\x01 \x01(\x0b2).google.cloud.speech.v1.RecognitionConfigB\x03\xe0A\x02\x12<\n\x05audio\x18\x02 \x01(\x0b2(.google.cloud.speech.v1.RecognitionAudioB\x03\xe0A\x02"\xe7\x01\n\x1bLongRunningRecognizeRequest\x12>\n\x06config\x18\x01 \x01(\x0b2).google.cloud.speech.v1.RecognitionConfigB\x03\xe0A\x02\x12<\n\x05audio\x18\x02 \x01(\x0b2(.google.cloud.speech.v1.RecognitionAudioB\x03\xe0A\x02\x12J\n\routput_config\x18\x04 \x01(\x0b2..google.cloud.speech.v1.TranscriptOutputConfigB\x03\xe0A\x01":\n\x16TranscriptOutputConfig\x12\x11\n\x07gcs_uri\x18\x01 \x01(\tH\x00B\r\n\x0boutput_type"\x99\x01\n\x19StreamingRecognizeRequest\x12N\n\x10streaming_config\x18\x01 \x01(\x0b22.google.cloud.speech.v1.StreamingRecognitionConfigH\x00\x12\x17\n\raudio_content\x18\x02 \x01(\x0cH\x00B\x13\n\x11streaming_request"\xa7\x03\n\x1aStreamingRecognitionConfig\x12>\n\x06config\x18\x01 \x01(\x0b2).google.cloud.speech.v1.RecognitionConfigB\x03\xe0A\x02\x12\x18\n\x10single_utterance\x18\x02 \x01(\x08\x12\x17\n\x0finterim_results\x18\x03 \x01(\x08\x12$\n\x1cenable_voice_activity_events\x18\x05 \x01(\x08\x12g\n\x16voice_activity_timeout\x18\x06 \x01(\x0b2G.google.cloud.speech.v1.StreamingRecognitionConfig.VoiceActivityTimeout\x1a\x86\x01\n\x14VoiceActivityTimeout\x127\n\x14speech_start_timeout\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x125\n\x12speech_end_timeout\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\xca\x08\n\x11RecognitionConfig\x12I\n\x08encoding\x18\x01 \x01(\x0e27.google.cloud.speech.v1.RecognitionConfig.AudioEncoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05\x12\x1b\n\x13audio_channel_count\x18\x07 \x01(\x05\x12/\n\'enable_separate_recognition_per_channel\x18\x0c \x01(\x08\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x02\x12"\n\x1aalternative_language_codes\x18\x12 \x03(\t\x12\x18\n\x10max_alternatives\x18\x04 \x01(\x05\x12\x18\n\x10profanity_filter\x18\x05 \x01(\x08\x12<\n\nadaptation\x18\x14 \x01(\x0b2(.google.cloud.speech.v1.SpeechAdaptation\x12V\n\x18transcript_normalization\x18\x18 \x01(\x0b2/.google.cloud.speech.v1.TranscriptNormalizationB\x03\xe0A\x01\x12>\n\x0fspeech_contexts\x18\x06 \x03(\x0b2%.google.cloud.speech.v1.SpeechContext\x12 \n\x18enable_word_time_offsets\x18\x08 \x01(\x08\x12\x1e\n\x16enable_word_confidence\x18\x0f \x01(\x08\x12$\n\x1cenable_automatic_punctuation\x18\x0b \x01(\x08\x12=\n\x19enable_spoken_punctuation\x18\x16 \x01(\x0b2\x1a.google.protobuf.BoolValue\x128\n\x14enable_spoken_emojis\x18\x17 \x01(\x0b2\x1a.google.protobuf.BoolValue\x12L\n\x12diarization_config\x18\x13 \x01(\x0b20.google.cloud.speech.v1.SpeakerDiarizationConfig\x12=\n\x08metadata\x18\t \x01(\x0b2+.google.cloud.speech.v1.RecognitionMetadata\x12\r\n\x05model\x18\r \x01(\t\x12\x14\n\x0cuse_enhanced\x18\x0e \x01(\x08"\xa3\x01\n\rAudioEncoding\x12\x18\n\x14ENCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08LINEAR16\x10\x01\x12\x08\n\x04FLAC\x10\x02\x12\t\n\x05MULAW\x10\x03\x12\x07\n\x03AMR\x10\x04\x12\n\n\x06AMR_WB\x10\x05\x12\x0c\n\x08OGG_OPUS\x10\x06\x12\x1a\n\x16SPEEX_WITH_HEADER_BYTE\x10\x07\x12\x07\n\x03MP3\x10\x08\x12\r\n\tWEBM_OPUS\x10\t"\x90\x01\n\x18SpeakerDiarizationConfig\x12"\n\x1aenable_speaker_diarization\x18\x01 \x01(\x08\x12\x19\n\x11min_speaker_count\x18\x02 \x01(\x05\x12\x19\n\x11max_speaker_count\x18\x03 \x01(\x05\x12\x1a\n\x0bspeaker_tag\x18\x05 \x01(\x05B\x05\x18\x01\xe0A\x03"\xa4\x08\n\x13RecognitionMetadata\x12U\n\x10interaction_type\x18\x01 \x01(\x0e2;.google.cloud.speech.v1.RecognitionMetadata.InteractionType\x12$\n\x1cindustry_naics_code_of_audio\x18\x03 \x01(\r\x12[\n\x13microphone_distance\x18\x04 \x01(\x0e2>.google.cloud.speech.v1.RecognitionMetadata.MicrophoneDistance\x12Z\n\x13original_media_type\x18\x05 \x01(\x0e2=.google.cloud.speech.v1.RecognitionMetadata.OriginalMediaType\x12^\n\x15recording_device_type\x18\x06 \x01(\x0e2?.google.cloud.speech.v1.RecognitionMetadata.RecordingDeviceType\x12\x1d\n\x15recording_device_name\x18\x07 \x01(\t\x12\x1a\n\x12original_mime_type\x18\x08 \x01(\t\x12\x13\n\x0baudio_topic\x18\n \x01(\t"\xc5\x01\n\x0fInteractionType\x12 \n\x1cINTERACTION_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nDISCUSSION\x10\x01\x12\x10\n\x0cPRESENTATION\x10\x02\x12\x0e\n\nPHONE_CALL\x10\x03\x12\r\n\tVOICEMAIL\x10\x04\x12\x1b\n\x17PROFESSIONALLY_PRODUCED\x10\x05\x12\x10\n\x0cVOICE_SEARCH\x10\x06\x12\x11\n\rVOICE_COMMAND\x10\x07\x12\r\n\tDICTATION\x10\x08"d\n\x12MicrophoneDistance\x12#\n\x1fMICROPHONE_DISTANCE_UNSPECIFIED\x10\x00\x12\r\n\tNEARFIELD\x10\x01\x12\x0c\n\x08MIDFIELD\x10\x02\x12\x0c\n\x08FARFIELD\x10\x03"N\n\x11OriginalMediaType\x12#\n\x1fORIGINAL_MEDIA_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05AUDIO\x10\x01\x12\t\n\x05VIDEO\x10\x02"\xa4\x01\n\x13RecordingDeviceType\x12%\n!RECORDING_DEVICE_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nSMARTPHONE\x10\x01\x12\x06\n\x02PC\x10\x02\x12\x0e\n\nPHONE_LINE\x10\x03\x12\x0b\n\x07VEHICLE\x10\x04\x12\x18\n\x14OTHER_OUTDOOR_DEVICE\x10\x05\x12\x17\n\x13OTHER_INDOOR_DEVICE\x10\x06:\x02\x18\x01"/\n\rSpeechContext\x12\x0f\n\x07phrases\x18\x01 \x03(\t\x12\r\n\x05boost\x18\x04 \x01(\x02"D\n\x10RecognitionAudio\x12\x11\n\x07content\x18\x01 \x01(\x0cH\x00\x12\r\n\x03uri\x18\x02 \x01(\tH\x00B\x0e\n\x0caudio_source"\xed\x01\n\x11RecognizeResponse\x12@\n\x07results\x18\x02 \x03(\x0b2/.google.cloud.speech.v1.SpeechRecognitionResult\x124\n\x11total_billed_time\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12L\n\x16speech_adaptation_info\x18\x07 \x01(\x0b2,.google.cloud.speech.v1.SpeechAdaptationInfo\x12\x12\n\nrequest_id\x18\x08 \x01(\x03"\xe9\x02\n\x1cLongRunningRecognizeResponse\x12@\n\x07results\x18\x02 \x03(\x0b2/.google.cloud.speech.v1.SpeechRecognitionResult\x124\n\x11total_billed_time\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12E\n\routput_config\x18\x06 \x01(\x0b2..google.cloud.speech.v1.TranscriptOutputConfig\x12(\n\x0coutput_error\x18\x07 \x01(\x0b2\x12.google.rpc.Status\x12L\n\x16speech_adaptation_info\x18\x08 \x01(\x0b2,.google.cloud.speech.v1.SpeechAdaptationInfo\x12\x12\n\nrequest_id\x18\t \x01(\x03"\xb0\x01\n\x1cLongRunningRecognizeMetadata\x12\x18\n\x10progress_percent\x18\x01 \x01(\x05\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10last_update_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x10\n\x03uri\x18\x04 \x01(\tB\x03\xe0A\x03"\xd1\x04\n\x1aStreamingRecognizeResponse\x12!\n\x05error\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12C\n\x07results\x18\x02 \x03(\x0b22.google.cloud.speech.v1.StreamingRecognitionResult\x12]\n\x11speech_event_type\x18\x04 \x01(\x0e2B.google.cloud.speech.v1.StreamingRecognizeResponse.SpeechEventType\x124\n\x11speech_event_time\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x124\n\x11total_billed_time\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration\x12L\n\x16speech_adaptation_info\x18\t \x01(\x0b2,.google.cloud.speech.v1.SpeechAdaptationInfo\x12\x12\n\nrequest_id\x18\n \x01(\x03"\x9d\x01\n\x0fSpeechEventType\x12\x1c\n\x18SPEECH_EVENT_UNSPECIFIED\x10\x00\x12\x1b\n\x17END_OF_SINGLE_UTTERANCE\x10\x01\x12\x19\n\x15SPEECH_ACTIVITY_BEGIN\x10\x02\x12\x17\n\x13SPEECH_ACTIVITY_END\x10\x03\x12\x1b\n\x17SPEECH_ACTIVITY_TIMEOUT\x10\x04"\xf2\x01\n\x1aStreamingRecognitionResult\x12J\n\x0calternatives\x18\x01 \x03(\x0b24.google.cloud.speech.v1.SpeechRecognitionAlternative\x12\x10\n\x08is_final\x18\x02 \x01(\x08\x12\x11\n\tstability\x18\x03 \x01(\x02\x122\n\x0fresult_end_time\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12\x13\n\x0bchannel_tag\x18\x05 \x01(\x05\x12\x1a\n\rlanguage_code\x18\x06 \x01(\tB\x03\xe0A\x03"\xca\x01\n\x17SpeechRecognitionResult\x12J\n\x0calternatives\x18\x01 \x03(\x0b24.google.cloud.speech.v1.SpeechRecognitionAlternative\x12\x13\n\x0bchannel_tag\x18\x02 \x01(\x05\x122\n\x0fresult_end_time\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12\x1a\n\rlanguage_code\x18\x05 \x01(\tB\x03\xe0A\x03"w\n\x1cSpeechRecognitionAlternative\x12\x12\n\ntranscript\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12/\n\x05words\x18\x03 \x03(\x0b2 .google.cloud.speech.v1.WordInfo"\xc0\x01\n\x08WordInfo\x12-\n\nstart_time\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12+\n\x08end_time\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12\x0c\n\x04word\x18\x03 \x01(\t\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x12\x1a\n\x0bspeaker_tag\x18\x05 \x01(\x05B\x05\x18\x01\xe0A\x03\x12\x1a\n\rspeaker_label\x18\x06 \x01(\tB\x03\xe0A\x03"K\n\x14SpeechAdaptationInfo\x12\x1a\n\x12adaptation_timeout\x18\x01 \x01(\x08\x12\x17\n\x0ftimeout_message\x18\x04 \x01(\t2\xd1\x04\n\x06Speech\x12\x90\x01\n\tRecognize\x12(.google.cloud.speech.v1.RecognizeRequest\x1a).google.cloud.speech.v1.RecognizeResponse".\xdaA\x0cconfig,audio\x82\xd3\xe4\x93\x02\x19"\x14/v1/speech:recognize:\x01*\x12\xe4\x01\n\x14LongRunningRecognize\x123.google.cloud.speech.v1.LongRunningRecognizeRequest\x1a\x1d.google.longrunning.Operation"x\xcaA<\n\x1cLongRunningRecognizeResponse\x12\x1cLongRunningRecognizeMetadata\xdaA\x0cconfig,audio\x82\xd3\xe4\x93\x02$"\x1f/v1/speech:longrunningrecognize:\x01*\x12\x81\x01\n\x12StreamingRecognize\x121.google.cloud.speech.v1.StreamingRecognizeRequest\x1a2.google.cloud.speech.v1.StreamingRecognizeResponse"\x00(\x010\x01\x1aI\xcaA\x15speech.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBh\n\x1acom.google.cloud.speech.v1B\x0bSpeechProtoP\x01Z2cloud.google.com/go/speech/apiv1/speechpb;speechpb\xf8\x01\x01\xa2\x02\x03GCSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.speech.v1.cloud_speech_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.speech.v1B\x0bSpeechProtoP\x01Z2cloud.google.com/go/speech/apiv1/speechpb;speechpb\xf8\x01\x01\xa2\x02\x03GCS'
    _globals['_RECOGNIZEREQUEST'].fields_by_name['config']._loaded_options = None
    _globals['_RECOGNIZEREQUEST'].fields_by_name['config']._serialized_options = b'\xe0A\x02'
    _globals['_RECOGNIZEREQUEST'].fields_by_name['audio']._loaded_options = None
    _globals['_RECOGNIZEREQUEST'].fields_by_name['audio']._serialized_options = b'\xe0A\x02'
    _globals['_LONGRUNNINGRECOGNIZEREQUEST'].fields_by_name['config']._loaded_options = None
    _globals['_LONGRUNNINGRECOGNIZEREQUEST'].fields_by_name['config']._serialized_options = b'\xe0A\x02'
    _globals['_LONGRUNNINGRECOGNIZEREQUEST'].fields_by_name['audio']._loaded_options = None
    _globals['_LONGRUNNINGRECOGNIZEREQUEST'].fields_by_name['audio']._serialized_options = b'\xe0A\x02'
    _globals['_LONGRUNNINGRECOGNIZEREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_LONGRUNNINGRECOGNIZEREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMINGRECOGNITIONCONFIG'].fields_by_name['config']._loaded_options = None
    _globals['_STREAMINGRECOGNITIONCONFIG'].fields_by_name['config']._serialized_options = b'\xe0A\x02'
    _globals['_RECOGNITIONCONFIG'].fields_by_name['language_code']._loaded_options = None
    _globals['_RECOGNITIONCONFIG'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_RECOGNITIONCONFIG'].fields_by_name['transcript_normalization']._loaded_options = None
    _globals['_RECOGNITIONCONFIG'].fields_by_name['transcript_normalization']._serialized_options = b'\xe0A\x01'
    _globals['_SPEAKERDIARIZATIONCONFIG'].fields_by_name['speaker_tag']._loaded_options = None
    _globals['_SPEAKERDIARIZATIONCONFIG'].fields_by_name['speaker_tag']._serialized_options = b'\x18\x01\xe0A\x03'
    _globals['_RECOGNITIONMETADATA']._loaded_options = None
    _globals['_RECOGNITIONMETADATA']._serialized_options = b'\x18\x01'
    _globals['_LONGRUNNINGRECOGNIZEMETADATA'].fields_by_name['uri']._loaded_options = None
    _globals['_LONGRUNNINGRECOGNIZEMETADATA'].fields_by_name['uri']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGRECOGNITIONRESULT'].fields_by_name['language_code']._loaded_options = None
    _globals['_STREAMINGRECOGNITIONRESULT'].fields_by_name['language_code']._serialized_options = b'\xe0A\x03'
    _globals['_SPEECHRECOGNITIONRESULT'].fields_by_name['language_code']._loaded_options = None
    _globals['_SPEECHRECOGNITIONRESULT'].fields_by_name['language_code']._serialized_options = b'\xe0A\x03'
    _globals['_WORDINFO'].fields_by_name['speaker_tag']._loaded_options = None
    _globals['_WORDINFO'].fields_by_name['speaker_tag']._serialized_options = b'\x18\x01\xe0A\x03'
    _globals['_WORDINFO'].fields_by_name['speaker_label']._loaded_options = None
    _globals['_WORDINFO'].fields_by_name['speaker_label']._serialized_options = b'\xe0A\x03'
    _globals['_SPEECH']._loaded_options = None
    _globals['_SPEECH']._serialized_options = b'\xcaA\x15speech.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SPEECH'].methods_by_name['Recognize']._loaded_options = None
    _globals['_SPEECH'].methods_by_name['Recognize']._serialized_options = b'\xdaA\x0cconfig,audio\x82\xd3\xe4\x93\x02\x19"\x14/v1/speech:recognize:\x01*'
    _globals['_SPEECH'].methods_by_name['LongRunningRecognize']._loaded_options = None
    _globals['_SPEECH'].methods_by_name['LongRunningRecognize']._serialized_options = b'\xcaA<\n\x1cLongRunningRecognizeResponse\x12\x1cLongRunningRecognizeMetadata\xdaA\x0cconfig,audio\x82\xd3\xe4\x93\x02$"\x1f/v1/speech:longrunningrecognize:\x01*'
    _globals['_RECOGNIZEREQUEST']._serialized_start = 356
    _globals['_RECOGNIZEREQUEST']._serialized_end = 500
    _globals['_LONGRUNNINGRECOGNIZEREQUEST']._serialized_start = 503
    _globals['_LONGRUNNINGRECOGNIZEREQUEST']._serialized_end = 734
    _globals['_TRANSCRIPTOUTPUTCONFIG']._serialized_start = 736
    _globals['_TRANSCRIPTOUTPUTCONFIG']._serialized_end = 794
    _globals['_STREAMINGRECOGNIZEREQUEST']._serialized_start = 797
    _globals['_STREAMINGRECOGNIZEREQUEST']._serialized_end = 950
    _globals['_STREAMINGRECOGNITIONCONFIG']._serialized_start = 953
    _globals['_STREAMINGRECOGNITIONCONFIG']._serialized_end = 1376
    _globals['_STREAMINGRECOGNITIONCONFIG_VOICEACTIVITYTIMEOUT']._serialized_start = 1242
    _globals['_STREAMINGRECOGNITIONCONFIG_VOICEACTIVITYTIMEOUT']._serialized_end = 1376
    _globals['_RECOGNITIONCONFIG']._serialized_start = 1379
    _globals['_RECOGNITIONCONFIG']._serialized_end = 2477
    _globals['_RECOGNITIONCONFIG_AUDIOENCODING']._serialized_start = 2314
    _globals['_RECOGNITIONCONFIG_AUDIOENCODING']._serialized_end = 2477
    _globals['_SPEAKERDIARIZATIONCONFIG']._serialized_start = 2480
    _globals['_SPEAKERDIARIZATIONCONFIG']._serialized_end = 2624
    _globals['_RECOGNITIONMETADATA']._serialized_start = 2627
    _globals['_RECOGNITIONMETADATA']._serialized_end = 3687
    _globals['_RECOGNITIONMETADATA_INTERACTIONTYPE']._serialized_start = 3137
    _globals['_RECOGNITIONMETADATA_INTERACTIONTYPE']._serialized_end = 3334
    _globals['_RECOGNITIONMETADATA_MICROPHONEDISTANCE']._serialized_start = 3336
    _globals['_RECOGNITIONMETADATA_MICROPHONEDISTANCE']._serialized_end = 3436
    _globals['_RECOGNITIONMETADATA_ORIGINALMEDIATYPE']._serialized_start = 3438
    _globals['_RECOGNITIONMETADATA_ORIGINALMEDIATYPE']._serialized_end = 3516
    _globals['_RECOGNITIONMETADATA_RECORDINGDEVICETYPE']._serialized_start = 3519
    _globals['_RECOGNITIONMETADATA_RECORDINGDEVICETYPE']._serialized_end = 3683
    _globals['_SPEECHCONTEXT']._serialized_start = 3689
    _globals['_SPEECHCONTEXT']._serialized_end = 3736
    _globals['_RECOGNITIONAUDIO']._serialized_start = 3738
    _globals['_RECOGNITIONAUDIO']._serialized_end = 3806
    _globals['_RECOGNIZERESPONSE']._serialized_start = 3809
    _globals['_RECOGNIZERESPONSE']._serialized_end = 4046
    _globals['_LONGRUNNINGRECOGNIZERESPONSE']._serialized_start = 4049
    _globals['_LONGRUNNINGRECOGNIZERESPONSE']._serialized_end = 4410
    _globals['_LONGRUNNINGRECOGNIZEMETADATA']._serialized_start = 4413
    _globals['_LONGRUNNINGRECOGNIZEMETADATA']._serialized_end = 4589
    _globals['_STREAMINGRECOGNIZERESPONSE']._serialized_start = 4592
    _globals['_STREAMINGRECOGNIZERESPONSE']._serialized_end = 5185
    _globals['_STREAMINGRECOGNIZERESPONSE_SPEECHEVENTTYPE']._serialized_start = 5028
    _globals['_STREAMINGRECOGNIZERESPONSE_SPEECHEVENTTYPE']._serialized_end = 5185
    _globals['_STREAMINGRECOGNITIONRESULT']._serialized_start = 5188
    _globals['_STREAMINGRECOGNITIONRESULT']._serialized_end = 5430
    _globals['_SPEECHRECOGNITIONRESULT']._serialized_start = 5433
    _globals['_SPEECHRECOGNITIONRESULT']._serialized_end = 5635
    _globals['_SPEECHRECOGNITIONALTERNATIVE']._serialized_start = 5637
    _globals['_SPEECHRECOGNITIONALTERNATIVE']._serialized_end = 5756
    _globals['_WORDINFO']._serialized_start = 5759
    _globals['_WORDINFO']._serialized_end = 5951
    _globals['_SPEECHADAPTATIONINFO']._serialized_start = 5953
    _globals['_SPEECHADAPTATIONINFO']._serialized_end = 6028
    _globals['_SPEECH']._serialized_start = 6031
    _globals['_SPEECH']._serialized_end = 6624