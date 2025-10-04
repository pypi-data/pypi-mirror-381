"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/texttospeech/v1/cloud_tts.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/texttospeech/v1/cloud_tts.proto\x12\x1cgoogle.cloud.texttospeech.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"/\n\x11ListVoicesRequest\x12\x1a\n\rlanguage_code\x18\x01 \x01(\tB\x03\xe0A\x01"I\n\x12ListVoicesResponse\x123\n\x06voices\x18\x01 \x03(\x0b2#.google.cloud.texttospeech.v1.Voice"\x94\x01\n\x05Voice\x12\x16\n\x0elanguage_codes\x18\x01 \x03(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12B\n\x0bssml_gender\x18\x03 \x01(\x0e2-.google.cloud.texttospeech.v1.SsmlVoiceGender\x12!\n\x19natural_sample_rate_hertz\x18\x04 \x01(\x05"d\n\x14AdvancedVoiceOptions\x12*\n\x1dlow_latency_journey_synthesis\x18\x01 \x01(\x08H\x00\x88\x01\x01B \n\x1e_low_latency_journey_synthesis"\xdd\x02\n\x17SynthesizeSpeechRequest\x12@\n\x05input\x18\x01 \x01(\x0b2,.google.cloud.texttospeech.v1.SynthesisInputB\x03\xe0A\x02\x12F\n\x05voice\x18\x02 \x01(\x0b22.google.cloud.texttospeech.v1.VoiceSelectionParamsB\x03\xe0A\x02\x12D\n\x0caudio_config\x18\x03 \x01(\x0b2).google.cloud.texttospeech.v1.AudioConfigB\x03\xe0A\x02\x12W\n\x16advanced_voice_options\x18\x08 \x01(\x0b22.google.cloud.texttospeech.v1.AdvancedVoiceOptionsH\x00\x88\x01\x01B\x19\n\x17_advanced_voice_options"\xa2\x03\n\x19CustomPronunciationParams\x12\x13\n\x06phrase\x18\x01 \x01(\tH\x00\x88\x01\x01\x12h\n\x11phonetic_encoding\x18\x02 \x01(\x0e2H.google.cloud.texttospeech.v1.CustomPronunciationParams.PhoneticEncodingH\x01\x88\x01\x01\x12\x1a\n\rpronunciation\x18\x03 \x01(\tH\x02\x88\x01\x01"\xb6\x01\n\x10PhoneticEncoding\x12!\n\x1dPHONETIC_ENCODING_UNSPECIFIED\x10\x00\x12\x19\n\x15PHONETIC_ENCODING_IPA\x10\x01\x12\x1d\n\x19PHONETIC_ENCODING_X_SAMPA\x10\x02\x12\'\n#PHONETIC_ENCODING_JAPANESE_YOMIGANA\x10\x03\x12\x1c\n\x18PHONETIC_ENCODING_PINYIN\x10\x04B\t\n\x07_phraseB\x14\n\x12_phonetic_encodingB\x10\n\x0e_pronunciation"g\n\x14CustomPronunciations\x12O\n\x0epronunciations\x18\x01 \x03(\x0b27.google.cloud.texttospeech.v1.CustomPronunciationParams"\x90\x01\n\x12MultiSpeakerMarkup\x12I\n\x05turns\x18\x01 \x03(\x0b25.google.cloud.texttospeech.v1.MultiSpeakerMarkup.TurnB\x03\xe0A\x02\x1a/\n\x04Turn\x12\x14\n\x07speaker\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04text\x18\x02 \x01(\tB\x03\xe0A\x02"P\n\x19MultispeakerPrebuiltVoice\x12\x1a\n\rspeaker_alias\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nspeaker_id\x18\x02 \x01(\tB\x03\xe0A\x02"v\n\x17MultiSpeakerVoiceConfig\x12[\n\x15speaker_voice_configs\x18\x02 \x03(\x0b27.google.cloud.texttospeech.v1.MultispeakerPrebuiltVoiceB\x03\xe0A\x02"\x9c\x02\n\x0eSynthesisInput\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12\x10\n\x06markup\x18\x05 \x01(\tH\x00\x12\x0e\n\x04ssml\x18\x02 \x01(\tH\x00\x12P\n\x14multi_speaker_markup\x18\x04 \x01(\x0b20.google.cloud.texttospeech.v1.MultiSpeakerMarkupH\x00\x12\x13\n\x06prompt\x18\x06 \x01(\tH\x01\x88\x01\x01\x12V\n\x15custom_pronunciations\x18\x03 \x01(\x0b22.google.cloud.texttospeech.v1.CustomPronunciationsB\x03\xe0A\x01B\x0e\n\x0cinput_sourceB\t\n\x07_prompt"\x8e\x03\n\x14VoiceSelectionParams\x12\x1a\n\rlanguage_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0c\n\x04name\x18\x02 \x01(\t\x12B\n\x0bssml_gender\x18\x03 \x01(\x0e2-.google.cloud.texttospeech.v1.SsmlVoiceGender\x12E\n\x0ccustom_voice\x18\x04 \x01(\x0b2/.google.cloud.texttospeech.v1.CustomVoiceParams\x12H\n\x0bvoice_clone\x18\x05 \x01(\x0b2..google.cloud.texttospeech.v1.VoiceCloneParamsB\x03\xe0A\x01\x12\x17\n\nmodel_name\x18\x06 \x01(\tB\x03\xe0A\x01\x12^\n\x1amulti_speaker_voice_config\x18\x07 \x01(\x0b25.google.cloud.texttospeech.v1.MultiSpeakerVoiceConfigB\x03\xe0A\x01"\xf1\x01\n\x0bAudioConfig\x12H\n\x0eaudio_encoding\x18\x01 \x01(\x0e2+.google.cloud.texttospeech.v1.AudioEncodingB\x03\xe0A\x02\x12\x1d\n\rspeaking_rate\x18\x02 \x01(\x01B\x06\xe0A\x04\xe0A\x01\x12\x15\n\x05pitch\x18\x03 \x01(\x01B\x06\xe0A\x04\xe0A\x01\x12\x1e\n\x0evolume_gain_db\x18\x04 \x01(\x01B\x06\xe0A\x04\xe0A\x01\x12\x1e\n\x11sample_rate_hertz\x18\x05 \x01(\x05B\x03\xe0A\x01\x12"\n\x12effects_profile_id\x18\x06 \x03(\tB\x06\xe0A\x04\xe0A\x01"\xf1\x01\n\x11CustomVoiceParams\x122\n\x05model\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model\x12\\\n\x0ereported_usage\x18\x03 \x01(\x0e2=.google.cloud.texttospeech.v1.CustomVoiceParams.ReportedUsageB\x05\x18\x01\xe0A\x01"J\n\rReportedUsage\x12\x1e\n\x1aREPORTED_USAGE_UNSPECIFIED\x10\x00\x12\x0c\n\x08REALTIME\x10\x01\x12\x0b\n\x07OFFLINE\x10\x02"2\n\x10VoiceCloneParams\x12\x1e\n\x11voice_cloning_key\x18\x01 \x01(\tB\x03\xe0A\x02"1\n\x18SynthesizeSpeechResponse\x12\x15\n\raudio_content\x18\x01 \x01(\x0c"\x9f\x01\n\x14StreamingAudioConfig\x12H\n\x0eaudio_encoding\x18\x01 \x01(\x0e2+.google.cloud.texttospeech.v1.AudioEncodingB\x03\xe0A\x02\x12\x1e\n\x11sample_rate_hertz\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x1d\n\rspeaking_rate\x18\x03 \x01(\x01B\x06\xe0A\x04\xe0A\x01"\x94\x02\n\x19StreamingSynthesizeConfig\x12F\n\x05voice\x18\x01 \x01(\x0b22.google.cloud.texttospeech.v1.VoiceSelectionParamsB\x03\xe0A\x02\x12W\n\x16streaming_audio_config\x18\x04 \x01(\x0b22.google.cloud.texttospeech.v1.StreamingAudioConfigB\x03\xe0A\x01\x12V\n\x15custom_pronunciations\x18\x05 \x01(\x0b22.google.cloud.texttospeech.v1.CustomPronunciationsB\x03\xe0A\x01"\xbd\x01\n\x17StreamingSynthesisInput\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12\x10\n\x06markup\x18\x05 \x01(\tH\x00\x12P\n\x14multi_speaker_markup\x18\x07 \x01(\x0b20.google.cloud.texttospeech.v1.MultiSpeakerMarkupH\x00\x12\x13\n\x06prompt\x18\x06 \x01(\tH\x01\x88\x01\x01B\x0e\n\x0cinput_sourceB\t\n\x07_prompt"\xce\x01\n\x1aStreamingSynthesizeRequest\x12S\n\x10streaming_config\x18\x01 \x01(\x0b27.google.cloud.texttospeech.v1.StreamingSynthesizeConfigH\x00\x12F\n\x05input\x18\x02 \x01(\x0b25.google.cloud.texttospeech.v1.StreamingSynthesisInputH\x00B\x13\n\x11streaming_request"4\n\x1bStreamingSynthesizeResponse\x12\x15\n\raudio_content\x18\x01 \x01(\x0c*W\n\x0fSsmlVoiceGender\x12!\n\x1dSSML_VOICE_GENDER_UNSPECIFIED\x10\x00\x12\x08\n\x04MALE\x10\x01\x12\n\n\x06FEMALE\x10\x02\x12\x0b\n\x07NEUTRAL\x10\x03*{\n\rAudioEncoding\x12\x1e\n\x1aAUDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08LINEAR16\x10\x01\x12\x07\n\x03MP3\x10\x02\x12\x0c\n\x08OGG_OPUS\x10\x03\x12\t\n\x05MULAW\x10\x05\x12\x08\n\x04ALAW\x10\x06\x12\x07\n\x03PCM\x10\x07\x12\x07\n\x03M4A\x10\x082\xc7\x04\n\x0cTextToSpeech\x12\x93\x01\n\nListVoices\x12/.google.cloud.texttospeech.v1.ListVoicesRequest\x1a0.google.cloud.texttospeech.v1.ListVoicesResponse""\xdaA\rlanguage_code\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/voices\x12\xbc\x01\n\x10SynthesizeSpeech\x125.google.cloud.texttospeech.v1.SynthesizeSpeechRequest\x1a6.google.cloud.texttospeech.v1.SynthesizeSpeechResponse"9\xdaA\x18input,voice,audio_config\x82\xd3\xe4\x93\x02\x18"\x13/v1/text:synthesize:\x01*\x12\x90\x01\n\x13StreamingSynthesize\x128.google.cloud.texttospeech.v1.StreamingSynthesizeRequest\x1a9.google.cloud.texttospeech.v1.StreamingSynthesizeResponse"\x00(\x010\x01\x1aO\xcaA\x1btexttospeech.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xbc\x02\n com.google.cloud.texttospeech.v1B\x11TextToSpeechProtoP\x01ZDcloud.google.com/go/texttospeech/apiv1/texttospeechpb;texttospeechpb\xa2\x02\x04CTTS\xaa\x02\x1cGoogle.Cloud.TextToSpeech.V1\xca\x02\x1cGoogle\\Cloud\\TextToSpeech\\V1\xea\x02\x1fGoogle::Cloud::TextToSpeech::V1\xeaAU\n\x1bautoml.googleapis.com/Model\x126projects/{project}/locations/{location}/models/{model}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.texttospeech.v1.cloud_tts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.texttospeech.v1B\x11TextToSpeechProtoP\x01ZDcloud.google.com/go/texttospeech/apiv1/texttospeechpb;texttospeechpb\xa2\x02\x04CTTS\xaa\x02\x1cGoogle.Cloud.TextToSpeech.V1\xca\x02\x1cGoogle\\Cloud\\TextToSpeech\\V1\xea\x02\x1fGoogle::Cloud::TextToSpeech::V1\xeaAU\n\x1bautoml.googleapis.com/Model\x126projects/{project}/locations/{location}/models/{model}'
    _globals['_LISTVOICESREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_LISTVOICESREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_SYNTHESIZESPEECHREQUEST'].fields_by_name['input']._loaded_options = None
    _globals['_SYNTHESIZESPEECHREQUEST'].fields_by_name['input']._serialized_options = b'\xe0A\x02'
    _globals['_SYNTHESIZESPEECHREQUEST'].fields_by_name['voice']._loaded_options = None
    _globals['_SYNTHESIZESPEECHREQUEST'].fields_by_name['voice']._serialized_options = b'\xe0A\x02'
    _globals['_SYNTHESIZESPEECHREQUEST'].fields_by_name['audio_config']._loaded_options = None
    _globals['_SYNTHESIZESPEECHREQUEST'].fields_by_name['audio_config']._serialized_options = b'\xe0A\x02'
    _globals['_MULTISPEAKERMARKUP_TURN'].fields_by_name['speaker']._loaded_options = None
    _globals['_MULTISPEAKERMARKUP_TURN'].fields_by_name['speaker']._serialized_options = b'\xe0A\x02'
    _globals['_MULTISPEAKERMARKUP_TURN'].fields_by_name['text']._loaded_options = None
    _globals['_MULTISPEAKERMARKUP_TURN'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_MULTISPEAKERMARKUP'].fields_by_name['turns']._loaded_options = None
    _globals['_MULTISPEAKERMARKUP'].fields_by_name['turns']._serialized_options = b'\xe0A\x02'
    _globals['_MULTISPEAKERPREBUILTVOICE'].fields_by_name['speaker_alias']._loaded_options = None
    _globals['_MULTISPEAKERPREBUILTVOICE'].fields_by_name['speaker_alias']._serialized_options = b'\xe0A\x02'
    _globals['_MULTISPEAKERPREBUILTVOICE'].fields_by_name['speaker_id']._loaded_options = None
    _globals['_MULTISPEAKERPREBUILTVOICE'].fields_by_name['speaker_id']._serialized_options = b'\xe0A\x02'
    _globals['_MULTISPEAKERVOICECONFIG'].fields_by_name['speaker_voice_configs']._loaded_options = None
    _globals['_MULTISPEAKERVOICECONFIG'].fields_by_name['speaker_voice_configs']._serialized_options = b'\xe0A\x02'
    _globals['_SYNTHESISINPUT'].fields_by_name['custom_pronunciations']._loaded_options = None
    _globals['_SYNTHESISINPUT'].fields_by_name['custom_pronunciations']._serialized_options = b'\xe0A\x01'
    _globals['_VOICESELECTIONPARAMS'].fields_by_name['language_code']._loaded_options = None
    _globals['_VOICESELECTIONPARAMS'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_VOICESELECTIONPARAMS'].fields_by_name['voice_clone']._loaded_options = None
    _globals['_VOICESELECTIONPARAMS'].fields_by_name['voice_clone']._serialized_options = b'\xe0A\x01'
    _globals['_VOICESELECTIONPARAMS'].fields_by_name['model_name']._loaded_options = None
    _globals['_VOICESELECTIONPARAMS'].fields_by_name['model_name']._serialized_options = b'\xe0A\x01'
    _globals['_VOICESELECTIONPARAMS'].fields_by_name['multi_speaker_voice_config']._loaded_options = None
    _globals['_VOICESELECTIONPARAMS'].fields_by_name['multi_speaker_voice_config']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIOCONFIG'].fields_by_name['audio_encoding']._loaded_options = None
    _globals['_AUDIOCONFIG'].fields_by_name['audio_encoding']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIOCONFIG'].fields_by_name['speaking_rate']._loaded_options = None
    _globals['_AUDIOCONFIG'].fields_by_name['speaking_rate']._serialized_options = b'\xe0A\x04\xe0A\x01'
    _globals['_AUDIOCONFIG'].fields_by_name['pitch']._loaded_options = None
    _globals['_AUDIOCONFIG'].fields_by_name['pitch']._serialized_options = b'\xe0A\x04\xe0A\x01'
    _globals['_AUDIOCONFIG'].fields_by_name['volume_gain_db']._loaded_options = None
    _globals['_AUDIOCONFIG'].fields_by_name['volume_gain_db']._serialized_options = b'\xe0A\x04\xe0A\x01'
    _globals['_AUDIOCONFIG'].fields_by_name['sample_rate_hertz']._loaded_options = None
    _globals['_AUDIOCONFIG'].fields_by_name['sample_rate_hertz']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIOCONFIG'].fields_by_name['effects_profile_id']._loaded_options = None
    _globals['_AUDIOCONFIG'].fields_by_name['effects_profile_id']._serialized_options = b'\xe0A\x04\xe0A\x01'
    _globals['_CUSTOMVOICEPARAMS'].fields_by_name['model']._loaded_options = None
    _globals['_CUSTOMVOICEPARAMS'].fields_by_name['model']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bautoml.googleapis.com/Model'
    _globals['_CUSTOMVOICEPARAMS'].fields_by_name['reported_usage']._loaded_options = None
    _globals['_CUSTOMVOICEPARAMS'].fields_by_name['reported_usage']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_VOICECLONEPARAMS'].fields_by_name['voice_cloning_key']._loaded_options = None
    _globals['_VOICECLONEPARAMS'].fields_by_name['voice_cloning_key']._serialized_options = b'\xe0A\x02'
    _globals['_STREAMINGAUDIOCONFIG'].fields_by_name['audio_encoding']._loaded_options = None
    _globals['_STREAMINGAUDIOCONFIG'].fields_by_name['audio_encoding']._serialized_options = b'\xe0A\x02'
    _globals['_STREAMINGAUDIOCONFIG'].fields_by_name['sample_rate_hertz']._loaded_options = None
    _globals['_STREAMINGAUDIOCONFIG'].fields_by_name['sample_rate_hertz']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMINGAUDIOCONFIG'].fields_by_name['speaking_rate']._loaded_options = None
    _globals['_STREAMINGAUDIOCONFIG'].fields_by_name['speaking_rate']._serialized_options = b'\xe0A\x04\xe0A\x01'
    _globals['_STREAMINGSYNTHESIZECONFIG'].fields_by_name['voice']._loaded_options = None
    _globals['_STREAMINGSYNTHESIZECONFIG'].fields_by_name['voice']._serialized_options = b'\xe0A\x02'
    _globals['_STREAMINGSYNTHESIZECONFIG'].fields_by_name['streaming_audio_config']._loaded_options = None
    _globals['_STREAMINGSYNTHESIZECONFIG'].fields_by_name['streaming_audio_config']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMINGSYNTHESIZECONFIG'].fields_by_name['custom_pronunciations']._loaded_options = None
    _globals['_STREAMINGSYNTHESIZECONFIG'].fields_by_name['custom_pronunciations']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTTOSPEECH']._loaded_options = None
    _globals['_TEXTTOSPEECH']._serialized_options = b'\xcaA\x1btexttospeech.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_TEXTTOSPEECH'].methods_by_name['ListVoices']._loaded_options = None
    _globals['_TEXTTOSPEECH'].methods_by_name['ListVoices']._serialized_options = b'\xdaA\rlanguage_code\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/voices'
    _globals['_TEXTTOSPEECH'].methods_by_name['SynthesizeSpeech']._loaded_options = None
    _globals['_TEXTTOSPEECH'].methods_by_name['SynthesizeSpeech']._serialized_options = b'\xdaA\x18input,voice,audio_config\x82\xd3\xe4\x93\x02\x18"\x13/v1/text:synthesize:\x01*'
    _globals['_SSMLVOICEGENDER']._serialized_start = 3972
    _globals['_SSMLVOICEGENDER']._serialized_end = 4059
    _globals['_AUDIOENCODING']._serialized_start = 4061
    _globals['_AUDIOENCODING']._serialized_end = 4184
    _globals['_LISTVOICESREQUEST']._serialized_start = 193
    _globals['_LISTVOICESREQUEST']._serialized_end = 240
    _globals['_LISTVOICESRESPONSE']._serialized_start = 242
    _globals['_LISTVOICESRESPONSE']._serialized_end = 315
    _globals['_VOICE']._serialized_start = 318
    _globals['_VOICE']._serialized_end = 466
    _globals['_ADVANCEDVOICEOPTIONS']._serialized_start = 468
    _globals['_ADVANCEDVOICEOPTIONS']._serialized_end = 568
    _globals['_SYNTHESIZESPEECHREQUEST']._serialized_start = 571
    _globals['_SYNTHESIZESPEECHREQUEST']._serialized_end = 920
    _globals['_CUSTOMPRONUNCIATIONPARAMS']._serialized_start = 923
    _globals['_CUSTOMPRONUNCIATIONPARAMS']._serialized_end = 1341
    _globals['_CUSTOMPRONUNCIATIONPARAMS_PHONETICENCODING']._serialized_start = 1108
    _globals['_CUSTOMPRONUNCIATIONPARAMS_PHONETICENCODING']._serialized_end = 1290
    _globals['_CUSTOMPRONUNCIATIONS']._serialized_start = 1343
    _globals['_CUSTOMPRONUNCIATIONS']._serialized_end = 1446
    _globals['_MULTISPEAKERMARKUP']._serialized_start = 1449
    _globals['_MULTISPEAKERMARKUP']._serialized_end = 1593
    _globals['_MULTISPEAKERMARKUP_TURN']._serialized_start = 1546
    _globals['_MULTISPEAKERMARKUP_TURN']._serialized_end = 1593
    _globals['_MULTISPEAKERPREBUILTVOICE']._serialized_start = 1595
    _globals['_MULTISPEAKERPREBUILTVOICE']._serialized_end = 1675
    _globals['_MULTISPEAKERVOICECONFIG']._serialized_start = 1677
    _globals['_MULTISPEAKERVOICECONFIG']._serialized_end = 1795
    _globals['_SYNTHESISINPUT']._serialized_start = 1798
    _globals['_SYNTHESISINPUT']._serialized_end = 2082
    _globals['_VOICESELECTIONPARAMS']._serialized_start = 2085
    _globals['_VOICESELECTIONPARAMS']._serialized_end = 2483
    _globals['_AUDIOCONFIG']._serialized_start = 2486
    _globals['_AUDIOCONFIG']._serialized_end = 2727
    _globals['_CUSTOMVOICEPARAMS']._serialized_start = 2730
    _globals['_CUSTOMVOICEPARAMS']._serialized_end = 2971
    _globals['_CUSTOMVOICEPARAMS_REPORTEDUSAGE']._serialized_start = 2897
    _globals['_CUSTOMVOICEPARAMS_REPORTEDUSAGE']._serialized_end = 2971
    _globals['_VOICECLONEPARAMS']._serialized_start = 2973
    _globals['_VOICECLONEPARAMS']._serialized_end = 3023
    _globals['_SYNTHESIZESPEECHRESPONSE']._serialized_start = 3025
    _globals['_SYNTHESIZESPEECHRESPONSE']._serialized_end = 3074
    _globals['_STREAMINGAUDIOCONFIG']._serialized_start = 3077
    _globals['_STREAMINGAUDIOCONFIG']._serialized_end = 3236
    _globals['_STREAMINGSYNTHESIZECONFIG']._serialized_start = 3239
    _globals['_STREAMINGSYNTHESIZECONFIG']._serialized_end = 3515
    _globals['_STREAMINGSYNTHESISINPUT']._serialized_start = 3518
    _globals['_STREAMINGSYNTHESISINPUT']._serialized_end = 3707
    _globals['_STREAMINGSYNTHESIZEREQUEST']._serialized_start = 3710
    _globals['_STREAMINGSYNTHESIZEREQUEST']._serialized_end = 3916
    _globals['_STREAMINGSYNTHESIZERESPONSE']._serialized_start = 3918
    _globals['_STREAMINGSYNTHESIZERESPONSE']._serialized_end = 3970
    _globals['_TEXTTOSPEECH']._serialized_start = 4187
    _globals['_TEXTTOSPEECH']._serialized_end = 4770