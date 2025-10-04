"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/chat/v1/event_payload.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.chat.v1 import membership_pb2 as google_dot_chat_dot_v1_dot_membership__pb2
from ....google.chat.v1 import message_pb2 as google_dot_chat_dot_v1_dot_message__pb2
from ....google.chat.v1 import reaction_pb2 as google_dot_chat_dot_v1_dot_reaction__pb2
from ....google.chat.v1 import space_pb2 as google_dot_chat_dot_v1_dot_space__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/chat/v1/event_payload.proto\x12\x0egoogle.chat.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/chat/v1/membership.proto\x1a\x1cgoogle/chat/v1/message.proto\x1a\x1dgoogle/chat/v1/reaction.proto\x1a\x1agoogle/chat/v1/space.proto"L\n\x1aMembershipCreatedEventData\x12.\n\nmembership\x18\x01 \x01(\x0b2\x1a.google.chat.v1.Membership"L\n\x1aMembershipDeletedEventData\x12.\n\nmembership\x18\x01 \x01(\x0b2\x1a.google.chat.v1.Membership"L\n\x1aMembershipUpdatedEventData\x12.\n\nmembership\x18\x01 \x01(\x0b2\x1a.google.chat.v1.Membership"b\n\x1fMembershipBatchCreatedEventData\x12?\n\x0bmemberships\x18\x01 \x03(\x0b2*.google.chat.v1.MembershipCreatedEventData"b\n\x1fMembershipBatchUpdatedEventData\x12?\n\x0bmemberships\x18\x01 \x03(\x0b2*.google.chat.v1.MembershipUpdatedEventData"b\n\x1fMembershipBatchDeletedEventData\x12?\n\x0bmemberships\x18\x01 \x03(\x0b2*.google.chat.v1.MembershipDeletedEventData"C\n\x17MessageCreatedEventData\x12(\n\x07message\x18\x01 \x01(\x0b2\x17.google.chat.v1.Message"C\n\x17MessageUpdatedEventData\x12(\n\x07message\x18\x01 \x01(\x0b2\x17.google.chat.v1.Message"C\n\x17MessageDeletedEventData\x12(\n\x07message\x18\x01 \x01(\x0b2\x17.google.chat.v1.Message"Y\n\x1cMessageBatchCreatedEventData\x129\n\x08messages\x18\x01 \x03(\x0b2\'.google.chat.v1.MessageCreatedEventData"Y\n\x1cMessageBatchUpdatedEventData\x129\n\x08messages\x18\x01 \x03(\x0b2\'.google.chat.v1.MessageUpdatedEventData"Y\n\x1cMessageBatchDeletedEventData\x129\n\x08messages\x18\x01 \x03(\x0b2\'.google.chat.v1.MessageDeletedEventData"=\n\x15SpaceUpdatedEventData\x12$\n\x05space\x18\x01 \x01(\x0b2\x15.google.chat.v1.Space"S\n\x1aSpaceBatchUpdatedEventData\x125\n\x06spaces\x18\x01 \x03(\x0b2%.google.chat.v1.SpaceUpdatedEventData"F\n\x18ReactionCreatedEventData\x12*\n\x08reaction\x18\x01 \x01(\x0b2\x18.google.chat.v1.Reaction"F\n\x18ReactionDeletedEventData\x12*\n\x08reaction\x18\x01 \x01(\x0b2\x18.google.chat.v1.Reaction"\\\n\x1dReactionBatchCreatedEventData\x12;\n\treactions\x18\x01 \x03(\x0b2(.google.chat.v1.ReactionCreatedEventData"\\\n\x1dReactionBatchDeletedEventData\x12;\n\treactions\x18\x01 \x03(\x0b2(.google.chat.v1.ReactionDeletedEventDataB\xaa\x01\n\x12com.google.chat.v1B\x11EventPayloadProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.event_payload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x11EventPayloadProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_MEMBERSHIPCREATEDEVENTDATA']._serialized_start = 209
    _globals['_MEMBERSHIPCREATEDEVENTDATA']._serialized_end = 285
    _globals['_MEMBERSHIPDELETEDEVENTDATA']._serialized_start = 287
    _globals['_MEMBERSHIPDELETEDEVENTDATA']._serialized_end = 363
    _globals['_MEMBERSHIPUPDATEDEVENTDATA']._serialized_start = 365
    _globals['_MEMBERSHIPUPDATEDEVENTDATA']._serialized_end = 441
    _globals['_MEMBERSHIPBATCHCREATEDEVENTDATA']._serialized_start = 443
    _globals['_MEMBERSHIPBATCHCREATEDEVENTDATA']._serialized_end = 541
    _globals['_MEMBERSHIPBATCHUPDATEDEVENTDATA']._serialized_start = 543
    _globals['_MEMBERSHIPBATCHUPDATEDEVENTDATA']._serialized_end = 641
    _globals['_MEMBERSHIPBATCHDELETEDEVENTDATA']._serialized_start = 643
    _globals['_MEMBERSHIPBATCHDELETEDEVENTDATA']._serialized_end = 741
    _globals['_MESSAGECREATEDEVENTDATA']._serialized_start = 743
    _globals['_MESSAGECREATEDEVENTDATA']._serialized_end = 810
    _globals['_MESSAGEUPDATEDEVENTDATA']._serialized_start = 812
    _globals['_MESSAGEUPDATEDEVENTDATA']._serialized_end = 879
    _globals['_MESSAGEDELETEDEVENTDATA']._serialized_start = 881
    _globals['_MESSAGEDELETEDEVENTDATA']._serialized_end = 948
    _globals['_MESSAGEBATCHCREATEDEVENTDATA']._serialized_start = 950
    _globals['_MESSAGEBATCHCREATEDEVENTDATA']._serialized_end = 1039
    _globals['_MESSAGEBATCHUPDATEDEVENTDATA']._serialized_start = 1041
    _globals['_MESSAGEBATCHUPDATEDEVENTDATA']._serialized_end = 1130
    _globals['_MESSAGEBATCHDELETEDEVENTDATA']._serialized_start = 1132
    _globals['_MESSAGEBATCHDELETEDEVENTDATA']._serialized_end = 1221
    _globals['_SPACEUPDATEDEVENTDATA']._serialized_start = 1223
    _globals['_SPACEUPDATEDEVENTDATA']._serialized_end = 1284
    _globals['_SPACEBATCHUPDATEDEVENTDATA']._serialized_start = 1286
    _globals['_SPACEBATCHUPDATEDEVENTDATA']._serialized_end = 1369
    _globals['_REACTIONCREATEDEVENTDATA']._serialized_start = 1371
    _globals['_REACTIONCREATEDEVENTDATA']._serialized_end = 1441
    _globals['_REACTIONDELETEDEVENTDATA']._serialized_start = 1443
    _globals['_REACTIONDELETEDEVENTDATA']._serialized_end = 1513
    _globals['_REACTIONBATCHCREATEDEVENTDATA']._serialized_start = 1515
    _globals['_REACTIONBATCHCREATEDEVENTDATA']._serialized_end = 1607
    _globals['_REACTIONBATCHDELETEDEVENTDATA']._serialized_start = 1609
    _globals['_REACTIONBATCHDELETEDEVENTDATA']._serialized_end = 1701