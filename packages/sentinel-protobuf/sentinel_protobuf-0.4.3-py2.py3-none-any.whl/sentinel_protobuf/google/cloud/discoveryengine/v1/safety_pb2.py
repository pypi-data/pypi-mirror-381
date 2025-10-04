"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/safety.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/discoveryengine/v1/safety.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto"\xce\x04\n\x0cSafetyRating\x12D\n\x08category\x18\x01 \x01(\x0e2-.google.cloud.discoveryengine.v1.HarmCategoryB\x03\xe0A\x03\x12W\n\x0bprobability\x18\x02 \x01(\x0e2=.google.cloud.discoveryengine.v1.SafetyRating.HarmProbabilityB\x03\xe0A\x03\x12\x1e\n\x11probability_score\x18\x05 \x01(\x02B\x03\xe0A\x03\x12Q\n\x08severity\x18\x06 \x01(\x0e2:.google.cloud.discoveryengine.v1.SafetyRating.HarmSeverityB\x03\xe0A\x03\x12\x1b\n\x0eseverity_score\x18\x07 \x01(\x02B\x03\xe0A\x03\x12\x14\n\x07blocked\x18\x03 \x01(\x08B\x03\xe0A\x03"b\n\x0fHarmProbability\x12 \n\x1cHARM_PROBABILITY_UNSPECIFIED\x10\x00\x12\x0e\n\nNEGLIGIBLE\x10\x01\x12\x07\n\x03LOW\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x08\n\x04HIGH\x10\x04"\x94\x01\n\x0cHarmSeverity\x12\x1d\n\x19HARM_SEVERITY_UNSPECIFIED\x10\x00\x12\x1c\n\x18HARM_SEVERITY_NEGLIGIBLE\x10\x01\x12\x15\n\x11HARM_SEVERITY_LOW\x10\x02\x12\x18\n\x14HARM_SEVERITY_MEDIUM\x10\x03\x12\x16\n\x12HARM_SEVERITY_HIGH\x10\x04*\xd7\x01\n\x0cHarmCategory\x12\x1d\n\x19HARM_CATEGORY_UNSPECIFIED\x10\x00\x12\x1d\n\x19HARM_CATEGORY_HATE_SPEECH\x10\x01\x12#\n\x1fHARM_CATEGORY_DANGEROUS_CONTENT\x10\x02\x12\x1c\n\x18HARM_CATEGORY_HARASSMENT\x10\x03\x12#\n\x1fHARM_CATEGORY_SEXUALLY_EXPLICIT\x10\x04\x12!\n\x1dHARM_CATEGORY_CIVIC_INTEGRITY\x10\x05B\xfe\x01\n#com.google.cloud.discoveryengine.v1B\x0bSafetyProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.safety_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x0bSafetyProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_SAFETYRATING'].fields_by_name['category']._loaded_options = None
    _globals['_SAFETYRATING'].fields_by_name['category']._serialized_options = b'\xe0A\x03'
    _globals['_SAFETYRATING'].fields_by_name['probability']._loaded_options = None
    _globals['_SAFETYRATING'].fields_by_name['probability']._serialized_options = b'\xe0A\x03'
    _globals['_SAFETYRATING'].fields_by_name['probability_score']._loaded_options = None
    _globals['_SAFETYRATING'].fields_by_name['probability_score']._serialized_options = b'\xe0A\x03'
    _globals['_SAFETYRATING'].fields_by_name['severity']._loaded_options = None
    _globals['_SAFETYRATING'].fields_by_name['severity']._serialized_options = b'\xe0A\x03'
    _globals['_SAFETYRATING'].fields_by_name['severity_score']._loaded_options = None
    _globals['_SAFETYRATING'].fields_by_name['severity_score']._serialized_options = b'\xe0A\x03'
    _globals['_SAFETYRATING'].fields_by_name['blocked']._loaded_options = None
    _globals['_SAFETYRATING'].fields_by_name['blocked']._serialized_options = b'\xe0A\x03'
    _globals['_HARMCATEGORY']._serialized_start = 708
    _globals['_HARMCATEGORY']._serialized_end = 923
    _globals['_SAFETYRATING']._serialized_start = 115
    _globals['_SAFETYRATING']._serialized_end = 705
    _globals['_SAFETYRATING_HARMPROBABILITY']._serialized_start = 456
    _globals['_SAFETYRATING_HARMPROBABILITY']._serialized_end = 554
    _globals['_SAFETYRATING_HARMSEVERITY']._serialized_start = 557
    _globals['_SAFETYRATING_HARMSEVERITY']._serialized_end = 705