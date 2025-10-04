"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/licensemanager/v1/licensemanager.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.licensemanager.v1 import api_entities_pb2 as google_dot_cloud_dot_licensemanager_dot_v1_dot_api__entities__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/licensemanager/v1/licensemanager.proto\x12\x1egoogle.cloud.licensemanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/licensemanager/v1/api_entities.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbd\x01\n\x19ListConfigurationsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+licensemanager.googleapis.com/Configuration\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x91\x01\n\x1aListConfigurationsResponse\x12E\n\x0econfigurations\x18\x01 \x03(\x0b2-.google.cloud.licensemanager.v1.Configuration\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\\\n\x17GetConfigurationRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+licensemanager.googleapis.com/Configuration"\xec\x01\n\x1aCreateConfigurationRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+licensemanager.googleapis.com/Configuration\x12\x1d\n\x10configuration_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12I\n\rconfiguration\x18\x03 \x01(\x0b2-.google.cloud.licensemanager.v1.ConfigurationB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xbe\x01\n\x1aUpdateConfigurationRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12I\n\rconfiguration\x18\x02 \x01(\x0b2-.google.cloud.licensemanager.v1.ConfigurationB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x80\x01\n\x1aDeleteConfigurationRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+licensemanager.googleapis.com/Configuration\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xb3\x01\n\x14ListInstancesRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&licensemanager.googleapis.com/Instance\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x82\x01\n\x15ListInstancesResponse\x12;\n\tinstances\x18\x01 \x03(\x0b2(.google.cloud.licensemanager.v1.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"R\n\x12GetInstanceRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&licensemanager.googleapis.com/Instance"\xd2\x01\n%QueryConfigurationLicenseUsageRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+licensemanager.googleapis.com/Configuration\x123\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"\x7f\n&QueryConfigurationLicenseUsageResponse\x12J\n\x10user_count_usage\x18\x01 \x01(\x0b2..google.cloud.licensemanager.v1.UserCountUsageH\x00B\t\n\x07details"\x84\x01\n\x1eDeactivateConfigurationRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+licensemanager.googleapis.com/Configuration\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x84\x01\n\x1eReactivateConfigurationRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+licensemanager.googleapis.com/Configuration\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x9f\x02\n\x15AggregateUsageRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+licensemanager.googleapis.com/Configuration\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x06 \x01(\tB\x03\xe0A\x01\x123\n\nstart_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x121\n\x08end_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"}\n\x16AggregateUsageResponse\x125\n\x06usages\x18\x01 \x03(\x0b2%.google.cloud.licensemanager.v1.Usage\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\xb1\x01\n\x13ListProductsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%licensemanager.googleapis.com/Product\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x7f\n\x14ListProductsResponse\x129\n\x08products\x18\x01 \x03(\x0b2\'.google.cloud.licensemanager.v1.Product\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"P\n\x11GetProductRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%licensemanager.googleapis.com/Product"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xa6\x17\n\x0eLicenseManager\x12\xd0\x01\n\x12ListConfigurations\x129.google.cloud.licensemanager.v1.ListConfigurationsRequest\x1a:.google.cloud.licensemanager.v1.ListConfigurationsResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/configurations\x12\xbd\x01\n\x10GetConfiguration\x127.google.cloud.licensemanager.v1.GetConfigurationRequest\x1a-.google.cloud.licensemanager.v1.Configuration"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/configurations/*}\x12\x89\x02\n\x13CreateConfiguration\x12:.google.cloud.licensemanager.v1.CreateConfigurationRequest\x1a\x1d.google.longrunning.Operation"\x96\x01\xcaA"\n\rConfiguration\x12\x11OperationMetadata\xdaA%parent,configuration,configuration_id\x82\xd3\xe4\x93\x02C"2/v1/{parent=projects/*/locations/*}/configurations:\rconfiguration\x12\x8b\x02\n\x13UpdateConfiguration\x12:.google.cloud.licensemanager.v1.UpdateConfigurationRequest\x1a\x1d.google.longrunning.Operation"\x98\x01\xcaA"\n\rConfiguration\x12\x11OperationMetadata\xdaA\x19configuration,update_mask\x82\xd3\xe4\x93\x02Q2@/v1/{configuration.name=projects/*/locations/*/configurations/*}:\rconfiguration\x12\xe0\x01\n\x13DeleteConfiguration\x12:.google.cloud.licensemanager.v1.DeleteConfigurationRequest\x1a\x1d.google.longrunning.Operation"n\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1/{name=projects/*/locations/*/configurations/*}\x12\xbc\x01\n\rListInstances\x124.google.cloud.licensemanager.v1.ListInstancesRequest\x1a5.google.cloud.licensemanager.v1.ListInstancesResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/instances\x12\xa9\x01\n\x0bGetInstance\x122.google.cloud.licensemanager.v1.GetInstanceRequest\x1a(.google.cloud.licensemanager.v1.Instance"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}\x12\xee\x01\n\x17DeactivateConfiguration\x12>.google.cloud.licensemanager.v1.DeactivateConfigurationRequest\x1a\x1d.google.longrunning.Operation"t\xcaA"\n\rConfiguration\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02B"=/v1/{name=projects/*/locations/*/configurations/*}:deactivate:\x01*\x12\xee\x01\n\x17ReactivateConfiguration\x12>.google.cloud.licensemanager.v1.ReactivateConfigurationRequest\x1a\x1d.google.longrunning.Operation"t\xcaA"\n\rConfiguration\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02B"=/v1/{name=projects/*/locations/*/configurations/*}:reactivate:\x01*\x12\x98\x02\n\x1eQueryConfigurationLicenseUsage\x12E.google.cloud.licensemanager.v1.QueryConfigurationLicenseUsageRequest\x1aF.google.cloud.licensemanager.v1.QueryConfigurationLicenseUsageResponse"g\xdaA\x18name,start_time,end_time\x82\xd3\xe4\x93\x02F\x12D/v1/{name=projects/*/locations/*/configurations/*}:queryLicenseUsage\x12\xe5\x01\n\x0eAggregateUsage\x125.google.cloud.licensemanager.v1.AggregateUsageRequest\x1a6.google.cloud.licensemanager.v1.AggregateUsageResponse"d\xdaA\x18name,start_time,end_time\x82\xd3\xe4\x93\x02C\x12A/v1/{name=projects/*/locations/*/configurations/*}:aggregateUsage\x12\xb8\x01\n\x0cListProducts\x123.google.cloud.licensemanager.v1.ListProductsRequest\x1a4.google.cloud.licensemanager.v1.ListProductsResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/products\x12\xa5\x01\n\nGetProduct\x121.google.cloud.licensemanager.v1.GetProductRequest\x1a\'.google.cloud.licensemanager.v1.Product";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/products/*}\x1aQ\xcaA\x1dlicensemanager.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xce\x02\n"com.google.cloud.licensemanager.v1B\x13LicenseManagerProtoP\x01ZJcloud.google.com/go/licensemanager/apiv1/licensemanagerpb;licensemanagerpb\xaa\x02\x1eGoogle.Cloud.LicenseManager.V1\xca\x02\x1eGoogle\\Cloud\\LicenseManager\\V1\xea\x02!Google::Cloud::LicenseManager::V1\xeaA^\n&compute.googleapis.com/ComputeInstance\x124projects/{project}/zones/{zone}/instances/{instance}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.licensemanager.v1.licensemanager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.licensemanager.v1B\x13LicenseManagerProtoP\x01ZJcloud.google.com/go/licensemanager/apiv1/licensemanagerpb;licensemanagerpb\xaa\x02\x1eGoogle.Cloud.LicenseManager.V1\xca\x02\x1eGoogle\\Cloud\\LicenseManager\\V1\xea\x02!Google::Cloud::LicenseManager::V1\xeaA^\n&compute.googleapis.com/ComputeInstance\x124projects/{project}/zones/{zone}/instances/{instance}'
    _globals['_LISTCONFIGURATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONFIGURATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+licensemanager.googleapis.com/Configuration'
    _globals['_LISTCONFIGURATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONFIGURATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONFIGURATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONFIGURATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONFIGURATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCONFIGURATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONFIGURATIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTCONFIGURATIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETCONFIGURATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONFIGURATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+licensemanager.googleapis.com/Configuration'
    _globals['_CREATECONFIGURATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONFIGURATIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+licensemanager.googleapis.com/Configuration'
    _globals['_CREATECONFIGURATIONREQUEST'].fields_by_name['configuration_id']._loaded_options = None
    _globals['_CREATECONFIGURATIONREQUEST'].fields_by_name['configuration_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONFIGURATIONREQUEST'].fields_by_name['configuration']._loaded_options = None
    _globals['_CREATECONFIGURATIONREQUEST'].fields_by_name['configuration']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONFIGURATIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATECONFIGURATIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_UPDATECONFIGURATIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONFIGURATIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATECONFIGURATIONREQUEST'].fields_by_name['configuration']._loaded_options = None
    _globals['_UPDATECONFIGURATIONREQUEST'].fields_by_name['configuration']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONFIGURATIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATECONFIGURATIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_DELETECONFIGURATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONFIGURATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+licensemanager.googleapis.com/Configuration'
    _globals['_DELETECONFIGURATIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETECONFIGURATIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&licensemanager.googleapis.com/Instance'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&licensemanager.googleapis.com/Instance'
    _globals['_QUERYCONFIGURATIONLICENSEUSAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_QUERYCONFIGURATIONLICENSEUSAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+licensemanager.googleapis.com/Configuration'
    _globals['_QUERYCONFIGURATIONLICENSEUSAGEREQUEST'].fields_by_name['start_time']._loaded_options = None
    _globals['_QUERYCONFIGURATIONLICENSEUSAGEREQUEST'].fields_by_name['start_time']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYCONFIGURATIONLICENSEUSAGEREQUEST'].fields_by_name['end_time']._loaded_options = None
    _globals['_QUERYCONFIGURATIONLICENSEUSAGEREQUEST'].fields_by_name['end_time']._serialized_options = b'\xe0A\x02'
    _globals['_DEACTIVATECONFIGURATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DEACTIVATECONFIGURATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+licensemanager.googleapis.com/Configuration'
    _globals['_DEACTIVATECONFIGURATIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DEACTIVATECONFIGURATIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_REACTIVATECONFIGURATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REACTIVATECONFIGURATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+licensemanager.googleapis.com/Configuration'
    _globals['_REACTIVATECONFIGURATIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_REACTIVATECONFIGURATIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+licensemanager.googleapis.com/Configuration'
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['start_time']._loaded_options = None
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['start_time']._serialized_options = b'\xe0A\x02'
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['end_time']._loaded_options = None
    _globals['_AGGREGATEUSAGEREQUEST'].fields_by_name['end_time']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%licensemanager.googleapis.com/Product"
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTPRODUCTSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETPRODUCTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPRODUCTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%licensemanager.googleapis.com/Product"
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_LICENSEMANAGER']._loaded_options = None
    _globals['_LICENSEMANAGER']._serialized_options = b'\xcaA\x1dlicensemanager.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_LICENSEMANAGER'].methods_by_name['ListConfigurations']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['ListConfigurations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/configurations'
    _globals['_LICENSEMANAGER'].methods_by_name['GetConfiguration']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['GetConfiguration']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/configurations/*}'
    _globals['_LICENSEMANAGER'].methods_by_name['CreateConfiguration']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['CreateConfiguration']._serialized_options = b'\xcaA"\n\rConfiguration\x12\x11OperationMetadata\xdaA%parent,configuration,configuration_id\x82\xd3\xe4\x93\x02C"2/v1/{parent=projects/*/locations/*}/configurations:\rconfiguration'
    _globals['_LICENSEMANAGER'].methods_by_name['UpdateConfiguration']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['UpdateConfiguration']._serialized_options = b'\xcaA"\n\rConfiguration\x12\x11OperationMetadata\xdaA\x19configuration,update_mask\x82\xd3\xe4\x93\x02Q2@/v1/{configuration.name=projects/*/locations/*/configurations/*}:\rconfiguration'
    _globals['_LICENSEMANAGER'].methods_by_name['DeleteConfiguration']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['DeleteConfiguration']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1/{name=projects/*/locations/*/configurations/*}'
    _globals['_LICENSEMANAGER'].methods_by_name['ListInstances']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['ListInstances']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/instances'
    _globals['_LICENSEMANAGER'].methods_by_name['GetInstance']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['GetInstance']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}'
    _globals['_LICENSEMANAGER'].methods_by_name['DeactivateConfiguration']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['DeactivateConfiguration']._serialized_options = b'\xcaA"\n\rConfiguration\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02B"=/v1/{name=projects/*/locations/*/configurations/*}:deactivate:\x01*'
    _globals['_LICENSEMANAGER'].methods_by_name['ReactivateConfiguration']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['ReactivateConfiguration']._serialized_options = b'\xcaA"\n\rConfiguration\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02B"=/v1/{name=projects/*/locations/*/configurations/*}:reactivate:\x01*'
    _globals['_LICENSEMANAGER'].methods_by_name['QueryConfigurationLicenseUsage']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['QueryConfigurationLicenseUsage']._serialized_options = b'\xdaA\x18name,start_time,end_time\x82\xd3\xe4\x93\x02F\x12D/v1/{name=projects/*/locations/*/configurations/*}:queryLicenseUsage'
    _globals['_LICENSEMANAGER'].methods_by_name['AggregateUsage']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['AggregateUsage']._serialized_options = b'\xdaA\x18name,start_time,end_time\x82\xd3\xe4\x93\x02C\x12A/v1/{name=projects/*/locations/*/configurations/*}:aggregateUsage'
    _globals['_LICENSEMANAGER'].methods_by_name['ListProducts']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['ListProducts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/products'
    _globals['_LICENSEMANAGER'].methods_by_name['GetProduct']._loaded_options = None
    _globals['_LICENSEMANAGER'].methods_by_name['GetProduct']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/products/*}'
    _globals['_LISTCONFIGURATIONSREQUEST']._serialized_start = 416
    _globals['_LISTCONFIGURATIONSREQUEST']._serialized_end = 605
    _globals['_LISTCONFIGURATIONSRESPONSE']._serialized_start = 608
    _globals['_LISTCONFIGURATIONSRESPONSE']._serialized_end = 753
    _globals['_GETCONFIGURATIONREQUEST']._serialized_start = 755
    _globals['_GETCONFIGURATIONREQUEST']._serialized_end = 847
    _globals['_CREATECONFIGURATIONREQUEST']._serialized_start = 850
    _globals['_CREATECONFIGURATIONREQUEST']._serialized_end = 1086
    _globals['_UPDATECONFIGURATIONREQUEST']._serialized_start = 1089
    _globals['_UPDATECONFIGURATIONREQUEST']._serialized_end = 1279
    _globals['_DELETECONFIGURATIONREQUEST']._serialized_start = 1282
    _globals['_DELETECONFIGURATIONREQUEST']._serialized_end = 1410
    _globals['_LISTINSTANCESREQUEST']._serialized_start = 1413
    _globals['_LISTINSTANCESREQUEST']._serialized_end = 1592
    _globals['_LISTINSTANCESRESPONSE']._serialized_start = 1595
    _globals['_LISTINSTANCESRESPONSE']._serialized_end = 1725
    _globals['_GETINSTANCEREQUEST']._serialized_start = 1727
    _globals['_GETINSTANCEREQUEST']._serialized_end = 1809
    _globals['_QUERYCONFIGURATIONLICENSEUSAGEREQUEST']._serialized_start = 1812
    _globals['_QUERYCONFIGURATIONLICENSEUSAGEREQUEST']._serialized_end = 2022
    _globals['_QUERYCONFIGURATIONLICENSEUSAGERESPONSE']._serialized_start = 2024
    _globals['_QUERYCONFIGURATIONLICENSEUSAGERESPONSE']._serialized_end = 2151
    _globals['_DEACTIVATECONFIGURATIONREQUEST']._serialized_start = 2154
    _globals['_DEACTIVATECONFIGURATIONREQUEST']._serialized_end = 2286
    _globals['_REACTIVATECONFIGURATIONREQUEST']._serialized_start = 2289
    _globals['_REACTIVATECONFIGURATIONREQUEST']._serialized_end = 2421
    _globals['_AGGREGATEUSAGEREQUEST']._serialized_start = 2424
    _globals['_AGGREGATEUSAGEREQUEST']._serialized_end = 2711
    _globals['_AGGREGATEUSAGERESPONSE']._serialized_start = 2713
    _globals['_AGGREGATEUSAGERESPONSE']._serialized_end = 2838
    _globals['_LISTPRODUCTSREQUEST']._serialized_start = 2841
    _globals['_LISTPRODUCTSREQUEST']._serialized_end = 3018
    _globals['_LISTPRODUCTSRESPONSE']._serialized_start = 3020
    _globals['_LISTPRODUCTSRESPONSE']._serialized_end = 3147
    _globals['_GETPRODUCTREQUEST']._serialized_start = 3149
    _globals['_GETPRODUCTREQUEST']._serialized_end = 3229
    _globals['_OPERATIONMETADATA']._serialized_start = 3232
    _globals['_OPERATIONMETADATA']._serialized_end = 3488
    _globals['_LICENSEMANAGER']._serialized_start = 3491
    _globals['_LICENSEMANAGER']._serialized_end = 6473