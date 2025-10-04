"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/lfp/v1beta/lfpinventory.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/shopping/merchant/lfp/v1beta/lfpinventory.proto\x12#google.shopping.merchant.lfp.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/shopping/type/types.proto"\xa2\x05\n\x0cLfpInventory\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12\x1b\n\x0etarget_account\x18\x02 \x01(\x03B\x03\xe0A\x02\x12\x17\n\nstore_code\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x18\n\x08offer_id\x18\x04 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12\x18\n\x0bregion_code\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10content_language\x18\x06 \x01(\tB\x03\xe0A\x02\x12\x16\n\x04gtin\x18\x07 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12/\n\x05price\x18\x08 \x01(\x0b2\x1b.google.shopping.type.PriceB\x03\xe0A\x01\x12\x19\n\x0cavailability\x18\t \x01(\tB\x03\xe0A\x02\x12\x1a\n\x08quantity\x18\n \x01(\x03B\x03\xe0A\x01H\x01\x88\x01\x01\x128\n\x0fcollection_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12\x1f\n\rpickup_method\x18\x0c \x01(\tB\x03\xe0A\x01H\x02\x88\x01\x01\x12\x1c\n\npickup_sla\x18\r \x01(\tB\x03\xe0A\x01H\x03\x88\x01\x01\x12\x1c\n\nfeed_label\x18\x0e \x01(\tB\x03\xe0A\x01H\x04\x88\x01\x01:\x95\x01\xeaA\x91\x01\n\'merchantapi.googleapis.com/LfpInventory\x12Haccounts/{account}/lfpInventories/{target_merchant}~{store_code}~{offer}*\x0elfpInventories2\x0clfpInventoryB\x07\n\x05_gtinB\x0b\n\t_quantityB\x10\n\x0e_pickup_methodB\r\n\x0b_pickup_slaB\r\n\x0b_feed_label"\xab\x01\n\x19InsertLfpInventoryRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'merchantapi.googleapis.com/LfpInventory\x12M\n\rlfp_inventory\x18\x02 \x01(\x0b21.google.shopping.merchant.lfp.v1beta.LfpInventoryB\x03\xe0A\x022\xb6\x02\n\x13LfpInventoryService\x12\xd5\x01\n\x12InsertLfpInventory\x12>.google.shopping.merchant.lfp.v1beta.InsertLfpInventoryRequest\x1a1.google.shopping.merchant.lfp.v1beta.LfpInventory"L\x82\xd3\xe4\x93\x02F"5/lfp/v1beta/{parent=accounts/*}/lfpInventories:insert:\rlfp_inventory\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xba\x01\n\'com.google.shopping.merchant.lfp.v1betaB\x11LfpInventoryProtoP\x01Z?cloud.google.com/go/shopping/merchant/lfp/apiv1beta/lfppb;lfppb\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.lfp.v1beta.lfpinventory_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\'com.google.shopping.merchant.lfp.v1betaB\x11LfpInventoryProtoP\x01Z?cloud.google.com/go/shopping/merchant/lfp/apiv1beta/lfppb;lfppb\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}'
    _globals['_LFPINVENTORY'].fields_by_name['name']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_LFPINVENTORY'].fields_by_name['target_account']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['target_account']._serialized_options = b'\xe0A\x02'
    _globals['_LFPINVENTORY'].fields_by_name['store_code']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['store_code']._serialized_options = b'\xe0A\x02'
    _globals['_LFPINVENTORY'].fields_by_name['offer_id']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['offer_id']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_LFPINVENTORY'].fields_by_name['region_code']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['region_code']._serialized_options = b'\xe0A\x02'
    _globals['_LFPINVENTORY'].fields_by_name['content_language']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['content_language']._serialized_options = b'\xe0A\x02'
    _globals['_LFPINVENTORY'].fields_by_name['gtin']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['gtin']._serialized_options = b'\xe0A\x01'
    _globals['_LFPINVENTORY'].fields_by_name['price']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['price']._serialized_options = b'\xe0A\x01'
    _globals['_LFPINVENTORY'].fields_by_name['availability']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['availability']._serialized_options = b'\xe0A\x02'
    _globals['_LFPINVENTORY'].fields_by_name['quantity']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['quantity']._serialized_options = b'\xe0A\x01'
    _globals['_LFPINVENTORY'].fields_by_name['collection_time']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['collection_time']._serialized_options = b'\xe0A\x01'
    _globals['_LFPINVENTORY'].fields_by_name['pickup_method']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['pickup_method']._serialized_options = b'\xe0A\x01'
    _globals['_LFPINVENTORY'].fields_by_name['pickup_sla']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['pickup_sla']._serialized_options = b'\xe0A\x01'
    _globals['_LFPINVENTORY'].fields_by_name['feed_label']._loaded_options = None
    _globals['_LFPINVENTORY'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x01'
    _globals['_LFPINVENTORY']._loaded_options = None
    _globals['_LFPINVENTORY']._serialized_options = b"\xeaA\x91\x01\n'merchantapi.googleapis.com/LfpInventory\x12Haccounts/{account}/lfpInventories/{target_merchant}~{store_code}~{offer}*\x0elfpInventories2\x0clfpInventory"
    _globals['_INSERTLFPINVENTORYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_INSERTLFPINVENTORYREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'merchantapi.googleapis.com/LfpInventory"
    _globals['_INSERTLFPINVENTORYREQUEST'].fields_by_name['lfp_inventory']._loaded_options = None
    _globals['_INSERTLFPINVENTORYREQUEST'].fields_by_name['lfp_inventory']._serialized_options = b'\xe0A\x02'
    _globals['_LFPINVENTORYSERVICE']._loaded_options = None
    _globals['_LFPINVENTORYSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_LFPINVENTORYSERVICE'].methods_by_name['InsertLfpInventory']._loaded_options = None
    _globals['_LFPINVENTORYSERVICE'].methods_by_name['InsertLfpInventory']._serialized_options = b'\x82\xd3\xe4\x93\x02F"5/lfp/v1beta/{parent=accounts/*}/lfpInventories:insert:\rlfp_inventory'
    _globals['_LFPINVENTORY']._serialized_start = 278
    _globals['_LFPINVENTORY']._serialized_end = 952
    _globals['_INSERTLFPINVENTORYREQUEST']._serialized_start = 955
    _globals['_INSERTLFPINVENTORYREQUEST']._serialized_end = 1126
    _globals['_LFPINVENTORYSERVICE']._serialized_start = 1129
    _globals['_LFPINVENTORYSERVICE']._serialized_end = 1439