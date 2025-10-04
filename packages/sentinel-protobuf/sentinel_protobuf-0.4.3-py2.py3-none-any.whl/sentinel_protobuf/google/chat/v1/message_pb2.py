"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/chat/v1/message.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.apps.card.v1 import card_pb2 as google_dot_apps_dot_card_dot_v1_dot_card__pb2
from ....google.chat.v1 import action_status_pb2 as google_dot_chat_dot_v1_dot_action__status__pb2
from ....google.chat.v1 import annotation_pb2 as google_dot_chat_dot_v1_dot_annotation__pb2
from ....google.chat.v1 import attachment_pb2 as google_dot_chat_dot_v1_dot_attachment__pb2
from ....google.chat.v1 import contextual_addon_pb2 as google_dot_chat_dot_v1_dot_contextual__addon__pb2
from ....google.chat.v1 import deletion_metadata_pb2 as google_dot_chat_dot_v1_dot_deletion__metadata__pb2
from ....google.chat.v1 import matched_url_pb2 as google_dot_chat_dot_v1_dot_matched__url__pb2
from ....google.chat.v1 import reaction_pb2 as google_dot_chat_dot_v1_dot_reaction__pb2
from ....google.chat.v1 import slash_command_pb2 as google_dot_chat_dot_v1_dot_slash__command__pb2
from ....google.chat.v1 import space_pb2 as google_dot_chat_dot_v1_dot_space__pb2
from ....google.chat.v1 import user_pb2 as google_dot_chat_dot_v1_dot_user__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgoogle/chat/v1/message.proto\x12\x0egoogle.chat.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/apps/card/v1/card.proto\x1a"google/chat/v1/action_status.proto\x1a\x1fgoogle/chat/v1/annotation.proto\x1a\x1fgoogle/chat/v1/attachment.proto\x1a%google/chat/v1/contextual_addon.proto\x1a&google/chat/v1/deletion_metadata.proto\x1a google/chat/v1/matched_url.proto\x1a\x1dgoogle/chat/v1/reaction.proto\x1a"google/chat/v1/slash_command.proto\x1a\x1agoogle/chat/v1/space.proto\x1a\x19google/chat/v1/user.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd4\n\n\x07Message\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12)\n\x06sender\x18\x02 \x01(\x0b2\x14.google.chat.v1.UserB\x03\xe0A\x03\x127\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x06\xe0A\x05\xe0A\x01\x129\n\x10last_update_time\x18\x17 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x1a \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04text\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0eformatted_text\x18+ \x01(\tB\x03\xe0A\x03\x12=\n\x05cards\x18\x05 \x03(\x0b2*.google.chat.v1.ContextualAddOnMarkup.CardB\x02\x18\x01\x121\n\x08cards_v2\x18\x16 \x03(\x0b2\x1a.google.chat.v1.CardWithIdB\x03\xe0A\x01\x124\n\x0bannotations\x18\n \x03(\x0b2\x1a.google.chat.v1.AnnotationB\x03\xe0A\x03\x12&\n\x06thread\x18\x0b \x01(\x0b2\x16.google.chat.v1.Thread\x12)\n\x05space\x18\x0c \x01(\x0b2\x15.google.chat.v1.SpaceB\x03\xe0A\x03\x12\x1a\n\rfallback_text\x18\r \x01(\tB\x03\xe0A\x01\x12<\n\x0faction_response\x18\x0e \x01(\x0b2\x1e.google.chat.v1.ActionResponseB\x03\xe0A\x04\x12\x1a\n\rargument_text\x18\x0f \x01(\tB\x03\xe0A\x03\x128\n\rslash_command\x18\x11 \x01(\x0b2\x1c.google.chat.v1.SlashCommandB\x03\xe0A\x03\x123\n\nattachment\x18\x12 \x03(\x0b2\x1a.google.chat.v1.AttachmentB\x03\xe0A\x01\x124\n\x0bmatched_url\x18\x14 \x01(\x0b2\x1a.google.chat.v1.MatchedUrlB\x03\xe0A\x03\x12\x19\n\x0cthread_reply\x18\x19 \x01(\x08B\x03\xe0A\x03\x12\'\n\x1aclient_assigned_message_id\x18  \x01(\tB\x03\xe0A\x01\x12K\n\x18emoji_reaction_summaries\x18! \x03(\x0b2$.google.chat.v1.EmojiReactionSummaryB\x03\xe0A\x03\x12<\n\x16private_message_viewer\x18$ \x01(\x0b2\x14.google.chat.v1.UserB\x06\xe0A\x05\xe0A\x01\x12@\n\x11deletion_metadata\x18& \x01(\x0b2 .google.chat.v1.DeletionMetadataB\x03\xe0A\x03\x12K\n\x17quoted_message_metadata\x18\' \x01(\x0b2%.google.chat.v1.QuotedMessageMetadataB\x03\xe0A\x01\x127\n\rattached_gifs\x18* \x03(\x0b2\x1b.google.chat.v1.AttachedGifB\x03\xe0A\x03\x12?\n\x11accessory_widgets\x18, \x03(\x0b2\x1f.google.chat.v1.AccessoryWidgetB\x03\xe0A\x01:C\xeaA@\n\x1bchat.googleapis.com/Message\x12!spaces/{space}/messages/{message}"\x1f\n\x0bAttachedGif\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x03"\x89\x02\n\x15QuotedMessageMetadata\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bchat.googleapis.com/Message\x129\n\x10last_update_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02:\x81\x01\xeaA~\n)chat.googleapis.com/QuotedMessageMetadata\x12Qspaces/{space}/messages/{message}/quotedMessageMetadata/{quoted_message_metadata}"v\n\x06Thread\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x17\n\nthread_key\x18\x03 \x01(\tB\x03\xe0A\x01:@\xeaA=\n\x1achat.googleapis.com/Thread\x12\x1fspaces/{space}/threads/{thread}"\xd2\x04\n\x0eActionResponse\x12>\n\x04type\x18\x01 \x01(\x0e2+.google.chat.v1.ActionResponse.ResponseTypeB\x03\xe0A\x04\x12\x10\n\x03url\x18\x02 \x01(\tB\x03\xe0A\x04\x128\n\rdialog_action\x18\x03 \x01(\x0b2\x1c.google.chat.v1.DialogActionB\x03\xe0A\x04\x12I\n\x0eupdated_widget\x18\x04 \x01(\x0b2,.google.chat.v1.ActionResponse.UpdatedWidgetB\x03\xe0A\x04\x1aR\n\x0eSelectionItems\x12@\n\x05items\x18\x01 \x03(\x0b21.google.apps.card.v1.SelectionInput.SelectionItem\x1aw\n\rUpdatedWidget\x12D\n\x0bsuggestions\x18\x01 \x01(\x0b2-.google.chat.v1.ActionResponse.SelectionItemsH\x00\x12\x0e\n\x06widget\x18\x02 \x01(\tB\x10\n\x0eupdated_widget"\x9b\x01\n\x0cResponseType\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bNEW_MESSAGE\x10\x01\x12\x12\n\x0eUPDATE_MESSAGE\x10\x02\x12\x1d\n\x19UPDATE_USER_MESSAGE_CARDS\x10\x06\x12\x12\n\x0eREQUEST_CONFIG\x10\x03\x12\n\n\x06DIALOG\x10\x04\x12\x11\n\rUPDATE_WIDGET\x10\x07"S\n\x0fAccessoryWidget\x126\n\x0bbutton_list\x18\x01 \x01(\x0b2\x1f.google.apps.card.v1.ButtonListH\x00B\x08\n\x06action"F\n\x11GetMessageRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bchat.googleapis.com/Message"]\n\x14DeleteMessageRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bchat.googleapis.com/Message\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x01"\x97\x01\n\x14UpdateMessageRequest\x12-\n\x07message\x18\x01 \x01(\x0b2\x17.google.chat.v1.MessageB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12\x1a\n\rallow_missing\x18\x04 \x01(\x08B\x03\xe0A\x01"\xa4\x03\n\x14CreateMessageRequest\x123\n\x06parent\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\x12\x1bchat.googleapis.com/Message\x12-\n\x07message\x18\x04 \x01(\x0b2\x17.google.chat.v1.MessageB\x03\xe0A\x02\x12\x19\n\nthread_key\x18\x06 \x01(\tB\x05\x18\x01\xe0A\x01\x12\x17\n\nrequest_id\x18\x07 \x01(\tB\x03\xe0A\x01\x12Z\n\x14message_reply_option\x18\x08 \x01(\x0e27.google.chat.v1.CreateMessageRequest.MessageReplyOptionB\x03\xe0A\x01\x12\x17\n\nmessage_id\x18\t \x01(\tB\x03\xe0A\x01"\x7f\n\x12MessageReplyOption\x12$\n MESSAGE_REPLY_OPTION_UNSPECIFIED\x10\x00\x12(\n$REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD\x10\x01\x12\x19\n\x15REPLY_MESSAGE_OR_FAIL\x10\x02"\xc2\x01\n\x13ListMessagesRequest\x123\n\x06parent\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\x12\x1bchat.googleapis.com/Message\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cshow_deleted\x18\x06 \x01(\x08B\x03\xe0A\x01"Z\n\x14ListMessagesResponse\x12)\n\x08messages\x18\x01 \x03(\x0b2\x17.google.chat.v1.Message\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x81\x01\n\x0cDialogAction\x12-\n\x06dialog\x18\x01 \x01(\x0b2\x16.google.chat.v1.DialogB\x03\xe0A\x04H\x00\x128\n\raction_status\x18\x02 \x01(\x0b2\x1c.google.chat.v1.ActionStatusB\x03\xe0A\x04B\x08\n\x06action"6\n\x06Dialog\x12,\n\x04body\x18\x01 \x01(\x0b2\x19.google.apps.card.v1.CardB\x03\xe0A\x04"F\n\nCardWithId\x12\x0f\n\x07card_id\x18\x01 \x01(\t\x12\'\n\x04card\x18\x02 \x01(\x0b2\x19.google.apps.card.v1.CardB\xa5\x01\n\x12com.google.chat.v1B\x0cMessageProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x0cMessageProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_MESSAGE'].fields_by_name['name']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_MESSAGE'].fields_by_name['sender']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['sender']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['create_time']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x05\xe0A\x01'
    _globals['_MESSAGE'].fields_by_name['last_update_time']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['last_update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['delete_time']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['text']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['text']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGE'].fields_by_name['formatted_text']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['formatted_text']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['cards']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['cards']._serialized_options = b'\x18\x01'
    _globals['_MESSAGE'].fields_by_name['cards_v2']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['cards_v2']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGE'].fields_by_name['annotations']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['annotations']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['space']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['space']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['fallback_text']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['fallback_text']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGE'].fields_by_name['action_response']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['action_response']._serialized_options = b'\xe0A\x04'
    _globals['_MESSAGE'].fields_by_name['argument_text']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['argument_text']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['slash_command']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['slash_command']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['attachment']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['attachment']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGE'].fields_by_name['matched_url']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['matched_url']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['thread_reply']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['thread_reply']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['client_assigned_message_id']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['client_assigned_message_id']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGE'].fields_by_name['emoji_reaction_summaries']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['emoji_reaction_summaries']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['private_message_viewer']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['private_message_viewer']._serialized_options = b'\xe0A\x05\xe0A\x01'
    _globals['_MESSAGE'].fields_by_name['deletion_metadata']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['deletion_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['quoted_message_metadata']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['quoted_message_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGE'].fields_by_name['attached_gifs']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['attached_gifs']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['accessory_widgets']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['accessory_widgets']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGE']._loaded_options = None
    _globals['_MESSAGE']._serialized_options = b'\xeaA@\n\x1bchat.googleapis.com/Message\x12!spaces/{space}/messages/{message}'
    _globals['_ATTACHEDGIF'].fields_by_name['uri']._loaded_options = None
    _globals['_ATTACHEDGIF'].fields_by_name['uri']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTEDMESSAGEMETADATA'].fields_by_name['name']._loaded_options = None
    _globals['_QUOTEDMESSAGEMETADATA'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bchat.googleapis.com/Message'
    _globals['_QUOTEDMESSAGEMETADATA'].fields_by_name['last_update_time']._loaded_options = None
    _globals['_QUOTEDMESSAGEMETADATA'].fields_by_name['last_update_time']._serialized_options = b'\xe0A\x02'
    _globals['_QUOTEDMESSAGEMETADATA']._loaded_options = None
    _globals['_QUOTEDMESSAGEMETADATA']._serialized_options = b'\xeaA~\n)chat.googleapis.com/QuotedMessageMetadata\x12Qspaces/{space}/messages/{message}/quotedMessageMetadata/{quoted_message_metadata}'
    _globals['_THREAD'].fields_by_name['name']._loaded_options = None
    _globals['_THREAD'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_THREAD'].fields_by_name['thread_key']._loaded_options = None
    _globals['_THREAD'].fields_by_name['thread_key']._serialized_options = b'\xe0A\x01'
    _globals['_THREAD']._loaded_options = None
    _globals['_THREAD']._serialized_options = b'\xeaA=\n\x1achat.googleapis.com/Thread\x12\x1fspaces/{space}/threads/{thread}'
    _globals['_ACTIONRESPONSE'].fields_by_name['type']._loaded_options = None
    _globals['_ACTIONRESPONSE'].fields_by_name['type']._serialized_options = b'\xe0A\x04'
    _globals['_ACTIONRESPONSE'].fields_by_name['url']._loaded_options = None
    _globals['_ACTIONRESPONSE'].fields_by_name['url']._serialized_options = b'\xe0A\x04'
    _globals['_ACTIONRESPONSE'].fields_by_name['dialog_action']._loaded_options = None
    _globals['_ACTIONRESPONSE'].fields_by_name['dialog_action']._serialized_options = b'\xe0A\x04'
    _globals['_ACTIONRESPONSE'].fields_by_name['updated_widget']._loaded_options = None
    _globals['_ACTIONRESPONSE'].fields_by_name['updated_widget']._serialized_options = b'\xe0A\x04'
    _globals['_GETMESSAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMESSAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bchat.googleapis.com/Message'
    _globals['_DELETEMESSAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMESSAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bchat.googleapis.com/Message'
    _globals['_DELETEMESSAGEREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEMESSAGEREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEMESSAGEREQUEST'].fields_by_name['message']._loaded_options = None
    _globals['_UPDATEMESSAGEREQUEST'].fields_by_name['message']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMESSAGEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMESSAGEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMESSAGEREQUEST'].fields_by_name['allow_missing']._loaded_options = None
    _globals['_UPDATEMESSAGEREQUEST'].fields_by_name['allow_missing']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEMESSAGEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMESSAGEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1d\x12\x1bchat.googleapis.com/Message'
    _globals['_CREATEMESSAGEREQUEST'].fields_by_name['message']._loaded_options = None
    _globals['_CREATEMESSAGEREQUEST'].fields_by_name['message']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMESSAGEREQUEST'].fields_by_name['thread_key']._loaded_options = None
    _globals['_CREATEMESSAGEREQUEST'].fields_by_name['thread_key']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_CREATEMESSAGEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEMESSAGEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEMESSAGEREQUEST'].fields_by_name['message_reply_option']._loaded_options = None
    _globals['_CREATEMESSAGEREQUEST'].fields_by_name['message_reply_option']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEMESSAGEREQUEST'].fields_by_name['message_id']._loaded_options = None
    _globals['_CREATEMESSAGEREQUEST'].fields_by_name['message_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1d\x12\x1bchat.googleapis.com/Message'
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['show_deleted']._loaded_options = None
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['show_deleted']._serialized_options = b'\xe0A\x01'
    _globals['_DIALOGACTION'].fields_by_name['dialog']._loaded_options = None
    _globals['_DIALOGACTION'].fields_by_name['dialog']._serialized_options = b'\xe0A\x04'
    _globals['_DIALOGACTION'].fields_by_name['action_status']._loaded_options = None
    _globals['_DIALOGACTION'].fields_by_name['action_status']._serialized_options = b'\xe0A\x04'
    _globals['_DIALOG'].fields_by_name['body']._loaded_options = None
    _globals['_DIALOG'].fields_by_name['body']._serialized_options = b'\xe0A\x04'
    _globals['_MESSAGE']._serialized_start = 545
    _globals['_MESSAGE']._serialized_end = 1909
    _globals['_ATTACHEDGIF']._serialized_start = 1911
    _globals['_ATTACHEDGIF']._serialized_end = 1942
    _globals['_QUOTEDMESSAGEMETADATA']._serialized_start = 1945
    _globals['_QUOTEDMESSAGEMETADATA']._serialized_end = 2210
    _globals['_THREAD']._serialized_start = 2212
    _globals['_THREAD']._serialized_end = 2330
    _globals['_ACTIONRESPONSE']._serialized_start = 2333
    _globals['_ACTIONRESPONSE']._serialized_end = 2927
    _globals['_ACTIONRESPONSE_SELECTIONITEMS']._serialized_start = 2566
    _globals['_ACTIONRESPONSE_SELECTIONITEMS']._serialized_end = 2648
    _globals['_ACTIONRESPONSE_UPDATEDWIDGET']._serialized_start = 2650
    _globals['_ACTIONRESPONSE_UPDATEDWIDGET']._serialized_end = 2769
    _globals['_ACTIONRESPONSE_RESPONSETYPE']._serialized_start = 2772
    _globals['_ACTIONRESPONSE_RESPONSETYPE']._serialized_end = 2927
    _globals['_ACCESSORYWIDGET']._serialized_start = 2929
    _globals['_ACCESSORYWIDGET']._serialized_end = 3012
    _globals['_GETMESSAGEREQUEST']._serialized_start = 3014
    _globals['_GETMESSAGEREQUEST']._serialized_end = 3084
    _globals['_DELETEMESSAGEREQUEST']._serialized_start = 3086
    _globals['_DELETEMESSAGEREQUEST']._serialized_end = 3179
    _globals['_UPDATEMESSAGEREQUEST']._serialized_start = 3182
    _globals['_UPDATEMESSAGEREQUEST']._serialized_end = 3333
    _globals['_CREATEMESSAGEREQUEST']._serialized_start = 3336
    _globals['_CREATEMESSAGEREQUEST']._serialized_end = 3756
    _globals['_CREATEMESSAGEREQUEST_MESSAGEREPLYOPTION']._serialized_start = 3629
    _globals['_CREATEMESSAGEREQUEST_MESSAGEREPLYOPTION']._serialized_end = 3756
    _globals['_LISTMESSAGESREQUEST']._serialized_start = 3759
    _globals['_LISTMESSAGESREQUEST']._serialized_end = 3953
    _globals['_LISTMESSAGESRESPONSE']._serialized_start = 3955
    _globals['_LISTMESSAGESRESPONSE']._serialized_end = 4045
    _globals['_DIALOGACTION']._serialized_start = 4048
    _globals['_DIALOGACTION']._serialized_end = 4177
    _globals['_DIALOG']._serialized_start = 4179
    _globals['_DIALOG']._serialized_end = 4233
    _globals['_CARDWITHID']._serialized_start = 4235
    _globals['_CARDWITHID']._serialized_end = 4305