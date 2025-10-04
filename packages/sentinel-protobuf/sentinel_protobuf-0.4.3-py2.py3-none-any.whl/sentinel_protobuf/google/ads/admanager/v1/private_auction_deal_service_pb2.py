"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/private_auction_deal_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import private_auction_deal_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_private__auction__deal__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/admanager/v1/private_auction_deal_service.proto\x12\x17google.ads.admanager.v1\x1a;google/ads/admanager/v1/private_auction_deal_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"a\n\x1cGetPrivateAuctionDealRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+admanager.googleapis.com/PrivateAuctionDeal"\xca\x01\n\x1eListPrivateAuctionDealsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04skip\x18\x06 \x01(\x05B\x03\xe0A\x01"\x9a\x01\n\x1fListPrivateAuctionDealsResponse\x12J\n\x15private_auction_deals\x18\x01 \x03(\x0b2+.google.ads.admanager.v1.PrivateAuctionDeal\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\xab\x01\n\x1fCreatePrivateAuctionDealRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x12N\n\x14private_auction_deal\x18\x02 \x01(\x0b2+.google.ads.admanager.v1.PrivateAuctionDealB\x03\xe0A\x02"\xa7\x01\n\x1fUpdatePrivateAuctionDealRequest\x12N\n\x14private_auction_deal\x18\x01 \x01(\x0b2+.google.ads.admanager.v1.PrivateAuctionDealB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x022\xe0\x07\n\x19PrivateAuctionDealService\x12\xb7\x01\n\x15GetPrivateAuctionDeal\x125.google.ads.admanager.v1.GetPrivateAuctionDealRequest\x1a+.google.ads.admanager.v1.PrivateAuctionDeal":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=networks/*/privateAuctionDeals/*}\x12\xca\x01\n\x17ListPrivateAuctionDeals\x127.google.ads.admanager.v1.ListPrivateAuctionDealsRequest\x1a8.google.ads.admanager.v1.ListPrivateAuctionDealsResponse"<\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=networks/*}/privateAuctionDeals\x12\xea\x01\n\x18CreatePrivateAuctionDeal\x128.google.ads.admanager.v1.CreatePrivateAuctionDealRequest\x1a+.google.ads.admanager.v1.PrivateAuctionDeal"g\xdaA\x1bparent,private_auction_deal\x82\xd3\xe4\x93\x02C"+/v1/{parent=networks/*}/privateAuctionDeals:\x14private_auction_deal\x12\x85\x02\n\x18UpdatePrivateAuctionDeal\x128.google.ads.admanager.v1.UpdatePrivateAuctionDealRequest\x1a+.google.ads.admanager.v1.PrivateAuctionDeal"\x81\x01\xdaA private_auction_deal,update_mask\x82\xd3\xe4\x93\x02X2@/v1/{private_auction_deal.name=networks/*/privateAuctionDeals/*}:\x14private_auction_deal\x1aG\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanagerB\xd2\x01\n\x1bcom.google.ads.admanager.v1B\x1ePrivateAuctionDealServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.private_auction_deal_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x1ePrivateAuctionDealServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GETPRIVATEAUCTIONDEALREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPRIVATEAUCTIONDEALREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+admanager.googleapis.com/PrivateAuctionDeal'
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEPRIVATEAUCTIONDEALREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPRIVATEAUCTIONDEALREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_CREATEPRIVATEAUCTIONDEALREQUEST'].fields_by_name['private_auction_deal']._loaded_options = None
    _globals['_CREATEPRIVATEAUCTIONDEALREQUEST'].fields_by_name['private_auction_deal']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPRIVATEAUCTIONDEALREQUEST'].fields_by_name['private_auction_deal']._loaded_options = None
    _globals['_UPDATEPRIVATEAUCTIONDEALREQUEST'].fields_by_name['private_auction_deal']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPRIVATEAUCTIONDEALREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPRIVATEAUCTIONDEALREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_PRIVATEAUCTIONDEALSERVICE']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEALSERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanager'
    _globals['_PRIVATEAUCTIONDEALSERVICE'].methods_by_name['GetPrivateAuctionDeal']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEALSERVICE'].methods_by_name['GetPrivateAuctionDeal']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=networks/*/privateAuctionDeals/*}'
    _globals['_PRIVATEAUCTIONDEALSERVICE'].methods_by_name['ListPrivateAuctionDeals']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEALSERVICE'].methods_by_name['ListPrivateAuctionDeals']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=networks/*}/privateAuctionDeals'
    _globals['_PRIVATEAUCTIONDEALSERVICE'].methods_by_name['CreatePrivateAuctionDeal']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEALSERVICE'].methods_by_name['CreatePrivateAuctionDeal']._serialized_options = b'\xdaA\x1bparent,private_auction_deal\x82\xd3\xe4\x93\x02C"+/v1/{parent=networks/*}/privateAuctionDeals:\x14private_auction_deal'
    _globals['_PRIVATEAUCTIONDEALSERVICE'].methods_by_name['UpdatePrivateAuctionDeal']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEALSERVICE'].methods_by_name['UpdatePrivateAuctionDeal']._serialized_options = b'\xdaA private_auction_deal,update_mask\x82\xd3\xe4\x93\x02X2@/v1/{private_auction_deal.name=networks/*/privateAuctionDeals/*}:\x14private_auction_deal'
    _globals['_GETPRIVATEAUCTIONDEALREQUEST']._serialized_start = 297
    _globals['_GETPRIVATEAUCTIONDEALREQUEST']._serialized_end = 394
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST']._serialized_start = 397
    _globals['_LISTPRIVATEAUCTIONDEALSREQUEST']._serialized_end = 599
    _globals['_LISTPRIVATEAUCTIONDEALSRESPONSE']._serialized_start = 602
    _globals['_LISTPRIVATEAUCTIONDEALSRESPONSE']._serialized_end = 756
    _globals['_CREATEPRIVATEAUCTIONDEALREQUEST']._serialized_start = 759
    _globals['_CREATEPRIVATEAUCTIONDEALREQUEST']._serialized_end = 930
    _globals['_UPDATEPRIVATEAUCTIONDEALREQUEST']._serialized_start = 933
    _globals['_UPDATEPRIVATEAUCTIONDEALREQUEST']._serialized_end = 1100
    _globals['_PRIVATEAUCTIONDEALSERVICE']._serialized_start = 1103
    _globals['_PRIVATEAUCTIONDEALSERVICE']._serialized_end = 2095