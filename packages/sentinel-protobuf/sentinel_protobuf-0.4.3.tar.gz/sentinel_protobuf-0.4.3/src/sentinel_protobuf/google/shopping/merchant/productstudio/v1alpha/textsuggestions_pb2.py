"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/productstudio/v1alpha/textsuggestions.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/shopping/merchant/productstudio/v1alpha/textsuggestions.proto\x12.google.shopping.merchant.productstudio.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto"\xd8\x02\n%GenerateProductTextSuggestionsRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12V\n\x0cproduct_info\x18\x02 \x01(\x0b2;.google.shopping.merchant.productstudio.v1alpha.ProductInfoB\x03\xe0A\x02\x12Y\n\x0boutput_spec\x18\x03 \x01(\x0b2:.google.shopping.merchant.productstudio.v1alpha.OutputSpecB\x03\xe0A\x01H\x00\x88\x01\x01\x12Y\n\x0etitle_examples\x18\x04 \x03(\x0b2<.google.shopping.merchant.productstudio.v1alpha.TitleExampleB\x03\xe0A\x01B\x0e\n\x0c_output_spec"\xb4\x04\n&GenerateProductTextSuggestionsResponse\x12c\n\x05title\x18\x01 \x01(\x0b2O.google.shopping.merchant.productstudio.v1alpha.ProductTextGenerationSuggestionH\x00\x88\x01\x01\x12i\n\x0bdescription\x18\x02 \x01(\x0b2O.google.shopping.merchant.productstudio.v1alpha.ProductTextGenerationSuggestionH\x01\x88\x01\x01\x12z\n\nattributes\x18\x03 \x03(\x0b2f.google.shopping.merchant.productstudio.v1alpha.GenerateProductTextSuggestionsResponse.AttributesEntry\x12d\n\x08metadata\x18\x04 \x01(\x0b2M.google.shopping.merchant.productstudio.v1alpha.ProductTextGenerationMetadataH\x02\x88\x01\x01\x1a1\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x08\n\x06_titleB\x0e\n\x0c_descriptionB\x0b\n\t_metadata"\xb4\x03\n\x0cTitleExample\x12h\n\x0cproduct_info\x18\x01 \x03(\x0b2M.google.shopping.merchant.productstudio.v1alpha.TitleExample.ProductInfoEntryB\x03\xe0A\x02\x12\x1a\n\x08category\x18\x02 \x01(\tB\x03\xe0A\x02H\x00\x88\x01\x01\x12\x1e\n\x0ctitle_format\x18\x03 \x01(\tB\x03\xe0A\x02H\x01\x88\x01\x01\x12s\n\x12final_product_info\x18\x04 \x03(\x0b2R.google.shopping.merchant.productstudio.v1alpha.TitleExample.FinalProductInfoEntryB\x03\xe0A\x02\x1a2\n\x10ProductInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a7\n\x15FinalProductInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x0b\n\t_categoryB\x0f\n\r_title_format"J\n\x1dProductTextGenerationMetadata\x12)\n\x08metadata\x18\x01 \x01(\x0b2\x17.google.protobuf.Struct"/\n\x05Image\x12\r\n\x03uri\x18\x01 \x01(\tH\x00\x12\x0e\n\x04data\x18\x02 \x01(\x0cH\x00B\x07\n\x05image"\xa6\x02\n\x0bProductInfo\x12s\n\x12product_attributes\x18\x01 \x03(\x0b2R.google.shopping.merchant.productstudio.v1alpha.ProductInfo.ProductAttributesEntryB\x03\xe0A\x02\x12V\n\rproduct_image\x18\x02 \x01(\x0b25.google.shopping.merchant.productstudio.v1alpha.ImageB\x03\xe0A\x01H\x00\x88\x01\x01\x1a8\n\x16ProductAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x10\n\x0e_product_image"\xab\x02\n\nOutputSpec\x12\x1d\n\x0bworkflow_id\x18\x01 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12\x16\n\x04tone\x18\x02 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x12#\n\x11editorial_changes\x18\x03 \x01(\tB\x03\xe0A\x01H\x02\x88\x01\x01\x12!\n\x0ftarget_language\x18\x04 \x01(\tB\x03\xe0A\x01H\x03\x88\x01\x01\x12\x1c\n\x0fattribute_order\x18\x05 \x03(\tB\x03\xe0A\x01\x12%\n\x13attribute_separator\x18\x06 \x01(\tB\x03\xe0A\x01H\x04\x88\x01\x01B\x0e\n\x0c_workflow_idB\x07\n\x05_toneB\x14\n\x12_editorial_changesB\x12\n\x10_target_languageB\x16\n\x14_attribute_separator"\x8b\x01\n\x1fProductTextGenerationSuggestion\x12\x11\n\x04text\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05score\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x1b\n\x0echange_summary\x18\x03 \x01(\tH\x02\x88\x01\x01B\x07\n\x05_textB\x08\n\x06_scoreB\x11\n\x0f_change_summary2\x8e\x03\n\x16TextSuggestionsService\x12\xaa\x02\n\x1eGenerateProductTextSuggestions\x12U.google.shopping.merchant.productstudio.v1alpha.GenerateProductTextSuggestionsRequest\x1aV.google.shopping.merchant.productstudio.v1alpha.GenerateProductTextSuggestionsResponse"Y\xdaA\x04name\x82\xd3\xe4\x93\x02L"G/productstudio/v1alpha/{name=accounts/*}:generateProductTextSuggestions:\x01*\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xac\x01\n2com.google.shopping.merchant.productstudio.v1alphaB\x14TextSuggestionsProtoP\x01Z^cloud.google.com/go/shopping/merchant/productstudio/apiv1alpha/productstudiopb;productstudiopbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.productstudio.v1alpha.textsuggestions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n2com.google.shopping.merchant.productstudio.v1alphaB\x14TextSuggestionsProtoP\x01Z^cloud.google.com/go/shopping/merchant/productstudio/apiv1alpha/productstudiopb;productstudiopb'
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSREQUEST'].fields_by_name['product_info']._loaded_options = None
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSREQUEST'].fields_by_name['product_info']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSREQUEST'].fields_by_name['output_spec']._loaded_options = None
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSREQUEST'].fields_by_name['output_spec']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSREQUEST'].fields_by_name['title_examples']._loaded_options = None
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSREQUEST'].fields_by_name['title_examples']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSRESPONSE_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSRESPONSE_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_TITLEEXAMPLE_PRODUCTINFOENTRY']._loaded_options = None
    _globals['_TITLEEXAMPLE_PRODUCTINFOENTRY']._serialized_options = b'8\x01'
    _globals['_TITLEEXAMPLE_FINALPRODUCTINFOENTRY']._loaded_options = None
    _globals['_TITLEEXAMPLE_FINALPRODUCTINFOENTRY']._serialized_options = b'8\x01'
    _globals['_TITLEEXAMPLE'].fields_by_name['product_info']._loaded_options = None
    _globals['_TITLEEXAMPLE'].fields_by_name['product_info']._serialized_options = b'\xe0A\x02'
    _globals['_TITLEEXAMPLE'].fields_by_name['category']._loaded_options = None
    _globals['_TITLEEXAMPLE'].fields_by_name['category']._serialized_options = b'\xe0A\x02'
    _globals['_TITLEEXAMPLE'].fields_by_name['title_format']._loaded_options = None
    _globals['_TITLEEXAMPLE'].fields_by_name['title_format']._serialized_options = b'\xe0A\x02'
    _globals['_TITLEEXAMPLE'].fields_by_name['final_product_info']._loaded_options = None
    _globals['_TITLEEXAMPLE'].fields_by_name['final_product_info']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTINFO_PRODUCTATTRIBUTESENTRY']._loaded_options = None
    _globals['_PRODUCTINFO_PRODUCTATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_PRODUCTINFO'].fields_by_name['product_attributes']._loaded_options = None
    _globals['_PRODUCTINFO'].fields_by_name['product_attributes']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTINFO'].fields_by_name['product_image']._loaded_options = None
    _globals['_PRODUCTINFO'].fields_by_name['product_image']._serialized_options = b'\xe0A\x01'
    _globals['_OUTPUTSPEC'].fields_by_name['workflow_id']._loaded_options = None
    _globals['_OUTPUTSPEC'].fields_by_name['workflow_id']._serialized_options = b'\xe0A\x01'
    _globals['_OUTPUTSPEC'].fields_by_name['tone']._loaded_options = None
    _globals['_OUTPUTSPEC'].fields_by_name['tone']._serialized_options = b'\xe0A\x01'
    _globals['_OUTPUTSPEC'].fields_by_name['editorial_changes']._loaded_options = None
    _globals['_OUTPUTSPEC'].fields_by_name['editorial_changes']._serialized_options = b'\xe0A\x01'
    _globals['_OUTPUTSPEC'].fields_by_name['target_language']._loaded_options = None
    _globals['_OUTPUTSPEC'].fields_by_name['target_language']._serialized_options = b'\xe0A\x01'
    _globals['_OUTPUTSPEC'].fields_by_name['attribute_order']._loaded_options = None
    _globals['_OUTPUTSPEC'].fields_by_name['attribute_order']._serialized_options = b'\xe0A\x01'
    _globals['_OUTPUTSPEC'].fields_by_name['attribute_separator']._loaded_options = None
    _globals['_OUTPUTSPEC'].fields_by_name['attribute_separator']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTSUGGESTIONSSERVICE']._loaded_options = None
    _globals['_TEXTSUGGESTIONSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_TEXTSUGGESTIONSSERVICE'].methods_by_name['GenerateProductTextSuggestions']._loaded_options = None
    _globals['_TEXTSUGGESTIONSSERVICE'].methods_by_name['GenerateProductTextSuggestions']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02L"G/productstudio/v1alpha/{name=accounts/*}:generateProductTextSuggestions:\x01*'
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSREQUEST']._serialized_start = 239
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSREQUEST']._serialized_end = 583
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSRESPONSE']._serialized_start = 586
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSRESPONSE']._serialized_end = 1150
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSRESPONSE_ATTRIBUTESENTRY']._serialized_start = 1062
    _globals['_GENERATEPRODUCTTEXTSUGGESTIONSRESPONSE_ATTRIBUTESENTRY']._serialized_end = 1111
    _globals['_TITLEEXAMPLE']._serialized_start = 1153
    _globals['_TITLEEXAMPLE']._serialized_end = 1589
    _globals['_TITLEEXAMPLE_PRODUCTINFOENTRY']._serialized_start = 1452
    _globals['_TITLEEXAMPLE_PRODUCTINFOENTRY']._serialized_end = 1502
    _globals['_TITLEEXAMPLE_FINALPRODUCTINFOENTRY']._serialized_start = 1504
    _globals['_TITLEEXAMPLE_FINALPRODUCTINFOENTRY']._serialized_end = 1559
    _globals['_PRODUCTTEXTGENERATIONMETADATA']._serialized_start = 1591
    _globals['_PRODUCTTEXTGENERATIONMETADATA']._serialized_end = 1665
    _globals['_IMAGE']._serialized_start = 1667
    _globals['_IMAGE']._serialized_end = 1714
    _globals['_PRODUCTINFO']._serialized_start = 1717
    _globals['_PRODUCTINFO']._serialized_end = 2011
    _globals['_PRODUCTINFO_PRODUCTATTRIBUTESENTRY']._serialized_start = 1937
    _globals['_PRODUCTINFO_PRODUCTATTRIBUTESENTRY']._serialized_end = 1993
    _globals['_OUTPUTSPEC']._serialized_start = 2014
    _globals['_OUTPUTSPEC']._serialized_end = 2313
    _globals['_PRODUCTTEXTGENERATIONSUGGESTION']._serialized_start = 2316
    _globals['_PRODUCTTEXTGENERATIONSUGGESTION']._serialized_end = 2455
    _globals['_TEXTSUGGESTIONSSERVICE']._serialized_start = 2458
    _globals['_TEXTSUGGESTIONSSERVICE']._serialized_end = 2856