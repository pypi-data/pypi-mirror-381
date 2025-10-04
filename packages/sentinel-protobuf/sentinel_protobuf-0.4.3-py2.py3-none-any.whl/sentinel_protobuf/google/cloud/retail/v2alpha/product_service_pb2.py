"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/product_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import common_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_common__pb2
from .....google.cloud.retail.v2alpha import export_config_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_export__config__pb2
from .....google.cloud.retail.v2alpha import import_config_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_import__config__pb2
from .....google.cloud.retail.v2alpha import product_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_product__pb2
from .....google.cloud.retail.v2alpha import purge_config_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_purge__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/retail/v2alpha/product_service.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/retail/v2alpha/common.proto\x1a/google/cloud/retail/v2alpha/export_config.proto\x1a/google/cloud/retail/v2alpha/import_config.proto\x1a)google/cloud/retail/v2alpha/product.proto\x1a.google/cloud/retail/v2alpha/purge_config.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa1\x01\n\x14CreateProductRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12:\n\x07product\x18\x02 \x01(\x0b2$.google.cloud.retail.v2alpha.ProductB\x03\xe0A\x02\x12\x17\n\nproduct_id\x18\x03 \x01(\tB\x03\xe0A\x02"H\n\x11GetProductRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product"\x9a\x01\n\x14UpdateProductRequest\x12:\n\x07product\x18\x01 \x01(\x0b2$.google.cloud.retail.v2alpha.ProductB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x15\n\rallow_missing\x18\x03 \x01(\x08"Z\n\x14DeleteProductRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12\r\n\x05force\x18\x04 \x01(\x08"\xcd\x01\n\x13ListProductsRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x1a\n\x12require_total_size\x18\x06 \x01(\x08"{\n\x14ListProductsResponse\x126\n\x08products\x18\x01 \x03(\x0b2$.google.cloud.retail.v2alpha.Product\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\xc6\x01\n\x13SetInventoryRequest\x12<\n\tinventory\x18\x01 \x01(\x0b2$.google.cloud.retail.v2alpha.ProductB\x03\xe0A\x02\x12,\n\x08set_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12,\n\x08set_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x04 \x01(\x08"\x16\n\x14SetInventoryMetadata"\x16\n\x14SetInventoryResponse"\xc5\x01\n\x1bAddFulfillmentPlacesRequest\x126\n\x07product\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12\x11\n\x04type\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tplace_ids\x18\x03 \x03(\tB\x03\xe0A\x02\x12,\n\x08add_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x05 \x01(\x08"\x1e\n\x1cAddFulfillmentPlacesMetadata"\x1e\n\x1cAddFulfillmentPlacesResponse"\x94\x02\n\x1aAddLocalInventoriesRequest\x126\n\x07product\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12K\n\x11local_inventories\x18\x02 \x03(\x0b2+.google.cloud.retail.v2alpha.LocalInventoryB\x03\xe0A\x02\x12,\n\x08add_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12,\n\x08add_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x06 \x01(\x08"\x1d\n\x1bAddLocalInventoriesMetadata"\x1d\n\x1bAddLocalInventoriesResponse"\xb7\x01\n\x1dRemoveLocalInventoriesRequest\x126\n\x07product\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12\x16\n\tplace_ids\x18\x02 \x03(\tB\x03\xe0A\x02\x12/\n\x0bremove_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x03 \x01(\x08" \n\x1eRemoveLocalInventoriesMetadata" \n\x1eRemoveLocalInventoriesResponse"\xcb\x01\n\x1eRemoveFulfillmentPlacesRequest\x126\n\x07product\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Product\x12\x11\n\x04type\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tplace_ids\x18\x03 \x03(\tB\x03\xe0A\x02\x12/\n\x0bremove_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rallow_missing\x18\x05 \x01(\x08"!\n\x1fRemoveFulfillmentPlacesMetadata"!\n\x1fRemoveFulfillmentPlacesResponse2\xb9\x1d\n\x0eProductService\x12\xde\x01\n\rCreateProduct\x121.google.cloud.retail.v2alpha.CreateProductRequest\x1a$.google.cloud.retail.v2alpha.Product"t\xdaA\x19parent,product,product_id\x82\xd3\xe4\x93\x02R"G/v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:\x07product\x12\xbb\x01\n\nGetProduct\x12..google.cloud.retail.v2alpha.GetProductRequest\x1a$.google.cloud.retail.v2alpha.Product"W\xdaA\x04name\x82\xd3\xe4\x93\x02J\x12H/v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}\x12\xcd\x01\n\x0cListProducts\x120.google.cloud.retail.v2alpha.ListProductsRequest\x1a1.google.cloud.retail.v2alpha.ListProductsResponse"X\xdaA\x06parent\x82\xd3\xe4\x93\x02I\x12G/v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products\x12\xe1\x01\n\rUpdateProduct\x121.google.cloud.retail.v2alpha.UpdateProductRequest\x1a$.google.cloud.retail.v2alpha.Product"w\xdaA\x13product,update_mask\x82\xd3\xe4\x93\x02[2P/v2alpha/{product.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:\x07product\x12\xb3\x01\n\rDeleteProduct\x121.google.cloud.retail.v2alpha.DeleteProductRequest\x1a\x16.google.protobuf.Empty"W\xdaA\x04name\x82\xd3\xe4\x93\x02J*H/v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}\x12\xa5\x02\n\rPurgeProducts\x121.google.cloud.retail.v2alpha.PurgeProductsRequest\x1a\x1d.google.longrunning.Operation"\xc1\x01\xcaAf\n1google.cloud.retail.v2alpha.PurgeProductsResponse\x121google.cloud.retail.v2alpha.PurgeProductsMetadata\x82\xd3\xe4\x93\x02R"M/v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:purge:\x01*\x12\xa2\x02\n\x0eImportProducts\x122.google.cloud.retail.v2alpha.ImportProductsRequest\x1a\x1d.google.longrunning.Operation"\xbc\x01\xcaA`\n2google.cloud.retail.v2alpha.ImportProductsResponse\x12*google.cloud.retail.v2alpha.ImportMetadata\x82\xd3\xe4\x93\x02S"N/v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:import:\x01*\x12\xa2\x02\n\x0eExportProducts\x122.google.cloud.retail.v2alpha.ExportProductsRequest\x1a\x1d.google.longrunning.Operation"\xbc\x01\xcaA`\n2google.cloud.retail.v2alpha.ExportProductsResponse\x12*google.cloud.retail.v2alpha.ExportMetadata\x82\xd3\xe4\x93\x02S"N/v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:export:\x01*\x12\xc8\x02\n\x0cSetInventory\x120.google.cloud.retail.v2alpha.SetInventoryRequest\x1a\x1d.google.longrunning.Operation"\xe6\x01\xcaAd\n0google.cloud.retail.v2alpha.SetInventoryResponse\x120google.cloud.retail.v2alpha.SetInventoryMetadata\xdaA\x12inventory,set_mask\x82\xd3\xe4\x93\x02d"_/v2alpha/{inventory.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:setInventory:\x01*\x12\xde\x02\n\x14AddFulfillmentPlaces\x128.google.cloud.retail.v2alpha.AddFulfillmentPlacesRequest\x1a\x1d.google.longrunning.Operation"\xec\x01\xcaAt\n8google.cloud.retail.v2alpha.AddFulfillmentPlacesResponse\x128google.cloud.retail.v2alpha.AddFulfillmentPlacesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02e"`/v2alpha/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addFulfillmentPlaces:\x01*\x12\xed\x02\n\x17RemoveFulfillmentPlaces\x12;.google.cloud.retail.v2alpha.RemoveFulfillmentPlacesRequest\x1a\x1d.google.longrunning.Operation"\xf5\x01\xcaAz\n;google.cloud.retail.v2alpha.RemoveFulfillmentPlacesResponse\x12;google.cloud.retail.v2alpha.RemoveFulfillmentPlacesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02h"c/v2alpha/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeFulfillmentPlaces:\x01*\x12\xd9\x02\n\x13AddLocalInventories\x127.google.cloud.retail.v2alpha.AddLocalInventoriesRequest\x1a\x1d.google.longrunning.Operation"\xe9\x01\xcaAr\n7google.cloud.retail.v2alpha.AddLocalInventoriesResponse\x127google.cloud.retail.v2alpha.AddLocalInventoriesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02d"_/v2alpha/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addLocalInventories:\x01*\x12\xe8\x02\n\x16RemoveLocalInventories\x12:.google.cloud.retail.v2alpha.RemoveLocalInventoriesRequest\x1a\x1d.google.longrunning.Operation"\xf2\x01\xcaAx\n:google.cloud.retail.v2alpha.RemoveLocalInventoriesResponse\x12:google.cloud.retail.v2alpha.RemoveLocalInventoriesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02g"b/v2alpha/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeLocalInventories:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd7\x01\n\x1fcom.google.cloud.retail.v2alphaB\x13ProductServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.product_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x13ProductServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
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
    _globals['_PRODUCTSERVICE'].methods_by_name['CreateProduct']._serialized_options = b'\xdaA\x19parent,product,product_id\x82\xd3\xe4\x93\x02R"G/v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:\x07product'
    _globals['_PRODUCTSERVICE'].methods_by_name['GetProduct']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['GetProduct']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02J\x12H/v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}'
    _globals['_PRODUCTSERVICE'].methods_by_name['ListProducts']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['ListProducts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02I\x12G/v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products'
    _globals['_PRODUCTSERVICE'].methods_by_name['UpdateProduct']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['UpdateProduct']._serialized_options = b'\xdaA\x13product,update_mask\x82\xd3\xe4\x93\x02[2P/v2alpha/{product.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:\x07product'
    _globals['_PRODUCTSERVICE'].methods_by_name['DeleteProduct']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['DeleteProduct']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02J*H/v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*/products/**}'
    _globals['_PRODUCTSERVICE'].methods_by_name['PurgeProducts']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['PurgeProducts']._serialized_options = b'\xcaAf\n1google.cloud.retail.v2alpha.PurgeProductsResponse\x121google.cloud.retail.v2alpha.PurgeProductsMetadata\x82\xd3\xe4\x93\x02R"M/v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:purge:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['ImportProducts']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['ImportProducts']._serialized_options = b'\xcaA`\n2google.cloud.retail.v2alpha.ImportProductsResponse\x12*google.cloud.retail.v2alpha.ImportMetadata\x82\xd3\xe4\x93\x02S"N/v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:import:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['ExportProducts']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['ExportProducts']._serialized_options = b'\xcaA`\n2google.cloud.retail.v2alpha.ExportProductsResponse\x12*google.cloud.retail.v2alpha.ExportMetadata\x82\xd3\xe4\x93\x02S"N/v2alpha/{parent=projects/*/locations/*/catalogs/*/branches/*}/products:export:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['SetInventory']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['SetInventory']._serialized_options = b'\xcaAd\n0google.cloud.retail.v2alpha.SetInventoryResponse\x120google.cloud.retail.v2alpha.SetInventoryMetadata\xdaA\x12inventory,set_mask\x82\xd3\xe4\x93\x02d"_/v2alpha/{inventory.name=projects/*/locations/*/catalogs/*/branches/*/products/**}:setInventory:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['AddFulfillmentPlaces']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['AddFulfillmentPlaces']._serialized_options = b'\xcaAt\n8google.cloud.retail.v2alpha.AddFulfillmentPlacesResponse\x128google.cloud.retail.v2alpha.AddFulfillmentPlacesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02e"`/v2alpha/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addFulfillmentPlaces:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['RemoveFulfillmentPlaces']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['RemoveFulfillmentPlaces']._serialized_options = b'\xcaAz\n;google.cloud.retail.v2alpha.RemoveFulfillmentPlacesResponse\x12;google.cloud.retail.v2alpha.RemoveFulfillmentPlacesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02h"c/v2alpha/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeFulfillmentPlaces:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['AddLocalInventories']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['AddLocalInventories']._serialized_options = b'\xcaAr\n7google.cloud.retail.v2alpha.AddLocalInventoriesResponse\x127google.cloud.retail.v2alpha.AddLocalInventoriesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02d"_/v2alpha/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:addLocalInventories:\x01*'
    _globals['_PRODUCTSERVICE'].methods_by_name['RemoveLocalInventories']._loaded_options = None
    _globals['_PRODUCTSERVICE'].methods_by_name['RemoveLocalInventories']._serialized_options = b'\xcaAx\n:google.cloud.retail.v2alpha.RemoveLocalInventoriesResponse\x12:google.cloud.retail.v2alpha.RemoveLocalInventoriesMetadata\xdaA\x07product\x82\xd3\xe4\x93\x02g"b/v2alpha/{product=projects/*/locations/*/catalogs/*/branches/*/products/**}:removeLocalInventories:\x01*'
    _globals['_CREATEPRODUCTREQUEST']._serialized_start = 562
    _globals['_CREATEPRODUCTREQUEST']._serialized_end = 723
    _globals['_GETPRODUCTREQUEST']._serialized_start = 725
    _globals['_GETPRODUCTREQUEST']._serialized_end = 797
    _globals['_UPDATEPRODUCTREQUEST']._serialized_start = 800
    _globals['_UPDATEPRODUCTREQUEST']._serialized_end = 954
    _globals['_DELETEPRODUCTREQUEST']._serialized_start = 956
    _globals['_DELETEPRODUCTREQUEST']._serialized_end = 1046
    _globals['_LISTPRODUCTSREQUEST']._serialized_start = 1049
    _globals['_LISTPRODUCTSREQUEST']._serialized_end = 1254
    _globals['_LISTPRODUCTSRESPONSE']._serialized_start = 1256
    _globals['_LISTPRODUCTSRESPONSE']._serialized_end = 1379
    _globals['_SETINVENTORYREQUEST']._serialized_start = 1382
    _globals['_SETINVENTORYREQUEST']._serialized_end = 1580
    _globals['_SETINVENTORYMETADATA']._serialized_start = 1582
    _globals['_SETINVENTORYMETADATA']._serialized_end = 1604
    _globals['_SETINVENTORYRESPONSE']._serialized_start = 1606
    _globals['_SETINVENTORYRESPONSE']._serialized_end = 1628
    _globals['_ADDFULFILLMENTPLACESREQUEST']._serialized_start = 1631
    _globals['_ADDFULFILLMENTPLACESREQUEST']._serialized_end = 1828
    _globals['_ADDFULFILLMENTPLACESMETADATA']._serialized_start = 1830
    _globals['_ADDFULFILLMENTPLACESMETADATA']._serialized_end = 1860
    _globals['_ADDFULFILLMENTPLACESRESPONSE']._serialized_start = 1862
    _globals['_ADDFULFILLMENTPLACESRESPONSE']._serialized_end = 1892
    _globals['_ADDLOCALINVENTORIESREQUEST']._serialized_start = 1895
    _globals['_ADDLOCALINVENTORIESREQUEST']._serialized_end = 2171
    _globals['_ADDLOCALINVENTORIESMETADATA']._serialized_start = 2173
    _globals['_ADDLOCALINVENTORIESMETADATA']._serialized_end = 2202
    _globals['_ADDLOCALINVENTORIESRESPONSE']._serialized_start = 2204
    _globals['_ADDLOCALINVENTORIESRESPONSE']._serialized_end = 2233
    _globals['_REMOVELOCALINVENTORIESREQUEST']._serialized_start = 2236
    _globals['_REMOVELOCALINVENTORIESREQUEST']._serialized_end = 2419
    _globals['_REMOVELOCALINVENTORIESMETADATA']._serialized_start = 2421
    _globals['_REMOVELOCALINVENTORIESMETADATA']._serialized_end = 2453
    _globals['_REMOVELOCALINVENTORIESRESPONSE']._serialized_start = 2455
    _globals['_REMOVELOCALINVENTORIESRESPONSE']._serialized_end = 2487
    _globals['_REMOVEFULFILLMENTPLACESREQUEST']._serialized_start = 2490
    _globals['_REMOVEFULFILLMENTPLACESREQUEST']._serialized_end = 2693
    _globals['_REMOVEFULFILLMENTPLACESMETADATA']._serialized_start = 2695
    _globals['_REMOVEFULFILLMENTPLACESMETADATA']._serialized_end = 2728
    _globals['_REMOVEFULFILLMENTPLACESRESPONSE']._serialized_start = 2730
    _globals['_REMOVEFULFILLMENTPLACESRESPONSE']._serialized_end = 2763
    _globals['_PRODUCTSERVICE']._serialized_start = 2766
    _globals['_PRODUCTSERVICE']._serialized_end = 6535