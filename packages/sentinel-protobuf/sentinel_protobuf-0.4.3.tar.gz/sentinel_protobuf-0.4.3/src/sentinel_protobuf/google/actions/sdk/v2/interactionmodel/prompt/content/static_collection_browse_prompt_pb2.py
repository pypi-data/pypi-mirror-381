"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/actions/sdk/v2/interactionmodel/prompt/content/static_collection_browse_prompt.proto')
_sym_db = _symbol_database.Default()
from ........google.actions.sdk.v2.interactionmodel.prompt.content import static_image_prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_content_dot_static__image__prompt__pb2
from ........google.actions.sdk.v2.interactionmodel.prompt.content import static_link_prompt_pb2 as google_dot_actions_dot_sdk_dot_v2_dot_interactionmodel_dot_prompt_dot_content_dot_static__link__prompt__pb2
from ........google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n[google/actions/sdk/v2/interactionmodel/prompt/content/static_collection_browse_prompt.proto\x12-google.actions.sdk.v2.interactionmodel.prompt\x1aOgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_image_prompt.proto\x1aNgoogle/actions/sdk/v2/interactionmodel/prompt/content/static_link_prompt.proto\x1a\x1fgoogle/api/field_behavior.proto"\xe8\x03\n\x1cStaticCollectionBrowsePrompt\x12o\n\x05items\x18\x01 \x03(\x0b2`.google.actions.sdk.v2.interactionmodel.prompt.StaticCollectionBrowsePrompt.CollectionBrowseItem\x12^\n\nimage_fill\x18\x02 \x01(\x0e2J.google.actions.sdk.v2.interactionmodel.prompt.StaticImagePrompt.ImageFill\x1a\xf6\x01\n\x14CollectionBrowseItem\x12\x12\n\x05title\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x0e\n\x06footer\x18\x03 \x01(\t\x12O\n\x05image\x18\x04 \x01(\x0b2@.google.actions.sdk.v2.interactionmodel.prompt.StaticImagePrompt\x12T\n\x0fopen_uri_action\x18\x05 \x01(\x0b26.google.actions.sdk.v2.interactionmodel.prompt.OpenUrlB\x03\xe0A\x02B\xad\x01\n1com.google.actions.sdk.v2.interactionmodel.promptB!StaticCollectionBrowsePromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;promptb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.interactionmodel.prompt.content.static_collection_browse_prompt_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.actions.sdk.v2.interactionmodel.promptB!StaticCollectionBrowsePromptProtoP\x01ZSgoogle.golang.org/genproto/googleapis/actions/sdk/v2/interactionmodel/prompt;prompt'
    _globals['_STATICCOLLECTIONBROWSEPROMPT_COLLECTIONBROWSEITEM'].fields_by_name['title']._loaded_options = None
    _globals['_STATICCOLLECTIONBROWSEPROMPT_COLLECTIONBROWSEITEM'].fields_by_name['title']._serialized_options = b'\xe0A\x02'
    _globals['_STATICCOLLECTIONBROWSEPROMPT_COLLECTIONBROWSEITEM'].fields_by_name['open_uri_action']._loaded_options = None
    _globals['_STATICCOLLECTIONBROWSEPROMPT_COLLECTIONBROWSEITEM'].fields_by_name['open_uri_action']._serialized_options = b'\xe0A\x02'
    _globals['_STATICCOLLECTIONBROWSEPROMPT']._serialized_start = 337
    _globals['_STATICCOLLECTIONBROWSEPROMPT']._serialized_end = 825
    _globals['_STATICCOLLECTIONBROWSEPROMPT_COLLECTIONBROWSEITEM']._serialized_start = 579
    _globals['_STATICCOLLECTIONBROWSEPROMPT_COLLECTIONBROWSEITEM']._serialized_end = 825