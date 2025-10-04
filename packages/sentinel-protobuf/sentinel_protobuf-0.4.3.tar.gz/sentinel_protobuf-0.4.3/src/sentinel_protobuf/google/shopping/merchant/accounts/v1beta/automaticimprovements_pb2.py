"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1beta/automaticimprovements.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/shopping/merchant/accounts/v1beta/automaticimprovements.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xac\x04\n\x15AutomaticImprovements\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12Y\n\x0citem_updates\x18\x02 \x01(\x0b2>.google.shopping.merchant.accounts.v1beta.AutomaticItemUpdatesH\x00\x88\x01\x01\x12e\n\x12image_improvements\x18\x03 \x01(\x0b2D.google.shopping.merchant.accounts.v1beta.AutomaticImageImprovementsH\x01\x88\x01\x01\x12k\n\x15shipping_improvements\x18\x04 \x01(\x0b2G.google.shopping.merchant.accounts.v1beta.AutomaticShippingImprovementsH\x02\x88\x01\x01:\x8e\x01\xeaA\x8a\x01\n0merchantapi.googleapis.com/AutomaticImprovements\x12(accounts/{account}/automaticImprovements*\x15automaticImprovements2\x15automaticImprovementsB\x0f\n\r_item_updatesB\x15\n\x13_image_improvementsB\x18\n\x16_shipping_improvements"\xaa\x05\n\x14AutomaticItemUpdates\x12\x8a\x01\n\x1daccount_item_updates_settings\x18\x01 \x01(\x0b2^.google.shopping.merchant.accounts.v1beta.AutomaticItemUpdates.ItemUpdatesAccountLevelSettingsB\x03\xe0A\x01\x12*\n\x1deffective_allow_price_updates\x18\x02 \x01(\x08B\x03\xe0A\x03\x121\n$effective_allow_availability_updates\x18\x03 \x01(\x08B\x03\xe0A\x03\x128\n+effective_allow_strict_availability_updates\x18\x04 \x01(\x08B\x03\xe0A\x03\x12.\n!effective_allow_condition_updates\x18\x05 \x01(\x08B\x03\xe0A\x03\x1a\xbb\x02\n\x1fItemUpdatesAccountLevelSettings\x12 \n\x13allow_price_updates\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\'\n\x1aallow_availability_updates\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12.\n!allow_strict_availability_updates\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12$\n\x17allow_condition_updates\x18\x04 \x01(\x08H\x03\x88\x01\x01B\x16\n\x14_allow_price_updatesB\x1d\n\x1b_allow_availability_updatesB$\n"_allow_strict_availability_updatesB\x1a\n\x18_allow_condition_updates"\xa4\x03\n\x1aAutomaticImageImprovements\x12\xa1\x01\n#account_image_improvements_settings\x18\x01 \x01(\x0b2j.google.shopping.merchant.accounts.v1beta.AutomaticImageImprovements.ImageImprovementsAccountLevelSettingsB\x03\xe0A\x01H\x00\x88\x01\x01\x129\n,effective_allow_automatic_image_improvements\x18\x02 \x01(\x08B\x03\xe0A\x03\x1a\x7f\n%ImageImprovementsAccountLevelSettings\x12/\n"allow_automatic_image_improvements\x18\x01 \x01(\x08H\x00\x88\x01\x01B%\n#_allow_automatic_image_improvementsB&\n$_account_image_improvements_settings"i\n\x1dAutomaticShippingImprovements\x12(\n\x1ballow_shipping_improvements\x18\x01 \x01(\x08H\x00\x88\x01\x01B\x1e\n\x1c_allow_shipping_improvements"i\n\x1fGetAutomaticImprovementsRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0merchantapi.googleapis.com/AutomaticImprovements"\xc0\x01\n"UpdateAutomaticImprovementsRequest\x12d\n\x16automatic_improvements\x18\x01 \x01(\x0b2?.google.shopping.merchant.accounts.v1beta.AutomaticImprovementsB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x022\x9f\x05\n\x1cAutomaticImprovementsService\x12\xef\x01\n\x18GetAutomaticImprovements\x12I.google.shopping.merchant.accounts.v1beta.GetAutomaticImprovementsRequest\x1a?.google.shopping.merchant.accounts.v1beta.AutomaticImprovements"G\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/accounts/v1beta/{name=accounts/*/automaticImprovements}\x12\xc3\x02\n\x1bUpdateAutomaticImprovements\x12L.google.shopping.merchant.accounts.v1beta.UpdateAutomaticImprovementsRequest\x1a?.google.shopping.merchant.accounts.v1beta.AutomaticImprovements"\x94\x01\xdaA"automatic_improvements,update_mask\x82\xd3\xe4\x93\x02i2O/accounts/v1beta/{automatic_improvements.name=accounts/*/automaticImprovements}:\x16automatic_improvements\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x9c\x01\n,com.google.shopping.merchant.accounts.v1betaB\x1aAutomaticImprovementsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.automaticimprovements_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\x1aAutomaticImprovementsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_AUTOMATICIMPROVEMENTS'].fields_by_name['name']._loaded_options = None
    _globals['_AUTOMATICIMPROVEMENTS'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_AUTOMATICIMPROVEMENTS']._loaded_options = None
    _globals['_AUTOMATICIMPROVEMENTS']._serialized_options = b'\xeaA\x8a\x01\n0merchantapi.googleapis.com/AutomaticImprovements\x12(accounts/{account}/automaticImprovements*\x15automaticImprovements2\x15automaticImprovements'
    _globals['_AUTOMATICITEMUPDATES'].fields_by_name['account_item_updates_settings']._loaded_options = None
    _globals['_AUTOMATICITEMUPDATES'].fields_by_name['account_item_updates_settings']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOMATICITEMUPDATES'].fields_by_name['effective_allow_price_updates']._loaded_options = None
    _globals['_AUTOMATICITEMUPDATES'].fields_by_name['effective_allow_price_updates']._serialized_options = b'\xe0A\x03'
    _globals['_AUTOMATICITEMUPDATES'].fields_by_name['effective_allow_availability_updates']._loaded_options = None
    _globals['_AUTOMATICITEMUPDATES'].fields_by_name['effective_allow_availability_updates']._serialized_options = b'\xe0A\x03'
    _globals['_AUTOMATICITEMUPDATES'].fields_by_name['effective_allow_strict_availability_updates']._loaded_options = None
    _globals['_AUTOMATICITEMUPDATES'].fields_by_name['effective_allow_strict_availability_updates']._serialized_options = b'\xe0A\x03'
    _globals['_AUTOMATICITEMUPDATES'].fields_by_name['effective_allow_condition_updates']._loaded_options = None
    _globals['_AUTOMATICITEMUPDATES'].fields_by_name['effective_allow_condition_updates']._serialized_options = b'\xe0A\x03'
    _globals['_AUTOMATICIMAGEIMPROVEMENTS'].fields_by_name['account_image_improvements_settings']._loaded_options = None
    _globals['_AUTOMATICIMAGEIMPROVEMENTS'].fields_by_name['account_image_improvements_settings']._serialized_options = b'\xe0A\x01'
    _globals['_AUTOMATICIMAGEIMPROVEMENTS'].fields_by_name['effective_allow_automatic_image_improvements']._loaded_options = None
    _globals['_AUTOMATICIMAGEIMPROVEMENTS'].fields_by_name['effective_allow_automatic_image_improvements']._serialized_options = b'\xe0A\x03'
    _globals['_GETAUTOMATICIMPROVEMENTSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAUTOMATICIMPROVEMENTSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0merchantapi.googleapis.com/AutomaticImprovements'
    _globals['_UPDATEAUTOMATICIMPROVEMENTSREQUEST'].fields_by_name['automatic_improvements']._loaded_options = None
    _globals['_UPDATEAUTOMATICIMPROVEMENTSREQUEST'].fields_by_name['automatic_improvements']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAUTOMATICIMPROVEMENTSREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEAUTOMATICIMPROVEMENTSREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_AUTOMATICIMPROVEMENTSSERVICE']._loaded_options = None
    _globals['_AUTOMATICIMPROVEMENTSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_AUTOMATICIMPROVEMENTSSERVICE'].methods_by_name['GetAutomaticImprovements']._loaded_options = None
    _globals['_AUTOMATICIMPROVEMENTSSERVICE'].methods_by_name['GetAutomaticImprovements']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/accounts/v1beta/{name=accounts/*/automaticImprovements}'
    _globals['_AUTOMATICIMPROVEMENTSSERVICE'].methods_by_name['UpdateAutomaticImprovements']._loaded_options = None
    _globals['_AUTOMATICIMPROVEMENTSSERVICE'].methods_by_name['UpdateAutomaticImprovements']._serialized_options = b'\xdaA"automatic_improvements,update_mask\x82\xd3\xe4\x93\x02i2O/accounts/v1beta/{automatic_improvements.name=accounts/*/automaticImprovements}:\x16automatic_improvements'
    _globals['_AUTOMATICIMPROVEMENTS']._serialized_start = 264
    _globals['_AUTOMATICIMPROVEMENTS']._serialized_end = 820
    _globals['_AUTOMATICITEMUPDATES']._serialized_start = 823
    _globals['_AUTOMATICITEMUPDATES']._serialized_end = 1505
    _globals['_AUTOMATICITEMUPDATES_ITEMUPDATESACCOUNTLEVELSETTINGS']._serialized_start = 1190
    _globals['_AUTOMATICITEMUPDATES_ITEMUPDATESACCOUNTLEVELSETTINGS']._serialized_end = 1505
    _globals['_AUTOMATICIMAGEIMPROVEMENTS']._serialized_start = 1508
    _globals['_AUTOMATICIMAGEIMPROVEMENTS']._serialized_end = 1928
    _globals['_AUTOMATICIMAGEIMPROVEMENTS_IMAGEIMPROVEMENTSACCOUNTLEVELSETTINGS']._serialized_start = 1761
    _globals['_AUTOMATICIMAGEIMPROVEMENTS_IMAGEIMPROVEMENTSACCOUNTLEVELSETTINGS']._serialized_end = 1888
    _globals['_AUTOMATICSHIPPINGIMPROVEMENTS']._serialized_start = 1930
    _globals['_AUTOMATICSHIPPINGIMPROVEMENTS']._serialized_end = 2035
    _globals['_GETAUTOMATICIMPROVEMENTSREQUEST']._serialized_start = 2037
    _globals['_GETAUTOMATICIMPROVEMENTSREQUEST']._serialized_end = 2142
    _globals['_UPDATEAUTOMATICIMPROVEMENTSREQUEST']._serialized_start = 2145
    _globals['_UPDATEAUTOMATICIMPROVEMENTSREQUEST']._serialized_end = 2337
    _globals['_AUTOMATICIMPROVEMENTSSERVICE']._serialized_start = 2340
    _globals['_AUTOMATICIMPROVEMENTSSERVICE']._serialized_end = 3011