"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/actions/sdk/v2/interactionmodel/prompt/static_simple_prompt.proto')
_sym_db = _symbol_database.Default()
from .......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/actions/sdk/v2/interactionmodel/prompt/static_simple_prompt.proto\x12-google.actions.sdk.v2.interactionmodel.prompt\x1a\x1fgoogle/api/field_behavior.proto"\xa4\x01\n\x12StaticSimplePrompt\x12[\n\x08variants\x18\x01 \x03(\x0b2I.google.actions.sdk.v2.interactionmodel.prompt.StaticSimplePrompt.Variant\x1a1\n\x07Variant\x12\x13\n\x06speech\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04text\x18\x02 \x01(\tB\x03\xe0A\x01B\xa3\x01\n1com.google.actions.sdk.v2.interactionmodel.promptB\x17StaticSimplePromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;promptb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.prompt.static_simple_prompt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.actions.sdk.v2.interactionmodel.promptB\x17StaticSimplePromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;prompt'
    _globals['_STATICSIMPLEPROMPT_VARIANT'].fields_by_name['speech']._loaded_options = None
    _globals['_STATICSIMPLEPROMPT_VARIANT'].fields_by_name['speech']._serialized_options = b'\xe0A\x01'
    _globals['_STATICSIMPLEPROMPT_VARIANT'].fields_by_name['text']._loaded_options = None
    _globals['_STATICSIMPLEPROMPT_VARIANT'].fields_by_name['text']._serialized_options = b'\xe0A\x01'
    _globals['_STATICSIMPLEPROMPT']._serialized_start = 157
    _globals['_STATICSIMPLEPROMPT']._serialized_end = 321
    _globals['_STATICSIMPLEPROMPT_VARIANT']._serialized_start = 272
    _globals['_STATICSIMPLEPROMPT_VARIANT']._serialized_end = 321