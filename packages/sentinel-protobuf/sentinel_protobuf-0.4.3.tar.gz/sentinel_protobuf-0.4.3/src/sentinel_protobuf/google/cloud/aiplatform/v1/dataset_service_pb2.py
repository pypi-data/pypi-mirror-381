"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/dataset_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import annotation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_annotation__pb2
from .....google.cloud.aiplatform.v1 import annotation_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_annotation__spec__pb2
from .....google.cloud.aiplatform.v1 import data_item_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_data__item__pb2
from .....google.cloud.aiplatform.v1 import dataset_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_dataset__pb2
from .....google.cloud.aiplatform.v1 import dataset_version_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_dataset__version__pb2
from .....google.cloud.aiplatform.v1 import model_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_model__pb2
from .....google.cloud.aiplatform.v1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_operation__pb2
from .....google.cloud.aiplatform.v1 import saved_query_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_saved__query__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/aiplatform/v1/dataset_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/aiplatform/v1/annotation.proto\x1a0google/cloud/aiplatform/v1/annotation_spec.proto\x1a*google/cloud/aiplatform/v1/data_item.proto\x1a(google/cloud/aiplatform/v1/dataset.proto\x1a0google/cloud/aiplatform/v1/dataset_version.proto\x1a&google/cloud/aiplatform/v1/model.proto\x1a*google/cloud/aiplatform/v1/operation.proto\x1a,google/cloud/aiplatform/v1/saved_query.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x8c\x01\n\x14CreateDatasetRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x129\n\x07dataset\x18\x02 \x01(\x0b2#.google.cloud.aiplatform.v1.DatasetB\x03\xe0A\x02"p\n\x1eCreateDatasetOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"{\n\x11GetDatasetRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12-\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x87\x01\n\x14UpdateDatasetRequest\x129\n\x07dataset\x18\x01 \x01(\x0b2#.google.cloud.aiplatform.v1.DatasetB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\x9d\x01\n\x1bUpdateDatasetVersionRequest\x12H\n\x0fdataset_version\x18\x01 \x01(\x0b2*.google.cloud.aiplatform.v1.DatasetVersionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xc8\x01\n\x13ListDatasetsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x10\n\x08order_by\x18\x06 \x01(\t"f\n\x14ListDatasetsResponse\x125\n\x08datasets\x18\x01 \x03(\x0b2#.google.cloud.aiplatform.v1.Dataset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"O\n\x14DeleteDatasetRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset"\x97\x01\n\x11ImportDataRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12I\n\x0eimport_configs\x18\x02 \x03(\x0b2,.google.cloud.aiplatform.v1.ImportDataConfigB\x03\xe0A\x02"\x14\n\x12ImportDataResponse"m\n\x1bImportDataOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"\x96\x01\n\x11ExportDataRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12H\n\rexport_config\x18\x02 \x01(\x0b2,.google.cloud.aiplatform.v1.ExportDataConfigB\x03\xe0A\x02"m\n\x12ExportDataResponse\x12\x16\n\x0eexported_files\x18\x01 \x03(\t\x12?\n\ndata_stats\x18\x02 \x01(\x0b2+.google.cloud.aiplatform.v1.Model.DataStats"\x8b\x01\n\x1bExportDataOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata\x12\x1c\n\x14gcs_output_directory\x18\x02 \x01(\t"\xa2\x01\n\x1bCreateDatasetVersionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12H\n\x0fdataset_version\x18\x02 \x01(\x0b2*.google.cloud.aiplatform.v1.DatasetVersionB\x03\xe0A\x02"w\n%CreateDatasetVersionOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"]\n\x1bDeleteDatasetVersionRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/DatasetVersion"\x89\x01\n\x18GetDatasetVersionRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/DatasetVersion\x12-\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xe8\x01\n\x1aListDatasetVersionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x122\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x06 \x01(\tB\x03\xe0A\x01"|\n\x1bListDatasetVersionsResponse\x12D\n\x10dataset_versions\x18\x01 \x03(\x0b2*.google.cloud.aiplatform.v1.DatasetVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"^\n\x1cRestoreDatasetVersionRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/DatasetVersion"x\n&RestoreDatasetVersionOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"\xc9\x01\n\x14ListDataItemsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x10\n\x08order_by\x18\x06 \x01(\t"j\n\x15ListDataItemsResponse\x128\n\ndata_items\x18\x01 \x03(\x0b2$.google.cloud.aiplatform.v1.DataItem\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xdc\x04\n\x16SearchDataItemsRequest\x12\x1c\n\x12order_by_data_item\x18\x0c \x01(\tH\x00\x12c\n\x13order_by_annotation\x18\r \x01(\x0b2D.google.cloud.aiplatform.v1.SearchDataItemsRequest.OrderByAnnotationH\x00\x12:\n\x07dataset\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12@\n\x0bsaved_query\x18\x02 \x01(\tB+\x18\x01\xfaA&\n$aiplatform.googleapis.com/SavedQuery\x12\x19\n\x11data_labeling_job\x18\x03 \x01(\t\x12\x18\n\x10data_item_filter\x18\x04 \x01(\t\x12\x1e\n\x12annotations_filter\x18\x05 \x01(\tB\x02\x18\x01\x12\x1a\n\x12annotation_filters\x18\x0b \x03(\t\x12.\n\nfield_mask\x18\x06 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x19\n\x11annotations_limit\x18\x07 \x01(\x05\x12\x11\n\tpage_size\x18\x08 \x01(\x05\x12\x14\n\x08order_by\x18\t \x01(\tB\x02\x18\x01\x12\x12\n\npage_token\x18\n \x01(\t\x1a?\n\x11OrderByAnnotation\x12\x18\n\x0bsaved_query\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08order_by\x18\x02 \x01(\tB\x07\n\x05order"u\n\x17SearchDataItemsResponse\x12A\n\x0fdata_item_views\x18\x01 \x03(\x0b2(.google.cloud.aiplatform.v1.DataItemView\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa7\x01\n\x0cDataItemView\x127\n\tdata_item\x18\x01 \x01(\x0b2$.google.cloud.aiplatform.v1.DataItem\x12;\n\x0bannotations\x18\x02 \x03(\x0b2&.google.cloud.aiplatform.v1.Annotation\x12!\n\x19has_truncated_annotations\x18\x03 \x01(\x08"\xcc\x01\n\x17ListSavedQueriesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x10\n\x08order_by\x18\x06 \x01(\t"r\n\x18ListSavedQueriesResponse\x12=\n\rsaved_queries\x18\x01 \x03(\x0b2&.google.cloud.aiplatform.v1.SavedQuery\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"U\n\x17DeleteSavedQueryRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/SavedQuery"\x89\x01\n\x18GetAnnotationSpecRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/AnnotationSpec\x12-\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xcc\x01\n\x16ListAnnotationsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/DataItem\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x10\n\x08order_by\x18\x06 \x01(\t"o\n\x17ListAnnotationsResponse\x12;\n\x0bannotations\x18\x01 \x03(\x0b2&.google.cloud.aiplatform.v1.Annotation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd9$\n\x0eDatasetService\x12\xf6\x01\n\rCreateDataset\x120.google.cloud.aiplatform.v1.CreateDatasetRequest\x1a\x1d.google.longrunning.Operation"\x93\x01\xcaA)\n\x07Dataset\x12\x1eCreateDatasetOperationMetadata\xdaA\x0eparent,dataset\x82\xd3\xe4\x93\x02P",/v1/{parent=projects/*/locations/*}/datasets:\x07datasetZ\x17"\x0c/v1/datasets:\x07dataset\x12\xb6\x01\n\nGetDataset\x12-.google.cloud.aiplatform.v1.GetDatasetRequest\x1a#.google.cloud.aiplatform.v1.Dataset"T\xdaA\x04name\x82\xd3\xe4\x93\x02G\x12,/v1/{name=projects/*/locations/*/datasets/*}Z\x17\x12\x15/v1/{name=datasets/*}\x12\xee\x01\n\rUpdateDataset\x120.google.cloud.aiplatform.v1.UpdateDatasetRequest\x1a#.google.cloud.aiplatform.v1.Dataset"\x85\x01\xdaA\x13dataset,update_mask\x82\xd3\xe4\x93\x02i24/v1/{dataset.name=projects/*/locations/*/datasets/*}:\x07datasetZ(2\x1d/v1/{dataset.name=datasets/*}:\x07dataset\x12\xc0\x01\n\x0cListDatasets\x12/.google.cloud.aiplatform.v1.ListDatasetsRequest\x1a0.google.cloud.aiplatform.v1.ListDatasetsResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12,/v1/{parent=projects/*/locations/*}/datasetsZ\x0e\x12\x0c/v1/datasets\x12\xea\x01\n\rDeleteDataset\x120.google.cloud.aiplatform.v1.DeleteDatasetRequest\x1a\x1d.google.longrunning.Operation"\x87\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02G*,/v1/{name=projects/*/locations/*/datasets/*}Z\x17*\x15/v1/{name=datasets/*}\x12\xe5\x01\n\nImportData\x12-.google.cloud.aiplatform.v1.ImportDataRequest\x1a\x1d.google.longrunning.Operation"\x88\x01\xcaA1\n\x12ImportDataResponse\x12\x1bImportDataOperationMetadata\xdaA\x13name,import_configs\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/locations/*/datasets/*}:import:\x01*\x12\xe4\x01\n\nExportData\x12-.google.cloud.aiplatform.v1.ExportDataRequest\x1a\x1d.google.longrunning.Operation"\x87\x01\xcaA1\n\x12ExportDataResponse\x12\x1bExportDataOperationMetadata\xdaA\x12name,export_config\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/locations/*/datasets/*}:export:\x01*\x12\xd8\x02\n\x14CreateDatasetVersion\x127.google.cloud.aiplatform.v1.CreateDatasetVersionRequest\x1a\x1d.google.longrunning.Operation"\xe7\x01\xcaA7\n\x0eDatasetVersion\x12%CreateDatasetVersionOperationMetadata\xdaA\x16parent,dataset_version\x82\xd3\xe4\x93\x02\x8d\x01">/v1/{parent=projects/*/locations/*/datasets/*}/datasetVersions:\x0fdataset_versionZ:"\'/v1/{parent=datasets/*}/datasetVersions:\x0fdataset_version\x12\xd0\x02\n\x14UpdateDatasetVersion\x127.google.cloud.aiplatform.v1.UpdateDatasetVersionRequest\x1a*.google.cloud.aiplatform.v1.DatasetVersion"\xd2\x01\xdaA\x1bdataset_version,update_mask\x82\xd3\xe4\x93\x02\xad\x012N/v1/{dataset_version.name=projects/*/locations/*/datasets/*/datasetVersions/*}:\x0fdataset_versionZJ27/v1/{dataset_version.name=datasets/*/datasetVersions/*}:\x0fdataset_version\x12\x9c\x02\n\x14DeleteDatasetVersion\x127.google.cloud.aiplatform.v1.DeleteDatasetVersionRequest\x1a\x1d.google.longrunning.Operation"\xab\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02k*>/v1/{name=projects/*/locations/*/datasets/*/datasetVersions/*}Z)*\'/v1/{name=datasets/*/datasetVersions/*}\x12\xef\x01\n\x11GetDatasetVersion\x124.google.cloud.aiplatform.v1.GetDatasetVersionRequest\x1a*.google.cloud.aiplatform.v1.DatasetVersion"x\xdaA\x04name\x82\xd3\xe4\x93\x02k\x12>/v1/{name=projects/*/locations/*/datasets/*/datasetVersions/*}Z)\x12\'/v1/{name=datasets/*/datasetVersions/*}\x12\x82\x02\n\x13ListDatasetVersions\x126.google.cloud.aiplatform.v1.ListDatasetVersionsRequest\x1a7.google.cloud.aiplatform.v1.ListDatasetVersionsResponse"z\xdaA\x06parent\x82\xd3\xe4\x93\x02k\x12>/v1/{parent=projects/*/locations/*/datasets/*}/datasetVersionsZ)\x12\'/v1/{parent=datasets/*}/datasetVersions\x12\xb6\x02\n\x15RestoreDatasetVersion\x128.google.cloud.aiplatform.v1.RestoreDatasetVersionRequest\x1a\x1d.google.longrunning.Operation"\xc3\x01\xcaA8\n\x0eDatasetVersion\x12&RestoreDatasetVersionOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02{\x12F/v1/{name=projects/*/locations/*/datasets/*/datasetVersions/*}:restoreZ1\x12//v1/{name=datasets/*/datasetVersions/*}:restore\x12\xbf\x01\n\rListDataItems\x120.google.cloud.aiplatform.v1.ListDataItemsRequest\x1a1.google.cloud.aiplatform.v1.ListDataItemsResponse"I\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1/{parent=projects/*/locations/*/datasets/*}/dataItems\x12\xc3\x01\n\x0fSearchDataItems\x122.google.cloud.aiplatform.v1.SearchDataItemsRequest\x1a3.google.cloud.aiplatform.v1.SearchDataItemsResponse"G\x82\xd3\xe4\x93\x02A\x12?/v1/{dataset=projects/*/locations/*/datasets/*}:searchDataItems\x12\xcb\x01\n\x10ListSavedQueries\x123.google.cloud.aiplatform.v1.ListSavedQueriesRequest\x1a4.google.cloud.aiplatform.v1.ListSavedQueriesResponse"L\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1/{parent=projects/*/locations/*/datasets/*}/savedQueries\x12\xe5\x01\n\x10DeleteSavedQuery\x123.google.cloud.aiplatform.v1.DeleteSavedQueryRequest\x1a\x1d.google.longrunning.Operation"}\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1/{name=projects/*/locations/*/datasets/*/savedQueries/*}\x12\xc4\x01\n\x11GetAnnotationSpec\x124.google.cloud.aiplatform.v1.GetAnnotationSpecRequest\x1a*.google.cloud.aiplatform.v1.AnnotationSpec"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}\x12\xd3\x01\n\x0fListAnnotations\x122.google.cloud.aiplatform.v1.ListAnnotationsRequest\x1a3.google.cloud.aiplatform.v1.ListAnnotationsResponse"W\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v1/{parent=projects/*/locations/*/datasets/*/dataItems/*}/annotations\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd1\x01\n\x1ecom.google.cloud.aiplatform.v1B\x13DatasetServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.dataset_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x13DatasetServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_CREATEDATASETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATASETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEDATASETREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_CREATEDATASETREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATASETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDATASETREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATASETVERSIONREQUEST'].fields_by_name['dataset_version']._loaded_options = None
    _globals['_UPDATEDATASETVERSIONREQUEST'].fields_by_name['dataset_version']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATASETVERSIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDATASETVERSIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDATASETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATASETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETEDATASETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATASETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_IMPORTDATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_IMPORTDATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_IMPORTDATAREQUEST'].fields_by_name['import_configs']._loaded_options = None
    _globals['_IMPORTDATAREQUEST'].fields_by_name['import_configs']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTDATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTDATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_EXPORTDATAREQUEST'].fields_by_name['export_config']._loaded_options = None
    _globals['_EXPORTDATAREQUEST'].fields_by_name['export_config']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATASETVERSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATASETVERSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_CREATEDATASETVERSIONREQUEST'].fields_by_name['dataset_version']._loaded_options = None
    _globals['_CREATEDATASETVERSIONREQUEST'].fields_by_name['dataset_version']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDATASETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATASETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/DatasetVersion'
    _globals['_GETDATASETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/DatasetVersion'
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['read_mask']._loaded_options = None
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['read_mask']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTDATASETVERSIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_RESTOREDATASETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESTOREDATASETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/DatasetVersion'
    _globals['_LISTDATAITEMSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATAITEMSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_SEARCHDATAITEMSREQUEST_ORDERBYANNOTATION'].fields_by_name['saved_query']._loaded_options = None
    _globals['_SEARCHDATAITEMSREQUEST_ORDERBYANNOTATION'].fields_by_name['saved_query']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['saved_query']._loaded_options = None
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['saved_query']._serialized_options = b'\x18\x01\xfaA&\n$aiplatform.googleapis.com/SavedQuery'
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['annotations_filter']._loaded_options = None
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['annotations_filter']._serialized_options = b'\x18\x01'
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_SEARCHDATAITEMSREQUEST'].fields_by_name['order_by']._serialized_options = b'\x18\x01'
    _globals['_LISTSAVEDQUERIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSAVEDQUERIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_DELETESAVEDQUERYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESAVEDQUERYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$aiplatform.googleapis.com/SavedQuery'
    _globals['_GETANNOTATIONSPECREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETANNOTATIONSPECREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/AnnotationSpec'
    _globals['_LISTANNOTATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTANNOTATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/DataItem'
    _globals['_DATASETSERVICE']._loaded_options = None
    _globals['_DATASETSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATASETSERVICE'].methods_by_name['CreateDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['CreateDataset']._serialized_options = b'\xcaA)\n\x07Dataset\x12\x1eCreateDatasetOperationMetadata\xdaA\x0eparent,dataset\x82\xd3\xe4\x93\x02P",/v1/{parent=projects/*/locations/*}/datasets:\x07datasetZ\x17"\x0c/v1/datasets:\x07dataset'
    _globals['_DATASETSERVICE'].methods_by_name['GetDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetDataset']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02G\x12,/v1/{name=projects/*/locations/*/datasets/*}Z\x17\x12\x15/v1/{name=datasets/*}'
    _globals['_DATASETSERVICE'].methods_by_name['UpdateDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['UpdateDataset']._serialized_options = b'\xdaA\x13dataset,update_mask\x82\xd3\xe4\x93\x02i24/v1/{dataset.name=projects/*/locations/*/datasets/*}:\x07datasetZ(2\x1d/v1/{dataset.name=datasets/*}:\x07dataset'
    _globals['_DATASETSERVICE'].methods_by_name['ListDatasets']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ListDatasets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12,/v1/{parent=projects/*/locations/*}/datasetsZ\x0e\x12\x0c/v1/datasets'
    _globals['_DATASETSERVICE'].methods_by_name['DeleteDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['DeleteDataset']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02G*,/v1/{name=projects/*/locations/*/datasets/*}Z\x17*\x15/v1/{name=datasets/*}'
    _globals['_DATASETSERVICE'].methods_by_name['ImportData']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ImportData']._serialized_options = b'\xcaA1\n\x12ImportDataResponse\x12\x1bImportDataOperationMetadata\xdaA\x13name,import_configs\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/locations/*/datasets/*}:import:\x01*'
    _globals['_DATASETSERVICE'].methods_by_name['ExportData']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ExportData']._serialized_options = b'\xcaA1\n\x12ExportDataResponse\x12\x1bExportDataOperationMetadata\xdaA\x12name,export_config\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/locations/*/datasets/*}:export:\x01*'
    _globals['_DATASETSERVICE'].methods_by_name['CreateDatasetVersion']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['CreateDatasetVersion']._serialized_options = b'\xcaA7\n\x0eDatasetVersion\x12%CreateDatasetVersionOperationMetadata\xdaA\x16parent,dataset_version\x82\xd3\xe4\x93\x02\x8d\x01">/v1/{parent=projects/*/locations/*/datasets/*}/datasetVersions:\x0fdataset_versionZ:"\'/v1/{parent=datasets/*}/datasetVersions:\x0fdataset_version'
    _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetVersion']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetVersion']._serialized_options = b'\xdaA\x1bdataset_version,update_mask\x82\xd3\xe4\x93\x02\xad\x012N/v1/{dataset_version.name=projects/*/locations/*/datasets/*/datasetVersions/*}:\x0fdataset_versionZJ27/v1/{dataset_version.name=datasets/*/datasetVersions/*}:\x0fdataset_version'
    _globals['_DATASETSERVICE'].methods_by_name['DeleteDatasetVersion']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['DeleteDatasetVersion']._serialized_options = b"\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02k*>/v1/{name=projects/*/locations/*/datasets/*/datasetVersions/*}Z)*'/v1/{name=datasets/*/datasetVersions/*}"
    _globals['_DATASETSERVICE'].methods_by_name['GetDatasetVersion']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetDatasetVersion']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02k\x12>/v1/{name=projects/*/locations/*/datasets/*/datasetVersions/*}Z)\x12'/v1/{name=datasets/*/datasetVersions/*}"
    _globals['_DATASETSERVICE'].methods_by_name['ListDatasetVersions']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ListDatasetVersions']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02k\x12>/v1/{parent=projects/*/locations/*/datasets/*}/datasetVersionsZ)\x12'/v1/{parent=datasets/*}/datasetVersions"
    _globals['_DATASETSERVICE'].methods_by_name['RestoreDatasetVersion']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['RestoreDatasetVersion']._serialized_options = b'\xcaA8\n\x0eDatasetVersion\x12&RestoreDatasetVersionOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02{\x12F/v1/{name=projects/*/locations/*/datasets/*/datasetVersions/*}:restoreZ1\x12//v1/{name=datasets/*/datasetVersions/*}:restore'
    _globals['_DATASETSERVICE'].methods_by_name['ListDataItems']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ListDataItems']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1/{parent=projects/*/locations/*/datasets/*}/dataItems'
    _globals['_DATASETSERVICE'].methods_by_name['SearchDataItems']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['SearchDataItems']._serialized_options = b'\x82\xd3\xe4\x93\x02A\x12?/v1/{dataset=projects/*/locations/*/datasets/*}:searchDataItems'
    _globals['_DATASETSERVICE'].methods_by_name['ListSavedQueries']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ListSavedQueries']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1/{parent=projects/*/locations/*/datasets/*}/savedQueries'
    _globals['_DATASETSERVICE'].methods_by_name['DeleteSavedQuery']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['DeleteSavedQuery']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1/{name=projects/*/locations/*/datasets/*/savedQueries/*}'
    _globals['_DATASETSERVICE'].methods_by_name['GetAnnotationSpec']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetAnnotationSpec']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/{name=projects/*/locations/*/datasets/*/annotationSpecs/*}'
    _globals['_DATASETSERVICE'].methods_by_name['ListAnnotations']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ListAnnotations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v1/{parent=projects/*/locations/*/datasets/*/dataItems/*}/annotations'
    _globals['_CREATEDATASETREQUEST']._serialized_start = 657
    _globals['_CREATEDATASETREQUEST']._serialized_end = 797
    _globals['_CREATEDATASETOPERATIONMETADATA']._serialized_start = 799
    _globals['_CREATEDATASETOPERATIONMETADATA']._serialized_end = 911
    _globals['_GETDATASETREQUEST']._serialized_start = 913
    _globals['_GETDATASETREQUEST']._serialized_end = 1036
    _globals['_UPDATEDATASETREQUEST']._serialized_start = 1039
    _globals['_UPDATEDATASETREQUEST']._serialized_end = 1174
    _globals['_UPDATEDATASETVERSIONREQUEST']._serialized_start = 1177
    _globals['_UPDATEDATASETVERSIONREQUEST']._serialized_end = 1334
    _globals['_LISTDATASETSREQUEST']._serialized_start = 1337
    _globals['_LISTDATASETSREQUEST']._serialized_end = 1537
    _globals['_LISTDATASETSRESPONSE']._serialized_start = 1539
    _globals['_LISTDATASETSRESPONSE']._serialized_end = 1641
    _globals['_DELETEDATASETREQUEST']._serialized_start = 1643
    _globals['_DELETEDATASETREQUEST']._serialized_end = 1722
    _globals['_IMPORTDATAREQUEST']._serialized_start = 1725
    _globals['_IMPORTDATAREQUEST']._serialized_end = 1876
    _globals['_IMPORTDATARESPONSE']._serialized_start = 1878
    _globals['_IMPORTDATARESPONSE']._serialized_end = 1898
    _globals['_IMPORTDATAOPERATIONMETADATA']._serialized_start = 1900
    _globals['_IMPORTDATAOPERATIONMETADATA']._serialized_end = 2009
    _globals['_EXPORTDATAREQUEST']._serialized_start = 2012
    _globals['_EXPORTDATAREQUEST']._serialized_end = 2162
    _globals['_EXPORTDATARESPONSE']._serialized_start = 2164
    _globals['_EXPORTDATARESPONSE']._serialized_end = 2273
    _globals['_EXPORTDATAOPERATIONMETADATA']._serialized_start = 2276
    _globals['_EXPORTDATAOPERATIONMETADATA']._serialized_end = 2415
    _globals['_CREATEDATASETVERSIONREQUEST']._serialized_start = 2418
    _globals['_CREATEDATASETVERSIONREQUEST']._serialized_end = 2580
    _globals['_CREATEDATASETVERSIONOPERATIONMETADATA']._serialized_start = 2582
    _globals['_CREATEDATASETVERSIONOPERATIONMETADATA']._serialized_end = 2701
    _globals['_DELETEDATASETVERSIONREQUEST']._serialized_start = 2703
    _globals['_DELETEDATASETVERSIONREQUEST']._serialized_end = 2796
    _globals['_GETDATASETVERSIONREQUEST']._serialized_start = 2799
    _globals['_GETDATASETVERSIONREQUEST']._serialized_end = 2936
    _globals['_LISTDATASETVERSIONSREQUEST']._serialized_start = 2939
    _globals['_LISTDATASETVERSIONSREQUEST']._serialized_end = 3171
    _globals['_LISTDATASETVERSIONSRESPONSE']._serialized_start = 3173
    _globals['_LISTDATASETVERSIONSRESPONSE']._serialized_end = 3297
    _globals['_RESTOREDATASETVERSIONREQUEST']._serialized_start = 3299
    _globals['_RESTOREDATASETVERSIONREQUEST']._serialized_end = 3393
    _globals['_RESTOREDATASETVERSIONOPERATIONMETADATA']._serialized_start = 3395
    _globals['_RESTOREDATASETVERSIONOPERATIONMETADATA']._serialized_end = 3515
    _globals['_LISTDATAITEMSREQUEST']._serialized_start = 3518
    _globals['_LISTDATAITEMSREQUEST']._serialized_end = 3719
    _globals['_LISTDATAITEMSRESPONSE']._serialized_start = 3721
    _globals['_LISTDATAITEMSRESPONSE']._serialized_end = 3827
    _globals['_SEARCHDATAITEMSREQUEST']._serialized_start = 3830
    _globals['_SEARCHDATAITEMSREQUEST']._serialized_end = 4434
    _globals['_SEARCHDATAITEMSREQUEST_ORDERBYANNOTATION']._serialized_start = 4362
    _globals['_SEARCHDATAITEMSREQUEST_ORDERBYANNOTATION']._serialized_end = 4425
    _globals['_SEARCHDATAITEMSRESPONSE']._serialized_start = 4436
    _globals['_SEARCHDATAITEMSRESPONSE']._serialized_end = 4553
    _globals['_DATAITEMVIEW']._serialized_start = 4556
    _globals['_DATAITEMVIEW']._serialized_end = 4723
    _globals['_LISTSAVEDQUERIESREQUEST']._serialized_start = 4726
    _globals['_LISTSAVEDQUERIESREQUEST']._serialized_end = 4930
    _globals['_LISTSAVEDQUERIESRESPONSE']._serialized_start = 4932
    _globals['_LISTSAVEDQUERIESRESPONSE']._serialized_end = 5046
    _globals['_DELETESAVEDQUERYREQUEST']._serialized_start = 5048
    _globals['_DELETESAVEDQUERYREQUEST']._serialized_end = 5133
    _globals['_GETANNOTATIONSPECREQUEST']._serialized_start = 5136
    _globals['_GETANNOTATIONSPECREQUEST']._serialized_end = 5273
    _globals['_LISTANNOTATIONSREQUEST']._serialized_start = 5276
    _globals['_LISTANNOTATIONSREQUEST']._serialized_end = 5480
    _globals['_LISTANNOTATIONSRESPONSE']._serialized_start = 5482
    _globals['_LISTANNOTATIONSRESPONSE']._serialized_end = 5593
    _globals['_DATASETSERVICE']._serialized_start = 5596
    _globals['_DATASETSERVICE']._serialized_end = 10293