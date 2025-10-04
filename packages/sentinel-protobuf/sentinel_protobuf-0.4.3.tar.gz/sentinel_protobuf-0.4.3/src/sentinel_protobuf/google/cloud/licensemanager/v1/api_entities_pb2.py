"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/licensemanager/v1/api_entities.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/licensemanager/v1/api_entities.proto\x12\x1egoogle.cloud.licensemanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8b\x07\n\rConfiguration\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x02\x12>\n\x07product\x18\x06 \x01(\tB-\xe0A\x02\xfaA\'\n%licensemanager.googleapis.com/Product\x12F\n\x0clicense_type\x18\x07 \x01(\x0e2+.google.cloud.licensemanager.v1.LicenseTypeB\x03\xe0A\x02\x12N\n\x14current_billing_info\x18\x08 \x01(\x0b2+.google.cloud.licensemanager.v1.BillingInfoB\x03\xe0A\x02\x12K\n\x11next_billing_info\x18\t \x01(\x0b2+.google.cloud.licensemanager.v1.BillingInfoB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12N\n\x06labels\x18\x04 \x03(\x0b29.google.cloud.licensemanager.v1.Configuration.LabelsEntryB\x03\xe0A\x01\x12G\n\x05state\x18\n \x01(\x0e23.google.cloud.licensemanager.v1.Configuration.StateB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"X\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cSTATE_ACTIVE\x10\x01\x12\x13\n\x0fSTATE_SUSPENDED\x10\x02\x12\x11\n\rSTATE_DELETED\x10\x03:\x98\x01\xeaA\x94\x01\n+licensemanager.googleapis.com/Configuration\x12Fprojects/{project}/locations/{location}/configurations/{configuration}*\x0econfigurations2\rconfiguration"\xe6\x01\n\x0bBillingInfo\x12W\n\x12user_count_billing\x18\x01 \x01(\x0b24.google.cloud.licensemanager.v1.UserCountBillingInfoB\x03\xe0A\x02H\x00\x123\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03B\x16\n\x14current_billing_info"/\n\x14UserCountBillingInfo\x12\x17\n\nuser_count\x18\x01 \x01(\x05B\x03\xe0A\x02"0\n\x0eUserCountUsage\x12\x1e\n\x11unique_user_count\x18\x01 \x01(\x05B\x03\xe0A\x02"\xcd\x03\n\x07Product\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x07version\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0fproduct_company\x18\x03 \x01(\tB\x03\xe0A\x02\x12A\n\x05state\x18\x04 \x01(\x0e2-.google.cloud.licensemanager.v1.Product.StateB\x03\xe0A\x03\x12\x10\n\x03sku\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cdisplay_name\x18\x07 \x01(\tB\x03\xe0A\x02"v\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x16\n\x12STATE_PROVISIONING\x10\x01\x12\x11\n\rSTATE_RUNNING\x10\x02\x12\x15\n\x11STATE_TERMINATING\x10\x03\x12\x14\n\x10STATE_TERMINATED\x10\x04:y\xeaAv\n%licensemanager.googleapis.com/Product\x12:projects/{project}/locations/{location}/products/{product}*\x08products2\x07product"\x9b\x07\n\x08Instance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12I\n\x06labels\x18\x04 \x03(\x0b24.google.cloud.licensemanager.v1.Instance.LabelsEntryB\x03\xe0A\x01\x12B\n\x05state\x18\x05 \x01(\x0e2..google.cloud.licensemanager.v1.Instance.StateB\x03\xe0A\x03\x12\x13\n\x06region\x18\x06 \x01(\tB\x03\xe0A\x03\x12`\n\x12product_activation\x18\x07 \x03(\x0b2?.google.cloud.licensemanager.v1.Instance.ProductActivationEntryB\x03\xe0A\x03\x12\x1f\n\x12license_version_id\x18\x08 \x01(\tB\x03\xe0A\x03\x12H\n\x10compute_instance\x18\t \x01(\tB.\xe0A\x02\xfaA(\n&compute.googleapis.com/ComputeInstance\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1ai\n\x16ProductActivationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12>\n\x05value\x18\x02 \x01(\x0e2/.google.cloud.licensemanager.v1.ActivationState:\x028\x01"\x84\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0b\n\x07STAGING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\x0e\n\nTERMINATED\x10\x06\x12\r\n\tREPAIRING\x10\x07:~\xeaA{\n&licensemanager.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}*\tinstances2\x08instance"Z\n\x05Usage\x12B\n\rlima_instance\x18\x01 \x01(\tB+\xfaA(\n&licensemanager.googleapis.com/Instance\x12\r\n\x05users\x18\x02 \x01(\x05*y\n\x0bLicenseType\x12\x1c\n\x18LICENSE_TYPE_UNSPECIFIED\x10\x00\x12#\n\x1fLICENSE_TYPE_PER_MONTH_PER_USER\x10\x01\x12\'\n#LICENSE_TYPE_BRING_YOUR_OWN_LICENSE\x10\x02*\xfe\x01\n\x0fActivationState\x12 \n\x1cACTIVATION_STATE_UNSPECIFIED\x10\x00\x12"\n\x1eACTIVATION_STATE_KEY_REQUESTED\x10\x01\x12\x1f\n\x1bACTIVATION_STATE_ACTIVATING\x10\x02\x12\x1e\n\x1aACTIVATION_STATE_ACTIVATED\x10\x03\x12!\n\x1dACTIVATION_STATE_DEACTIVATING\x10\x04\x12 \n\x1cACTIVATION_STATE_DEACTIVATED\x10\x05\x12\x1f\n\x1bACTIVATION_STATE_TERMINATED\x10\x06B\xea\x01\n"com.google.cloud.licensemanager.v1B\x10ApiEntitiesProtoP\x01ZJcloud.google.com/go/licensemanager/apiv1/licensemanagerpb;licensemanagerpb\xaa\x02\x1eGoogle.Cloud.LicenseManager.V1\xca\x02\x1eGoogle\\Cloud\\LicenseManager\\V1\xea\x02!Google::Cloud::LicenseManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.licensemanager.v1.api_entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.licensemanager.v1B\x10ApiEntitiesProtoP\x01ZJcloud.google.com/go/licensemanager/apiv1/licensemanagerpb;licensemanagerpb\xaa\x02\x1eGoogle.Cloud.LicenseManager.V1\xca\x02\x1eGoogle\\Cloud\\LicenseManager\\V1\xea\x02!Google::Cloud::LicenseManager::V1'
    _globals['_CONFIGURATION_LABELSENTRY']._loaded_options = None
    _globals['_CONFIGURATION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CONFIGURATION'].fields_by_name['name']._loaded_options = None
    _globals['_CONFIGURATION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CONFIGURATION'].fields_by_name['display_name']._loaded_options = None
    _globals['_CONFIGURATION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CONFIGURATION'].fields_by_name['product']._loaded_options = None
    _globals['_CONFIGURATION'].fields_by_name['product']._serialized_options = b"\xe0A\x02\xfaA'\n%licensemanager.googleapis.com/Product"
    _globals['_CONFIGURATION'].fields_by_name['license_type']._loaded_options = None
    _globals['_CONFIGURATION'].fields_by_name['license_type']._serialized_options = b'\xe0A\x02'
    _globals['_CONFIGURATION'].fields_by_name['current_billing_info']._loaded_options = None
    _globals['_CONFIGURATION'].fields_by_name['current_billing_info']._serialized_options = b'\xe0A\x02'
    _globals['_CONFIGURATION'].fields_by_name['next_billing_info']._loaded_options = None
    _globals['_CONFIGURATION'].fields_by_name['next_billing_info']._serialized_options = b'\xe0A\x02'
    _globals['_CONFIGURATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_CONFIGURATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONFIGURATION'].fields_by_name['update_time']._loaded_options = None
    _globals['_CONFIGURATION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONFIGURATION'].fields_by_name['labels']._loaded_options = None
    _globals['_CONFIGURATION'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_CONFIGURATION'].fields_by_name['state']._loaded_options = None
    _globals['_CONFIGURATION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CONFIGURATION']._loaded_options = None
    _globals['_CONFIGURATION']._serialized_options = b'\xeaA\x94\x01\n+licensemanager.googleapis.com/Configuration\x12Fprojects/{project}/locations/{location}/configurations/{configuration}*\x0econfigurations2\rconfiguration'
    _globals['_BILLINGINFO'].fields_by_name['user_count_billing']._loaded_options = None
    _globals['_BILLINGINFO'].fields_by_name['user_count_billing']._serialized_options = b'\xe0A\x02'
    _globals['_BILLINGINFO'].fields_by_name['start_time']._loaded_options = None
    _globals['_BILLINGINFO'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_BILLINGINFO'].fields_by_name['end_time']._loaded_options = None
    _globals['_BILLINGINFO'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_USERCOUNTBILLINGINFO'].fields_by_name['user_count']._loaded_options = None
    _globals['_USERCOUNTBILLINGINFO'].fields_by_name['user_count']._serialized_options = b'\xe0A\x02'
    _globals['_USERCOUNTUSAGE'].fields_by_name['unique_user_count']._loaded_options = None
    _globals['_USERCOUNTUSAGE'].fields_by_name['unique_user_count']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCT'].fields_by_name['name']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PRODUCT'].fields_by_name['version']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['version']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCT'].fields_by_name['product_company']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['product_company']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCT'].fields_by_name['state']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCT'].fields_by_name['sku']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['sku']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCT'].fields_by_name['description']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['description']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCT'].fields_by_name['display_name']._loaded_options = None
    _globals['_PRODUCT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCT']._loaded_options = None
    _globals['_PRODUCT']._serialized_options = b'\xeaAv\n%licensemanager.googleapis.com/Product\x12:projects/{project}/locations/{location}/products/{product}*\x08products2\x07product'
    _globals['_INSTANCE_LABELSENTRY']._loaded_options = None
    _globals['_INSTANCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE_PRODUCTACTIVATIONENTRY']._loaded_options = None
    _globals['_INSTANCE_PRODUCTACTIVATIONENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_INSTANCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['labels']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE'].fields_by_name['state']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['region']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['region']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['product_activation']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['product_activation']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['license_version_id']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['license_version_id']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['compute_instance']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['compute_instance']._serialized_options = b'\xe0A\x02\xfaA(\n&compute.googleapis.com/ComputeInstance'
    _globals['_INSTANCE']._loaded_options = None
    _globals['_INSTANCE']._serialized_options = b'\xeaA{\n&licensemanager.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}*\tinstances2\x08instance'
    _globals['_USAGE'].fields_by_name['lima_instance']._loaded_options = None
    _globals['_USAGE'].fields_by_name['lima_instance']._serialized_options = b'\xfaA(\n&licensemanager.googleapis.com/Instance'
    _globals['_LICENSETYPE']._serialized_start = 2902
    _globals['_LICENSETYPE']._serialized_end = 3023
    _globals['_ACTIVATIONSTATE']._serialized_start = 3026
    _globals['_ACTIVATIONSTATE']._serialized_end = 3280
    _globals['_CONFIGURATION']._serialized_start = 179
    _globals['_CONFIGURATION']._serialized_end = 1086
    _globals['_CONFIGURATION_LABELSENTRY']._serialized_start = 796
    _globals['_CONFIGURATION_LABELSENTRY']._serialized_end = 841
    _globals['_CONFIGURATION_STATE']._serialized_start = 843
    _globals['_CONFIGURATION_STATE']._serialized_end = 931
    _globals['_BILLINGINFO']._serialized_start = 1089
    _globals['_BILLINGINFO']._serialized_end = 1319
    _globals['_USERCOUNTBILLINGINFO']._serialized_start = 1321
    _globals['_USERCOUNTBILLINGINFO']._serialized_end = 1368
    _globals['_USERCOUNTUSAGE']._serialized_start = 1370
    _globals['_USERCOUNTUSAGE']._serialized_end = 1418
    _globals['_PRODUCT']._serialized_start = 1421
    _globals['_PRODUCT']._serialized_end = 1882
    _globals['_PRODUCT_STATE']._serialized_start = 1641
    _globals['_PRODUCT_STATE']._serialized_end = 1759
    _globals['_INSTANCE']._serialized_start = 1885
    _globals['_INSTANCE']._serialized_end = 2808
    _globals['_INSTANCE_LABELSENTRY']._serialized_start = 796
    _globals['_INSTANCE_LABELSENTRY']._serialized_end = 841
    _globals['_INSTANCE_PRODUCTACTIVATIONENTRY']._serialized_start = 2440
    _globals['_INSTANCE_PRODUCTACTIVATIONENTRY']._serialized_end = 2545
    _globals['_INSTANCE_STATE']._serialized_start = 2548
    _globals['_INSTANCE_STATE']._serialized_end = 2680
    _globals['_USAGE']._serialized_start = 2810
    _globals['_USAGE']._serialized_end = 2900