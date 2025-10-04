"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/financialservices/v1/engine_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.financialservices.v1 import bigquery_destination_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_bigquery__destination__pb2
from .....google.cloud.financialservices.v1 import line_of_business_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_line__of__business__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/financialservices/v1/engine_config.proto\x12!google.cloud.financialservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a<google/cloud/financialservices/v1/bigquery_destination.proto\x1a8google/cloud/financialservices/v1/line_of_business.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x83\x0c\n\x0cEngineConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12K\n\x06labels\x18\x04 \x03(\x0b2;.google.cloud.financialservices.v1.EngineConfig.LabelsEntry\x12I\n\x05state\x18\x05 \x01(\x0e25.google.cloud.financialservices.v1.EngineConfig.StateB\x03\xe0A\x03\x12N\n\x0eengine_version\x18\x06 \x01(\tB6\xe0A\x02\xfaA0\n.financialservices.googleapis.com/EngineVersion\x12K\n\x06tuning\x18\x07 \x01(\x0b26.google.cloud.financialservices.v1.EngineConfig.TuningB\x03\xe0A\x01\x12b\n\x12performance_target\x18\x0b \x01(\x0b2A.google.cloud.financialservices.v1.EngineConfig.PerformanceTargetB\x03\xe0A\x01\x12P\n\x10line_of_business\x18\x0c \x01(\x0e21.google.cloud.financialservices.v1.LineOfBusinessB\x03\xe0A\x03\x12q\n\x1ahyperparameter_source_type\x18\x0f \x01(\x0e2H.google.cloud.financialservices.v1.EngineConfig.HyperparameterSourceTypeB\x03\xe0A\x01\x12h\n\x15hyperparameter_source\x18\x10 \x01(\x0b2D.google.cloud.financialservices.v1.EngineConfig.HyperparameterSourceB\x03\xe0A\x01\x1a\x86\x01\n\x06Tuning\x12I\n\x0fprimary_dataset\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(financialservices.googleapis.com/Dataset\x121\n\x08end_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x1aF\n\x11PerformanceTarget\x121\n$party_investigations_per_period_hint\x18\x01 \x01(\x03B\x03\xe0A\x02\x1a]\n\x14HyperparameterSource\x12!\n\x14source_engine_config\x18\x01 \x01(\tB\x03\xe0A\x02\x12"\n\x15source_engine_version\x18\x02 \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04"a\n\x18HyperparameterSourceType\x12*\n&HYPERPARAMETER_SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06TUNING\x10\x01\x12\r\n\tINHERITED\x10\x02:\x93\x01\xeaA\x8f\x01\n-financialservices.googleapis.com/EngineConfig\x12^projects/{project_num}/locations/{location}/instances/{instance}/engineConfigs/{engine_config}"\xa6\x01\n\x18ListEngineConfigsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x92\x01\n\x19ListEngineConfigsResponse\x12G\n\x0eengine_configs\x18\x01 \x03(\x0b2/.google.cloud.financialservices.v1.EngineConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"]\n\x16GetEngineConfigRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-financialservices.googleapis.com/EngineConfig"\xe3\x01\n\x19CreateEngineConfigRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12\x1d\n\x10engine_config_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12K\n\rengine_config\x18\x03 \x01(\x0b2/.google.cloud.financialservices.v1.EngineConfigB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xb7\x01\n\x19UpdateEngineConfigRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12K\n\rengine_config\x18\x02 \x01(\x0b2/.google.cloud.financialservices.v1.EngineConfigB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"y\n\x19DeleteEngineConfigRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-financialservices.googleapis.com/EngineConfig\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\xd7\x01\n!ExportEngineConfigMetadataRequest\x12L\n\rengine_config\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-financialservices.googleapis.com/EngineConfig\x12d\n\x1fstructured_metadata_destination\x18\x02 \x01(\x0b26.google.cloud.financialservices.v1.BigQueryDestinationB\x03\xe0A\x02"$\n"ExportEngineConfigMetadataResponseB\x80\x02\n%com.google.cloud.financialservices.v1B\x11EngineConfigProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.financialservices.v1.engine_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.financialservices.v1B\x11EngineConfigProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1'
    _globals['_ENGINECONFIG_TUNING'].fields_by_name['primary_dataset']._loaded_options = None
    _globals['_ENGINECONFIG_TUNING'].fields_by_name['primary_dataset']._serialized_options = b'\xe0A\x02\xfaA*\n(financialservices.googleapis.com/Dataset'
    _globals['_ENGINECONFIG_TUNING'].fields_by_name['end_time']._loaded_options = None
    _globals['_ENGINECONFIG_TUNING'].fields_by_name['end_time']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINECONFIG_PERFORMANCETARGET'].fields_by_name['party_investigations_per_period_hint']._loaded_options = None
    _globals['_ENGINECONFIG_PERFORMANCETARGET'].fields_by_name['party_investigations_per_period_hint']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINECONFIG_HYPERPARAMETERSOURCE'].fields_by_name['source_engine_config']._loaded_options = None
    _globals['_ENGINECONFIG_HYPERPARAMETERSOURCE'].fields_by_name['source_engine_config']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINECONFIG_HYPERPARAMETERSOURCE'].fields_by_name['source_engine_version']._loaded_options = None
    _globals['_ENGINECONFIG_HYPERPARAMETERSOURCE'].fields_by_name['source_engine_version']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINECONFIG_LABELSENTRY']._loaded_options = None
    _globals['_ENGINECONFIG_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ENGINECONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_ENGINECONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINECONFIG'].fields_by_name['create_time']._loaded_options = None
    _globals['_ENGINECONFIG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINECONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENGINECONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINECONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_ENGINECONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINECONFIG'].fields_by_name['engine_version']._loaded_options = None
    _globals['_ENGINECONFIG'].fields_by_name['engine_version']._serialized_options = b'\xe0A\x02\xfaA0\n.financialservices.googleapis.com/EngineVersion'
    _globals['_ENGINECONFIG'].fields_by_name['tuning']._loaded_options = None
    _globals['_ENGINECONFIG'].fields_by_name['tuning']._serialized_options = b'\xe0A\x01'
    _globals['_ENGINECONFIG'].fields_by_name['performance_target']._loaded_options = None
    _globals['_ENGINECONFIG'].fields_by_name['performance_target']._serialized_options = b'\xe0A\x01'
    _globals['_ENGINECONFIG'].fields_by_name['line_of_business']._loaded_options = None
    _globals['_ENGINECONFIG'].fields_by_name['line_of_business']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINECONFIG'].fields_by_name['hyperparameter_source_type']._loaded_options = None
    _globals['_ENGINECONFIG'].fields_by_name['hyperparameter_source_type']._serialized_options = b'\xe0A\x01'
    _globals['_ENGINECONFIG'].fields_by_name['hyperparameter_source']._loaded_options = None
    _globals['_ENGINECONFIG'].fields_by_name['hyperparameter_source']._serialized_options = b'\xe0A\x01'
    _globals['_ENGINECONFIG']._loaded_options = None
    _globals['_ENGINECONFIG']._serialized_options = b'\xeaA\x8f\x01\n-financialservices.googleapis.com/EngineConfig\x12^projects/{project_num}/locations/{location}/instances/{instance}/engineConfigs/{engine_config}'
    _globals['_LISTENGINECONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENGINECONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_GETENGINECONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENGINECONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-financialservices.googleapis.com/EngineConfig'
    _globals['_CREATEENGINECONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENGINECONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_CREATEENGINECONFIGREQUEST'].fields_by_name['engine_config_id']._loaded_options = None
    _globals['_CREATEENGINECONFIGREQUEST'].fields_by_name['engine_config_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENGINECONFIGREQUEST'].fields_by_name['engine_config']._loaded_options = None
    _globals['_CREATEENGINECONFIGREQUEST'].fields_by_name['engine_config']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENGINECONFIGREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEENGINECONFIGREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEENGINECONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEENGINECONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEENGINECONFIGREQUEST'].fields_by_name['engine_config']._loaded_options = None
    _globals['_UPDATEENGINECONFIGREQUEST'].fields_by_name['engine_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENGINECONFIGREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEENGINECONFIGREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEENGINECONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENGINECONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-financialservices.googleapis.com/EngineConfig'
    _globals['_DELETEENGINECONFIGREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEENGINECONFIGREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTENGINECONFIGMETADATAREQUEST'].fields_by_name['engine_config']._loaded_options = None
    _globals['_EXPORTENGINECONFIGMETADATAREQUEST'].fields_by_name['engine_config']._serialized_options = b'\xe0A\x02\xfaA/\n-financialservices.googleapis.com/EngineConfig'
    _globals['_EXPORTENGINECONFIGMETADATAREQUEST'].fields_by_name['structured_metadata_destination']._loaded_options = None
    _globals['_EXPORTENGINECONFIGMETADATAREQUEST'].fields_by_name['structured_metadata_destination']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINECONFIG']._serialized_start = 340
    _globals['_ENGINECONFIG']._serialized_end = 1879
    _globals['_ENGINECONFIG_TUNING']._serialized_start = 1196
    _globals['_ENGINECONFIG_TUNING']._serialized_end = 1330
    _globals['_ENGINECONFIG_PERFORMANCETARGET']._serialized_start = 1332
    _globals['_ENGINECONFIG_PERFORMANCETARGET']._serialized_end = 1402
    _globals['_ENGINECONFIG_HYPERPARAMETERSOURCE']._serialized_start = 1404
    _globals['_ENGINECONFIG_HYPERPARAMETERSOURCE']._serialized_end = 1497
    _globals['_ENGINECONFIG_LABELSENTRY']._serialized_start = 1499
    _globals['_ENGINECONFIG_LABELSENTRY']._serialized_end = 1544
    _globals['_ENGINECONFIG_STATE']._serialized_start = 1546
    _globals['_ENGINECONFIG_STATE']._serialized_end = 1630
    _globals['_ENGINECONFIG_HYPERPARAMETERSOURCETYPE']._serialized_start = 1632
    _globals['_ENGINECONFIG_HYPERPARAMETERSOURCETYPE']._serialized_end = 1729
    _globals['_LISTENGINECONFIGSREQUEST']._serialized_start = 1882
    _globals['_LISTENGINECONFIGSREQUEST']._serialized_end = 2048
    _globals['_LISTENGINECONFIGSRESPONSE']._serialized_start = 2051
    _globals['_LISTENGINECONFIGSRESPONSE']._serialized_end = 2197
    _globals['_GETENGINECONFIGREQUEST']._serialized_start = 2199
    _globals['_GETENGINECONFIGREQUEST']._serialized_end = 2292
    _globals['_CREATEENGINECONFIGREQUEST']._serialized_start = 2295
    _globals['_CREATEENGINECONFIGREQUEST']._serialized_end = 2522
    _globals['_UPDATEENGINECONFIGREQUEST']._serialized_start = 2525
    _globals['_UPDATEENGINECONFIGREQUEST']._serialized_end = 2708
    _globals['_DELETEENGINECONFIGREQUEST']._serialized_start = 2710
    _globals['_DELETEENGINECONFIGREQUEST']._serialized_end = 2831
    _globals['_EXPORTENGINECONFIGMETADATAREQUEST']._serialized_start = 2834
    _globals['_EXPORTENGINECONFIGMETADATAREQUEST']._serialized_end = 3049
    _globals['_EXPORTENGINECONFIGMETADATARESPONSE']._serialized_start = 3051
    _globals['_EXPORTENGINECONFIGMETADATARESPONSE']._serialized_end = 3087