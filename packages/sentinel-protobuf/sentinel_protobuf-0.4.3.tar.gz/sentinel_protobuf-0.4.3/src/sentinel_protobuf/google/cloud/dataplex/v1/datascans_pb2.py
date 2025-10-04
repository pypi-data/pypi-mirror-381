"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dataplex/v1/datascans.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataplex.v1 import data_discovery_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_data__discovery__pb2
from .....google.cloud.dataplex.v1 import data_profile_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_data__profile__pb2
from .....google.cloud.dataplex.v1 import data_quality_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_data__quality__pb2
from .....google.cloud.dataplex.v1 import processing_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_processing__pb2
from .....google.cloud.dataplex.v1 import resources_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_resources__pb2
from .....google.cloud.dataplex.v1 import service_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/dataplex/v1/datascans.proto\x12\x18google.cloud.dataplex.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/dataplex/v1/data_discovery.proto\x1a+google/cloud/dataplex/v1/data_profile.proto\x1a+google/cloud/dataplex/v1/data_quality.proto\x1a)google/cloud/dataplex/v1/processing.proto\x1a(google/cloud/dataplex/v1/resources.proto\x1a&google/cloud/dataplex/v1/service.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc5\x01\n\x15CreateDataScanRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12:\n\tdata_scan\x18\x02 \x01(\x0b2".google.cloud.dataplex.v1.DataScanB\x03\xe0A\x02\x12\x19\n\x0cdata_scan_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01"\xa5\x01\n\x15UpdateDataScanRequest\x12:\n\tdata_scan\x18\x01 \x01(\x0b2".google.cloud.dataplex.v1.DataScanB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"c\n\x15DeleteDataScanRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dataplex.googleapis.com/DataScan\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x01"\xdf\x01\n\x12GetDataScanRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dataplex.googleapis.com/DataScan\x12L\n\x04view\x18\x02 \x01(\x0e29.google.cloud.dataplex.v1.GetDataScanRequest.DataScanViewB\x03\xe0A\x01"C\n\x0cDataScanView\x12\x1e\n\x1aDATA_SCAN_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\n"\xae\x01\n\x14ListDataScansRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"}\n\x15ListDataScansResponse\x126\n\ndata_scans\x18\x01 \x03(\x0b2".google.cloud.dataplex.v1.DataScan\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"L\n\x12RunDataScanRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dataplex.googleapis.com/DataScan"I\n\x13RunDataScanResponse\x122\n\x03job\x18\x01 \x01(\x0b2%.google.cloud.dataplex.v1.DataScanJob"\xf2\x01\n\x15GetDataScanJobRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#dataplex.googleapis.com/DataScanJob\x12R\n\x04view\x18\x02 \x01(\x0e2?.google.cloud.dataplex.v1.GetDataScanJobRequest.DataScanJobViewB\x03\xe0A\x01"J\n\x0fDataScanJobView\x12"\n\x1eDATA_SCAN_JOB_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\n"\x99\x01\n\x17ListDataScanJobsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dataplex.googleapis.com/DataScan\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"r\n\x18ListDataScanJobsResponse\x12=\n\x0edata_scan_jobs\x18\x01 \x03(\x0b2%.google.cloud.dataplex.v1.DataScanJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"4\n\x1fGenerateDataQualityRulesRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"[\n GenerateDataQualityRulesResponse\x127\n\x04rule\x18\x01 \x03(\x0b2).google.cloud.dataplex.v1.DataQualityRule"\xa9\x0c\n\x08DataScan\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12\x18\n\x03uid\x18\x02 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x04 \x01(\tB\x03\xe0A\x01\x12C\n\x06labels\x18\x05 \x03(\x0b2..google.cloud.dataplex.v1.DataScan.LabelsEntryB\x03\xe0A\x01\x123\n\x05state\x18\x06 \x01(\x0e2\x1f.google.cloud.dataplex.v1.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x127\n\x04data\x18\t \x01(\x0b2$.google.cloud.dataplex.v1.DataSourceB\x03\xe0A\x02\x12M\n\x0eexecution_spec\x18\n \x01(\x0b20.google.cloud.dataplex.v1.DataScan.ExecutionSpecB\x03\xe0A\x01\x12Q\n\x10execution_status\x18\x0b \x01(\x0b22.google.cloud.dataplex.v1.DataScan.ExecutionStatusB\x03\xe0A\x03\x129\n\x04type\x18\x0c \x01(\x0e2&.google.cloud.dataplex.v1.DataScanTypeB\x03\xe0A\x03\x12F\n\x11data_quality_spec\x18d \x01(\x0b2).google.cloud.dataplex.v1.DataQualitySpecH\x00\x12F\n\x11data_profile_spec\x18e \x01(\x0b2).google.cloud.dataplex.v1.DataProfileSpecH\x00\x12J\n\x13data_discovery_spec\x18f \x01(\x0b2+.google.cloud.dataplex.v1.DataDiscoverySpecH\x00\x12P\n\x13data_quality_result\x18\xc8\x01 \x01(\x0b2+.google.cloud.dataplex.v1.DataQualityResultB\x03\xe0A\x03H\x01\x12P\n\x13data_profile_result\x18\xc9\x01 \x01(\x0b2+.google.cloud.dataplex.v1.DataProfileResultB\x03\xe0A\x03H\x01\x12T\n\x15data_discovery_result\x18\xca\x01 \x01(\x0b2-.google.cloud.dataplex.v1.DataDiscoveryResultB\x03\xe0A\x03H\x01\x1am\n\rExecutionSpec\x127\n\x07trigger\x18\x01 \x01(\x0b2!.google.cloud.dataplex.v1.TriggerB\x03\xe0A\x01\x12\x14\n\x05field\x18d \x01(\tB\x03\xe0A\x05H\x00B\r\n\x0bincremental\x1a\xd0\x01\n\x0fExecutionStatus\x12>\n\x15latest_job_start_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12<\n\x13latest_job_end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12?\n\x16latest_job_create_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:c\xeaA`\n dataplex.googleapis.com/DataScan\x12<projects/{project}/locations/{location}/dataScans/{dataScan}B\x06\n\x04specB\x08\n\x06result"\xca\x08\n\x0bDataScanJob\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12\x18\n\x03uid\x18\x02 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12?\n\x05state\x18\x05 \x01(\x0e2+.google.cloud.dataplex.v1.DataScanJob.StateB\x03\xe0A\x03\x12\x14\n\x07message\x18\x06 \x01(\tB\x03\xe0A\x03\x129\n\x04type\x18\x07 \x01(\x0e2&.google.cloud.dataplex.v1.DataScanTypeB\x03\xe0A\x03\x12K\n\x11data_quality_spec\x18d \x01(\x0b2).google.cloud.dataplex.v1.DataQualitySpecB\x03\xe0A\x03H\x00\x12K\n\x11data_profile_spec\x18e \x01(\x0b2).google.cloud.dataplex.v1.DataProfileSpecB\x03\xe0A\x03H\x00\x12O\n\x13data_discovery_spec\x18f \x01(\x0b2+.google.cloud.dataplex.v1.DataDiscoverySpecB\x03\xe0A\x03H\x00\x12P\n\x13data_quality_result\x18\xc8\x01 \x01(\x0b2+.google.cloud.dataplex.v1.DataQualityResultB\x03\xe0A\x03H\x01\x12P\n\x13data_profile_result\x18\xc9\x01 \x01(\x0b2+.google.cloud.dataplex.v1.DataProfileResultB\x03\xe0A\x03H\x01\x12T\n\x15data_discovery_result\x18\xca\x01 \x01(\x0b2-.google.cloud.dataplex.v1.DataDiscoveryResultB\x03\xe0A\x03H\x01"q\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\r\n\tCANCELING\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\n\n\x06FAILED\x10\x05\x12\x0b\n\x07PENDING\x10\x07:q\xeaAn\n#dataplex.googleapis.com/DataScanJob\x12Gprojects/{project}/locations/{location}/dataScans/{dataScan}/jobs/{job}B\x06\n\x04specB\x08\n\x06result*f\n\x0cDataScanType\x12\x1e\n\x1aDATA_SCAN_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cDATA_QUALITY\x10\x01\x12\x10\n\x0cDATA_PROFILE\x10\x02\x12\x12\n\x0eDATA_DISCOVERY\x10\x032\xb6\x0f\n\x0fDataScanService\x12\xe3\x01\n\x0eCreateDataScan\x12/.google.cloud.dataplex.v1.CreateDataScanRequest\x1a\x1d.google.longrunning.Operation"\x80\x01\xcaA\x1d\n\x08DataScan\x12\x11OperationMetadata\xdaA\x1dparent,data_scan,data_scan_id\x82\xd3\xe4\x93\x02:"-/v1/{parent=projects/*/locations/*}/dataScans:\tdata_scan\x12\xe5\x01\n\x0eUpdateDataScan\x12/.google.cloud.dataplex.v1.UpdateDataScanRequest\x1a\x1d.google.longrunning.Operation"\x82\x01\xcaA\x1d\n\x08DataScan\x12\x11OperationMetadata\xdaA\x15data_scan,update_mask\x82\xd3\xe4\x93\x02D27/v1/{data_scan.name=projects/*/locations/*/dataScans/*}:\tdata_scan\x12\xcb\x01\n\x0eDeleteDataScan\x12/.google.cloud.dataplex.v1.DeleteDataScanRequest\x1a\x1d.google.longrunning.Operation"i\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/dataScans/*}\x12\x9d\x01\n\x0bGetDataScan\x12,.google.cloud.dataplex.v1.GetDataScanRequest\x1a".google.cloud.dataplex.v1.DataScan"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/dataScans/*}\x12\xb0\x01\n\rListDataScans\x12..google.cloud.dataplex.v1.ListDataScansRequest\x1a/.google.cloud.dataplex.v1.ListDataScansResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/dataScans\x12\xaf\x01\n\x0bRunDataScan\x12,.google.cloud.dataplex.v1.RunDataScanRequest\x1a-.google.cloud.dataplex.v1.RunDataScanResponse"C\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/dataScans/*}:run:\x01*\x12\xad\x01\n\x0eGetDataScanJob\x12/.google.cloud.dataplex.v1.GetDataScanJobRequest\x1a%.google.cloud.dataplex.v1.DataScanJob"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/dataScans/*/jobs/*}\x12\xc0\x01\n\x10ListDataScanJobs\x121.google.cloud.dataplex.v1.ListDataScanJobsRequest\x1a2.google.cloud.dataplex.v1.ListDataScanJobsResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*/dataScans/*}/jobs\x12\xc1\x02\n\x18GenerateDataQualityRules\x129.google.cloud.dataplex.v1.GenerateDataQualityRulesRequest\x1a:.google.cloud.dataplex.v1.GenerateDataQualityRulesResponse"\xad\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x9f\x01"F/v1/{name=projects/*/locations/*/dataScans/*}:generateDataQualityRules:\x01*ZR"M/v1/{name=projects/*/locations/*/dataScans/*/jobs/*}:generateDataQualityRules:\x01*\x1aK\xcaA\x17dataplex.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBj\n\x1ccom.google.cloud.dataplex.v1B\x0eDataScansProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataplex.v1.datascans_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataplex.v1B\x0eDataScansProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb'
    _globals['_CREATEDATASCANREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATASCANREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEDATASCANREQUEST'].fields_by_name['data_scan']._loaded_options = None
    _globals['_CREATEDATASCANREQUEST'].fields_by_name['data_scan']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATASCANREQUEST'].fields_by_name['data_scan_id']._loaded_options = None
    _globals['_CREATEDATASCANREQUEST'].fields_by_name['data_scan_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATASCANREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATEDATASCANREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEDATASCANREQUEST'].fields_by_name['data_scan']._loaded_options = None
    _globals['_UPDATEDATASCANREQUEST'].fields_by_name['data_scan']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATASCANREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDATASCANREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEDATASCANREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATEDATASCANREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEDATASCANREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATASCANREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n dataplex.googleapis.com/DataScan'
    _globals['_DELETEDATASCANREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEDATASCANREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_GETDATASCANREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASCANREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n dataplex.googleapis.com/DataScan'
    _globals['_GETDATASCANREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_GETDATASCANREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASCANSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATASCANSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTDATASCANSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDATASCANSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASCANSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDATASCANSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASCANSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTDATASCANSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASCANSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTDATASCANSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_RUNDATASCANREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RUNDATASCANREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n dataplex.googleapis.com/DataScan'
    _globals['_GETDATASCANJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASCANJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#dataplex.googleapis.com/DataScanJob'
    _globals['_GETDATASCANJOBREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_GETDATASCANJOBREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASCANJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATASCANJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n dataplex.googleapis.com/DataScan'
    _globals['_LISTDATASCANJOBSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDATASCANJOBSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASCANJOBSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDATASCANJOBSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASCANJOBSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTDATASCANJOBSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEDATAQUALITYRULESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GENERATEDATAQUALITYRULESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_DATASCAN_EXECUTIONSPEC'].fields_by_name['trigger']._loaded_options = None
    _globals['_DATASCAN_EXECUTIONSPEC'].fields_by_name['trigger']._serialized_options = b'\xe0A\x01'
    _globals['_DATASCAN_EXECUTIONSPEC'].fields_by_name['field']._loaded_options = None
    _globals['_DATASCAN_EXECUTIONSPEC'].fields_by_name['field']._serialized_options = b'\xe0A\x05'
    _globals['_DATASCAN_EXECUTIONSTATUS'].fields_by_name['latest_job_start_time']._loaded_options = None
    _globals['_DATASCAN_EXECUTIONSTATUS'].fields_by_name['latest_job_start_time']._serialized_options = b'\xe0A\x01'
    _globals['_DATASCAN_EXECUTIONSTATUS'].fields_by_name['latest_job_end_time']._loaded_options = None
    _globals['_DATASCAN_EXECUTIONSTATUS'].fields_by_name['latest_job_end_time']._serialized_options = b'\xe0A\x01'
    _globals['_DATASCAN_EXECUTIONSTATUS'].fields_by_name['latest_job_create_time']._loaded_options = None
    _globals['_DATASCAN_EXECUTIONSTATUS'].fields_by_name['latest_job_create_time']._serialized_options = b'\xe0A\x01'
    _globals['_DATASCAN_LABELSENTRY']._loaded_options = None
    _globals['_DATASCAN_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DATASCAN'].fields_by_name['name']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_DATASCAN'].fields_by_name['uid']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_DATASCAN'].fields_by_name['description']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_DATASCAN'].fields_by_name['display_name']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_DATASCAN'].fields_by_name['labels']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_DATASCAN'].fields_by_name['state']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCAN'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCAN'].fields_by_name['update_time']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCAN'].fields_by_name['data']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['data']._serialized_options = b'\xe0A\x02'
    _globals['_DATASCAN'].fields_by_name['execution_spec']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['execution_spec']._serialized_options = b'\xe0A\x01'
    _globals['_DATASCAN'].fields_by_name['execution_status']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['execution_status']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCAN'].fields_by_name['type']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCAN'].fields_by_name['data_quality_result']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['data_quality_result']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCAN'].fields_by_name['data_profile_result']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['data_profile_result']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCAN'].fields_by_name['data_discovery_result']._loaded_options = None
    _globals['_DATASCAN'].fields_by_name['data_discovery_result']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCAN']._loaded_options = None
    _globals['_DATASCAN']._serialized_options = b'\xeaA`\n dataplex.googleapis.com/DataScan\x12<projects/{project}/locations/{location}/dataScans/{dataScan}'
    _globals['_DATASCANJOB'].fields_by_name['name']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_DATASCANJOB'].fields_by_name['uid']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_DATASCANJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANJOB'].fields_by_name['start_time']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANJOB'].fields_by_name['end_time']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANJOB'].fields_by_name['state']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANJOB'].fields_by_name['message']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['message']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANJOB'].fields_by_name['type']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANJOB'].fields_by_name['data_quality_spec']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['data_quality_spec']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANJOB'].fields_by_name['data_profile_spec']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['data_profile_spec']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANJOB'].fields_by_name['data_discovery_spec']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['data_discovery_spec']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANJOB'].fields_by_name['data_quality_result']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['data_quality_result']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANJOB'].fields_by_name['data_profile_result']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['data_profile_result']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANJOB'].fields_by_name['data_discovery_result']._loaded_options = None
    _globals['_DATASCANJOB'].fields_by_name['data_discovery_result']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANJOB']._loaded_options = None
    _globals['_DATASCANJOB']._serialized_options = b'\xeaAn\n#dataplex.googleapis.com/DataScanJob\x12Gprojects/{project}/locations/{location}/dataScans/{dataScan}/jobs/{job}'
    _globals['_DATASCANSERVICE']._loaded_options = None
    _globals['_DATASCANSERVICE']._serialized_options = b'\xcaA\x17dataplex.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATASCANSERVICE'].methods_by_name['CreateDataScan']._loaded_options = None
    _globals['_DATASCANSERVICE'].methods_by_name['CreateDataScan']._serialized_options = b'\xcaA\x1d\n\x08DataScan\x12\x11OperationMetadata\xdaA\x1dparent,data_scan,data_scan_id\x82\xd3\xe4\x93\x02:"-/v1/{parent=projects/*/locations/*}/dataScans:\tdata_scan'
    _globals['_DATASCANSERVICE'].methods_by_name['UpdateDataScan']._loaded_options = None
    _globals['_DATASCANSERVICE'].methods_by_name['UpdateDataScan']._serialized_options = b'\xcaA\x1d\n\x08DataScan\x12\x11OperationMetadata\xdaA\x15data_scan,update_mask\x82\xd3\xe4\x93\x02D27/v1/{data_scan.name=projects/*/locations/*/dataScans/*}:\tdata_scan'
    _globals['_DATASCANSERVICE'].methods_by_name['DeleteDataScan']._loaded_options = None
    _globals['_DATASCANSERVICE'].methods_by_name['DeleteDataScan']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/dataScans/*}'
    _globals['_DATASCANSERVICE'].methods_by_name['GetDataScan']._loaded_options = None
    _globals['_DATASCANSERVICE'].methods_by_name['GetDataScan']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/dataScans/*}'
    _globals['_DATASCANSERVICE'].methods_by_name['ListDataScans']._loaded_options = None
    _globals['_DATASCANSERVICE'].methods_by_name['ListDataScans']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/dataScans'
    _globals['_DATASCANSERVICE'].methods_by_name['RunDataScan']._loaded_options = None
    _globals['_DATASCANSERVICE'].methods_by_name['RunDataScan']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/dataScans/*}:run:\x01*'
    _globals['_DATASCANSERVICE'].methods_by_name['GetDataScanJob']._loaded_options = None
    _globals['_DATASCANSERVICE'].methods_by_name['GetDataScanJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/dataScans/*/jobs/*}'
    _globals['_DATASCANSERVICE'].methods_by_name['ListDataScanJobs']._loaded_options = None
    _globals['_DATASCANSERVICE'].methods_by_name['ListDataScanJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*/dataScans/*}/jobs'
    _globals['_DATASCANSERVICE'].methods_by_name['GenerateDataQualityRules']._loaded_options = None
    _globals['_DATASCANSERVICE'].methods_by_name['GenerateDataQualityRules']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x9f\x01"F/v1/{name=projects/*/locations/*/dataScans/*}:generateDataQualityRules:\x01*ZR"M/v1/{name=projects/*/locations/*/dataScans/*/jobs/*}:generateDataQualityRules:\x01*'
    _globals['_DATASCANTYPE']._serialized_start = 5106
    _globals['_DATASCANTYPE']._serialized_end = 5208
    _globals['_CREATEDATASCANREQUEST']._serialized_start = 610
    _globals['_CREATEDATASCANREQUEST']._serialized_end = 807
    _globals['_UPDATEDATASCANREQUEST']._serialized_start = 810
    _globals['_UPDATEDATASCANREQUEST']._serialized_end = 975
    _globals['_DELETEDATASCANREQUEST']._serialized_start = 977
    _globals['_DELETEDATASCANREQUEST']._serialized_end = 1076
    _globals['_GETDATASCANREQUEST']._serialized_start = 1079
    _globals['_GETDATASCANREQUEST']._serialized_end = 1302
    _globals['_GETDATASCANREQUEST_DATASCANVIEW']._serialized_start = 1235
    _globals['_GETDATASCANREQUEST_DATASCANVIEW']._serialized_end = 1302
    _globals['_LISTDATASCANSREQUEST']._serialized_start = 1305
    _globals['_LISTDATASCANSREQUEST']._serialized_end = 1479
    _globals['_LISTDATASCANSRESPONSE']._serialized_start = 1481
    _globals['_LISTDATASCANSRESPONSE']._serialized_end = 1606
    _globals['_RUNDATASCANREQUEST']._serialized_start = 1608
    _globals['_RUNDATASCANREQUEST']._serialized_end = 1684
    _globals['_RUNDATASCANRESPONSE']._serialized_start = 1686
    _globals['_RUNDATASCANRESPONSE']._serialized_end = 1759
    _globals['_GETDATASCANJOBREQUEST']._serialized_start = 1762
    _globals['_GETDATASCANJOBREQUEST']._serialized_end = 2004
    _globals['_GETDATASCANJOBREQUEST_DATASCANJOBVIEW']._serialized_start = 1930
    _globals['_GETDATASCANJOBREQUEST_DATASCANJOBVIEW']._serialized_end = 2004
    _globals['_LISTDATASCANJOBSREQUEST']._serialized_start = 2007
    _globals['_LISTDATASCANJOBSREQUEST']._serialized_end = 2160
    _globals['_LISTDATASCANJOBSRESPONSE']._serialized_start = 2162
    _globals['_LISTDATASCANJOBSRESPONSE']._serialized_end = 2276
    _globals['_GENERATEDATAQUALITYRULESREQUEST']._serialized_start = 2278
    _globals['_GENERATEDATAQUALITYRULESREQUEST']._serialized_end = 2330
    _globals['_GENERATEDATAQUALITYRULESRESPONSE']._serialized_start = 2332
    _globals['_GENERATEDATAQUALITYRULESRESPONSE']._serialized_end = 2423
    _globals['_DATASCAN']._serialized_start = 2426
    _globals['_DATASCAN']._serialized_end = 4003
    _globals['_DATASCAN_EXECUTIONSPEC']._serialized_start = 3517
    _globals['_DATASCAN_EXECUTIONSPEC']._serialized_end = 3626
    _globals['_DATASCAN_EXECUTIONSTATUS']._serialized_start = 3629
    _globals['_DATASCAN_EXECUTIONSTATUS']._serialized_end = 3837
    _globals['_DATASCAN_LABELSENTRY']._serialized_start = 3839
    _globals['_DATASCAN_LABELSENTRY']._serialized_end = 3884
    _globals['_DATASCANJOB']._serialized_start = 4006
    _globals['_DATASCANJOB']._serialized_end = 5104
    _globals['_DATASCANJOB_STATE']._serialized_start = 4858
    _globals['_DATASCANJOB_STATE']._serialized_end = 4971
    _globals['_DATASCANSERVICE']._serialized_start = 5211
    _globals['_DATASCANSERVICE']._serialized_end = 7185