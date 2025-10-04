"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/products/v1beta/products.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.shopping.merchant.products.v1beta import products_common_pb2 as google_dot_shopping_dot_merchant_dot_products_dot_v1beta_dot_products__common__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/shopping/merchant/products/v1beta/products.proto\x12(google.shopping.merchant.products.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a>google/shopping/merchant/products/v1beta/products_common.proto\x1a google/shopping/type/types.proto"\x92\x05\n\x07Product\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x07channel\x18\x02 \x01(\x0e2).google.shopping.type.Channel.ChannelEnumB\x03\xe0A\x03\x12\x15\n\x08offer_id\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10content_language\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x17\n\nfeed_label\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdata_source\x18\x06 \x01(\tB\x03\xe0A\x03\x12 \n\x0eversion_number\x18\x07 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12M\n\nattributes\x18\x08 \x01(\x0b24.google.shopping.merchant.products.v1beta.AttributesB\x03\xe0A\x03\x12E\n\x11custom_attributes\x18\t \x03(\x0b2%.google.shopping.type.CustomAttributeB\x03\xe0A\x03\x12T\n\x0eproduct_status\x18\n \x01(\x0b27.google.shopping.merchant.products.v1beta.ProductStatusB\x03\xe0A\x03\x12^\n\x13automated_discounts\x18\x0c \x01(\x0b2<.google.shopping.merchant.products.v1beta.AutomatedDiscountsB\x03\xe0A\x03:N\xeaAK\n"merchantapi.googleapis.com/Product\x12%accounts/{account}/products/{product}B\x11\n\x0f_version_number"M\n\x11GetProductRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Product"x\n\x13ListProductsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"merchantapi.googleapis.com/Product\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"t\n\x14ListProductsResponse\x12C\n\x08products\x18\x01 \x03(\x0b21.google.shopping.merchant.products.v1beta.Product\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe7\x03\n\x0fProductsService\x12\xba\x01\n\nGetProduct\x12;.google.shopping.merchant.products.v1beta.GetProductRequest\x1a1.google.shopping.merchant.products.v1beta.Product"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/products/v1beta/{name=accounts/*/products/*}\x12\xcd\x01\n\x0cListProducts\x12=.google.shopping.merchant.products.v1beta.ListProductsRequest\x1a>.google.shopping.merchant.products.v1beta.ListProductsResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/products/v1beta/{parent=accounts/*}/products\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xca\x01\n,com.google.shopping.merchant.products.v1betaB\rProductsProtoP\x01ZNcloud.google.com/go/shopping/merchant/products/apiv1beta/productspb;productspb\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.products.v1beta.products_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.products.v1betaB\rProductsProtoP\x01ZNcloud.google.com/go/shopping/merchant/products/apiv1beta/productspb;productspb\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}'
    _globals['_PRODUCT'].fields_by_name['channel']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['channel']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['offer_id']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['offer_id']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['content_language']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['content_language']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['feed_label']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['data_source']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['data_source']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['version_number']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['version_number']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['attributes']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['attributes']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['custom_attributes']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['custom_attributes']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['product_status']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['product_status']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['automated_discounts']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['automated_discounts']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT']._loaded_options = None
    _globals['_PRODUCT']._serialized_options = b'\xeaAK\n"merchantapi.googleapis.com/Product\x12%accounts/{account}/products/{product}'
    _globals['_GETPRODUCTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPRODUCTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Product'
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"merchantapi.googleapis.com/Product'
    _globals['_PRODUCTSSERVICE']._loaded_options = None
    _globals['_PRODUCTSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_PRODUCTSSERVICE'].methods_by_name['GetProduct']._loaded_options = None
    _globals['_PRODUCTSSERVICE'].methods_by_name['GetProduct']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/products/v1beta/{name=accounts/*/products/*}'
    _globals['_PRODUCTSSERVICE'].methods_by_name['ListProducts']._loaded_options = None
    _globals['_PRODUCTSSERVICE'].methods_by_name['ListProducts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/products/v1beta/{parent=accounts/*}/products'
    _globals['_PRODUCT']._serialized_start = 315
    _globals['_PRODUCT']._serialized_end = 973
    _globals['_GETPRODUCTREQUEST']._serialized_start = 975
    _globals['_GETPRODUCTREQUEST']._serialized_end = 1052
    _globals['_LISTPRODUCTSREQUEST']._serialized_start = 1054
    _globals['_LISTPRODUCTSREQUEST']._serialized_end = 1174
    _globals['_LISTPRODUCTSRESPONSE']._serialized_start = 1176
    _globals['_LISTPRODUCTSRESPONSE']._serialized_end = 1292
    _globals['_PRODUCTSSERVICE']._serialized_start = 1295
    _globals['_PRODUCTSSERVICE']._serialized_end = 1782