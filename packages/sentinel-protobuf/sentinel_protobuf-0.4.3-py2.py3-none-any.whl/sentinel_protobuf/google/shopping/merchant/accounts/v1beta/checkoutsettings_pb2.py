"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1beta/checkoutsettings.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/shopping/merchant/accounts/v1beta/checkoutsettings.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a google/shopping/type/types.proto"_\n\x1aGetCheckoutSettingsRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/CheckoutSettings"\xc0\x01\n\x1dCreateCheckoutSettingsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+merchantapi.googleapis.com/CheckoutSettings\x12Z\n\x11checkout_settings\x18\x02 \x01(\x0b2:.google.shopping.merchant.accounts.v1beta.CheckoutSettingsB\x03\xe0A\x02"\xb1\x01\n\x1dUpdateCheckoutSettingsRequest\x12Z\n\x11checkout_settings\x18\x01 \x01(\x0b2:.google.shopping.merchant.accounts.v1beta.CheckoutSettingsB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"b\n\x1dDeleteCheckoutSettingsRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/CheckoutSettings"\xe5\t\n\x10CheckoutSettings\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12P\n\x0curi_settings\x18\x02 \x01(\x0b25.google.shopping.merchant.accounts.v1beta.UriSettingsH\x00\x88\x01\x01\x12U\n\x15eligible_destinations\x18\x08 \x03(\x0e21.google.shopping.type.Destination.DestinationEnumB\x03\xe0A\x01\x12v\n\x10enrollment_state\x18\x03 \x01(\x0e2R.google.shopping.merchant.accounts.v1beta.CheckoutSettings.CheckoutEnrollmentStateB\x03\xe0A\x03H\x01\x88\x01\x01\x12n\n\x0creview_state\x18\x04 \x01(\x0e2N.google.shopping.merchant.accounts.v1beta.CheckoutSettings.CheckoutReviewStateB\x03\xe0A\x03H\x02\x88\x01\x01\x12Z\n\x16effective_uri_settings\x18\x05 \x01(\x0b25.google.shopping.merchant.accounts.v1beta.UriSettingsB\x03\xe0A\x03\x12\x80\x01\n\x1aeffective_enrollment_state\x18\x06 \x01(\x0e2R.google.shopping.merchant.accounts.v1beta.CheckoutSettings.CheckoutEnrollmentStateB\x03\xe0A\x03H\x03\x88\x01\x01\x12x\n\x16effective_review_state\x18\x07 \x01(\x0e2N.google.shopping.merchant.accounts.v1beta.CheckoutSettings.CheckoutReviewStateB\x03\xe0A\x03H\x04\x88\x01\x01"o\n\x17CheckoutEnrollmentState\x12)\n%CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01\x12\x0c\n\x08ENROLLED\x10\x02\x12\r\n\tOPTED_OUT\x10\x03"j\n\x13CheckoutReviewState\x12%\n!CHECKOUT_REVIEW_STATE_UNSPECIFIED\x10\x00\x12\r\n\tIN_REVIEW\x10\x01\x12\x0c\n\x08APPROVED\x10\x02\x12\x0f\n\x0bDISAPPROVED\x10\x03:\x85\x01\xeaA\x81\x01\n+merchantapi.googleapis.com/CheckoutSettings\x126accounts/{account}/programs/{program}/checkoutSettings*\x08settings2\x10checkoutSettingsB\x0f\n\r_uri_settingsB\x13\n\x11_enrollment_stateB\x0f\n\r_review_stateB\x1d\n\x1b_effective_enrollment_stateB\x19\n\x17_effective_review_state"[\n\x0bUriSettings\x12\x1f\n\x15checkout_uri_template\x18\x01 \x01(\tH\x00\x12\x1b\n\x11cart_uri_template\x18\x02 \x01(\tH\x00B\x0e\n\x0curi_template2\xdc\x08\n\x17CheckoutSettingsService\x12\xe6\x01\n\x13GetCheckoutSettings\x12D.google.shopping.merchant.accounts.v1beta.GetCheckoutSettingsRequest\x1a:.google.shopping.merchant.accounts.v1beta.CheckoutSettings"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/accounts/v1beta/{name=accounts/*/programs/*/checkoutSettings}\x12\x95\x02\n\x16CreateCheckoutSettings\x12G.google.shopping.merchant.accounts.v1beta.CreateCheckoutSettingsRequest\x1a:.google.shopping.merchant.accounts.v1beta.CheckoutSettings"v\xdaA\x18parent,checkout_settings\x82\xd3\xe4\x93\x02U"@/accounts/v1beta/{parent=accounts/*/programs/*}/checkoutSettings:\x11checkout_settings\x12\xab\x02\n\x16UpdateCheckoutSettings\x12G.google.shopping.merchant.accounts.v1beta.UpdateCheckoutSettingsRequest\x1a:.google.shopping.merchant.accounts.v1beta.CheckoutSettings"\x8b\x01\xdaA\x1dcheckout_settings,update_mask\x82\xd3\xe4\x93\x02e2P/accounts/v1beta/{checkout_settings.name=accounts/*/programs/*/checkoutSettings}:\x11checkout_settings\x12\xc8\x01\n\x16DeleteCheckoutSettings\x12G.google.shopping.merchant.accounts.v1beta.DeleteCheckoutSettingsRequest\x1a\x16.google.protobuf.Empty"M\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/accounts/v1beta/{name=accounts/*/programs/*/checkoutSettings}\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x97\x01\n,com.google.shopping.merchant.accounts.v1betaB\x15CheckoutsettingsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.checkoutsettings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\x15CheckoutsettingsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_GETCHECKOUTSETTINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCHECKOUTSETTINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/CheckoutSettings'
    _globals['_CREATECHECKOUTSETTINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECHECKOUTSETTINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+merchantapi.googleapis.com/CheckoutSettings'
    _globals['_CREATECHECKOUTSETTINGSREQUEST'].fields_by_name['checkout_settings']._loaded_options = None
    _globals['_CREATECHECKOUTSETTINGSREQUEST'].fields_by_name['checkout_settings']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECHECKOUTSETTINGSREQUEST'].fields_by_name['checkout_settings']._loaded_options = None
    _globals['_UPDATECHECKOUTSETTINGSREQUEST'].fields_by_name['checkout_settings']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECHECKOUTSETTINGSREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECHECKOUTSETTINGSREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECHECKOUTSETTINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECHECKOUTSETTINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/CheckoutSettings'
    _globals['_CHECKOUTSETTINGS'].fields_by_name['name']._loaded_options = None
    _globals['_CHECKOUTSETTINGS'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CHECKOUTSETTINGS'].fields_by_name['eligible_destinations']._loaded_options = None
    _globals['_CHECKOUTSETTINGS'].fields_by_name['eligible_destinations']._serialized_options = b'\xe0A\x01'
    _globals['_CHECKOUTSETTINGS'].fields_by_name['enrollment_state']._loaded_options = None
    _globals['_CHECKOUTSETTINGS'].fields_by_name['enrollment_state']._serialized_options = b'\xe0A\x03'
    _globals['_CHECKOUTSETTINGS'].fields_by_name['review_state']._loaded_options = None
    _globals['_CHECKOUTSETTINGS'].fields_by_name['review_state']._serialized_options = b'\xe0A\x03'
    _globals['_CHECKOUTSETTINGS'].fields_by_name['effective_uri_settings']._loaded_options = None
    _globals['_CHECKOUTSETTINGS'].fields_by_name['effective_uri_settings']._serialized_options = b'\xe0A\x03'
    _globals['_CHECKOUTSETTINGS'].fields_by_name['effective_enrollment_state']._loaded_options = None
    _globals['_CHECKOUTSETTINGS'].fields_by_name['effective_enrollment_state']._serialized_options = b'\xe0A\x03'
    _globals['_CHECKOUTSETTINGS'].fields_by_name['effective_review_state']._loaded_options = None
    _globals['_CHECKOUTSETTINGS'].fields_by_name['effective_review_state']._serialized_options = b'\xe0A\x03'
    _globals['_CHECKOUTSETTINGS']._loaded_options = None
    _globals['_CHECKOUTSETTINGS']._serialized_options = b'\xeaA\x81\x01\n+merchantapi.googleapis.com/CheckoutSettings\x126accounts/{account}/programs/{program}/checkoutSettings*\x08settings2\x10checkoutSettings'
    _globals['_CHECKOUTSETTINGSSERVICE']._loaded_options = None
    _globals['_CHECKOUTSETTINGSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_CHECKOUTSETTINGSSERVICE'].methods_by_name['GetCheckoutSettings']._loaded_options = None
    _globals['_CHECKOUTSETTINGSSERVICE'].methods_by_name['GetCheckoutSettings']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/accounts/v1beta/{name=accounts/*/programs/*/checkoutSettings}'
    _globals['_CHECKOUTSETTINGSSERVICE'].methods_by_name['CreateCheckoutSettings']._loaded_options = None
    _globals['_CHECKOUTSETTINGSSERVICE'].methods_by_name['CreateCheckoutSettings']._serialized_options = b'\xdaA\x18parent,checkout_settings\x82\xd3\xe4\x93\x02U"@/accounts/v1beta/{parent=accounts/*/programs/*}/checkoutSettings:\x11checkout_settings'
    _globals['_CHECKOUTSETTINGSSERVICE'].methods_by_name['UpdateCheckoutSettings']._loaded_options = None
    _globals['_CHECKOUTSETTINGSSERVICE'].methods_by_name['UpdateCheckoutSettings']._serialized_options = b'\xdaA\x1dcheckout_settings,update_mask\x82\xd3\xe4\x93\x02e2P/accounts/v1beta/{checkout_settings.name=accounts/*/programs/*/checkoutSettings}:\x11checkout_settings'
    _globals['_CHECKOUTSETTINGSSERVICE'].methods_by_name['DeleteCheckoutSettings']._loaded_options = None
    _globals['_CHECKOUTSETTINGSSERVICE'].methods_by_name['DeleteCheckoutSettings']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/accounts/v1beta/{name=accounts/*/programs/*/checkoutSettings}'
    _globals['_GETCHECKOUTSETTINGSREQUEST']._serialized_start = 321
    _globals['_GETCHECKOUTSETTINGSREQUEST']._serialized_end = 416
    _globals['_CREATECHECKOUTSETTINGSREQUEST']._serialized_start = 419
    _globals['_CREATECHECKOUTSETTINGSREQUEST']._serialized_end = 611
    _globals['_UPDATECHECKOUTSETTINGSREQUEST']._serialized_start = 614
    _globals['_UPDATECHECKOUTSETTINGSREQUEST']._serialized_end = 791
    _globals['_DELETECHECKOUTSETTINGSREQUEST']._serialized_start = 793
    _globals['_DELETECHECKOUTSETTINGSREQUEST']._serialized_end = 891
    _globals['_CHECKOUTSETTINGS']._serialized_start = 894
    _globals['_CHECKOUTSETTINGS']._serialized_end = 2147
    _globals['_CHECKOUTSETTINGS_CHECKOUTENROLLMENTSTATE']._serialized_start = 1679
    _globals['_CHECKOUTSETTINGS_CHECKOUTENROLLMENTSTATE']._serialized_end = 1790
    _globals['_CHECKOUTSETTINGS_CHECKOUTREVIEWSTATE']._serialized_start = 1792
    _globals['_CHECKOUTSETTINGS_CHECKOUTREVIEWSTATE']._serialized_end = 1898
    _globals['_URISETTINGS']._serialized_start = 2149
    _globals['_URISETTINGS']._serialized_end = 2240
    _globals['_CHECKOUTSETTINGSSERVICE']._serialized_start = 2243
    _globals['_CHECKOUTSETTINGSSERVICE']._serialized_end = 3359