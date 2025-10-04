"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkservices/v1/gateway.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.networkservices.v1 import common_pb2 as google_dot_cloud_dot_networkservices_dot_v1_dot_common__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/networkservices/v1/gateway.proto\x12\x1fgoogle.cloud.networkservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/networkservices/v1/common.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x84\x0b\n\x07Gateway\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x16\n\tself_link\x18\r \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12I\n\x06labels\x18\x04 \x03(\x0b24.google.cloud.networkservices.v1.Gateway.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01\x12@\n\x04type\x18\x06 \x01(\x0e2-.google.cloud.networkservices.v1.Gateway.TypeB\x03\xe0A\x05\x129\n\taddresses\x18\x07 \x03(\tB&\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Address\x12\x12\n\x05ports\x18\x0b \x03(\x05B\x03\xe0A\x02\x12\x12\n\x05scope\x18\x08 \x01(\tB\x03\xe0A\x01\x12Q\n\x11server_tls_policy\x18\t \x01(\tB6\xe0A\x01\xfaA0\n.networksecurity.googleapis.com/ServerTlsPolicy\x12O\n\x10certificate_urls\x18\x0e \x03(\tB5\xe0A\x01\xfaA/\n-certificatemanager.googleapis.com/Certificate\x12]\n\x17gateway_security_policy\x18\x12 \x01(\tB<\xe0A\x01\xfaA6\n4networksecurity.googleapis.com/GatewaySecurityPolicy\x127\n\x07network\x18\x10 \x01(\tB&\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Network\x12=\n\nsubnetwork\x18\x11 \x01(\tB)\xe0A\x01\xfaA#\n!compute.googleapis.com/Subnetwork\x12K\n\nip_version\x18\x15 \x01(\x0e22.google.cloud.networkservices.v1.Gateway.IpVersionB\x03\xe0A\x01\x12N\n\renvoy_headers\x18\x1c \x01(\x0e2-.google.cloud.networkservices.v1.EnvoyHeadersB\x03\xe0A\x01H\x00\x88\x01\x01\x12O\n\x0crouting_mode\x18  \x01(\x0e24.google.cloud.networkservices.v1.Gateway.RoutingModeB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"C\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\r\n\tOPEN_MESH\x10\x01\x12\x16\n\x12SECURE_WEB_GATEWAY\x10\x02";\n\tIpVersion\x12\x1a\n\x16IP_VERSION_UNSPECIFIED\x10\x00\x12\x08\n\x04IPV4\x10\x01\x12\x08\n\x04IPV6\x10\x02"C\n\x0bRoutingMode\x12\x19\n\x15EXPLICIT_ROUTING_MODE\x10\x00\x12\x19\n\x15NEXT_HOP_ROUTING_MODE\x10\x01:g\xeaAd\n&networkservices.googleapis.com/Gateway\x12:projects/{project}/locations/{location}/gateways/{gateway}B\x10\n\x0e_envoy_headers"|\n\x13ListGatewaysRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&networkservices.googleapis.com/Gateway\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x80\x01\n\x14ListGatewaysResponse\x12:\n\x08gateways\x18\x01 \x03(\x0b2(.google.cloud.networkservices.v1.Gateway\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"Q\n\x11GetGatewayRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&networkservices.googleapis.com/Gateway"\xaf\x01\n\x14CreateGatewayRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&networkservices.googleapis.com/Gateway\x12\x17\n\ngateway_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12>\n\x07gateway\x18\x03 \x01(\x0b2(.google.cloud.networkservices.v1.GatewayB\x03\xe0A\x02"\x8c\x01\n\x14UpdateGatewayRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12>\n\x07gateway\x18\x02 \x01(\x0b2(.google.cloud.networkservices.v1.GatewayB\x03\xe0A\x02"T\n\x14DeleteGatewayRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&networkservices.googleapis.com/GatewayB\x89\x06\n#com.google.cloud.networkservices.v1B\x0cGatewayProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1\xeaA\x91\x01\n4networksecurity.googleapis.com/GatewaySecurityPolicy\x12Yprojects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy}\xeaAa\n!compute.googleapis.com/Subnetwork\x12<projects/{project}/regions/{region}/subnetworks/{subnetwork}\xeaAN\n\x1ecompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}\xeaAY\n\x1ecompute.googleapis.com/Address\x127projects/{project}/regions/{region}/addresses/{address}\xeaAs\n-certificatemanager.googleapis.com/Certificate\x12Bprojects/{project}/locations/{location}/certificates/{certificate}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1.gateway_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networkservices.v1B\x0cGatewayProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1\xeaA\x91\x01\n4networksecurity.googleapis.com/GatewaySecurityPolicy\x12Yprojects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy}\xeaAa\n!compute.googleapis.com/Subnetwork\x12<projects/{project}/regions/{region}/subnetworks/{subnetwork}\xeaAN\n\x1ecompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}\xeaAY\n\x1ecompute.googleapis.com/Address\x127projects/{project}/regions/{region}/addresses/{address}\xeaAs\n-certificatemanager.googleapis.com/Certificate\x12Bprojects/{project}/locations/{location}/certificates/{certificate}'
    _globals['_GATEWAY_LABELSENTRY']._loaded_options = None
    _globals['_GATEWAY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_GATEWAY'].fields_by_name['name']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_GATEWAY'].fields_by_name['self_link']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['self_link']._serialized_options = b'\xe0A\x03'
    _globals['_GATEWAY'].fields_by_name['create_time']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_GATEWAY'].fields_by_name['update_time']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_GATEWAY'].fields_by_name['labels']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_GATEWAY'].fields_by_name['description']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_GATEWAY'].fields_by_name['type']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_GATEWAY'].fields_by_name['addresses']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['addresses']._serialized_options = b'\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Address'
    _globals['_GATEWAY'].fields_by_name['ports']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['ports']._serialized_options = b'\xe0A\x02'
    _globals['_GATEWAY'].fields_by_name['scope']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['scope']._serialized_options = b'\xe0A\x01'
    _globals['_GATEWAY'].fields_by_name['server_tls_policy']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['server_tls_policy']._serialized_options = b'\xe0A\x01\xfaA0\n.networksecurity.googleapis.com/ServerTlsPolicy'
    _globals['_GATEWAY'].fields_by_name['certificate_urls']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['certificate_urls']._serialized_options = b'\xe0A\x01\xfaA/\n-certificatemanager.googleapis.com/Certificate'
    _globals['_GATEWAY'].fields_by_name['gateway_security_policy']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['gateway_security_policy']._serialized_options = b'\xe0A\x01\xfaA6\n4networksecurity.googleapis.com/GatewaySecurityPolicy'
    _globals['_GATEWAY'].fields_by_name['network']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['network']._serialized_options = b'\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Network'
    _globals['_GATEWAY'].fields_by_name['subnetwork']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['subnetwork']._serialized_options = b'\xe0A\x01\xfaA#\n!compute.googleapis.com/Subnetwork'
    _globals['_GATEWAY'].fields_by_name['ip_version']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['ip_version']._serialized_options = b'\xe0A\x01'
    _globals['_GATEWAY'].fields_by_name['envoy_headers']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['envoy_headers']._serialized_options = b'\xe0A\x01'
    _globals['_GATEWAY'].fields_by_name['routing_mode']._loaded_options = None
    _globals['_GATEWAY'].fields_by_name['routing_mode']._serialized_options = b'\xe0A\x01'
    _globals['_GATEWAY']._loaded_options = None
    _globals['_GATEWAY']._serialized_options = b'\xeaAd\n&networkservices.googleapis.com/Gateway\x12:projects/{project}/locations/{location}/gateways/{gateway}'
    _globals['_LISTGATEWAYSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTGATEWAYSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&networkservices.googleapis.com/Gateway'
    _globals['_GETGATEWAYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETGATEWAYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&networkservices.googleapis.com/Gateway'
    _globals['_CREATEGATEWAYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEGATEWAYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&networkservices.googleapis.com/Gateway'
    _globals['_CREATEGATEWAYREQUEST'].fields_by_name['gateway_id']._loaded_options = None
    _globals['_CREATEGATEWAYREQUEST'].fields_by_name['gateway_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEGATEWAYREQUEST'].fields_by_name['gateway']._loaded_options = None
    _globals['_CREATEGATEWAYREQUEST'].fields_by_name['gateway']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGATEWAYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEGATEWAYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEGATEWAYREQUEST'].fields_by_name['gateway']._loaded_options = None
    _globals['_UPDATEGATEWAYREQUEST'].fields_by_name['gateway']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEGATEWAYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEGATEWAYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&networkservices.googleapis.com/Gateway'
    _globals['_GATEWAY']._serialized_start = 256
    _globals['_GATEWAY']._serialized_end = 1668
    _globals['_GATEWAY_LABELSENTRY']._serialized_start = 1301
    _globals['_GATEWAY_LABELSENTRY']._serialized_end = 1346
    _globals['_GATEWAY_TYPE']._serialized_start = 1348
    _globals['_GATEWAY_TYPE']._serialized_end = 1415
    _globals['_GATEWAY_IPVERSION']._serialized_start = 1417
    _globals['_GATEWAY_IPVERSION']._serialized_end = 1476
    _globals['_GATEWAY_ROUTINGMODE']._serialized_start = 1478
    _globals['_GATEWAY_ROUTINGMODE']._serialized_end = 1545
    _globals['_LISTGATEWAYSREQUEST']._serialized_start = 1670
    _globals['_LISTGATEWAYSREQUEST']._serialized_end = 1794
    _globals['_LISTGATEWAYSRESPONSE']._serialized_start = 1797
    _globals['_LISTGATEWAYSRESPONSE']._serialized_end = 1925
    _globals['_GETGATEWAYREQUEST']._serialized_start = 1927
    _globals['_GETGATEWAYREQUEST']._serialized_end = 2008
    _globals['_CREATEGATEWAYREQUEST']._serialized_start = 2011
    _globals['_CREATEGATEWAYREQUEST']._serialized_end = 2186
    _globals['_UPDATEGATEWAYREQUEST']._serialized_start = 2189
    _globals['_UPDATEGATEWAYREQUEST']._serialized_end = 2329
    _globals['_DELETEGATEWAYREQUEST']._serialized_start = 2331
    _globals['_DELETEGATEWAYREQUEST']._serialized_end = 2415