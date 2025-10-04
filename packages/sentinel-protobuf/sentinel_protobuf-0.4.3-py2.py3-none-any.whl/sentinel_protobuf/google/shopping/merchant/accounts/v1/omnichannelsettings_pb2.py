"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/omnichannelsettings.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/shopping/merchant/accounts/v1/omnichannelsettings.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xc7\x06\n\x12OmnichannelSetting\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1b\n\x0bregion_code\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12W\n\x08lsf_type\x18\x0c \x01(\x0e2@.google.shopping.merchant.accounts.v1.OmnichannelSetting.LsfTypeB\x03\xe0A\x02\x12D\n\x08in_stock\x18\r \x01(\x0b2-.google.shopping.merchant.accounts.v1.InStockB\x03\xe0A\x01\x12A\n\x06pickup\x18\x0e \x01(\x0b2,.google.shopping.merchant.accounts.v1.PickupB\x03\xe0A\x01\x12D\n\x08lfp_link\x18\x05 \x01(\x0b2-.google.shopping.merchant.accounts.v1.LfpLinkB\x03\xe0A\x03\x12H\n\x03odo\x18\x06 \x01(\x0b26.google.shopping.merchant.accounts.v1.OnDisplayToOrderB\x03\xe0A\x01\x12?\n\x05about\x18\x07 \x01(\x0b2+.google.shopping.merchant.accounts.v1.AboutB\x03\xe0A\x01\x12`\n\x16inventory_verification\x18\x08 \x01(\x0b2;.google.shopping.merchant.accounts.v1.InventoryVerificationB\x03\xe0A\x01"O\n\x07LsfType\x12\x18\n\x14LSF_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05GHLSF\x10\x01\x12\x0f\n\x0bMHLSF_BASIC\x10\x02\x12\x0e\n\nMHLSF_FULL\x10\x03:\x9a\x01\xeaA\x96\x01\n-merchantapi.googleapis.com/OmnichannelSetting\x12<accounts/{account}/omnichannelSettings/{omnichannel_setting}*\x13omnichannelSettings2\x12omnichannelSetting"g\n\x0bReviewState"X\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\n\n\x06FAILED\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\x13\n\x0fACTION_REQUIRED\x10\x04"h\n\x07InStock\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x01\x12K\n\x05state\x18\x02 \x01(\x0e27.google.shopping.merchant.accounts.v1.ReviewState.StateB\x03\xe0A\x03"g\n\x06Pickup\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\x05state\x18\x02 \x01(\x0e27.google.shopping.merchant.accounts.v1.ReviewState.StateB\x03\xe0A\x03"\x93\x01\n\x07LfpLink\x12\x19\n\x0clfp_provider\x18\x01 \x01(\tB\x03\xe0A\x02\x12 \n\x13external_account_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12K\n\x05state\x18\x03 \x01(\x0e27.google.shopping.merchant.accounts.v1.ReviewState.StateB\x03\xe0A\x03"q\n\x10OnDisplayToOrder\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\x05state\x18\x02 \x01(\x0e27.google.shopping.merchant.accounts.v1.ReviewState.StateB\x03\xe0A\x03"f\n\x05About\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\x05state\x18\x02 \x01(\x0e27.google.shopping.merchant.accounts.v1.ReviewState.StateB\x03\xe0A\x03"\xe3\x02\n\x15InventoryVerification\x12U\n\x05state\x18\x01 \x01(\x0e2A.google.shopping.merchant.accounts.v1.InventoryVerification.StateB\x03\xe0A\x03\x12\x14\n\x07contact\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rcontact_email\x18\x03 \x01(\tB\x03\xe0A\x02\x12S\n\rcontact_state\x18\x04 \x01(\x0e27.google.shopping.merchant.accounts.v1.ReviewState.StateB\x03\xe0A\x03"l\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x13\n\x0fACTION_REQUIRED\x10\x01\x12\x0c\n\x08INACTIVE\x10\x05\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\r\n\tSUSPENDED\x10\x04"c\n\x1cGetOmnichannelSettingRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-merchantapi.googleapis.com/OmnichannelSetting"\x8d\x01\n\x1eListOmnichannelSettingsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x92\x01\n\x1fListOmnichannelSettingsResponse\x12V\n\x14omnichannel_settings\x18\x01 \x03(\x0b28.google.shopping.merchant.accounts.v1.OmnichannelSetting\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb9\x01\n\x1fCreateOmnichannelSettingRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12Z\n\x13omnichannel_setting\x18\x02 \x01(\x0b28.google.shopping.merchant.accounts.v1.OmnichannelSettingB\x03\xe0A\x02"\xb3\x01\n\x1fUpdateOmnichannelSettingRequest\x12Z\n\x13omnichannel_setting\x18\x01 \x01(\x0b28.google.shopping.merchant.accounts.v1.OmnichannelSettingB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"j\n#RequestInventoryVerificationRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-merchantapi.googleapis.com/OmnichannelSetting"}\n$RequestInventoryVerificationResponse\x12U\n\x13omnichannel_setting\x18\x01 \x01(\x0b28.google.shopping.merchant.accounts.v1.OmnichannelSetting2\x85\x0b\n\x1aOmnichannelSettingsService\x12\xda\x01\n\x15GetOmnichannelSetting\x12B.google.shopping.merchant.accounts.v1.GetOmnichannelSettingRequest\x1a8.google.shopping.merchant.accounts.v1.OmnichannelSetting"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/accounts/v1/{name=accounts/*/omnichannelSettings/*}\x12\xed\x01\n\x17ListOmnichannelSettings\x12D.google.shopping.merchant.accounts.v1.ListOmnichannelSettingsRequest\x1aE.google.shopping.merchant.accounts.v1.ListOmnichannelSettingsResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/accounts/v1/{parent=accounts/*}/omnichannelSettings\x12\x8b\x02\n\x18CreateOmnichannelSetting\x12E.google.shopping.merchant.accounts.v1.CreateOmnichannelSettingRequest\x1a8.google.shopping.merchant.accounts.v1.OmnichannelSetting"n\xdaA\x1aparent,omnichannel_setting\x82\xd3\xe4\x93\x02K"4/accounts/v1/{parent=accounts/*}/omnichannelSettings:\x13omnichannel_setting\x12\xa5\x02\n\x18UpdateOmnichannelSetting\x12E.google.shopping.merchant.accounts.v1.UpdateOmnichannelSettingRequest\x1a8.google.shopping.merchant.accounts.v1.OmnichannelSetting"\x87\x01\xdaA\x1fomnichannel_setting,update_mask\x82\xd3\xe4\x93\x02_2H/accounts/v1/{omnichannel_setting.name=accounts/*/omnichannelSettings/*}:\x13omnichannel_setting\x12\x9a\x02\n\x1cRequestInventoryVerification\x12I.google.shopping.merchant.accounts.v1.RequestInventoryVerificationRequest\x1aJ.google.shopping.merchant.accounts.v1.RequestInventoryVerificationResponse"c\xdaA\x04name\x82\xd3\xe4\x93\x02V"Q/accounts/v1/{name=accounts/*/omnichannelSettings/*}:requestInventoryVerification:\x01*\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x8b\x02\n(com.google.shopping.merchant.accounts.v1B\x18OmnichannelSettingsProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.omnichannelsettings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B\x18OmnichannelSettingsProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_OMNICHANNELSETTING'].fields_by_name['name']._loaded_options = None
    _globals['_OMNICHANNELSETTING'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_OMNICHANNELSETTING'].fields_by_name['region_code']._loaded_options = None
    _globals['_OMNICHANNELSETTING'].fields_by_name['region_code']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_OMNICHANNELSETTING'].fields_by_name['lsf_type']._loaded_options = None
    _globals['_OMNICHANNELSETTING'].fields_by_name['lsf_type']._serialized_options = b'\xe0A\x02'
    _globals['_OMNICHANNELSETTING'].fields_by_name['in_stock']._loaded_options = None
    _globals['_OMNICHANNELSETTING'].fields_by_name['in_stock']._serialized_options = b'\xe0A\x01'
    _globals['_OMNICHANNELSETTING'].fields_by_name['pickup']._loaded_options = None
    _globals['_OMNICHANNELSETTING'].fields_by_name['pickup']._serialized_options = b'\xe0A\x01'
    _globals['_OMNICHANNELSETTING'].fields_by_name['lfp_link']._loaded_options = None
    _globals['_OMNICHANNELSETTING'].fields_by_name['lfp_link']._serialized_options = b'\xe0A\x03'
    _globals['_OMNICHANNELSETTING'].fields_by_name['odo']._loaded_options = None
    _globals['_OMNICHANNELSETTING'].fields_by_name['odo']._serialized_options = b'\xe0A\x01'
    _globals['_OMNICHANNELSETTING'].fields_by_name['about']._loaded_options = None
    _globals['_OMNICHANNELSETTING'].fields_by_name['about']._serialized_options = b'\xe0A\x01'
    _globals['_OMNICHANNELSETTING'].fields_by_name['inventory_verification']._loaded_options = None
    _globals['_OMNICHANNELSETTING'].fields_by_name['inventory_verification']._serialized_options = b'\xe0A\x01'
    _globals['_OMNICHANNELSETTING']._loaded_options = None
    _globals['_OMNICHANNELSETTING']._serialized_options = b'\xeaA\x96\x01\n-merchantapi.googleapis.com/OmnichannelSetting\x12<accounts/{account}/omnichannelSettings/{omnichannel_setting}*\x13omnichannelSettings2\x12omnichannelSetting'
    _globals['_INSTOCK'].fields_by_name['uri']._loaded_options = None
    _globals['_INSTOCK'].fields_by_name['uri']._serialized_options = b'\xe0A\x01'
    _globals['_INSTOCK'].fields_by_name['state']._loaded_options = None
    _globals['_INSTOCK'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PICKUP'].fields_by_name['uri']._loaded_options = None
    _globals['_PICKUP'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_PICKUP'].fields_by_name['state']._loaded_options = None
    _globals['_PICKUP'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_LFPLINK'].fields_by_name['lfp_provider']._loaded_options = None
    _globals['_LFPLINK'].fields_by_name['lfp_provider']._serialized_options = b'\xe0A\x02'
    _globals['_LFPLINK'].fields_by_name['external_account_id']._loaded_options = None
    _globals['_LFPLINK'].fields_by_name['external_account_id']._serialized_options = b'\xe0A\x02'
    _globals['_LFPLINK'].fields_by_name['state']._loaded_options = None
    _globals['_LFPLINK'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ONDISPLAYTOORDER'].fields_by_name['uri']._loaded_options = None
    _globals['_ONDISPLAYTOORDER'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_ONDISPLAYTOORDER'].fields_by_name['state']._loaded_options = None
    _globals['_ONDISPLAYTOORDER'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ABOUT'].fields_by_name['uri']._loaded_options = None
    _globals['_ABOUT'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_ABOUT'].fields_by_name['state']._loaded_options = None
    _globals['_ABOUT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INVENTORYVERIFICATION'].fields_by_name['state']._loaded_options = None
    _globals['_INVENTORYVERIFICATION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INVENTORYVERIFICATION'].fields_by_name['contact']._loaded_options = None
    _globals['_INVENTORYVERIFICATION'].fields_by_name['contact']._serialized_options = b'\xe0A\x02'
    _globals['_INVENTORYVERIFICATION'].fields_by_name['contact_email']._loaded_options = None
    _globals['_INVENTORYVERIFICATION'].fields_by_name['contact_email']._serialized_options = b'\xe0A\x02'
    _globals['_INVENTORYVERIFICATION'].fields_by_name['contact_state']._loaded_options = None
    _globals['_INVENTORYVERIFICATION'].fields_by_name['contact_state']._serialized_options = b'\xe0A\x03'
    _globals['_GETOMNICHANNELSETTINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETOMNICHANNELSETTINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-merchantapi.googleapis.com/OmnichannelSetting'
    _globals['_LISTOMNICHANNELSETTINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTOMNICHANNELSETTINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_LISTOMNICHANNELSETTINGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTOMNICHANNELSETTINGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTOMNICHANNELSETTINGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTOMNICHANNELSETTINGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEOMNICHANNELSETTINGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEOMNICHANNELSETTINGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_CREATEOMNICHANNELSETTINGREQUEST'].fields_by_name['omnichannel_setting']._loaded_options = None
    _globals['_CREATEOMNICHANNELSETTINGREQUEST'].fields_by_name['omnichannel_setting']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEOMNICHANNELSETTINGREQUEST'].fields_by_name['omnichannel_setting']._loaded_options = None
    _globals['_UPDATEOMNICHANNELSETTINGREQUEST'].fields_by_name['omnichannel_setting']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEOMNICHANNELSETTINGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEOMNICHANNELSETTINGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_REQUESTINVENTORYVERIFICATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REQUESTINVENTORYVERIFICATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-merchantapi.googleapis.com/OmnichannelSetting'
    _globals['_OMNICHANNELSETTINGSSERVICE']._loaded_options = None
    _globals['_OMNICHANNELSETTINGSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_OMNICHANNELSETTINGSSERVICE'].methods_by_name['GetOmnichannelSetting']._loaded_options = None
    _globals['_OMNICHANNELSETTINGSSERVICE'].methods_by_name['GetOmnichannelSetting']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/accounts/v1/{name=accounts/*/omnichannelSettings/*}'
    _globals['_OMNICHANNELSETTINGSSERVICE'].methods_by_name['ListOmnichannelSettings']._loaded_options = None
    _globals['_OMNICHANNELSETTINGSSERVICE'].methods_by_name['ListOmnichannelSettings']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/accounts/v1/{parent=accounts/*}/omnichannelSettings'
    _globals['_OMNICHANNELSETTINGSSERVICE'].methods_by_name['CreateOmnichannelSetting']._loaded_options = None
    _globals['_OMNICHANNELSETTINGSSERVICE'].methods_by_name['CreateOmnichannelSetting']._serialized_options = b'\xdaA\x1aparent,omnichannel_setting\x82\xd3\xe4\x93\x02K"4/accounts/v1/{parent=accounts/*}/omnichannelSettings:\x13omnichannel_setting'
    _globals['_OMNICHANNELSETTINGSSERVICE'].methods_by_name['UpdateOmnichannelSetting']._loaded_options = None
    _globals['_OMNICHANNELSETTINGSSERVICE'].methods_by_name['UpdateOmnichannelSetting']._serialized_options = b'\xdaA\x1fomnichannel_setting,update_mask\x82\xd3\xe4\x93\x02_2H/accounts/v1/{omnichannel_setting.name=accounts/*/omnichannelSettings/*}:\x13omnichannel_setting'
    _globals['_OMNICHANNELSETTINGSSERVICE'].methods_by_name['RequestInventoryVerification']._loaded_options = None
    _globals['_OMNICHANNELSETTINGSSERVICE'].methods_by_name['RequestInventoryVerification']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02V"Q/accounts/v1/{name=accounts/*/omnichannelSettings/*}:requestInventoryVerification:\x01*'
    _globals['_OMNICHANNELSETTING']._serialized_start = 254
    _globals['_OMNICHANNELSETTING']._serialized_end = 1093
    _globals['_OMNICHANNELSETTING_LSFTYPE']._serialized_start = 857
    _globals['_OMNICHANNELSETTING_LSFTYPE']._serialized_end = 936
    _globals['_REVIEWSTATE']._serialized_start = 1095
    _globals['_REVIEWSTATE']._serialized_end = 1198
    _globals['_REVIEWSTATE_STATE']._serialized_start = 1110
    _globals['_REVIEWSTATE_STATE']._serialized_end = 1198
    _globals['_INSTOCK']._serialized_start = 1200
    _globals['_INSTOCK']._serialized_end = 1304
    _globals['_PICKUP']._serialized_start = 1306
    _globals['_PICKUP']._serialized_end = 1409
    _globals['_LFPLINK']._serialized_start = 1412
    _globals['_LFPLINK']._serialized_end = 1559
    _globals['_ONDISPLAYTOORDER']._serialized_start = 1561
    _globals['_ONDISPLAYTOORDER']._serialized_end = 1674
    _globals['_ABOUT']._serialized_start = 1676
    _globals['_ABOUT']._serialized_end = 1778
    _globals['_INVENTORYVERIFICATION']._serialized_start = 1781
    _globals['_INVENTORYVERIFICATION']._serialized_end = 2136
    _globals['_INVENTORYVERIFICATION_STATE']._serialized_start = 2028
    _globals['_INVENTORYVERIFICATION_STATE']._serialized_end = 2136
    _globals['_GETOMNICHANNELSETTINGREQUEST']._serialized_start = 2138
    _globals['_GETOMNICHANNELSETTINGREQUEST']._serialized_end = 2237
    _globals['_LISTOMNICHANNELSETTINGSREQUEST']._serialized_start = 2240
    _globals['_LISTOMNICHANNELSETTINGSREQUEST']._serialized_end = 2381
    _globals['_LISTOMNICHANNELSETTINGSRESPONSE']._serialized_start = 2384
    _globals['_LISTOMNICHANNELSETTINGSRESPONSE']._serialized_end = 2530
    _globals['_CREATEOMNICHANNELSETTINGREQUEST']._serialized_start = 2533
    _globals['_CREATEOMNICHANNELSETTINGREQUEST']._serialized_end = 2718
    _globals['_UPDATEOMNICHANNELSETTINGREQUEST']._serialized_start = 2721
    _globals['_UPDATEOMNICHANNELSETTINGREQUEST']._serialized_end = 2900
    _globals['_REQUESTINVENTORYVERIFICATIONREQUEST']._serialized_start = 2902
    _globals['_REQUESTINVENTORYVERIFICATIONREQUEST']._serialized_end = 3008
    _globals['_REQUESTINVENTORYVERIFICATIONRESPONSE']._serialized_start = 3010
    _globals['_REQUESTINVENTORYVERIFICATIONRESPONSE']._serialized_end = 3135
    _globals['_OMNICHANNELSETTINGSSERVICE']._serialized_start = 3138
    _globals['_OMNICHANNELSETTINGSSERVICE']._serialized_end = 4551