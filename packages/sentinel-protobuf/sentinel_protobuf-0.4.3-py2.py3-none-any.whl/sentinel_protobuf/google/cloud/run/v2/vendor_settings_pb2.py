"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/run/v2/vendor_settings.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/run/v2/vendor_settings.proto\x12\x13google.cloud.run.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x81\x03\n\tVpcAccess\x12:\n\tconnector\x18\x01 \x01(\tB\'\xfaA$\n"vpcaccess.googleapis.com/Connector\x12=\n\x06egress\x18\x02 \x01(\x0e2(.google.cloud.run.v2.VpcAccess.VpcEgressB\x03\xe0A\x01\x12P\n\x12network_interfaces\x18\x03 \x03(\x0b2/.google.cloud.run.v2.VpcAccess.NetworkInterfaceB\x03\xe0A\x01\x1aT\n\x10NetworkInterface\x12\x14\n\x07network\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x17\n\nsubnetwork\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04tags\x18\x03 \x03(\tB\x03\xe0A\x01"Q\n\tVpcEgress\x12\x1a\n\x16VPC_EGRESS_UNSPECIFIED\x10\x00\x12\x0f\n\x0bALL_TRAFFIC\x10\x01\x12\x17\n\x13PRIVATE_RANGES_ONLY\x10\x02"\xb0\x01\n\x13BinaryAuthorization\x12\x1a\n\x0buse_default\x18\x01 \x01(\x08B\x03\xe0A\x01H\x00\x12C\n\x06policy\x18\x03 \x01(\tB1\xe0A\x01\xfaA+\n)binaryauthorization.googleapis.com/PolicyH\x00\x12%\n\x18breakglass_justification\x18\x02 \x01(\tB\x03\xe0A\x01B\x11\n\x0fbinauthz_method"S\n\x0fRevisionScaling\x12\x1f\n\x12min_instance_count\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x1f\n\x12max_instance_count\x18\x02 \x01(\x05B\x03\xe0A\x01"E\n\x0bServiceMesh\x126\n\x04mesh\x18\x01 \x01(\tB(\xfaA%\n#networkservices.googleapis.com/Mesh"\x88\x02\n\x0eServiceScaling\x12\x1f\n\x12min_instance_count\x18\x01 \x01(\x05B\x03\xe0A\x01\x12J\n\x0cscaling_mode\x18\x03 \x01(\x0e2/.google.cloud.run.v2.ServiceScaling.ScalingModeB\x03\xe0A\x01\x12\'\n\x15manual_instance_count\x18\x06 \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01"F\n\x0bScalingMode\x12\x1c\n\x18SCALING_MODE_UNSPECIFIED\x10\x00\x12\r\n\tAUTOMATIC\x10\x01\x12\n\n\x06MANUAL\x10\x02B\x18\n\x16_manual_instance_count"V\n\x11WorkerPoolScaling\x12\'\n\x15manual_instance_count\x18\x06 \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01B\x18\n\x16_manual_instance_count"(\n\x0cNodeSelector\x12\x18\n\x0baccelerator\x18\x01 \x01(\tB\x03\xe0A\x02"\xd6\x03\n\x0bBuildConfig\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x03\xfaA!\n\x1fcloudbuild.googleapis.com/Build\x12\x17\n\x0fsource_location\x18\x02 \x01(\t\x12\x1c\n\x0ffunction_target\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x16\n\timage_uri\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x17\n\nbase_image\x18\x05 \x01(\tB\x03\xe0A\x01\x12%\n\x18enable_automatic_updates\x18\x06 \x01(\x08B\x03\xe0A\x01\x12F\n\x0bworker_pool\x18\x07 \x01(\tB1\xe0A\x01\xfaA+\n)cloudbuild.googleapis.com/BuildWorkerPool\x12^\n\x15environment_variables\x18\x08 \x03(\x0b2:.google.cloud.run.v2.BuildConfig.EnvironmentVariablesEntryB\x03\xe0A\x01\x12\x1c\n\x0fservice_account\x18\t \x01(\tB\x03\xe0A\x01\x1a;\n\x19EnvironmentVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01*\xb3\x01\n\x0eIngressTraffic\x12\x1f\n\x1bINGRESS_TRAFFIC_UNSPECIFIED\x10\x00\x12\x17\n\x13INGRESS_TRAFFIC_ALL\x10\x01\x12!\n\x1dINGRESS_TRAFFIC_INTERNAL_ONLY\x10\x02\x12*\n&INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER\x10\x03\x12\x18\n\x14INGRESS_TRAFFIC_NONE\x10\x04*}\n\x14ExecutionEnvironment\x12%\n!EXECUTION_ENVIRONMENT_UNSPECIFIED\x10\x00\x12\x1e\n\x1aEXECUTION_ENVIRONMENT_GEN1\x10\x01\x12\x1e\n\x1aEXECUTION_ENVIRONMENT_GEN2\x10\x02*p\n\x1dEncryptionKeyRevocationAction\x120\n,ENCRYPTION_KEY_REVOCATION_ACTION_UNSPECIFIED\x10\x00\x12\x0f\n\x0bPREVENT_NEW\x10\x01\x12\x0c\n\x08SHUTDOWN\x10\x02B\xfc\x02\n\x17com.google.cloud.run.v2B\x13VendorSettingsProtoP\x01Z)cloud.google.com/go/run/apiv2/runpb;runpb\xeaAc\n)binaryauthorization.googleapis.com/Policy\x12\x19projects/{project}/policy\x12\x1blocations/{location}/policy\xeaA\\\n#networkservices.googleapis.com/Mesh\x125projects/{project}/locations/{location}/meshes/{mesh}\xeaAY\n\x1fcloudbuild.googleapis.com/Build\x126projects/{project}/locations/{location}/builds/{build}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.run.v2.vendor_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.run.v2B\x13VendorSettingsProtoP\x01Z)cloud.google.com/go/run/apiv2/runpb;runpb\xeaAc\n)binaryauthorization.googleapis.com/Policy\x12\x19projects/{project}/policy\x12\x1blocations/{location}/policy\xeaA\\\n#networkservices.googleapis.com/Mesh\x125projects/{project}/locations/{location}/meshes/{mesh}\xeaAY\n\x1fcloudbuild.googleapis.com/Build\x126projects/{project}/locations/{location}/builds/{build}'
    _globals['_VPCACCESS_NETWORKINTERFACE'].fields_by_name['network']._loaded_options = None
    _globals['_VPCACCESS_NETWORKINTERFACE'].fields_by_name['network']._serialized_options = b'\xe0A\x01'
    _globals['_VPCACCESS_NETWORKINTERFACE'].fields_by_name['subnetwork']._loaded_options = None
    _globals['_VPCACCESS_NETWORKINTERFACE'].fields_by_name['subnetwork']._serialized_options = b'\xe0A\x01'
    _globals['_VPCACCESS_NETWORKINTERFACE'].fields_by_name['tags']._loaded_options = None
    _globals['_VPCACCESS_NETWORKINTERFACE'].fields_by_name['tags']._serialized_options = b'\xe0A\x01'
    _globals['_VPCACCESS'].fields_by_name['connector']._loaded_options = None
    _globals['_VPCACCESS'].fields_by_name['connector']._serialized_options = b'\xfaA$\n"vpcaccess.googleapis.com/Connector'
    _globals['_VPCACCESS'].fields_by_name['egress']._loaded_options = None
    _globals['_VPCACCESS'].fields_by_name['egress']._serialized_options = b'\xe0A\x01'
    _globals['_VPCACCESS'].fields_by_name['network_interfaces']._loaded_options = None
    _globals['_VPCACCESS'].fields_by_name['network_interfaces']._serialized_options = b'\xe0A\x01'
    _globals['_BINARYAUTHORIZATION'].fields_by_name['use_default']._loaded_options = None
    _globals['_BINARYAUTHORIZATION'].fields_by_name['use_default']._serialized_options = b'\xe0A\x01'
    _globals['_BINARYAUTHORIZATION'].fields_by_name['policy']._loaded_options = None
    _globals['_BINARYAUTHORIZATION'].fields_by_name['policy']._serialized_options = b'\xe0A\x01\xfaA+\n)binaryauthorization.googleapis.com/Policy'
    _globals['_BINARYAUTHORIZATION'].fields_by_name['breakglass_justification']._loaded_options = None
    _globals['_BINARYAUTHORIZATION'].fields_by_name['breakglass_justification']._serialized_options = b'\xe0A\x01'
    _globals['_REVISIONSCALING'].fields_by_name['min_instance_count']._loaded_options = None
    _globals['_REVISIONSCALING'].fields_by_name['min_instance_count']._serialized_options = b'\xe0A\x01'
    _globals['_REVISIONSCALING'].fields_by_name['max_instance_count']._loaded_options = None
    _globals['_REVISIONSCALING'].fields_by_name['max_instance_count']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICEMESH'].fields_by_name['mesh']._loaded_options = None
    _globals['_SERVICEMESH'].fields_by_name['mesh']._serialized_options = b'\xfaA%\n#networkservices.googleapis.com/Mesh'
    _globals['_SERVICESCALING'].fields_by_name['min_instance_count']._loaded_options = None
    _globals['_SERVICESCALING'].fields_by_name['min_instance_count']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICESCALING'].fields_by_name['scaling_mode']._loaded_options = None
    _globals['_SERVICESCALING'].fields_by_name['scaling_mode']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICESCALING'].fields_by_name['manual_instance_count']._loaded_options = None
    _globals['_SERVICESCALING'].fields_by_name['manual_instance_count']._serialized_options = b'\xe0A\x01'
    _globals['_WORKERPOOLSCALING'].fields_by_name['manual_instance_count']._loaded_options = None
    _globals['_WORKERPOOLSCALING'].fields_by_name['manual_instance_count']._serialized_options = b'\xe0A\x01'
    _globals['_NODESELECTOR'].fields_by_name['accelerator']._loaded_options = None
    _globals['_NODESELECTOR'].fields_by_name['accelerator']._serialized_options = b'\xe0A\x02'
    _globals['_BUILDCONFIG_ENVIRONMENTVARIABLESENTRY']._loaded_options = None
    _globals['_BUILDCONFIG_ENVIRONMENTVARIABLESENTRY']._serialized_options = b'8\x01'
    _globals['_BUILDCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_BUILDCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xfaA!\n\x1fcloudbuild.googleapis.com/Build'
    _globals['_BUILDCONFIG'].fields_by_name['function_target']._loaded_options = None
    _globals['_BUILDCONFIG'].fields_by_name['function_target']._serialized_options = b'\xe0A\x01'
    _globals['_BUILDCONFIG'].fields_by_name['image_uri']._loaded_options = None
    _globals['_BUILDCONFIG'].fields_by_name['image_uri']._serialized_options = b'\xe0A\x01'
    _globals['_BUILDCONFIG'].fields_by_name['base_image']._loaded_options = None
    _globals['_BUILDCONFIG'].fields_by_name['base_image']._serialized_options = b'\xe0A\x01'
    _globals['_BUILDCONFIG'].fields_by_name['enable_automatic_updates']._loaded_options = None
    _globals['_BUILDCONFIG'].fields_by_name['enable_automatic_updates']._serialized_options = b'\xe0A\x01'
    _globals['_BUILDCONFIG'].fields_by_name['worker_pool']._loaded_options = None
    _globals['_BUILDCONFIG'].fields_by_name['worker_pool']._serialized_options = b'\xe0A\x01\xfaA+\n)cloudbuild.googleapis.com/BuildWorkerPool'
    _globals['_BUILDCONFIG'].fields_by_name['environment_variables']._loaded_options = None
    _globals['_BUILDCONFIG'].fields_by_name['environment_variables']._serialized_options = b'\xe0A\x01'
    _globals['_BUILDCONFIG'].fields_by_name['service_account']._loaded_options = None
    _globals['_BUILDCONFIG'].fields_by_name['service_account']._serialized_options = b'\xe0A\x01'
    _globals['_INGRESSTRAFFIC']._serialized_start = 1720
    _globals['_INGRESSTRAFFIC']._serialized_end = 1899
    _globals['_EXECUTIONENVIRONMENT']._serialized_start = 1901
    _globals['_EXECUTIONENVIRONMENT']._serialized_end = 2026
    _globals['_ENCRYPTIONKEYREVOCATIONACTION']._serialized_start = 2028
    _globals['_ENCRYPTIONKEYREVOCATIONACTION']._serialized_end = 2140
    _globals['_VPCACCESS']._serialized_start = 127
    _globals['_VPCACCESS']._serialized_end = 512
    _globals['_VPCACCESS_NETWORKINTERFACE']._serialized_start = 345
    _globals['_VPCACCESS_NETWORKINTERFACE']._serialized_end = 429
    _globals['_VPCACCESS_VPCEGRESS']._serialized_start = 431
    _globals['_VPCACCESS_VPCEGRESS']._serialized_end = 512
    _globals['_BINARYAUTHORIZATION']._serialized_start = 515
    _globals['_BINARYAUTHORIZATION']._serialized_end = 691
    _globals['_REVISIONSCALING']._serialized_start = 693
    _globals['_REVISIONSCALING']._serialized_end = 776
    _globals['_SERVICEMESH']._serialized_start = 778
    _globals['_SERVICEMESH']._serialized_end = 847
    _globals['_SERVICESCALING']._serialized_start = 850
    _globals['_SERVICESCALING']._serialized_end = 1114
    _globals['_SERVICESCALING_SCALINGMODE']._serialized_start = 1018
    _globals['_SERVICESCALING_SCALINGMODE']._serialized_end = 1088
    _globals['_WORKERPOOLSCALING']._serialized_start = 1116
    _globals['_WORKERPOOLSCALING']._serialized_end = 1202
    _globals['_NODESELECTOR']._serialized_start = 1204
    _globals['_NODESELECTOR']._serialized_end = 1244
    _globals['_BUILDCONFIG']._serialized_start = 1247
    _globals['_BUILDCONFIG']._serialized_end = 1717
    _globals['_BUILDCONFIG_ENVIRONMENTVARIABLESENTRY']._serialized_start = 1658
    _globals['_BUILDCONFIG_ENVIRONMENTVARIABLESENTRY']._serialized_end = 1717