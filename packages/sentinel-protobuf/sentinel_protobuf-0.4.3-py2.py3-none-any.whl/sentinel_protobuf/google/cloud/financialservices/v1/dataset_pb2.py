"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/financialservices/v1/dataset.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
from .....google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/financialservices/v1/dataset.proto\x12!google.cloud.financialservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoogle/type/datetime.proto\x1a\x1agoogle/type/interval.proto"\x83\x06\n\x07Dataset\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12F\n\x06labels\x18\x04 \x03(\x0b26.google.cloud.financialservices.v1.Dataset.LabelsEntry\x12T\n\x0btable_specs\x18\x05 \x03(\x0b2:.google.cloud.financialservices.v1.Dataset.TableSpecsEntryB\x03\xe0A\x02\x12D\n\x05state\x18\x07 \x01(\x0e20.google.cloud.financialservices.v1.Dataset.StateB\x03\xe0A\x03\x12.\n\ndate_range\x18\x08 \x01(\x0b2\x15.google.type.IntervalB\x03\xe0A\x02\x12(\n\ttime_zone\x18\t \x01(\x0b2\x15.google.type.TimeZone\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a1\n\x0fTableSpecsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04:\x82\x01\xeaA\x7f\n(financialservices.googleapis.com/Dataset\x12Sprojects/{project_num}/locations/{location}/instances/{instance}/datasets/{dataset}"\xa1\x01\n\x13ListDatasetsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x82\x01\n\x14ListDatasetsResponse\x12<\n\x08datasets\x18\x01 \x03(\x0b2*.google.cloud.financialservices.v1.Dataset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"S\n\x11GetDatasetRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(financialservices.googleapis.com/Dataset"\xcd\x01\n\x14CreateDatasetRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12@\n\x07dataset\x18\x03 \x01(\x0b2*.google.cloud.financialservices.v1.DatasetB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa7\x01\n\x14UpdateDatasetRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12@\n\x07dataset\x18\x02 \x01(\x0b2*.google.cloud.financialservices.v1.DatasetB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"o\n\x14DeleteDatasetRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(financialservices.googleapis.com/Dataset\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01B\xfb\x01\n%com.google.cloud.financialservices.v1B\x0cDatasetProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.financialservices.v1.dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.financialservices.v1B\x0cDatasetProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1'
    _globals['_DATASET_LABELSENTRY']._loaded_options = None
    _globals['_DATASET_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DATASET_TABLESPECSENTRY']._loaded_options = None
    _globals['_DATASET_TABLESPECSENTRY']._serialized_options = b'8\x01'
    _globals['_DATASET'].fields_by_name['name']._loaded_options = None
    _globals['_DATASET'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATASET'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['update_time']._loaded_options = None
    _globals['_DATASET'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['table_specs']._loaded_options = None
    _globals['_DATASET'].fields_by_name['table_specs']._serialized_options = b'\xe0A\x02'
    _globals['_DATASET'].fields_by_name['state']._loaded_options = None
    _globals['_DATASET'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['date_range']._loaded_options = None
    _globals['_DATASET'].fields_by_name['date_range']._serialized_options = b'\xe0A\x02'
    _globals['_DATASET']._loaded_options = None
    _globals['_DATASET']._serialized_options = b'\xeaA\x7f\n(financialservices.googleapis.com/Dataset\x12Sprojects/{project_num}/locations/{location}/instances/{instance}/datasets/{dataset}'
    _globals['_LISTDATASETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATASETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_GETDATASETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(financialservices.googleapis.com/Dataset'
    _globals['_CREATEDATASETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATASETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_CREATEDATASETREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_CREATEDATASETREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATASETREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_CREATEDATASETREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATASETREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEDATASETREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEDATASETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATASETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(financialservices.googleapis.com/Dataset'
    _globals['_DELETEDATASETREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEDATASETREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET']._serialized_start = 270
    _globals['_DATASET']._serialized_end = 1041
    _globals['_DATASET_LABELSENTRY']._serialized_start = 726
    _globals['_DATASET_LABELSENTRY']._serialized_end = 771
    _globals['_DATASET_TABLESPECSENTRY']._serialized_start = 773
    _globals['_DATASET_TABLESPECSENTRY']._serialized_end = 822
    _globals['_DATASET_STATE']._serialized_start = 824
    _globals['_DATASET_STATE']._serialized_end = 908
    _globals['_LISTDATASETSREQUEST']._serialized_start = 1044
    _globals['_LISTDATASETSREQUEST']._serialized_end = 1205
    _globals['_LISTDATASETSRESPONSE']._serialized_start = 1208
    _globals['_LISTDATASETSRESPONSE']._serialized_end = 1338
    _globals['_GETDATASETREQUEST']._serialized_start = 1340
    _globals['_GETDATASETREQUEST']._serialized_end = 1423
    _globals['_CREATEDATASETREQUEST']._serialized_start = 1426
    _globals['_CREATEDATASETREQUEST']._serialized_end = 1631
    _globals['_UPDATEDATASETREQUEST']._serialized_start = 1634
    _globals['_UPDATEDATASETREQUEST']._serialized_end = 1801
    _globals['_DELETEDATASETREQUEST']._serialized_start = 1803
    _globals['_DELETEDATASETREQUEST']._serialized_end = 1914