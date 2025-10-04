"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/monitoring/v3/alert_service.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.monitoring.v3 import alert_pb2 as google_dot_monitoring_dot_v3_dot_alert__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/monitoring/v3/alert_service.proto\x12\x14google.monitoring.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/monitoring/v3/alert.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x95\x01\n\x18CreateAlertPolicyRequest\x12;\n\x04name\x18\x03 \x01(\tB-\xe0A\x02\xfaA\'\x12%monitoring.googleapis.com/AlertPolicy\x12<\n\x0calert_policy\x18\x02 \x01(\x0b2!.google.monitoring.v3.AlertPolicyB\x03\xe0A\x02"T\n\x15GetAlertPolicyRequest\x12;\n\x04name\x18\x03 \x01(\tB-\xe0A\x02\xfaA\'\n%monitoring.googleapis.com/AlertPolicy"\xb4\x01\n\x18ListAlertPoliciesRequest\x12;\n\x04name\x18\x04 \x01(\tB-\xe0A\x02\xfaA\'\x12%monitoring.googleapis.com/AlertPolicy\x12\x13\n\x06filter\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x83\x01\n\x19ListAlertPoliciesResponse\x129\n\x0ealert_policies\x18\x03 \x03(\x0b2!.google.monitoring.v3.AlertPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x04 \x01(\x05"\x8e\x01\n\x18UpdateAlertPolicyRequest\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12<\n\x0calert_policy\x18\x03 \x01(\x0b2!.google.monitoring.v3.AlertPolicyB\x03\xe0A\x02"W\n\x18DeleteAlertPolicyRequest\x12;\n\x04name\x18\x03 \x01(\tB-\xe0A\x02\xfaA\'\n%monitoring.googleapis.com/AlertPolicy2\x9e\x08\n\x12AlertPolicyService\x12\xa8\x01\n\x11ListAlertPolicies\x12..google.monitoring.v3.ListAlertPoliciesRequest\x1a/.google.monitoring.v3.ListAlertPoliciesResponse"2\xdaA\x04name\x82\xd3\xe4\x93\x02%\x12#/v3/{name=projects/*}/alertPolicies\x12\x96\x01\n\x0eGetAlertPolicy\x12+.google.monitoring.v3.GetAlertPolicyRequest\x1a!.google.monitoring.v3.AlertPolicy"4\xdaA\x04name\x82\xd3\xe4\x93\x02\'\x12%/v3/{name=projects/*/alertPolicies/*}\x12\xb5\x01\n\x11CreateAlertPolicy\x12..google.monitoring.v3.CreateAlertPolicyRequest\x1a!.google.monitoring.v3.AlertPolicy"M\xdaA\x11name,alert_policy\x82\xd3\xe4\x93\x023"#/v3/{name=projects/*}/alertPolicies:\x0calert_policy\x12\x91\x01\n\x11DeleteAlertPolicy\x12..google.monitoring.v3.DeleteAlertPolicyRequest\x1a\x16.google.protobuf.Empty"4\xdaA\x04name\x82\xd3\xe4\x93\x02\'*%/v3/{name=projects/*/alertPolicies/*}\x12\xcb\x01\n\x11UpdateAlertPolicy\x12..google.monitoring.v3.UpdateAlertPolicyRequest\x1a!.google.monitoring.v3.AlertPolicy"c\xdaA\x18update_mask,alert_policy\x82\xd3\xe4\x93\x02B22/v3/{alert_policy.name=projects/*/alertPolicies/*}:\x0calert_policy\x1a\xa9\x01\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.readB\xcc\x01\n\x18com.google.monitoring.v3B\x11AlertServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.alert_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\x11AlertServiceProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_CREATEALERTPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CREATEALERTPOLICYREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\x12%monitoring.googleapis.com/AlertPolicy"
    _globals['_CREATEALERTPOLICYREQUEST'].fields_by_name['alert_policy']._loaded_options = None
    _globals['_CREATEALERTPOLICYREQUEST'].fields_by_name['alert_policy']._serialized_options = b'\xe0A\x02'
    _globals['_GETALERTPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETALERTPOLICYREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%monitoring.googleapis.com/AlertPolicy"
    _globals['_LISTALERTPOLICIESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTALERTPOLICIESREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\x12%monitoring.googleapis.com/AlertPolicy"
    _globals['_LISTALERTPOLICIESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTALERTPOLICIESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTALERTPOLICIESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTALERTPOLICIESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTALERTPOLICIESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTALERTPOLICIESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTALERTPOLICIESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTALERTPOLICIESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEALERTPOLICYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEALERTPOLICYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEALERTPOLICYREQUEST'].fields_by_name['alert_policy']._loaded_options = None
    _globals['_UPDATEALERTPOLICYREQUEST'].fields_by_name['alert_policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEALERTPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEALERTPOLICYREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%monitoring.googleapis.com/AlertPolicy"
    _globals['_ALERTPOLICYSERVICE']._loaded_options = None
    _globals['_ALERTPOLICYSERVICE']._serialized_options = b'\xcaA\x19monitoring.googleapis.com\xd2A\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read'
    _globals['_ALERTPOLICYSERVICE'].methods_by_name['ListAlertPolicies']._loaded_options = None
    _globals['_ALERTPOLICYSERVICE'].methods_by_name['ListAlertPolicies']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02%\x12#/v3/{name=projects/*}/alertPolicies'
    _globals['_ALERTPOLICYSERVICE'].methods_by_name['GetAlertPolicy']._loaded_options = None
    _globals['_ALERTPOLICYSERVICE'].methods_by_name['GetAlertPolicy']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02'\x12%/v3/{name=projects/*/alertPolicies/*}"
    _globals['_ALERTPOLICYSERVICE'].methods_by_name['CreateAlertPolicy']._loaded_options = None
    _globals['_ALERTPOLICYSERVICE'].methods_by_name['CreateAlertPolicy']._serialized_options = b'\xdaA\x11name,alert_policy\x82\xd3\xe4\x93\x023"#/v3/{name=projects/*}/alertPolicies:\x0calert_policy'
    _globals['_ALERTPOLICYSERVICE'].methods_by_name['DeleteAlertPolicy']._loaded_options = None
    _globals['_ALERTPOLICYSERVICE'].methods_by_name['DeleteAlertPolicy']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02'*%/v3/{name=projects/*/alertPolicies/*}"
    _globals['_ALERTPOLICYSERVICE'].methods_by_name['UpdateAlertPolicy']._loaded_options = None
    _globals['_ALERTPOLICYSERVICE'].methods_by_name['UpdateAlertPolicy']._serialized_options = b'\xdaA\x18update_mask,alert_policy\x82\xd3\xe4\x93\x02B22/v3/{alert_policy.name=projects/*/alertPolicies/*}:\x0calert_policy'
    _globals['_CREATEALERTPOLICYREQUEST']._serialized_start = 279
    _globals['_CREATEALERTPOLICYREQUEST']._serialized_end = 428
    _globals['_GETALERTPOLICYREQUEST']._serialized_start = 430
    _globals['_GETALERTPOLICYREQUEST']._serialized_end = 514
    _globals['_LISTALERTPOLICIESREQUEST']._serialized_start = 517
    _globals['_LISTALERTPOLICIESREQUEST']._serialized_end = 697
    _globals['_LISTALERTPOLICIESRESPONSE']._serialized_start = 700
    _globals['_LISTALERTPOLICIESRESPONSE']._serialized_end = 831
    _globals['_UPDATEALERTPOLICYREQUEST']._serialized_start = 834
    _globals['_UPDATEALERTPOLICYREQUEST']._serialized_end = 976
    _globals['_DELETEALERTPOLICYREQUEST']._serialized_start = 978
    _globals['_DELETEALERTPOLICYREQUEST']._serialized_end = 1065
    _globals['_ALERTPOLICYSERVICE']._serialized_start = 1068
    _globals['_ALERTPOLICYSERVICE']._serialized_end = 2122