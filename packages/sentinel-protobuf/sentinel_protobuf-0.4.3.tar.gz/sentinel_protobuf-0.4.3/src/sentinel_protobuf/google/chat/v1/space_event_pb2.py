"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/chat/v1/space_event.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.chat.v1 import event_payload_pb2 as google_dot_chat_dot_v1_dot_event__payload__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/chat/v1/space_event.proto\x12\x0egoogle.chat.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a"google/chat/v1/event_payload.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xce\r\n\nSpaceEvent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\nevent_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x12\n\nevent_type\x18\x06 \x01(\t\x12M\n\x1amessage_created_event_data\x18\x0c \x01(\x0b2\'.google.chat.v1.MessageCreatedEventDataH\x00\x12M\n\x1amessage_updated_event_data\x18\r \x01(\x0b2\'.google.chat.v1.MessageUpdatedEventDataH\x00\x12M\n\x1amessage_deleted_event_data\x18\x0e \x01(\x0b2\'.google.chat.v1.MessageDeletedEventDataH\x00\x12X\n message_batch_created_event_data\x18\x1a \x01(\x0b2,.google.chat.v1.MessageBatchCreatedEventDataH\x00\x12X\n message_batch_updated_event_data\x18\x1b \x01(\x0b2,.google.chat.v1.MessageBatchUpdatedEventDataH\x00\x12X\n message_batch_deleted_event_data\x18\x1c \x01(\x0b2,.google.chat.v1.MessageBatchDeletedEventDataH\x00\x12I\n\x18space_updated_event_data\x18\x0f \x01(\x0b2%.google.chat.v1.SpaceUpdatedEventDataH\x00\x12T\n\x1espace_batch_updated_event_data\x18\x1d \x01(\x0b2*.google.chat.v1.SpaceBatchUpdatedEventDataH\x00\x12S\n\x1dmembership_created_event_data\x18\x11 \x01(\x0b2*.google.chat.v1.MembershipCreatedEventDataH\x00\x12S\n\x1dmembership_updated_event_data\x18\x12 \x01(\x0b2*.google.chat.v1.MembershipUpdatedEventDataH\x00\x12T\n\x1dmembership_deleted_event_data\x18\xdb\x01 \x01(\x0b2*.google.chat.v1.MembershipDeletedEventDataH\x00\x12^\n#membership_batch_created_event_data\x18\x1f \x01(\x0b2/.google.chat.v1.MembershipBatchCreatedEventDataH\x00\x12^\n#membership_batch_updated_event_data\x18  \x01(\x0b2/.google.chat.v1.MembershipBatchUpdatedEventDataH\x00\x12^\n#membership_batch_deleted_event_data\x18! \x01(\x0b2/.google.chat.v1.MembershipBatchDeletedEventDataH\x00\x12O\n\x1breaction_created_event_data\x18\x15 \x01(\x0b2(.google.chat.v1.ReactionCreatedEventDataH\x00\x12O\n\x1breaction_deleted_event_data\x18\x16 \x01(\x0b2(.google.chat.v1.ReactionDeletedEventDataH\x00\x12Z\n!reaction_batch_created_event_data\x18" \x01(\x0b2-.google.chat.v1.ReactionBatchCreatedEventDataH\x00\x12Z\n!reaction_batch_deleted_event_data\x18# \x01(\x0b2-.google.chat.v1.ReactionBatchDeletedEventDataH\x00:M\xeaAJ\n\x1echat.googleapis.com/SpaceEvent\x12(spaces/{space}/spaceEvents/{space_event}B\t\n\x07payload"L\n\x14GetSpaceEventRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1echat.googleapis.com/SpaceEvent"\x96\x01\n\x16ListSpaceEventsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1echat.googleapis.com/SpaceEvent\x12\x16\n\tpage_size\x18\x05 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x08 \x01(\tB\x03\xe0A\x02"d\n\x17ListSpaceEventsResponse\x120\n\x0cspace_events\x18\x01 \x03(\x0b2\x1a.google.chat.v1.SpaceEvent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\tB\x9a\x01\n\x12com.google.chat.v1B\x0fSpaceEventProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.space_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x0fSpaceEventProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_SPACEEVENT']._loaded_options = None
    _globals['_SPACEEVENT']._serialized_options = b'\xeaAJ\n\x1echat.googleapis.com/SpaceEvent\x12(spaces/{space}/spaceEvents/{space_event}'
    _globals['_GETSPACEEVENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSPACEEVENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1echat.googleapis.com/SpaceEvent'
    _globals['_LISTSPACEEVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSPACEEVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1echat.googleapis.com/SpaceEvent'
    _globals['_LISTSPACEEVENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSPACEEVENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSPACEEVENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSPACEEVENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSPACEEVENTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTSPACEEVENTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_SPACEEVENT']._serialized_start = 182
    _globals['_SPACEEVENT']._serialized_end = 1924
    _globals['_GETSPACEEVENTREQUEST']._serialized_start = 1926
    _globals['_GETSPACEEVENTREQUEST']._serialized_end = 2002
    _globals['_LISTSPACEEVENTSREQUEST']._serialized_start = 2005
    _globals['_LISTSPACEEVENTSREQUEST']._serialized_end = 2155
    _globals['_LISTSPACEEVENTSRESPONSE']._serialized_start = 2157
    _globals['_LISTSPACEEVENTSRESPONSE']._serialized_end = 2257