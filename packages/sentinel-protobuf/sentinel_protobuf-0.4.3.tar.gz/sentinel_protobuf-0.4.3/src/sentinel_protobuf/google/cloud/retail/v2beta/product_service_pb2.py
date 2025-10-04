"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2beta/product_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2beta import common_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_common__pb2
from .....google.cloud.retail.v2beta import export_config_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_export__config__pb2
from .....google.cloud.retail.v2beta import import_config_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_import__config__pb2
from .....google.cloud.retail.v2beta import product_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_product__pb2
from .....google.cloud.retail.v2beta import purge_config_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_purge__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/retail/v2beta/product_service.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/retail/v2beta/common.proto\x1a.google/cloud/retail/v2beta/export_config.proto\x1a.google/cloud/retail/v2beta/import_config.proto\x1a(google/cloud/retail/v2beta/product.proto\x1a-google/cloud/retail/v2beta/purge_config.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa0\x01\n\x14CreateProductRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x129\n\x07product\x18\x02 \x01(\x0b2#.google.cloud.retail.v2beta.ProductB\x03\xe0A\x02\x12\x17\n\nproduct_id\x18\x03 \x01(\tB\x03\xe0A\x02"H\n\x11GetProductRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product"\x99\x01\n\x14UpdateProductRequest\x129\n\x07product\x18\x01 \x01(\x0b2#.google.cloud.retail.v2beta.ProductB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x15\n\rallow_missing\x18\x03 \x01(\x08"K\n\x14DeleteProductRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product"\xb1\x01\n\x13ListProductsRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"f\n\x14ListProductsResponse\x125\n\x08products\x18\x01 \x03(\x0b2#.google.cloud.retail.v2beta.Product\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc5\x01\n\x13SetInventoryRequest\x12;\n\tinventory\x18\x01 \x01(\x0b2#.google.cloud.retail.v2beta.ProductB\x03\xe0A\x02\x12,\n\x08set_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12,\n\x08set_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x04 \x01(\x08"\x16\n\x14SetInventoryMetadata"\x16\n\x14SetInventoryResponse"\xc5\x01\n\x1bAddFulfillmentPlacesRequest\x126\n\x07product\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12\x11\n\x04type\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tplace_ids\x18\x03 \x03(\tB\x03\xe0A\x02\x12,\n\x08add_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x05 \x01(\x08"\x1e\n\x1cAddFulfillmentPlacesMetadata"\x1e\n\x1cAddFulfillmentPlacesResponse"\x93\x02\n\x1aAddLocalInventoriesRequest\x126\n\x07product\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12J\n\x11local_inventories\x18\x02 \x03(\x0b2*.google.cloud.retail.v2beta.LocalInventoryB\x03\xe0A\x02\x12,\n\x08add_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12,\n\x08add_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x06 \x01(\x08"\x1d\n\x1bAddLocalInventoriesMetadata"\x1d\n\x1bAddLocalInventoriesResponse"\xb7\x01\n\x1dRemoveLocalInventoriesRequest\x126\n\x07product\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12\x16\n\tplace_ids\x18\x02 \x03(\tB\x03\xe0A\x02\x12/\n\x0bremove_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x03 \x01(\x08" \n\x1eRemoveLocalInventoriesMetadata" \n\x1eRemoveLocalInventoriesResponse"\xcb\x01\n\x1eRemoveFulfillmentPlacesRequest\x126\n\x07product\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12\x11\n\x04type\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tplace_ids\x18\x03 \x03(\tB\x03\xe0A\x02\x12/\n\x0bremove_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x05 \x01(\x08"!\n\x1fRemoveFulfillmentPlacesMetadata"!\n\x1fRemoveFulfillmentPlacesResponse2\x8b\x1d\n\x0eProductService\x12\xdb\x01\n\rCreateProduct\x120.google.cloud.retail.v2beta.CreateProductRequest\x1a#.google.cloud.retail.v2beta.Product"s\xdaA\x19parent,product,product_id\x82\xd3\xe4\x93\x02Q"F/v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:\x07product\x12\xb8\x01\n\nGetProduct\x12-.google.cloud.retail.v2beta.GetProductRequest\x1a#.google.cloud.retail.v2beta.Product"V\xdaA\x04name\x82\xd3\xe4\x93\x02I\x12G/v2beta/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}\x12\xca\x01\n\x0cListProducts\x12/.google.cloud.retail.v2beta.ListProductsRequest\x1a0.google.cloud.retail.v2beta.ListProductsResponse"W\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products\x12\xde\x01\n\rUpdateProduct\x120.google.cloud.retail.v2beta.UpdateProductRequest\x1a#.google.cloud.retail.v2beta.Product"v\xdaA\x13product,update_mask\x82\xd3\xe4\x93\x02Z2O/v2beta/{product.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:\x07product\x12\xb1\x01\n\rDeleteProduct\x120.google.cloud.retail.v2beta.DeleteProductRequest\x1a\x16.google.protobuf.Empty"V\xdaA\x04name\x82\xd3\xe4\x93\x02I*G/v2beta/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}\x12\xa1\x02\n\rPurgeProducts\x120.google.cloud.retail.v2beta.PurgeProductsRequest\x1a\x1d.google.longrunning.Operation"\xbe\x01\xcaAd\n0google.cloud.retail.v2beta.PurgeProductsResponse\x120google.cloud.retail.v2beta.PurgeProductsMetadata\x82\xd3\xe4\x93\x02Q"L/v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:purge:\x01*\x12\x9e\x02\n\x0eImportProducts\x121.google.cloud.retail.v2beta.ImportProductsRequest\x1a\x1d.google.longrunning.Operation"\xb9\x01\xcaA^\n1google.cloud.retail.v2beta.ImportProductsResponse\x12)google.cloud.retail.v2beta.ImportMetadata\x82\xd3\xe4\x93\x02R"M/v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:import:\x01*\x12\x9e\x02\n\x0eExportProducts\x121.google.cloud.retail.v2beta.ExportProductsRequest\x1a\x1d.google.longrunning.Operation"\xb9\x01\xcaA^\n1google.cloud.retail.v2beta.ExportProductsResponse\x12)google.cloud.retail.v2beta.ExportMetadata\x82\xd3\xe4\x93\x02R"M/v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:export:\x01*\x12\xc4\x02\n\x0cSetInventory\x12/.google.cloud.retail.v2beta.SetInventoryRequest\x1a\x1d.google.longrunning.Operation"\xe3\x01\xcaAb\n/google.cloud.retail.v2beta.SetInventoryResponse\x12/google.cloud.retail.v2beta.SetInventoryMetadata\xdaA\x12inventory,set_mask\x82\xd3\xe4\x93\x02c"^/v2beta/{inventory.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:setInventory:\x01*\x12\xda\x02\n\x14AddFulfillmentPlaces\x127.google.cloud.retail.v2beta.AddFulfillmentPlacesRequest\x1a\x1d.google.longrunning.Operation"\xe9\x01\xcaAr\n7google.cloud.retail.v2beta.AddFulfillmentPlacesResponse\x127google.cloud.retail.v2beta.AddFulfillmentPlacesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02d"_/v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addFulfillmentPlaces:\x01*\x12\xe9\x02\n\x17RemoveFulfillmentPlaces\x12:.google.cloud.retail.v2beta.RemoveFulfillmentPlacesRequest\x1a\x1d.google.longrunning.Operation"\xf2\x01\xcaAx\n:google.cloud.retail.v2beta.RemoveFulfillmentPlacesResponse\x12:google.cloud.retail.v2beta.RemoveFulfillmentPlacesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02g"b/v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeFulfillmentPlaces:\x01*\x12\xd5\x02\n\x13AddLocalInventories\x126.google.cloud.retail.v2beta.AddLocalInventoriesRequest\x1a\x1d.google.longrunning.Operation"\xe6\x01\xcaAp\n6google.cloud.retail.v2beta.AddLocalInventoriesResponse\x126google.cloud.retail.v2beta.AddLocalInventoriesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02c"^/v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addLocalInventories:\x01*\x12\xe4\x02\n\x16RemoveLocalInventories\x129.google.cloud.retail.v2beta.RemoveLocalInventoriesRequest\x1a\x1d.google.longrunning.Operation"\xef\x01\xcaAv\n9google.cloud.retail.v2beta.RemoveLocalInventoriesResponse\x129google.cloud.retail.v2beta.RemoveLocalInventoriesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02f"a/v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeLocalInventories:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd2\x01\n\x1ecom.google.cloud.retail.v2betaB\x13ProductServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.product_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x13ProductServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
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
    _globals['_PRODUCTSERVICE'].methods_by_name['CreateProduct']._serialized_options = b'\xdaA\x19parent,product,product_id\x82\xd3\xe4\x93\x02Q"F/v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:\x07product'
    _globals['_PRODUCTSERVICE'].methods_by_name['GetProduct']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['GetProduct']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02I\x12G/v2beta/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}'
    _globals['_PRODUCTSERVICE'].methods_by_name['ListProducts']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['ListProducts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products'
    _globals['_PRODUCTSERVICE'].methods_by_name['UpdateProduct']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['UpdateProduct']._serialized_options = b'\xdaA\x13product,update_mask\x82\xd3\xe4\x93\x02Z2O/v2beta/{product.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:\x07product'
    _globals['_PRODUCTSERVICE'].methods_by_name['DeleteProduct']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['DeleteProduct']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02I*G/v2beta/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}'
    _globals['_PRODUCTSERVICE'].methods_by_name['PurgeProducts']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['PurgeProducts']._serialized_options = b'\xcaAd\n0google.cloud.retail.v2beta.PurgeProductsResponse\x120google.cloud.retail.v2beta.PurgeProductsMetadata\x82\xd3\xe4\x93\x02Q"L/v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:purge:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['ImportProducts']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['ImportProducts']._serialized_options = b'\xcaA^\n1google.cloud.retail.v2beta.ImportProductsResponse\x12)google.cloud.retail.v2beta.ImportMetadata\x82\xd3\xe4\x93\x02R"M/v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:import:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['ExportProducts']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['ExportProducts']._serialized_options = b'\xcaA^\n1google.cloud.retail.v2beta.ExportProductsResponse\x12)google.cloud.retail.v2beta.ExportMetadata\x82\xd3\xe4\x93\x02R"M/v2beta/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:export:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['SetInventory']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['SetInventory']._serialized_options = b'\xcaAb\n/google.cloud.retail.v2beta.SetInventoryResponse\x12/google.cloud.retail.v2beta.SetInventoryMetadata\xdaA\x12inventory,set_mask\x82\xd3\xe4\x93\x02c"^/v2beta/{inventory.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:setInventory:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['AddFulfillmentPlaces']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['AddFulfillmentPlaces']._serialized_options = b'\xcaAr\n7google.cloud.retail.v2beta.AddFulfillmentPlacesResponse\x127google.cloud.retail.v2beta.AddFulfillmentPlacesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02d"_/v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addFulfillmentPlaces:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['RemoveFulfillmentPlaces']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['RemoveFulfillmentPlaces']._serialized_options = b'\xcaAx\n:google.cloud.retail.v2beta.RemoveFulfillmentPlacesResponse\x12:google.cloud.retail.v2beta.RemoveFulfillmentPlacesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02g"b/v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeFulfillmentPlaces:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['AddLocalInventories']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['AddLocalInventories']._serialized_options = b'\xcaAp\n6google.cloud.retail.v2beta.AddLocalInventoriesResponse\x126google.cloud.retail.v2beta.AddLocalInventoriesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02c"^/v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addLocalInventories:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['RemoveLocalInventories']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['RemoveLocalInventories']._serialized_options = b'\xcaAv\n9google.cloud.retail.v2beta.RemoveLocalInventoriesResponse\x129google.cloud.retail.v2beta.RemoveLocalInventoriesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02f"a/v2beta/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeLocalInventories:\x01*'
    _globals['_CREATEPRODUCTREQUEST']._serialized_start = 555
    _globals['_CREATEPRODUCTREQUEST']._serialized_end = 715
    _globals['_GETPRODUCTREQUEST']._serialized_start = 717
    _globals['_GETPRODUCTREQUEST']._serialized_end = 789
    _globals['_UPDATEPRODUCTREQUEST']._serialized_start = 792
    _globals['_UPDATEPRODUCTREQUEST']._serialized_end = 945
    _globals['_DELETEPRODUCTREQUEST']._serialized_start = 947
    _globals['_DELETEPRODUCTREQUEST']._serialized_end = 1022
    _globals['_LISTPRODUCTSREQUEST']._serialized_start = 1025
    _globals['_LISTPRODUCTSREQUEST']._serialized_end = 1202
    _globals['_LISTPRODUCTSRESPONSE']._serialized_start = 1204
    _globals['_LISTPRODUCTSRESPONSE']._serialized_end = 1306
    _globals['_SETINVENTORYREQUEST']._serialized_start = 1309
    _globals['_SETINVENTORYREQUEST']._serialized_end = 1506
    _globals['_SETINVENTORYMETADATA']._serialized_start = 1508
    _globals['_SETINVENTORYMETADATA']._serialized_end = 1530
    _globals['_SETINVENTORYRESPONSE']._serialized_start = 1532
    _globals['_SETINVENTORYRESPONSE']._serialized_end = 1554
    _globals['_ADDFULFILLMENTPLACESREQUEST']._serialized_start = 1557
    _globals['_ADDFULFILLMENTPLACESREQUEST']._serialized_end = 1754
    _globals['_ADDFULFILLMENTPLACESMETADATA']._serialized_start = 1756
    _globals['_ADDFULFILLMENTPLACESMETADATA']._serialized_end = 1786
    _globals['_ADDFULFILLMENTPLACESRESPONSE']._serialized_start = 1788
    _globals['_ADDFULFILLMENTPLACESRESPONSE']._serialized_end = 1818
    _globals['_ADDLOCALINVENTORIESREQUEST']._serialized_start = 1821
    _globals['_ADDLOCALINVENTORIESREQUEST']._serialized_end = 2096
    _globals['_ADDLOCALINVENTORIESMETADATA']._serialized_start = 2098
    _globals['_ADDLOCALINVENTORIESMETADATA']._serialized_end = 2127
    _globals['_ADDLOCALINVENTORIESRESPONSE']._serialized_start = 2129
    _globals['_ADDLOCALINVENTORIESRESPONSE']._serialized_end = 2158
    _globals['_REMOVELOCALINVENTORIESREQUEST']._serialized_start = 2161
    _globals['_REMOVELOCALINVENTORIESREQUEST']._serialized_end = 2344
    _globals['_REMOVELOCALINVENTORIESMETADATA']._serialized_start = 2346
    _globals['_REMOVELOCALINVENTORIESMETADATA']._serialized_end = 2378
    _globals['_REMOVELOCALINVENTORIESRESPONSE']._serialized_start = 2380
    _globals['_REMOVELOCALINVENTORIESRESPONSE']._serialized_end = 2412
    _globals['_REMOVEFULFILLMENTPLACESREQUEST']._serialized_start = 2415
    _globals['_REMOVEFULFILLMENTPLACESREQUEST']._serialized_end = 2618
    _globals['_REMOVEFULFILLMENTPLACESMETADATA']._serialized_start = 2620
    _globals['_REMOVEFULFILLMENTPLACESMETADATA']._serialized_end = 2653
    _globals['_REMOVEFULFILLMENTPLACESRESPONSE']._serialized_start = 2655
    _globals['_REMOVEFULFILLMENTPLACESRESPONSE']._serialized_end = 2688
    _globals['_PRODUCTSERVICE']._serialized_start = 2691
    _globals['_PRODUCTSERVICE']._serialized_end = 6414