"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkmanagement/v1beta1/connectivity_test.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.networkmanagement.v1beta1 import trace_pb2 as google_dot_cloud_dot_networkmanagement_dot_v1beta1_dot_trace__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/networkmanagement/v1beta1/connectivity_test.proto\x12&google.cloud.networkmanagement.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/networkmanagement/v1beta1/trace.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xcc\x07\n\x10ConnectivityTest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12E\n\x06source\x18\x03 \x01(\x0b20.google.cloud.networkmanagement.v1beta1.EndpointB\x03\xe0A\x02\x12J\n\x0bdestination\x18\x04 \x01(\x0b20.google.cloud.networkmanagement.v1beta1.EndpointB\x03\xe0A\x02\x12\x10\n\x08protocol\x18\x05 \x01(\t\x12\x18\n\x10related_projects\x18\x06 \x03(\t\x12\x19\n\x0cdisplay_name\x18\x07 \x01(\tB\x03\xe0A\x03\x12T\n\x06labels\x18\x08 \x03(\x0b2D.google.cloud.networkmanagement.v1beta1.ConnectivityTest.LabelsEntry\x124\n\x0bcreate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12^\n\x14reachability_details\x18\x0c \x01(\x0b2;.google.cloud.networkmanagement.v1beta1.ReachabilityDetailsB\x03\xe0A\x03\x12T\n\x0fprobing_details\x18\x0e \x01(\x0b26.google.cloud.networkmanagement.v1beta1.ProbingDetailsB\x03\xe0A\x03\x12\x12\n\nround_trip\x18\x0f \x01(\x08\x12e\n\x1breturn_reachability_details\x18\x10 \x01(\x0b2;.google.cloud.networkmanagement.v1beta1.ReachabilityDetailsB\x03\xe0A\x03\x12\x1e\n\x16bypass_firewall_checks\x18\x11 \x01(\x08\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:t\xeaAq\n1networkmanagement.googleapis.com/ConnectivityTest\x12<projects/{project}/locations/global/connectivityTests/{test}"\x8f\n\n\x08Endpoint\x12\x12\n\nip_address\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x10\n\x08instance\x18\x03 \x01(\t\x12\x17\n\x0fforwarding_rule\x18\r \x01(\t\x12o\n\x16forwarding_rule_target\x18\x0e \x01(\x0e2E.google.cloud.networkmanagement.v1beta1.Endpoint.ForwardingRuleTargetB\x03\xe0A\x03H\x00\x88\x01\x01\x12"\n\x10load_balancer_id\x18\x0f \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12^\n\x12load_balancer_type\x18\x10 \x01(\x0e28.google.cloud.networkmanagement.v1beta1.LoadBalancerTypeB\x03\xe0A\x03H\x02\x88\x01\x01\x12\x1a\n\x12gke_master_cluster\x18\x07 \x01(\t\x12\x0c\n\x04fqdn\x18\x13 \x01(\t\x12\x1a\n\x12cloud_sql_instance\x18\x08 \x01(\t\x12\x16\n\x0eredis_instance\x18\x11 \x01(\t\x12\x15\n\rredis_cluster\x18\x12 \x01(\t\x12^\n\x0ecloud_function\x18\n \x01(\x0b2F.google.cloud.networkmanagement.v1beta1.Endpoint.CloudFunctionEndpoint\x12e\n\x12app_engine_version\x18\x0b \x01(\x0b2I.google.cloud.networkmanagement.v1beta1.Endpoint.AppEngineVersionEndpoint\x12e\n\x12cloud_run_revision\x18\x0c \x01(\x0b2I.google.cloud.networkmanagement.v1beta1.Endpoint.CloudRunRevisionEndpoint\x12\x0f\n\x07network\x18\x04 \x01(\t\x12R\n\x0cnetwork_type\x18\x05 \x01(\x0e2<.google.cloud.networkmanagement.v1beta1.Endpoint.NetworkType\x12\x12\n\nproject_id\x18\x06 \x01(\t\x1a$\n\x15CloudFunctionEndpoint\x12\x0b\n\x03uri\x18\x01 \x01(\t\x1a\'\n\x18AppEngineVersionEndpoint\x12\x0b\n\x03uri\x18\x01 \x01(\t\x1aA\n\x18CloudRunRevisionEndpoint\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x18\n\x0bservice_uri\x18\x02 \x01(\tB\x03\xe0A\x03"Q\n\x0bNetworkType\x12\x1c\n\x18NETWORK_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bGCP_NETWORK\x10\x01\x12\x13\n\x0fNON_GCP_NETWORK\x10\x02"y\n\x14ForwardingRuleTarget\x12&\n"FORWARDING_RULE_TARGET_UNSPECIFIED\x10\x00\x12\x0c\n\x08INSTANCE\x10\x01\x12\x11\n\rLOAD_BALANCER\x10\x02\x12\x0f\n\x0bVPN_GATEWAY\x10\x03\x12\x07\n\x03PSC\x10\x04B\x19\n\x17_forwarding_rule_targetB\x13\n\x11_load_balancer_idB\x15\n\x13_load_balancer_type"\xdf\x02\n\x13ReachabilityDetails\x12R\n\x06result\x18\x01 \x01(\x0e2B.google.cloud.networkmanagement.v1beta1.ReachabilityDetails.Result\x12/\n\x0bverify_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12!\n\x05error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12=\n\x06traces\x18\x05 \x03(\x0b2-.google.cloud.networkmanagement.v1beta1.Trace"a\n\x06Result\x12\x16\n\x12RESULT_UNSPECIFIED\x10\x00\x12\r\n\tREACHABLE\x10\x01\x12\x0f\n\x0bUNREACHABLE\x10\x02\x12\r\n\tAMBIGUOUS\x10\x04\x12\x10\n\x0cUNDETERMINED\x10\x05"<\n\x11LatencyPercentile\x12\x0f\n\x07percent\x18\x01 \x01(\x05\x12\x16\n\x0elatency_micros\x18\x02 \x01(\x03"m\n\x13LatencyDistribution\x12V\n\x13latency_percentiles\x18\x01 \x03(\x0b29.google.cloud.networkmanagement.v1beta1.LatencyPercentile"\xf9\n\n\x0eProbingDetails\x12T\n\x06result\x18\x01 \x01(\x0e2D.google.cloud.networkmanagement.v1beta1.ProbingDetails.ProbingResult\x12/\n\x0bverify_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12!\n\x05error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12]\n\x0babort_cause\x18\x04 \x01(\x0e2H.google.cloud.networkmanagement.v1beta1.ProbingDetails.ProbingAbortCause\x12\x18\n\x10sent_probe_count\x18\x05 \x01(\x05\x12\x1e\n\x16successful_probe_count\x18\x06 \x01(\x05\x12K\n\rendpoint_info\x18\x07 \x01(\x0b24.google.cloud.networkmanagement.v1beta1.EndpointInfo\x12T\n\x0fprobing_latency\x18\x08 \x01(\x0b2;.google.cloud.networkmanagement.v1beta1.LatencyDistribution\x12h\n\x1bdestination_egress_location\x18\t \x01(\x0b2C.google.cloud.networkmanagement.v1beta1.ProbingDetails.EdgeLocation\x12a\n\x0eedge_responses\x18\n \x03(\x0b2I.google.cloud.networkmanagement.v1beta1.ProbingDetails.SingleEdgeResponse\x12\x1a\n\x12probed_all_devices\x18\x0b \x01(\x08\x1a)\n\x0cEdgeLocation\x12\x19\n\x11metropolitan_area\x18\x01 \x01(\t\x1a\x80\x03\n\x12SingleEdgeResponse\x12T\n\x06result\x18\x01 \x01(\x0e2D.google.cloud.networkmanagement.v1beta1.ProbingDetails.ProbingResult\x12\x18\n\x10sent_probe_count\x18\x02 \x01(\x05\x12\x1e\n\x16successful_probe_count\x18\x03 \x01(\x05\x12T\n\x0fprobing_latency\x18\x04 \x01(\x0b2;.google.cloud.networkmanagement.v1beta1.LatencyDistribution\x12h\n\x1bdestination_egress_location\x18\x05 \x01(\x0b2C.google.cloud.networkmanagement.v1beta1.ProbingDetails.EdgeLocation\x12\x1a\n\x12destination_router\x18\x06 \x01(\t"\x80\x01\n\rProbingResult\x12\x1e\n\x1aPROBING_RESULT_UNSPECIFIED\x10\x00\x12\r\n\tREACHABLE\x10\x01\x12\x0f\n\x0bUNREACHABLE\x10\x02\x12\x1d\n\x19REACHABILITY_INCONSISTENT\x10\x03\x12\x10\n\x0cUNDETERMINED\x10\x04"g\n\x11ProbingAbortCause\x12#\n\x1fPROBING_ABORT_CAUSE_UNSPECIFIED\x10\x00\x12\x15\n\x11PERMISSION_DENIED\x10\x01\x12\x16\n\x12NO_SOURCE_LOCATION\x10\x02B\x96\x02\n*com.google.cloud.networkmanagement.v1beta1B\x0eTestOuterClassP\x01ZXcloud.google.com/go/networkmanagement/apiv1beta1/networkmanagementpb;networkmanagementpb\xaa\x02&Google.Cloud.NetworkManagement.V1Beta1\xca\x02&Google\\Cloud\\NetworkManagement\\V1beta1\xea\x02)Google::Cloud::NetworkManagement::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkmanagement.v1beta1.connectivity_test_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.networkmanagement.v1beta1B\x0eTestOuterClassP\x01ZXcloud.google.com/go/networkmanagement/apiv1beta1/networkmanagementpb;networkmanagementpb\xaa\x02&Google.Cloud.NetworkManagement.V1Beta1\xca\x02&Google\\Cloud\\NetworkManagement\\V1beta1\xea\x02)Google::Cloud::NetworkManagement::V1beta1'
    _globals['_CONNECTIVITYTEST_LABELSENTRY']._loaded_options = None
    _globals['_CONNECTIVITYTEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CONNECTIVITYTEST'].fields_by_name['name']._loaded_options = None
    _globals['_CONNECTIVITYTEST'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CONNECTIVITYTEST'].fields_by_name['source']._loaded_options = None
    _globals['_CONNECTIVITYTEST'].fields_by_name['source']._serialized_options = b'\xe0A\x02'
    _globals['_CONNECTIVITYTEST'].fields_by_name['destination']._loaded_options = None
    _globals['_CONNECTIVITYTEST'].fields_by_name['destination']._serialized_options = b'\xe0A\x02'
    _globals['_CONNECTIVITYTEST'].fields_by_name['display_name']._loaded_options = None
    _globals['_CONNECTIVITYTEST'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIVITYTEST'].fields_by_name['create_time']._loaded_options = None
    _globals['_CONNECTIVITYTEST'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIVITYTEST'].fields_by_name['update_time']._loaded_options = None
    _globals['_CONNECTIVITYTEST'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIVITYTEST'].fields_by_name['reachability_details']._loaded_options = None
    _globals['_CONNECTIVITYTEST'].fields_by_name['reachability_details']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIVITYTEST'].fields_by_name['probing_details']._loaded_options = None
    _globals['_CONNECTIVITYTEST'].fields_by_name['probing_details']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIVITYTEST'].fields_by_name['return_reachability_details']._loaded_options = None
    _globals['_CONNECTIVITYTEST'].fields_by_name['return_reachability_details']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIVITYTEST']._loaded_options = None
    _globals['_CONNECTIVITYTEST']._serialized_options = b'\xeaAq\n1networkmanagement.googleapis.com/ConnectivityTest\x12<projects/{project}/locations/global/connectivityTests/{test}'
    _globals['_ENDPOINT_CLOUDRUNREVISIONENDPOINT'].fields_by_name['service_uri']._loaded_options = None
    _globals['_ENDPOINT_CLOUDRUNREVISIONENDPOINT'].fields_by_name['service_uri']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['forwarding_rule_target']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['forwarding_rule_target']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['load_balancer_id']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['load_balancer_id']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['load_balancer_type']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['load_balancer_type']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTIVITYTEST']._serialized_start = 277
    _globals['_CONNECTIVITYTEST']._serialized_end = 1249
    _globals['_CONNECTIVITYTEST_LABELSENTRY']._serialized_start = 1086
    _globals['_CONNECTIVITYTEST_LABELSENTRY']._serialized_end = 1131
    _globals['_ENDPOINT']._serialized_start = 1252
    _globals['_ENDPOINT']._serialized_end = 2547
    _globals['_ENDPOINT_CLOUDFUNCTIONENDPOINT']._serialized_start = 2126
    _globals['_ENDPOINT_CLOUDFUNCTIONENDPOINT']._serialized_end = 2162
    _globals['_ENDPOINT_APPENGINEVERSIONENDPOINT']._serialized_start = 2164
    _globals['_ENDPOINT_APPENGINEVERSIONENDPOINT']._serialized_end = 2203
    _globals['_ENDPOINT_CLOUDRUNREVISIONENDPOINT']._serialized_start = 2205
    _globals['_ENDPOINT_CLOUDRUNREVISIONENDPOINT']._serialized_end = 2270
    _globals['_ENDPOINT_NETWORKTYPE']._serialized_start = 2272
    _globals['_ENDPOINT_NETWORKTYPE']._serialized_end = 2353
    _globals['_ENDPOINT_FORWARDINGRULETARGET']._serialized_start = 2355
    _globals['_ENDPOINT_FORWARDINGRULETARGET']._serialized_end = 2476
    _globals['_REACHABILITYDETAILS']._serialized_start = 2550
    _globals['_REACHABILITYDETAILS']._serialized_end = 2901
    _globals['_REACHABILITYDETAILS_RESULT']._serialized_start = 2804
    _globals['_REACHABILITYDETAILS_RESULT']._serialized_end = 2901
    _globals['_LATENCYPERCENTILE']._serialized_start = 2903
    _globals['_LATENCYPERCENTILE']._serialized_end = 2963
    _globals['_LATENCYDISTRIBUTION']._serialized_start = 2965
    _globals['_LATENCYDISTRIBUTION']._serialized_end = 3074
    _globals['_PROBINGDETAILS']._serialized_start = 3077
    _globals['_PROBINGDETAILS']._serialized_end = 4478
    _globals['_PROBINGDETAILS_EDGELOCATION']._serialized_start = 3814
    _globals['_PROBINGDETAILS_EDGELOCATION']._serialized_end = 3855
    _globals['_PROBINGDETAILS_SINGLEEDGERESPONSE']._serialized_start = 3858
    _globals['_PROBINGDETAILS_SINGLEEDGERESPONSE']._serialized_end = 4242
    _globals['_PROBINGDETAILS_PROBINGRESULT']._serialized_start = 4245
    _globals['_PROBINGDETAILS_PROBINGRESULT']._serialized_end = 4373
    _globals['_PROBINGDETAILS_PROBINGABORTCAUSE']._serialized_start = 4375
    _globals['_PROBINGDETAILS_PROBINGABORTCAUSE']._serialized_end = 4478