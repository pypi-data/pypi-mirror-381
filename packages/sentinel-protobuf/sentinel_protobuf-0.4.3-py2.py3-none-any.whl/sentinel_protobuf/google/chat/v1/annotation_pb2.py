"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/chat/v1/annotation.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.chat.v1 import attachment_pb2 as google_dot_chat_dot_v1_dot_attachment__pb2
from ....google.chat.v1 import reaction_pb2 as google_dot_chat_dot_v1_dot_reaction__pb2
from ....google.chat.v1 import user_pb2 as google_dot_chat_dot_v1_dot_user__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fgoogle/chat/v1/annotation.proto\x12\x0egoogle.chat.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/chat/v1/attachment.proto\x1a\x1dgoogle/chat/v1/reaction.proto\x1a\x19google/chat/v1/user.proto"\x82\x03\n\nAnnotation\x12,\n\x04type\x18\x01 \x01(\x0e2\x1e.google.chat.v1.AnnotationType\x12\x18\n\x0bstart_index\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x0e\n\x06length\x18\x03 \x01(\x05\x12;\n\x0cuser_mention\x18\x04 \x01(\x0b2#.google.chat.v1.UserMentionMetadataH\x00\x12=\n\rslash_command\x18\x05 \x01(\x0b2$.google.chat.v1.SlashCommandMetadataH\x00\x12>\n\x12rich_link_metadata\x18\x06 \x01(\x0b2 .google.chat.v1.RichLinkMetadataH\x00\x12D\n\x15custom_emoji_metadata\x18\x07 \x01(\x0b2#.google.chat.v1.CustomEmojiMetadataH\x00B\n\n\x08metadataB\x0e\n\x0c_start_index"\xa5\x01\n\x13UserMentionMetadata\x12"\n\x04user\x18\x01 \x01(\x0b2\x14.google.chat.v1.User\x126\n\x04type\x18\x02 \x01(\x0e2(.google.chat.v1.UserMentionMetadata.Type"2\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03ADD\x10\x01\x12\x0b\n\x07MENTION\x10\x02"\xe8\x01\n\x14SlashCommandMetadata\x12!\n\x03bot\x18\x01 \x01(\x0b2\x14.google.chat.v1.User\x127\n\x04type\x18\x02 \x01(\x0e2).google.chat.v1.SlashCommandMetadata.Type\x12\x14\n\x0ccommand_name\x18\x03 \x01(\t\x12\x12\n\ncommand_id\x18\x04 \x01(\x03\x12\x17\n\x0ftriggers_dialog\x18\x05 \x01(\x08"1\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03ADD\x10\x01\x12\n\n\x06INVOKE\x10\x02"\xed\x03\n\x10RichLinkMetadata\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12E\n\x0erich_link_type\x18\x02 \x01(\x0e2-.google.chat.v1.RichLinkMetadata.RichLinkType\x128\n\x0fdrive_link_data\x18\x03 \x01(\x0b2\x1d.google.chat.v1.DriveLinkDataH\x00\x12A\n\x14chat_space_link_data\x18\x04 \x01(\x0b2!.google.chat.v1.ChatSpaceLinkDataH\x00\x12A\n\x14meet_space_link_data\x18\x05 \x01(\x0b2!.google.chat.v1.MeetSpaceLinkDataH\x00\x12I\n\x18calendar_event_link_data\x18\x06 \x01(\x0b2%.google.chat.v1.CalendarEventLinkDataH\x00"r\n\x0cRichLinkType\x12\x1e\n\x1aRICH_LINK_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nDRIVE_FILE\x10\x01\x12\x0e\n\nCHAT_SPACE\x10\x02\x12\x0e\n\nMEET_SPACE\x10\x04\x12\x12\n\x0eCALENDAR_EVENT\x10\x05B\x06\n\x04data"H\n\x13CustomEmojiMetadata\x121\n\x0ccustom_emoji\x18\x01 \x01(\x0b2\x1b.google.chat.v1.CustomEmoji"X\n\rDriveLinkData\x124\n\x0edrive_data_ref\x18\x01 \x01(\x0b2\x1c.google.chat.v1.DriveDataRef\x12\x11\n\tmime_type\x18\x02 \x01(\t"\xa6\x01\n\x11ChatSpaceLinkData\x12-\n\x05space\x18\x01 \x01(\tB\x1e\xfaA\x1b\n\x19chat.googleapis.com/Space\x12/\n\x06thread\x18\x02 \x01(\tB\x1f\xfaA\x1c\n\x1achat.googleapis.com/Thread\x121\n\x07message\x18\x03 \x01(\tB \xfaA\x1d\n\x1bchat.googleapis.com/Message"\xb8\x02\n\x11MeetSpaceLinkData\x12\x14\n\x0cmeeting_code\x18\x01 \x01(\t\x124\n\x04type\x18\x02 \x01(\x0e2&.google.chat.v1.MeetSpaceLinkData.Type\x12M\n\rhuddle_status\x18\x03 \x01(\x0e2..google.chat.v1.MeetSpaceLinkData.HuddleStatusB\x06\xe0A\x01\xe0A\x03"5\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07MEETING\x10\x01\x12\n\n\x06HUDDLE\x10\x02"Q\n\x0cHuddleStatus\x12\x1d\n\x19HUDDLE_STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\t\n\x05ENDED\x10\x02\x12\n\n\x06MISSED\x10\x03">\n\x15CalendarEventLinkData\x12\x13\n\x0bcalendar_id\x18\x01 \x01(\t\x12\x10\n\x08event_id\x18\x02 \x01(\t*w\n\x0eAnnotationType\x12\x1f\n\x1bANNOTATION_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cUSER_MENTION\x10\x01\x12\x11\n\rSLASH_COMMAND\x10\x02\x12\r\n\tRICH_LINK\x10\x03\x12\x10\n\x0cCUSTOM_EMOJI\x10\x04B\xa8\x01\n\x12com.google.chat.v1B\x0fAnnotationProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.annotation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x0fAnnotationProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_CHATSPACELINKDATA'].fields_by_name['space']._loaded_options = None
    _globals['_CHATSPACELINKDATA'].fields_by_name['space']._serialized_options = b'\xfaA\x1b\n\x19chat.googleapis.com/Space'
    _globals['_CHATSPACELINKDATA'].fields_by_name['thread']._loaded_options = None
    _globals['_CHATSPACELINKDATA'].fields_by_name['thread']._serialized_options = b'\xfaA\x1c\n\x1achat.googleapis.com/Thread'
    _globals['_CHATSPACELINKDATA'].fields_by_name['message']._loaded_options = None
    _globals['_CHATSPACELINKDATA'].fields_by_name['message']._serialized_options = b'\xfaA\x1d\n\x1bchat.googleapis.com/Message'
    _globals['_MEETSPACELINKDATA'].fields_by_name['huddle_status']._loaded_options = None
    _globals['_MEETSPACELINKDATA'].fields_by_name['huddle_status']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_ANNOTATIONTYPE']._serialized_start = 2202
    _globals['_ANNOTATIONTYPE']._serialized_end = 2321
    _globals['_ANNOTATION']._serialized_start = 203
    _globals['_ANNOTATION']._serialized_end = 589
    _globals['_USERMENTIONMETADATA']._serialized_start = 592
    _globals['_USERMENTIONMETADATA']._serialized_end = 757
    _globals['_USERMENTIONMETADATA_TYPE']._serialized_start = 707
    _globals['_USERMENTIONMETADATA_TYPE']._serialized_end = 757
    _globals['_SLASHCOMMANDMETADATA']._serialized_start = 760
    _globals['_SLASHCOMMANDMETADATA']._serialized_end = 992
    _globals['_SLASHCOMMANDMETADATA_TYPE']._serialized_start = 943
    _globals['_SLASHCOMMANDMETADATA_TYPE']._serialized_end = 992
    _globals['_RICHLINKMETADATA']._serialized_start = 995
    _globals['_RICHLINKMETADATA']._serialized_end = 1488
    _globals['_RICHLINKMETADATA_RICHLINKTYPE']._serialized_start = 1366
    _globals['_RICHLINKMETADATA_RICHLINKTYPE']._serialized_end = 1480
    _globals['_CUSTOMEMOJIMETADATA']._serialized_start = 1490
    _globals['_CUSTOMEMOJIMETADATA']._serialized_end = 1562
    _globals['_DRIVELINKDATA']._serialized_start = 1564
    _globals['_DRIVELINKDATA']._serialized_end = 1652
    _globals['_CHATSPACELINKDATA']._serialized_start = 1655
    _globals['_CHATSPACELINKDATA']._serialized_end = 1821
    _globals['_MEETSPACELINKDATA']._serialized_start = 1824
    _globals['_MEETSPACELINKDATA']._serialized_end = 2136
    _globals['_MEETSPACELINKDATA_TYPE']._serialized_start = 2000
    _globals['_MEETSPACELINKDATA_TYPE']._serialized_end = 2053
    _globals['_MEETSPACELINKDATA_HUDDLESTATUS']._serialized_start = 2055
    _globals['_MEETSPACELINKDATA_HUDDLESTATUS']._serialized_end = 2136
    _globals['_CALENDAREVENTLINKDATA']._serialized_start = 2138
    _globals['_CALENDAREVENTLINKDATA']._serialized_end = 2200