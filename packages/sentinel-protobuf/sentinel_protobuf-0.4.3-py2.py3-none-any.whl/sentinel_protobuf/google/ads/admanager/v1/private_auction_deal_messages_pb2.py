"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/private_auction_deal_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import deal_buyer_permission_type_enum_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_deal__buyer__permission__type__enum__pb2
from .....google.ads.admanager.v1 import private_marketplace_enums_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_private__marketplace__enums__pb2
from .....google.ads.admanager.v1 import size_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_size__pb2
from .....google.ads.admanager.v1 import targeting_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_targeting__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/admanager/v1/private_auction_deal_messages.proto\x12\x17google.ads.admanager.v1\x1a=google/ads/admanager/v1/deal_buyer_permission_type_enum.proto\x1a7google/ads/admanager/v1/private_marketplace_enums.proto\x1a"google/ads/admanager/v1/size.proto\x1a\'google/ads/admanager/v1/targeting.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/type/money.proto"\xe0\x0b\n\x12PrivateAuctionDeal\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12)\n\x17private_auction_deal_id\x18\x02 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12$\n\x12private_auction_id\x18\x03 \x01(\x03B\x03\xe0A\x05H\x01\x88\x01\x01\x12.\n\x1cprivate_auction_display_name\x18\x14 \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12"\n\x10buyer_account_id\x18\x04 \x01(\x03B\x03\xe0A\x05H\x03\x88\x01\x01\x12"\n\x10external_deal_id\x18\x05 \x01(\x03B\x03\xe0A\x03H\x04\x88\x01\x01\x12?\n\ttargeting\x18\x06 \x01(\x0b2".google.ads.admanager.v1.TargetingB\x03\xe0A\x01H\x05\x88\x01\x01\x126\n\x08end_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01H\x06\x88\x01\x01\x121\n\x0bfloor_price\x18\t \x01(\x0b2\x12.google.type.MoneyB\x03\xe0A\x02H\x07\x88\x01\x01\x12:\n\x0ecreative_sizes\x18\x12 \x03(\x0b2\x1d.google.ads.admanager.v1.SizeB\x03\xe0A\x01\x12p\n\x06status\x18\n \x01(\x0e2V.google.ads.admanager.v1.PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatusB\x03\xe0A\x03H\x08\x88\x01\x01\x12*\n\x18auction_priority_enabled\x18\x0b \x01(\x08B\x03\xe0A\x01H\t\x88\x01\x01\x12(\n\x16block_override_enabled\x18\x0c \x01(\x08B\x03\xe0A\x01H\n\x88\x01\x01\x12u\n\x15buyer_permission_type\x18\r \x01(\x0e2L.google.ads.admanager.v1.DealBuyerPermissionTypeEnum.DealBuyerPermissionTypeB\x03\xe0A\x01H\x0b\x88\x01\x01\x12S\n\nbuyer_data\x18\x0e \x01(\x0b25.google.ads.admanager.v1.PrivateAuctionDeal.BuyerDataB\x03\xe0A\x01H\x0c\x88\x01\x01\x129\n\x0bcreate_time\x18\x0f \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03H\r\x88\x01\x01\x129\n\x0bupdate_time\x18\x10 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03H\x0e\x88\x01\x01\x1a&\n\tBuyerData\x12\x19\n\x0cbuyer_emails\x18\x01 \x03(\tB\x03\xe0A\x01:\x9e\x01\xeaA\x9a\x01\n+admanager.googleapis.com/PrivateAuctionDeal\x12Bnetworks/{network_code}/privateAuctionDeals/{private_auction_deal}*\x13privateAuctionDeals2\x12privateAuctionDealB\x1a\n\x18_private_auction_deal_idB\x15\n\x13_private_auction_idB\x1f\n\x1d_private_auction_display_nameB\x13\n\x11_buyer_account_idB\x13\n\x11_external_deal_idB\x0c\n\n_targetingB\x0b\n\t_end_timeB\x0e\n\x0c_floor_priceB\t\n\x07_statusB\x1b\n\x19_auction_priority_enabledB\x19\n\x17_block_override_enabledB\x18\n\x16_buyer_permission_typeB\r\n\x0b_buyer_dataB\x0e\n\x0c_create_timeB\x0e\n\x0c_update_timeB\xd3\x01\n\x1bcom.google.ads.admanager.v1B\x1fPrivateAuctionDealMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.private_auction_deal_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x1fPrivateAuctionDealMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_PRIVATEAUCTIONDEAL_BUYERDATA'].fields_by_name['buyer_emails']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL_BUYERDATA'].fields_by_name['buyer_emails']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['name']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['private_auction_deal_id']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['private_auction_deal_id']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['private_auction_id']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['private_auction_id']._serialized_options = b'\xe0A\x05'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['private_auction_display_name']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['private_auction_display_name']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['buyer_account_id']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['buyer_account_id']._serialized_options = b'\xe0A\x05'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['external_deal_id']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['external_deal_id']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['targeting']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['targeting']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['end_time']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['end_time']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['floor_price']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['floor_price']._serialized_options = b'\xe0A\x02'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['creative_sizes']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['creative_sizes']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['status']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['auction_priority_enabled']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['auction_priority_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['block_override_enabled']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['block_override_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['buyer_permission_type']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['buyer_permission_type']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['buyer_data']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['buyer_data']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['create_time']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['update_time']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEAUCTIONDEAL']._loaded_options = None
    _globals['_PRIVATEAUCTIONDEAL']._serialized_options = b'\xeaA\x9a\x01\n+admanager.googleapis.com/PrivateAuctionDeal\x12Bnetworks/{network_code}/privateAuctionDeals/{private_auction_deal}*\x13privateAuctionDeals2\x12privateAuctionDeal'
    _globals['_PRIVATEAUCTIONDEAL']._serialized_start = 404
    _globals['_PRIVATEAUCTIONDEAL']._serialized_end = 1908
    _globals['_PRIVATEAUCTIONDEAL_BUYERDATA']._serialized_start = 1400
    _globals['_PRIVATEAUCTIONDEAL_BUYERDATA']._serialized_end = 1438