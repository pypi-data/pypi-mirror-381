"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/products/v1/productinputs.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.shopping.merchant.products.v1 import products_common_pb2 as google_dot_shopping_dot_merchant_dot_products_dot_v1_dot_products__common__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/shopping/merchant/products/v1/productinputs.proto\x12$google.shopping.merchant.products.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a:google/shopping/merchant/products/v1/products_common.proto\x1a google/shopping/type/types.proto"\xff\x03\n\x0cProductInput\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x07product\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0clegacy_local\x18\n \x01(\x08B\x03\xe0A\x05\x12\x18\n\x08offer_id\x18\x04 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12 \n\x10content_language\x18\x05 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12\x1a\n\nfeed_label\x18\x06 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12#\n\x0eversion_number\x18\x07 \x01(\x03B\x06\xe0A\x01\xe0A\x05H\x00\x88\x01\x01\x12X\n\x12product_attributes\x18\x0b \x01(\x0b27.google.shopping.merchant.products.v1.ProductAttributesB\x03\xe0A\x01\x12E\n\x11custom_attributes\x18\t \x03(\x0b2%.google.shopping.type.CustomAttributeB\x03\xe0A\x01:z\xeaAw\n\'merchantapi.googleapis.com/ProductInput\x12/accounts/{account}/productInputs/{productinput}*\rproductInputs2\x0cproductInputB\x11\n\x0f_version_number"\xc1\x01\n\x19InsertProductInputRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"merchantapi.googleapis.com/Product\x12N\n\rproduct_input\x18\x02 \x01(\x0b22.google.shopping.merchant.products.v1.ProductInputB\x03\xe0A\x02\x12\x18\n\x0bdata_source\x18\x03 \x01(\tB\x03\xe0A\x02"\xbb\x01\n\x19UpdateProductInputRequest\x12N\n\rproduct_input\x18\x01 \x01(\x0b22.google.shopping.merchant.products.v1.ProductInputB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12\x18\n\x0bdata_source\x18\x03 \x01(\tB\x03\xe0A\x02"t\n\x19DeleteProductInputRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'merchantapi.googleapis.com/ProductInput\x12\x18\n\x0bdata_source\x18\x02 \x01(\tB\x03\xe0A\x022\xe5\x05\n\x14ProductInputsService\x12\xd7\x01\n\x12InsertProductInput\x12?.google.shopping.merchant.products.v1.InsertProductInputRequest\x1a2.google.shopping.merchant.products.v1.ProductInput"L\x82\xd3\xe4\x93\x02F"5/products/v1/{parent=accounts/*}/productInputs:insert:\rproduct_input\x12\xfa\x01\n\x12UpdateProductInput\x12?.google.shopping.merchant.products.v1.UpdateProductInputRequest\x1a2.google.shopping.merchant.products.v1.ProductInput"o\xdaA\x19product_input,update_mask\x82\xd3\xe4\x93\x02M2</products/v1/{product_input.name=accounts/*/productInputs/*}:\rproduct_input\x12\xac\x01\n\x12DeleteProductInput\x12?.google.shopping.merchant.products.v1.DeleteProductInputRequest\x1a\x16.google.protobuf.Empty"=\xdaA\x04name\x82\xd3\xe4\x93\x020*./products/v1/{name=accounts/*/productInputs/*}\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x85\x02\n(com.google.shopping.merchant.products.v1B\x12ProductInputsProtoP\x01ZJcloud.google.com/go/shopping/merchant/products/apiv1/productspb;productspb\xaa\x02$Google.Shopping.Merchant.Products.V1\xca\x02$Google\\Shopping\\Merchant\\Products\\V1\xea\x02(Google::Shopping::Merchant::Products::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.products.v1.productinputs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.products.v1B\x12ProductInputsProtoP\x01ZJcloud.google.com/go/shopping/merchant/products/apiv1/productspb;productspb\xaa\x02$Google.Shopping.Merchant.Products.V1\xca\x02$Google\\Shopping\\Merchant\\Products\\V1\xea\x02(Google::Shopping::Merchant::Products::V1'
    _globals['_PRODUCTINPUT'].fields_by_name['name']._loaded_options = None
    _globals['_PRODUCTINPUT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PRODUCTINPUT'].fields_by_name['product']._loaded_options = None
    _globals['_PRODUCTINPUT'].fields_by_name['product']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTINPUT'].fields_by_name['legacy_local']._loaded_options = None
    _globals['_PRODUCTINPUT'].fields_by_name['legacy_local']._serialized_options = b'\xe0A\x05'
    _globals['_PRODUCTINPUT'].fields_by_name['offer_id']._loaded_options = None
    _globals['_PRODUCTINPUT'].fields_by_name['offer_id']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_PRODUCTINPUT'].fields_by_name['content_language']._loaded_options = None
    _globals['_PRODUCTINPUT'].fields_by_name['content_language']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_PRODUCTINPUT'].fields_by_name['feed_label']._loaded_options = None
    _globals['_PRODUCTINPUT'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_PRODUCTINPUT'].fields_by_name['version_number']._loaded_options = None
    _globals['_PRODUCTINPUT'].fields_by_name['version_number']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_PRODUCTINPUT'].fields_by_name['product_attributes']._loaded_options = None
    _globals['_PRODUCTINPUT'].fields_by_name['product_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTINPUT'].fields_by_name['custom_attributes']._loaded_options = None
    _globals['_PRODUCTINPUT'].fields_by_name['custom_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTINPUT']._loaded_options = None
    _globals['_PRODUCTINPUT']._serialized_options = b"\xeaAw\n'merchantapi.googleapis.com/ProductInput\x12/accounts/{account}/productInputs/{productinput}*\rproductInputs2\x0cproductInput"
    _globals['_INSERTPRODUCTINPUTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_INSERTPRODUCTINPUTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"merchantapi.googleapis.com/Product'
    _globals['_INSERTPRODUCTINPUTREQUEST'].fields_by_name['product_input']._loaded_options = None
    _globals['_INSERTPRODUCTINPUTREQUEST'].fields_by_name['product_input']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTPRODUCTINPUTREQUEST'].fields_by_name['data_source']._loaded_options = None
    _globals['_INSERTPRODUCTINPUTREQUEST'].fields_by_name['data_source']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPRODUCTINPUTREQUEST'].fields_by_name['product_input']._loaded_options = None
    _globals['_UPDATEPRODUCTINPUTREQUEST'].fields_by_name['product_input']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPRODUCTINPUTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPRODUCTINPUTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEPRODUCTINPUTREQUEST'].fields_by_name['data_source']._loaded_options = None
    _globals['_UPDATEPRODUCTINPUTREQUEST'].fields_by_name['data_source']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPRODUCTINPUTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPRODUCTINPUTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'merchantapi.googleapis.com/ProductInput"
    _globals['_DELETEPRODUCTINPUTREQUEST'].fields_by_name['data_source']._loaded_options = None
    _globals['_DELETEPRODUCTINPUTREQUEST'].fields_by_name['data_source']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTINPUTSSERVICE']._loaded_options = None
    _globals['_PRODUCTINPUTSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_PRODUCTINPUTSSERVICE'].methods_by_name['InsertProductInput']._loaded_options = None
    _globals['_PRODUCTINPUTSSERVICE'].methods_by_name['InsertProductInput']._serialized_options = b'\x82\xd3\xe4\x93\x02F"5/products/v1/{parent=accounts/*}/productInputs:insert:\rproduct_input'
    _globals['_PRODUCTINPUTSSERVICE'].methods_by_name['UpdateProductInput']._loaded_options = None
    _globals['_PRODUCTINPUTSSERVICE'].methods_by_name['UpdateProductInput']._serialized_options = b'\xdaA\x19product_input,update_mask\x82\xd3\xe4\x93\x02M2</products/v1/{product_input.name=accounts/*/productInputs/*}:\rproduct_input'
    _globals['_PRODUCTINPUTSSERVICE'].methods_by_name['DeleteProductInput']._loaded_options = None
    _globals['_PRODUCTINPUTSSERVICE'].methods_by_name['DeleteProductInput']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020*./products/v1/{name=accounts/*/productInputs/*}'
    _globals['_PRODUCTINPUT']._serialized_start = 371
    _globals['_PRODUCTINPUT']._serialized_end = 882
    _globals['_INSERTPRODUCTINPUTREQUEST']._serialized_start = 885
    _globals['_INSERTPRODUCTINPUTREQUEST']._serialized_end = 1078
    _globals['_UPDATEPRODUCTINPUTREQUEST']._serialized_start = 1081
    _globals['_UPDATEPRODUCTINPUTREQUEST']._serialized_end = 1268
    _globals['_DELETEPRODUCTINPUTREQUEST']._serialized_start = 1270
    _globals['_DELETEPRODUCTINPUTREQUEST']._serialized_end = 1386
    _globals['_PRODUCTINPUTSSERVICE']._serialized_start = 1389
    _globals['_PRODUCTINPUTSSERVICE']._serialized_end = 2130