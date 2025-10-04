"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/financialservices/v1/model.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.financialservices.v1 import bigquery_destination_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_bigquery__destination__pb2
from .....google.cloud.financialservices.v1 import line_of_business_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_line__of__business__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/financialservices/v1/model.proto\x12!google.cloud.financialservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a<google/cloud/financialservices/v1/bigquery_destination.proto\x1a8google/cloud/financialservices/v1/line_of_business.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x81\x07\n\x05Model\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12D\n\x06labels\x18\x04 \x03(\x0b24.google.cloud.financialservices.v1.Model.LabelsEntry\x12B\n\x05state\x18\x05 \x01(\x0e2..google.cloud.financialservices.v1.Model.StateB\x03\xe0A\x03\x12N\n\x0eengine_version\x18\x06 \x01(\tB6\xe0A\x03\xfaA0\n.financialservices.googleapis.com/EngineVersion\x12L\n\rengine_config\x18\x07 \x01(\tB5\xe0A\x02\xfaA/\n-financialservices.googleapis.com/EngineConfig\x12I\n\x0fprimary_dataset\x18\x08 \x01(\tB0\xe0A\x02\xfaA*\n(financialservices.googleapis.com/Dataset\x121\n\x08end_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x12P\n\x10line_of_business\x18\x0c \x01(\x0e21.google.cloud.financialservices.v1.LineOfBusinessB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04:|\xeaAy\n&financialservices.googleapis.com/Model\x12Oprojects/{project_num}/locations/{location}/instances/{instance}/models/{model}"\x9f\x01\n\x11ListModelsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"|\n\x12ListModelsResponse\x128\n\x06models\x18\x01 \x03(\x0b2(.google.cloud.financialservices.v1.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"O\n\x0fGetModelRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&financialservices.googleapis.com/Model"\xc5\x01\n\x12CreateModelRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12\x15\n\x08model_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12<\n\x05model\x18\x03 \x01(\x0b2(.google.cloud.financialservices.v1.ModelB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa1\x01\n\x12UpdateModelRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12<\n\x05model\x18\x02 \x01(\x0b2(.google.cloud.financialservices.v1.ModelB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"k\n\x12DeleteModelRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&financialservices.googleapis.com/Model\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\xc1\x01\n\x1aExportModelMetadataRequest\x12=\n\x05model\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&financialservices.googleapis.com/Model\x12d\n\x1fstructured_metadata_destination\x18\x02 \x01(\x0b26.google.cloud.financialservices.v1.BigQueryDestinationB\x03\xe0A\x02"\x1d\n\x1bExportModelMetadataResponseB\xf9\x01\n%com.google.cloud.financialservices.v1B\nModelProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.financialservices.v1.model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.financialservices.v1B\nModelProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1'
    _globals['_MODEL_LABELSENTRY']._loaded_options = None
    _globals['_MODEL_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_MODEL'].fields_by_name['name']._loaded_options = None
    _globals['_MODEL'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['create_time']._loaded_options = None
    _globals['_MODEL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['update_time']._loaded_options = None
    _globals['_MODEL'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['state']._loaded_options = None
    _globals['_MODEL'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['engine_version']._loaded_options = None
    _globals['_MODEL'].fields_by_name['engine_version']._serialized_options = b'\xe0A\x03\xfaA0\n.financialservices.googleapis.com/EngineVersion'
    _globals['_MODEL'].fields_by_name['engine_config']._loaded_options = None
    _globals['_MODEL'].fields_by_name['engine_config']._serialized_options = b'\xe0A\x02\xfaA/\n-financialservices.googleapis.com/EngineConfig'
    _globals['_MODEL'].fields_by_name['primary_dataset']._loaded_options = None
    _globals['_MODEL'].fields_by_name['primary_dataset']._serialized_options = b'\xe0A\x02\xfaA*\n(financialservices.googleapis.com/Dataset'
    _globals['_MODEL'].fields_by_name['end_time']._loaded_options = None
    _globals['_MODEL'].fields_by_name['end_time']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL'].fields_by_name['line_of_business']._loaded_options = None
    _globals['_MODEL'].fields_by_name['line_of_business']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL']._loaded_options = None
    _globals['_MODEL']._serialized_options = b'\xeaAy\n&financialservices.googleapis.com/Model\x12Oprojects/{project_num}/locations/{location}/instances/{instance}/models/{model}'
    _globals['_LISTMODELSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMODELSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_GETMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&financialservices.googleapis.com/Model'
    _globals['_CREATEMODELREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMODELREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_CREATEMODELREQUEST'].fields_by_name['model_id']._loaded_options = None
    _globals['_CREATEMODELREQUEST'].fields_by_name['model_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMODELREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_CREATEMODELREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMODELREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEMODELREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEMODELREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMODELREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEMODELREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_UPDATEMODELREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMODELREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEMODELREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&financialservices.googleapis.com/Model'
    _globals['_DELETEMODELREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEMODELREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTMODELMETADATAREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_EXPORTMODELMETADATAREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x02\xfaA(\n&financialservices.googleapis.com/Model'
    _globals['_EXPORTMODELMETADATAREQUEST'].fields_by_name['structured_metadata_destination']._loaded_options = None
    _globals['_EXPORTMODELMETADATAREQUEST'].fields_by_name['structured_metadata_destination']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL']._serialized_start = 332
    _globals['_MODEL']._serialized_end = 1229
    _globals['_MODEL_LABELSENTRY']._serialized_start = 972
    _globals['_MODEL_LABELSENTRY']._serialized_end = 1017
    _globals['_MODEL_STATE']._serialized_start = 1019
    _globals['_MODEL_STATE']._serialized_end = 1103
    _globals['_LISTMODELSREQUEST']._serialized_start = 1232
    _globals['_LISTMODELSREQUEST']._serialized_end = 1391
    _globals['_LISTMODELSRESPONSE']._serialized_start = 1393
    _globals['_LISTMODELSRESPONSE']._serialized_end = 1517
    _globals['_GETMODELREQUEST']._serialized_start = 1519
    _globals['_GETMODELREQUEST']._serialized_end = 1598
    _globals['_CREATEMODELREQUEST']._serialized_start = 1601
    _globals['_CREATEMODELREQUEST']._serialized_end = 1798
    _globals['_UPDATEMODELREQUEST']._serialized_start = 1801
    _globals['_UPDATEMODELREQUEST']._serialized_end = 1962
    _globals['_DELETEMODELREQUEST']._serialized_start = 1964
    _globals['_DELETEMODELREQUEST']._serialized_end = 2071
    _globals['_EXPORTMODELMETADATAREQUEST']._serialized_start = 2074
    _globals['_EXPORTMODELMETADATAREQUEST']._serialized_end = 2267
    _globals['_EXPORTMODELMETADATARESPONSE']._serialized_start = 2269
    _globals['_EXPORTMODELMETADATARESPONSE']._serialized_end = 2298