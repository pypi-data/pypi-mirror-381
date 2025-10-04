"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/biglake/v1/iceberg_rest_catalog.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/biglake/v1/iceberg_rest_catalog.proto\x12\x17google.cloud.biglake.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/httpbody.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb5\x01\n\x1bRegisterIcebergTableRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n biglake.googleapis.com/Namespace\x12\x11\n\x04name\x18\x02 \x01(\tB\x03\xe0A\x02\x121\n\x11metadata_location\x18\x03 \x01(\tB\x03\xe0A\x02R\x11metadata-location\x12\x16\n\toverwrite\x18\x04 \x01(\tB\x03\xe0A\x01"\xaf\x06\n\x0eIcebergCatalog\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12e\n\x0fcredential_mode\x18\x02 \x01(\x0e26.google.cloud.biglake.v1.IcebergCatalog.CredentialModeB\x03\xe0A\x01R\x0fcredential-mode\x12=\n\x17biglake_service_account\x18\x03 \x01(\tB\x03\xe0A\x03R\x17biglake-service-account\x12\\\n\x0ccatalog_type\x18\x04 \x01(\x0e23.google.cloud.biglake.v1.IcebergCatalog.CatalogTypeB\x03\xe0A\x02R\x0ccatalog-type\x12/\n\x10default_location\x18\x05 \x01(\tB\x03\xe0A\x01R\x10default-location\x12-\n\x0fcatalog_regions\x18\x06 \x03(\tB\x03\xe0A\x03R\x0fcatalog-regions\x12A\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03R\x0bcreate-time\x12A\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03R\x0bupdate-time"H\n\x0bCatalogType\x12\x1c\n\x18CATALOG_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17CATALOG_TYPE_GCS_BUCKET\x10\x01"w\n\x0eCredentialMode\x12\x1f\n\x1bCREDENTIAL_MODE_UNSPECIFIED\x10\x00\x12\x1c\n\x18CREDENTIAL_MODE_END_USER\x10\x01\x12&\n"CREDENTIAL_MODE_VENDED_CREDENTIALS\x10\x02:]\xeaAZ\n\x1ebiglake.googleapis.com/Catalog\x12%projects/{project}/catalogs/{catalog}*\x08catalogs2\x07catalog"\xde\x01\n\x1bCreateIcebergCatalogRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x123\n\x12iceberg_catalog_id\x18\x03 \x01(\tB\x03\xe0A\x02R\x12iceberg-catalog-id\x12E\n\x0ficeberg_catalog\x18\x02 \x01(\x0b2\'.google.cloud.biglake.v1.IcebergCatalogB\x03\xe0A\x02"S\n\x1bDeleteIcebergCatalogRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog"\x9a\x01\n\x1bUpdateIcebergCatalogRequest\x12E\n\x0ficeberg_catalog\x18\x01 \x01(\x0b2\'.google.cloud.biglake.v1.IcebergCatalogB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"P\n\x18GetIcebergCatalogRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog"\xd9\x02\n\x1aListIcebergCatalogsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12R\n\x04view\x18\x02 \x01(\x0e2?.google.cloud.biglake.v1.ListIcebergCatalogsRequest.CatalogViewB\x03\xe0A\x01\x12!\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01R\tpage-size\x12#\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01R\npage-token"Z\n\x0bCatalogView\x12\x1c\n\x18CATALOG_VIEW_UNSPECIFIED\x10\x00\x12\x16\n\x12CATALOG_VIEW_BASIC\x10\x01\x12\x15\n\x11CATALOG_VIEW_FULL\x10\x02"\xc0\x01\n\x1bListIcebergCatalogsResponse\x12X\n\x10iceberg_catalogs\x18\x01 \x03(\x0b2\'.google.cloud.biglake.v1.IcebergCatalogB\x03\xe0A\x03R\x10iceberg-catalogs\x12-\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x03R\x0fnext-page-token\x12\x18\n\x0bunreachable\x18\x03 \x03(\tB\x03\xe0A\x03"\xbc\x01\n\x1dFailoverIcebergCatalogRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0fprimary_replica\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01\x12N\n%conditional_failover_replication_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01"[\n\x1eFailoverIcebergCatalogResponse\x129\n\x10replication_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\x86\x01\n\x19UpdateIcebergTableRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table\x125\n\thttp_body\x18\x02 \x01(\x0b2\x14.google.api.HttpBodyB\x03\xe0A\x02R\x07updates"d\n\x16GetIcebergTableRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table\x12\x16\n\tsnapshots\x18\x02 \x01(\tB\x03\xe0A\x01"m\n\x19DeleteIcebergTableRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table\x12\x1c\n\x0fpurge_requested\x18\x02 \x01(\x08B\x03\xe0A\x01"\x83\x01\n\x19CreateIcebergTableRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n biglake.googleapis.com/Namespace\x12,\n\thttp_body\x18\x03 \x01(\x0b2\x14.google.api.HttpBodyB\x03\xe0A\x02"\x8f\x01\n"ListIcebergTableIdentifiersRequest\x12\x17\n\npage_token\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x128\n\x06parent\x18\x03 \x01(\tB(\xe0A\x02\xfaA"\n biglake.googleapis.com/Namespace"Y\n\x0fTableIdentifier\x128\n\tnamespace\x18\x01 \x03(\tB%\xfaA"\n biglake.googleapis.com/Namespace\x12\x0c\n\x04name\x18\x02 \x01(\t"\x98\x01\n#ListIcebergTableIdentifiersResponse\x12B\n\x0bidentifiers\x18\x01 \x03(\x0b2(.google.cloud.biglake.v1.TableIdentifierB\x03\xe0A\x03\x12-\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x03R\x0fnext-page-token"\xb3\x01\n\x16IcebergNamespaceUpdate\x12\x15\n\x08removals\x18\x02 \x03(\tB\x03\xe0A\x01\x12R\n\x07updates\x18\x03 \x03(\x0b2<.google.cloud.biglake.v1.IcebergNamespaceUpdate.UpdatesEntryB\x03\xe0A\x01\x1a.\n\x0cUpdatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xaf\x01\n\x1dUpdateIcebergNamespaceRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n biglake.googleapis.com/Namespace\x12V\n\x18iceberg_namespace_update\x18\x02 \x01(\x0b2/.google.cloud.biglake.v1.IcebergNamespaceUpdateB\x03\xe0A\x02"i\n\x1eUpdateIcebergNamespaceResponse\x12\x14\n\x07removed\x18\x01 \x03(\tB\x03\xe0A\x03\x12\x1b\n\x07updated\x18\x02 \x03(\tB\x03\xe0A\x03R\x05added\x12\x14\n\x07missing\x18\x03 \x03(\tB\x03\xe0A\x03"W\n\x1dDeleteIcebergNamespaceRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n biglake.googleapis.com/Namespace"\xb1\x01\n\x10IcebergNamespace\x12\x16\n\tnamespace\x18\x01 \x03(\tB\x03\xe0A\x02\x12R\n\nproperties\x18\x02 \x03(\x0b29.google.cloud.biglake.v1.IcebergNamespace.PropertiesEntryB\x03\xe0A\x01\x1a1\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xad\x01\n\x1dCreateIcebergNamespaceRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog\x12T\n\x11iceberg_namespace\x18\x02 \x01(\x0b2).google.cloud.biglake.v1.IcebergNamespaceB\x03\xe0A\x02R\tnamespace"8\n\x1eGetIcebergCatalogConfigRequest\x12\x16\n\twarehouse\x18\x01 \x01(\tB\x03\xe0A\x02"\xbb\x02\n\x14IcebergCatalogConfig\x12T\n\toverrides\x18\x01 \x03(\x0b2<.google.cloud.biglake.v1.IcebergCatalogConfig.OverridesEntryB\x03\xe0A\x03\x12R\n\x08defaults\x18\x02 \x03(\x0b2;.google.cloud.biglake.v1.IcebergCatalogConfig.DefaultsEntryB\x03\xe0A\x03\x12\x16\n\tendpoints\x18\x03 \x03(\tB\x03\xe0A\x03\x1a0\n\x0eOverridesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a/\n\rDefaultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x1aGetIcebergNamespaceRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n biglake.googleapis.com/Namespace"}\n\x1cListIcebergNamespacesRequest\x12\x17\n\npage_token\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\napi_parent\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06parent\x18\x04 \x01(\tB\x03\xe0A\x01"y\n\x1dListIcebergNamespacesResponse\x12.\n\nnamespaces\x18\x01 \x03(\x0b2\x1a.google.protobuf.ListValue\x12(\n\x0fnext_page_token\x18\x02 \x01(\tR\x0fnext-page-token"\x9a\x01\n\x11StorageCredential\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12F\n\x06config\x18\x02 \x03(\x0b26.google.cloud.biglake.v1.StorageCredential.ConfigEntry\x1a-\n\x0bConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x83\x01\n#LoadIcebergTableCredentialsResponse\x12\\\n\x13storage_credentials\x18\x01 \x03(\x0b2*.google.cloud.biglake.v1.StorageCredentialR\x13storage-credentials2\x82$\n\x15IcebergCatalogService\x12\xac\x01\n\x17GetIcebergCatalogConfig\x127.google.cloud.biglake.v1.GetIcebergCatalogConfigRequest\x1a-.google.cloud.biglake.v1.IcebergCatalogConfig")\x82\xd3\xe4\x93\x02#\x12!/iceberg/v1/restcatalog/v1/config\x12\xe5\x01\n\x15ListIcebergNamespaces\x125.google.cloud.biglake.v1.ListIcebergNamespacesRequest\x1a6.google.cloud.biglake.v1.ListIcebergNamespacesResponse"]\xdaA\napi_parent\x82\xd3\xe4\x93\x02J\x12H/iceberg/v1/restcatalog/v1/{api_parent=projects/*/catalogs/*}/namespaces\x12s\n\x1bCheckIcebergNamespaceExists\x123.google.cloud.biglake.v1.GetIcebergNamespaceRequest\x1a\x16.google.protobuf.Empty"\x07\xdaA\x04name\x12\xca\x01\n\x13GetIcebergNamespace\x123.google.cloud.biglake.v1.GetIcebergNamespaceRequest\x1a).google.cloud.biglake.v1.IcebergNamespace"S\xdaA\x04name\x82\xd3\xe4\x93\x02F\x12D/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*}\x12\xf7\x01\n\x16CreateIcebergNamespace\x126.google.cloud.biglake.v1.CreateIcebergNamespaceRequest\x1a).google.cloud.biglake.v1.IcebergNamespace"z\xdaA\x18parent,iceberg_namespace\x82\xd3\xe4\x93\x02Y"D/iceberg/v1/restcatalog/v1/{parent=projects/*/catalogs/*}/namespaces:\x11iceberg_namespace\x12\xbd\x01\n\x16DeleteIcebergNamespace\x126.google.cloud.biglake.v1.DeleteIcebergNamespaceRequest\x1a\x16.google.protobuf.Empty"S\xdaA\x04name\x82\xd3\xe4\x93\x02F*D/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*}\x12\xeb\x02\n\x16UpdateIcebergNamespace\x126.google.cloud.biglake.v1.UpdateIcebergNamespaceRequest\x1a7.google.cloud.biglake.v1.UpdateIcebergNamespaceResponse"\xdf\x01\x82\xd3\xe4\x93\x02\xd8\x012O/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*}/properties:\x18iceberg_namespace_updateZk"O/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*}/properties:\x18iceberg_namespace_update\x12\xf8\x01\n\x1bListIcebergTableIdentifiers\x12;.google.cloud.biglake.v1.ListIcebergTableIdentifiersRequest\x1a<.google.cloud.biglake.v1.ListIcebergTableIdentifiersResponse"^\xdaA\x06parent\x82\xd3\xe4\x93\x02O\x12M/iceberg/v1/restcatalog/v1/{parent=projects/*/catalogs/*/namespaces/*}/tables\x12\xcb\x01\n\x12CreateIcebergTable\x122.google.cloud.biglake.v1.CreateIcebergTableRequest\x1a\x14.google.api.HttpBody"k\xdaA\x10parent,http_body\x82\xd3\xe4\x93\x02R"M/iceberg/v1/restcatalog/v1/{parent=projects/*/catalogs/*/namespaces/*}/tables:\x01*\x12k\n\x17CheckIcebergTableExists\x12/.google.cloud.biglake.v1.GetIcebergTableRequest\x1a\x16.google.protobuf.Empty"\x07\xdaA\x04name\x12\xbe\x01\n\x12DeleteIcebergTable\x122.google.cloud.biglake.v1.DeleteIcebergTableRequest\x1a\x16.google.protobuf.Empty"\\\xdaA\x04name\x82\xd3\xe4\x93\x02O*M/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*/tables/*}\x12\xc0\x01\n\x0fGetIcebergTable\x12/.google.cloud.biglake.v1.GetIcebergTableRequest\x1a\x14.google.api.HttpBody"f\xdaA\x0ename,snapshots\x82\xd3\xe4\x93\x02O\x12M/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*/tables/*}\x12\xf6\x01\n\x1bLoadIcebergTableCredentials\x12/.google.cloud.biglake.v1.GetIcebergTableRequest\x1a<.google.cloud.biglake.v1.LoadIcebergTableCredentialsResponse"h\xdaA\x04name\x82\xd3\xe4\x93\x02[\x12Y/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*/tables/*}/credentials\x12\xb8\x01\n\x12UpdateIcebergTable\x122.google.cloud.biglake.v1.UpdateIcebergTableRequest\x1a\x14.google.api.HttpBody"X\x82\xd3\xe4\x93\x02R"M/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*/tables/*}:\x01*\x12\xbe\x01\n\x14RegisterIcebergTable\x124.google.cloud.biglake.v1.RegisterIcebergTableRequest\x1a\x14.google.api.HttpBody"Z\x82\xd3\xe4\x93\x02T"O/iceberg/v1/restcatalog/v1/{parent=projects/*/catalogs/*/namespaces/*}/register:\x01*\x12\xbf\x01\n\x11GetIcebergCatalog\x121.google.cloud.biglake.v1.GetIcebergCatalogRequest\x1a\'.google.cloud.biglake.v1.IcebergCatalog"N\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/iceberg/v1/restcatalog/extensions/{name=projects/*/catalogs/*}\x12\xd2\x01\n\x13ListIcebergCatalogs\x123.google.cloud.biglake.v1.ListIcebergCatalogsRequest\x1a4.google.cloud.biglake.v1.ListIcebergCatalogsResponse"P\xdaA\x06parent\x82\xd3\xe4\x93\x02A\x12?/iceberg/v1/restcatalog/extensions/{parent=projects/*}/catalogs\x12\xb4\x01\n\x14DeleteIcebergCatalog\x124.google.cloud.biglake.v1.DeleteIcebergCatalogRequest\x1a\x16.google.protobuf.Empty"N\xdaA\x04name\x82\xd3\xe4\x93\x02A*?/iceberg/v1/restcatalog/extensions/{name=projects/*/catalogs/*}\x12\xfe\x01\n\x14UpdateIcebergCatalog\x124.google.cloud.biglake.v1.UpdateIcebergCatalogRequest\x1a\'.google.cloud.biglake.v1.IcebergCatalog"\x86\x01\xdaA\x1biceberg_catalog,update_mask\x82\xd3\xe4\x93\x02b2O/iceberg/v1/restcatalog/extensions/{iceberg_catalog.name=projects/*/catalogs/*}:\x0ficeberg_catalog\x12\xfc\x01\n\x14CreateIcebergCatalog\x124.google.cloud.biglake.v1.CreateIcebergCatalogRequest\x1a\'.google.cloud.biglake.v1.IcebergCatalog"\x84\x01\xdaA)parent,iceberg_catalog,iceberg_catalog_id\x82\xd3\xe4\x93\x02R"?/iceberg/v1/restcatalog/extensions/{parent=projects/*}/catalogs:\x0ficeberg_catalog\x12\xf5\x01\n\x16FailoverIcebergCatalog\x126.google.cloud.biglake.v1.FailoverIcebergCatalogRequest\x1a7.google.cloud.biglake.v1.FailoverIcebergCatalogResponse"j\xdaA\x14name,primary_replica\x82\xd3\xe4\x93\x02M"H/iceberg/v1/restcatalog/extensions/{name=projects/*/catalogs/*}:failover:\x01*\x1as\xcaA\x16biglake.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platformB\xc0\x02\n\x1bcom.google.cloud.biglake.v1B\x17IcebergRestCatalogProtoP\x01Z5cloud.google.com/go/biglake/apiv1/biglakepb;biglakepb\xeaAk\n\x1cbiglake.googleapis.com/Table\x12Kprojects/{project}/catalogs/{catalog}/namespaces/{namespace}/tables/{table}\xeaA`\n biglake.googleapis.com/Namespace\x12<projects/{project}/catalogs/{catalog}/namespaces/{namespace}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.biglake.v1.iceberg_rest_catalog_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.cloud.biglake.v1B\x17IcebergRestCatalogProtoP\x01Z5cloud.google.com/go/biglake/apiv1/biglakepb;biglakepb\xeaAk\n\x1cbiglake.googleapis.com/Table\x12Kprojects/{project}/catalogs/{catalog}/namespaces/{namespace}/tables/{table}\xeaA`\n biglake.googleapis.com/Namespace\x12<projects/{project}/catalogs/{catalog}/namespaces/{namespace}'
    _globals['_REGISTERICEBERGTABLEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_REGISTERICEBERGTABLEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n biglake.googleapis.com/Namespace'
    _globals['_REGISTERICEBERGTABLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REGISTERICEBERGTABLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_REGISTERICEBERGTABLEREQUEST'].fields_by_name['metadata_location']._loaded_options = None
    _globals['_REGISTERICEBERGTABLEREQUEST'].fields_by_name['metadata_location']._serialized_options = b'\xe0A\x02'
    _globals['_REGISTERICEBERGTABLEREQUEST'].fields_by_name['overwrite']._loaded_options = None
    _globals['_REGISTERICEBERGTABLEREQUEST'].fields_by_name['overwrite']._serialized_options = b'\xe0A\x01'
    _globals['_ICEBERGCATALOG'].fields_by_name['name']._loaded_options = None
    _globals['_ICEBERGCATALOG'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ICEBERGCATALOG'].fields_by_name['credential_mode']._loaded_options = None
    _globals['_ICEBERGCATALOG'].fields_by_name['credential_mode']._serialized_options = b'\xe0A\x01'
    _globals['_ICEBERGCATALOG'].fields_by_name['biglake_service_account']._loaded_options = None
    _globals['_ICEBERGCATALOG'].fields_by_name['biglake_service_account']._serialized_options = b'\xe0A\x03'
    _globals['_ICEBERGCATALOG'].fields_by_name['catalog_type']._loaded_options = None
    _globals['_ICEBERGCATALOG'].fields_by_name['catalog_type']._serialized_options = b'\xe0A\x02'
    _globals['_ICEBERGCATALOG'].fields_by_name['default_location']._loaded_options = None
    _globals['_ICEBERGCATALOG'].fields_by_name['default_location']._serialized_options = b'\xe0A\x01'
    _globals['_ICEBERGCATALOG'].fields_by_name['catalog_regions']._loaded_options = None
    _globals['_ICEBERGCATALOG'].fields_by_name['catalog_regions']._serialized_options = b'\xe0A\x03'
    _globals['_ICEBERGCATALOG'].fields_by_name['create_time']._loaded_options = None
    _globals['_ICEBERGCATALOG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ICEBERGCATALOG'].fields_by_name['update_time']._loaded_options = None
    _globals['_ICEBERGCATALOG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ICEBERGCATALOG']._loaded_options = None
    _globals['_ICEBERGCATALOG']._serialized_options = b'\xeaAZ\n\x1ebiglake.googleapis.com/Catalog\x12%projects/{project}/catalogs/{catalog}*\x08catalogs2\x07catalog'
    _globals['_CREATEICEBERGCATALOGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEICEBERGCATALOGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATEICEBERGCATALOGREQUEST'].fields_by_name['iceberg_catalog_id']._loaded_options = None
    _globals['_CREATEICEBERGCATALOGREQUEST'].fields_by_name['iceberg_catalog_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEICEBERGCATALOGREQUEST'].fields_by_name['iceberg_catalog']._loaded_options = None
    _globals['_CREATEICEBERGCATALOGREQUEST'].fields_by_name['iceberg_catalog']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEICEBERGCATALOGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEICEBERGCATALOGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog'
    _globals['_UPDATEICEBERGCATALOGREQUEST'].fields_by_name['iceberg_catalog']._loaded_options = None
    _globals['_UPDATEICEBERGCATALOGREQUEST'].fields_by_name['iceberg_catalog']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEICEBERGCATALOGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEICEBERGCATALOGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_GETICEBERGCATALOGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETICEBERGCATALOGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog'
    _globals['_LISTICEBERGCATALOGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTICEBERGCATALOGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_LISTICEBERGCATALOGSREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_LISTICEBERGCATALOGSREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_LISTICEBERGCATALOGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTICEBERGCATALOGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTICEBERGCATALOGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTICEBERGCATALOGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTICEBERGCATALOGSRESPONSE'].fields_by_name['iceberg_catalogs']._loaded_options = None
    _globals['_LISTICEBERGCATALOGSRESPONSE'].fields_by_name['iceberg_catalogs']._serialized_options = b'\xe0A\x03'
    _globals['_LISTICEBERGCATALOGSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_LISTICEBERGCATALOGSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x03'
    _globals['_LISTICEBERGCATALOGSRESPONSE'].fields_by_name['unreachable']._loaded_options = None
    _globals['_LISTICEBERGCATALOGSRESPONSE'].fields_by_name['unreachable']._serialized_options = b'\xe0A\x03'
    _globals['_FAILOVERICEBERGCATALOGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_FAILOVERICEBERGCATALOGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_FAILOVERICEBERGCATALOGREQUEST'].fields_by_name['primary_replica']._loaded_options = None
    _globals['_FAILOVERICEBERGCATALOGREQUEST'].fields_by_name['primary_replica']._serialized_options = b'\xe0A\x02'
    _globals['_FAILOVERICEBERGCATALOGREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_FAILOVERICEBERGCATALOGREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_FAILOVERICEBERGCATALOGREQUEST'].fields_by_name['conditional_failover_replication_time']._loaded_options = None
    _globals['_FAILOVERICEBERGCATALOGREQUEST'].fields_by_name['conditional_failover_replication_time']._serialized_options = b'\xe0A\x01'
    _globals['_FAILOVERICEBERGCATALOGRESPONSE'].fields_by_name['replication_time']._loaded_options = None
    _globals['_FAILOVERICEBERGCATALOGRESPONSE'].fields_by_name['replication_time']._serialized_options = b'\xe0A\x03'
    _globals['_UPDATEICEBERGTABLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEICEBERGTABLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table'
    _globals['_UPDATEICEBERGTABLEREQUEST'].fields_by_name['http_body']._loaded_options = None
    _globals['_UPDATEICEBERGTABLEREQUEST'].fields_by_name['http_body']._serialized_options = b'\xe0A\x02'
    _globals['_GETICEBERGTABLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETICEBERGTABLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table'
    _globals['_GETICEBERGTABLEREQUEST'].fields_by_name['snapshots']._loaded_options = None
    _globals['_GETICEBERGTABLEREQUEST'].fields_by_name['snapshots']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEICEBERGTABLEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEICEBERGTABLEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cbiglake.googleapis.com/Table'
    _globals['_DELETEICEBERGTABLEREQUEST'].fields_by_name['purge_requested']._loaded_options = None
    _globals['_DELETEICEBERGTABLEREQUEST'].fields_by_name['purge_requested']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEICEBERGTABLEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEICEBERGTABLEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n biglake.googleapis.com/Namespace'
    _globals['_CREATEICEBERGTABLEREQUEST'].fields_by_name['http_body']._loaded_options = None
    _globals['_CREATEICEBERGTABLEREQUEST'].fields_by_name['http_body']._serialized_options = b'\xe0A\x02'
    _globals['_LISTICEBERGTABLEIDENTIFIERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTICEBERGTABLEIDENTIFIERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTICEBERGTABLEIDENTIFIERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTICEBERGTABLEIDENTIFIERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTICEBERGTABLEIDENTIFIERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTICEBERGTABLEIDENTIFIERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n biglake.googleapis.com/Namespace'
    _globals['_TABLEIDENTIFIER'].fields_by_name['namespace']._loaded_options = None
    _globals['_TABLEIDENTIFIER'].fields_by_name['namespace']._serialized_options = b'\xfaA"\n biglake.googleapis.com/Namespace'
    _globals['_LISTICEBERGTABLEIDENTIFIERSRESPONSE'].fields_by_name['identifiers']._loaded_options = None
    _globals['_LISTICEBERGTABLEIDENTIFIERSRESPONSE'].fields_by_name['identifiers']._serialized_options = b'\xe0A\x03'
    _globals['_LISTICEBERGTABLEIDENTIFIERSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_LISTICEBERGTABLEIDENTIFIERSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x03'
    _globals['_ICEBERGNAMESPACEUPDATE_UPDATESENTRY']._loaded_options = None
    _globals['_ICEBERGNAMESPACEUPDATE_UPDATESENTRY']._serialized_options = b'8\x01'
    _globals['_ICEBERGNAMESPACEUPDATE'].fields_by_name['removals']._loaded_options = None
    _globals['_ICEBERGNAMESPACEUPDATE'].fields_by_name['removals']._serialized_options = b'\xe0A\x01'
    _globals['_ICEBERGNAMESPACEUPDATE'].fields_by_name['updates']._loaded_options = None
    _globals['_ICEBERGNAMESPACEUPDATE'].fields_by_name['updates']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEICEBERGNAMESPACEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEICEBERGNAMESPACEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n biglake.googleapis.com/Namespace'
    _globals['_UPDATEICEBERGNAMESPACEREQUEST'].fields_by_name['iceberg_namespace_update']._loaded_options = None
    _globals['_UPDATEICEBERGNAMESPACEREQUEST'].fields_by_name['iceberg_namespace_update']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEICEBERGNAMESPACERESPONSE'].fields_by_name['removed']._loaded_options = None
    _globals['_UPDATEICEBERGNAMESPACERESPONSE'].fields_by_name['removed']._serialized_options = b'\xe0A\x03'
    _globals['_UPDATEICEBERGNAMESPACERESPONSE'].fields_by_name['updated']._loaded_options = None
    _globals['_UPDATEICEBERGNAMESPACERESPONSE'].fields_by_name['updated']._serialized_options = b'\xe0A\x03'
    _globals['_UPDATEICEBERGNAMESPACERESPONSE'].fields_by_name['missing']._loaded_options = None
    _globals['_UPDATEICEBERGNAMESPACERESPONSE'].fields_by_name['missing']._serialized_options = b'\xe0A\x03'
    _globals['_DELETEICEBERGNAMESPACEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEICEBERGNAMESPACEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n biglake.googleapis.com/Namespace'
    _globals['_ICEBERGNAMESPACE_PROPERTIESENTRY']._loaded_options = None
    _globals['_ICEBERGNAMESPACE_PROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_ICEBERGNAMESPACE'].fields_by_name['namespace']._loaded_options = None
    _globals['_ICEBERGNAMESPACE'].fields_by_name['namespace']._serialized_options = b'\xe0A\x02'
    _globals['_ICEBERGNAMESPACE'].fields_by_name['properties']._loaded_options = None
    _globals['_ICEBERGNAMESPACE'].fields_by_name['properties']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEICEBERGNAMESPACEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEICEBERGNAMESPACEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \n\x1ebiglake.googleapis.com/Catalog'
    _globals['_CREATEICEBERGNAMESPACEREQUEST'].fields_by_name['iceberg_namespace']._loaded_options = None
    _globals['_CREATEICEBERGNAMESPACEREQUEST'].fields_by_name['iceberg_namespace']._serialized_options = b'\xe0A\x02'
    _globals['_GETICEBERGCATALOGCONFIGREQUEST'].fields_by_name['warehouse']._loaded_options = None
    _globals['_GETICEBERGCATALOGCONFIGREQUEST'].fields_by_name['warehouse']._serialized_options = b'\xe0A\x02'
    _globals['_ICEBERGCATALOGCONFIG_OVERRIDESENTRY']._loaded_options = None
    _globals['_ICEBERGCATALOGCONFIG_OVERRIDESENTRY']._serialized_options = b'8\x01'
    _globals['_ICEBERGCATALOGCONFIG_DEFAULTSENTRY']._loaded_options = None
    _globals['_ICEBERGCATALOGCONFIG_DEFAULTSENTRY']._serialized_options = b'8\x01'
    _globals['_ICEBERGCATALOGCONFIG'].fields_by_name['overrides']._loaded_options = None
    _globals['_ICEBERGCATALOGCONFIG'].fields_by_name['overrides']._serialized_options = b'\xe0A\x03'
    _globals['_ICEBERGCATALOGCONFIG'].fields_by_name['defaults']._loaded_options = None
    _globals['_ICEBERGCATALOGCONFIG'].fields_by_name['defaults']._serialized_options = b'\xe0A\x03'
    _globals['_ICEBERGCATALOGCONFIG'].fields_by_name['endpoints']._loaded_options = None
    _globals['_ICEBERGCATALOGCONFIG'].fields_by_name['endpoints']._serialized_options = b'\xe0A\x03'
    _globals['_GETICEBERGNAMESPACEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETICEBERGNAMESPACEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n biglake.googleapis.com/Namespace'
    _globals['_LISTICEBERGNAMESPACESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTICEBERGNAMESPACESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTICEBERGNAMESPACESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTICEBERGNAMESPACESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTICEBERGNAMESPACESREQUEST'].fields_by_name['api_parent']._loaded_options = None
    _globals['_LISTICEBERGNAMESPACESREQUEST'].fields_by_name['api_parent']._serialized_options = b'\xe0A\x02'
    _globals['_LISTICEBERGNAMESPACESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTICEBERGNAMESPACESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGECREDENTIAL_CONFIGENTRY']._loaded_options = None
    _globals['_STORAGECREDENTIAL_CONFIGENTRY']._serialized_options = b'8\x01'
    _globals['_ICEBERGCATALOGSERVICE']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE']._serialized_options = b'\xcaA\x16biglake.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['GetIcebergCatalogConfig']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['GetIcebergCatalogConfig']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/iceberg/v1/restcatalog/v1/config'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['ListIcebergNamespaces']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['ListIcebergNamespaces']._serialized_options = b'\xdaA\napi_parent\x82\xd3\xe4\x93\x02J\x12H/iceberg/v1/restcatalog/v1/{api_parent=projects/*/catalogs/*}/namespaces'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['CheckIcebergNamespaceExists']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['CheckIcebergNamespaceExists']._serialized_options = b'\xdaA\x04name'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['GetIcebergNamespace']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['GetIcebergNamespace']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02F\x12D/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*}'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['CreateIcebergNamespace']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['CreateIcebergNamespace']._serialized_options = b'\xdaA\x18parent,iceberg_namespace\x82\xd3\xe4\x93\x02Y"D/iceberg/v1/restcatalog/v1/{parent=projects/*/catalogs/*}/namespaces:\x11iceberg_namespace'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['DeleteIcebergNamespace']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['DeleteIcebergNamespace']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02F*D/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*}'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['UpdateIcebergNamespace']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['UpdateIcebergNamespace']._serialized_options = b'\x82\xd3\xe4\x93\x02\xd8\x012O/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*}/properties:\x18iceberg_namespace_updateZk"O/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*}/properties:\x18iceberg_namespace_update'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['ListIcebergTableIdentifiers']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['ListIcebergTableIdentifiers']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02O\x12M/iceberg/v1/restcatalog/v1/{parent=projects/*/catalogs/*/namespaces/*}/tables'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['CreateIcebergTable']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['CreateIcebergTable']._serialized_options = b'\xdaA\x10parent,http_body\x82\xd3\xe4\x93\x02R"M/iceberg/v1/restcatalog/v1/{parent=projects/*/catalogs/*/namespaces/*}/tables:\x01*'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['CheckIcebergTableExists']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['CheckIcebergTableExists']._serialized_options = b'\xdaA\x04name'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['DeleteIcebergTable']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['DeleteIcebergTable']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02O*M/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*/tables/*}'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['GetIcebergTable']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['GetIcebergTable']._serialized_options = b'\xdaA\x0ename,snapshots\x82\xd3\xe4\x93\x02O\x12M/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*/tables/*}'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['LoadIcebergTableCredentials']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['LoadIcebergTableCredentials']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02[\x12Y/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*/tables/*}/credentials'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['UpdateIcebergTable']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['UpdateIcebergTable']._serialized_options = b'\x82\xd3\xe4\x93\x02R"M/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*/tables/*}:\x01*'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['RegisterIcebergTable']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['RegisterIcebergTable']._serialized_options = b'\x82\xd3\xe4\x93\x02T"O/iceberg/v1/restcatalog/v1/{parent=projects/*/catalogs/*/namespaces/*}/register:\x01*'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['GetIcebergCatalog']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['GetIcebergCatalog']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/iceberg/v1/restcatalog/extensions/{name=projects/*/catalogs/*}'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['ListIcebergCatalogs']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['ListIcebergCatalogs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02A\x12?/iceberg/v1/restcatalog/extensions/{parent=projects/*}/catalogs'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['DeleteIcebergCatalog']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['DeleteIcebergCatalog']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A*?/iceberg/v1/restcatalog/extensions/{name=projects/*/catalogs/*}'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['UpdateIcebergCatalog']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['UpdateIcebergCatalog']._serialized_options = b'\xdaA\x1biceberg_catalog,update_mask\x82\xd3\xe4\x93\x02b2O/iceberg/v1/restcatalog/extensions/{iceberg_catalog.name=projects/*/catalogs/*}:\x0ficeberg_catalog'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['CreateIcebergCatalog']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['CreateIcebergCatalog']._serialized_options = b'\xdaA)parent,iceberg_catalog,iceberg_catalog_id\x82\xd3\xe4\x93\x02R"?/iceberg/v1/restcatalog/extensions/{parent=projects/*}/catalogs:\x0ficeberg_catalog'
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['FailoverIcebergCatalog']._loaded_options = None
    _globals['_ICEBERGCATALOGSERVICE'].methods_by_name['FailoverIcebergCatalog']._serialized_options = b'\xdaA\x14name,primary_replica\x82\xd3\xe4\x93\x02M"H/iceberg/v1/restcatalog/extensions/{name=projects/*/catalogs/*}:failover:\x01*'
    _globals['_REGISTERICEBERGTABLEREQUEST']._serialized_start = 348
    _globals['_REGISTERICEBERGTABLEREQUEST']._serialized_end = 529
    _globals['_ICEBERGCATALOG']._serialized_start = 532
    _globals['_ICEBERGCATALOG']._serialized_end = 1347
    _globals['_ICEBERGCATALOG_CATALOGTYPE']._serialized_start = 1059
    _globals['_ICEBERGCATALOG_CATALOGTYPE']._serialized_end = 1131
    _globals['_ICEBERGCATALOG_CREDENTIALMODE']._serialized_start = 1133
    _globals['_ICEBERGCATALOG_CREDENTIALMODE']._serialized_end = 1252
    _globals['_CREATEICEBERGCATALOGREQUEST']._serialized_start = 1350
    _globals['_CREATEICEBERGCATALOGREQUEST']._serialized_end = 1572
    _globals['_DELETEICEBERGCATALOGREQUEST']._serialized_start = 1574
    _globals['_DELETEICEBERGCATALOGREQUEST']._serialized_end = 1657
    _globals['_UPDATEICEBERGCATALOGREQUEST']._serialized_start = 1660
    _globals['_UPDATEICEBERGCATALOGREQUEST']._serialized_end = 1814
    _globals['_GETICEBERGCATALOGREQUEST']._serialized_start = 1816
    _globals['_GETICEBERGCATALOGREQUEST']._serialized_end = 1896
    _globals['_LISTICEBERGCATALOGSREQUEST']._serialized_start = 1899
    _globals['_LISTICEBERGCATALOGSREQUEST']._serialized_end = 2244
    _globals['_LISTICEBERGCATALOGSREQUEST_CATALOGVIEW']._serialized_start = 2154
    _globals['_LISTICEBERGCATALOGSREQUEST_CATALOGVIEW']._serialized_end = 2244
    _globals['_LISTICEBERGCATALOGSRESPONSE']._serialized_start = 2247
    _globals['_LISTICEBERGCATALOGSRESPONSE']._serialized_end = 2439
    _globals['_FAILOVERICEBERGCATALOGREQUEST']._serialized_start = 2442
    _globals['_FAILOVERICEBERGCATALOGREQUEST']._serialized_end = 2630
    _globals['_FAILOVERICEBERGCATALOGRESPONSE']._serialized_start = 2632
    _globals['_FAILOVERICEBERGCATALOGRESPONSE']._serialized_end = 2723
    _globals['_UPDATEICEBERGTABLEREQUEST']._serialized_start = 2726
    _globals['_UPDATEICEBERGTABLEREQUEST']._serialized_end = 2860
    _globals['_GETICEBERGTABLEREQUEST']._serialized_start = 2862
    _globals['_GETICEBERGTABLEREQUEST']._serialized_end = 2962
    _globals['_DELETEICEBERGTABLEREQUEST']._serialized_start = 2964
    _globals['_DELETEICEBERGTABLEREQUEST']._serialized_end = 3073
    _globals['_CREATEICEBERGTABLEREQUEST']._serialized_start = 3076
    _globals['_CREATEICEBERGTABLEREQUEST']._serialized_end = 3207
    _globals['_LISTICEBERGTABLEIDENTIFIERSREQUEST']._serialized_start = 3210
    _globals['_LISTICEBERGTABLEIDENTIFIERSREQUEST']._serialized_end = 3353
    _globals['_TABLEIDENTIFIER']._serialized_start = 3355
    _globals['_TABLEIDENTIFIER']._serialized_end = 3444
    _globals['_LISTICEBERGTABLEIDENTIFIERSRESPONSE']._serialized_start = 3447
    _globals['_LISTICEBERGTABLEIDENTIFIERSRESPONSE']._serialized_end = 3599
    _globals['_ICEBERGNAMESPACEUPDATE']._serialized_start = 3602
    _globals['_ICEBERGNAMESPACEUPDATE']._serialized_end = 3781
    _globals['_ICEBERGNAMESPACEUPDATE_UPDATESENTRY']._serialized_start = 3735
    _globals['_ICEBERGNAMESPACEUPDATE_UPDATESENTRY']._serialized_end = 3781
    _globals['_UPDATEICEBERGNAMESPACEREQUEST']._serialized_start = 3784
    _globals['_UPDATEICEBERGNAMESPACEREQUEST']._serialized_end = 3959
    _globals['_UPDATEICEBERGNAMESPACERESPONSE']._serialized_start = 3961
    _globals['_UPDATEICEBERGNAMESPACERESPONSE']._serialized_end = 4066
    _globals['_DELETEICEBERGNAMESPACEREQUEST']._serialized_start = 4068
    _globals['_DELETEICEBERGNAMESPACEREQUEST']._serialized_end = 4155
    _globals['_ICEBERGNAMESPACE']._serialized_start = 4158
    _globals['_ICEBERGNAMESPACE']._serialized_end = 4335
    _globals['_ICEBERGNAMESPACE_PROPERTIESENTRY']._serialized_start = 4286
    _globals['_ICEBERGNAMESPACE_PROPERTIESENTRY']._serialized_end = 4335
    _globals['_CREATEICEBERGNAMESPACEREQUEST']._serialized_start = 4338
    _globals['_CREATEICEBERGNAMESPACEREQUEST']._serialized_end = 4511
    _globals['_GETICEBERGCATALOGCONFIGREQUEST']._serialized_start = 4513
    _globals['_GETICEBERGCATALOGCONFIGREQUEST']._serialized_end = 4569
    _globals['_ICEBERGCATALOGCONFIG']._serialized_start = 4572
    _globals['_ICEBERGCATALOGCONFIG']._serialized_end = 4887
    _globals['_ICEBERGCATALOGCONFIG_OVERRIDESENTRY']._serialized_start = 4790
    _globals['_ICEBERGCATALOGCONFIG_OVERRIDESENTRY']._serialized_end = 4838
    _globals['_ICEBERGCATALOGCONFIG_DEFAULTSENTRY']._serialized_start = 4840
    _globals['_ICEBERGCATALOGCONFIG_DEFAULTSENTRY']._serialized_end = 4887
    _globals['_GETICEBERGNAMESPACEREQUEST']._serialized_start = 4889
    _globals['_GETICEBERGNAMESPACEREQUEST']._serialized_end = 4973
    _globals['_LISTICEBERGNAMESPACESREQUEST']._serialized_start = 4975
    _globals['_LISTICEBERGNAMESPACESREQUEST']._serialized_end = 5100
    _globals['_LISTICEBERGNAMESPACESRESPONSE']._serialized_start = 5102
    _globals['_LISTICEBERGNAMESPACESRESPONSE']._serialized_end = 5223
    _globals['_STORAGECREDENTIAL']._serialized_start = 5226
    _globals['_STORAGECREDENTIAL']._serialized_end = 5380
    _globals['_STORAGECREDENTIAL_CONFIGENTRY']._serialized_start = 5335
    _globals['_STORAGECREDENTIAL_CONFIGENTRY']._serialized_end = 5380
    _globals['_LOADICEBERGTABLECREDENTIALSRESPONSE']._serialized_start = 5383
    _globals['_LOADICEBERGTABLECREDENTIALSRESPONSE']._serialized_end = 5514
    _globals['_ICEBERGCATALOGSERVICE']._serialized_start = 5517
    _globals['_ICEBERGCATALOGSERVICE']._serialized_end = 10127