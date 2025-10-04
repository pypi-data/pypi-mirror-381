"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/css/v1/css_product_inputs.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.shopping.css.v1 import css_product_common_pb2 as google_dot_shopping_dot_css_dot_v1_dot_css__product__common__pb2
from .....google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/shopping/css/v1/css_product_inputs.proto\x12\x16google.shopping.css.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a/google/shopping/css/v1/css_product_common.proto\x1a google/shopping/type/types.proto"\xa2\x03\n\x0fCssProductInput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\nfinal_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0fraw_provided_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10content_language\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x17\n\nfeed_label\x18\x05 \x01(\tB\x03\xe0A\x02\x126\n\x0efreshness_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x02\x18\x01\x126\n\nattributes\x18\x07 \x01(\x0b2".google.shopping.css.v1.Attributes\x12@\n\x11custom_attributes\x18\x08 \x03(\x0b2%.google.shopping.type.CustomAttribute:`\xeaA]\n"css.googleapis.com/CssProductInput\x127accounts/{account}/cssProductInputs/{css_product_input}"\xbb\x01\n\x1cInsertCssProductInputRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"css.googleapis.com/CssProductInput\x12G\n\x11css_product_input\x18\x02 \x01(\x0b2\'.google.shopping.css.v1.CssProductInputB\x03\xe0A\x02\x12\x16\n\x07feed_id\x18\x03 \x01(\x03B\x05\x18\x01\xe0A\x01"\x98\x01\n\x1cUpdateCssProductInputRequest\x12G\n\x11css_product_input\x18\x01 \x01(\x0b2\'.google.shopping.css.v1.CssProductInputB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x94\x01\n\x1cDeleteCssProductInputRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"css.googleapis.com/CssProductInput\x12!\n\x14supplemental_feed_id\x18\x02 \x01(\x03H\x00\x88\x01\x01B\x17\n\x15_supplemental_feed_id2\xb0\x05\n\x17CssProductInputsService\x12\xc2\x01\n\x15InsertCssProductInput\x124.google.shopping.css.v1.InsertCssProductInputRequest\x1a\'.google.shopping.css.v1.CssProductInput"J\x82\xd3\xe4\x93\x02D"//v1/{parent=accounts/*}/cssProductInputs:insert:\x11css_product_input\x12\xed\x01\n\x15UpdateCssProductInput\x124.google.shopping.css.v1.UpdateCssProductInputRequest\x1a\'.google.shopping.css.v1.CssProductInput"u\xdaA\x1dcss_product_input,update_mask\x82\xd3\xe4\x93\x02O2:/v1/{css_product_input.name=accounts/*/cssProductInputs/*}:\x11css_product_input\x12\x9e\x01\n\x15DeleteCssProductInput\x124.google.shopping.css.v1.DeleteCssProductInputRequest\x1a\x16.google.protobuf.Empty"7\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1/{name=accounts/*/cssProductInputs/*}\x1a?\xcaA\x12css.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xb7\x01\n\x1acom.google.shopping.css.v1B\x15CssProductInputsProtoP\x01Z2cloud.google.com/go/shopping/css/apiv1/csspb;csspb\xaa\x02\x16Google.Shopping.Css.V1\xca\x02\x16Google\\Shopping\\Css\\V1\xea\x02\x19Google::Shopping::Css::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.css.v1.css_product_inputs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.shopping.css.v1B\x15CssProductInputsProtoP\x01Z2cloud.google.com/go/shopping/css/apiv1/csspb;csspb\xaa\x02\x16Google.Shopping.Css.V1\xca\x02\x16Google\\Shopping\\Css\\V1\xea\x02\x19Google::Shopping::Css::V1'
    _globals['_CSSPRODUCTINPUT'].fields_by_name['final_name']._loaded_options = None
    _globals['_CSSPRODUCTINPUT'].fields_by_name['final_name']._serialized_options = b'\xe0A\x03'
    _globals['_CSSPRODUCTINPUT'].fields_by_name['raw_provided_id']._loaded_options = None
    _globals['_CSSPRODUCTINPUT'].fields_by_name['raw_provided_id']._serialized_options = b'\xe0A\x02'
    _globals['_CSSPRODUCTINPUT'].fields_by_name['content_language']._loaded_options = None
    _globals['_CSSPRODUCTINPUT'].fields_by_name['content_language']._serialized_options = b'\xe0A\x02'
    _globals['_CSSPRODUCTINPUT'].fields_by_name['feed_label']._loaded_options = None
    _globals['_CSSPRODUCTINPUT'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x02'
    _globals['_CSSPRODUCTINPUT'].fields_by_name['freshness_time']._loaded_options = None
    _globals['_CSSPRODUCTINPUT'].fields_by_name['freshness_time']._serialized_options = b'\x18\x01'
    _globals['_CSSPRODUCTINPUT']._loaded_options = None
    _globals['_CSSPRODUCTINPUT']._serialized_options = b'\xeaA]\n"css.googleapis.com/CssProductInput\x127accounts/{account}/cssProductInputs/{css_product_input}'
    _globals['_INSERTCSSPRODUCTINPUTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_INSERTCSSPRODUCTINPUTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"css.googleapis.com/CssProductInput'
    _globals['_INSERTCSSPRODUCTINPUTREQUEST'].fields_by_name['css_product_input']._loaded_options = None
    _globals['_INSERTCSSPRODUCTINPUTREQUEST'].fields_by_name['css_product_input']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTCSSPRODUCTINPUTREQUEST'].fields_by_name['feed_id']._loaded_options = None
    _globals['_INSERTCSSPRODUCTINPUTREQUEST'].fields_by_name['feed_id']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_UPDATECSSPRODUCTINPUTREQUEST'].fields_by_name['css_product_input']._loaded_options = None
    _globals['_UPDATECSSPRODUCTINPUTREQUEST'].fields_by_name['css_product_input']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECSSPRODUCTINPUTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECSSPRODUCTINPUTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"css.googleapis.com/CssProductInput'
    _globals['_CSSPRODUCTINPUTSSERVICE']._loaded_options = None
    _globals['_CSSPRODUCTINPUTSSERVICE']._serialized_options = b"\xcaA\x12css.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_CSSPRODUCTINPUTSSERVICE'].methods_by_name['InsertCssProductInput']._loaded_options = None
    _globals['_CSSPRODUCTINPUTSSERVICE'].methods_by_name['InsertCssProductInput']._serialized_options = b'\x82\xd3\xe4\x93\x02D"//v1/{parent=accounts/*}/cssProductInputs:insert:\x11css_product_input'
    _globals['_CSSPRODUCTINPUTSSERVICE'].methods_by_name['UpdateCssProductInput']._loaded_options = None
    _globals['_CSSPRODUCTINPUTSSERVICE'].methods_by_name['UpdateCssProductInput']._serialized_options = b'\xdaA\x1dcss_product_input,update_mask\x82\xd3\xe4\x93\x02O2:/v1/{css_product_input.name=accounts/*/cssProductInputs/*}:\x11css_product_input'
    _globals['_CSSPRODUCTINPUTSSERVICE'].methods_by_name['DeleteCssProductInput']._loaded_options = None
    _globals['_CSSPRODUCTINPUTSSERVICE'].methods_by_name['DeleteCssProductInput']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1/{name=accounts/*/cssProductInputs/*}'
    _globals['_CSSPRODUCTINPUT']._serialized_start = 370
    _globals['_CSSPRODUCTINPUT']._serialized_end = 788
    _globals['_INSERTCSSPRODUCTINPUTREQUEST']._serialized_start = 791
    _globals['_INSERTCSSPRODUCTINPUTREQUEST']._serialized_end = 978
    _globals['_UPDATECSSPRODUCTINPUTREQUEST']._serialized_start = 981
    _globals['_UPDATECSSPRODUCTINPUTREQUEST']._serialized_end = 1133
    _globals['_DELETECSSPRODUCTINPUTREQUEST']._serialized_start = 1136
    _globals['_DELETECSSPRODUCTINPUTREQUEST']._serialized_end = 1284
    _globals['_CSSPRODUCTINPUTSSERVICE']._serialized_start = 1287
    _globals['_CSSPRODUCTINPUTSSERVICE']._serialized_end = 1975