"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/product_link_invitation_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import product_link_invitation_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_product__link__invitation__status__pb2
from ......google.ads.googleads.v19.resources import product_link_invitation_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_product__link__invitation__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/ads/googleads/v19/services/product_link_invitation_service.proto\x12!google.ads.googleads.v19.services\x1aCgoogle/ads/googleads/v19/enums/product_link_invitation_status.proto\x1a@google/ads/googleads/v19/resources/product_link_invitation.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x9f\x01\n"CreateProductLinkInvitationRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12_\n\x17product_link_invitation\x18\x02 \x01(\x0b29.google.ads.googleads.v19.resources.ProductLinkInvitationB\x03\xe0A\x02"q\n#CreateProductLinkInvitationResponse\x12J\n\rresource_name\x18\x01 \x01(\tB3\xfaA0\n.googleads.googleapis.com/ProductLinkInvitation"\x98\x02\n"UpdateProductLinkInvitationRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x88\x01\n\x1eproduct_link_invitation_status\x18\x02 \x01(\x0e2[.google.ads.googleads.v19.enums.ProductLinkInvitationStatusEnum.ProductLinkInvitationStatusB\x03\xe0A\x02\x12M\n\rresource_name\x18\x03 \x01(\tB6\xe0A\x02\xfaA0\n.googleads.googleapis.com/ProductLinkInvitation"q\n#UpdateProductLinkInvitationResponse\x12J\n\rresource_name\x18\x01 \x01(\tB3\xfaA0\n.googleads.googleapis.com/ProductLinkInvitation"\x8d\x01\n"RemoveProductLinkInvitationRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12M\n\rresource_name\x18\x02 \x01(\tB6\xe0A\x02\xfaA0\n.googleads.googleapis.com/ProductLinkInvitation"q\n#RemoveProductLinkInvitationResponse\x12J\n\rresource_name\x18\x01 \x01(\tB3\xfaA0\n.googleads.googleapis.com/ProductLinkInvitation2\xcb\x07\n\x1cProductLinkInvitationService\x12\x9b\x02\n\x1bCreateProductLinkInvitation\x12E.google.ads.googleads.v19.services.CreateProductLinkInvitationRequest\x1aF.google.ads.googleads.v19.services.CreateProductLinkInvitationResponse"m\xdaA#customer_id,product_link_invitation\x82\xd3\xe4\x93\x02A"</v19/customers/{customer_id=*}/productLinkInvitations:create:\x01*\x12\xb1\x02\n\x1bUpdateProductLinkInvitation\x12E.google.ads.googleads.v19.services.UpdateProductLinkInvitationRequest\x1aF.google.ads.googleads.v19.services.UpdateProductLinkInvitationResponse"\x82\x01\xdaA8customer_id,product_link_invitation_status,resource_name\x82\xd3\xe4\x93\x02A"</v19/customers/{customer_id=*}/productLinkInvitations:update:\x01*\x12\x91\x02\n\x1bRemoveProductLinkInvitation\x12E.google.ads.googleads.v19.services.RemoveProductLinkInvitationRequest\x1aF.google.ads.googleads.v19.services.RemoveProductLinkInvitationResponse"c\xdaA\x19customer_id,resource_name\x82\xd3\xe4\x93\x02A"</v19/customers/{customer_id=*}/productLinkInvitations:remove:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8d\x02\n%com.google.ads.googleads.v19.servicesB!ProductLinkInvitationServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.product_link_invitation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB!ProductLinkInvitationServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_CREATEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_CREATEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['product_link_invitation']._loaded_options = None
    _globals['_CREATEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['product_link_invitation']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPRODUCTLINKINVITATIONRESPONSE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CREATEPRODUCTLINKINVITATIONRESPONSE'].fields_by_name['resource_name']._serialized_options = b'\xfaA0\n.googleads.googleapis.com/ProductLinkInvitation'
    _globals['_UPDATEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_UPDATEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['product_link_invitation_status']._loaded_options = None
    _globals['_UPDATEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['product_link_invitation_status']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_UPDATEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA0\n.googleads.googleapis.com/ProductLinkInvitation'
    _globals['_UPDATEPRODUCTLINKINVITATIONRESPONSE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_UPDATEPRODUCTLINKINVITATIONRESPONSE'].fields_by_name['resource_name']._serialized_options = b'\xfaA0\n.googleads.googleapis.com/ProductLinkInvitation'
    _globals['_REMOVEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_REMOVEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_REMOVEPRODUCTLINKINVITATIONREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA0\n.googleads.googleapis.com/ProductLinkInvitation'
    _globals['_REMOVEPRODUCTLINKINVITATIONRESPONSE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_REMOVEPRODUCTLINKINVITATIONRESPONSE'].fields_by_name['resource_name']._serialized_options = b'\xfaA0\n.googleads.googleapis.com/ProductLinkInvitation'
    _globals['_PRODUCTLINKINVITATIONSERVICE']._loaded_options = None
    _globals['_PRODUCTLINKINVITATIONSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_PRODUCTLINKINVITATIONSERVICE'].methods_by_name['CreateProductLinkInvitation']._loaded_options = None
    _globals['_PRODUCTLINKINVITATIONSERVICE'].methods_by_name['CreateProductLinkInvitation']._serialized_options = b'\xdaA#customer_id,product_link_invitation\x82\xd3\xe4\x93\x02A"</v19/customers/{customer_id=*}/productLinkInvitations:create:\x01*'
    _globals['_PRODUCTLINKINVITATIONSERVICE'].methods_by_name['UpdateProductLinkInvitation']._loaded_options = None
    _globals['_PRODUCTLINKINVITATIONSERVICE'].methods_by_name['UpdateProductLinkInvitation']._serialized_options = b'\xdaA8customer_id,product_link_invitation_status,resource_name\x82\xd3\xe4\x93\x02A"</v19/customers/{customer_id=*}/productLinkInvitations:update:\x01*'
    _globals['_PRODUCTLINKINVITATIONSERVICE'].methods_by_name['RemoveProductLinkInvitation']._loaded_options = None
    _globals['_PRODUCTLINKINVITATIONSERVICE'].methods_by_name['RemoveProductLinkInvitation']._serialized_options = b'\xdaA\x19customer_id,resource_name\x82\xd3\xe4\x93\x02A"</v19/customers/{customer_id=*}/productLinkInvitations:remove:\x01*'
    _globals['_CREATEPRODUCTLINKINVITATIONREQUEST']._serialized_start = 361
    _globals['_CREATEPRODUCTLINKINVITATIONREQUEST']._serialized_end = 520
    _globals['_CREATEPRODUCTLINKINVITATIONRESPONSE']._serialized_start = 522
    _globals['_CREATEPRODUCTLINKINVITATIONRESPONSE']._serialized_end = 635
    _globals['_UPDATEPRODUCTLINKINVITATIONREQUEST']._serialized_start = 638
    _globals['_UPDATEPRODUCTLINKINVITATIONREQUEST']._serialized_end = 918
    _globals['_UPDATEPRODUCTLINKINVITATIONRESPONSE']._serialized_start = 920
    _globals['_UPDATEPRODUCTLINKINVITATIONRESPONSE']._serialized_end = 1033
    _globals['_REMOVEPRODUCTLINKINVITATIONREQUEST']._serialized_start = 1036
    _globals['_REMOVEPRODUCTLINKINVITATIONREQUEST']._serialized_end = 1177
    _globals['_REMOVEPRODUCTLINKINVITATIONRESPONSE']._serialized_start = 1179
    _globals['_REMOVEPRODUCTLINKINVITATIONRESPONSE']._serialized_end = 1292
    _globals['_PRODUCTLINKINVITATIONSERVICE']._serialized_start = 1295
    _globals['_PRODUCTLINKINVITATIONSERVICE']._serialized_end = 2266