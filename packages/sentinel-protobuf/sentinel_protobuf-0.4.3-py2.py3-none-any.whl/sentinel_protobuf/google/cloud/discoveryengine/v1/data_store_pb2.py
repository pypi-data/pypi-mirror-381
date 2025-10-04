"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/data_store.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import cmek_config_service_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_cmek__config__service__pb2
from .....google.cloud.discoveryengine.v1 import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_common__pb2
from .....google.cloud.discoveryengine.v1 import document_processing_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_document__processing__config__pb2
from .....google.cloud.discoveryengine.v1 import schema_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_schema__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/discoveryengine/v1/data_store.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a9google/cloud/discoveryengine/v1/cmek_config_service.proto\x1a,google/cloud/discoveryengine/v1/common.proto\x1a@google/cloud/discoveryengine/v1/document_processing_config.proto\x1a,google/cloud/discoveryengine/v1/schema.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe7\r\n\tDataStore\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x05\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12Q\n\x11industry_vertical\x18\x03 \x01(\x0e21.google.cloud.discoveryengine.v1.IndustryVerticalB\x03\xe0A\x05\x12E\n\x0esolution_types\x18\x05 \x03(\x0e2-.google.cloud.discoveryengine.v1.SolutionType\x12\x1e\n\x11default_schema_id\x18\x07 \x01(\tB\x03\xe0A\x03\x12U\n\x0econtent_config\x18\x06 \x01(\x0e28.google.cloud.discoveryengine.v1.DataStore.ContentConfigB\x03\xe0A\x05\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12c\n\x1badvanced_site_search_config\x18\x0c \x01(\x0b29.google.cloud.discoveryengine.v1.AdvancedSiteSearchConfigB\x03\xe0A\x01\x12\x19\n\x0ckms_key_name\x18  \x01(\tB\x03\xe0A\x04\x12E\n\x0bcmek_config\x18\x12 \x01(\x0b2+.google.cloud.discoveryengine.v1.CmekConfigB\x03\xe0A\x03\x12]\n\x12billing_estimation\x18\x17 \x01(\x0b2<.google.cloud.discoveryengine.v1.DataStore.BillingEstimationB\x03\xe0A\x03\x12\x18\n\x0bacl_enabled\x18\x18 \x01(\x08B\x03\xe0A\x05\x12J\n\x10workspace_config\x18\x19 \x01(\x0b20.google.cloud.discoveryengine.v1.WorkspaceConfig\x12]\n\x1adocument_processing_config\x18\x1b \x01(\x0b29.google.cloud.discoveryengine.v1.DocumentProcessingConfig\x12@\n\x0fstarting_schema\x18\x1c \x01(\x0b2\'.google.cloud.discoveryengine.v1.Schema\x12Z\n\x16healthcare_fhir_config\x18\x1d \x01(\x0b25.google.cloud.discoveryengine.v1.HealthcareFhirConfigB\x03\xe0A\x01\x12[\n\x16identity_mapping_store\x18\x1f \x01(\tB;\xe0A\x05\xfaA5\n3discoveryengine.googleapis.com/IdentityMappingStore\x1a\xae\x02\n\x11BillingEstimation\x12\x1c\n\x14structured_data_size\x18\x01 \x01(\x03\x12\x1e\n\x16unstructured_data_size\x18\x02 \x01(\x03\x12\x19\n\x11website_data_size\x18\x03 \x01(\x03\x12?\n\x1bstructured_data_update_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12A\n\x1dunstructured_data_update_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12<\n\x18website_data_update_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x7f\n\rContentConfig\x12\x1e\n\x1aCONTENT_CONFIG_UNSPECIFIED\x10\x00\x12\x0e\n\nNO_CONTENT\x10\x01\x12\x14\n\x10CONTENT_REQUIRED\x10\x02\x12\x12\n\x0ePUBLIC_WEBSITE\x10\x03\x12\x14\n\x10GOOGLE_WORKSPACE\x10\x04:\xc9\x01\xeaA\xc5\x01\n(discoveryengine.googleapis.com/DataStore\x12?projects/{project}/locations/{location}/dataStores/{data_store}\x12Xprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}"\x9e\x01\n\x18AdvancedSiteSearchConfig\x12"\n\x15disable_initial_index\x18\x03 \x01(\x08H\x00\x88\x01\x01\x12&\n\x19disable_automatic_refresh\x18\x04 \x01(\x08H\x01\x88\x01\x01B\x18\n\x16_disable_initial_indexB\x1c\n\x1a_disable_automatic_refresh"\xf5\x02\n\x0fWorkspaceConfig\x12C\n\x04type\x18\x01 \x01(\x0e25.google.cloud.discoveryengine.v1.WorkspaceConfig.Type\x12\x1a\n\x12dasher_customer_id\x18\x02 \x01(\t\x12(\n\x1bsuper_admin_service_account\x18\x04 \x01(\tB\x03\xe0A\x01\x12&\n\x19super_admin_email_address\x18\x05 \x01(\tB\x03\xe0A\x01"\xae\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cGOOGLE_DRIVE\x10\x01\x12\x0f\n\x0bGOOGLE_MAIL\x10\x02\x12\x10\n\x0cGOOGLE_SITES\x10\x03\x12\x13\n\x0fGOOGLE_CALENDAR\x10\x04\x12\x0f\n\x0bGOOGLE_CHAT\x10\x05\x12\x11\n\rGOOGLE_GROUPS\x10\x06\x12\x0f\n\x0bGOOGLE_KEEP\x10\x07\x12\x11\n\rGOOGLE_PEOPLE\x10\x08B\x81\x02\n#com.google.cloud.discoveryengine.v1B\x0eDataStoreProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.data_store_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x0eDataStoreProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_DATASTORE'].fields_by_name['name']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['name']._serialized_options = b'\xe0A\x05\xe0A\x08'
    _globals['_DATASTORE'].fields_by_name['display_name']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_DATASTORE'].fields_by_name['industry_vertical']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['industry_vertical']._serialized_options = b'\xe0A\x05'
    _globals['_DATASTORE'].fields_by_name['default_schema_id']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['default_schema_id']._serialized_options = b'\xe0A\x03'
    _globals['_DATASTORE'].fields_by_name['content_config']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['content_config']._serialized_options = b'\xe0A\x05'
    _globals['_DATASTORE'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASTORE'].fields_by_name['advanced_site_search_config']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['advanced_site_search_config']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORE'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['kms_key_name']._serialized_options = b'\xe0A\x04'
    _globals['_DATASTORE'].fields_by_name['cmek_config']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['cmek_config']._serialized_options = b'\xe0A\x03'
    _globals['_DATASTORE'].fields_by_name['billing_estimation']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['billing_estimation']._serialized_options = b'\xe0A\x03'
    _globals['_DATASTORE'].fields_by_name['acl_enabled']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['acl_enabled']._serialized_options = b'\xe0A\x05'
    _globals['_DATASTORE'].fields_by_name['healthcare_fhir_config']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['healthcare_fhir_config']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORE'].fields_by_name['identity_mapping_store']._loaded_options = None
    _globals['_DATASTORE'].fields_by_name['identity_mapping_store']._serialized_options = b'\xe0A\x05\xfaA5\n3discoveryengine.googleapis.com/IdentityMappingStore'
    _globals['_DATASTORE']._loaded_options = None
    _globals['_DATASTORE']._serialized_options = b'\xeaA\xc5\x01\n(discoveryengine.googleapis.com/DataStore\x12?projects/{project}/locations/{location}/dataStores/{data_store}\x12Xprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}'
    _globals['_WORKSPACECONFIG'].fields_by_name['super_admin_service_account']._loaded_options = None
    _globals['_WORKSPACECONFIG'].fields_by_name['super_admin_service_account']._serialized_options = b'\xe0A\x01'
    _globals['_WORKSPACECONFIG'].fields_by_name['super_admin_email_address']._loaded_options = None
    _globals['_WORKSPACECONFIG'].fields_by_name['super_admin_email_address']._serialized_options = b'\xe0A\x01'
    _globals['_DATASTORE']._serialized_start = 396
    _globals['_DATASTORE']._serialized_end = 2163
    _globals['_DATASTORE_BILLINGESTIMATION']._serialized_start = 1528
    _globals['_DATASTORE_BILLINGESTIMATION']._serialized_end = 1830
    _globals['_DATASTORE_CONTENTCONFIG']._serialized_start = 1832
    _globals['_DATASTORE_CONTENTCONFIG']._serialized_end = 1959
    _globals['_ADVANCEDSITESEARCHCONFIG']._serialized_start = 2166
    _globals['_ADVANCEDSITESEARCHCONFIG']._serialized_end = 2324
    _globals['_WORKSPACECONFIG']._serialized_start = 2327
    _globals['_WORKSPACECONFIG']._serialized_end = 2700
    _globals['_WORKSPACECONFIG_TYPE']._serialized_start = 2526
    _globals['_WORKSPACECONFIG_TYPE']._serialized_end = 2700