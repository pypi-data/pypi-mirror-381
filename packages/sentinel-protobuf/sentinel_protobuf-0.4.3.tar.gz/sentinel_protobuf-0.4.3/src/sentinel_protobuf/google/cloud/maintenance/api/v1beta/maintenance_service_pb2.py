"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/maintenance/api/v1beta/maintenance_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/maintenance/api/v1beta/maintenance_service.proto\x12#google.cloud.maintenance.api.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb4\x01\n\x1cSummarizeMaintenancesRequest\x12G\n\x06parent\x18\x96N \x01(\tB6\xe0A\x02\xfaA0\x12.maintenance.googleapis.com/ResourceMaintenance\x12\x12\n\tpage_size\x18\x89R \x01(\x05\x12\x13\n\npage_token\x18\x8aR \x01(\t\x12\x0f\n\x06filter\x18\x8bR \x01(\t\x12\x11\n\x08order_by\x18\x8cR \x01(\t"\xa4\x01\n\x1dSummarizeMaintenancesResponse\x12N\n\x0cmaintenances\x18\x8dR \x03(\x0b27.google.cloud.maintenance.api.v1beta.MaintenanceSummary\x12\x18\n\x0fnext_page_token\x18\x8eR \x01(\t\x12\x19\n\x0bunreachable\x18\x8fR \x03(\tB\x03\xe0A\x06"\xa6\x06\n\x12MaintenanceSummary\x12\x1d\n\x10maintenance_name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x12\n\x05title\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x03\x12O\n\x08category\x18\r \x01(\x0e28.google.cloud.maintenance.api.v1beta.MaintenanceCategoryB\x03\xe0A\x03\x12I\n maintenance_scheduled_start_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12G\n\x1emaintenance_scheduled_end_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12?\n\x16maintenance_start_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\x14maintenance_end_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1e\n\x11user_controllable\x18\n \x01(\x08B\x03\xe0A\x03\x12N\n\x08controls\x18\x0e \x03(\x0b27.google.cloud.maintenance.api.v1beta.MaintenanceControlB\x03\xe0A\x03\x12Q\n\x05stats\x18\x0c \x03(\x0b2=.google.cloud.maintenance.api.v1beta.MaintenanceSummary.StatsB\x03\xe0A\x03\x1ap\n\x05Stats\x12\x10\n\x08group_by\x18\x01 \x01(\t\x12U\n\naggregates\x18\x02 \x03(\x0b2A.google.cloud.maintenance.api.v1beta.MaintenanceSummary.Aggregate\x1a)\n\tAggregate\x12\r\n\x05group\x18\x01 \x01(\t\x12\r\n\x05count\x18\x02 \x01(\x03"\xc8\r\n\x13ResourceMaintenance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12X\n\x08resource\x18\x02 \x01(\x0b2A.google.cloud.maintenance.api.v1beta.ResourceMaintenance.ResourceB\x03\xe0A\x03\x12^\n\x0bmaintenance\x18\x03 \x01(\x0b2D.google.cloud.maintenance.api.v1beta.ResourceMaintenance.MaintenanceB\x03\xe0A\x03\x12R\n\x05state\x18\x04 \x01(\x0e2>.google.cloud.maintenance.api.v1beta.ResourceMaintenance.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12?\n\x16maintenance_start_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\x14maintenance_end_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12@\n\x17maintenance_cancel_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12I\n maintenance_scheduled_start_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12G\n\x1emaintenance_scheduled_end_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1e\n\x11user_controllable\x18\x0c \x01(\x08B\x03\xe0A\x03\x12N\n\x08controls\x18\r \x03(\x0b27.google.cloud.maintenance.api.v1beta.MaintenanceControlB\x03\xe0A\x03\x12Z\n\x06labels\x18\xa1Q \x03(\x0b2D.google.cloud.maintenance.api.v1beta.ResourceMaintenance.LabelsEntryB\x03\xe0A\x01\x12d\n\x0bannotations\x18\xa2Q \x03(\x0b2I.google.cloud.maintenance.api.v1beta.ResourceMaintenance.AnnotationsEntryB\x03\xe0A\x01\x12\x19\n\x03uid\x18\xd9O \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x12\n\x04etag\x18\xdaO \x01(\tB\x03\xe0A\x03\x1aP\n\x08Resource\x12\x1a\n\rresource_name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08location\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04type\x18\x03 \x01(\tB\x03\xe0A\x03\x1a\xa6\x01\n\x0bMaintenance\x12\x18\n\x10maintenance_name\x18\x01 \x01(\t\x12\x12\n\x05title\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x03\x12O\n\x08category\x18\x04 \x01(\x0e28.google.cloud.maintenance.api.v1beta.MaintenanceCategoryB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"X\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSCHEDULED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\r\n\tSUCCEEDED\x10\x04:\xb4\x01\xeaA\xb0\x01\n.maintenance.googleapis.com/ResourceMaintenance\x12Sprojects/{project}/locations/{location}/resourceMaintenances/{resource_maintenance}*\x14resourceMaintenances2\x13resourceMaintenance"\xe2\x01\n\x12MaintenanceControl\x12P\n\x07control\x18\x01 \x01(\x0e2?.google.cloud.maintenance.api.v1beta.MaintenanceControl.Control\x12\x11\n\tis_custom\x18\x02 \x01(\x08\x12\x15\n\rdocumentation\x18\x03 \x01(\t"P\n\x07Control\x12\x17\n\x13CONTROL_UNSPECIFIED\x10\x00\x12\t\n\x05APPLY\x10\x01\x12\x11\n\rMANAGE_POLICY\x10\x02\x12\x0e\n\nRESCHEDULE\x10\x03"\xb7\x01\n\x1fListResourceMaintenancesRequest\x12G\n\x06parent\x18\x96N \x01(\tB6\xe0A\x02\xfaA0\x12.maintenance.googleapis.com/ResourceMaintenance\x12\x12\n\tpage_size\x18\x89R \x01(\x05\x12\x13\n\npage_token\x18\x8aR \x01(\t\x12\x0f\n\x06filter\x18\x8bR \x01(\t\x12\x11\n\x08order_by\x18\x8cR \x01(\t"\xac\x01\n ListResourceMaintenancesResponse\x12X\n\x15resource_maintenances\x18\x8dR \x03(\x0b28.google.cloud.maintenance.api.v1beta.ResourceMaintenance\x12\x18\n\x0fnext_page_token\x18\x8eR \x01(\t\x12\x14\n\x0bunreachable\x18\x8fR \x03(\t"f\n\x1dGetResourceMaintenanceRequest\x12E\n\x04name\x18\x91N \x01(\tB6\xe0A\x02\xfaA0\n.maintenance.googleapis.com/ResourceMaintenance*c\n\x13MaintenanceCategory\x12$\n MAINTENANCE_CATEGORY_UNSPECIFIED\x10\x00\x12\x12\n\x0eINFRASTRUCTURE\x10\x01\x12\x12\n\x0eSERVICE_UPDATE\x10\x032\xb6\x06\n\x0bMaintenance\x12\xf7\x01\n\x15SummarizeMaintenances\x12A.google.cloud.maintenance.api.v1beta.SummarizeMaintenancesRequest\x1aB.google.cloud.maintenance.api.v1beta.SummarizeMaintenancesResponse"W\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v1beta/{parent=projects/*/locations/*}/resourceMaintenances:summarize\x12\xf6\x01\n\x18ListResourceMaintenances\x12D.google.cloud.maintenance.api.v1beta.ListResourceMaintenancesRequest\x1aE.google.cloud.maintenance.api.v1beta.ListResourceMaintenancesResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1beta/{parent=projects/*/locations/*}/resourceMaintenances\x12\xe3\x01\n\x16GetResourceMaintenance\x12B.google.cloud.maintenance.api.v1beta.GetResourceMaintenanceRequest\x1a8.google.cloud.maintenance.api.v1beta.ResourceMaintenance"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1beta/{name=projects/*/locations/*/resourceMaintenances/*}\x1aN\xcaA\x1amaintenance.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBw\n\'com.google.cloud.maintenance.api.v1betaB\x0fUMMServiceProtoP\x01Z9cloud.google.com/go/maintenance/api/apiv1beta/apipb;apipbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.maintenance.api.v1beta.maintenance_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.maintenance.api.v1betaB\x0fUMMServiceProtoP\x01Z9cloud.google.com/go/maintenance/api/apiv1beta/apipb;apipb"
    _globals['_SUMMARIZEMAINTENANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SUMMARIZEMAINTENANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.maintenance.googleapis.com/ResourceMaintenance'
    _globals['_SUMMARIZEMAINTENANCESRESPONSE'].fields_by_name['unreachable']._loaded_options = None
    _globals['_SUMMARIZEMAINTENANCESRESPONSE'].fields_by_name['unreachable']._serialized_options = b'\xe0A\x06'
    _globals['_MAINTENANCESUMMARY'].fields_by_name['maintenance_name']._loaded_options = None
    _globals['_MAINTENANCESUMMARY'].fields_by_name['maintenance_name']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCESUMMARY'].fields_by_name['title']._loaded_options = None
    _globals['_MAINTENANCESUMMARY'].fields_by_name['title']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCESUMMARY'].fields_by_name['description']._loaded_options = None
    _globals['_MAINTENANCESUMMARY'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCESUMMARY'].fields_by_name['category']._loaded_options = None
    _globals['_MAINTENANCESUMMARY'].fields_by_name['category']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCESUMMARY'].fields_by_name['maintenance_scheduled_start_time']._loaded_options = None
    _globals['_MAINTENANCESUMMARY'].fields_by_name['maintenance_scheduled_start_time']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCESUMMARY'].fields_by_name['maintenance_scheduled_end_time']._loaded_options = None
    _globals['_MAINTENANCESUMMARY'].fields_by_name['maintenance_scheduled_end_time']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCESUMMARY'].fields_by_name['maintenance_start_time']._loaded_options = None
    _globals['_MAINTENANCESUMMARY'].fields_by_name['maintenance_start_time']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCESUMMARY'].fields_by_name['maintenance_end_time']._loaded_options = None
    _globals['_MAINTENANCESUMMARY'].fields_by_name['maintenance_end_time']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCESUMMARY'].fields_by_name['user_controllable']._loaded_options = None
    _globals['_MAINTENANCESUMMARY'].fields_by_name['user_controllable']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCESUMMARY'].fields_by_name['controls']._loaded_options = None
    _globals['_MAINTENANCESUMMARY'].fields_by_name['controls']._serialized_options = b'\xe0A\x03'
    _globals['_MAINTENANCESUMMARY'].fields_by_name['stats']._loaded_options = None
    _globals['_MAINTENANCESUMMARY'].fields_by_name['stats']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE_RESOURCE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE_RESOURCE'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE_RESOURCE'].fields_by_name['location']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE_RESOURCE'].fields_by_name['location']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE_RESOURCE'].fields_by_name['type']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE_RESOURCE'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE_MAINTENANCE'].fields_by_name['title']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE_MAINTENANCE'].fields_by_name['title']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE_MAINTENANCE'].fields_by_name['description']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE_MAINTENANCE'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE_MAINTENANCE'].fields_by_name['category']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE_MAINTENANCE'].fields_by_name['category']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE_LABELSENTRY']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_RESOURCEMAINTENANCE_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['name']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['resource']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['resource']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['maintenance']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['maintenance']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['state']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['maintenance_start_time']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['maintenance_start_time']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['maintenance_end_time']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['maintenance_end_time']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['maintenance_cancel_time']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['maintenance_cancel_time']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['maintenance_scheduled_start_time']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['maintenance_scheduled_start_time']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['maintenance_scheduled_end_time']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['maintenance_scheduled_end_time']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['user_controllable']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['user_controllable']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['controls']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['controls']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['labels']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['annotations']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['uid']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['etag']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEMAINTENANCE']._loaded_options = None
    _globals['_RESOURCEMAINTENANCE']._serialized_options = b'\xeaA\xb0\x01\n.maintenance.googleapis.com/ResourceMaintenance\x12Sprojects/{project}/locations/{location}/resourceMaintenances/{resource_maintenance}*\x14resourceMaintenances2\x13resourceMaintenance'
    _globals['_LISTRESOURCEMAINTENANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRESOURCEMAINTENANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.maintenance.googleapis.com/ResourceMaintenance'
    _globals['_GETRESOURCEMAINTENANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRESOURCEMAINTENANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.maintenance.googleapis.com/ResourceMaintenance'
    _globals['_MAINTENANCE']._loaded_options = None
    _globals['_MAINTENANCE']._serialized_options = b'\xcaA\x1amaintenance.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MAINTENANCE'].methods_by_name['SummarizeMaintenances']._loaded_options = None
    _globals['_MAINTENANCE'].methods_by_name['SummarizeMaintenances']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v1beta/{parent=projects/*/locations/*}/resourceMaintenances:summarize'
    _globals['_MAINTENANCE'].methods_by_name['ListResourceMaintenances']._loaded_options = None
    _globals['_MAINTENANCE'].methods_by_name['ListResourceMaintenances']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1beta/{parent=projects/*/locations/*}/resourceMaintenances'
    _globals['_MAINTENANCE'].methods_by_name['GetResourceMaintenance']._loaded_options = None
    _globals['_MAINTENANCE'].methods_by_name['GetResourceMaintenance']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1beta/{name=projects/*/locations/*/resourceMaintenances/*}'
    _globals['_MAINTENANCECATEGORY']._serialized_start = 3871
    _globals['_MAINTENANCECATEGORY']._serialized_end = 3970
    _globals['_SUMMARIZEMAINTENANCESREQUEST']._serialized_start = 280
    _globals['_SUMMARIZEMAINTENANCESREQUEST']._serialized_end = 460
    _globals['_SUMMARIZEMAINTENANCESRESPONSE']._serialized_start = 463
    _globals['_SUMMARIZEMAINTENANCESRESPONSE']._serialized_end = 627
    _globals['_MAINTENANCESUMMARY']._serialized_start = 630
    _globals['_MAINTENANCESUMMARY']._serialized_end = 1436
    _globals['_MAINTENANCESUMMARY_STATS']._serialized_start = 1281
    _globals['_MAINTENANCESUMMARY_STATS']._serialized_end = 1393
    _globals['_MAINTENANCESUMMARY_AGGREGATE']._serialized_start = 1395
    _globals['_MAINTENANCESUMMARY_AGGREGATE']._serialized_end = 1436
    _globals['_RESOURCEMAINTENANCE']._serialized_start = 1439
    _globals['_RESOURCEMAINTENANCE']._serialized_end = 3175
    _globals['_RESOURCEMAINTENANCE_RESOURCE']._serialized_start = 2554
    _globals['_RESOURCEMAINTENANCE_RESOURCE']._serialized_end = 2634
    _globals['_RESOURCEMAINTENANCE_MAINTENANCE']._serialized_start = 2637
    _globals['_RESOURCEMAINTENANCE_MAINTENANCE']._serialized_end = 2803
    _globals['_RESOURCEMAINTENANCE_LABELSENTRY']._serialized_start = 2805
    _globals['_RESOURCEMAINTENANCE_LABELSENTRY']._serialized_end = 2850
    _globals['_RESOURCEMAINTENANCE_ANNOTATIONSENTRY']._serialized_start = 2852
    _globals['_RESOURCEMAINTENANCE_ANNOTATIONSENTRY']._serialized_end = 2902
    _globals['_RESOURCEMAINTENANCE_STATE']._serialized_start = 2904
    _globals['_RESOURCEMAINTENANCE_STATE']._serialized_end = 2992
    _globals['_MAINTENANCECONTROL']._serialized_start = 3178
    _globals['_MAINTENANCECONTROL']._serialized_end = 3404
    _globals['_MAINTENANCECONTROL_CONTROL']._serialized_start = 3324
    _globals['_MAINTENANCECONTROL_CONTROL']._serialized_end = 3404
    _globals['_LISTRESOURCEMAINTENANCESREQUEST']._serialized_start = 3407
    _globals['_LISTRESOURCEMAINTENANCESREQUEST']._serialized_end = 3590
    _globals['_LISTRESOURCEMAINTENANCESRESPONSE']._serialized_start = 3593
    _globals['_LISTRESOURCEMAINTENANCESRESPONSE']._serialized_end = 3765
    _globals['_GETRESOURCEMAINTENANCEREQUEST']._serialized_start = 3767
    _globals['_GETRESOURCEMAINTENANCEREQUEST']._serialized_end = 3869
    _globals['_MAINTENANCE']._serialized_start = 3973
    _globals['_MAINTENANCE']._serialized_end = 4795