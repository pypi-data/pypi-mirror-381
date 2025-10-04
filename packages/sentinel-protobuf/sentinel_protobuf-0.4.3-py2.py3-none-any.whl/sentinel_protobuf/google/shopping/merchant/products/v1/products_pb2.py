"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/products/v1/products.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.shopping.merchant.products.v1 import products_common_pb2 as google_dot_shopping_dot_merchant_dot_products_dot_v1_dot_products__common__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/shopping/merchant/products/v1/products.proto\x12$google.shopping.merchant.products.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a:google/shopping/merchant/products/v1/products_common.proto\x1a google/shopping/type/types.proto"\xef\x04\n\x07Product\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0clegacy_local\x18\x0b \x01(\x08B\x03\xe0A\x03\x12\x15\n\x08offer_id\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10content_language\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x17\n\nfeed_label\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdata_source\x18\x06 \x01(\tB\x03\xe0A\x03\x12 \n\x0eversion_number\x18\x07 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12X\n\x12product_attributes\x18\r \x01(\x0b27.google.shopping.merchant.products.v1.ProductAttributesB\x03\xe0A\x03\x12E\n\x11custom_attributes\x18\t \x03(\x0b2%.google.shopping.type.CustomAttributeB\x03\xe0A\x03\x12P\n\x0eproduct_status\x18\n \x01(\x0b23.google.shopping.merchant.products.v1.ProductStatusB\x03\xe0A\x03\x12Z\n\x13automated_discounts\x18\x0c \x01(\x0b28.google.shopping.merchant.products.v1.AutomatedDiscountsB\x03\xe0A\x03:N\xeaAK\n"merchantapi.googleapis.com/Product\x12%accounts/{account}/products/{product}B\x11\n\x0f_version_number"M\n\x11GetProductRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Product"x\n\x13ListProductsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"merchantapi.googleapis.com/Product\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"p\n\x14ListProductsResponse\x12?\n\x08products\x18\x01 \x03(\x0b2-.google.shopping.merchant.products.v1.Product\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xcf\x03\n\x0fProductsService\x12\xae\x01\n\nGetProduct\x127.google.shopping.merchant.products.v1.GetProductRequest\x1a-.google.shopping.merchant.products.v1.Product"8\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/products/v1/{name=accounts/*/products/*}\x12\xc1\x01\n\x0cListProducts\x129.google.shopping.merchant.products.v1.ListProductsRequest\x1a:.google.shopping.merchant.products.v1.ListProductsResponse":\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/products/v1/{parent=accounts/*}/products\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xbb\x02\n(com.google.shopping.merchant.products.v1B\rProductsProtoP\x01ZJcloud.google.com/go/shopping/merchant/products/apiv1/productspb;productspb\xaa\x02$Google.Shopping.Merchant.Products.V1\xca\x02$Google\\Shopping\\Merchant\\Products\\V1\xea\x02(Google::Shopping::Merchant::Products::V1\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.products.v1.products_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.products.v1B\rProductsProtoP\x01ZJcloud.google.com/go/shopping/merchant/products/apiv1/productspb;productspb\xaa\x02$Google.Shopping.Merchant.Products.V1\xca\x02$Google\\Shopping\\Merchant\\Products\\V1\xea\x02(Google::Shopping::Merchant::Products::V1\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}'
    _globals['_PRODUCT'].fields_by_name['legacy_local']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['legacy_local']._serialized_options = b'\xe0A\x03'
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
    _globals['_PRODUCT'].fields_by_name['product_attributes']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['product_attributes']._serialized_options = b'\xe0A\x03'
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
    _globals['_PRODUCTSSERVICE'].methods_by_name['GetProduct']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02+\x12)/products/v1/{name=accounts/*/products/*}'
    _globals['_PRODUCTSSERVICE'].methods_by_name['ListProducts']._loaded_options = None
    _globals['_PRODUCTSSERVICE'].methods_by_name['ListProducts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/products/v1/{parent=accounts/*}/products'
    _globals['_PRODUCT']._serialized_start = 303
    _globals['_PRODUCT']._serialized_end = 926
    _globals['_GETPRODUCTREQUEST']._serialized_start = 928
    _globals['_GETPRODUCTREQUEST']._serialized_end = 1005
    _globals['_LISTPRODUCTSREQUEST']._serialized_start = 1007
    _globals['_LISTPRODUCTSREQUEST']._serialized_end = 1127
    _globals['_LISTPRODUCTSRESPONSE']._serialized_start = 1129
    _globals['_LISTPRODUCTSRESPONSE']._serialized_end = 1241
    _globals['_PRODUCTSSERVICE']._serialized_start = 1244
    _globals['_PRODUCTSSERVICE']._serialized_end = 1707