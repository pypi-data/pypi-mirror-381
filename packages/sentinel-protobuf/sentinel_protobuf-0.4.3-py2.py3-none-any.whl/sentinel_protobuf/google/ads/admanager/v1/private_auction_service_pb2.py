"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/private_auction_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import private_auction_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_private__auction__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/ads/admanager/v1/private_auction_service.proto\x12\x17google.ads.admanager.v1\x1a6google/ads/admanager/v1/private_auction_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"Y\n\x18GetPrivateAuctionRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'admanager.googleapis.com/PrivateAuction"\xc6\x01\n\x1aListPrivateAuctionsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04skip\x18\x06 \x01(\x05B\x03\xe0A\x01"\x8d\x01\n\x1bListPrivateAuctionsResponse\x12A\n\x10private_auctions\x18\x01 \x03(\x0b2\'.google.ads.admanager.v1.PrivateAuction\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\x9e\x01\n\x1bCreatePrivateAuctionRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x12E\n\x0fprivate_auction\x18\x02 \x01(\x0b2\'.google.ads.admanager.v1.PrivateAuctionB\x03\xe0A\x02"\x9a\x01\n\x1bUpdatePrivateAuctionRequest\x12E\n\x0fprivate_auction\x18\x01 \x01(\x0b2\'.google.ads.admanager.v1.PrivateAuctionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x022\x82\x07\n\x15PrivateAuctionService\x12\xa7\x01\n\x11GetPrivateAuction\x121.google.ads.admanager.v1.GetPrivateAuctionRequest\x1a\'.google.ads.admanager.v1.PrivateAuction"6\xdaA\x04name\x82\xd3\xe4\x93\x02)\x12\'/v1/{name=networks/*/privateAuctions/*}\x12\xba\x01\n\x13ListPrivateAuctions\x123.google.ads.admanager.v1.ListPrivateAuctionsRequest\x1a4.google.ads.admanager.v1.ListPrivateAuctionsResponse"8\xdaA\x06parent\x82\xd3\xe4\x93\x02)\x12\'/v1/{parent=networks/*}/privateAuctions\x12\xd0\x01\n\x14CreatePrivateAuction\x124.google.ads.admanager.v1.CreatePrivateAuctionRequest\x1a\'.google.ads.admanager.v1.PrivateAuction"Y\xdaA\x16parent,private_auction\x82\xd3\xe4\x93\x02:"\'/v1/{parent=networks/*}/privateAuctions:\x0fprivate_auction\x12\xe5\x01\n\x14UpdatePrivateAuction\x124.google.ads.admanager.v1.UpdatePrivateAuctionRequest\x1a\'.google.ads.admanager.v1.PrivateAuction"n\xdaA\x1bprivate_auction,update_mask\x82\xd3\xe4\x93\x02J27/v1/{private_auction.name=networks/*/privateAuctions/*}:\x0fprivate_auction\x1aG\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanagerB\xce\x01\n\x1bcom.google.ads.admanager.v1B\x1aPrivateAuctionServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.private_auction_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x1aPrivateAuctionServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GETPRIVATEAUCTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPRIVATEAUCTIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'admanager.googleapis.com/PrivateAuction"
    _globals['_LISTPRIVATEAUCTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPRIVATEAUCTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_LISTPRIVATEAUCTIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPRIVATEAUCTIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRIVATEAUCTIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPRIVATEAUCTIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRIVATEAUCTIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTPRIVATEAUCTIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRIVATEAUCTIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTPRIVATEAUCTIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRIVATEAUCTIONSREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTPRIVATEAUCTIONSREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEPRIVATEAUCTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPRIVATEAUCTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_CREATEPRIVATEAUCTIONREQUEST'].fields_by_name['private_auction']._loaded_options = None
    _globals['_CREATEPRIVATEAUCTIONREQUEST'].fields_by_name['private_auction']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPRIVATEAUCTIONREQUEST'].fields_by_name['private_auction']._loaded_options = None
    _globals['_UPDATEPRIVATEAUCTIONREQUEST'].fields_by_name['private_auction']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPRIVATEAUCTIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPRIVATEAUCTIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_PRIVATEAUCTIONSERVICE']._loaded_options = None
    _globals['_PRIVATEAUCTIONSERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanager'
    _globals['_PRIVATEAUCTIONSERVICE'].methods_by_name['GetPrivateAuction']._loaded_options = None
    _globals['_PRIVATEAUCTIONSERVICE'].methods_by_name['GetPrivateAuction']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02)\x12'/v1/{name=networks/*/privateAuctions/*}"
    _globals['_PRIVATEAUCTIONSERVICE'].methods_by_name['ListPrivateAuctions']._loaded_options = None
    _globals['_PRIVATEAUCTIONSERVICE'].methods_by_name['ListPrivateAuctions']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02)\x12'/v1/{parent=networks/*}/privateAuctions"
    _globals['_PRIVATEAUCTIONSERVICE'].methods_by_name['CreatePrivateAuction']._loaded_options = None
    _globals['_PRIVATEAUCTIONSERVICE'].methods_by_name['CreatePrivateAuction']._serialized_options = b'\xdaA\x16parent,private_auction\x82\xd3\xe4\x93\x02:"\'/v1/{parent=networks/*}/privateAuctions:\x0fprivate_auction'
    _globals['_PRIVATEAUCTIONSERVICE'].methods_by_name['UpdatePrivateAuction']._loaded_options = None
    _globals['_PRIVATEAUCTIONSERVICE'].methods_by_name['UpdatePrivateAuction']._serialized_options = b'\xdaA\x1bprivate_auction,update_mask\x82\xd3\xe4\x93\x02J27/v1/{private_auction.name=networks/*/privateAuctions/*}:\x0fprivate_auction'
    _globals['_GETPRIVATEAUCTIONREQUEST']._serialized_start = 287
    _globals['_GETPRIVATEAUCTIONREQUEST']._serialized_end = 376
    _globals['_LISTPRIVATEAUCTIONSREQUEST']._serialized_start = 379
    _globals['_LISTPRIVATEAUCTIONSREQUEST']._serialized_end = 577
    _globals['_LISTPRIVATEAUCTIONSRESPONSE']._serialized_start = 580
    _globals['_LISTPRIVATEAUCTIONSRESPONSE']._serialized_end = 721
    _globals['_CREATEPRIVATEAUCTIONREQUEST']._serialized_start = 724
    _globals['_CREATEPRIVATEAUCTIONREQUEST']._serialized_end = 882
    _globals['_UPDATEPRIVATEAUCTIONREQUEST']._serialized_start = 885
    _globals['_UPDATEPRIVATEAUCTIONREQUEST']._serialized_end = 1039
    _globals['_PRIVATEAUCTIONSERVICE']._serialized_start = 1042
    _globals['_PRIVATEAUCTIONSERVICE']._serialized_end = 1940