"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1beta2/safety.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ai/generativelanguage/v1beta2/safety.proto\x12$google.ai.generativelanguage.v1beta2\x1a\x1fgoogle/api/field_behavior.proto"\xcc\x01\n\rContentFilter\x12Q\n\x06reason\x18\x01 \x01(\x0e2A.google.ai.generativelanguage.v1beta2.ContentFilter.BlockedReason\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01"F\n\rBlockedReason\x12\x1e\n\x1aBLOCKED_REASON_UNSPECIFIED\x10\x00\x12\n\n\x06SAFETY\x10\x01\x12\t\n\x05OTHER\x10\x02B\n\n\x08_message"\x9a\x01\n\x0eSafetyFeedback\x12B\n\x06rating\x18\x01 \x01(\x0b22.google.ai.generativelanguage.v1beta2.SafetyRating\x12D\n\x07setting\x18\x02 \x01(\x0b23.google.ai.generativelanguage.v1beta2.SafetySetting"\x9b\x02\n\x0cSafetyRating\x12I\n\x08category\x18\x03 \x01(\x0e22.google.ai.generativelanguage.v1beta2.HarmCategoryB\x03\xe0A\x02\x12\\\n\x0bprobability\x18\x04 \x01(\x0e2B.google.ai.generativelanguage.v1beta2.SafetyRating.HarmProbabilityB\x03\xe0A\x02"b\n\x0fHarmProbability\x12 \n\x1cHARM_PROBABILITY_UNSPECIFIED\x10\x00\x12\x0e\n\nNEGLIGIBLE\x10\x01\x12\x07\n\x03LOW\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x08\n\x04HIGH\x10\x04"\xc1\x02\n\rSafetySetting\x12I\n\x08category\x18\x03 \x01(\x0e22.google.ai.generativelanguage.v1beta2.HarmCategoryB\x03\xe0A\x02\x12^\n\tthreshold\x18\x04 \x01(\x0e2F.google.ai.generativelanguage.v1beta2.SafetySetting.HarmBlockThresholdB\x03\xe0A\x02"\x84\x01\n\x12HarmBlockThreshold\x12$\n HARM_BLOCK_THRESHOLD_UNSPECIFIED\x10\x00\x12\x17\n\x13BLOCK_LOW_AND_ABOVE\x10\x01\x12\x1a\n\x16BLOCK_MEDIUM_AND_ABOVE\x10\x02\x12\x13\n\x0fBLOCK_ONLY_HIGH\x10\x03*\xd5\x01\n\x0cHarmCategory\x12\x1d\n\x19HARM_CATEGORY_UNSPECIFIED\x10\x00\x12\x1c\n\x18HARM_CATEGORY_DEROGATORY\x10\x01\x12\x1a\n\x16HARM_CATEGORY_TOXICITY\x10\x02\x12\x1a\n\x16HARM_CATEGORY_VIOLENCE\x10\x03\x12\x18\n\x14HARM_CATEGORY_SEXUAL\x10\x04\x12\x19\n\x15HARM_CATEGORY_MEDICAL\x10\x05\x12\x1b\n\x17HARM_CATEGORY_DANGEROUS\x10\x06B\x99\x01\n(com.google.ai.generativelanguage.v1beta2B\x0bSafetyProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1beta2/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta2.safety_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ai.generativelanguage.v1beta2B\x0bSafetyProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1beta2/generativelanguagepb;generativelanguagepb'
    _globals['_SAFETYRATING'].fields_by_name['category']._loaded_options = None
    _globals['_SAFETYRATING'].fields_by_name['category']._serialized_options = b'\xe0A\x02'
    _globals['_SAFETYRATING'].fields_by_name['probability']._loaded_options = None
    _globals['_SAFETYRATING'].fields_by_name['probability']._serialized_options = b'\xe0A\x02'
    _globals['_SAFETYSETTING'].fields_by_name['category']._loaded_options = None
    _globals['_SAFETYSETTING'].fields_by_name['category']._serialized_options = b'\xe0A\x02'
    _globals['_SAFETYSETTING'].fields_by_name['threshold']._loaded_options = None
    _globals['_SAFETYSETTING'].fields_by_name['threshold']._serialized_options = b'\xe0A\x02'
    _globals['_HARMCATEGORY']._serialized_start = 1099
    _globals['_HARMCATEGORY']._serialized_end = 1312
    _globals['_CONTENTFILTER']._serialized_start = 125
    _globals['_CONTENTFILTER']._serialized_end = 329
    _globals['_CONTENTFILTER_BLOCKEDREASON']._serialized_start = 247
    _globals['_CONTENTFILTER_BLOCKEDREASON']._serialized_end = 317
    _globals['_SAFETYFEEDBACK']._serialized_start = 332
    _globals['_SAFETYFEEDBACK']._serialized_end = 486
    _globals['_SAFETYRATING']._serialized_start = 489
    _globals['_SAFETYRATING']._serialized_end = 772
    _globals['_SAFETYRATING_HARMPROBABILITY']._serialized_start = 674
    _globals['_SAFETYRATING_HARMPROBABILITY']._serialized_end = 772
    _globals['_SAFETYSETTING']._serialized_start = 775
    _globals['_SAFETYSETTING']._serialized_end = 1096
    _globals['_SAFETYSETTING_HARMBLOCKTHRESHOLD']._serialized_start = 964
    _globals['_SAFETYSETTING_HARMBLOCKTHRESHOLD']._serialized_end = 1096