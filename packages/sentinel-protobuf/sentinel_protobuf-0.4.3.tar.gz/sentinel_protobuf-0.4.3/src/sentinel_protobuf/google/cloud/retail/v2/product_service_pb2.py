"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2/product_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2 import common_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_common__pb2
from .....google.cloud.retail.v2 import import_config_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_import__config__pb2
from .....google.cloud.retail.v2 import product_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_product__pb2
from .....google.cloud.retail.v2 import purge_config_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_purge__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/retail/v2/product_service.proto\x12\x16google.cloud.retail.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/retail/v2/common.proto\x1a*google/cloud/retail/v2/import_config.proto\x1a$google/cloud/retail/v2/product.proto\x1a)google/cloud/retail/v2/purge_config.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9c\x01\n\x14CreateProductRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x125\n\x07product\x18\x02 \x01(\x0b2\x1f.google.cloud.retail.v2.ProductB\x03\xe0A\x02\x12\x17\n\nproduct_id\x18\x03 \x01(\tB\x03\xe0A\x02"H\n\x11GetProductRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product"\x95\x01\n\x14UpdateProductRequest\x125\n\x07product\x18\x01 \x01(\x0b2\x1f.google.cloud.retail.v2.ProductB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x15\n\rallow_missing\x18\x03 \x01(\x08"K\n\x14DeleteProductRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product"\xb1\x01\n\x13ListProductsRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"b\n\x14ListProductsResponse\x121\n\x08products\x18\x01 \x03(\x0b2\x1f.google.cloud.retail.v2.Product\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc1\x01\n\x13SetInventoryRequest\x127\n\tinventory\x18\x01 \x01(\x0b2\x1f.google.cloud.retail.v2.ProductB\x03\xe0A\x02\x12,\n\x08set_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12,\n\x08set_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x04 \x01(\x08"\x16\n\x14SetInventoryMetadata"\x16\n\x14SetInventoryResponse"\xc5\x01\n\x1bAddFulfillmentPlacesRequest\x126\n\x07product\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12\x11\n\x04type\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tplace_ids\x18\x03 \x03(\tB\x03\xe0A\x02\x12,\n\x08add_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x05 \x01(\x08"\x1e\n\x1cAddFulfillmentPlacesMetadata"\x1e\n\x1cAddFulfillmentPlacesResponse"\x8f\x02\n\x1aAddLocalInventoriesRequest\x126\n\x07product\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12F\n\x11local_inventories\x18\x02 \x03(\x0b2&.google.cloud.retail.v2.LocalInventoryB\x03\xe0A\x02\x12,\n\x08add_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12,\n\x08add_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x06 \x01(\x08"\x1d\n\x1bAddLocalInventoriesMetadata"\x1d\n\x1bAddLocalInventoriesResponse"\xb7\x01\n\x1dRemoveLocalInventoriesRequest\x126\n\x07product\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12\x16\n\tplace_ids\x18\x02 \x03(\tB\x03\xe0A\x02\x12/\n\x0bremove_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x03 \x01(\x08" \n\x1eRemoveLocalInventoriesMetadata" \n\x1eRemoveLocalInventoriesResponse"\xcb\x01\n\x1eRemoveFulfillmentPlacesRequest\x126\n\x07product\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12\x11\n\x04type\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tplace_ids\x18\x03 \x03(\tB\x03\xe0A\x02\x12/\n\x0bremove_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x05 \x01(\x08"!\n\x1fRemoveFulfillmentPlacesMetadata"!\n\x1fRemoveFulfillmentPlacesResponse2\xc2\x19\n\x0eProductService\x12\xcf\x01\n\rCreateProduct\x12,.google.cloud.retail.v2.CreateProductRequest\x1a\x1f.google.cloud.retail.v2.Product"o\xdaA\x19parent,product,product_id\x82\xd3\xe4\x93\x02M"B/v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:\x07product\x12\xac\x01\n\nGetProduct\x12).google.cloud.retail.v2.GetProductRequest\x1a\x1f.google.cloud.retail.v2.Product"R\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/v2/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}\x12\xbe\x01\n\x0cListProducts\x12+.google.cloud.retail.v2.ListProductsRequest\x1a,.google.cloud.retail.v2.ListProductsResponse"S\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products\x12\xd2\x01\n\rUpdateProduct\x12,.google.cloud.retail.v2.UpdateProductRequest\x1a\x1f.google.cloud.retail.v2.Product"r\xdaA\x13product,update_mask\x82\xd3\xe4\x93\x02V2K/v2/{product.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:\x07product\x12\xa9\x01\n\rDeleteProduct\x12,.google.cloud.retail.v2.DeleteProductRequest\x1a\x16.google.protobuf.Empty"R\xdaA\x04name\x82\xd3\xe4\x93\x02E*C/v2/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}\x12\x91\x02\n\rPurgeProducts\x12,.google.cloud.retail.v2.PurgeProductsRequest\x1a\x1d.google.longrunning.Operation"\xb2\x01\xcaA\\\n,google.cloud.retail.v2.PurgeProductsResponse\x12,google.cloud.retail.v2.PurgeProductsMetadata\x82\xd3\xe4\x93\x02M"H/v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:purge:\x01*\x12\x8e\x02\n\x0eImportProducts\x12-.google.cloud.retail.v2.ImportProductsRequest\x1a\x1d.google.longrunning.Operation"\xad\x01\xcaAV\n-google.cloud.retail.v2.ImportProductsResponse\x12%google.cloud.retail.v2.ImportMetadata\x82\xd3\xe4\x93\x02N"I/v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:import:\x01*\x12\xb4\x02\n\x0cSetInventory\x12+.google.cloud.retail.v2.SetInventoryRequest\x1a\x1d.google.longrunning.Operation"\xd7\x01\xcaAZ\n+google.cloud.retail.v2.SetInventoryResponse\x12+google.cloud.retail.v2.SetInventoryMetadata\xdaA\x12inventory,set_mask\x82\xd3\xe4\x93\x02_"Z/v2/{inventory.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:setInventory:\x01*\x12\xca\x02\n\x14AddFulfillmentPlaces\x123.google.cloud.retail.v2.AddFulfillmentPlacesRequest\x1a\x1d.google.longrunning.Operation"\xdd\x01\xcaAj\n3google.cloud.retail.v2.AddFulfillmentPlacesResponse\x123google.cloud.retail.v2.AddFulfillmentPlacesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02`"[/v2/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addFulfillmentPlaces:\x01*\x12\xd9\x02\n\x17RemoveFulfillmentPlaces\x126.google.cloud.retail.v2.RemoveFulfillmentPlacesRequest\x1a\x1d.google.longrunning.Operation"\xe6\x01\xcaAp\n6google.cloud.retail.v2.RemoveFulfillmentPlacesResponse\x126google.cloud.retail.v2.RemoveFulfillmentPlacesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02c"^/v2/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeFulfillmentPlaces:\x01*\x12\xc5\x02\n\x13AddLocalInventories\x122.google.cloud.retail.v2.AddLocalInventoriesRequest\x1a\x1d.google.longrunning.Operation"\xda\x01\xcaAh\n2google.cloud.retail.v2.AddLocalInventoriesResponse\x122google.cloud.retail.v2.AddLocalInventoriesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02_"Z/v2/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addLocalInventories:\x01*\x12\xd4\x02\n\x16RemoveLocalInventories\x125.google.cloud.retail.v2.RemoveLocalInventoriesRequest\x1a\x1d.google.longrunning.Operation"\xe3\x01\xcaAn\n5google.cloud.retail.v2.RemoveLocalInventoriesResponse\x125google.cloud.retail.v2.RemoveLocalInventoriesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02b"]/v2/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeLocalInventories:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xbe\x01\n\x1acom.google.cloud.retail.v2B\x13ProductServiceProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2.product_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.retail.v2B\x13ProductServiceProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2'
    _globals['_CREATEPRODUCTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPRODUCTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch'
    _globals['_CREATEPRODUCTREQUEST'].fields_by_name['product']._loaded_options = None
    _globals['_CREATEPRODUCTREQUEST'].fields_by_name['product']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPRODUCTREQUEST'].fields_by_name['product_id']._loaded_options = None
    _globals['_CREATEPRODUCTREQUEST'].fields_by_name['product_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETPRODUCTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPRODUCTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product'
    _globals['_UPDATEPRODUCTREQUEST'].fields_by_name['product']._loaded_options = None
    _globals['_UPDATEPRODUCTREQUEST'].fields_by_name['product']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPRODUCTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPRODUCTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product'
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch'
    _globals['_SETINVENTORYREQUEST'].fields_by_name['inventory']._loaded_options = None
    _globals['_SETINVENTORYREQUEST'].fields_by_name['inventory']._serialized_options = b'\xe0A\x02'
    _globals['_ADDFULFILLMENTPLACESREQUEST'].fields_by_name['product']._loaded_options = None
    _globals['_ADDFULFILLMENTPLACESREQUEST'].fields_by_name['product']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product'
    _globals['_ADDFULFILLMENTPLACESREQUEST'].fields_by_name['type']._loaded_options = None
    _globals['_ADDFULFILLMENTPLACESREQUEST'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_ADDFULFILLMENTPLACESREQUEST'].fields_by_name['place_ids']._loaded_options = None
    _globals['_ADDFULFILLMENTPLACESREQUEST'].fields_by_name['place_ids']._serialized_options = b'\xe0A\x02'
    _globals['_ADDLOCALINVENTORIESREQUEST'].fields_by_name['product']._loaded_options = None
    _globals['_ADDLOCALINVENTORIESREQUEST'].fields_by_name['product']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product'
    _globals['_ADDLOCALINVENTORIESREQUEST'].fields_by_name['local_inventories']._loaded_options = None
    _globals['_ADDLOCALINVENTORIESREQUEST'].fields_by_name['local_inventories']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVELOCALINVENTORIESREQUEST'].fields_by_name['product']._loaded_options = None
    _globals['_REMOVELOCALINVENTORIESREQUEST'].fields_by_name['product']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product'
    _globals['_REMOVELOCALINVENTORIESREQUEST'].fields_by_name['place_ids']._loaded_options = None
    _globals['_REMOVELOCALINVENTORIESREQUEST'].fields_by_name['place_ids']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEFULFILLMENTPLACESREQUEST'].fields_by_name['product']._loaded_options = None
    _globals['_REMOVEFULFILLMENTPLACESREQUEST'].fields_by_name['product']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product'
    _globals['_REMOVEFULFILLMENTPLACESREQUEST'].fields_by_name['type']._loaded_options = None
    _globals['_REMOVEFULFILLMENTPLACESREQUEST'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEFULFILLMENTPLACESREQUEST'].fields_by_name['place_ids']._loaded_options = None
    _globals['_REMOVEFULFILLMENTPLACESREQUEST'].fields_by_name['place_ids']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTSERVICE']._loaded_options = None
    _globals['_PRODUCTSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PRODUCTSERVICE'].methods_by_name['CreateProduct']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['CreateProduct']._serialized_options = b'\xdaA\x19parent,product,product_id\x82\xd3\xe4\x93\x02M"B/v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:\x07product'
    _globals['_PRODUCTSERVICE'].methods_by_name['GetProduct']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['GetProduct']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/v2/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}'
    _globals['_PRODUCTSERVICE'].methods_by_name['ListProducts']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['ListProducts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products'
    _globals['_PRODUCTSERVICE'].methods_by_name['UpdateProduct']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['UpdateProduct']._serialized_options = b'\xdaA\x13product,update_mask\x82\xd3\xe4\x93\x02V2K/v2/{product.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:\x07product'
    _globals['_PRODUCTSERVICE'].methods_by_name['DeleteProduct']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['DeleteProduct']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E*C/v2/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}'
    _globals['_PRODUCTSERVICE'].methods_by_name['PurgeProducts']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['PurgeProducts']._serialized_options = b'\xcaA\\\n,google.cloud.retail.v2.PurgeProductsResponse\x12,google.cloud.retail.v2.PurgeProductsMetadata\x82\xd3\xe4\x93\x02M"H/v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:purge:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['ImportProducts']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['ImportProducts']._serialized_options = b'\xcaAV\n-google.cloud.retail.v2.ImportProductsResponse\x12%google.cloud.retail.v2.ImportMetadata\x82\xd3\xe4\x93\x02N"I/v2/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:import:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['SetInventory']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['SetInventory']._serialized_options = b'\xcaAZ\n+google.cloud.retail.v2.SetInventoryResponse\x12+google.cloud.retail.v2.SetInventoryMetadata\xdaA\x12inventory,set_mask\x82\xd3\xe4\x93\x02_"Z/v2/{inventory.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:setInventory:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['AddFulfillmentPlaces']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['AddFulfillmentPlaces']._serialized_options = b'\xcaAj\n3google.cloud.retail.v2.AddFulfillmentPlacesResponse\x123google.cloud.retail.v2.AddFulfillmentPlacesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02`"[/v2/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addFulfillmentPlaces:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['RemoveFulfillmentPlaces']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['RemoveFulfillmentPlaces']._serialized_options = b'\xcaAp\n6google.cloud.retail.v2.RemoveFulfillmentPlacesResponse\x126google.cloud.retail.v2.RemoveFulfillmentPlacesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02c"^/v2/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeFulfillmentPlaces:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['AddLocalInventories']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['AddLocalInventories']._serialized_options = b'\xcaAh\n2google.cloud.retail.v2.AddLocalInventoriesResponse\x122google.cloud.retail.v2.AddLocalInventoriesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02_"Z/v2/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addLocalInventories:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['RemoveLocalInventories']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['RemoveLocalInventories']._serialized_options = b'\xcaAn\n5google.cloud.retail.v2.RemoveLocalInventoriesResponse\x125google.cloud.retail.v2.RemoveLocalInventoriesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02b"]/v2/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeLocalInventories:\x01*'
    _globals['_CREATEPRODUCTREQUEST']._serialized_start = 483
    _globals['_CREATEPRODUCTREQUEST']._serialized_end = 639
    _globals['_GETPRODUCTREQUEST']._serialized_start = 641
    _globals['_GETPRODUCTREQUEST']._serialized_end = 713
    _globals['_UPDATEPRODUCTREQUEST']._serialized_start = 716
    _globals['_UPDATEPRODUCTREQUEST']._serialized_end = 865
    _globals['_DELETEPRODUCTREQUEST']._serialized_start = 867
    _globals['_DELETEPRODUCTREQUEST']._serialized_end = 942
    _globals['_LISTPRODUCTSREQUEST']._serialized_start = 945
    _globals['_LISTPRODUCTSREQUEST']._serialized_end = 1122
    _globals['_LISTPRODUCTSRESPONSE']._serialized_start = 1124
    _globals['_LISTPRODUCTSRESPONSE']._serialized_end = 1222
    _globals['_SETINVENTORYREQUEST']._serialized_start = 1225
    _globals['_SETINVENTORYREQUEST']._serialized_end = 1418
    _globals['_SETINVENTORYMETADATA']._serialized_start = 1420
    _globals['_SETINVENTORYMETADATA']._serialized_end = 1442
    _globals['_SETINVENTORYRESPONSE']._serialized_start = 1444
    _globals['_SETINVENTORYRESPONSE']._serialized_end = 1466
    _globals['_ADDFULFILLMENTPLACESREQUEST']._serialized_start = 1469
    _globals['_ADDFULFILLMENTPLACESREQUEST']._serialized_end = 1666
    _globals['_ADDFULFILLMENTPLACESMETADATA']._serialized_start = 1668
    _globals['_ADDFULFILLMENTPLACESMETADATA']._serialized_end = 1698
    _globals['_ADDFULFILLMENTPLACESRESPONSE']._serialized_start = 1700
    _globals['_ADDFULFILLMENTPLACESRESPONSE']._serialized_end = 1730
    _globals['_ADDLOCALINVENTORIESREQUEST']._serialized_start = 1733
    _globals['_ADDLOCALINVENTORIESREQUEST']._serialized_end = 2004
    _globals['_ADDLOCALINVENTORIESMETADATA']._serialized_start = 2006
    _globals['_ADDLOCALINVENTORIESMETADATA']._serialized_end = 2035
    _globals['_ADDLOCALINVENTORIESRESPONSE']._serialized_start = 2037
    _globals['_ADDLOCALINVENTORIESRESPONSE']._serialized_end = 2066
    _globals['_REMOVELOCALINVENTORIESREQUEST']._serialized_start = 2069
    _globals['_REMOVELOCALINVENTORIESREQUEST']._serialized_end = 2252
    _globals['_REMOVELOCALINVENTORIESMETADATA']._serialized_start = 2254
    _globals['_REMOVELOCALINVENTORIESMETADATA']._serialized_end = 2286
    _globals['_REMOVELOCALINVENTORIESRESPONSE']._serialized_start = 2288
    _globals['_REMOVELOCALINVENTORIESRESPONSE']._serialized_end = 2320
    _globals['_REMOVEFULFILLMENTPLACESREQUEST']._serialized_start = 2323
    _globals['_REMOVEFULFILLMENTPLACESREQUEST']._serialized_end = 2526
    _globals['_REMOVEFULFILLMENTPLACESMETADATA']._serialized_start = 2528
    _globals['_REMOVEFULFILLMENTPLACESMETADATA']._serialized_end = 2561
    _globals['_REMOVEFULFILLMENTPLACESRESPONSE']._serialized_start = 2563
    _globals['_REMOVEFULFILLMENTPLACESRESPONSE']._serialized_end = 2596
    _globals['_PRODUCTSERVICE']._serialized_start = 2599
    _globals['_PRODUCTSERVICE']._serialized_end = 5865