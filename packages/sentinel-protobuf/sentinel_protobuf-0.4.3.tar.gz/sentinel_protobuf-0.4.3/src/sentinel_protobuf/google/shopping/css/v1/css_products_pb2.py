"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/css/v1/css_products.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.shopping.css.v1 import css_product_common_pb2 as google_dot_shopping_dot_css_dot_v1_dot_css__product__common__pb2
from .....google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/shopping/css/v1/css_products.proto\x12\x16google.shopping.css.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/shopping/css/v1/css_product_common.proto\x1a google/shopping/type/types.proto"K\n\x14GetCssProductRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dcss.googleapis.com/CssProduct"\xaa\x03\n\nCssProduct\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1c\n\x0fraw_provided_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10content_language\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x17\n\nfeed_label\x18\x04 \x01(\tB\x03\xe0A\x03\x12;\n\nattributes\x18\x05 \x01(\x0b2".google.shopping.css.v1.AttributesB\x03\xe0A\x03\x12E\n\x11custom_attributes\x18\x06 \x03(\x0b2%.google.shopping.type.CustomAttributeB\x03\xe0A\x03\x12I\n\x12css_product_status\x18\x08 \x01(\x0b2(.google.shopping.css.v1.CssProductStatusB\x03\xe0A\x03:i\xeaAf\n\x1dcss.googleapis.com/CssProduct\x12,accounts/{account}/cssProducts/{css_product}*\x0bcssProducts2\ncssProduct"v\n\x16ListCssProductsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\x12\x1dcss.googleapis.com/CssProduct\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"l\n\x17ListCssProductsResponse\x128\n\x0ccss_products\x18\x01 \x03(\x0b2".google.shopping.css.v1.CssProduct\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x98\x03\n\x12CssProductsService\x12\x95\x01\n\rGetCssProduct\x12,.google.shopping.css.v1.GetCssProductRequest\x1a".google.shopping.css.v1.CssProduct"2\xdaA\x04name\x82\xd3\xe4\x93\x02%\x12#/v1/{name=accounts/*/cssProducts/*}\x12\xa8\x01\n\x0fListCssProducts\x12..google.shopping.css.v1.ListCssProductsRequest\x1a/.google.shopping.css.v1.ListCssProductsResponse"4\xdaA\x06parent\x82\xd3\xe4\x93\x02%\x12#/v1/{parent=accounts/*}/cssProducts\x1a?\xcaA\x12css.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xb2\x01\n\x1acom.google.shopping.css.v1B\x10CssProductsProtoP\x01Z2cloud.google.com/go/shopping/css/apiv1/csspb;csspb\xaa\x02\x16Google.Shopping.Css.V1\xca\x02\x16Google\\Shopping\\Css\\V1\xea\x02\x19Google::Shopping::Css::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.css.v1.css_products_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.shopping.css.v1B\x10CssProductsProtoP\x01Z2cloud.google.com/go/shopping/css/apiv1/csspb;csspb\xaa\x02\x16Google.Shopping.Css.V1\xca\x02\x16Google\\Shopping\\Css\\V1\xea\x02\x19Google::Shopping::Css::V1'
    _globals['_GETCSSPRODUCTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCSSPRODUCTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dcss.googleapis.com/CssProduct'
    _globals['_CSSPRODUCT'].fields_by_name['raw_provided_id']._loaded_options = None
    _globals['_CSSPRODUCT'].fields_by_name['raw_provided_id']._serialized_options = b'\xe0A\x03'
    _globals['_CSSPRODUCT'].fields_by_name['content_language']._loaded_options = None
    _globals['_CSSPRODUCT'].fields_by_name['content_language']._serialized_options = b'\xe0A\x03'
    _globals['_CSSPRODUCT'].fields_by_name['feed_label']._loaded_options = None
    _globals['_CSSPRODUCT'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x03'
    _globals['_CSSPRODUCT'].fields_by_name['attributes']._loaded_options = None
    _globals['_CSSPRODUCT'].fields_by_name['attributes']._serialized_options = b'\xe0A\x03'
    _globals['_CSSPRODUCT'].fields_by_name['custom_attributes']._loaded_options = None
    _globals['_CSSPRODUCT'].fields_by_name['custom_attributes']._serialized_options = b'\xe0A\x03'
    _globals['_CSSPRODUCT'].fields_by_name['css_product_status']._loaded_options = None
    _globals['_CSSPRODUCT'].fields_by_name['css_product_status']._serialized_options = b'\xe0A\x03'
    _globals['_CSSPRODUCT']._loaded_options = None
    _globals['_CSSPRODUCT']._serialized_options = b'\xeaAf\n\x1dcss.googleapis.com/CssProduct\x12,accounts/{account}/cssProducts/{css_product}*\x0bcssProducts2\ncssProduct'
    _globals['_LISTCSSPRODUCTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCSSPRODUCTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\x12\x1dcss.googleapis.com/CssProduct'
    _globals['_CSSPRODUCTSSERVICE']._loaded_options = None
    _globals['_CSSPRODUCTSSERVICE']._serialized_options = b"\xcaA\x12css.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_CSSPRODUCTSSERVICE'].methods_by_name['GetCssProduct']._loaded_options = None
    _globals['_CSSPRODUCTSSERVICE'].methods_by_name['GetCssProduct']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02%\x12#/v1/{name=accounts/*/cssProducts/*}'
    _globals['_CSSPRODUCTSSERVICE'].methods_by_name['ListCssProducts']._loaded_options = None
    _globals['_CSSPRODUCTSSERVICE'].methods_by_name['ListCssProducts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02%\x12#/v1/{parent=accounts/*}/cssProducts'
    _globals['_GETCSSPRODUCTREQUEST']._serialized_start = 267
    _globals['_GETCSSPRODUCTREQUEST']._serialized_end = 342
    _globals['_CSSPRODUCT']._serialized_start = 345
    _globals['_CSSPRODUCT']._serialized_end = 771
    _globals['_LISTCSSPRODUCTSREQUEST']._serialized_start = 773
    _globals['_LISTCSSPRODUCTSREQUEST']._serialized_end = 891
    _globals['_LISTCSSPRODUCTSRESPONSE']._serialized_start = 893
    _globals['_LISTCSSPRODUCTSRESPONSE']._serialized_end = 1001
    _globals['_CSSPRODUCTSSERVICE']._serialized_start = 1004
    _globals['_CSSPRODUCTSSERVICE']._serialized_end = 1412