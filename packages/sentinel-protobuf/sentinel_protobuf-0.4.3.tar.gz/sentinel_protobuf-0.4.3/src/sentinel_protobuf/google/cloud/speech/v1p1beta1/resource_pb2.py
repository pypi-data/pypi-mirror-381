"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/speech/v1p1beta1/resource.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/speech/v1p1beta1/resource.proto\x12\x1dgoogle.cloud.speech.v1p1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe4\x06\n\x0bCustomClass\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0fcustom_class_id\x18\x02 \x01(\t\x12C\n\x05items\x18\x03 \x03(\x0b24.google.cloud.speech.v1p1beta1.CustomClass.ClassItem\x12?\n\x0ckms_key_name\x18\x06 \x01(\tB)\xe0A\x03\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12N\n\x14kms_key_version_name\x18\x07 \x01(\tB0\xe0A\x03\xfaA*\n(cloudkms.googleapis.com/CryptoKeyVersion\x12\x10\n\x03uid\x18\x08 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\t \x01(\tB\x03\xe0A\x03\x12D\n\x05state\x18\n \x01(\x0e20.google.cloud.speech.v1p1beta1.CustomClass.StateB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12U\n\x0bannotations\x18\r \x03(\x0b2;.google.cloud.speech.v1p1beta1.CustomClass.AnnotationsEntryB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x0e \x01(\tB\x03\xe0A\x03\x12\x18\n\x0breconciling\x18\x0f \x01(\x08B\x03\xe0A\x03\x1a\x1a\n\tClassItem\x12\r\n\x05value\x18\x01 \x01(\t\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"7\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x02\x12\x0b\n\x07DELETED\x10\x04:l\xeaAi\n!speech.googleapis.com/CustomClass\x12Dprojects/{project}/locations/{location}/customClasses/{custom_class}"\xd6\x06\n\tPhraseSet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x07phrases\x18\x02 \x03(\x0b2/.google.cloud.speech.v1p1beta1.PhraseSet.Phrase\x12\r\n\x05boost\x18\x04 \x01(\x02\x12?\n\x0ckms_key_name\x18\x07 \x01(\tB)\xe0A\x03\xfaA#\n!cloudkms.googleapis.com/CryptoKey\x12N\n\x14kms_key_version_name\x18\x08 \x01(\tB0\xe0A\x03\xfaA*\n(cloudkms.googleapis.com/CryptoKeyVersion\x12\x10\n\x03uid\x18\t \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\n \x01(\tB\x03\xe0A\x03\x12B\n\x05state\x18\x0b \x01(\x0e2..google.cloud.speech.v1p1beta1.PhraseSet.StateB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12S\n\x0bannotations\x18\x0e \x03(\x0b29.google.cloud.speech.v1p1beta1.PhraseSet.AnnotationsEntryB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x0f \x01(\tB\x03\xe0A\x03\x12\x18\n\x0breconciling\x18\x10 \x01(\x08B\x03\xe0A\x03\x1a&\n\x06Phrase\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05boost\x18\x02 \x01(\x02\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"7\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x02\x12\x0b\n\x07DELETED\x10\x04:e\xeaAb\n\x1fspeech.googleapis.com/PhraseSet\x12?projects/{project}/locations/{location}/phraseSets/{phrase_set}"\xd2\x02\n\x10SpeechAdaptation\x12=\n\x0bphrase_sets\x18\x01 \x03(\x0b2(.google.cloud.speech.v1p1beta1.PhraseSet\x12C\n\x15phrase_set_references\x18\x02 \x03(\tB$\xfaA!\n\x1fspeech.googleapis.com/PhraseSet\x12B\n\x0ecustom_classes\x18\x03 \x03(\x0b2*.google.cloud.speech.v1p1beta1.CustomClass\x12Q\n\x0cabnf_grammar\x18\x04 \x01(\x0b2;.google.cloud.speech.v1p1beta1.SpeechAdaptation.ABNFGrammar\x1a#\n\x0bABNFGrammar\x12\x14\n\x0cabnf_strings\x18\x01 \x03(\t"\xaa\x01\n\x17TranscriptNormalization\x12M\n\x07entries\x18\x01 \x03(\x0b2<.google.cloud.speech.v1p1beta1.TranscriptNormalization.Entry\x1a@\n\x05Entry\x12\x0e\n\x06search\x18\x01 \x01(\t\x12\x0f\n\x07replace\x18\x02 \x01(\t\x12\x16\n\x0ecase_sensitive\x18\x03 \x01(\x08B\xa0\x03\n!com.google.cloud.speech.v1p1beta1B\x13SpeechResourceProtoP\x01Z9cloud.google.com/go/speech/apiv1p1beta1/speechpb;speechpb\xa2\x02\x03GCS\xeaAx\n!cloudkms.googleapis.com/CryptoKey\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}\xeaA\xa6\x01\n(cloudkms.googleapis.com/CryptoKeyVersion\x12zprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.speech.v1p1beta1.resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.speech.v1p1beta1B\x13SpeechResourceProtoP\x01Z9cloud.google.com/go/speech/apiv1p1beta1/speechpb;speechpb\xa2\x02\x03GCS\xeaAx\n!cloudkms.googleapis.com/CryptoKey\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}\xeaA\xa6\x01\n(cloudkms.googleapis.com/CryptoKeyVersion\x12zprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}'
    _globals['_CUSTOMCLASS_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_CUSTOMCLASS_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_CUSTOMCLASS'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_CUSTOMCLASS'].fields_by_name['kms_key_name']._serialized_options = b'\xe0A\x03\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_CUSTOMCLASS'].fields_by_name['kms_key_version_name']._loaded_options = None
    _globals['_CUSTOMCLASS'].fields_by_name['kms_key_version_name']._serialized_options = b'\xe0A\x03\xfaA*\n(cloudkms.googleapis.com/CryptoKeyVersion'
    _globals['_CUSTOMCLASS'].fields_by_name['uid']._loaded_options = None
    _globals['_CUSTOMCLASS'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCLASS'].fields_by_name['display_name']._loaded_options = None
    _globals['_CUSTOMCLASS'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCLASS'].fields_by_name['state']._loaded_options = None
    _globals['_CUSTOMCLASS'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCLASS'].fields_by_name['delete_time']._loaded_options = None
    _globals['_CUSTOMCLASS'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCLASS'].fields_by_name['expire_time']._loaded_options = None
    _globals['_CUSTOMCLASS'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCLASS'].fields_by_name['annotations']._loaded_options = None
    _globals['_CUSTOMCLASS'].fields_by_name['annotations']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCLASS'].fields_by_name['etag']._loaded_options = None
    _globals['_CUSTOMCLASS'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCLASS'].fields_by_name['reconciling']._loaded_options = None
    _globals['_CUSTOMCLASS'].fields_by_name['reconciling']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMCLASS']._loaded_options = None
    _globals['_CUSTOMCLASS']._serialized_options = b'\xeaAi\n!speech.googleapis.com/CustomClass\x12Dprojects/{project}/locations/{location}/customClasses/{custom_class}'
    _globals['_PHRASESET_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_PHRASESET_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_PHRASESET'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_PHRASESET'].fields_by_name['kms_key_name']._serialized_options = b'\xe0A\x03\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_PHRASESET'].fields_by_name['kms_key_version_name']._loaded_options = None
    _globals['_PHRASESET'].fields_by_name['kms_key_version_name']._serialized_options = b'\xe0A\x03\xfaA*\n(cloudkms.googleapis.com/CryptoKeyVersion'
    _globals['_PHRASESET'].fields_by_name['uid']._loaded_options = None
    _globals['_PHRASESET'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_PHRASESET'].fields_by_name['display_name']._loaded_options = None
    _globals['_PHRASESET'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_PHRASESET'].fields_by_name['state']._loaded_options = None
    _globals['_PHRASESET'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PHRASESET'].fields_by_name['delete_time']._loaded_options = None
    _globals['_PHRASESET'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_PHRASESET'].fields_by_name['expire_time']._loaded_options = None
    _globals['_PHRASESET'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_PHRASESET'].fields_by_name['annotations']._loaded_options = None
    _globals['_PHRASESET'].fields_by_name['annotations']._serialized_options = b'\xe0A\x03'
    _globals['_PHRASESET'].fields_by_name['etag']._loaded_options = None
    _globals['_PHRASESET'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_PHRASESET'].fields_by_name['reconciling']._loaded_options = None
    _globals['_PHRASESET'].fields_by_name['reconciling']._serialized_options = b'\xe0A\x03'
    _globals['_PHRASESET']._loaded_options = None
    _globals['_PHRASESET']._serialized_options = b'\xeaAb\n\x1fspeech.googleapis.com/PhraseSet\x12?projects/{project}/locations/{location}/phraseSets/{phrase_set}'
    _globals['_SPEECHADAPTATION'].fields_by_name['phrase_set_references']._loaded_options = None
    _globals['_SPEECHADAPTATION'].fields_by_name['phrase_set_references']._serialized_options = b'\xfaA!\n\x1fspeech.googleapis.com/PhraseSet'
    _globals['_CUSTOMCLASS']._serialized_start = 173
    _globals['_CUSTOMCLASS']._serialized_end = 1041
    _globals['_CUSTOMCLASS_CLASSITEM']._serialized_start = 796
    _globals['_CUSTOMCLASS_CLASSITEM']._serialized_end = 822
    _globals['_CUSTOMCLASS_ANNOTATIONSENTRY']._serialized_start = 824
    _globals['_CUSTOMCLASS_ANNOTATIONSENTRY']._serialized_end = 874
    _globals['_CUSTOMCLASS_STATE']._serialized_start = 876
    _globals['_CUSTOMCLASS_STATE']._serialized_end = 931
    _globals['_PHRASESET']._serialized_start = 1044
    _globals['_PHRASESET']._serialized_end = 1898
    _globals['_PHRASESET_PHRASE']._serialized_start = 1648
    _globals['_PHRASESET_PHRASE']._serialized_end = 1686
    _globals['_PHRASESET_ANNOTATIONSENTRY']._serialized_start = 824
    _globals['_PHRASESET_ANNOTATIONSENTRY']._serialized_end = 874
    _globals['_PHRASESET_STATE']._serialized_start = 876
    _globals['_PHRASESET_STATE']._serialized_end = 931
    _globals['_SPEECHADAPTATION']._serialized_start = 1901
    _globals['_SPEECHADAPTATION']._serialized_end = 2239
    _globals['_SPEECHADAPTATION_ABNFGRAMMAR']._serialized_start = 2204
    _globals['_SPEECHADAPTATION_ABNFGRAMMAR']._serialized_end = 2239
    _globals['_TRANSCRIPTNORMALIZATION']._serialized_start = 2242
    _globals['_TRANSCRIPTNORMALIZATION']._serialized_end = 2412
    _globals['_TRANSCRIPTNORMALIZATION_ENTRY']._serialized_start = 2348
    _globals['_TRANSCRIPTNORMALIZATION_ENTRY']._serialized_end = 2412