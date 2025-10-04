"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/chat/v1/reaction.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.chat.v1 import user_pb2 as google_dot_chat_dot_v1_dot_user__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dgoogle/chat/v1/reaction.proto\x12\x0egoogle.chat.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x19google/chat/v1/user.proto"\xcc\x01\n\x08Reaction\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\'\n\x04user\x18\x02 \x01(\x0b2\x14.google.chat.v1.UserB\x03\xe0A\x03\x12)\n\x05emoji\x18\x03 \x01(\x0b2\x15.google.chat.v1.EmojiB\x03\xe0A\x02:Y\xeaAV\n\x1cchat.googleapis.com/Reaction\x126spaces/{space}/messages/{message}/reactions/{reaction}"_\n\x05Emoji\x12\x16\n\x07unicode\x18\x01 \x01(\tB\x03\xe0A\x01H\x00\x123\n\x0ccustom_emoji\x18\x02 \x01(\x0b2\x1b.google.chat.v1.CustomEmojiH\x00B\t\n\x07content"\xed\x02\n\x0bCustomEmoji\x12\x11\n\x04name\x18\x02 \x01(\tB\x03\xe0A\x08\x12\x18\n\x03uid\x18\x01 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x1a\n\nemoji_name\x18\x03 \x01(\tB\x06\xe0A\x01\xe0A\x05\x12 \n\x13temporary_image_uri\x18\x04 \x01(\tB\x03\xe0A\x03\x12G\n\x07payload\x18\x05 \x01(\x0b2..google.chat.v1.CustomEmoji.CustomEmojiPayloadB\x06\xe0A\x04\xe0A\x01\x1aL\n\x12CustomEmojiPayload\x12\x1c\n\x0cfile_content\x18\x01 \x01(\x0cB\x06\xe0A\x04\xe0A\x02\x12\x18\n\x08filename\x18\x02 \x01(\tB\x06\xe0A\x04\xe0A\x02:\\\xeaAY\n\x1fchat.googleapis.com/CustomEmoji\x12\x1bcustomEmojis/{custom_emoji}*\x0ccustomEmojis2\x0bcustomEmoji"v\n\x14EmojiReactionSummary\x12)\n\x05emoji\x18\x01 \x01(\x0b2\x15.google.chat.v1.EmojiB\x03\xe0A\x03\x12 \n\x0ereaction_count\x18\x02 \x01(\x05B\x03\xe0A\x03H\x00\x88\x01\x01B\x11\n\x0f_reaction_count"~\n\x15CreateReactionRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\x12\x1cchat.googleapis.com/Reaction\x12/\n\x08reaction\x18\x02 \x01(\x0b2\x18.google.chat.v1.ReactionB\x03\xe0A\x02"\x92\x01\n\x14ListReactionsRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\x12\x1cchat.googleapis.com/Reaction\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"]\n\x15ListReactionsResponse\x12+\n\treactions\x18\x01 \x03(\x0b2\x18.google.chat.v1.Reaction\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"K\n\x15DeleteReactionRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cchat.googleapis.com/Reaction"R\n\x18CreateCustomEmojiRequest\x126\n\x0ccustom_emoji\x18\x01 \x01(\x0b2\x1b.google.chat.v1.CustomEmojiB\x03\xe0A\x02"N\n\x15GetCustomEmojiRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fchat.googleapis.com/CustomEmoji"_\n\x17ListCustomEmojisRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x01"l\n\x18ListCustomEmojisResponse\x127\n\rcustom_emojis\x18\x01 \x03(\x0b2\x1b.google.chat.v1.CustomEmojiB\x03\xe0A\x06\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Q\n\x18DeleteCustomEmojiRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fchat.googleapis.com/CustomEmojiB\xa6\x01\n\x12com.google.chat.v1B\rReactionProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.reaction_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\rReactionProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_REACTION'].fields_by_name['name']._loaded_options = None
    _globals['_REACTION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_REACTION'].fields_by_name['user']._loaded_options = None
    _globals['_REACTION'].fields_by_name['user']._serialized_options = b'\xe0A\x03'
    _globals['_REACTION'].fields_by_name['emoji']._loaded_options = None
    _globals['_REACTION'].fields_by_name['emoji']._serialized_options = b'\xe0A\x02'
    _globals['_REACTION']._loaded_options = None
    _globals['_REACTION']._serialized_options = b'\xeaAV\n\x1cchat.googleapis.com/Reaction\x126spaces/{space}/messages/{message}/reactions/{reaction}'
    _globals['_EMOJI'].fields_by_name['unicode']._loaded_options = None
    _globals['_EMOJI'].fields_by_name['unicode']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMEMOJI_CUSTOMEMOJIPAYLOAD'].fields_by_name['file_content']._loaded_options = None
    _globals['_CUSTOMEMOJI_CUSTOMEMOJIPAYLOAD'].fields_by_name['file_content']._serialized_options = b'\xe0A\x04\xe0A\x02'
    _globals['_CUSTOMEMOJI_CUSTOMEMOJIPAYLOAD'].fields_by_name['filename']._loaded_options = None
    _globals['_CUSTOMEMOJI_CUSTOMEMOJIPAYLOAD'].fields_by_name['filename']._serialized_options = b'\xe0A\x04\xe0A\x02'
    _globals['_CUSTOMEMOJI'].fields_by_name['name']._loaded_options = None
    _globals['_CUSTOMEMOJI'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CUSTOMEMOJI'].fields_by_name['uid']._loaded_options = None
    _globals['_CUSTOMEMOJI'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_CUSTOMEMOJI'].fields_by_name['emoji_name']._loaded_options = None
    _globals['_CUSTOMEMOJI'].fields_by_name['emoji_name']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_CUSTOMEMOJI'].fields_by_name['temporary_image_uri']._loaded_options = None
    _globals['_CUSTOMEMOJI'].fields_by_name['temporary_image_uri']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMEMOJI'].fields_by_name['payload']._loaded_options = None
    _globals['_CUSTOMEMOJI'].fields_by_name['payload']._serialized_options = b'\xe0A\x04\xe0A\x01'
    _globals['_CUSTOMEMOJI']._loaded_options = None
    _globals['_CUSTOMEMOJI']._serialized_options = b'\xeaAY\n\x1fchat.googleapis.com/CustomEmoji\x12\x1bcustomEmojis/{custom_emoji}*\x0ccustomEmojis2\x0bcustomEmoji'
    _globals['_EMOJIREACTIONSUMMARY'].fields_by_name['emoji']._loaded_options = None
    _globals['_EMOJIREACTIONSUMMARY'].fields_by_name['emoji']._serialized_options = b'\xe0A\x03'
    _globals['_EMOJIREACTIONSUMMARY'].fields_by_name['reaction_count']._loaded_options = None
    _globals['_EMOJIREACTIONSUMMARY'].fields_by_name['reaction_count']._serialized_options = b'\xe0A\x03'
    _globals['_CREATEREACTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREACTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\x12\x1cchat.googleapis.com/Reaction'
    _globals['_CREATEREACTIONREQUEST'].fields_by_name['reaction']._loaded_options = None
    _globals['_CREATEREACTIONREQUEST'].fields_by_name['reaction']._serialized_options = b'\xe0A\x02'
    _globals['_LISTREACTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREACTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\x12\x1cchat.googleapis.com/Reaction'
    _globals['_LISTREACTIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTREACTIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREACTIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTREACTIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREACTIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTREACTIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEREACTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEREACTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cchat.googleapis.com/Reaction'
    _globals['_CREATECUSTOMEMOJIREQUEST'].fields_by_name['custom_emoji']._loaded_options = None
    _globals['_CREATECUSTOMEMOJIREQUEST'].fields_by_name['custom_emoji']._serialized_options = b'\xe0A\x02'
    _globals['_GETCUSTOMEMOJIREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCUSTOMEMOJIREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fchat.googleapis.com/CustomEmoji'
    _globals['_LISTCUSTOMEMOJISREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCUSTOMEMOJISREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCUSTOMEMOJISREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCUSTOMEMOJISREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCUSTOMEMOJISREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCUSTOMEMOJISREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCUSTOMEMOJISRESPONSE'].fields_by_name['custom_emojis']._loaded_options = None
    _globals['_LISTCUSTOMEMOJISRESPONSE'].fields_by_name['custom_emojis']._serialized_options = b'\xe0A\x06'
    _globals['_DELETECUSTOMEMOJIREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECUSTOMEMOJIREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fchat.googleapis.com/CustomEmoji'
    _globals['_REACTION']._serialized_start = 166
    _globals['_REACTION']._serialized_end = 370
    _globals['_EMOJI']._serialized_start = 372
    _globals['_EMOJI']._serialized_end = 467
    _globals['_CUSTOMEMOJI']._serialized_start = 470
    _globals['_CUSTOMEMOJI']._serialized_end = 835
    _globals['_CUSTOMEMOJI_CUSTOMEMOJIPAYLOAD']._serialized_start = 665
    _globals['_CUSTOMEMOJI_CUSTOMEMOJIPAYLOAD']._serialized_end = 741
    _globals['_EMOJIREACTIONSUMMARY']._serialized_start = 837
    _globals['_EMOJIREACTIONSUMMARY']._serialized_end = 955
    _globals['_CREATEREACTIONREQUEST']._serialized_start = 957
    _globals['_CREATEREACTIONREQUEST']._serialized_end = 1083
    _globals['_LISTREACTIONSREQUEST']._serialized_start = 1086
    _globals['_LISTREACTIONSREQUEST']._serialized_end = 1232
    _globals['_LISTREACTIONSRESPONSE']._serialized_start = 1234
    _globals['_LISTREACTIONSRESPONSE']._serialized_end = 1327
    _globals['_DELETEREACTIONREQUEST']._serialized_start = 1329
    _globals['_DELETEREACTIONREQUEST']._serialized_end = 1404
    _globals['_CREATECUSTOMEMOJIREQUEST']._serialized_start = 1406
    _globals['_CREATECUSTOMEMOJIREQUEST']._serialized_end = 1488
    _globals['_GETCUSTOMEMOJIREQUEST']._serialized_start = 1490
    _globals['_GETCUSTOMEMOJIREQUEST']._serialized_end = 1568
    _globals['_LISTCUSTOMEMOJISREQUEST']._serialized_start = 1570
    _globals['_LISTCUSTOMEMOJISREQUEST']._serialized_end = 1665
    _globals['_LISTCUSTOMEMOJISRESPONSE']._serialized_start = 1667
    _globals['_LISTCUSTOMEMOJISRESPONSE']._serialized_end = 1775
    _globals['_DELETECUSTOMEMOJIREQUEST']._serialized_start = 1777
    _globals['_DELETECUSTOMEMOJIREQUEST']._serialized_end = 1858