"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkehub/v1alpha/feature.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkehub.v1alpha.cloudauditlogging import cloudauditlogging_pb2 as google_dot_cloud_dot_gkehub_dot_v1alpha_dot_cloudauditlogging_dot_cloudauditlogging__pb2
from .....google.cloud.gkehub.v1alpha.configmanagement import configmanagement_pb2 as google_dot_cloud_dot_gkehub_dot_v1alpha_dot_configmanagement_dot_configmanagement__pb2
from .....google.cloud.gkehub.v1alpha.metering import metering_pb2 as google_dot_cloud_dot_gkehub_dot_v1alpha_dot_metering_dot_metering__pb2
from .....google.cloud.gkehub.v1alpha.multiclusteringress import multiclusteringress_pb2 as google_dot_cloud_dot_gkehub_dot_v1alpha_dot_multiclusteringress_dot_multiclusteringress__pb2
from .....google.cloud.gkehub.v1alpha.servicemesh import servicemesh_pb2 as google_dot_cloud_dot_gkehub_dot_v1alpha_dot_servicemesh_dot_servicemesh__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/gkehub/v1alpha/feature.proto\x12\x1bgoogle.cloud.gkehub.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aEgoogle/cloud/gkehub/v1alpha/cloudauditlogging/cloudauditlogging.proto\x1aCgoogle/cloud/gkehub/v1alpha/configmanagement/configmanagement.proto\x1a3google/cloud/gkehub/v1alpha/metering/metering.proto\x1aIgoogle/cloud/gkehub/v1alpha/multiclusteringress/multiclusteringress.proto\x1a9google/cloud/gkehub/v1alpha/servicemesh/servicemesh.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf7\x07\n\x07Feature\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12@\n\x06labels\x18\x02 \x03(\x0b20.google.cloud.gkehub.v1alpha.Feature.LabelsEntry\x12N\n\x0eresource_state\x18\x03 \x01(\x0b21.google.cloud.gkehub.v1alpha.FeatureResourceStateB\x03\xe0A\x03\x12A\n\x04spec\x18\x04 \x01(\x0b2..google.cloud.gkehub.v1alpha.CommonFeatureSpecB\x03\xe0A\x01\x12X\n\x10membership_specs\x18\x05 \x03(\x0b29.google.cloud.gkehub.v1alpha.Feature.MembershipSpecsEntryB\x03\xe0A\x01\x12C\n\x05state\x18\x06 \x01(\x0b2/.google.cloud.gkehub.v1alpha.CommonFeatureStateB\x03\xe0A\x03\x12Z\n\x11membership_states\x18\x07 \x03(\x0b2:.google.cloud.gkehub.v1alpha.Feature.MembershipStatesEntryB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1aj\n\x14MembershipSpecsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12A\n\x05value\x18\x02 \x01(\x0b22.google.cloud.gkehub.v1alpha.MembershipFeatureSpec:\x028\x01\x1al\n\x15MembershipStatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12B\n\x05value\x18\x02 \x01(\x0b23.google.cloud.gkehub.v1alpha.MembershipFeatureState:\x028\x01:^\xeaA[\n\x1dgkehub.googleapis.com/Feature\x12:projects/{project}/locations/{location}/features/{feature}"\xcb\x01\n\x14FeatureResourceState\x12F\n\x05state\x18\x01 \x01(\x0e27.google.cloud.gkehub.v1alpha.FeatureResourceState.State"k\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08ENABLING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\r\n\tDISABLING\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x14\n\x10SERVICE_UPDATING\x10\x05"\xd0\x01\n\x0cFeatureState\x12<\n\x04code\x18\x01 \x01(\x0e2..google.cloud.gkehub.v1alpha.FeatureState.Code\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"<\n\x04Code\x12\x14\n\x10CODE_UNSPECIFIED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05ERROR\x10\x03"\xd9\x01\n\x11CommonFeatureSpec\x12[\n\x13multiclusteringress\x18f \x01(\x0b2<.google.cloud.gkehub.multiclusteringress.v1alpha.FeatureSpecH\x00\x12W\n\x11cloudauditlogging\x18l \x01(\x0b2:.google.cloud.gkehub.cloudauditlogging.v1alpha.FeatureSpecH\x00B\x0e\n\x0cfeature_spec"\xb2\x01\n\x12CommonFeatureState\x12L\n\x0bservicemesh\x18d \x01(\x0b25.google.cloud.gkehub.servicemesh.v1alpha.FeatureStateH\x00\x12=\n\x05state\x18\x01 \x01(\x0b2).google.cloud.gkehub.v1alpha.FeatureStateB\x03\xe0A\x03B\x0f\n\rfeature_state"\x81\x01\n\x15MembershipFeatureSpec\x12X\n\x10configmanagement\x18j \x01(\x0b2<.google.cloud.gkehub.configmanagement.v1alpha.MembershipSpecH\x00B\x0e\n\x0cfeature_spec"\xda\x02\n\x16MembershipFeatureState\x12O\n\x0bservicemesh\x18d \x01(\x0b28.google.cloud.gkehub.servicemesh.v1alpha.MembershipStateH\x00\x12I\n\x08metering\x18h \x01(\x0b25.google.cloud.gkehub.metering.v1alpha.MembershipStateH\x00\x12Y\n\x10configmanagement\x18j \x01(\x0b2=.google.cloud.gkehub.configmanagement.v1alpha.MembershipStateH\x00\x128\n\x05state\x18\x01 \x01(\x0b2).google.cloud.gkehub.v1alpha.FeatureStateB\x0f\n\rfeature_stateB\xc7\x01\n\x1fcom.google.cloud.gkehub.v1alphaB\x0cFeatureProtoP\x01Z7cloud.google.com/go/gkehub/apiv1alpha/gkehubpb;gkehubpb\xaa\x02\x1bGoogle.Cloud.GkeHub.V1Alpha\xca\x02\x1bGoogle\\Cloud\\GkeHub\\V1alpha\xea\x02\x1eGoogle::Cloud::GkeHub::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.v1alpha.feature_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.gkehub.v1alphaB\x0cFeatureProtoP\x01Z7cloud.google.com/go/gkehub/apiv1alpha/gkehubpb;gkehubpb\xaa\x02\x1bGoogle.Cloud.GkeHub.V1Alpha\xca\x02\x1bGoogle\\Cloud\\GkeHub\\V1alpha\xea\x02\x1eGoogle::Cloud::GkeHub::V1alpha'
    _globals['_FEATURE_LABELSENTRY']._loaded_options = None
    _globals['_FEATURE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_FEATURE_MEMBERSHIPSPECSENTRY']._loaded_options = None
    _globals['_FEATURE_MEMBERSHIPSPECSENTRY']._serialized_options = b'8\x01'
    _globals['_FEATURE_MEMBERSHIPSTATESENTRY']._loaded_options = None
    _globals['_FEATURE_MEMBERSHIPSTATESENTRY']._serialized_options = b'8\x01'
    _globals['_FEATURE'].fields_by_name['name']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE'].fields_by_name['resource_state']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['resource_state']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE'].fields_by_name['spec']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['spec']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURE'].fields_by_name['membership_specs']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['membership_specs']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURE'].fields_by_name['state']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE'].fields_by_name['membership_states']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['membership_states']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE'].fields_by_name['create_time']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE'].fields_by_name['update_time']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE'].fields_by_name['delete_time']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE']._loaded_options = None
    _globals['_FEATURE']._serialized_options = b'\xeaA[\n\x1dgkehub.googleapis.com/Feature\x12:projects/{project}/locations/{location}/features/{feature}'
    _globals['_COMMONFEATURESTATE'].fields_by_name['state']._loaded_options = None
    _globals['_COMMONFEATURESTATE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE']._serialized_start = 495
    _globals['_FEATURE']._serialized_end = 1510
    _globals['_FEATURE_LABELSENTRY']._serialized_start = 1151
    _globals['_FEATURE_LABELSENTRY']._serialized_end = 1196
    _globals['_FEATURE_MEMBERSHIPSPECSENTRY']._serialized_start = 1198
    _globals['_FEATURE_MEMBERSHIPSPECSENTRY']._serialized_end = 1304
    _globals['_FEATURE_MEMBERSHIPSTATESENTRY']._serialized_start = 1306
    _globals['_FEATURE_MEMBERSHIPSTATESENTRY']._serialized_end = 1414
    _globals['_FEATURERESOURCESTATE']._serialized_start = 1513
    _globals['_FEATURERESOURCESTATE']._serialized_end = 1716
    _globals['_FEATURERESOURCESTATE_STATE']._serialized_start = 1609
    _globals['_FEATURERESOURCESTATE_STATE']._serialized_end = 1716
    _globals['_FEATURESTATE']._serialized_start = 1719
    _globals['_FEATURESTATE']._serialized_end = 1927
    _globals['_FEATURESTATE_CODE']._serialized_start = 1867
    _globals['_FEATURESTATE_CODE']._serialized_end = 1927
    _globals['_COMMONFEATURESPEC']._serialized_start = 1930
    _globals['_COMMONFEATURESPEC']._serialized_end = 2147
    _globals['_COMMONFEATURESTATE']._serialized_start = 2150
    _globals['_COMMONFEATURESTATE']._serialized_end = 2328
    _globals['_MEMBERSHIPFEATURESPEC']._serialized_start = 2331
    _globals['_MEMBERSHIPFEATURESPEC']._serialized_end = 2460
    _globals['_MEMBERSHIPFEATURESTATE']._serialized_start = 2463
    _globals['_MEMBERSHIPFEATURESTATE']._serialized_end = 2809