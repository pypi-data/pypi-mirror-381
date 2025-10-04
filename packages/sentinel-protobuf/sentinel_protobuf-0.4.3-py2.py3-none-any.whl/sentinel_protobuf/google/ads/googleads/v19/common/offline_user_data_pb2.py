"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/common/offline_user_data.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import consent_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_consent__pb2
from ......google.ads.googleads.v19.enums import user_identifier_source_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_user__identifier__source__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/googleads/v19/common/offline_user_data.proto\x12\x1fgoogle.ads.googleads.v19.common\x1a-google/ads/googleads/v19/common/consent.proto\x1a;google/ads/googleads/v19/enums/user_identifier_source.proto\x1a\x1fgoogle/api/field_behavior.proto"\xd0\x02\n\x16OfflineUserAddressInfo\x12\x1e\n\x11hashed_first_name\x18\x07 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10hashed_last_name\x18\x08 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04city\x18\t \x01(\tH\x02\x88\x01\x01\x12\x12\n\x05state\x18\n \x01(\tH\x03\x88\x01\x01\x12\x19\n\x0ccountry_code\x18\x0b \x01(\tH\x04\x88\x01\x01\x12\x18\n\x0bpostal_code\x18\x0c \x01(\tH\x05\x88\x01\x01\x12"\n\x15hashed_street_address\x18\r \x01(\tH\x06\x88\x01\x01B\x14\n\x12_hashed_first_nameB\x13\n\x11_hashed_last_nameB\x07\n\x05_cityB\x08\n\x06_stateB\x0f\n\r_country_codeB\x0e\n\x0c_postal_codeB\x18\n\x16_hashed_street_address"\xc9\x02\n\x0eUserIdentifier\x12m\n\x16user_identifier_source\x18\x06 \x01(\x0e2M.google.ads.googleads.v19.enums.UserIdentifierSourceEnum.UserIdentifierSource\x12\x16\n\x0chashed_email\x18\x07 \x01(\tH\x00\x12\x1d\n\x13hashed_phone_number\x18\x08 \x01(\tH\x00\x12\x13\n\tmobile_id\x18\t \x01(\tH\x00\x12\x1d\n\x13third_party_user_id\x18\n \x01(\tH\x00\x12O\n\x0caddress_info\x18\x05 \x01(\x0b27.google.ads.googleads.v19.common.OfflineUserAddressInfoH\x00B\x0c\n\nidentifier"\xe0\x03\n\x14TransactionAttribute\x12"\n\x15transaction_date_time\x18\x08 \x01(\tH\x00\x88\x01\x01\x12&\n\x19transaction_amount_micros\x18\t \x01(\x01H\x01\x88\x01\x01\x12\x1a\n\rcurrency_code\x18\n \x01(\tH\x02\x88\x01\x01\x12\x1e\n\x11conversion_action\x18\x0b \x01(\tH\x03\x88\x01\x01\x12\x15\n\x08order_id\x18\x0c \x01(\tH\x04\x88\x01\x01\x12H\n\x0fstore_attribute\x18\x06 \x01(\x0b2/.google.ads.googleads.v19.common.StoreAttribute\x12\x19\n\x0ccustom_value\x18\r \x01(\tH\x05\x88\x01\x01\x12F\n\x0eitem_attribute\x18\x0e \x01(\x0b2..google.ads.googleads.v19.common.ItemAttributeB\x18\n\x16_transaction_date_timeB\x1c\n\x1a_transaction_amount_microsB\x10\n\x0e_currency_codeB\x14\n\x12_conversion_actionB\x0b\n\t_order_idB\x0f\n\r_custom_value"8\n\x0eStoreAttribute\x12\x17\n\nstore_code\x18\x02 \x01(\tH\x00\x88\x01\x01B\r\n\x0b_store_code"\x89\x01\n\rItemAttribute\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12\x18\n\x0bmerchant_id\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12\x14\n\x0ccountry_code\x18\x03 \x01(\t\x12\x15\n\rlanguage_code\x18\x04 \x01(\t\x12\x10\n\x08quantity\x18\x05 \x01(\x03B\x0e\n\x0c_merchant_id"\xbf\x02\n\x08UserData\x12I\n\x10user_identifiers\x18\x01 \x03(\x0b2/.google.ads.googleads.v19.common.UserIdentifier\x12T\n\x15transaction_attribute\x18\x02 \x01(\x0b25.google.ads.googleads.v19.common.TransactionAttribute\x12F\n\x0euser_attribute\x18\x03 \x01(\x0b2..google.ads.googleads.v19.common.UserAttribute\x12>\n\x07consent\x18\x04 \x01(\x0b2(.google.ads.googleads.v19.common.ConsentH\x00\x88\x01\x01B\n\n\x08_consent"\x8c\x04\n\rUserAttribute\x12"\n\x15lifetime_value_micros\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12"\n\x15lifetime_value_bucket\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x1f\n\x17last_purchase_date_time\x18\x03 \x01(\t\x12\x1e\n\x16average_purchase_count\x18\x04 \x01(\x05\x12%\n\x1daverage_purchase_value_micros\x18\x05 \x01(\x03\x12\x1d\n\x15acquisition_date_time\x18\x06 \x01(\t\x12O\n\x10shopping_loyalty\x18\x07 \x01(\x0b20.google.ads.googleads.v19.common.ShoppingLoyaltyH\x02\x88\x01\x01\x12\x1c\n\x0flifecycle_stage\x18\x08 \x01(\tB\x03\xe0A\x01\x12%\n\x18first_purchase_date_time\x18\t \x01(\tB\x03\xe0A\x01\x12M\n\x0fevent_attribute\x18\n \x03(\x0b2/.google.ads.googleads.v19.common.EventAttributeB\x03\xe0A\x01B\x18\n\x16_lifetime_value_microsB\x18\n\x16_lifetime_value_bucketB\x13\n\x11_shopping_loyalty"\x94\x01\n\x0eEventAttribute\x12\x12\n\x05event\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0fevent_date_time\x18\x02 \x01(\tB\x03\xe0A\x02\x12P\n\x0eitem_attribute\x18\x03 \x03(\x0b23.google.ads.googleads.v19.common.EventItemAttributeB\x03\xe0A\x02"*\n\x12EventItemAttribute\x12\x14\n\x07item_id\x18\x01 \x01(\tB\x03\xe0A\x01"=\n\x0fShoppingLoyalty\x12\x19\n\x0cloyalty_tier\x18\x01 \x01(\tH\x00\x88\x01\x01B\x0f\n\r_loyalty_tier"\x91\x01\n\x1dCustomerMatchUserListMetadata\x12\x16\n\tuser_list\x18\x02 \x01(\tH\x00\x88\x01\x01\x12>\n\x07consent\x18\x03 \x01(\x0b2(.google.ads.googleads.v19.common.ConsentH\x01\x88\x01\x01B\x0c\n\n_user_listB\n\n\x08_consent"\x97\x02\n\x12StoreSalesMetadata\x12\x1d\n\x10loyalty_fraction\x18\x05 \x01(\x01H\x00\x88\x01\x01\x12(\n\x1btransaction_upload_fraction\x18\x06 \x01(\x01H\x01\x88\x01\x01\x12\x17\n\ncustom_key\x18\x07 \x01(\tH\x02\x88\x01\x01\x12[\n\x14third_party_metadata\x18\x03 \x01(\x0b2=.google.ads.googleads.v19.common.StoreSalesThirdPartyMetadataB\x13\n\x11_loyalty_fractionB\x1e\n\x1c_transaction_upload_fractionB\r\n\x0b_custom_key"\x98\x03\n\x1cStoreSalesThirdPartyMetadata\x12(\n\x1badvertiser_upload_date_time\x18\x07 \x01(\tH\x00\x88\x01\x01\x12\'\n\x1avalid_transaction_fraction\x18\x08 \x01(\x01H\x01\x88\x01\x01\x12#\n\x16partner_match_fraction\x18\t \x01(\x01H\x02\x88\x01\x01\x12$\n\x17partner_upload_fraction\x18\n \x01(\x01H\x03\x88\x01\x01\x12"\n\x15bridge_map_version_id\x18\x0b \x01(\tH\x04\x88\x01\x01\x12\x17\n\npartner_id\x18\x0c \x01(\x03H\x05\x88\x01\x01B\x1e\n\x1c_advertiser_upload_date_timeB\x1d\n\x1b_valid_transaction_fractionB\x19\n\x17_partner_match_fractionB\x1a\n\x18_partner_upload_fractionB\x18\n\x16_bridge_map_version_idB\r\n\x0b_partner_idB\xf4\x01\n#com.google.ads.googleads.v19.commonB\x14OfflineUserDataProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.common.offline_user_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v19.commonB\x14OfflineUserDataProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Common'
    _globals['_USERATTRIBUTE'].fields_by_name['lifecycle_stage']._loaded_options = None
    _globals['_USERATTRIBUTE'].fields_by_name['lifecycle_stage']._serialized_options = b'\xe0A\x01'
    _globals['_USERATTRIBUTE'].fields_by_name['first_purchase_date_time']._loaded_options = None
    _globals['_USERATTRIBUTE'].fields_by_name['first_purchase_date_time']._serialized_options = b'\xe0A\x01'
    _globals['_USERATTRIBUTE'].fields_by_name['event_attribute']._loaded_options = None
    _globals['_USERATTRIBUTE'].fields_by_name['event_attribute']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTATTRIBUTE'].fields_by_name['event']._loaded_options = None
    _globals['_EVENTATTRIBUTE'].fields_by_name['event']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTATTRIBUTE'].fields_by_name['event_date_time']._loaded_options = None
    _globals['_EVENTATTRIBUTE'].fields_by_name['event_date_time']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTATTRIBUTE'].fields_by_name['item_attribute']._loaded_options = None
    _globals['_EVENTATTRIBUTE'].fields_by_name['item_attribute']._serialized_options = b'\xe0A\x02'
    _globals['_EVENTITEMATTRIBUTE'].fields_by_name['item_id']._loaded_options = None
    _globals['_EVENTITEMATTRIBUTE'].fields_by_name['item_id']._serialized_options = b'\xe0A\x01'
    _globals['_OFFLINEUSERADDRESSINFO']._serialized_start = 234
    _globals['_OFFLINEUSERADDRESSINFO']._serialized_end = 570
    _globals['_USERIDENTIFIER']._serialized_start = 573
    _globals['_USERIDENTIFIER']._serialized_end = 902
    _globals['_TRANSACTIONATTRIBUTE']._serialized_start = 905
    _globals['_TRANSACTIONATTRIBUTE']._serialized_end = 1385
    _globals['_STOREATTRIBUTE']._serialized_start = 1387
    _globals['_STOREATTRIBUTE']._serialized_end = 1443
    _globals['_ITEMATTRIBUTE']._serialized_start = 1446
    _globals['_ITEMATTRIBUTE']._serialized_end = 1583
    _globals['_USERDATA']._serialized_start = 1586
    _globals['_USERDATA']._serialized_end = 1905
    _globals['_USERATTRIBUTE']._serialized_start = 1908
    _globals['_USERATTRIBUTE']._serialized_end = 2432
    _globals['_EVENTATTRIBUTE']._serialized_start = 2435
    _globals['_EVENTATTRIBUTE']._serialized_end = 2583
    _globals['_EVENTITEMATTRIBUTE']._serialized_start = 2585
    _globals['_EVENTITEMATTRIBUTE']._serialized_end = 2627
    _globals['_SHOPPINGLOYALTY']._serialized_start = 2629
    _globals['_SHOPPINGLOYALTY']._serialized_end = 2690
    _globals['_CUSTOMERMATCHUSERLISTMETADATA']._serialized_start = 2693
    _globals['_CUSTOMERMATCHUSERLISTMETADATA']._serialized_end = 2838
    _globals['_STORESALESMETADATA']._serialized_start = 2841
    _globals['_STORESALESMETADATA']._serialized_end = 3120
    _globals['_STORESALESTHIRDPARTYMETADATA']._serialized_start = 3123
    _globals['_STORESALESTHIRDPARTYMETADATA']._serialized_end = 3531