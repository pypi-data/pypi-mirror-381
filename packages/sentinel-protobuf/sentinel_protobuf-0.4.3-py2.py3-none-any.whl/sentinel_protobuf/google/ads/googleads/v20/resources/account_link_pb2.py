"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/account_link.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import account_link_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_account__link__status__pb2
from ......google.ads.googleads.v20.enums import linked_account_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_linked__account__type__pb2
from ......google.ads.googleads.v20.enums import mobile_app_vendor_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_mobile__app__vendor__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/ads/googleads/v20/resources/account_link.proto\x12"google.ads.googleads.v20.resources\x1a8google/ads/googleads/v20/enums/account_link_status.proto\x1a8google/ads/googleads/v20/enums/linked_account_type.proto\x1a6google/ads/googleads/v20/enums/mobile_app_vendor.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa7\x04\n\x0bAccountLink\x12C\n\rresource_name\x18\x01 \x01(\tB,\xe0A\x05\xfaA&\n$googleads.googleapis.com/AccountLink\x12!\n\x0faccount_link_id\x18\x08 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12W\n\x06status\x18\x03 \x01(\x0e2G.google.ads.googleads.v20.enums.AccountLinkStatusEnum.AccountLinkStatus\x12Z\n\x04type\x18\x04 \x01(\x0e2G.google.ads.googleads.v20.enums.LinkedAccountTypeEnum.LinkedAccountTypeB\x03\xe0A\x03\x12r\n\x19third_party_app_analytics\x18\x05 \x01(\x0b2H.google.ads.googleads.v20.resources.ThirdPartyAppAnalyticsLinkIdentifierB\x03\xe0A\x05H\x00:a\xeaA^\n$googleads.googleapis.com/AccountLink\x126customers/{customer_id}/accountLinks/{account_link_id}B\x10\n\x0elinked_accountB\x12\n\x10_account_link_id"\xf4\x01\n$ThirdPartyAppAnalyticsLinkIdentifier\x12+\n\x19app_analytics_provider_id\x18\x04 \x01(\x03B\x03\xe0A\x05H\x00\x88\x01\x01\x12\x18\n\x06app_id\x18\x05 \x01(\tB\x03\xe0A\x05H\x01\x88\x01\x01\x12\\\n\napp_vendor\x18\x03 \x01(\x0e2C.google.ads.googleads.v20.enums.MobileAppVendorEnum.MobileAppVendorB\x03\xe0A\x05B\x1c\n\x1a_app_analytics_provider_idB\t\n\x07_app_idB\x82\x02\n&com.google.ads.googleads.v20.resourcesB\x10AccountLinkProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.account_link_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x10AccountLinkProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ACCOUNTLINK'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ACCOUNTLINK'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA&\n$googleads.googleapis.com/AccountLink'
    _globals['_ACCOUNTLINK'].fields_by_name['account_link_id']._loaded_options = None
    _globals['_ACCOUNTLINK'].fields_by_name['account_link_id']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTLINK'].fields_by_name['type']._loaded_options = None
    _globals['_ACCOUNTLINK'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTLINK'].fields_by_name['third_party_app_analytics']._loaded_options = None
    _globals['_ACCOUNTLINK'].fields_by_name['third_party_app_analytics']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTLINK']._loaded_options = None
    _globals['_ACCOUNTLINK']._serialized_options = b'\xeaA^\n$googleads.googleapis.com/AccountLink\x126customers/{customer_id}/accountLinks/{account_link_id}'
    _globals['_THIRDPARTYAPPANALYTICSLINKIDENTIFIER'].fields_by_name['app_analytics_provider_id']._loaded_options = None
    _globals['_THIRDPARTYAPPANALYTICSLINKIDENTIFIER'].fields_by_name['app_analytics_provider_id']._serialized_options = b'\xe0A\x05'
    _globals['_THIRDPARTYAPPANALYTICSLINKIDENTIFIER'].fields_by_name['app_id']._loaded_options = None
    _globals['_THIRDPARTYAPPANALYTICSLINKIDENTIFIER'].fields_by_name['app_id']._serialized_options = b'\xe0A\x05'
    _globals['_THIRDPARTYAPPANALYTICSLINKIDENTIFIER'].fields_by_name['app_vendor']._loaded_options = None
    _globals['_THIRDPARTYAPPANALYTICSLINKIDENTIFIER'].fields_by_name['app_vendor']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTLINK']._serialized_start = 326
    _globals['_ACCOUNTLINK']._serialized_end = 877
    _globals['_THIRDPARTYAPPANALYTICSLINKIDENTIFIER']._serialized_start = 880
    _globals['_THIRDPARTYAPPANALYTICSLINKIDENTIFIER']._serialized_end = 1124