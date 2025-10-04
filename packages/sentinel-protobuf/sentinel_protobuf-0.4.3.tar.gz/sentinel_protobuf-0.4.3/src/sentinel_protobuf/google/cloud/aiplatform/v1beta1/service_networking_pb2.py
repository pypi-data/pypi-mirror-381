"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/service_networking.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/aiplatform/v1beta1/service_networking.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe0\x01\n\x13PSCAutomationConfig\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07network\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\nip_address\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0fforwarding_rule\x18\x04 \x01(\tB\x03\xe0A\x03\x12G\n\x05state\x18\x05 \x01(\x0e23.google.cloud.aiplatform.v1beta1.PSCAutomationStateB\x03\xe0A\x03\x12\x1a\n\rerror_message\x18\x06 \x01(\tB\x03\xe0A\x03"\x95\x02\n\x1bPrivateServiceConnectConfig\x12+\n\x1eenable_private_service_connect\x18\x01 \x01(\x08B\x03\xe0A\x02\x12\x19\n\x11project_allowlist\x18\x02 \x03(\t\x12Y\n\x16psc_automation_configs\x18\x03 \x03(\x0b24.google.cloud.aiplatform.v1beta1.PSCAutomationConfigB\x03\xe0A\x01\x122\n%enable_secure_private_service_connect\x18\x04 \x01(\x08B\x03\xe0A\x01\x12\x1f\n\x12service_attachment\x18\x05 \x01(\tB\x03\xe0A\x03"S\n\x15PscAutomatedEndpoints\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07network\x18\x02 \x01(\t\x12\x15\n\rmatch_address\x18\x03 \x01(\t"\xb7\x01\n\x12PscInterfaceConfig\x12L\n\x12network_attachment\x18\x01 \x01(\tB0\xe0A\x01\xfaA*\n(compute.googleapis.com/NetworkAttachment\x12S\n\x13dns_peering_configs\x18\x02 \x03(\x0b21.google.cloud.aiplatform.v1beta1.DnsPeeringConfigB\x03\xe0A\x01"a\n\x10DnsPeeringConfig\x12\x13\n\x06domain\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0etarget_project\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0etarget_network\x18\x03 \x01(\tB\x03\xe0A\x02*\x80\x01\n\x12PSCAutomationState\x12$\n PSC_AUTOMATION_STATE_UNSPECIFIED\x10\x00\x12#\n\x1fPSC_AUTOMATION_STATE_SUCCESSFUL\x10\x01\x12\x1f\n\x1bPSC_AUTOMATION_STATE_FAILED\x10\x02B\xe6\x02\n#com.google.cloud.aiplatform.v1beta1B\x16ServiceNetworkingProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1\xeaAv\n(compute.googleapis.com/NetworkAttachment\x12Jprojects/{project}/regions/{region}/networkAttachments/{networkattachment}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.service_networking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x16ServiceNetworkingProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1\xeaAv\n(compute.googleapis.com/NetworkAttachment\x12Jprojects/{project}/regions/{region}/networkAttachments/{networkattachment}'
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['project_id']._loaded_options = None
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['network']._loaded_options = None
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['network']._serialized_options = b'\xe0A\x02'
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['ip_address']._loaded_options = None
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['ip_address']._serialized_options = b'\xe0A\x03'
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['forwarding_rule']._loaded_options = None
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['forwarding_rule']._serialized_options = b'\xe0A\x03'
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['error_message']._loaded_options = None
    _globals['_PSCAUTOMATIONCONFIG'].fields_by_name['error_message']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATESERVICECONNECTCONFIG'].fields_by_name['enable_private_service_connect']._loaded_options = None
    _globals['_PRIVATESERVICECONNECTCONFIG'].fields_by_name['enable_private_service_connect']._serialized_options = b'\xe0A\x02'
    _globals['_PRIVATESERVICECONNECTCONFIG'].fields_by_name['psc_automation_configs']._loaded_options = None
    _globals['_PRIVATESERVICECONNECTCONFIG'].fields_by_name['psc_automation_configs']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVATESERVICECONNECTCONFIG'].fields_by_name['enable_secure_private_service_connect']._loaded_options = None
    _globals['_PRIVATESERVICECONNECTCONFIG'].fields_by_name['enable_secure_private_service_connect']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVATESERVICECONNECTCONFIG'].fields_by_name['service_attachment']._loaded_options = None
    _globals['_PRIVATESERVICECONNECTCONFIG'].fields_by_name['service_attachment']._serialized_options = b'\xe0A\x03'
    _globals['_PSCINTERFACECONFIG'].fields_by_name['network_attachment']._loaded_options = None
    _globals['_PSCINTERFACECONFIG'].fields_by_name['network_attachment']._serialized_options = b'\xe0A\x01\xfaA*\n(compute.googleapis.com/NetworkAttachment'
    _globals['_PSCINTERFACECONFIG'].fields_by_name['dns_peering_configs']._loaded_options = None
    _globals['_PSCINTERFACECONFIG'].fields_by_name['dns_peering_configs']._serialized_options = b'\xe0A\x01'
    _globals['_DNSPEERINGCONFIG'].fields_by_name['domain']._loaded_options = None
    _globals['_DNSPEERINGCONFIG'].fields_by_name['domain']._serialized_options = b'\xe0A\x02'
    _globals['_DNSPEERINGCONFIG'].fields_by_name['target_project']._loaded_options = None
    _globals['_DNSPEERINGCONFIG'].fields_by_name['target_project']._serialized_options = b'\xe0A\x02'
    _globals['_DNSPEERINGCONFIG'].fields_by_name['target_network']._loaded_options = None
    _globals['_DNSPEERINGCONFIG'].fields_by_name['target_network']._serialized_options = b'\xe0A\x02'
    _globals['_PSCAUTOMATIONSTATE']._serialized_start = 1031
    _globals['_PSCAUTOMATIONSTATE']._serialized_end = 1159
    _globals['_PSCAUTOMATIONCONFIG']._serialized_start = 154
    _globals['_PSCAUTOMATIONCONFIG']._serialized_end = 378
    _globals['_PRIVATESERVICECONNECTCONFIG']._serialized_start = 381
    _globals['_PRIVATESERVICECONNECTCONFIG']._serialized_end = 658
    _globals['_PSCAUTOMATEDENDPOINTS']._serialized_start = 660
    _globals['_PSCAUTOMATEDENDPOINTS']._serialized_end = 743
    _globals['_PSCINTERFACECONFIG']._serialized_start = 746
    _globals['_PSCINTERFACECONFIG']._serialized_end = 929
    _globals['_DNSPEERINGCONFIG']._serialized_start = 931
    _globals['_DNSPEERINGCONFIG']._serialized_end = 1028