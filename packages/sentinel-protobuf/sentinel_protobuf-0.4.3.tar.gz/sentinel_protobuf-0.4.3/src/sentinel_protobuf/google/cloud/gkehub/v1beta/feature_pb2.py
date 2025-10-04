"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkehub/v1beta/feature.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkehub.policycontroller.v1beta import policycontroller_pb2 as google_dot_cloud_dot_gkehub_dot_policycontroller_dot_v1beta_dot_policycontroller__pb2
from .....google.cloud.gkehub.servicemesh.v1beta import servicemesh_pb2 as google_dot_cloud_dot_gkehub_dot_servicemesh_dot_v1beta_dot_servicemesh__pb2
from .....google.cloud.gkehub.v1beta.configmanagement import configmanagement_pb2 as google_dot_cloud_dot_gkehub_dot_v1beta_dot_configmanagement_dot_configmanagement__pb2
from .....google.cloud.gkehub.v1beta.metering import metering_pb2 as google_dot_cloud_dot_gkehub_dot_v1beta_dot_metering_dot_metering__pb2
from .....google.cloud.gkehub.v1beta.multiclusteringress import multiclusteringress_pb2 as google_dot_cloud_dot_gkehub_dot_v1beta_dot_multiclusteringress_dot_multiclusteringress__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/gkehub/v1beta/feature.proto\x12\x1agoogle.cloud.gkehub.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aBgoogle/cloud/gkehub/policycontroller/v1beta/policycontroller.proto\x1a8google/cloud/gkehub/servicemesh/v1beta/servicemesh.proto\x1aBgoogle/cloud/gkehub/v1beta/configmanagement/configmanagement.proto\x1a2google/cloud/gkehub/v1beta/metering/metering.proto\x1aHgoogle/cloud/gkehub/v1beta/multiclusteringress/multiclusteringress.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xef\x07\n\x07Feature\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12?\n\x06labels\x18\x02 \x03(\x0b2/.google.cloud.gkehub.v1beta.Feature.LabelsEntry\x12M\n\x0eresource_state\x18\x03 \x01(\x0b20.google.cloud.gkehub.v1beta.FeatureResourceStateB\x03\xe0A\x03\x12@\n\x04spec\x18\x04 \x01(\x0b2-.google.cloud.gkehub.v1beta.CommonFeatureSpecB\x03\xe0A\x01\x12W\n\x10membership_specs\x18\x05 \x03(\x0b28.google.cloud.gkehub.v1beta.Feature.MembershipSpecsEntryB\x03\xe0A\x01\x12B\n\x05state\x18\x06 \x01(\x0b2..google.cloud.gkehub.v1beta.CommonFeatureStateB\x03\xe0A\x03\x12Y\n\x11membership_states\x18\x07 \x03(\x0b29.google.cloud.gkehub.v1beta.Feature.MembershipStatesEntryB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1ai\n\x14MembershipSpecsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b21.google.cloud.gkehub.v1beta.MembershipFeatureSpec:\x028\x01\x1ak\n\x15MembershipStatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12A\n\x05value\x18\x02 \x01(\x0b22.google.cloud.gkehub.v1beta.MembershipFeatureState:\x028\x01:^\xeaA[\n\x1dgkehub.googleapis.com/Feature\x12:projects/{project}/locations/{location}/features/{feature}"\xca\x01\n\x14FeatureResourceState\x12E\n\x05state\x18\x01 \x01(\x0e26.google.cloud.gkehub.v1beta.FeatureResourceState.State"k\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08ENABLING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\r\n\tDISABLING\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x14\n\x10SERVICE_UPDATING\x10\x05"\xcf\x01\n\x0cFeatureState\x12;\n\x04code\x18\x01 \x01(\x0e2-.google.cloud.gkehub.v1beta.FeatureState.Code\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"<\n\x04Code\x12\x14\n\x10CODE_UNSPECIFIED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05ERROR\x10\x03"\x7f\n\x11CommonFeatureSpec\x12Z\n\x13multiclusteringress\x18f \x01(\x0b2;.google.cloud.gkehub.multiclusteringress.v1beta.FeatureSpecH\x00B\x0e\n\x0cfeature_spec"R\n\x12CommonFeatureState\x12<\n\x05state\x18\x01 \x01(\x0b2(.google.cloud.gkehub.v1beta.FeatureStateB\x03\xe0A\x03"\xa1\x02\n\x15MembershipFeatureSpec\x12W\n\x10configmanagement\x18j \x01(\x0b2;.google.cloud.gkehub.configmanagement.v1beta.MembershipSpecH\x00\x12F\n\x04mesh\x18t \x01(\x0b26.google.cloud.gkehub.servicemesh.v1beta.MembershipSpecH\x00\x12W\n\x10policycontroller\x18v \x01(\x0b2;.google.cloud.gkehub.policycontroller.v1beta.MembershipSpecH\x00B\x0e\n\x0cfeature_spec"\xb0\x03\n\x16MembershipFeatureState\x12N\n\x0bservicemesh\x18d \x01(\x0b27.google.cloud.gkehub.servicemesh.v1beta.MembershipStateH\x00\x12H\n\x08metering\x18h \x01(\x0b24.google.cloud.gkehub.metering.v1beta.MembershipStateH\x00\x12X\n\x10configmanagement\x18j \x01(\x0b2<.google.cloud.gkehub.configmanagement.v1beta.MembershipStateH\x00\x12X\n\x10policycontroller\x18t \x01(\x0b2<.google.cloud.gkehub.policycontroller.v1beta.MembershipStateH\x00\x127\n\x05state\x18\x01 \x01(\x0b2(.google.cloud.gkehub.v1beta.FeatureStateB\x0f\n\rfeature_stateB\xc2\x01\n\x1ecom.google.cloud.gkehub.v1betaB\x0cFeatureProtoP\x01Z6cloud.google.com/go/gkehub/apiv1beta/gkehubpb;gkehubpb\xaa\x02\x1aGoogle.Cloud.GkeHub.V1Beta\xca\x02\x1aGoogle\\Cloud\\GkeHub\\V1beta\xea\x02\x1dGoogle::Cloud::GkeHub::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.v1beta.feature_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.gkehub.v1betaB\x0cFeatureProtoP\x01Z6cloud.google.com/go/gkehub/apiv1beta/gkehubpb;gkehubpb\xaa\x02\x1aGoogle.Cloud.GkeHub.V1Beta\xca\x02\x1aGoogle\\Cloud\\GkeHub\\V1beta\xea\x02\x1dGoogle::Cloud::GkeHub::V1beta'
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
    _globals['_FEATURE']._serialized_start = 486
    _globals['_FEATURE']._serialized_end = 1493
    _globals['_FEATURE_LABELSENTRY']._serialized_start = 1136
    _globals['_FEATURE_LABELSENTRY']._serialized_end = 1181
    _globals['_FEATURE_MEMBERSHIPSPECSENTRY']._serialized_start = 1183
    _globals['_FEATURE_MEMBERSHIPSPECSENTRY']._serialized_end = 1288
    _globals['_FEATURE_MEMBERSHIPSTATESENTRY']._serialized_start = 1290
    _globals['_FEATURE_MEMBERSHIPSTATESENTRY']._serialized_end = 1397
    _globals['_FEATURERESOURCESTATE']._serialized_start = 1496
    _globals['_FEATURERESOURCESTATE']._serialized_end = 1698
    _globals['_FEATURERESOURCESTATE_STATE']._serialized_start = 1591
    _globals['_FEATURERESOURCESTATE_STATE']._serialized_end = 1698
    _globals['_FEATURESTATE']._serialized_start = 1701
    _globals['_FEATURESTATE']._serialized_end = 1908
    _globals['_FEATURESTATE_CODE']._serialized_start = 1848
    _globals['_FEATURESTATE_CODE']._serialized_end = 1908
    _globals['_COMMONFEATURESPEC']._serialized_start = 1910
    _globals['_COMMONFEATURESPEC']._serialized_end = 2037
    _globals['_COMMONFEATURESTATE']._serialized_start = 2039
    _globals['_COMMONFEATURESTATE']._serialized_end = 2121
    _globals['_MEMBERSHIPFEATURESPEC']._serialized_start = 2124
    _globals['_MEMBERSHIPFEATURESPEC']._serialized_end = 2413
    _globals['_MEMBERSHIPFEATURESTATE']._serialized_start = 2416
    _globals['_MEMBERSHIPFEATURESTATE']._serialized_end = 2848