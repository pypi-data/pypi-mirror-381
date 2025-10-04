"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkehub/v1/feature.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkehub.v1.configmanagement import configmanagement_pb2 as google_dot_cloud_dot_gkehub_dot_v1_dot_configmanagement_dot_configmanagement__pb2
from .....google.cloud.gkehub.v1.multiclusteringress import multiclusteringress_pb2 as google_dot_cloud_dot_gkehub_dot_v1_dot_multiclusteringress_dot_multiclusteringress__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/cloud/gkehub/v1/feature.proto\x12\x16google.cloud.gkehub.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a>google/cloud/gkehub/v1/configmanagement/configmanagement.proto\x1aDgoogle/cloud/gkehub/v1/multiclusteringress/multiclusteringress.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcf\x07\n\x07Feature\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12;\n\x06labels\x18\x02 \x03(\x0b2+.google.cloud.gkehub.v1.Feature.LabelsEntry\x12I\n\x0eresource_state\x18\x03 \x01(\x0b2,.google.cloud.gkehub.v1.FeatureResourceStateB\x03\xe0A\x03\x12<\n\x04spec\x18\x04 \x01(\x0b2).google.cloud.gkehub.v1.CommonFeatureSpecB\x03\xe0A\x01\x12S\n\x10membership_specs\x18\x05 \x03(\x0b24.google.cloud.gkehub.v1.Feature.MembershipSpecsEntryB\x03\xe0A\x01\x12>\n\x05state\x18\x06 \x01(\x0b2*.google.cloud.gkehub.v1.CommonFeatureStateB\x03\xe0A\x03\x12U\n\x11membership_states\x18\x07 \x03(\x0b25.google.cloud.gkehub.v1.Feature.MembershipStatesEntryB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1ae\n\x14MembershipSpecsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b2-.google.cloud.gkehub.v1.MembershipFeatureSpec:\x028\x01\x1ag\n\x15MembershipStatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b2..google.cloud.gkehub.v1.MembershipFeatureState:\x028\x01:^\xeaA[\n\x1dgkehub.googleapis.com/Feature\x12:projects/{project}/locations/{location}/features/{feature}"\xc6\x01\n\x14FeatureResourceState\x12A\n\x05state\x18\x01 \x01(\x0e22.google.cloud.gkehub.v1.FeatureResourceState.State"k\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08ENABLING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\r\n\tDISABLING\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x14\n\x10SERVICE_UPDATING\x10\x05"\xcb\x01\n\x0cFeatureState\x127\n\x04code\x18\x01 \x01(\x0e2).google.cloud.gkehub.v1.FeatureState.Code\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"<\n\x04Code\x12\x14\n\x10CODE_UNSPECIFIED\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05ERROR\x10\x03"{\n\x11CommonFeatureSpec\x12V\n\x13multiclusteringress\x18f \x01(\x0b27.google.cloud.gkehub.multiclusteringress.v1.FeatureSpecH\x00B\x0e\n\x0cfeature_spec"N\n\x12CommonFeatureState\x128\n\x05state\x18\x01 \x01(\x0b2$.google.cloud.gkehub.v1.FeatureStateB\x03\xe0A\x03"|\n\x15MembershipFeatureSpec\x12S\n\x10configmanagement\x18j \x01(\x0b27.google.cloud.gkehub.configmanagement.v1.MembershipSpecH\x00B\x0e\n\x0cfeature_spec"\xb4\x01\n\x16MembershipFeatureState\x12T\n\x10configmanagement\x18j \x01(\x0b28.google.cloud.gkehub.configmanagement.v1.MembershipStateH\x00\x123\n\x05state\x18\x01 \x01(\x0b2$.google.cloud.gkehub.v1.FeatureStateB\x0f\n\rfeature_stateB\xae\x01\n\x1acom.google.cloud.gkehub.v1B\x0cFeatureProtoP\x01Z2cloud.google.com/go/gkehub/apiv1/gkehubpb;gkehubpb\xaa\x02\x16Google.Cloud.GkeHub.V1\xca\x02\x16Google\\Cloud\\GkeHub\\V1\xea\x02\x19Google::Cloud::GkeHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.v1.feature_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.gkehub.v1B\x0cFeatureProtoP\x01Z2cloud.google.com/go/gkehub/apiv1/gkehubpb;gkehubpb\xaa\x02\x16Google.Cloud.GkeHub.V1\xca\x02\x16Google\\Cloud\\GkeHub\\V1\xea\x02\x19Google::Cloud::GkeHub::V1'
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
    _globals['_FEATURE']._serialized_start = 292
    _globals['_FEATURE']._serialized_end = 1267
    _globals['_FEATURE_LABELSENTRY']._serialized_start = 918
    _globals['_FEATURE_LABELSENTRY']._serialized_end = 963
    _globals['_FEATURE_MEMBERSHIPSPECSENTRY']._serialized_start = 965
    _globals['_FEATURE_MEMBERSHIPSPECSENTRY']._serialized_end = 1066
    _globals['_FEATURE_MEMBERSHIPSTATESENTRY']._serialized_start = 1068
    _globals['_FEATURE_MEMBERSHIPSTATESENTRY']._serialized_end = 1171
    _globals['_FEATURERESOURCESTATE']._serialized_start = 1270
    _globals['_FEATURERESOURCESTATE']._serialized_end = 1468
    _globals['_FEATURERESOURCESTATE_STATE']._serialized_start = 1361
    _globals['_FEATURERESOURCESTATE_STATE']._serialized_end = 1468
    _globals['_FEATURESTATE']._serialized_start = 1471
    _globals['_FEATURESTATE']._serialized_end = 1674
    _globals['_FEATURESTATE_CODE']._serialized_start = 1614
    _globals['_FEATURESTATE_CODE']._serialized_end = 1674
    _globals['_COMMONFEATURESPEC']._serialized_start = 1676
    _globals['_COMMONFEATURESPEC']._serialized_end = 1799
    _globals['_COMMONFEATURESTATE']._serialized_start = 1801
    _globals['_COMMONFEATURESTATE']._serialized_end = 1879
    _globals['_MEMBERSHIPFEATURESPEC']._serialized_start = 1881
    _globals['_MEMBERSHIPFEATURESPEC']._serialized_end = 2005
    _globals['_MEMBERSHIPFEATURESTATE']._serialized_start = 2008
    _globals['_MEMBERSHIPFEATURESTATE']._serialized_end = 2188