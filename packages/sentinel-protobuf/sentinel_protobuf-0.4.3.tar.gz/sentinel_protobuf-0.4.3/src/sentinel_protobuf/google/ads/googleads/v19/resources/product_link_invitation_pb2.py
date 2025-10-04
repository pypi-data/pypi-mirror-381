"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/product_link_invitation.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import linked_product_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_linked__product__type__pb2
from ......google.ads.googleads.v19.enums import product_link_invitation_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_product__link__invitation__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v19/resources/product_link_invitation.proto\x12"google.ads.googleads.v19.resources\x1a8google/ads/googleads/v19/enums/linked_product_type.proto\x1aCgoogle/ads/googleads/v19/enums/product_link_invitation_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb4\x06\n\x15ProductLinkInvitation\x12M\n\rresource_name\x18\x01 \x01(\tB6\xe0A\x05\xfaA0\n.googleads.googleapis.com/ProductLinkInvitation\x12\'\n\x1aproduct_link_invitation_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12p\n\x06status\x18\x03 \x01(\x0e2[.google.ads.googleads.v19.enums.ProductLinkInvitationStatusEnum.ProductLinkInvitationStatusB\x03\xe0A\x03\x12Z\n\x04type\x18\x06 \x01(\x0e2G.google.ads.googleads.v19.enums.LinkedProductTypeEnum.LinkedProductTypeB\x03\xe0A\x03\x12d\n\x0chotel_center\x18\x04 \x01(\x0b2G.google.ads.googleads.v19.resources.HotelCenterLinkInvitationIdentifierB\x03\xe0A\x03H\x00\x12j\n\x0fmerchant_center\x18\x05 \x01(\x0b2J.google.ads.googleads.v19.resources.MerchantCenterLinkInvitationIdentifierB\x03\xe0A\x03H\x00\x12r\n\x13advertising_partner\x18\x07 \x01(\x0b2N.google.ads.googleads.v19.resources.AdvertisingPartnerLinkInvitationIdentifierB\x03\xe0A\x03H\x00:|\xeaAy\n.googleads.googleapis.com/ProductLinkInvitation\x12Gcustomers/{customer_id}/productLinkInvitations/{customer_invitation_id}B\x11\n\x0finvited_account"C\n#HotelCenterLinkInvitationIdentifier\x12\x1c\n\x0fhotel_center_id\x18\x01 \x01(\x03B\x03\xe0A\x03"I\n&MerchantCenterLinkInvitationIdentifier\x12\x1f\n\x12merchant_center_id\x18\x01 \x01(\x03B\x03\xe0A\x03"{\n*AdvertisingPartnerLinkInvitationIdentifier\x12@\n\x08customer\x18\x01 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/CustomerH\x00\x88\x01\x01B\x0b\n\t_customerB\x8c\x02\n&com.google.ads.googleads.v19.resourcesB\x1aProductLinkInvitationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.product_link_invitation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x1aProductLinkInvitationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA0\n.googleads.googleapis.com/ProductLinkInvitation'
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['product_link_invitation_id']._loaded_options = None
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['product_link_invitation_id']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['status']._loaded_options = None
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['type']._loaded_options = None
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['hotel_center']._loaded_options = None
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['hotel_center']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['merchant_center']._loaded_options = None
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['merchant_center']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['advertising_partner']._loaded_options = None
    _globals['_PRODUCTLINKINVITATION'].fields_by_name['advertising_partner']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTLINKINVITATION']._loaded_options = None
    _globals['_PRODUCTLINKINVITATION']._serialized_options = b'\xeaAy\n.googleads.googleapis.com/ProductLinkInvitation\x12Gcustomers/{customer_id}/productLinkInvitations/{customer_invitation_id}'
    _globals['_HOTELCENTERLINKINVITATIONIDENTIFIER'].fields_by_name['hotel_center_id']._loaded_options = None
    _globals['_HOTELCENTERLINKINVITATIONIDENTIFIER'].fields_by_name['hotel_center_id']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTCENTERLINKINVITATIONIDENTIFIER'].fields_by_name['merchant_center_id']._loaded_options = None
    _globals['_MERCHANTCENTERLINKINVITATIONIDENTIFIER'].fields_by_name['merchant_center_id']._serialized_options = b'\xe0A\x03'
    _globals['_ADVERTISINGPARTNERLINKINVITATIONIDENTIFIER'].fields_by_name['customer']._loaded_options = None
    _globals['_ADVERTISINGPARTNERLINKINVITATIONIDENTIFIER'].fields_by_name['customer']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_PRODUCTLINKINVITATION']._serialized_start = 292
    _globals['_PRODUCTLINKINVITATION']._serialized_end = 1112
    _globals['_HOTELCENTERLINKINVITATIONIDENTIFIER']._serialized_start = 1114
    _globals['_HOTELCENTERLINKINVITATIONIDENTIFIER']._serialized_end = 1181
    _globals['_MERCHANTCENTERLINKINVITATIONIDENTIFIER']._serialized_start = 1183
    _globals['_MERCHANTCENTERLINKINVITATIONIDENTIFIER']._serialized_end = 1256
    _globals['_ADVERTISINGPARTNERLINKINVITATIONIDENTIFIER']._serialized_start = 1258
    _globals['_ADVERTISINGPARTNERLINKINVITATIONIDENTIFIER']._serialized_end = 1381