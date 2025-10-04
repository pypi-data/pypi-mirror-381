"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/product.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import common_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_common__pb2
from .....google.cloud.retail.v2alpha import promotion_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_promotion__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/retail/v2alpha/product.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/retail/v2alpha/common.proto\x1a+google/cloud/retail/v2alpha/promotion.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x9c\x0e\n\x07Product\x121\n\x0bexpire_time\x18\x10 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12-\n\x03ttl\x18\x11 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x04H\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x0f\n\x02id\x18\x02 \x01(\tB\x03\xe0A\x05\x12<\n\x04type\x18\x03 \x01(\x0e2).google.cloud.retail.v2alpha.Product.TypeB\x03\xe0A\x05\x12\x1a\n\x12primary_product_id\x18\x04 \x01(\t\x12\x1d\n\x15collection_member_ids\x18\x05 \x03(\t\x12\x0c\n\x04gtin\x18\x06 \x01(\t\x12\x12\n\ncategories\x18\x07 \x03(\t\x12\x12\n\x05title\x18\x08 \x01(\tB\x03\xe0A\x02\x12\x0e\n\x06brands\x18\t \x03(\t\x12\x13\n\x0bdescription\x18\n \x01(\t\x12\x15\n\rlanguage_code\x18\x0b \x01(\t\x12H\n\nattributes\x18\x0c \x03(\x0b24.google.cloud.retail.v2alpha.Product.AttributesEntry\x12\x0c\n\x04tags\x18\r \x03(\t\x12:\n\nprice_info\x18\x0e \x01(\x0b2&.google.cloud.retail.v2alpha.PriceInfo\x123\n\x06rating\x18\x0f \x01(\x0b2#.google.cloud.retail.v2alpha.Rating\x122\n\x0eavailable_time\x18\x12 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12G\n\x0cavailability\x18\x13 \x01(\x0e21.google.cloud.retail.v2alpha.Product.Availability\x127\n\x12available_quantity\x18\x14 \x01(\x0b2\x1b.google.protobuf.Int32Value\x12F\n\x10fulfillment_info\x18\x15 \x03(\x0b2,.google.cloud.retail.v2alpha.FulfillmentInfo\x12\x0b\n\x03uri\x18\x16 \x01(\t\x122\n\x06images\x18\x17 \x03(\x0b2".google.cloud.retail.v2alpha.Image\x127\n\x08audience\x18\x18 \x01(\x0b2%.google.cloud.retail.v2alpha.Audience\x12:\n\ncolor_info\x18\x19 \x01(\x0b2&.google.cloud.retail.v2alpha.ColorInfo\x12\r\n\x05sizes\x18\x1a \x03(\t\x12\x11\n\tmaterials\x18\x1b \x03(\t\x12\x10\n\x08patterns\x18\x1c \x03(\t\x12\x12\n\nconditions\x18\x1d \x03(\t\x12:\n\npromotions\x18" \x03(\x0b2&.google.cloud.retail.v2alpha.Promotion\x120\n\x0cpublish_time\x18! \x01(\x0b2\x1a.google.protobuf.Timestamp\x12:\n\x12retrievable_fields\x18\x1e \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x02\x18\x01\x12;\n\x08variants\x18\x1f \x03(\x0b2$.google.cloud.retail.v2alpha.ProductB\x03\xe0A\x03\x12K\n\x11local_inventories\x18# \x03(\x0b2+.google.cloud.retail.v2alpha.LocalInventoryB\x03\xe0A\x03\x1a_\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b2,.google.cloud.retail.v2alpha.CustomAttribute:\x028\x01"F\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PRIMARY\x10\x01\x12\x0b\n\x07VARIANT\x10\x02\x12\x0e\n\nCOLLECTION\x10\x03"i\n\x0cAvailability\x12\x1c\n\x18AVAILABILITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08IN_STOCK\x10\x01\x12\x10\n\x0cOUT_OF_STOCK\x10\x02\x12\x0c\n\x08PREORDER\x10\x03\x12\r\n\tBACKORDER\x10\x04:\x84\x01\xeaA\x80\x01\n\x1dretail.googleapis.com/Product\x12_projects/{project}/locations/{location}/catalogs/{catalog}/branches/{branch}/products/{product}B\x0c\n\nexpirationB\xd0\x01\n\x1fcom.google.cloud.retail.v2alphaB\x0cProductProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.product_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x0cProductProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_PRODUCT_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_PRODUCT_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_PRODUCT'].fields_by_name['ttl']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['ttl']._serialized_options = b'\xe0A\x04'
    _globals['_PRODUCT'].fields_by_name['name']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_PRODUCT'].fields_by_name['id']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['id']._serialized_options = b'\xe0A\x05'
    _globals['_PRODUCT'].fields_by_name['type']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_PRODUCT'].fields_by_name['title']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['title']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCT'].fields_by_name['retrievable_fields']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['retrievable_fields']._serialized_options = b'\x18\x01'
    _globals['_PRODUCT'].fields_by_name['variants']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['variants']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['local_inventories']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['local_inventories']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT']._loaded_options = None
    _globals['_PRODUCT']._serialized_options = b'\xeaA\x80\x01\n\x1dretail.googleapis.com/Product\x12_projects/{project}/locations/{location}/catalogs/{catalog}/branches/{branch}/products/{product}'
    _globals['_PRODUCT']._serialized_start = 353
    _globals['_PRODUCT']._serialized_end = 2173
    _globals['_PRODUCT_ATTRIBUTESENTRY']._serialized_start = 1750
    _globals['_PRODUCT_ATTRIBUTESENTRY']._serialized_end = 1845
    _globals['_PRODUCT_TYPE']._serialized_start = 1847
    _globals['_PRODUCT_TYPE']._serialized_end = 1917
    _globals['_PRODUCT_AVAILABILITY']._serialized_start = 1919
    _globals['_PRODUCT_AVAILABILITY']._serialized_end = 2024