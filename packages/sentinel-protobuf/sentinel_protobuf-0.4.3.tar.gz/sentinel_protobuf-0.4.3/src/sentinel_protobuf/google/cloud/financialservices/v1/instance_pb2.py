"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/financialservices/v1/instance.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.financialservices.v1 import bigquery_destination_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_bigquery__destination__pb2
from .....google.cloud.financialservices.v1 import line_of_business_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_line__of__business__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/financialservices/v1/instance.proto\x12!google.cloud.financialservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a<google/cloud/financialservices/v1/bigquery_destination.proto\x1a8google/cloud/financialservices/v1/line_of_business.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa2\x04\n\x08Instance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12E\n\x05state\x18\x04 \x01(\x0e21.google.cloud.financialservices.v1.Instance.StateB\x03\xe0A\x03\x12G\n\x06labels\x18\x05 \x03(\x0b27.google.cloud.financialservices.v1.Instance.LabelsEntry\x12\x14\n\x07kms_key\x18\x06 \x01(\tB\x03\xe0A\x02\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04:l\xeaAi\n)financialservices.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}"\x9a\x01\n\x14ListInstancesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x85\x01\n\x15ListInstancesResponse\x12>\n\tinstances\x18\x01 \x03(\x0b2+.google.cloud.financialservices.v1.Instance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"U\n\x12GetInstanceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance"\xc9\x01\n\x15CreateInstanceRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12B\n\x08instance\x18\x03 \x01(\x0b2+.google.cloud.financialservices.v1.InstanceB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xaa\x01\n\x15UpdateInstanceRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12B\n\x08instance\x18\x02 \x01(\x0b2+.google.cloud.financialservices.v1.InstanceB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"q\n\x15DeleteInstanceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x8f\x03\n\x1eImportRegisteredPartiesRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12\x19\n\x0cparty_tables\x18\x02 \x03(\tB\x03\xe0A\x01\x12_\n\x04mode\x18\x03 \x01(\x0e2L.google.cloud.financialservices.v1.ImportRegisteredPartiesRequest.UpdateModeB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01\x12P\n\x10line_of_business\x18\x05 \x01(\x0e21.google.cloud.financialservices.v1.LineOfBusinessB\x03\xe0A\x02"B\n\nUpdateMode\x12\x1b\n\x17UPDATE_MODE_UNSPECIFIED\x10\x00\x12\x0b\n\x07REPLACE\x10\x01\x12\n\n\x06APPEND\x10\x02"\xe4\x01\n\x1fImportRegisteredPartiesResponse\x12\x15\n\rparties_added\x18\x01 \x01(\x03\x12\x17\n\x0fparties_removed\x18\x02 \x01(\x03\x12\x15\n\rparties_total\x18\x03 \x01(\x03\x12 \n\x18parties_failed_to_remove\x18\x04 \x01(\x03\x12\x18\n\x10parties_uptiered\x18\x05 \x01(\x03\x12\x1a\n\x12parties_downtiered\x18\x06 \x01(\x03\x12"\n\x1aparties_failed_to_downtier\x18\x07 \x01(\x03"\x81\x02\n\x1eExportRegisteredPartiesRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12L\n\x07dataset\x18\x02 \x01(\x0b26.google.cloud.financialservices.v1.BigQueryDestinationB\x03\xe0A\x02\x12P\n\x10line_of_business\x18\x03 \x01(\x0e21.google.cloud.financialservices.v1.LineOfBusinessB\x03\xe0A\x02"!\n\x1fExportRegisteredPartiesResponseB\xfc\x01\n%com.google.cloud.financialservices.v1B\rInstanceProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.financialservices.v1.instance_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.financialservices.v1B\rInstanceProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1'
    _globals['_INSTANCE_LABELSENTRY']._loaded_options = None
    _globals['_INSTANCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INSTANCE'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['update_time']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['state']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_INSTANCE'].fields_by_name['kms_key']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['kms_key']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE']._loaded_options = None
    _globals['_INSTANCE']._serialized_options = b'\xeaAi\n)financialservices.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}'
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSTANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEINSTANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['instance']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEINSTANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEINSTANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTREGISTEREDPARTIESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_IMPORTREGISTEREDPARTIESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_IMPORTREGISTEREDPARTIESREQUEST'].fields_by_name['party_tables']._loaded_options = None
    _globals['_IMPORTREGISTEREDPARTIESREQUEST'].fields_by_name['party_tables']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTREGISTEREDPARTIESREQUEST'].fields_by_name['mode']._loaded_options = None
    _globals['_IMPORTREGISTEREDPARTIESREQUEST'].fields_by_name['mode']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTREGISTEREDPARTIESREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_IMPORTREGISTEREDPARTIESREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTREGISTEREDPARTIESREQUEST'].fields_by_name['line_of_business']._loaded_options = None
    _globals['_IMPORTREGISTEREDPARTIESREQUEST'].fields_by_name['line_of_business']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTREGISTEREDPARTIESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTREGISTEREDPARTIESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_EXPORTREGISTEREDPARTIESREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_EXPORTREGISTEREDPARTIESREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTREGISTEREDPARTIESREQUEST'].fields_by_name['line_of_business']._loaded_options = None
    _globals['_EXPORTREGISTEREDPARTIESREQUEST'].fields_by_name['line_of_business']._serialized_options = b'\xe0A\x02'
    _globals['_INSTANCE']._serialized_start = 335
    _globals['_INSTANCE']._serialized_end = 881
    _globals['_INSTANCE_LABELSENTRY']._serialized_start = 640
    _globals['_INSTANCE_LABELSENTRY']._serialized_end = 685
    _globals['_INSTANCE_STATE']._serialized_start = 687
    _globals['_INSTANCE_STATE']._serialized_end = 771
    _globals['_LISTINSTANCESREQUEST']._serialized_start = 884
    _globals['_LISTINSTANCESREQUEST']._serialized_end = 1038
    _globals['_LISTINSTANCESRESPONSE']._serialized_start = 1041
    _globals['_LISTINSTANCESRESPONSE']._serialized_end = 1174
    _globals['_GETINSTANCEREQUEST']._serialized_start = 1176
    _globals['_GETINSTANCEREQUEST']._serialized_end = 1261
    _globals['_CREATEINSTANCEREQUEST']._serialized_start = 1264
    _globals['_CREATEINSTANCEREQUEST']._serialized_end = 1465
    _globals['_UPDATEINSTANCEREQUEST']._serialized_start = 1468
    _globals['_UPDATEINSTANCEREQUEST']._serialized_end = 1638
    _globals['_DELETEINSTANCEREQUEST']._serialized_start = 1640
    _globals['_DELETEINSTANCEREQUEST']._serialized_end = 1753
    _globals['_IMPORTREGISTEREDPARTIESREQUEST']._serialized_start = 1756
    _globals['_IMPORTREGISTEREDPARTIESREQUEST']._serialized_end = 2155
    _globals['_IMPORTREGISTEREDPARTIESREQUEST_UPDATEMODE']._serialized_start = 2089
    _globals['_IMPORTREGISTEREDPARTIESREQUEST_UPDATEMODE']._serialized_end = 2155
    _globals['_IMPORTREGISTEREDPARTIESRESPONSE']._serialized_start = 2158
    _globals['_IMPORTREGISTEREDPARTIESRESPONSE']._serialized_end = 2386
    _globals['_EXPORTREGISTEREDPARTIESREQUEST']._serialized_start = 2389
    _globals['_EXPORTREGISTEREDPARTIESREQUEST']._serialized_end = 2646
    _globals['_EXPORTREGISTEREDPARTIESRESPONSE']._serialized_start = 2648
    _globals['_EXPORTREGISTEREDPARTIESRESPONSE']._serialized_end = 2681