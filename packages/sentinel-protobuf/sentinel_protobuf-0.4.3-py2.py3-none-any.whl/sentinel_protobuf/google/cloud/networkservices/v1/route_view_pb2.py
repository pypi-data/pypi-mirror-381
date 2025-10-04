"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkservices/v1/route_view.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/networkservices/v1/route_view.proto\x12\x1fgoogle.cloud.networkservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc9\x02\n\x10GatewayRouteView\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12!\n\x14route_project_number\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x1b\n\x0eroute_location\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x17\n\nroute_type\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08route_id\x18\x05 \x01(\tB\x03\xe0A\x03:\xae\x01\xeaA\xaa\x01\n/networkservices.googleapis.com/GatewayRouteView\x12Rprojects/{project}/locations/{location}/gateways/{gateway}/routeViews/{route_view}*\x11gatewayRouteViews2\x10gatewayRouteView"\xb8\x02\n\rMeshRouteView\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12!\n\x14route_project_number\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x1b\n\x0eroute_location\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x17\n\nroute_type\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08route_id\x18\x05 \x01(\tB\x03\xe0A\x03:\xa0\x01\xeaA\x9c\x01\n,networkservices.googleapis.com/MeshRouteView\x12Mprojects/{project}/locations/{location}/meshes/{mesh}/routeViews/{route_view}*\x0emeshRouteViews2\rmeshRouteView"c\n\x1aGetGatewayRouteViewRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/networkservices.googleapis.com/GatewayRouteView"]\n\x17GetMeshRouteViewRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,networkservices.googleapis.com/MeshRouteView"\x8e\x01\n\x1cListGatewayRouteViewsRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\x12/networkservices.googleapis.com/GatewayRouteView\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x88\x01\n\x19ListMeshRouteViewsRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,networkservices.googleapis.com/MeshRouteView\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x9d\x01\n\x1dListGatewayRouteViewsResponse\x12N\n\x13gateway_route_views\x18\x01 \x03(\x0b21.google.cloud.networkservices.v1.GatewayRouteView\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\x94\x01\n\x1aListMeshRouteViewsResponse\x12H\n\x10mesh_route_views\x18\x01 \x03(\x0b2..google.cloud.networkservices.v1.MeshRouteView\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\tB\xef\x01\n#com.google.cloud.networkservices.v1B\x0eRouteViewProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1.route_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networkservices.v1B\x0eRouteViewProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1'
    _globals['_GATEWAYROUTEVIEW'].fields_by_name['name']._loaded_options = None
    _globals['_GATEWAYROUTEVIEW'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_GATEWAYROUTEVIEW'].fields_by_name['route_project_number']._loaded_options = None
    _globals['_GATEWAYROUTEVIEW'].fields_by_name['route_project_number']._serialized_options = b'\xe0A\x03'
    _globals['_GATEWAYROUTEVIEW'].fields_by_name['route_location']._loaded_options = None
    _globals['_GATEWAYROUTEVIEW'].fields_by_name['route_location']._serialized_options = b'\xe0A\x03'
    _globals['_GATEWAYROUTEVIEW'].fields_by_name['route_type']._loaded_options = None
    _globals['_GATEWAYROUTEVIEW'].fields_by_name['route_type']._serialized_options = b'\xe0A\x03'
    _globals['_GATEWAYROUTEVIEW'].fields_by_name['route_id']._loaded_options = None
    _globals['_GATEWAYROUTEVIEW'].fields_by_name['route_id']._serialized_options = b'\xe0A\x03'
    _globals['_GATEWAYROUTEVIEW']._loaded_options = None
    _globals['_GATEWAYROUTEVIEW']._serialized_options = b'\xeaA\xaa\x01\n/networkservices.googleapis.com/GatewayRouteView\x12Rprojects/{project}/locations/{location}/gateways/{gateway}/routeViews/{route_view}*\x11gatewayRouteViews2\x10gatewayRouteView'
    _globals['_MESHROUTEVIEW'].fields_by_name['name']._loaded_options = None
    _globals['_MESHROUTEVIEW'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_MESHROUTEVIEW'].fields_by_name['route_project_number']._loaded_options = None
    _globals['_MESHROUTEVIEW'].fields_by_name['route_project_number']._serialized_options = b'\xe0A\x03'
    _globals['_MESHROUTEVIEW'].fields_by_name['route_location']._loaded_options = None
    _globals['_MESHROUTEVIEW'].fields_by_name['route_location']._serialized_options = b'\xe0A\x03'
    _globals['_MESHROUTEVIEW'].fields_by_name['route_type']._loaded_options = None
    _globals['_MESHROUTEVIEW'].fields_by_name['route_type']._serialized_options = b'\xe0A\x03'
    _globals['_MESHROUTEVIEW'].fields_by_name['route_id']._loaded_options = None
    _globals['_MESHROUTEVIEW'].fields_by_name['route_id']._serialized_options = b'\xe0A\x03'
    _globals['_MESHROUTEVIEW']._loaded_options = None
    _globals['_MESHROUTEVIEW']._serialized_options = b'\xeaA\x9c\x01\n,networkservices.googleapis.com/MeshRouteView\x12Mprojects/{project}/locations/{location}/meshes/{mesh}/routeViews/{route_view}*\x0emeshRouteViews2\rmeshRouteView'
    _globals['_GETGATEWAYROUTEVIEWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETGATEWAYROUTEVIEWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/networkservices.googleapis.com/GatewayRouteView'
    _globals['_GETMESHROUTEVIEWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMESHROUTEVIEWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,networkservices.googleapis.com/MeshRouteView'
    _globals['_LISTGATEWAYROUTEVIEWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTGATEWAYROUTEVIEWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\x12/networkservices.googleapis.com/GatewayRouteView'
    _globals['_LISTMESHROUTEVIEWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMESHROUTEVIEWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,networkservices.googleapis.com/MeshRouteView'
    _globals['_GATEWAYROUTEVIEW']._serialized_start = 146
    _globals['_GATEWAYROUTEVIEW']._serialized_end = 475
    _globals['_MESHROUTEVIEW']._serialized_start = 478
    _globals['_MESHROUTEVIEW']._serialized_end = 790
    _globals['_GETGATEWAYROUTEVIEWREQUEST']._serialized_start = 792
    _globals['_GETGATEWAYROUTEVIEWREQUEST']._serialized_end = 891
    _globals['_GETMESHROUTEVIEWREQUEST']._serialized_start = 893
    _globals['_GETMESHROUTEVIEWREQUEST']._serialized_end = 986
    _globals['_LISTGATEWAYROUTEVIEWSREQUEST']._serialized_start = 989
    _globals['_LISTGATEWAYROUTEVIEWSREQUEST']._serialized_end = 1131
    _globals['_LISTMESHROUTEVIEWSREQUEST']._serialized_start = 1134
    _globals['_LISTMESHROUTEVIEWSREQUEST']._serialized_end = 1270
    _globals['_LISTGATEWAYROUTEVIEWSRESPONSE']._serialized_start = 1273
    _globals['_LISTGATEWAYROUTEVIEWSRESPONSE']._serialized_end = 1430
    _globals['_LISTMESHROUTEVIEWSRESPONSE']._serialized_start = 1433
    _globals['_LISTMESHROUTEVIEWSRESPONSE']._serialized_end = 1581