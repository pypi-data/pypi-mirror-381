"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/productstudio/v1alpha/image.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.shopping.merchant.productstudio.v1alpha import productstudio_common_pb2 as google_dot_shopping_dot_merchant_dot_productstudio_dot_v1alpha_dot_productstudio__common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/shopping/merchant/productstudio/v1alpha/image.proto\x12.google.shopping.merchant.productstudio.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1aIgoogle/shopping/merchant/productstudio/v1alpha/productstudio_common.proto"\xd3\x02\n%GenerateProductImageBackgroundRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12]\n\routput_config\x18\x02 \x01(\x0b2A.google.shopping.merchant.productstudio.v1alpha.OutputImageConfigB\x03\xe0A\x01\x12T\n\x0binput_image\x18\x03 \x01(\x0b2:.google.shopping.merchant.productstudio.v1alpha.InputImageB\x03\xe0A\x02\x12b\n\x06config\x18\x04 \x01(\x0b2M.google.shopping.merchant.productstudio.v1alpha.GenerateImageBackgroundConfigB\x03\xe0A\x02"\x81\x01\n&GenerateProductImageBackgroundResponse\x12W\n\x0fgenerated_image\x18\x01 \x01(\x0b2>.google.shopping.merchant.productstudio.v1alpha.GeneratedImage"\xcf\x02\n#RemoveProductImageBackgroundRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12]\n\routput_config\x18\x02 \x01(\x0b2A.google.shopping.merchant.productstudio.v1alpha.OutputImageConfigB\x03\xe0A\x01\x12T\n\x0binput_image\x18\x03 \x01(\x0b2:.google.shopping.merchant.productstudio.v1alpha.InputImageB\x03\xe0A\x02\x12`\n\x06config\x18\x04 \x01(\x0b2K.google.shopping.merchant.productstudio.v1alpha.RemoveImageBackgroundConfigB\x03\xe0A\x01"\x7f\n$RemoveProductImageBackgroundResponse\x12W\n\x0fgenerated_image\x18\x01 \x01(\x0b2>.google.shopping.merchant.productstudio.v1alpha.GeneratedImage"\xe4\x01\n\x1aUpscaleProductImageRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12]\n\routput_config\x18\x02 \x01(\x0b2A.google.shopping.merchant.productstudio.v1alpha.OutputImageConfigB\x03\xe0A\x01\x12T\n\x0binput_image\x18\x03 \x01(\x0b2:.google.shopping.merchant.productstudio.v1alpha.InputImageB\x03\xe0A\x02"v\n\x1bUpscaleProductImageResponse\x12W\n\x0fgenerated_image\x18\x01 \x01(\x0b2>.google.shopping.merchant.productstudio.v1alpha.GeneratedImage"\x90\x02\n\x0eGeneratedImage\x12\r\n\x03uri\x18\x02 \x01(\tH\x00\x12\x15\n\x0bimage_bytes\x18\x03 \x01(\x0cH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x123\n\x0fgeneration_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp:\x86\x01\xeaA\x82\x01\n)merchantapi.googleapis.com/GeneratedImage\x124accounts/{account}/generatedImages/{generated_image}*\x0fgeneratedImages2\x0egeneratedImageB\x07\n\x05image"2\n\x11OutputImageConfig\x12\x1d\n\x10return_image_uri\x18\x01 \x01(\x08B\x03\xe0A\x01"f\n\x1dGenerateImageBackgroundConfig\x12 \n\x13product_description\x18\x01 \x01(\tB\x03\xe0A\x02\x12#\n\x16background_description\x18\x02 \x01(\tB\x03\xe0A\x02"v\n\x1bRemoveImageBackgroundConfig\x12W\n\x10background_color\x18\x01 \x01(\x0b28.google.shopping.merchant.productstudio.v1alpha.RgbColorB\x03\xe0A\x01"C\n\x08RgbColor\x12\x10\n\x03red\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x12\n\x05green\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x11\n\x04blue\x18\x03 \x01(\x05B\x03\xe0A\x012\xda\x07\n\x0cImageService\x12\xba\x02\n\x1eGenerateProductImageBackground\x12U.google.shopping.merchant.productstudio.v1alpha.GenerateProductImageBackgroundRequest\x1aV.google.shopping.merchant.productstudio.v1alpha.GenerateProductImageBackgroundResponse"i\xdaA\x04name\x82\xd3\xe4\x93\x02\\"W/productstudio/v1alpha/{name=accounts/*}/generatedImages:generateProductImageBackground:\x01*\x12\xb2\x02\n\x1cRemoveProductImageBackground\x12S.google.shopping.merchant.productstudio.v1alpha.RemoveProductImageBackgroundRequest\x1aT.google.shopping.merchant.productstudio.v1alpha.RemoveProductImageBackgroundResponse"g\xdaA\x04name\x82\xd3\xe4\x93\x02Z"U/productstudio/v1alpha/{name=accounts/*}/generatedImages:removeProductImageBackground:\x01*\x12\x8e\x02\n\x13UpscaleProductImage\x12J.google.shopping.merchant.productstudio.v1alpha.UpscaleProductImageRequest\x1aK.google.shopping.merchant.productstudio.v1alpha.UpscaleProductImageResponse"^\xdaA\x04name\x82\xd3\xe4\x93\x02Q"L/productstudio/v1alpha/{name=accounts/*}/generatedImages:upscaleProductImage:\x01*\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xa2\x01\n2com.google.shopping.merchant.productstudio.v1alphaB\nImageProtoP\x01Z^cloud.google.com/go/shopping/merchant/productstudio/apiv1alpha/productstudiopb;productstudiopbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.productstudio.v1alpha.image_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n2com.google.shopping.merchant.productstudio.v1alphaB\nImageProtoP\x01Z^cloud.google.com/go/shopping/merchant/productstudio/apiv1alpha/productstudiopb;productstudiopb'
    _globals['_GENERATEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GENERATEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_GENERATEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['input_image']._loaded_options = None
    _globals['_GENERATEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['input_image']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['config']._loaded_options = None
    _globals['_GENERATEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['config']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REMOVEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_REMOVEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x01'
    _globals['_REMOVEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['input_image']._loaded_options = None
    _globals['_REMOVEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['input_image']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['config']._loaded_options = None
    _globals['_REMOVEPRODUCTIMAGEBACKGROUNDREQUEST'].fields_by_name['config']._serialized_options = b'\xe0A\x01'
    _globals['_UPSCALEPRODUCTIMAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPSCALEPRODUCTIMAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_UPSCALEPRODUCTIMAGEREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_UPSCALEPRODUCTIMAGEREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x01'
    _globals['_UPSCALEPRODUCTIMAGEREQUEST'].fields_by_name['input_image']._loaded_options = None
    _globals['_UPSCALEPRODUCTIMAGEREQUEST'].fields_by_name['input_image']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEDIMAGE'].fields_by_name['name']._loaded_options = None
    _globals['_GENERATEDIMAGE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_GENERATEDIMAGE']._loaded_options = None
    _globals['_GENERATEDIMAGE']._serialized_options = b'\xeaA\x82\x01\n)merchantapi.googleapis.com/GeneratedImage\x124accounts/{account}/generatedImages/{generated_image}*\x0fgeneratedImages2\x0egeneratedImage'
    _globals['_OUTPUTIMAGECONFIG'].fields_by_name['return_image_uri']._loaded_options = None
    _globals['_OUTPUTIMAGECONFIG'].fields_by_name['return_image_uri']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEIMAGEBACKGROUNDCONFIG'].fields_by_name['product_description']._loaded_options = None
    _globals['_GENERATEIMAGEBACKGROUNDCONFIG'].fields_by_name['product_description']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEIMAGEBACKGROUNDCONFIG'].fields_by_name['background_description']._loaded_options = None
    _globals['_GENERATEIMAGEBACKGROUNDCONFIG'].fields_by_name['background_description']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEIMAGEBACKGROUNDCONFIG'].fields_by_name['background_color']._loaded_options = None
    _globals['_REMOVEIMAGEBACKGROUNDCONFIG'].fields_by_name['background_color']._serialized_options = b'\xe0A\x01'
    _globals['_RGBCOLOR'].fields_by_name['red']._loaded_options = None
    _globals['_RGBCOLOR'].fields_by_name['red']._serialized_options = b'\xe0A\x01'
    _globals['_RGBCOLOR'].fields_by_name['green']._loaded_options = None
    _globals['_RGBCOLOR'].fields_by_name['green']._serialized_options = b'\xe0A\x01'
    _globals['_RGBCOLOR'].fields_by_name['blue']._loaded_options = None
    _globals['_RGBCOLOR'].fields_by_name['blue']._serialized_options = b'\xe0A\x01'
    _globals['_IMAGESERVICE']._loaded_options = None
    _globals['_IMAGESERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_IMAGESERVICE'].methods_by_name['GenerateProductImageBackground']._loaded_options = None
    _globals['_IMAGESERVICE'].methods_by_name['GenerateProductImageBackground']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\\"W/productstudio/v1alpha/{name=accounts/*}/generatedImages:generateProductImageBackground:\x01*'
    _globals['_IMAGESERVICE'].methods_by_name['RemoveProductImageBackground']._loaded_options = None
    _globals['_IMAGESERVICE'].methods_by_name['RemoveProductImageBackground']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02Z"U/productstudio/v1alpha/{name=accounts/*}/generatedImages:removeProductImageBackground:\x01*'
    _globals['_IMAGESERVICE'].methods_by_name['UpscaleProductImage']._loaded_options = None
    _globals['_IMAGESERVICE'].methods_by_name['UpscaleProductImage']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02Q"L/productstudio/v1alpha/{name=accounts/*}/generatedImages:upscaleProductImage:\x01*'
    _globals['_GENERATEPRODUCTIMAGEBACKGROUNDREQUEST']._serialized_start = 334
    _globals['_GENERATEPRODUCTIMAGEBACKGROUNDREQUEST']._serialized_end = 673
    _globals['_GENERATEPRODUCTIMAGEBACKGROUNDRESPONSE']._serialized_start = 676
    _globals['_GENERATEPRODUCTIMAGEBACKGROUNDRESPONSE']._serialized_end = 805
    _globals['_REMOVEPRODUCTIMAGEBACKGROUNDREQUEST']._serialized_start = 808
    _globals['_REMOVEPRODUCTIMAGEBACKGROUNDREQUEST']._serialized_end = 1143
    _globals['_REMOVEPRODUCTIMAGEBACKGROUNDRESPONSE']._serialized_start = 1145
    _globals['_REMOVEPRODUCTIMAGEBACKGROUNDRESPONSE']._serialized_end = 1272
    _globals['_UPSCALEPRODUCTIMAGEREQUEST']._serialized_start = 1275
    _globals['_UPSCALEPRODUCTIMAGEREQUEST']._serialized_end = 1503
    _globals['_UPSCALEPRODUCTIMAGERESPONSE']._serialized_start = 1505
    _globals['_UPSCALEPRODUCTIMAGERESPONSE']._serialized_end = 1623
    _globals['_GENERATEDIMAGE']._serialized_start = 1626
    _globals['_GENERATEDIMAGE']._serialized_end = 1898
    _globals['_OUTPUTIMAGECONFIG']._serialized_start = 1900
    _globals['_OUTPUTIMAGECONFIG']._serialized_end = 1950
    _globals['_GENERATEIMAGEBACKGROUNDCONFIG']._serialized_start = 1952
    _globals['_GENERATEIMAGEBACKGROUNDCONFIG']._serialized_end = 2054
    _globals['_REMOVEIMAGEBACKGROUNDCONFIG']._serialized_start = 2056
    _globals['_REMOVEIMAGEBACKGROUNDCONFIG']._serialized_end = 2174
    _globals['_RGBCOLOR']._serialized_start = 2176
    _globals['_RGBCOLOR']._serialized_end = 2243
    _globals['_IMAGESERVICE']._serialized_start = 2246
    _globals['_IMAGESERVICE']._serialized_end = 3232