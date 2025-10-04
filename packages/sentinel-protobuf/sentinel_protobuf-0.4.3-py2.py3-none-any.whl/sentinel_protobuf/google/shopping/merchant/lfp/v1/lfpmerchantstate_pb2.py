"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/lfp/v1/lfpmerchantstate.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/shopping/merchant/lfp/v1/lfpmerchantstate.proto\x12\x1fgoogle.shopping.merchant.lfp.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc7\x0e\n\x10LfpMerchantState\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x13\n\x0blinked_gbps\x18\x02 \x01(\x03\x12Z\n\x0cstore_states\x18\x03 \x03(\x0b2?.google.shopping.merchant.lfp.v1.LfpMerchantState.LfpStoreStateB\x03\xe0A\x03\x12Y\n\x0finventory_stats\x18\x04 \x01(\x0b2@.google.shopping.merchant.lfp.v1.LfpMerchantState.InventoryStats\x12[\n\x10country_settings\x18\x05 \x03(\x0b2A.google.shopping.merchant.lfp.v1.LfpMerchantState.CountrySettings\x1a\xb8\x02\n\rLfpStoreState\x12\x1a\n\nstore_code\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12o\n\x0ematching_state\x18\x02 \x01(\x0e2R.google.shopping.merchant.lfp.v1.LfpMerchantState.LfpStoreState.StoreMatchingStateB\x03\xe0A\x03\x12\x1b\n\x13matching_state_hint\x18\x03 \x01(\t"}\n\x12StoreMatchingState\x12$\n STORE_MATCHING_STATE_UNSPECIFIED\x10\x00\x12 \n\x1cSTORE_MATCHING_STATE_MATCHED\x10\x01\x12\x1f\n\x1bSTORE_MATCHING_STATE_FAILED\x10\x02\x1a\x88\x01\n\x0eInventoryStats\x12\x19\n\x11submitted_entries\x18\x01 \x01(\x03\x12"\n\x1asubmitted_in_stock_entries\x18\x02 \x01(\x03\x12\x1b\n\x13unsubmitted_entries\x18\x03 \x01(\x03\x12\x1a\n\x12submitted_products\x18\x04 \x01(\x03\x1a\x9c\x07\n\x0fCountrySettings\x12\x18\n\x0bregion_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12#\n\x1bfree_local_listings_enabled\x18\x02 \x01(\x08\x12#\n\x1blocal_inventory_ads_enabled\x18\x03 \x01(\x08\x12~\n\x1cinventory_verification_state\x18\x04 \x01(\x0e2S.google.shopping.merchant.lfp.v1.LfpMerchantState.CountrySettings.VerificationStateB\x03\xe0A\x03\x12q\n\x11product_page_type\x18\x05 \x01(\x0e2Q.google.shopping.merchant.lfp.v1.LfpMerchantState.CountrySettings.ProductPageTypeB\x03\xe0A\x03\x12\x84\x01\n"instock_serving_verification_state\x18\x06 \x01(\x0e2S.google.shopping.merchant.lfp.v1.LfpMerchantState.CountrySettings.VerificationStateB\x03\xe0A\x03\x12\x83\x01\n!pickup_serving_verification_state\x18\x07 \x01(\x0e2S.google.shopping.merchant.lfp.v1.LfpMerchantState.CountrySettings.VerificationStateB\x03\xe0A\x03"\xa1\x01\n\x11VerificationState\x12"\n\x1eVERIFICATION_STATE_UNSPECIFIED\x10\x00\x12#\n\x1fVERIFICATION_STATE_NOT_APPROVED\x10\x01\x12"\n\x1eVERIFICATION_STATE_IN_PROGRESS\x10\x02\x12\x1f\n\x1bVERIFICATION_STATE_APPROVED\x10\x03"\x80\x01\n\x0fProductPageType\x12!\n\x1dPRODUCT_PAGE_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rGOOGLE_HOSTED\x10\x01\x12\x13\n\x0fMERCHANT_HOSTED\x10\x02\x12"\n\x1eMERCHANT_HOSTED_STORE_SPECIFIC\x10\x03:\x91\x01\xeaA\x8d\x01\n+merchantapi.googleapis.com/LfpMerchantState\x129accounts/{account}/lfpMerchantStates/{lfp_merchant_state}*\x11lfpMerchantStates2\x10lfpMerchantState"_\n\x1aGetLfpMerchantStateRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/LfpMerchantState2\xa8\x02\n\x17LfpMerchantStateService\x12\xc3\x01\n\x13GetLfpMerchantState\x12;.google.shopping.merchant.lfp.v1.GetLfpMerchantStateRequest\x1a1.google.shopping.merchant.lfp.v1.LfpMerchantState"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/lfp/v1/{name=accounts/*/lfpMerchantStates/*}\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xe5\x01\n#com.google.shopping.merchant.lfp.v1B\x15LfpMerchantStateProtoP\x01Z;cloud.google.com/go/shopping/merchant/lfp/apiv1/lfppb;lfppb\xaa\x02\x1fGoogle.Shopping.Merchant.Lfp.V1\xca\x02\x1fGoogle\\Shopping\\Merchant\\Lfp\\V1\xea\x02#Google::Shopping::Merchant::Lfp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.lfp.v1.lfpmerchantstate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.shopping.merchant.lfp.v1B\x15LfpMerchantStateProtoP\x01Z;cloud.google.com/go/shopping/merchant/lfp/apiv1/lfppb;lfppb\xaa\x02\x1fGoogle.Shopping.Merchant.Lfp.V1\xca\x02\x1fGoogle\\Shopping\\Merchant\\Lfp\\V1\xea\x02#Google::Shopping::Merchant::Lfp::V1'
    _globals['_LFPMERCHANTSTATE_LFPSTORESTATE'].fields_by_name['store_code']._loaded_options = None
    _globals['_LFPMERCHANTSTATE_LFPSTORESTATE'].fields_by_name['store_code']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_LFPMERCHANTSTATE_LFPSTORESTATE'].fields_by_name['matching_state']._loaded_options = None
    _globals['_LFPMERCHANTSTATE_LFPSTORESTATE'].fields_by_name['matching_state']._serialized_options = b'\xe0A\x03'
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS'].fields_by_name['region_code']._loaded_options = None
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS'].fields_by_name['region_code']._serialized_options = b'\xe0A\x02'
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS'].fields_by_name['inventory_verification_state']._loaded_options = None
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS'].fields_by_name['inventory_verification_state']._serialized_options = b'\xe0A\x03'
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS'].fields_by_name['product_page_type']._loaded_options = None
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS'].fields_by_name['product_page_type']._serialized_options = b'\xe0A\x03'
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS'].fields_by_name['instock_serving_verification_state']._loaded_options = None
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS'].fields_by_name['instock_serving_verification_state']._serialized_options = b'\xe0A\x03'
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS'].fields_by_name['pickup_serving_verification_state']._loaded_options = None
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS'].fields_by_name['pickup_serving_verification_state']._serialized_options = b'\xe0A\x03'
    _globals['_LFPMERCHANTSTATE'].fields_by_name['name']._loaded_options = None
    _globals['_LFPMERCHANTSTATE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_LFPMERCHANTSTATE'].fields_by_name['store_states']._loaded_options = None
    _globals['_LFPMERCHANTSTATE'].fields_by_name['store_states']._serialized_options = b'\xe0A\x03'
    _globals['_LFPMERCHANTSTATE']._loaded_options = None
    _globals['_LFPMERCHANTSTATE']._serialized_options = b'\xeaA\x8d\x01\n+merchantapi.googleapis.com/LfpMerchantState\x129accounts/{account}/lfpMerchantStates/{lfp_merchant_state}*\x11lfpMerchantStates2\x10lfpMerchantState'
    _globals['_GETLFPMERCHANTSTATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETLFPMERCHANTSTATEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/LfpMerchantState'
    _globals['_LFPMERCHANTSTATESERVICE']._loaded_options = None
    _globals['_LFPMERCHANTSTATESERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_LFPMERCHANTSTATESERVICE'].methods_by_name['GetLfpMerchantState']._loaded_options = None
    _globals['_LFPMERCHANTSTATESERVICE'].methods_by_name['GetLfpMerchantState']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/lfp/v1/{name=accounts/*/lfpMerchantStates/*}'
    _globals['_LFPMERCHANTSTATE']._serialized_start = 207
    _globals['_LFPMERCHANTSTATE']._serialized_end = 2070
    _globals['_LFPMERCHANTSTATE_LFPSTORESTATE']._serialized_start = 544
    _globals['_LFPMERCHANTSTATE_LFPSTORESTATE']._serialized_end = 856
    _globals['_LFPMERCHANTSTATE_LFPSTORESTATE_STOREMATCHINGSTATE']._serialized_start = 731
    _globals['_LFPMERCHANTSTATE_LFPSTORESTATE_STOREMATCHINGSTATE']._serialized_end = 856
    _globals['_LFPMERCHANTSTATE_INVENTORYSTATS']._serialized_start = 859
    _globals['_LFPMERCHANTSTATE_INVENTORYSTATS']._serialized_end = 995
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS']._serialized_start = 998
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS']._serialized_end = 1922
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS_VERIFICATIONSTATE']._serialized_start = 1630
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS_VERIFICATIONSTATE']._serialized_end = 1791
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS_PRODUCTPAGETYPE']._serialized_start = 1794
    _globals['_LFPMERCHANTSTATE_COUNTRYSETTINGS_PRODUCTPAGETYPE']._serialized_end = 1922
    _globals['_GETLFPMERCHANTSTATEREQUEST']._serialized_start = 2072
    _globals['_GETLFPMERCHANTSTATEREQUEST']._serialized_end = 2167
    _globals['_LFPMERCHANTSTATESERVICE']._serialized_start = 2170
    _globals['_LFPMERCHANTSTATESERVICE']._serialized_end = 2466