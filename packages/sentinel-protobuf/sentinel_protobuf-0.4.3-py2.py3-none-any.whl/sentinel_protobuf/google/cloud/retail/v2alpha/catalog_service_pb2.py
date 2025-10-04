"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/catalog_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import catalog_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_catalog__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/retail/v2alpha/catalog_service.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/retail/v2alpha/catalog.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"w\n\x13ListCatalogsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"g\n\x14ListCatalogsResponse\x126\n\x08catalogs\x18\x01 \x03(\x0b2$.google.cloud.retail.v2alpha.Catalog\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x83\x01\n\x14UpdateCatalogRequest\x12:\n\x07catalog\x18\x01 \x01(\x0b2$.google.cloud.retail.v2alpha.CatalogB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xa1\x01\n\x17SetDefaultBranchRequest\x123\n\x07catalog\x18\x01 \x01(\tB"\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x124\n\tbranch_id\x18\x02 \x01(\tB!\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12\x0c\n\x04note\x18\x03 \x01(\t\x12\r\n\x05force\x18\x04 \x01(\x08"N\n\x17GetDefaultBranchRequest\x123\n\x07catalog\x18\x01 \x01(\tB"\xfaA\x1f\n\x1dretail.googleapis.com/Catalog"\x89\x01\n\x18GetDefaultBranchResponse\x121\n\x06branch\x18\x01 \x01(\tB!\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12,\n\x08set_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04note\x18\x03 \x01(\t"Z\n\x1aGetCompletionConfigRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&retail.googleapis.com/CompletionConfig"\x9f\x01\n\x1dUpdateCompletionConfigRequest\x12M\n\x11completion_config\x18\x01 \x01(\x0b2-.google.cloud.retail.v2alpha.CompletionConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"Z\n\x1aGetAttributesConfigRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig"\x9f\x01\n\x1dUpdateAttributesConfigRequest\x12M\n\x11attributes_config\x18\x01 \x01(\x0b2-.google.cloud.retail.v2alpha.AttributesConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xb6\x01\n\x1aAddCatalogAttributeRequest\x12I\n\x11attributes_config\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig\x12M\n\x11catalog_attribute\x18\x02 \x01(\x0b2-.google.cloud.retail.v2alpha.CatalogAttributeB\x03\xe0A\x02"|\n\x1dRemoveCatalogAttributeRequest\x12I\n\x11attributes_config\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig\x12\x10\n\x03key\x18\x02 \x01(\tB\x03\xe0A\x02"\x8d\x01\n#BatchRemoveCatalogAttributesRequest\x12I\n\x11attributes_config\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig\x12\x1b\n\x0eattribute_keys\x18\x02 \x03(\tB\x03\xe0A\x02"l\n$BatchRemoveCatalogAttributesResponse\x12"\n\x1adeleted_catalog_attributes\x18\x01 \x03(\t\x12 \n\x18reset_catalog_attributes\x18\x02 \x03(\t"\xeb\x01\n\x1eReplaceCatalogAttributeRequest\x12I\n\x11attributes_config\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig\x12M\n\x11catalog_attribute\x18\x02 \x01(\x0b2-.google.cloud.retail.v2alpha.CatalogAttributeB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask2\xd6\x16\n\x0eCatalogService\x12\xb7\x01\n\x0cListCatalogs\x120.google.cloud.retail.v2alpha.ListCatalogsRequest\x1a1.google.cloud.retail.v2alpha.ListCatalogsResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v2alpha/{parent=projects/*/locations/*}/catalogs\x12\xca\x01\n\rUpdateCatalog\x121.google.cloud.retail.v2alpha.UpdateCatalogRequest\x1a$.google.cloud.retail.v2alpha.Catalog"`\xdaA\x13catalog,update_mask\x82\xd3\xe4\x93\x02D29/v2alpha/{catalog.name=projects/*/locations/*/catalogs/*}:\x07catalog\x12\xbc\x01\n\x10SetDefaultBranch\x124.google.cloud.retail.v2alpha.SetDefaultBranchRequest\x1a\x16.google.protobuf.Empty"Z\xdaA\x07catalog\x82\xd3\xe4\x93\x02J"E/v2alpha/{catalog=projects/*/locations/*/catalogs/*}:setDefaultBranch:\x01*\x12\xd8\x01\n\x10GetDefaultBranch\x124.google.cloud.retail.v2alpha.GetDefaultBranchRequest\x1a5.google.cloud.retail.v2alpha.GetDefaultBranchResponse"W\xdaA\x07catalog\x82\xd3\xe4\x93\x02G\x12E/v2alpha/{catalog=projects/*/locations/*/catalogs/*}:getDefaultBranch\x12\xd0\x01\n\x13GetCompletionConfig\x127.google.cloud.retail.v2alpha.GetCompletionConfigRequest\x1a-.google.cloud.retail.v2alpha.CompletionConfig"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v2alpha/{name=projects/*/locations/*/catalogs/*/completionConfig}\x12\x95\x02\n\x16UpdateCompletionConfig\x12:.google.cloud.retail.v2alpha.UpdateCompletionConfigRequest\x1a-.google.cloud.retail.v2alpha.CompletionConfig"\x8f\x01\xdaA\x1dcompletion_config,update_mask\x82\xd3\xe4\x93\x02i2T/v2alpha/{completion_config.name=projects/*/locations/*/catalogs/*/completionConfig}:\x11completion_config\x12\xd0\x01\n\x13GetAttributesConfig\x127.google.cloud.retail.v2alpha.GetAttributesConfigRequest\x1a-.google.cloud.retail.v2alpha.AttributesConfig"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v2alpha/{name=projects/*/locations/*/catalogs/*/attributesConfig}\x12\x95\x02\n\x16UpdateAttributesConfig\x12:.google.cloud.retail.v2alpha.UpdateAttributesConfigRequest\x1a-.google.cloud.retail.v2alpha.AttributesConfig"\x8f\x01\xdaA\x1dattributes_config,update_mask\x82\xd3\xe4\x93\x02i2T/v2alpha/{attributes_config.name=projects/*/locations/*/catalogs/*/attributesConfig}:\x11attributes_config\x12\xed\x01\n\x13AddCatalogAttribute\x127.google.cloud.retail.v2alpha.AddCatalogAttributeRequest\x1a-.google.cloud.retail.v2alpha.AttributesConfig"n\x82\xd3\xe4\x93\x02h"c/v2alpha/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:addCatalogAttribute:\x01*\x12\xf6\x01\n\x16RemoveCatalogAttribute\x12:.google.cloud.retail.v2alpha.RemoveCatalogAttributeRequest\x1a-.google.cloud.retail.v2alpha.AttributesConfig"q\x82\xd3\xe4\x93\x02k"f/v2alpha/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:removeCatalogAttribute:\x01*\x12\x9c\x02\n\x1cBatchRemoveCatalogAttributes\x12@.google.cloud.retail.v2alpha.BatchRemoveCatalogAttributesRequest\x1aA.google.cloud.retail.v2alpha.BatchRemoveCatalogAttributesResponse"w\x82\xd3\xe4\x93\x02q"l/v2alpha/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:batchRemoveCatalogAttributes:\x01*\x12\xf9\x01\n\x17ReplaceCatalogAttribute\x12;.google.cloud.retail.v2alpha.ReplaceCatalogAttributeRequest\x1a-.google.cloud.retail.v2alpha.AttributesConfig"r\x82\xd3\xe4\x93\x02l"g/v2alpha/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:replaceCatalogAttribute:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd7\x01\n\x1fcom.google.cloud.retail.v2alphaB\x13CatalogServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.catalog_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x13CatalogServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_LISTCATALOGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCATALOGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_UPDATECATALOGREQUEST'].fields_by_name['catalog']._loaded_options = None
    _globals['_UPDATECATALOGREQUEST'].fields_by_name['catalog']._serialized_options = b'\xe0A\x02'
    _globals['_SETDEFAULTBRANCHREQUEST'].fields_by_name['catalog']._loaded_options = None
    _globals['_SETDEFAULTBRANCHREQUEST'].fields_by_name['catalog']._serialized_options = b'\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_SETDEFAULTBRANCHREQUEST'].fields_by_name['branch_id']._loaded_options = None
    _globals['_SETDEFAULTBRANCHREQUEST'].fields_by_name['branch_id']._serialized_options = b'\xfaA\x1e\n\x1cretail.googleapis.com/Branch'
    _globals['_GETDEFAULTBRANCHREQUEST'].fields_by_name['catalog']._loaded_options = None
    _globals['_GETDEFAULTBRANCHREQUEST'].fields_by_name['catalog']._serialized_options = b'\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_GETDEFAULTBRANCHRESPONSE'].fields_by_name['branch']._loaded_options = None
    _globals['_GETDEFAULTBRANCHRESPONSE'].fields_by_name['branch']._serialized_options = b'\xfaA\x1e\n\x1cretail.googleapis.com/Branch'
    _globals['_GETCOMPLETIONCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCOMPLETIONCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&retail.googleapis.com/CompletionConfig'
    _globals['_UPDATECOMPLETIONCONFIGREQUEST'].fields_by_name['completion_config']._loaded_options = None
    _globals['_UPDATECOMPLETIONCONFIGREQUEST'].fields_by_name['completion_config']._serialized_options = b'\xe0A\x02'
    _globals['_GETATTRIBUTESCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETATTRIBUTESCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig'
    _globals['_UPDATEATTRIBUTESCONFIGREQUEST'].fields_by_name['attributes_config']._loaded_options = None
    _globals['_UPDATEATTRIBUTESCONFIGREQUEST'].fields_by_name['attributes_config']._serialized_options = b'\xe0A\x02'
    _globals['_ADDCATALOGATTRIBUTEREQUEST'].fields_by_name['attributes_config']._loaded_options = None
    _globals['_ADDCATALOGATTRIBUTEREQUEST'].fields_by_name['attributes_config']._serialized_options = b'\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig'
    _globals['_ADDCATALOGATTRIBUTEREQUEST'].fields_by_name['catalog_attribute']._loaded_options = None
    _globals['_ADDCATALOGATTRIBUTEREQUEST'].fields_by_name['catalog_attribute']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVECATALOGATTRIBUTEREQUEST'].fields_by_name['attributes_config']._loaded_options = None
    _globals['_REMOVECATALOGATTRIBUTEREQUEST'].fields_by_name['attributes_config']._serialized_options = b'\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig'
    _globals['_REMOVECATALOGATTRIBUTEREQUEST'].fields_by_name['key']._loaded_options = None
    _globals['_REMOVECATALOGATTRIBUTEREQUEST'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHREMOVECATALOGATTRIBUTESREQUEST'].fields_by_name['attributes_config']._loaded_options = None
    _globals['_BATCHREMOVECATALOGATTRIBUTESREQUEST'].fields_by_name['attributes_config']._serialized_options = b'\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig'
    _globals['_BATCHREMOVECATALOGATTRIBUTESREQUEST'].fields_by_name['attribute_keys']._loaded_options = None
    _globals['_BATCHREMOVECATALOGATTRIBUTESREQUEST'].fields_by_name['attribute_keys']._serialized_options = b'\xe0A\x02'
    _globals['_REPLACECATALOGATTRIBUTEREQUEST'].fields_by_name['attributes_config']._loaded_options = None
    _globals['_REPLACECATALOGATTRIBUTEREQUEST'].fields_by_name['attributes_config']._serialized_options = b'\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig'
    _globals['_REPLACECATALOGATTRIBUTEREQUEST'].fields_by_name['catalog_attribute']._loaded_options = None
    _globals['_REPLACECATALOGATTRIBUTEREQUEST'].fields_by_name['catalog_attribute']._serialized_options = b'\xe0A\x02'
    _globals['_CATALOGSERVICE']._loaded_options = None
    _globals['_CATALOGSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CATALOGSERVICE'].methods_by_name['ListCatalogs']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['ListCatalogs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v2alpha/{parent=projects/*/locations/*}/catalogs'
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateCatalog']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateCatalog']._serialized_options = b'\xdaA\x13catalog,update_mask\x82\xd3\xe4\x93\x02D29/v2alpha/{catalog.name=projects/*/locations/*/catalogs/*}:\x07catalog'
    _globals['_CATALOGSERVICE'].methods_by_name['SetDefaultBranch']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['SetDefaultBranch']._serialized_options = b'\xdaA\x07catalog\x82\xd3\xe4\x93\x02J"E/v2alpha/{catalog=projects/*/locations/*/catalogs/*}:setDefaultBranch:\x01*'
    _globals['_CATALOGSERVICE'].methods_by_name['GetDefaultBranch']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['GetDefaultBranch']._serialized_options = b'\xdaA\x07catalog\x82\xd3\xe4\x93\x02G\x12E/v2alpha/{catalog=projects/*/locations/*/catalogs/*}:getDefaultBranch'
    _globals['_CATALOGSERVICE'].methods_by_name['GetCompletionConfig']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['GetCompletionConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v2alpha/{name=projects/*/locations/*/catalogs/*/completionConfig}'
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateCompletionConfig']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateCompletionConfig']._serialized_options = b'\xdaA\x1dcompletion_config,update_mask\x82\xd3\xe4\x93\x02i2T/v2alpha/{completion_config.name=projects/*/locations/*/catalogs/*/completionConfig}:\x11completion_config'
    _globals['_CATALOGSERVICE'].methods_by_name['GetAttributesConfig']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['GetAttributesConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v2alpha/{name=projects/*/locations/*/catalogs/*/attributesConfig}'
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateAttributesConfig']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateAttributesConfig']._serialized_options = b'\xdaA\x1dattributes_config,update_mask\x82\xd3\xe4\x93\x02i2T/v2alpha/{attributes_config.name=projects/*/locations/*/catalogs/*/attributesConfig}:\x11attributes_config'
    _globals['_CATALOGSERVICE'].methods_by_name['AddCatalogAttribute']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['AddCatalogAttribute']._serialized_options = b'\x82\xd3\xe4\x93\x02h"c/v2alpha/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:addCatalogAttribute:\x01*'
    _globals['_CATALOGSERVICE'].methods_by_name['RemoveCatalogAttribute']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['RemoveCatalogAttribute']._serialized_options = b'\x82\xd3\xe4\x93\x02k"f/v2alpha/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:removeCatalogAttribute:\x01*'
    _globals['_CATALOGSERVICE'].methods_by_name['BatchRemoveCatalogAttributes']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['BatchRemoveCatalogAttributes']._serialized_options = b'\x82\xd3\xe4\x93\x02q"l/v2alpha/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:batchRemoveCatalogAttributes:\x01*'
    _globals['_CATALOGSERVICE'].methods_by_name['ReplaceCatalogAttribute']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['ReplaceCatalogAttribute']._serialized_options = b'\x82\xd3\xe4\x93\x02l"g/v2alpha/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:replaceCatalogAttribute:\x01*'
    _globals['_LISTCATALOGSREQUEST']._serialized_start = 336
    _globals['_LISTCATALOGSREQUEST']._serialized_end = 455
    _globals['_LISTCATALOGSRESPONSE']._serialized_start = 457
    _globals['_LISTCATALOGSRESPONSE']._serialized_end = 560
    _globals['_UPDATECATALOGREQUEST']._serialized_start = 563
    _globals['_UPDATECATALOGREQUEST']._serialized_end = 694
    _globals['_SETDEFAULTBRANCHREQUEST']._serialized_start = 697
    _globals['_SETDEFAULTBRANCHREQUEST']._serialized_end = 858
    _globals['_GETDEFAULTBRANCHREQUEST']._serialized_start = 860
    _globals['_GETDEFAULTBRANCHREQUEST']._serialized_end = 938
    _globals['_GETDEFAULTBRANCHRESPONSE']._serialized_start = 941
    _globals['_GETDEFAULTBRANCHRESPONSE']._serialized_end = 1078
    _globals['_GETCOMPLETIONCONFIGREQUEST']._serialized_start = 1080
    _globals['_GETCOMPLETIONCONFIGREQUEST']._serialized_end = 1170
    _globals['_UPDATECOMPLETIONCONFIGREQUEST']._serialized_start = 1173
    _globals['_UPDATECOMPLETIONCONFIGREQUEST']._serialized_end = 1332
    _globals['_GETATTRIBUTESCONFIGREQUEST']._serialized_start = 1334
    _globals['_GETATTRIBUTESCONFIGREQUEST']._serialized_end = 1424
    _globals['_UPDATEATTRIBUTESCONFIGREQUEST']._serialized_start = 1427
    _globals['_UPDATEATTRIBUTESCONFIGREQUEST']._serialized_end = 1586
    _globals['_ADDCATALOGATTRIBUTEREQUEST']._serialized_start = 1589
    _globals['_ADDCATALOGATTRIBUTEREQUEST']._serialized_end = 1771
    _globals['_REMOVECATALOGATTRIBUTEREQUEST']._serialized_start = 1773
    _globals['_REMOVECATALOGATTRIBUTEREQUEST']._serialized_end = 1897
    _globals['_BATCHREMOVECATALOGATTRIBUTESREQUEST']._serialized_start = 1900
    _globals['_BATCHREMOVECATALOGATTRIBUTESREQUEST']._serialized_end = 2041
    _globals['_BATCHREMOVECATALOGATTRIBUTESRESPONSE']._serialized_start = 2043
    _globals['_BATCHREMOVECATALOGATTRIBUTESRESPONSE']._serialized_end = 2151
    _globals['_REPLACECATALOGATTRIBUTEREQUEST']._serialized_start = 2154
    _globals['_REPLACECATALOGATTRIBUTEREQUEST']._serialized_end = 2389
    _globals['_CATALOGSERVICE']._serialized_start = 2392
    _globals['_CATALOGSERVICE']._serialized_end = 5294