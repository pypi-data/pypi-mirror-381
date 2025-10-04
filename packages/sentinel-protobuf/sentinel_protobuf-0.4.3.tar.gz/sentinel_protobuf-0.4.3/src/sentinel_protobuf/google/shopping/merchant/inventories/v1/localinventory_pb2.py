"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/inventories/v1/localinventory.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ......google.shopping.merchant.inventories.v1 import inventories_common_pb2 as google_dot_shopping_dot_merchant_dot_inventories_dot_v1_dot_inventories__common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/shopping/merchant/inventories/v1/localinventory.proto\x12\'google.shopping.merchant.inventories.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a@google/shopping/merchant/inventories/v1/inventories_common.proto"\xb6\x02\n\x0eLocalInventory\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07account\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x1a\n\nstore_code\x18\x03 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12j\n\x1alocal_inventory_attributes\x18\x0e \x01(\x0b2A.google.shopping.merchant.inventories.v1.LocalInventoryAttributesB\x03\xe0A\x01:s\xeaAp\n)merchantapi.googleapis.com/LocalInventory\x12Caccounts/{account}/products/{product}/localInventories/{store_code}"\x87\x01\n\x1bListLocalInventoriesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)merchantapi.googleapis.com/LocalInventory\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x8b\x01\n\x1cListLocalInventoriesResponse\x12R\n\x11local_inventories\x18\x01 \x03(\x0b27.google.shopping.merchant.inventories.v1.LocalInventory\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb7\x01\n\x1bInsertLocalInventoryRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)merchantapi.googleapis.com/LocalInventory\x12U\n\x0flocal_inventory\x18\x02 \x01(\x0b27.google.shopping.merchant.inventories.v1.LocalInventoryB\x03\xe0A\x02"^\n\x1bDeleteLocalInventoryRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/LocalInventory2\x98\x06\n\x15LocalInventoryService\x12\xf5\x01\n\x14ListLocalInventories\x12D.google.shopping.merchant.inventories.v1.ListLocalInventoriesRequest\x1aE.google.shopping.merchant.inventories.v1.ListLocalInventoriesResponse"P\xdaA\x06parent\x82\xd3\xe4\x93\x02A\x12?/inventories/v1/{parent=accounts/*/products/*}/localInventories\x12\xf6\x01\n\x14InsertLocalInventory\x12D.google.shopping.merchant.inventories.v1.InsertLocalInventoryRequest\x1a7.google.shopping.merchant.inventories.v1.LocalInventory"_\x82\xd3\xe4\x93\x02Y"F/inventories/v1/{parent=accounts/*/products/*}/localInventories:insert:\x0flocal_inventory\x12\xc4\x01\n\x14DeleteLocalInventory\x12D.google.shopping.merchant.inventories.v1.DeleteLocalInventoryRequest\x1a\x16.google.protobuf.Empty"N\xdaA\x04name\x82\xd3\xe4\x93\x02A*?/inventories/v1/{name=accounts/*/products/*/localInventories/*}\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xe9\x02\n+com.google.shopping.merchant.inventories.v1B\x13LocalInventoryProtoP\x01ZScloud.google.com/go/shopping/merchant/inventories/apiv1/inventoriespb;inventoriespb\xaa\x02\'Google.Shopping.Merchant.Inventories.V1\xca\x02\'Google\\Shopping\\Merchant\\Inventories\\V1\xea\x02+Google::Shopping::Merchant::Inventories::V1\xeaAK\n"merchantapi.googleapis.com/Product\x12%accounts/{account}/products/{product}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.inventories.v1.localinventory_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n+com.google.shopping.merchant.inventories.v1B\x13LocalInventoryProtoP\x01ZScloud.google.com/go/shopping/merchant/inventories/apiv1/inventoriespb;inventoriespb\xaa\x02\'Google.Shopping.Merchant.Inventories.V1\xca\x02\'Google\\Shopping\\Merchant\\Inventories\\V1\xea\x02+Google::Shopping::Merchant::Inventories::V1\xeaAK\n"merchantapi.googleapis.com/Product\x12%accounts/{account}/products/{product}'
    _globals['_LOCALINVENTORY'].fields_by_name['name']._loaded_options = None
    _globals['_LOCALINVENTORY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALINVENTORY'].fields_by_name['account']._loaded_options = None
    _globals['_LOCALINVENTORY'].fields_by_name['account']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALINVENTORY'].fields_by_name['store_code']._loaded_options = None
    _globals['_LOCALINVENTORY'].fields_by_name['store_code']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_LOCALINVENTORY'].fields_by_name['local_inventory_attributes']._loaded_options = None
    _globals['_LOCALINVENTORY'].fields_by_name['local_inventory_attributes']._serialized_options = b'\xe0A\x01'
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
    _globals['_LOCALINVENTORYSERVICE'].methods_by_name['ListLocalInventories']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02A\x12?/inventories/v1/{parent=accounts/*/products/*}/localInventories'
    _globals['_LOCALINVENTORYSERVICE'].methods_by_name['InsertLocalInventory']._loaded_options = None
    _globals['_LOCALINVENTORYSERVICE'].methods_by_name['InsertLocalInventory']._serialized_options = b'\x82\xd3\xe4\x93\x02Y"F/inventories/v1/{parent=accounts/*/products/*}/localInventories:insert:\x0flocal_inventory'
    _globals['_LOCALINVENTORYSERVICE'].methods_by_name['DeleteLocalInventory']._loaded_options = None
    _globals['_LOCALINVENTORYSERVICE'].methods_by_name['DeleteLocalInventory']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A*?/inventories/v1/{name=accounts/*/products/*/localInventories/*}'
    _globals['_LOCALINVENTORY']._serialized_start = 316
    _globals['_LOCALINVENTORY']._serialized_end = 626
    _globals['_LISTLOCALINVENTORIESREQUEST']._serialized_start = 629
    _globals['_LISTLOCALINVENTORIESREQUEST']._serialized_end = 764
    _globals['_LISTLOCALINVENTORIESRESPONSE']._serialized_start = 767
    _globals['_LISTLOCALINVENTORIESRESPONSE']._serialized_end = 906
    _globals['_INSERTLOCALINVENTORYREQUEST']._serialized_start = 909
    _globals['_INSERTLOCALINVENTORYREQUEST']._serialized_end = 1092
    _globals['_DELETELOCALINVENTORYREQUEST']._serialized_start = 1094
    _globals['_DELETELOCALINVENTORYREQUEST']._serialized_end = 1188
    _globals['_LOCALINVENTORYSERVICE']._serialized_start = 1191
    _globals['_LOCALINVENTORYSERVICE']._serialized_end = 1983