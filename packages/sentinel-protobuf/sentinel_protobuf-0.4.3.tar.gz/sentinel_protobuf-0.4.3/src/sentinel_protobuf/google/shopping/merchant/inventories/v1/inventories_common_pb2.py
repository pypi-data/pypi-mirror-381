"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/inventories/v1/inventories_common.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
from ......google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/shopping/merchant/inventories/v1/inventories_common.proto\x12\'google.shopping.merchant.inventories.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a google/shopping/type/types.proto\x1a\x1agoogle/type/interval.proto"\xd2\x08\n\x18LocalInventoryAttributes\x12/\n\x05price\x18\x01 \x01(\x0b2\x1b.google.shopping.type.PriceB\x03\xe0A\x01\x124\n\nsale_price\x18\x02 \x01(\x0b2\x1b.google.shopping.type.PriceB\x03\xe0A\x01\x12=\n\x19sale_price_effective_date\x18\x03 \x01(\x0b2\x15.google.type.IntervalB\x03\xe0A\x01\x12i\n\x0cavailability\x18\x04 \x01(\x0e2N.google.shopping.merchant.inventories.v1.LocalInventoryAttributes.AvailabilityH\x00\x88\x01\x01\x12\x1a\n\x08quantity\x18\x05 \x01(\x03B\x03\xe0A\x01H\x01\x88\x01\x01\x12o\n\rpickup_method\x18\x06 \x01(\x0e2N.google.shopping.merchant.inventories.v1.LocalInventoryAttributes.PickupMethodB\x03\xe0A\x01H\x02\x88\x01\x01\x12i\n\npickup_sla\x18\x07 \x01(\x0e2K.google.shopping.merchant.inventories.v1.LocalInventoryAttributes.PickupSlaB\x03\xe0A\x01H\x03\x88\x01\x01\x12*\n\x18instore_product_location\x18\x08 \x01(\tB\x03\xe0A\x01H\x04\x88\x01\x01"\x8f\x01\n\x0cAvailability\x12,\n(LOCAL_INVENTORY_AVAILABILITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08IN_STOCK\x10\x01\x12\x18\n\x14LIMITED_AVAILABILITY\x10\x02\x12\x17\n\x13ON_DISPLAY_TO_ORDER\x10\x03\x12\x10\n\x0cOUT_OF_STOCK\x10\x04"i\n\x0cPickupMethod\x12\x1d\n\x19PICKUP_METHOD_UNSPECIFIED\x10\x00\x12\x07\n\x03BUY\x10\x01\x12\x0b\n\x07RESERVE\x10\x02\x12\x11\n\rSHIP_TO_STORE\x10\x03\x12\x11\n\rNOT_SUPPORTED\x10\x04"\xa7\x01\n\tPickupSla\x12\x1a\n\x16PICKUP_SLA_UNSPECIFIED\x10\x00\x12\x0c\n\x08SAME_DAY\x10\x01\x12\x0c\n\x08NEXT_DAY\x10\x02\x12\x0b\n\x07TWO_DAY\x10\x03\x12\r\n\tTHREE_DAY\x10\x04\x12\x0c\n\x08FOUR_DAY\x10\x05\x12\x0c\n\x08FIVE_DAY\x10\x06\x12\x0b\n\x07SIX_DAY\x10\x07\x12\r\n\tSEVEN_DAY\x10\x08\x12\x0e\n\nMULTI_WEEK\x10\tB\x0f\n\r_availabilityB\x0b\n\t_quantityB\x10\n\x0e_pickup_methodB\r\n\x0b_pickup_slaB\x1b\n\x19_instore_product_location"\xa8\x03\n\x1bRegionalInventoryAttributes\x12/\n\x05price\x18\x01 \x01(\x0b2\x1b.google.shopping.type.PriceB\x03\xe0A\x01\x124\n\nsale_price\x18\x02 \x01(\x0b2\x1b.google.shopping.type.PriceB\x03\xe0A\x01\x12=\n\x19sale_price_effective_date\x18\x03 \x01(\x0b2\x15.google.type.IntervalB\x03\xe0A\x01\x12q\n\x0cavailability\x18\x04 \x01(\x0e2Q.google.shopping.merchant.inventories.v1.RegionalInventoryAttributes.AvailabilityB\x03\xe0A\x01H\x00\x88\x01\x01"_\n\x0cAvailability\x12/\n+REGIONAL_INVENTORY_AVAILABILITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08IN_STOCK\x10\x01\x12\x10\n\x0cOUT_OF_STOCK\x10\x02B\x0f\n\r_availabilityB\x9e\x02\n+com.google.shopping.merchant.inventories.v1B\x16InventoriesCommonProtoP\x01ZScloud.google.com/go/shopping/merchant/inventories/apiv1/inventoriespb;inventoriespb\xaa\x02\'Google.Shopping.Merchant.Inventories.V1\xca\x02\'Google\\Shopping\\Merchant\\Inventories\\V1\xea\x02+Google::Shopping::Merchant::Inventories::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.inventories.v1.inventories_common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.shopping.merchant.inventories.v1B\x16InventoriesCommonProtoP\x01ZScloud.google.com/go/shopping/merchant/inventories/apiv1/inventoriespb;inventoriespb\xaa\x02'Google.Shopping.Merchant.Inventories.V1\xca\x02'Google\\Shopping\\Merchant\\Inventories\\V1\xea\x02+Google::Shopping::Merchant::Inventories::V1"
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['price']._loaded_options = None
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['price']._serialized_options = b'\xe0A\x01'
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['sale_price']._loaded_options = None
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['sale_price']._serialized_options = b'\xe0A\x01'
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['sale_price_effective_date']._loaded_options = None
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['sale_price_effective_date']._serialized_options = b'\xe0A\x01'
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['quantity']._loaded_options = None
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['quantity']._serialized_options = b'\xe0A\x01'
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['pickup_method']._loaded_options = None
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['pickup_method']._serialized_options = b'\xe0A\x01'
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['pickup_sla']._loaded_options = None
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['pickup_sla']._serialized_options = b'\xe0A\x01'
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['instore_product_location']._loaded_options = None
    _globals['_LOCALINVENTORYATTRIBUTES'].fields_by_name['instore_product_location']._serialized_options = b'\xe0A\x01'
    _globals['_REGIONALINVENTORYATTRIBUTES'].fields_by_name['price']._loaded_options = None
    _globals['_REGIONALINVENTORYATTRIBUTES'].fields_by_name['price']._serialized_options = b'\xe0A\x01'
    _globals['_REGIONALINVENTORYATTRIBUTES'].fields_by_name['sale_price']._loaded_options = None
    _globals['_REGIONALINVENTORYATTRIBUTES'].fields_by_name['sale_price']._serialized_options = b'\xe0A\x01'
    _globals['_REGIONALINVENTORYATTRIBUTES'].fields_by_name['sale_price_effective_date']._loaded_options = None
    _globals['_REGIONALINVENTORYATTRIBUTES'].fields_by_name['sale_price_effective_date']._serialized_options = b'\xe0A\x01'
    _globals['_REGIONALINVENTORYATTRIBUTES'].fields_by_name['availability']._loaded_options = None
    _globals['_REGIONALINVENTORYATTRIBUTES'].fields_by_name['availability']._serialized_options = b'\xe0A\x01'
    _globals['_LOCALINVENTORYATTRIBUTES']._serialized_start = 205
    _globals['_LOCALINVENTORYATTRIBUTES']._serialized_end = 1311
    _globals['_LOCALINVENTORYATTRIBUTES_AVAILABILITY']._serialized_start = 799
    _globals['_LOCALINVENTORYATTRIBUTES_AVAILABILITY']._serialized_end = 942
    _globals['_LOCALINVENTORYATTRIBUTES_PICKUPMETHOD']._serialized_start = 944
    _globals['_LOCALINVENTORYATTRIBUTES_PICKUPMETHOD']._serialized_end = 1049
    _globals['_LOCALINVENTORYATTRIBUTES_PICKUPSLA']._serialized_start = 1052
    _globals['_LOCALINVENTORYATTRIBUTES_PICKUPSLA']._serialized_end = 1219
    _globals['_REGIONALINVENTORYATTRIBUTES']._serialized_start = 1314
    _globals['_REGIONALINVENTORYATTRIBUTES']._serialized_end = 1738
    _globals['_REGIONALINVENTORYATTRIBUTES_AVAILABILITY']._serialized_start = 1626
    _globals['_REGIONALINVENTORYATTRIBUTES_AVAILABILITY']._serialized_end = 1721