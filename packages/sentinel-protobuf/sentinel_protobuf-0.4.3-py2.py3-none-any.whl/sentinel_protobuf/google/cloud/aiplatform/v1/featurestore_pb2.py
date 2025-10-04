"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/featurestore.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/aiplatform/v1/featurestore.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/aiplatform/v1/encryption_spec.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x83\x08\n\x0cFeaturestore\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x05 \x01(\tB\x03\xe0A\x01\x12I\n\x06labels\x18\x06 \x03(\x0b24.google.cloud.aiplatform.v1.Featurestore.LabelsEntryB\x03\xe0A\x01\x12`\n\x15online_serving_config\x18\x07 \x01(\x0b2<.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfigB\x03\xe0A\x01\x12B\n\x05state\x18\x08 \x01(\x0e2..google.cloud.aiplatform.v1.Featurestore.StateB\x03\xe0A\x03\x12$\n\x17online_storage_ttl_days\x18\r \x01(\x05B\x03\xe0A\x01\x12H\n\x0fencryption_spec\x18\n \x01(\x0b2*.google.cloud.aiplatform.v1.EncryptionSpecB\x03\xe0A\x01\x12\x1a\n\rsatisfies_pzs\x18\x0e \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x0f \x01(\x08B\x03\xe0A\x03\x1a\xeb\x01\n\x13OnlineServingConfig\x12\x18\n\x10fixed_node_count\x18\x02 \x01(\x05\x12U\n\x07scaling\x18\x04 \x01(\x0b2D.google.cloud.aiplatform.v1.Featurestore.OnlineServingConfig.Scaling\x1ac\n\x07Scaling\x12\x1b\n\x0emin_node_count\x18\x01 \x01(\x05B\x03\xe0A\x02\x12\x16\n\x0emax_node_count\x18\x02 \x01(\x05\x12#\n\x16cpu_utilization_target\x18\x03 \x01(\x05B\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"8\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06STABLE\x10\x01\x12\x0c\n\x08UPDATING\x10\x02:q\xeaAn\n&aiplatform.googleapis.com/Featurestore\x12Dprojects/{project}/locations/{location}/featurestores/{featurestore}B\xcf\x01\n\x1ecom.google.cloud.aiplatform.v1B\x11FeaturestoreProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.featurestore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x11FeaturestoreProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_FEATURESTORE_ONLINESERVINGCONFIG_SCALING'].fields_by_name['min_node_count']._loaded_options = None
    _globals['_FEATURESTORE_ONLINESERVINGCONFIG_SCALING'].fields_by_name['min_node_count']._serialized_options = b'\xe0A\x02'
    _globals['_FEATURESTORE_ONLINESERVINGCONFIG_SCALING'].fields_by_name['cpu_utilization_target']._loaded_options = None
    _globals['_FEATURESTORE_ONLINESERVINGCONFIG_SCALING'].fields_by_name['cpu_utilization_target']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURESTORE_LABELSENTRY']._loaded_options = None
    _globals['_FEATURESTORE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_FEATURESTORE'].fields_by_name['name']._loaded_options = None
    _globals['_FEATURESTORE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURESTORE'].fields_by_name['create_time']._loaded_options = None
    _globals['_FEATURESTORE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURESTORE'].fields_by_name['update_time']._loaded_options = None
    _globals['_FEATURESTORE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURESTORE'].fields_by_name['etag']._loaded_options = None
    _globals['_FEATURESTORE'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURESTORE'].fields_by_name['labels']._loaded_options = None
    _globals['_FEATURESTORE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURESTORE'].fields_by_name['online_serving_config']._loaded_options = None
    _globals['_FEATURESTORE'].fields_by_name['online_serving_config']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURESTORE'].fields_by_name['state']._loaded_options = None
    _globals['_FEATURESTORE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURESTORE'].fields_by_name['online_storage_ttl_days']._loaded_options = None
    _globals['_FEATURESTORE'].fields_by_name['online_storage_ttl_days']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURESTORE'].fields_by_name['encryption_spec']._loaded_options = None
    _globals['_FEATURESTORE'].fields_by_name['encryption_spec']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURESTORE'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_FEATURESTORE'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURESTORE'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_FEATURESTORE'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURESTORE']._loaded_options = None
    _globals['_FEATURESTORE']._serialized_options = b'\xeaAn\n&aiplatform.googleapis.com/Featurestore\x12Dprojects/{project}/locations/{location}/featurestores/{featurestore}'
    _globals['_FEATURESTORE']._serialized_start = 221
    _globals['_FEATURESTORE']._serialized_end = 1248
    _globals['_FEATURESTORE_ONLINESERVINGCONFIG']._serialized_start = 793
    _globals['_FEATURESTORE_ONLINESERVINGCONFIG']._serialized_end = 1028
    _globals['_FEATURESTORE_ONLINESERVINGCONFIG_SCALING']._serialized_start = 929
    _globals['_FEATURESTORE_ONLINESERVINGCONFIG_SCALING']._serialized_end = 1028
    _globals['_FEATURESTORE_LABELSENTRY']._serialized_start = 1030
    _globals['_FEATURESTORE_LABELSENTRY']._serialized_end = 1075
    _globals['_FEATURESTORE_STATE']._serialized_start = 1077
    _globals['_FEATURESTORE_STATE']._serialized_end = 1133