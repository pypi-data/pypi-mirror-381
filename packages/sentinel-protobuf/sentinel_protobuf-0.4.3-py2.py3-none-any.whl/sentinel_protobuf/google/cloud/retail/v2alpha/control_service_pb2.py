"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/control_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import control_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_control__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/retail/v2alpha/control_service.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/retail/v2alpha/control.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xa2\x01\n\x14CreateControlRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12:\n\x07control\x18\x02 \x01(\x0b2$.google.cloud.retail.v2alpha.ControlB\x03\xe0A\x02\x12\x17\n\ncontrol_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x83\x01\n\x14UpdateControlRequest\x12:\n\x07control\x18\x01 \x01(\x0b2$.google.cloud.retail.v2alpha.ControlB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"K\n\x14DeleteControlRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Control"H\n\x11GetControlRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Control"\x92\x01\n\x13ListControlsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"g\n\x14ListControlsResponse\x126\n\x08controls\x18\x01 \x03(\x0b2$.google.cloud.retail.v2alpha.Control\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xaa\x08\n\x0eControlService\x12\xd3\x01\n\rCreateControl\x121.google.cloud.retail.v2alpha.CreateControlRequest\x1a$.google.cloud.retail.v2alpha.Control"i\xdaA\x19parent,control,control_id\x82\xd3\xe4\x93\x02G"</v2alpha/{parent=projects/*/locations/*/catalogs/*}/controls:\x07control\x12\xa7\x01\n\rDeleteControl\x121.google.cloud.retail.v2alpha.DeleteControlRequest\x1a\x16.google.protobuf.Empty"K\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v2alpha/{name=projects/*/locations/*/catalogs/*/controls/*}\x12\xd5\x01\n\rUpdateControl\x121.google.cloud.retail.v2alpha.UpdateControlRequest\x1a$.google.cloud.retail.v2alpha.Control"k\xdaA\x13control,update_mask\x82\xd3\xe4\x93\x02O2D/v2alpha/{control.name=projects/*/locations/*/catalogs/*/controls/*}:\x07control\x12\xaf\x01\n\nGetControl\x12..google.cloud.retail.v2alpha.GetControlRequest\x1a$.google.cloud.retail.v2alpha.Control"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v2alpha/{name=projects/*/locations/*/catalogs/*/controls/*}\x12\xc2\x01\n\x0cListControls\x120.google.cloud.retail.v2alpha.ListControlsRequest\x1a1.google.cloud.retail.v2alpha.ListControlsResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v2alpha/{parent=projects/*/locations/*/catalogs/*}/controls\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd7\x01\n\x1fcom.google.cloud.retail.v2alphaB\x13ControlServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.control_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x13ControlServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_CREATECONTROLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONTROLREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_CREATECONTROLREQUEST'].fields_by_name['control']._loaded_options = None
    _globals['_CREATECONTROLREQUEST'].fields_by_name['control']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONTROLREQUEST'].fields_by_name['control_id']._loaded_options = None
    _globals['_CREATECONTROLREQUEST'].fields_by_name['control_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONTROLREQUEST'].fields_by_name['control']._loaded_options = None
    _globals['_UPDATECONTROLREQUEST'].fields_by_name['control']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECONTROLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONTROLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Control'
    _globals['_GETCONTROLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONTROLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Control'
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCONTROLSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_CONTROLSERVICE']._loaded_options = None
    _globals['_CONTROLSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONTROLSERVICE'].methods_by_name['CreateControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['CreateControl']._serialized_options = b'\xdaA\x19parent,control,control_id\x82\xd3\xe4\x93\x02G"</v2alpha/{parent=projects/*/locations/*/catalogs/*}/controls:\x07control'
    _globals['_CONTROLSERVICE'].methods_by_name['DeleteControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['DeleteControl']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v2alpha/{name=projects/*/locations/*/catalogs/*/controls/*}'
    _globals['_CONTROLSERVICE'].methods_by_name['UpdateControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['UpdateControl']._serialized_options = b'\xdaA\x13control,update_mask\x82\xd3\xe4\x93\x02O2D/v2alpha/{control.name=projects/*/locations/*/catalogs/*/controls/*}:\x07control'
    _globals['_CONTROLSERVICE'].methods_by_name['GetControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['GetControl']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v2alpha/{name=projects/*/locations/*/catalogs/*/controls/*}'
    _globals['_CONTROLSERVICE'].methods_by_name['ListControls']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['ListControls']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v2alpha/{parent=projects/*/locations/*/catalogs/*}/controls'
    _globals['_CREATECONTROLREQUEST']._serialized_start = 304
    _globals['_CREATECONTROLREQUEST']._serialized_end = 466
    _globals['_UPDATECONTROLREQUEST']._serialized_start = 469
    _globals['_UPDATECONTROLREQUEST']._serialized_end = 600
    _globals['_DELETECONTROLREQUEST']._serialized_start = 602
    _globals['_DELETECONTROLREQUEST']._serialized_end = 677
    _globals['_GETCONTROLREQUEST']._serialized_start = 679
    _globals['_GETCONTROLREQUEST']._serialized_end = 751
    _globals['_LISTCONTROLSREQUEST']._serialized_start = 754
    _globals['_LISTCONTROLSREQUEST']._serialized_end = 900
    _globals['_LISTCONTROLSRESPONSE']._serialized_start = 902
    _globals['_LISTCONTROLSRESPONSE']._serialized_end = 1005
    _globals['_CONTROLSERVICE']._serialized_start = 1008
    _globals['_CONTROLSERVICE']._serialized_end = 2074