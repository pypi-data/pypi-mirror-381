"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/lustre/v1/instance.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/cloud/lustre/v1/instance.proto\x12\x16google.cloud.lustre.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa5\x06\n\x08Instance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1a\n\nfilesystem\x18\n \x01(\tB\x06\xe0A\x05\xe0A\x02\x12\x19\n\x0ccapacity_gib\x18\x02 \x01(\x03B\x03\xe0A\x02\x12:\n\x07network\x18\x03 \x01(\tB)\xe0A\x05\xe0A\x02\xfaA \n\x1ecompute.googleapis.com/Network\x12:\n\x05state\x18\x04 \x01(\x0e2&.google.cloud.lustre.v1.Instance.StateB\x03\xe0A\x03\x12\x18\n\x0bmount_point\x18\x05 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x08 \x01(\tB\x03\xe0A\x01\x12A\n\x06labels\x18\t \x03(\x0b2,.google.cloud.lustre.v1.Instance.LabelsEntryB\x03\xe0A\x01\x12(\n\x1bper_unit_storage_throughput\x18\x0b \x01(\x03B\x03\xe0A\x02\x12"\n\x13gke_support_enabled\x18\x0c \x01(\x08B\x05\x18\x01\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x7f\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0c\n\x08CREATING\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\r\n\tUPGRADING\x10\x04\x12\r\n\tREPAIRING\x10\x05\x12\x0b\n\x07STOPPED\x10\x06\x12\x0c\n\x08UPDATING\x10\x07:v\xeaAs\n\x1elustre.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}*\tinstances2\x08instance"\xab\x01\n\x14ListInstancesRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1elustre.googleapis.com/Instance\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x7f\n\x15ListInstancesResponse\x123\n\tinstances\x18\x01 \x03(\x0b2 .google.cloud.lustre.v1.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x18\n\x0bunreachable\x18\x03 \x03(\tB\x03\xe0A\x06"J\n\x12GetInstanceRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1elustre.googleapis.com/Instance"\xc3\x01\n\x15CreateInstanceRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1elustre.googleapis.com/Instance\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x127\n\x08instance\x18\x03 \x01(\x0b2 .google.cloud.lustre.v1.InstanceB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xa7\x01\n\x15UpdateInstanceRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x127\n\x08instance\x18\x02 \x01(\x0b2 .google.cloud.lustre.v1.InstanceB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"n\n\x15DeleteInstanceRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1elustre.googleapis.com/Instance\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x03Ba\n\x1acom.google.cloud.lustre.v1B\rInstanceProtoP\x01Z2cloud.google.com/go/lustre/apiv1/lustrepb;lustrepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.lustre.v1.instance_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.lustre.v1B\rInstanceProtoP\x01Z2cloud.google.com/go/lustre/apiv1/lustrepb;lustrepb'
    _globals['_INSTANCE_LABELSENTRY']._loaded_options = None
    _globals['_INSTANCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_INSTANCE'].fields_by_name['filesystem']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['filesystem']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_INSTANCE'].fields_by_name['capacity_gib']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['capacity_gib']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE'].fields_by_name['network']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['network']._serialized_options = b'\xe0A\x05\xe0A\x02\xfaA \n\x1ecompute.googleapis.com/Network'
    _globals['_INSTANCE'].fields_by_name['state']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['mount_point']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['mount_point']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['description']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE'].fields_by_name['labels']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_INSTANCE'].fields_by_name['per_unit_storage_throughput']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['per_unit_storage_throughput']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE'].fields_by_name['gke_support_enabled']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['gke_support_enabled']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_INSTANCE']._loaded_options = None
    _globals['_INSTANCE']._serialized_options = b'\xeaAs\n\x1elustre.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}*\tinstances2\x08instance'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1elustre.googleapis.com/Instance'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSTANCESRESPONSE'].fields_by_name['unreachable']._loaded_options = None
    _globals['_LISTINSTANCESRESPONSE'].fields_by_name['unreachable']._serialized_options = b'\xe0A\x06'
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1elustre.googleapis.com/Instance'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1elustre.googleapis.com/Instance'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1elustre.googleapis.com/Instance'
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE']._serialized_start = 222
    _globals['_INSTANCE']._serialized_end = 1027
    _globals['_INSTANCE_LABELSENTRY']._serialized_start = 733
    _globals['_INSTANCE_LABELSENTRY']._serialized_end = 778
    _globals['_INSTANCE_STATE']._serialized_start = 780
    _globals['_INSTANCE_STATE']._serialized_end = 907
    _globals['_LISTINSTANCESREQUEST']._serialized_start = 1030
    _globals['_LISTINSTANCESREQUEST']._serialized_end = 1201
    _globals['_LISTINSTANCESRESPONSE']._serialized_start = 1203
    _globals['_LISTINSTANCESRESPONSE']._serialized_end = 1330
    _globals['_GETINSTANCEREQUEST']._serialized_start = 1332
    _globals['_GETINSTANCEREQUEST']._serialized_end = 1406
    _globals['_CREATEINSTANCEREQUEST']._serialized_start = 1409
    _globals['_CREATEINSTANCEREQUEST']._serialized_end = 1604
    _globals['_UPDATEINSTANCEREQUEST']._serialized_start = 1607
    _globals['_UPDATEINSTANCEREQUEST']._serialized_end = 1774
    _globals['_DELETEINSTANCEREQUEST']._serialized_start = 1776
    _globals['_DELETEINSTANCEREQUEST']._serialized_end = 1886
    _globals['_OPERATIONMETADATA']._serialized_start = 1889
    _globals['_OPERATIONMETADATA']._serialized_end = 2145