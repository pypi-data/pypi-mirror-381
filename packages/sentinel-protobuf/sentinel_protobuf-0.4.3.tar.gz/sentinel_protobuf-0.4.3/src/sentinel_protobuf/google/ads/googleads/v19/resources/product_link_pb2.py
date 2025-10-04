"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/product_link.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import linked_product_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_linked__product__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/ads/googleads/v19/resources/product_link.proto\x12"google.ads.googleads.v19.resources\x1a8google/ads/googleads/v19/enums/linked_product_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xca\x05\n\x0bProductLink\x12C\n\rresource_name\x18\x01 \x01(\tB,\xe0A\x05\xfaA&\n$googleads.googleapis.com/ProductLink\x12!\n\x0fproduct_link_id\x18\x02 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12Z\n\x04type\x18\x03 \x01(\x0e2G.google.ads.googleads.v19.enums.LinkedProductTypeEnum.LinkedProductTypeB\x03\xe0A\x03\x12V\n\x0cdata_partner\x18\x04 \x01(\x0b29.google.ads.googleads.v19.resources.DataPartnerIdentifierB\x03\xe0A\x05H\x00\x12R\n\ngoogle_ads\x18\x05 \x01(\x0b27.google.ads.googleads.v19.resources.GoogleAdsIdentifierB\x03\xe0A\x05H\x00\x12\\\n\x0fmerchant_center\x18\x0c \x01(\x0b2<.google.ads.googleads.v19.resources.MerchantCenterIdentifierB\x03\xe0A\x05H\x00\x12d\n\x13advertising_partner\x18\r \x01(\x0b2@.google.ads.googleads.v19.resources.AdvertisingPartnerIdentifierB\x03\xe0A\x03H\x00:a\xeaA^\n$googleads.googleapis.com/ProductLink\x126customers/{customer_id}/productLinks/{product_link_id}B\x10\n\x0elinked_productB\x12\n\x10_product_link_id"N\n\x15DataPartnerIdentifier\x12!\n\x0fdata_partner_id\x18\x01 \x01(\x03B\x03\xe0A\x05H\x00\x88\x01\x01B\x12\n\x10_data_partner_id"d\n\x13GoogleAdsIdentifier\x12@\n\x08customer\x18\x01 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/CustomerH\x00\x88\x01\x01B\x0b\n\t_customer"W\n\x18MerchantCenterIdentifier\x12$\n\x12merchant_center_id\x18\x01 \x01(\x03B\x03\xe0A\x05H\x00\x88\x01\x01B\x15\n\x13_merchant_center_id"m\n\x1cAdvertisingPartnerIdentifier\x12@\n\x08customer\x18\x01 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/CustomerH\x00\x88\x01\x01B\x0b\n\t_customerB\x82\x02\n&com.google.ads.googleads.v19.resourcesB\x10ProductLinkProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.product_link_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x10ProductLinkProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_PRODUCTLINK'].fields_by_name['resource_name']._loaded_options = None
    _globals['_PRODUCTLINK'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA&\n$googleads.googleapis.com/ProductLink'
    _globals['_PRODUCTLINK'].fields_by_name['product_link_id']._loaded_options = None
    _globals['_PRODUCTLINK'].fields_by_name['product_link_id']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTLINK'].fields_by_name['type']._loaded_options = None
    _globals['_PRODUCTLINK'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTLINK'].fields_by_name['data_partner']._loaded_options = None
    _globals['_PRODUCTLINK'].fields_by_name['data_partner']._serialized_options = b'\xe0A\x05'
    _globals['_PRODUCTLINK'].fields_by_name['google_ads']._loaded_options = None
    _globals['_PRODUCTLINK'].fields_by_name['google_ads']._serialized_options = b'\xe0A\x05'
    _globals['_PRODUCTLINK'].fields_by_name['merchant_center']._loaded_options = None
    _globals['_PRODUCTLINK'].fields_by_name['merchant_center']._serialized_options = b'\xe0A\x05'
    _globals['_PRODUCTLINK'].fields_by_name['advertising_partner']._loaded_options = None
    _globals['_PRODUCTLINK'].fields_by_name['advertising_partner']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTLINK']._loaded_options = None
    _globals['_PRODUCTLINK']._serialized_options = b'\xeaA^\n$googleads.googleapis.com/ProductLink\x126customers/{customer_id}/productLinks/{product_link_id}'
    _globals['_DATAPARTNERIDENTIFIER'].fields_by_name['data_partner_id']._loaded_options = None
    _globals['_DATAPARTNERIDENTIFIER'].fields_by_name['data_partner_id']._serialized_options = b'\xe0A\x05'
    _globals['_GOOGLEADSIDENTIFIER'].fields_by_name['customer']._loaded_options = None
    _globals['_GOOGLEADSIDENTIFIER'].fields_by_name['customer']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_MERCHANTCENTERIDENTIFIER'].fields_by_name['merchant_center_id']._loaded_options = None
    _globals['_MERCHANTCENTERIDENTIFIER'].fields_by_name['merchant_center_id']._serialized_options = b'\xe0A\x05'
    _globals['_ADVERTISINGPARTNERIDENTIFIER'].fields_by_name['customer']._loaded_options = None
    _globals['_ADVERTISINGPARTNERIDENTIFIER'].fields_by_name['customer']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_PRODUCTLINK']._serialized_start = 212
    _globals['_PRODUCTLINK']._serialized_end = 926
    _globals['_DATAPARTNERIDENTIFIER']._serialized_start = 928
    _globals['_DATAPARTNERIDENTIFIER']._serialized_end = 1006
    _globals['_GOOGLEADSIDENTIFIER']._serialized_start = 1008
    _globals['_GOOGLEADSIDENTIFIER']._serialized_end = 1108
    _globals['_MERCHANTCENTERIDENTIFIER']._serialized_start = 1110
    _globals['_MERCHANTCENTERIDENTIFIER']._serialized_end = 1197
    _globals['_ADVERTISINGPARTNERIDENTIFIER']._serialized_start = 1199
    _globals['_ADVERTISINGPARTNERIDENTIFIER']._serialized_end = 1308