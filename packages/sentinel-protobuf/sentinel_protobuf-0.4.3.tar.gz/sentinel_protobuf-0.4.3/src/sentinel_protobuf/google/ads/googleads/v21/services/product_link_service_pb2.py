"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/product_link_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.resources import product_link_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_product__link__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/googleads/v21/services/product_link_service.proto\x12!google.ads.googleads.v21.services\x1a5google/ads/googleads/v21/resources/product_link.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x80\x01\n\x18CreateProductLinkRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12J\n\x0cproduct_link\x18\x02 \x01(\x0b2/.google.ads.googleads.v21.resources.ProductLinkB\x03\xe0A\x02"]\n\x19CreateProductLinkResponse\x12@\n\rresource_name\x18\x01 \x01(\tB)\xfaA&\n$googleads.googleapis.com/ProductLink"\x90\x01\n\x18RemoveProductLinkRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12C\n\rresource_name\x18\x02 \x01(\tB,\xe0A\x02\xfaA&\n$googleads.googleapis.com/ProductLink\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"]\n\x19RemoveProductLinkResponse\x12@\n\rresource_name\x18\x01 \x01(\tB)\xfaA&\n$googleads.googleapis.com/ProductLink2\xb2\x04\n\x12ProductLinkService\x12\xe8\x01\n\x11CreateProductLink\x12;.google.ads.googleads.v21.services.CreateProductLinkRequest\x1a<.google.ads.googleads.v21.services.CreateProductLinkResponse"X\xdaA\x18customer_id,product_link\x82\xd3\xe4\x93\x027"2/v21/customers/{customer_id=*}/productLinks:create:\x01*\x12\xe9\x01\n\x11RemoveProductLink\x12;.google.ads.googleads.v21.services.RemoveProductLinkRequest\x1a<.google.ads.googleads.v21.services.RemoveProductLinkResponse"Y\xdaA\x19customer_id,resource_name\x82\xd3\xe4\x93\x027"2/v21/customers/{customer_id=*}/productLinks:remove:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x83\x02\n%com.google.ads.googleads.v21.servicesB\x17ProductLinkServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.product_link_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x17ProductLinkServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_CREATEPRODUCTLINKREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_CREATEPRODUCTLINKREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPRODUCTLINKREQUEST'].fields_by_name['product_link']._loaded_options = None
    _globals['_CREATEPRODUCTLINKREQUEST'].fields_by_name['product_link']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPRODUCTLINKRESPONSE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CREATEPRODUCTLINKRESPONSE'].fields_by_name['resource_name']._serialized_options = b'\xfaA&\n$googleads.googleapis.com/ProductLink'
    _globals['_REMOVEPRODUCTLINKREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_REMOVEPRODUCTLINKREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEPRODUCTLINKREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_REMOVEPRODUCTLINKREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA&\n$googleads.googleapis.com/ProductLink'
    _globals['_REMOVEPRODUCTLINKRESPONSE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_REMOVEPRODUCTLINKRESPONSE'].fields_by_name['resource_name']._serialized_options = b'\xfaA&\n$googleads.googleapis.com/ProductLink'
    _globals['_PRODUCTLINKSERVICE']._loaded_options = None
    _globals['_PRODUCTLINKSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_PRODUCTLINKSERVICE'].methods_by_name['CreateProductLink']._loaded_options = None
    _globals['_PRODUCTLINKSERVICE'].methods_by_name['CreateProductLink']._serialized_options = b'\xdaA\x18customer_id,product_link\x82\xd3\xe4\x93\x027"2/v21/customers/{customer_id=*}/productLinks:create:\x01*'
    _globals['_PRODUCTLINKSERVICE'].methods_by_name['RemoveProductLink']._loaded_options = None
    _globals['_PRODUCTLINKSERVICE'].methods_by_name['RemoveProductLink']._serialized_options = b'\xdaA\x19customer_id,resource_name\x82\xd3\xe4\x93\x027"2/v21/customers/{customer_id=*}/productLinks:remove:\x01*'
    _globals['_CREATEPRODUCTLINKREQUEST']._serialized_start = 270
    _globals['_CREATEPRODUCTLINKREQUEST']._serialized_end = 398
    _globals['_CREATEPRODUCTLINKRESPONSE']._serialized_start = 400
    _globals['_CREATEPRODUCTLINKRESPONSE']._serialized_end = 493
    _globals['_REMOVEPRODUCTLINKREQUEST']._serialized_start = 496
    _globals['_REMOVEPRODUCTLINKREQUEST']._serialized_end = 640
    _globals['_REMOVEPRODUCTLINKRESPONSE']._serialized_start = 642
    _globals['_REMOVEPRODUCTLINKRESPONSE']._serialized_end = 735
    _globals['_PRODUCTLINKSERVICE']._serialized_start = 738
    _globals['_PRODUCTLINKSERVICE']._serialized_end = 1300