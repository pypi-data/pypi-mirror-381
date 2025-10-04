"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2beta/control_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2beta import control_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_control__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/retail/v2beta/control_service.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/retail/v2beta/control.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xa1\x01\n\x14CreateControlRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x129\n\x07control\x18\x02 \x01(\x0b2#.google.cloud.retail.v2beta.ControlB\x03\xe0A\x02\x12\x17\n\ncontrol_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x82\x01\n\x14UpdateControlRequest\x129\n\x07control\x18\x01 \x01(\x0b2#.google.cloud.retail.v2beta.ControlB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"K\n\x14DeleteControlRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Control"H\n\x11GetControlRequest\x123\n\x04name\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Control"\x92\x01\n\x13ListControlsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"f\n\x14ListControlsResponse\x125\n\x08controls\x18\x01 \x03(\x0b2#.google.cloud.retail.v2beta.Control\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x9c\x08\n\x0eControlService\x12\xd0\x01\n\rCreateControl\x120.google.cloud.retail.v2beta.CreateControlRequest\x1a#.google.cloud.retail.v2beta.Control"h\xdaA\x19parent,control,control_id\x82\xd3\xe4\x93\x02F";/v2beta/{parent=projects/*/locations/*/catalogs/*}/controls:\x07control\x12\xa5\x01\n\rDeleteControl\x120.google.cloud.retail.v2beta.DeleteControlRequest\x1a\x16.google.protobuf.Empty"J\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v2beta/{name=projects/*/locations/*/catalogs/*/controls/*}\x12\xd2\x01\n\rUpdateControl\x120.google.cloud.retail.v2beta.UpdateControlRequest\x1a#.google.cloud.retail.v2beta.Control"j\xdaA\x13control,update_mask\x82\xd3\xe4\x93\x02N2C/v2beta/{control.name=projects/*/locations/*/catalogs/*/controls/*}:\x07control\x12\xac\x01\n\nGetControl\x12-.google.cloud.retail.v2beta.GetControlRequest\x1a#.google.cloud.retail.v2beta.Control"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v2beta/{name=projects/*/locations/*/catalogs/*/controls/*}\x12\xbf\x01\n\x0cListControls\x12/.google.cloud.retail.v2beta.ListControlsRequest\x1a0.google.cloud.retail.v2beta.ListControlsResponse"L\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v2beta/{parent=projects/*/locations/*/catalogs/*}/controls\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd2\x01\n\x1ecom.google.cloud.retail.v2betaB\x13ControlServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.control_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x13ControlServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
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
    _globals['_CONTROLSERVICE'].methods_by_name['CreateControl']._serialized_options = b'\xdaA\x19parent,control,control_id\x82\xd3\xe4\x93\x02F";/v2beta/{parent=projects/*/locations/*/catalogs/*}/controls:\x07control'
    _globals['_CONTROLSERVICE'].methods_by_name['DeleteControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['DeleteControl']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v2beta/{name=projects/*/locations/*/catalogs/*/controls/*}'
    _globals['_CONTROLSERVICE'].methods_by_name['UpdateControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['UpdateControl']._serialized_options = b'\xdaA\x13control,update_mask\x82\xd3\xe4\x93\x02N2C/v2beta/{control.name=projects/*/locations/*/catalogs/*/controls/*}:\x07control'
    _globals['_CONTROLSERVICE'].methods_by_name['GetControl']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['GetControl']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v2beta/{name=projects/*/locations/*/catalogs/*/controls/*}'
    _globals['_CONTROLSERVICE'].methods_by_name['ListControls']._loaded_options = None
    _globals['_CONTROLSERVICE'].methods_by_name['ListControls']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v2beta/{parent=projects/*/locations/*/catalogs/*}/controls'
    _globals['_CREATECONTROLREQUEST']._serialized_start = 301
    _globals['_CREATECONTROLREQUEST']._serialized_end = 462
    _globals['_UPDATECONTROLREQUEST']._serialized_start = 465
    _globals['_UPDATECONTROLREQUEST']._serialized_end = 595
    _globals['_DELETECONTROLREQUEST']._serialized_start = 597
    _globals['_DELETECONTROLREQUEST']._serialized_end = 672
    _globals['_GETCONTROLREQUEST']._serialized_start = 674
    _globals['_GETCONTROLREQUEST']._serialized_end = 746
    _globals['_LISTCONTROLSREQUEST']._serialized_start = 749
    _globals['_LISTCONTROLSREQUEST']._serialized_end = 895
    _globals['_LISTCONTROLSRESPONSE']._serialized_start = 897
    _globals['_LISTCONTROLSRESPONSE']._serialized_end = 999
    _globals['_CONTROLSERVICE']._serialized_start = 1002
    _globals['_CONTROLSERVICE']._serialized_end = 2054