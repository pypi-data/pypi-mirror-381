"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2beta/catalog_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2beta import catalog_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_catalog__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/retail/v2beta/catalog_service.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/retail/v2beta/catalog.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"w\n\x13ListCatalogsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"f\n\x14ListCatalogsResponse\x125\n\x08catalogs\x18\x01 \x03(\x0b2#.google.cloud.retail.v2beta.Catalog\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x82\x01\n\x14UpdateCatalogRequest\x129\n\x07catalog\x18\x01 \x01(\x0b2#.google.cloud.retail.v2beta.CatalogB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xa1\x01\n\x17SetDefaultBranchRequest\x123\n\x07catalog\x18\x01 \x01(\tB"\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x124\n\tbranch_id\x18\x02 \x01(\tB!\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12\x0c\n\x04note\x18\x03 \x01(\t\x12\r\n\x05force\x18\x04 \x01(\x08"N\n\x17GetDefaultBranchRequest\x123\n\x07catalog\x18\x01 \x01(\tB"\xfaA\x1f\n\x1dretail.googleapis.com/Catalog"\x89\x01\n\x18GetDefaultBranchResponse\x121\n\x06branch\x18\x01 \x01(\tB!\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12,\n\x08set_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04note\x18\x03 \x01(\t"Z\n\x1aGetCompletionConfigRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&retail.googleapis.com/CompletionConfig"\x9e\x01\n\x1dUpdateCompletionConfigRequest\x12L\n\x11completion_config\x18\x01 \x01(\x0b2,.google.cloud.retail.v2beta.CompletionConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"Z\n\x1aGetAttributesConfigRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig"\x9e\x01\n\x1dUpdateAttributesConfigRequest\x12L\n\x11attributes_config\x18\x01 \x01(\x0b2,.google.cloud.retail.v2beta.AttributesConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xb5\x01\n\x1aAddCatalogAttributeRequest\x12I\n\x11attributes_config\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig\x12L\n\x11catalog_attribute\x18\x02 \x01(\x0b2,.google.cloud.retail.v2beta.CatalogAttributeB\x03\xe0A\x02"|\n\x1dRemoveCatalogAttributeRequest\x12I\n\x11attributes_config\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig\x12\x10\n\x03key\x18\x02 \x01(\tB\x03\xe0A\x02"\x8d\x01\n#BatchRemoveCatalogAttributesRequest\x12I\n\x11attributes_config\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig\x12\x1b\n\x0eattribute_keys\x18\x02 \x03(\tB\x03\xe0A\x02"l\n$BatchRemoveCatalogAttributesResponse\x12"\n\x1adeleted_catalog_attributes\x18\x01 \x03(\t\x12 \n\x18reset_catalog_attributes\x18\x02 \x03(\t"\xea\x01\n\x1eReplaceCatalogAttributeRequest\x12I\n\x11attributes_config\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&retail.googleapis.com/AttributesConfig\x12L\n\x11catalog_attribute\x18\x02 \x01(\x0b2,.google.cloud.retail.v2beta.CatalogAttributeB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask2\xb3\x16\n\x0eCatalogService\x12\xb4\x01\n\x0cListCatalogs\x12/.google.cloud.retail.v2beta.ListCatalogsRequest\x1a0.google.cloud.retail.v2beta.ListCatalogsResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v2beta/{parent=projects/*/locations/*}/catalogs\x12\xc7\x01\n\rUpdateCatalog\x120.google.cloud.retail.v2beta.UpdateCatalogRequest\x1a#.google.cloud.retail.v2beta.Catalog"_\xdaA\x13catalog,update_mask\x82\xd3\xe4\x93\x02C28/v2beta/{catalog.name=projects/*/locations/*/catalogs/*}:\x07catalog\x12\xba\x01\n\x10SetDefaultBranch\x123.google.cloud.retail.v2beta.SetDefaultBranchRequest\x1a\x16.google.protobuf.Empty"Y\xdaA\x07catalog\x82\xd3\xe4\x93\x02I"D/v2beta/{catalog=projects/*/locations/*/catalogs/*}:setDefaultBranch:\x01*\x12\xd5\x01\n\x10GetDefaultBranch\x123.google.cloud.retail.v2beta.GetDefaultBranchRequest\x1a4.google.cloud.retail.v2beta.GetDefaultBranchResponse"V\xdaA\x07catalog\x82\xd3\xe4\x93\x02F\x12D/v2beta/{catalog=projects/*/locations/*/catalogs/*}:getDefaultBranch\x12\xcd\x01\n\x13GetCompletionConfig\x126.google.cloud.retail.v2beta.GetCompletionConfigRequest\x1a,.google.cloud.retail.v2beta.CompletionConfig"P\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v2beta/{name=projects/*/locations/*/catalogs/*/completionConfig}\x12\x92\x02\n\x16UpdateCompletionConfig\x129.google.cloud.retail.v2beta.UpdateCompletionConfigRequest\x1a,.google.cloud.retail.v2beta.CompletionConfig"\x8e\x01\xdaA\x1dcompletion_config,update_mask\x82\xd3\xe4\x93\x02h2S/v2beta/{completion_config.name=projects/*/locations/*/catalogs/*/completionConfig}:\x11completion_config\x12\xcd\x01\n\x13GetAttributesConfig\x126.google.cloud.retail.v2beta.GetAttributesConfigRequest\x1a,.google.cloud.retail.v2beta.AttributesConfig"P\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v2beta/{name=projects/*/locations/*/catalogs/*/attributesConfig}\x12\x92\x02\n\x16UpdateAttributesConfig\x129.google.cloud.retail.v2beta.UpdateAttributesConfigRequest\x1a,.google.cloud.retail.v2beta.AttributesConfig"\x8e\x01\xdaA\x1dattributes_config,update_mask\x82\xd3\xe4\x93\x02h2S/v2beta/{attributes_config.name=projects/*/locations/*/catalogs/*/attributesConfig}:\x11attributes_config\x12\xea\x01\n\x13AddCatalogAttribute\x126.google.cloud.retail.v2beta.AddCatalogAttributeRequest\x1a,.google.cloud.retail.v2beta.AttributesConfig"m\x82\xd3\xe4\x93\x02g"b/v2beta/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:addCatalogAttribute:\x01*\x12\xf3\x01\n\x16RemoveCatalogAttribute\x129.google.cloud.retail.v2beta.RemoveCatalogAttributeRequest\x1a,.google.cloud.retail.v2beta.AttributesConfig"p\x82\xd3\xe4\x93\x02j"e/v2beta/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:removeCatalogAttribute:\x01*\x12\x99\x02\n\x1cBatchRemoveCatalogAttributes\x12?.google.cloud.retail.v2beta.BatchRemoveCatalogAttributesRequest\x1a@.google.cloud.retail.v2beta.BatchRemoveCatalogAttributesResponse"v\x82\xd3\xe4\x93\x02p"k/v2beta/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:batchRemoveCatalogAttributes:\x01*\x12\xf6\x01\n\x17ReplaceCatalogAttribute\x12:.google.cloud.retail.v2beta.ReplaceCatalogAttributeRequest\x1a,.google.cloud.retail.v2beta.AttributesConfig"q\x82\xd3\xe4\x93\x02k"f/v2beta/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:replaceCatalogAttribute:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd2\x01\n\x1ecom.google.cloud.retail.v2betaB\x13CatalogServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.catalog_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x13CatalogServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
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
    _globals['_CATALOGSERVICE'].methods_by_name['ListCatalogs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v2beta/{parent=projects/*/locations/*}/catalogs'
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateCatalog']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateCatalog']._serialized_options = b'\xdaA\x13catalog,update_mask\x82\xd3\xe4\x93\x02C28/v2beta/{catalog.name=projects/*/locations/*/catalogs/*}:\x07catalog'
    _globals['_CATALOGSERVICE'].methods_by_name['SetDefaultBranch']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['SetDefaultBranch']._serialized_options = b'\xdaA\x07catalog\x82\xd3\xe4\x93\x02I"D/v2beta/{catalog=projects/*/locations/*/catalogs/*}:setDefaultBranch:\x01*'
    _globals['_CATALOGSERVICE'].methods_by_name['GetDefaultBranch']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['GetDefaultBranch']._serialized_options = b'\xdaA\x07catalog\x82\xd3\xe4\x93\x02F\x12D/v2beta/{catalog=projects/*/locations/*/catalogs/*}:getDefaultBranch'
    _globals['_CATALOGSERVICE'].methods_by_name['GetCompletionConfig']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['GetCompletionConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v2beta/{name=projects/*/locations/*/catalogs/*/completionConfig}'
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateCompletionConfig']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateCompletionConfig']._serialized_options = b'\xdaA\x1dcompletion_config,update_mask\x82\xd3\xe4\x93\x02h2S/v2beta/{completion_config.name=projects/*/locations/*/catalogs/*/completionConfig}:\x11completion_config'
    _globals['_CATALOGSERVICE'].methods_by_name['GetAttributesConfig']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['GetAttributesConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v2beta/{name=projects/*/locations/*/catalogs/*/attributesConfig}'
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateAttributesConfig']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['UpdateAttributesConfig']._serialized_options = b'\xdaA\x1dattributes_config,update_mask\x82\xd3\xe4\x93\x02h2S/v2beta/{attributes_config.name=projects/*/locations/*/catalogs/*/attributesConfig}:\x11attributes_config'
    _globals['_CATALOGSERVICE'].methods_by_name['AddCatalogAttribute']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['AddCatalogAttribute']._serialized_options = b'\x82\xd3\xe4\x93\x02g"b/v2beta/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:addCatalogAttribute:\x01*'
    _globals['_CATALOGSERVICE'].methods_by_name['RemoveCatalogAttribute']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['RemoveCatalogAttribute']._serialized_options = b'\x82\xd3\xe4\x93\x02j"e/v2beta/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:removeCatalogAttribute:\x01*'
    _globals['_CATALOGSERVICE'].methods_by_name['BatchRemoveCatalogAttributes']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['BatchRemoveCatalogAttributes']._serialized_options = b'\x82\xd3\xe4\x93\x02p"k/v2beta/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:batchRemoveCatalogAttributes:\x01*'
    _globals['_CATALOGSERVICE'].methods_by_name['ReplaceCatalogAttribute']._loaded_options = None
    _globals['_CATALOGSERVICE'].methods_by_name['ReplaceCatalogAttribute']._serialized_options = b'\x82\xd3\xe4\x93\x02k"f/v2beta/{attributes_config=projects/*/locations/*/catalogs/*/attributesConfig}:replaceCatalogAttribute:\x01*'
    _globals['_LISTCATALOGSREQUEST']._serialized_start = 333
    _globals['_LISTCATALOGSREQUEST']._serialized_end = 452
    _globals['_LISTCATALOGSRESPONSE']._serialized_start = 454
    _globals['_LISTCATALOGSRESPONSE']._serialized_end = 556
    _globals['_UPDATECATALOGREQUEST']._serialized_start = 559
    _globals['_UPDATECATALOGREQUEST']._serialized_end = 689
    _globals['_SETDEFAULTBRANCHREQUEST']._serialized_start = 692
    _globals['_SETDEFAULTBRANCHREQUEST']._serialized_end = 853
    _globals['_GETDEFAULTBRANCHREQUEST']._serialized_start = 855
    _globals['_GETDEFAULTBRANCHREQUEST']._serialized_end = 933
    _globals['_GETDEFAULTBRANCHRESPONSE']._serialized_start = 936
    _globals['_GETDEFAULTBRANCHRESPONSE']._serialized_end = 1073
    _globals['_GETCOMPLETIONCONFIGREQUEST']._serialized_start = 1075
    _globals['_GETCOMPLETIONCONFIGREQUEST']._serialized_end = 1165
    _globals['_UPDATECOMPLETIONCONFIGREQUEST']._serialized_start = 1168
    _globals['_UPDATECOMPLETIONCONFIGREQUEST']._serialized_end = 1326
    _globals['_GETATTRIBUTESCONFIGREQUEST']._serialized_start = 1328
    _globals['_GETATTRIBUTESCONFIGREQUEST']._serialized_end = 1418
    _globals['_UPDATEATTRIBUTESCONFIGREQUEST']._serialized_start = 1421
    _globals['_UPDATEATTRIBUTESCONFIGREQUEST']._serialized_end = 1579
    _globals['_ADDCATALOGATTRIBUTEREQUEST']._serialized_start = 1582
    _globals['_ADDCATALOGATTRIBUTEREQUEST']._serialized_end = 1763
    _globals['_REMOVECATALOGATTRIBUTEREQUEST']._serialized_start = 1765
    _globals['_REMOVECATALOGATTRIBUTEREQUEST']._serialized_end = 1889
    _globals['_BATCHREMOVECATALOGATTRIBUTESREQUEST']._serialized_start = 1892
    _globals['_BATCHREMOVECATALOGATTRIBUTESREQUEST']._serialized_end = 2033
    _globals['_BATCHREMOVECATALOGATTRIBUTESRESPONSE']._serialized_start = 2035
    _globals['_BATCHREMOVECATALOGATTRIBUTESRESPONSE']._serialized_end = 2143
    _globals['_REPLACECATALOGATTRIBUTEREQUEST']._serialized_start = 2146
    _globals['_REPLACECATALOGATTRIBUTEREQUEST']._serialized_end = 2380
    _globals['_CATALOGSERVICE']._serialized_start = 2383
    _globals['_CATALOGSERVICE']._serialized_end = 5250