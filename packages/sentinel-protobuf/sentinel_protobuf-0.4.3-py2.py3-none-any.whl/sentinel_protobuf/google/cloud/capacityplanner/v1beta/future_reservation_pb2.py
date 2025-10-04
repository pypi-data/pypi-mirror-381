"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/capacityplanner/v1beta/future_reservation.proto')
_sym_db = _symbol_database.Default()
from .....google.cloud.capacityplanner.v1beta import allocation_pb2 as google_dot_cloud_dot_capacityplanner_dot_v1beta_dot_allocation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/capacityplanner/v1beta/future_reservation.proto\x12#google.cloud.capacityplanner.v1beta\x1a4google/cloud/capacityplanner/v1beta/allocation.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc1\x0b\n\x11FutureReservation\x12o\n\x17specific_sku_properties\x18\x08 \x01(\x0b2L.google.cloud.capacityplanner.v1beta.FutureReservation.SpecificSKUPropertiesH\x00\x12\n\n\x02id\x18\x01 \x01(\x03\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04zone\x18\x05 \x01(\t\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12\x1a\n\x12future_reservation\x18\x07 \x01(\t\x12\x18\n\x10owner_project_id\x18\x0f \x01(\t\x12V\n\x0btime_window\x18\t \x01(\x0b2A.google.cloud.capacityplanner.v1beta.FutureReservation.TimeWindow\x12U\n\x0eshare_settings\x18\n \x01(\x0b2=.google.cloud.capacityplanner.v1beta.Allocation.ShareSettings\x12\x13\n\x0bname_prefix\x18\x0b \x01(\t\x12M\n\x06status\x18\x0c \x01(\x0b2=.google.cloud.capacityplanner.v1beta.FutureReservation.Status\x12I\n%auto_created_reservations_delete_time\x18\r \x01(\x0b2\x1a.google.protobuf.Timestamp\x12-\n%auto_delete_auto_created_reservations\x18\x0e \x01(\x08\x1a\xac\x01\n\x15SpecificSKUProperties\x12~\n\x13instance_properties\x18\x01 \x01(\x0b2a.google.cloud.capacityplanner.v1beta.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties\x12\x13\n\x0btotal_count\x18\x02 \x01(\x03\x1aj\n\nTimeWindow\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\xf4\x03\n\x06Status\x12k\n\x12procurement_status\x18\x01 \x01(\x0e2O.google.cloud.capacityplanner.v1beta.FutureReservation.Status.ProcurementStatus\x12-\n\tlock_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12!\n\x19auto_created_reservations\x18\x03 \x03(\t\x12\x17\n\x0ffulfilled_count\x18\x04 \x01(\x03"\x91\x02\n\x11ProcurementStatus\x12"\n\x1ePROCUREMENT_STATUS_UNSPECIFIED\x10\x00\x12\x14\n\x10PENDING_APPROVAL\x10\x01\x12\x0c\n\x08APPROVED\x10\x02\x12\r\n\tCOMMITTED\x10\x03\x12\x0c\n\x08DECLINED\x10\x04\x12\r\n\tCANCELLED\x10\x05\x12\r\n\tPROCURING\x10\x06\x12\x10\n\x0cPROVISIONING\x10\x07\x12\r\n\tFULFILLED\x10\x08\x12\n\n\x06FAILED\x10\t\x12\x1e\n\x1aFAILED_PARTIALLY_FULFILLED\x10\n\x12\x0c\n\x08DRAFTING\x10\x0b\x12\x1e\n\x1aPENDING_AMENDMENT_APPROVAL\x10\x0cB\x06\n\x04typeB\x8b\x02\n\'com.google.cloud.capacityplanner.v1betaB\x16FutureReservationProtoP\x01ZQcloud.google.com/go/capacityplanner/apiv1beta/capacityplannerpb;capacityplannerpb\xaa\x02#Google.Cloud.CapacityPlanner.V1Beta\xca\x02#Google\\Cloud\\CapacityPlanner\\V1beta\xea\x02&Google::Cloud::CapacityPlanner::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.capacityplanner.v1beta.future_reservation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.capacityplanner.v1betaB\x16FutureReservationProtoP\x01ZQcloud.google.com/go/capacityplanner/apiv1beta/capacityplannerpb;capacityplannerpb\xaa\x02#Google.Cloud.CapacityPlanner.V1Beta\xca\x02#Google\\Cloud\\CapacityPlanner\\V1beta\xea\x02&Google::Cloud::CapacityPlanner::V1beta"
    _globals['_FUTURERESERVATION']._serialized_start = 189
    _globals['_FUTURERESERVATION']._serialized_end = 1662
    _globals['_FUTURERESERVATION_SPECIFICSKUPROPERTIES']._serialized_start = 871
    _globals['_FUTURERESERVATION_SPECIFICSKUPROPERTIES']._serialized_end = 1043
    _globals['_FUTURERESERVATION_TIMEWINDOW']._serialized_start = 1045
    _globals['_FUTURERESERVATION_TIMEWINDOW']._serialized_end = 1151
    _globals['_FUTURERESERVATION_STATUS']._serialized_start = 1154
    _globals['_FUTURERESERVATION_STATUS']._serialized_end = 1654
    _globals['_FUTURERESERVATION_STATUS_PROCUREMENTSTATUS']._serialized_start = 1381
    _globals['_FUTURERESERVATION_STATUS_PROCUREMENTSTATUS']._serialized_end = 1654