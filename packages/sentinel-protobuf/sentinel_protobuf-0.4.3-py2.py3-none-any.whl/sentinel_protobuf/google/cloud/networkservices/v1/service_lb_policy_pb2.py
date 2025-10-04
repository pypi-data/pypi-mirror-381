"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkservices/v1/service_lb_policy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/networkservices/v1/service_lb_policy.proto\x12\x1fgoogle.cloud.networkservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xba\x0b\n\x0fServiceLbPolicy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Q\n\x06labels\x18\x04 \x03(\x0b2<.google.cloud.networkservices.v1.ServiceLbPolicy.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01\x12n\n\x18load_balancing_algorithm\x18\x06 \x01(\x0e2G.google.cloud.networkservices.v1.ServiceLbPolicy.LoadBalancingAlgorithmB\x03\xe0A\x01\x12d\n\x13auto_capacity_drain\x18\x08 \x01(\x0b2B.google.cloud.networkservices.v1.ServiceLbPolicy.AutoCapacityDrainB\x03\xe0A\x01\x12]\n\x0ffailover_config\x18\n \x01(\x0b2?.google.cloud.networkservices.v1.ServiceLbPolicy.FailoverConfigB\x03\xe0A\x01\x12_\n\x10isolation_config\x18\x0b \x01(\x0b2@.google.cloud.networkservices.v1.ServiceLbPolicy.IsolationConfigB\x03\xe0A\x01\x1a(\n\x11AutoCapacityDrain\x12\x13\n\x06enable\x18\x01 \x01(\x08B\x03\xe0A\x01\x1a8\n\x0eFailoverConfig\x12&\n\x19failover_health_threshold\x18\x01 \x01(\x05B\x03\xe0A\x01\x1a\xd9\x01\n\x0fIsolationConfig\x12i\n\x15isolation_granularity\x18\x01 \x01(\x0e2E.google.cloud.networkservices.v1.ServiceLbPolicy.IsolationGranularityB\x03\xe0A\x01\x12[\n\x0eisolation_mode\x18\x02 \x01(\x0e2>.google.cloud.networkservices.v1.ServiceLbPolicy.IsolationModeB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x9b\x01\n\x16LoadBalancingAlgorithm\x12(\n$LOAD_BALANCING_ALGORITHM_UNSPECIFIED\x10\x00\x12\x12\n\x0eSPRAY_TO_WORLD\x10\x03\x12\x13\n\x0fSPRAY_TO_REGION\x10\x04\x12\x17\n\x13WATERFALL_BY_REGION\x10\x05\x12\x15\n\x11WATERFALL_BY_ZONE\x10\x06"I\n\x14IsolationGranularity\x12%\n!ISOLATION_GRANULARITY_UNSPECIFIED\x10\x00\x12\n\n\x06REGION\x10\x01"H\n\rIsolationMode\x12\x1e\n\x1aISOLATION_MODE_UNSPECIFIED\x10\x00\x12\x0b\n\x07NEAREST\x10\x01\x12\n\n\x06STRICT\x10\x02:\x82\x01\xeaA\x7f\n.networkservices.googleapis.com/ServiceLbPolicy\x12Mprojects/{project}/locations/{location}/serviceLbPolicies/{service_lb_policy}"\x8d\x01\n\x1cListServiceLbPoliciesRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.networkservices.googleapis.com/ServiceLbPolicy\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x9c\x01\n\x1dListServiceLbPoliciesResponse\x12M\n\x13service_lb_policies\x18\x01 \x03(\x0b20.google.cloud.networkservices.v1.ServiceLbPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"a\n\x19GetServiceLbPolicyRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.networkservices.googleapis.com/ServiceLbPolicy"\xdb\x01\n\x1cCreateServiceLbPolicyRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.networkservices.googleapis.com/ServiceLbPolicy\x12!\n\x14service_lb_policy_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12P\n\x11service_lb_policy\x18\x03 \x01(\x0b20.google.cloud.networkservices.v1.ServiceLbPolicyB\x03\xe0A\x02"\xa6\x01\n\x1cUpdateServiceLbPolicyRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12P\n\x11service_lb_policy\x18\x02 \x01(\x0b20.google.cloud.networkservices.v1.ServiceLbPolicyB\x03\xe0A\x02"d\n\x1cDeleteServiceLbPolicyRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.networkservices.googleapis.com/ServiceLbPolicyB\xf5\x01\n#com.google.cloud.networkservices.v1B\x14ServiceLbPolicyProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1.service_lb_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networkservices.v1B\x14ServiceLbPolicyProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1'
    _globals['_SERVICELBPOLICY_AUTOCAPACITYDRAIN'].fields_by_name['enable']._loaded_options = None
    _globals['_SERVICELBPOLICY_AUTOCAPACITYDRAIN'].fields_by_name['enable']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICELBPOLICY_FAILOVERCONFIG'].fields_by_name['failover_health_threshold']._loaded_options = None
    _globals['_SERVICELBPOLICY_FAILOVERCONFIG'].fields_by_name['failover_health_threshold']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICELBPOLICY_ISOLATIONCONFIG'].fields_by_name['isolation_granularity']._loaded_options = None
    _globals['_SERVICELBPOLICY_ISOLATIONCONFIG'].fields_by_name['isolation_granularity']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICELBPOLICY_ISOLATIONCONFIG'].fields_by_name['isolation_mode']._loaded_options = None
    _globals['_SERVICELBPOLICY_ISOLATIONCONFIG'].fields_by_name['isolation_mode']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICELBPOLICY_LABELSENTRY']._loaded_options = None
    _globals['_SERVICELBPOLICY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SERVICELBPOLICY'].fields_by_name['name']._loaded_options = None
    _globals['_SERVICELBPOLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SERVICELBPOLICY'].fields_by_name['create_time']._loaded_options = None
    _globals['_SERVICELBPOLICY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SERVICELBPOLICY'].fields_by_name['update_time']._loaded_options = None
    _globals['_SERVICELBPOLICY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SERVICELBPOLICY'].fields_by_name['labels']._loaded_options = None
    _globals['_SERVICELBPOLICY'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICELBPOLICY'].fields_by_name['description']._loaded_options = None
    _globals['_SERVICELBPOLICY'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICELBPOLICY'].fields_by_name['load_balancing_algorithm']._loaded_options = None
    _globals['_SERVICELBPOLICY'].fields_by_name['load_balancing_algorithm']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICELBPOLICY'].fields_by_name['auto_capacity_drain']._loaded_options = None
    _globals['_SERVICELBPOLICY'].fields_by_name['auto_capacity_drain']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICELBPOLICY'].fields_by_name['failover_config']._loaded_options = None
    _globals['_SERVICELBPOLICY'].fields_by_name['failover_config']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICELBPOLICY'].fields_by_name['isolation_config']._loaded_options = None
    _globals['_SERVICELBPOLICY'].fields_by_name['isolation_config']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICELBPOLICY']._loaded_options = None
    _globals['_SERVICELBPOLICY']._serialized_options = b'\xeaA\x7f\n.networkservices.googleapis.com/ServiceLbPolicy\x12Mprojects/{project}/locations/{location}/serviceLbPolicies/{service_lb_policy}'
    _globals['_LISTSERVICELBPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSERVICELBPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.networkservices.googleapis.com/ServiceLbPolicy'
    _globals['_GETSERVICELBPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSERVICELBPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.networkservices.googleapis.com/ServiceLbPolicy'
    _globals['_CREATESERVICELBPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESERVICELBPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.networkservices.googleapis.com/ServiceLbPolicy'
    _globals['_CREATESERVICELBPOLICYREQUEST'].fields_by_name['service_lb_policy_id']._loaded_options = None
    _globals['_CREATESERVICELBPOLICYREQUEST'].fields_by_name['service_lb_policy_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESERVICELBPOLICYREQUEST'].fields_by_name['service_lb_policy']._loaded_options = None
    _globals['_CREATESERVICELBPOLICYREQUEST'].fields_by_name['service_lb_policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESERVICELBPOLICYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESERVICELBPOLICYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESERVICELBPOLICYREQUEST'].fields_by_name['service_lb_policy']._loaded_options = None
    _globals['_UPDATESERVICELBPOLICYREQUEST'].fields_by_name['service_lb_policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESERVICELBPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESERVICELBPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.networkservices.googleapis.com/ServiceLbPolicy'
    _globals['_SERVICELBPOLICY']._serialized_start = 220
    _globals['_SERVICELBPOLICY']._serialized_end = 1686
    _globals['_SERVICELBPOLICY_AUTOCAPACITYDRAIN']._serialized_start = 881
    _globals['_SERVICELBPOLICY_AUTOCAPACITYDRAIN']._serialized_end = 921
    _globals['_SERVICELBPOLICY_FAILOVERCONFIG']._serialized_start = 923
    _globals['_SERVICELBPOLICY_FAILOVERCONFIG']._serialized_end = 979
    _globals['_SERVICELBPOLICY_ISOLATIONCONFIG']._serialized_start = 982
    _globals['_SERVICELBPOLICY_ISOLATIONCONFIG']._serialized_end = 1199
    _globals['_SERVICELBPOLICY_LABELSENTRY']._serialized_start = 1201
    _globals['_SERVICELBPOLICY_LABELSENTRY']._serialized_end = 1246
    _globals['_SERVICELBPOLICY_LOADBALANCINGALGORITHM']._serialized_start = 1249
    _globals['_SERVICELBPOLICY_LOADBALANCINGALGORITHM']._serialized_end = 1404
    _globals['_SERVICELBPOLICY_ISOLATIONGRANULARITY']._serialized_start = 1406
    _globals['_SERVICELBPOLICY_ISOLATIONGRANULARITY']._serialized_end = 1479
    _globals['_SERVICELBPOLICY_ISOLATIONMODE']._serialized_start = 1481
    _globals['_SERVICELBPOLICY_ISOLATIONMODE']._serialized_end = 1553
    _globals['_LISTSERVICELBPOLICIESREQUEST']._serialized_start = 1689
    _globals['_LISTSERVICELBPOLICIESREQUEST']._serialized_end = 1830
    _globals['_LISTSERVICELBPOLICIESRESPONSE']._serialized_start = 1833
    _globals['_LISTSERVICELBPOLICIESRESPONSE']._serialized_end = 1989
    _globals['_GETSERVICELBPOLICYREQUEST']._serialized_start = 1991
    _globals['_GETSERVICELBPOLICYREQUEST']._serialized_end = 2088
    _globals['_CREATESERVICELBPOLICYREQUEST']._serialized_start = 2091
    _globals['_CREATESERVICELBPOLICYREQUEST']._serialized_end = 2310
    _globals['_UPDATESERVICELBPOLICYREQUEST']._serialized_start = 2313
    _globals['_UPDATESERVICELBPOLICYREQUEST']._serialized_end = 2479
    _globals['_DELETESERVICELBPOLICYREQUEST']._serialized_start = 2481
    _globals['_DELETESERVICELBPOLICYREQUEST']._serialized_end = 2581