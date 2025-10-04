"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/inventories/v1beta/localinventory.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
from ......google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/shopping/merchant/inventories/v1beta/localinventory.proto\x12+google.shopping.merchant.inventories.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/shopping/type/types.proto\x1a\x1agoogle/type/interval.proto"\x8d\x05\n\x0eLocalInventory\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07account\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x1a\n\nstore_code\x18\x03 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12*\n\x05price\x18\x04 \x01(\x0b2\x1b.google.shopping.type.Price\x12/\n\nsale_price\x18\x05 \x01(\x0b2\x1b.google.shopping.type.Price\x128\n\x19sale_price_effective_date\x18\x06 \x01(\x0b2\x15.google.type.Interval\x12\x19\n\x0cavailability\x18\x07 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08quantity\x18\x08 \x01(\x03H\x01\x88\x01\x01\x12\x1a\n\rpickup_method\x18\t \x01(\tH\x02\x88\x01\x01\x12\x17\n\npickup_sla\x18\n \x01(\tH\x03\x88\x01\x01\x12%\n\x18instore_product_location\x18\x0b \x01(\tH\x04\x88\x01\x01\x12@\n\x11custom_attributes\x18\x0c \x03(\x0b2%.google.shopping.type.CustomAttribute:s\xeaAp\n)merchantapi.googleapis.com/LocalInventory\x12Caccounts/{account}/products/{product}/localInventories/{store_code}B\x0f\n\r_availabilityB\x0b\n\t_quantityB\x10\n\x0e_pickup_methodB\r\n\x0b_pickup_slaB\x1b\n\x19_instore_product_location"\x87\x01\n\x1bListLocalInventoriesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)merchantapi.googleapis.com/LocalInventory\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x8f\x01\n\x1cListLocalInventoriesResponse\x12V\n\x11local_inventories\x18\x01 \x03(\x0b2;.google.shopping.merchant.inventories.v1beta.LocalInventory\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xbb\x01\n\x1bInsertLocalInventoryRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)merchantapi.googleapis.com/LocalInventory\x12Y\n\x0flocal_inventory\x18\x02 \x01(\x0b2;.google.shopping.merchant.inventories.v1beta.LocalInventoryB\x03\xe0A\x02"^\n\x1bDeleteLocalInventoryRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/LocalInventory2\xb8\x06\n\x15LocalInventoryService\x12\x81\x02\n\x14ListLocalInventories\x12H.google.shopping.merchant.inventories.v1beta.ListLocalInventoriesRequest\x1aI.google.shopping.merchant.inventories.v1beta.ListLocalInventoriesResponse"T\xdaA\x06parent\x82\xd3\xe4\x93\x02E\x12C/inventories/v1beta/{parent=accounts/*/products/*}/localInventories\x12\x82\x02\n\x14InsertLocalInventory\x12H.google.shopping.merchant.inventories.v1beta.InsertLocalInventoryRequest\x1a;.google.shopping.merchant.inventories.v1beta.LocalInventory"c\x82\xd3\xe4\x93\x02]"J/inventories/v1beta/{parent=accounts/*/products/*}/localInventories:insert:\x0flocal_inventory\x12\xcc\x01\n\x14DeleteLocalInventory\x12H.google.shopping.merchant.inventories.v1beta.DeleteLocalInventoryRequest\x1a\x16.google.protobuf.Empty"R\xdaA\x04name\x82\xd3\xe4\x93\x02E*C/inventories/v1beta/{name=accounts/*/products/*/localInventories/*}\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xef\x01\n/com.google.shopping.merchant.inventories.v1betaB\x13LocalInventoryProtoP\x01ZWcloud.google.com/go/shopping/merchant/inventories/apiv1beta/inventoriespb;inventoriespb\xeaAK\n"merchantapi.googleapis.com/Product\x12%accounts/{account}/products/{product}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.inventories.v1beta.localinventory_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.shopping.merchant.inventories.v1betaB\x13LocalInventoryProtoP\x01ZWcloud.google.com/go/shopping/merchant/inventories/apiv1beta/inventoriespb;inventoriespb\xeaAK\n"merchantapi.googleapis.com/Product\x12%accounts/{account}/products/{product}'
    _globals['_LOCALINVENTORY'].fields_by_name['name']._loaded_options = None
    _globals['_LOCALINVENTORY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALINVENTORY'].fields_by_name['account']._loaded_options = None
    _globals['_LOCALINVENTORY'].fields_by_name['account']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALINVENTORY'].fields_by_name['store_code']._loaded_options = None
    _globals['_LOCALINVENTORY'].fields_by_name['store_code']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_LOCALINVENTORY']._loaded_options = None
    _globals['_LOCALINVENTORY']._serialized_options = b'\xeaAp\n)merchantapi.googleapis.com/LocalInventory\x12Caccounts/{account}/products/{product}/localInventories/{store_code}'
    _globals['_LISTLOCALINVENTORIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTLOCALINVENTORIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)merchantapi.googleapis.com/LocalInventory'
    _globals['_INSERTLOCALINVENTORYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_INSERTLOCALINVENTORYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)merchantapi.googleapis.com/LocalInventory'
    _globals['_INSERTLOCALINVENTORYREQUEST'].fields_by_name['local_inventory']._loaded_options = None
    _globals['_INSERTLOCALINVENTORYREQUEST'].fields_by_name['local_inventory']._serialized_options = b'\xe0A\x02'
    _globals['_DELETELOCALINVENTORYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETELOCALINVENTORYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/LocalInventory'
    _globals['_LOCALINVENTORYSERVICE']._loaded_options = None
    _globals['_LOCALINVENTORYSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_LOCALINVENTORYSERVICE'].methods_by_name['ListLocalInventories']._loaded_options = None
    _globals['_LOCALINVENTORYSERVICE'].methods_by_name['ListLocalInventories']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02E\x12C/inventories/v1beta/{parent=accounts/*/products/*}/localInventories'
    _globals['_LOCALINVENTORYSERVICE'].methods_by_name['InsertLocalInventory']._loaded_options = None
    _globals['_LOCALINVENTORYSERVICE'].methods_by_name['InsertLocalInventory']._serialized_options = b'\x82\xd3\xe4\x93\x02]"J/inventories/v1beta/{parent=accounts/*/products/*}/localInventories:insert:\x0flocal_inventory'
    _globals['_LOCALINVENTORYSERVICE'].methods_by_name['DeleteLocalInventory']._loaded_options = None
    _globals['_LOCALINVENTORYSERVICE'].methods_by_name['DeleteLocalInventory']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E*C/inventories/v1beta/{name=accounts/*/products/*/localInventories/*}'
    _globals['_LOCALINVENTORY']._serialized_start = 320
    _globals['_LOCALINVENTORY']._serialized_end = 973
    _globals['_LISTLOCALINVENTORIESREQUEST']._serialized_start = 976
    _globals['_LISTLOCALINVENTORIESREQUEST']._serialized_end = 1111
    _globals['_LISTLOCALINVENTORIESRESPONSE']._serialized_start = 1114
    _globals['_LISTLOCALINVENTORIESRESPONSE']._serialized_end = 1257
    _globals['_INSERTLOCALINVENTORYREQUEST']._serialized_start = 1260
    _globals['_INSERTLOCALINVENTORYREQUEST']._serialized_end = 1447
    _globals['_DELETELOCALINVENTORYREQUEST']._serialized_start = 1449
    _globals['_DELETELOCALINVENTORYREQUEST']._serialized_end = 1543
    _globals['_LOCALINVENTORYSERVICE']._serialized_start = 1546
    _globals['_LOCALINVENTORYSERVICE']._serialized_end = 2370