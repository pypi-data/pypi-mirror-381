"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/private_auction_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/admanager/v1/private_auction_messages.proto\x12\x17google.ads.admanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd0\x04\n\x0ePrivateAuction\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12$\n\x12private_auction_id\x18\x02 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1e\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x02H\x01\x88\x01\x01\x12\x1d\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01H\x02\x88\x01\x01\x12C\n\x14seller_contact_users\x18\t \x03(\tB%\xe0A\x01\xfaA\x1f\n\x1dadmanager.googleapis.com/User\x12\x1a\n\x08archived\x18\x06 \x01(\x08B\x03\xe0A\x03H\x03\x88\x01\x01\x129\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03H\x04\x88\x01\x01\x129\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03H\x05\x88\x01\x01:\x89\x01\xeaA\x85\x01\n\'admanager.googleapis.com/PrivateAuction\x129networks/{network_code}/privateAuctions/{private_auction}*\x0fprivateAuctions2\x0eprivateAuctionB\x15\n\x13_private_auction_idB\x0f\n\r_display_nameB\x0e\n\x0c_descriptionB\x0b\n\t_archivedB\x0e\n\x0c_create_timeB\x0e\n\x0c_update_timeB\xcf\x01\n\x1bcom.google.ads.admanager.v1B\x1bPrivateAuctionMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.private_auction_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x1bPrivateAuctionMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_PRIVATEAUCTION'].fields_by_name['name']._loaded_options = None
    _globals['_PRIVATEAUCTION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PRIVATEAUCTION'].fields_by_name['private_auction_id']._loaded_options = None
    _globals['_PRIVATEAUCTION'].fields_by_name['private_auction_id']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEAUCTION'].fields_by_name['display_name']._loaded_options = None
    _globals['_PRIVATEAUCTION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_PRIVATEAUCTION'].fields_by_name['description']._loaded_options = None
    _globals['_PRIVATEAUCTION'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVATEAUCTION'].fields_by_name['seller_contact_users']._loaded_options = None
    _globals['_PRIVATEAUCTION'].fields_by_name['seller_contact_users']._serialized_options = b'\xe0A\x01\xfaA\x1f\n\x1dadmanager.googleapis.com/User'
    _globals['_PRIVATEAUCTION'].fields_by_name['archived']._loaded_options = None
    _globals['_PRIVATEAUCTION'].fields_by_name['archived']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEAUCTION'].fields_by_name['create_time']._loaded_options = None
    _globals['_PRIVATEAUCTION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEAUCTION'].fields_by_name['update_time']._loaded_options = None
    _globals['_PRIVATEAUCTION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEAUCTION']._loaded_options = None
    _globals['_PRIVATEAUCTION']._serialized_options = b"\xeaA\x85\x01\n'admanager.googleapis.com/PrivateAuction\x129networks/{network_code}/privateAuctions/{private_auction}*\x0fprivateAuctions2\x0eprivateAuction"
    _globals['_PRIVATEAUCTION']._serialized_start = 177
    _globals['_PRIVATEAUCTION']._serialized_end = 769