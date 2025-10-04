"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/inventories/v1/regionalinventory.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ......google.shopping.merchant.inventories.v1 import inventories_common_pb2 as google_dot_shopping_dot_merchant_dot_inventories_dot_v1_dot_inventories__common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/shopping/merchant/inventories/v1/regionalinventory.proto\x12\'google.shopping.merchant.inventories.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a@google/shopping/merchant/inventories/v1/inventories_common.proto"\xbd\x02\n\x11RegionalInventory\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07account\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x16\n\x06region\x18\x03 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12p\n\x1dregional_inventory_attributes\x18\t \x01(\x0b2D.google.shopping.merchant.inventories.v1.RegionalInventoryAttributesB\x03\xe0A\x01:u\xeaAr\n,merchantapi.googleapis.com/RegionalInventory\x12Baccounts/{account}/products/{product}/regionalInventories/{region}"\x8d\x01\n\x1eListRegionalInventoriesRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,merchantapi.googleapis.com/RegionalInventory\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x94\x01\n\x1fListRegionalInventoriesResponse\x12X\n\x14regional_inventories\x18\x01 \x03(\x0b2:.google.shopping.merchant.inventories.v1.RegionalInventory\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc3\x01\n\x1eInsertRegionalInventoryRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,merchantapi.googleapis.com/RegionalInventory\x12[\n\x12regional_inventory\x18\x02 \x01(\x0b2:.google.shopping.merchant.inventories.v1.RegionalInventoryB\x03\xe0A\x02"d\n\x1eDeleteRegionalInventoryRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,merchantapi.googleapis.com/RegionalInventory2\xbf\x06\n\x18RegionalInventoryService\x12\x81\x02\n\x17ListRegionalInventories\x12G.google.shopping.merchant.inventories.v1.ListRegionalInventoriesRequest\x1aH.google.shopping.merchant.inventories.v1.ListRegionalInventoriesResponse"S\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/inventories/v1/{parent=accounts/*/products/*}/regionalInventories\x12\x85\x02\n\x17InsertRegionalInventory\x12G.google.shopping.merchant.inventories.v1.InsertRegionalInventoryRequest\x1a:.google.shopping.merchant.inventories.v1.RegionalInventory"e\x82\xd3\xe4\x93\x02_"I/inventories/v1/{parent=accounts/*/products/*}/regionalInventories:insert:\x12regional_inventory\x12\xcd\x01\n\x17DeleteRegionalInventory\x12G.google.shopping.merchant.inventories.v1.DeleteRegionalInventoryRequest\x1a\x16.google.protobuf.Empty"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D*B/inventories/v1/{name=accounts/*/products/*/regionalInventories/*}\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x9e\x02\n+com.google.shopping.merchant.inventories.v1B\x16RegionalInventoryProtoP\x01ZScloud.google.com/go/shopping/merchant/inventories/apiv1/inventoriespb;inventoriespb\xaa\x02\'Google.Shopping.Merchant.Inventories.V1\xca\x02\'Google\\Shopping\\Merchant\\Inventories\\V1\xea\x02+Google::Shopping::Merchant::Inventories::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.inventories.v1.regionalinventory_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.shopping.merchant.inventories.v1B\x16RegionalInventoryProtoP\x01ZScloud.google.com/go/shopping/merchant/inventories/apiv1/inventoriespb;inventoriespb\xaa\x02'Google.Shopping.Merchant.Inventories.V1\xca\x02'Google\\Shopping\\Merchant\\Inventories\\V1\xea\x02+Google::Shopping::Merchant::Inventories::V1"
    _globals['_REGIONALINVENTORY'].fields_by_name['name']._loaded_options = None
    _globals['_REGIONALINVENTORY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_REGIONALINVENTORY'].fields_by_name['account']._loaded_options = None
    _globals['_REGIONALINVENTORY'].fields_by_name['account']._serialized_options = b'\xe0A\x03'
    _globals['_REGIONALINVENTORY'].fields_by_name['region']._loaded_options = None
    _globals['_REGIONALINVENTORY'].fields_by_name['region']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_REGIONALINVENTORY'].fields_by_name['regional_inventory_attributes']._loaded_options = None
    _globals['_REGIONALINVENTORY'].fields_by_name['regional_inventory_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_REGIONALINVENTORY']._loaded_options = None
    _globals['_REGIONALINVENTORY']._serialized_options = b'\xeaAr\n,merchantapi.googleapis.com/RegionalInventory\x12Baccounts/{account}/products/{product}/regionalInventories/{region}'
    _globals['_LISTREGIONALINVENTORIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREGIONALINVENTORIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,merchantapi.googleapis.com/RegionalInventory'
    _globals['_INSERTREGIONALINVENTORYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_INSERTREGIONALINVENTORYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,merchantapi.googleapis.com/RegionalInventory'
    _globals['_INSERTREGIONALINVENTORYREQUEST'].fields_by_name['regional_inventory']._loaded_options = None
    _globals['_INSERTREGIONALINVENTORYREQUEST'].fields_by_name['regional_inventory']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEREGIONALINVENTORYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEREGIONALINVENTORYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,merchantapi.googleapis.com/RegionalInventory'
    _globals['_REGIONALINVENTORYSERVICE']._loaded_options = None
    _globals['_REGIONALINVENTORYSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_REGIONALINVENTORYSERVICE'].methods_by_name['ListRegionalInventories']._loaded_options = None
    _globals['_REGIONALINVENTORYSERVICE'].methods_by_name['ListRegionalInventories']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/inventories/v1/{parent=accounts/*/products/*}/regionalInventories'
    _globals['_REGIONALINVENTORYSERVICE'].methods_by_name['InsertRegionalInventory']._loaded_options = None
    _globals['_REGIONALINVENTORYSERVICE'].methods_by_name['InsertRegionalInventory']._serialized_options = b'\x82\xd3\xe4\x93\x02_"I/inventories/v1/{parent=accounts/*/products/*}/regionalInventories:insert:\x12regional_inventory'
    _globals['_REGIONALINVENTORYSERVICE'].methods_by_name['DeleteRegionalInventory']._loaded_options = None
    _globals['_REGIONALINVENTORYSERVICE'].methods_by_name['DeleteRegionalInventory']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D*B/inventories/v1/{name=accounts/*/products/*/regionalInventories/*}'
    _globals['_REGIONALINVENTORY']._serialized_start = 319
    _globals['_REGIONALINVENTORY']._serialized_end = 636
    _globals['_LISTREGIONALINVENTORIESREQUEST']._serialized_start = 639
    _globals['_LISTREGIONALINVENTORIESREQUEST']._serialized_end = 780
    _globals['_LISTREGIONALINVENTORIESRESPONSE']._serialized_start = 783
    _globals['_LISTREGIONALINVENTORIESRESPONSE']._serialized_end = 931
    _globals['_INSERTREGIONALINVENTORYREQUEST']._serialized_start = 934
    _globals['_INSERTREGIONALINVENTORYREQUEST']._serialized_end = 1129
    _globals['_DELETEREGIONALINVENTORYREQUEST']._serialized_start = 1131
    _globals['_DELETEREGIONALINVENTORYREQUEST']._serialized_end = 1231
    _globals['_REGIONALINVENTORYSERVICE']._serialized_start = 1234
    _globals['_REGIONALINVENTORYSERVICE']._serialized_end = 2065