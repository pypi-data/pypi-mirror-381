"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/model_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1 import evaluated_annotation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_evaluated__annotation__pb2
from .....google.cloud.aiplatform.v1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_explanation__pb2
from .....google.cloud.aiplatform.v1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_io__pb2
from .....google.cloud.aiplatform.v1 import model_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_model__pb2
from .....google.cloud.aiplatform.v1 import model_evaluation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_model__evaluation__pb2
from .....google.cloud.aiplatform.v1 import model_evaluation_slice_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_model__evaluation__slice__pb2
from .....google.cloud.aiplatform.v1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/aiplatform/v1/model_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/aiplatform/v1/encryption_spec.proto\x1a5google/cloud/aiplatform/v1/evaluated_annotation.proto\x1a,google/cloud/aiplatform/v1/explanation.proto\x1a#google/cloud/aiplatform/v1/io.proto\x1a&google/cloud/aiplatform/v1/model.proto\x1a1google/cloud/aiplatform/v1/model_evaluation.proto\x1a7google/cloud/aiplatform/v1/model_evaluation_slice.proto\x1a*google/cloud/aiplatform/v1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xd6\x01\n\x12UploadModelRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x19\n\x0cparent_model\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08model_id\x18\x05 \x01(\tB\x03\xe0A\x01\x125\n\x05model\x18\x02 \x01(\x0b2!.google.cloud.aiplatform.v1.ModelB\x03\xe0A\x02\x12\x1c\n\x0fservice_account\x18\x06 \x01(\tB\x03\xe0A\x01"n\n\x1cUploadModelOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"i\n\x13UploadModelResponse\x123\n\x05model\x18\x01 \x01(\tB$\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x1d\n\x10model_version_id\x18\x02 \x01(\tB\x03\xe0A\x03"H\n\x0fGetModelRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model"\xc6\x01\n\x11ListModelsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x10\n\x08order_by\x18\x06 \x01(\t"`\n\x12ListModelsResponse\x121\n\x06models\x18\x01 \x03(\x0b2!.google.cloud.aiplatform.v1.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc9\x01\n\x18ListModelVersionsRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x10\n\x08order_by\x18\x06 \x01(\t"g\n\x19ListModelVersionsResponse\x121\n\x06models\x18\x01 \x03(\x0b2!.google.cloud.aiplatform.v1.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8c\x01\n"ListModelVersionCheckpointsRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"L\n\x16ModelVersionCheckpoint\x12\x15\n\rcheckpoint_id\x18\x01 \x01(\t\x12\r\n\x05epoch\x18\x02 \x01(\x03\x12\x0c\n\x04step\x18\x03 \x01(\x03"\x87\x01\n#ListModelVersionCheckpointsResponse\x12G\n\x0bcheckpoints\x18\x01 \x03(\x0b22.google.cloud.aiplatform.v1.ModelVersionCheckpoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x81\x01\n\x12UpdateModelRequest\x125\n\x05model\x18\x01 \x01(\x0b2!.google.cloud.aiplatform.v1.ModelB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\x91\x01\n\x1fUpdateExplanationDatasetRequest\x126\n\x05model\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x126\n\x08examples\x18\x02 \x01(\x0b2$.google.cloud.aiplatform.v1.Examples"{\n)UpdateExplanationDatasetOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"K\n\x12DeleteModelRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model"R\n\x19DeleteModelVersionRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model"q\n\x1aMergeVersionAliasesRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x1c\n\x0fversion_aliases\x18\x02 \x03(\tB\x03\xe0A\x02"\xee\x02\n\x12ExportModelRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12W\n\routput_config\x18\x02 \x01(\x0b2;.google.cloud.aiplatform.v1.ExportModelRequest.OutputConfigB\x03\xe0A\x02\x1a\xc7\x01\n\x0cOutputConfig\x12\x18\n\x10export_format_id\x18\x01 \x01(\t\x12H\n\x14artifact_destination\x18\x03 \x01(\x0b2*.google.cloud.aiplatform.v1.GcsDestination\x12S\n\x11image_destination\x18\x04 \x01(\x0b28.google.cloud.aiplatform.v1.ContainerRegistryDestination"\x9c\x02\n\x1cExportModelOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata\x12]\n\x0boutput_info\x18\x02 \x01(\x0b2C.google.cloud.aiplatform.v1.ExportModelOperationMetadata.OutputInfoB\x03\xe0A\x03\x1aM\n\nOutputInfo\x12 \n\x13artifact_output_uri\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10image_output_uri\x18\x03 \x01(\tB\x03\xe0A\x03""\n UpdateExplanationDatasetResponse"\x15\n\x13ExportModelResponse"\xc0\x02\n\x10CopyModelRequest\x12\x17\n\x08model_id\x18\x04 \x01(\tB\x03\xe0A\x01H\x00\x12?\n\x0cparent_model\x18\x05 \x01(\tB\'\xe0A\x01\xfaA!\n\x1faiplatform.googleapis.com/ModelH\x00\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12=\n\x0csource_model\x18\x02 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12C\n\x0fencryption_spec\x18\x03 \x01(\x0b2*.google.cloud.aiplatform.v1.EncryptionSpecB\x13\n\x11destination_model"l\n\x1aCopyModelOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"g\n\x11CopyModelResponse\x123\n\x05model\x18\x01 \x01(\tB$\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x1d\n\x10model_version_id\x18\x02 \x01(\tB\x03\xe0A\x03"\xa3\x01\n\x1cImportModelEvaluationRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12J\n\x10model_evaluation\x18\x02 \x01(\x0b2+.google.cloud.aiplatform.v1.ModelEvaluationB\x03\xe0A\x02"\xc4\x01\n\'BatchImportModelEvaluationSlicesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ModelEvaluation\x12V\n\x17model_evaluation_slices\x18\x02 \x03(\x0b20.google.cloud.aiplatform.v1.ModelEvaluationSliceB\x03\xe0A\x02"Y\n(BatchImportModelEvaluationSlicesResponse\x12-\n imported_model_evaluation_slices\x18\x01 \x03(\tB\x03\xe0A\x03"\xc5\x01\n&BatchImportEvaluatedAnnotationsRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.aiplatform.googleapis.com/ModelEvaluationSlice\x12S\n\x15evaluated_annotations\x18\x02 \x03(\x0b2/.google.cloud.aiplatform.v1.EvaluatedAnnotationB\x03\xe0A\x02"\\\n\'BatchImportEvaluatedAnnotationsResponse\x121\n$imported_evaluated_annotations_count\x18\x01 \x01(\x05B\x03\xe0A\x03"\\\n\x19GetModelEvaluationRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ModelEvaluation"\xbc\x01\n\x1bListModelEvaluationsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x7f\n\x1cListModelEvaluationsResponse\x12F\n\x11model_evaluations\x18\x01 \x03(\x0b2+.google.cloud.aiplatform.v1.ModelEvaluation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"f\n\x1eGetModelEvaluationSliceRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.aiplatform.googleapis.com/ModelEvaluationSlice"\xcb\x01\n ListModelEvaluationSlicesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ModelEvaluation\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x8f\x01\n!ListModelEvaluationSlicesResponse\x12Q\n\x17model_evaluation_slices\x18\x01 \x03(\x0b20.google.cloud.aiplatform.v1.ModelEvaluationSlice\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x89"\n\x0cModelService\x12\xe0\x01\n\x0bUploadModel\x12..google.cloud.aiplatform.v1.UploadModelRequest\x1a\x1d.google.longrunning.Operation"\x81\x01\xcaA3\n\x13UploadModelResponse\x12\x1cUploadModelOperationMetadata\xdaA\x0cparent,model\x82\xd3\xe4\x93\x026"1/v1/{parent=projects/*/locations/*}/models:upload:\x01*\x12\x95\x01\n\x08GetModel\x12+.google.cloud.aiplatform.v1.GetModelRequest\x1a!.google.cloud.aiplatform.v1.Model"9\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v1/{name=projects/*/locations/*/models/*}\x12\xa8\x01\n\nListModels\x12-.google.cloud.aiplatform.v1.ListModelsRequest\x1a..google.cloud.aiplatform.v1.ListModelsResponse";\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=projects/*/locations/*}/models\x12\xc8\x01\n\x11ListModelVersions\x124.google.cloud.aiplatform.v1.ListModelVersionsRequest\x1a5.google.cloud.aiplatform.v1.ListModelVersionsResponse"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/{name=projects/*/locations/*/models/*}:listVersions\x12\xe9\x01\n\x1bListModelVersionCheckpoints\x12>.google.cloud.aiplatform.v1.ListModelVersionCheckpointsRequest\x1a?.google.cloud.aiplatform.v1.ListModelVersionCheckpointsResponse"I\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=projects/*/locations/*/models/*}:listCheckpoints\x12\xb5\x01\n\x0bUpdateModel\x12..google.cloud.aiplatform.v1.UpdateModelRequest\x1a!.google.cloud.aiplatform.v1.Model"S\xdaA\x11model,update_mask\x82\xd3\xe4\x93\x02920/v1/{model.name=projects/*/locations/*/models/*}:\x05model\x12\xa0\x02\n\x18UpdateExplanationDataset\x12;.google.cloud.aiplatform.v1.UpdateExplanationDatasetRequest\x1a\x1d.google.longrunning.Operation"\xa7\x01\xcaAM\n UpdateExplanationDatasetResponse\x12)UpdateExplanationDatasetOperationMetadata\xdaA\x05model\x82\xd3\xe4\x93\x02I"D/v1/{model=projects/*/locations/*/models/*}:updateExplanationDataset:\x01*\x12\xca\x01\n\x0bDeleteModel\x12..google.cloud.aiplatform.v1.DeleteModelRequest\x1a\x1d.google.longrunning.Operation"l\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v1/{name=projects/*/locations/*/models/*}\x12\xe6\x01\n\x12DeleteModelVersion\x125.google.cloud.aiplatform.v1.DeleteModelVersionRequest\x1a\x1d.google.longrunning.Operation"z\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/locations/*/models/*}:deleteVersion\x12\xd2\x01\n\x13MergeVersionAliases\x126.google.cloud.aiplatform.v1.MergeVersionAliasesRequest\x1a!.google.cloud.aiplatform.v1.Model"`\xdaA\x14name,version_aliases\x82\xd3\xe4\x93\x02C">/v1/{name=projects/*/locations/*/models/*}:mergeVersionAliases:\x01*\x12\xe6\x01\n\x0bExportModel\x12..google.cloud.aiplatform.v1.ExportModelRequest\x1a\x1d.google.longrunning.Operation"\x87\x01\xcaA3\n\x13ExportModelResponse\x12\x1cExportModelOperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/models/*}:export:\x01*\x12\xdd\x01\n\tCopyModel\x12,.google.cloud.aiplatform.v1.CopyModelRequest\x1a\x1d.google.longrunning.Operation"\x82\x01\xcaA/\n\x11CopyModelResponse\x12\x1aCopyModelOperationMetadata\xdaA\x13parent,source_model\x82\xd3\xe4\x93\x024"//v1/{parent=projects/*/locations/*}/models:copy:\x01*\x12\xe4\x01\n\x15ImportModelEvaluation\x128.google.cloud.aiplatform.v1.ImportModelEvaluationRequest\x1a+.google.cloud.aiplatform.v1.ModelEvaluation"d\xdaA\x17parent,model_evaluation\x82\xd3\xe4\x93\x02D"?/v1/{parent=projects/*/locations/*/models/*}/evaluations:import:\x01*\x12\xa8\x02\n BatchImportModelEvaluationSlices\x12C.google.cloud.aiplatform.v1.BatchImportModelEvaluationSlicesRequest\x1aD.google.cloud.aiplatform.v1.BatchImportModelEvaluationSlicesResponse"y\xdaA\x1eparent,model_evaluation_slices\x82\xd3\xe4\x93\x02R"M/v1/{parent=projects/*/locations/*/models/*/evaluations/*}/slices:batchImport:\x01*\x12\xa5\x02\n\x1fBatchImportEvaluatedAnnotations\x12B.google.cloud.aiplatform.v1.BatchImportEvaluatedAnnotationsRequest\x1aC.google.cloud.aiplatform.v1.BatchImportEvaluatedAnnotationsResponse"y\xdaA\x1cparent,evaluated_annotations\x82\xd3\xe4\x93\x02T"O/v1/{parent=projects/*/locations/*/models/*/evaluations/*/slices/*}:batchImport:\x01*\x12\xc1\x01\n\x12GetModelEvaluation\x125.google.cloud.aiplatform.v1.GetModelEvaluationRequest\x1a+.google.cloud.aiplatform.v1.ModelEvaluation"G\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1/{name=projects/*/locations/*/models/*/evaluations/*}\x12\xd4\x01\n\x14ListModelEvaluations\x127.google.cloud.aiplatform.v1.ListModelEvaluationsRequest\x1a8.google.cloud.aiplatform.v1.ListModelEvaluationsResponse"I\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1/{parent=projects/*/locations/*/models/*}/evaluations\x12\xd9\x01\n\x17GetModelEvaluationSlice\x12:.google.cloud.aiplatform.v1.GetModelEvaluationSliceRequest\x1a0.google.cloud.aiplatform.v1.ModelEvaluationSlice"P\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v1/{name=projects/*/locations/*/models/*/evaluations/*/slices/*}\x12\xec\x01\n\x19ListModelEvaluationSlices\x12<.google.cloud.aiplatform.v1.ListModelEvaluationSlicesRequest\x1a=.google.cloud.aiplatform.v1.ListModelEvaluationSlicesResponse"R\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1/{parent=projects/*/locations/*/models/*/evaluations/*}/slices\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xcf\x01\n\x1ecom.google.cloud.aiplatform.v1B\x11ModelServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.model_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x11ModelServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_UPLOADMODELREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_UPLOADMODELREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_UPLOADMODELREQUEST'].fields_by_name['parent_model']._loaded_options = None
    _globals['_UPLOADMODELREQUEST'].fields_by_name['parent_model']._serialized_options = b'\xe0A\x01'
    _globals['_UPLOADMODELREQUEST'].fields_by_name['model_id']._loaded_options = None
    _globals['_UPLOADMODELREQUEST'].fields_by_name['model_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPLOADMODELREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_UPLOADMODELREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADMODELREQUEST'].fields_by_name['service_account']._loaded_options = None
    _globals['_UPLOADMODELREQUEST'].fields_by_name['service_account']._serialized_options = b'\xe0A\x01'
    _globals['_UPLOADMODELRESPONSE'].fields_by_name['model']._loaded_options = None
    _globals['_UPLOADMODELRESPONSE'].fields_by_name['model']._serialized_options = b'\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_UPLOADMODELRESPONSE'].fields_by_name['model_version_id']._loaded_options = None
    _globals['_UPLOADMODELRESPONSE'].fields_by_name['model_version_id']._serialized_options = b'\xe0A\x03'
    _globals['_GETMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_LISTMODELSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMODELSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTMODELVERSIONSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTMODELVERSIONSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_LISTMODELVERSIONCHECKPOINTSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LISTMODELVERSIONCHECKPOINTSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_LISTMODELVERSIONCHECKPOINTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTMODELVERSIONCHECKPOINTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMODELVERSIONCHECKPOINTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTMODELVERSIONCHECKPOINTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEMODELREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_UPDATEMODELREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMODELREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMODELREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEEXPLANATIONDATASETREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_UPDATEEXPLANATIONDATASETREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_DELETEMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_DELETEMODELVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMODELVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_MERGEVERSIONALIASESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MERGEVERSIONALIASESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_MERGEVERSIONALIASESREQUEST'].fields_by_name['version_aliases']._loaded_options = None
    _globals['_MERGEVERSIONALIASESREQUEST'].fields_by_name['version_aliases']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_EXPORTMODELREQUEST'].fields_by_name['output_config']._loaded_options = None
    _globals['_EXPORTMODELREQUEST'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_EXPORTMODELOPERATIONMETADATA_OUTPUTINFO'].fields_by_name['artifact_output_uri']._loaded_options = None
    _globals['_EXPORTMODELOPERATIONMETADATA_OUTPUTINFO'].fields_by_name['artifact_output_uri']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTMODELOPERATIONMETADATA_OUTPUTINFO'].fields_by_name['image_output_uri']._loaded_options = None
    _globals['_EXPORTMODELOPERATIONMETADATA_OUTPUTINFO'].fields_by_name['image_output_uri']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTMODELOPERATIONMETADATA'].fields_by_name['output_info']._loaded_options = None
    _globals['_EXPORTMODELOPERATIONMETADATA'].fields_by_name['output_info']._serialized_options = b'\xe0A\x03'
    _globals['_COPYMODELREQUEST'].fields_by_name['model_id']._loaded_options = None
    _globals['_COPYMODELREQUEST'].fields_by_name['model_id']._serialized_options = b'\xe0A\x01'
    _globals['_COPYMODELREQUEST'].fields_by_name['parent_model']._loaded_options = None
    _globals['_COPYMODELREQUEST'].fields_by_name['parent_model']._serialized_options = b'\xe0A\x01\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_COPYMODELREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_COPYMODELREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_COPYMODELREQUEST'].fields_by_name['source_model']._loaded_options = None
    _globals['_COPYMODELREQUEST'].fields_by_name['source_model']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_COPYMODELRESPONSE'].fields_by_name['model']._loaded_options = None
    _globals['_COPYMODELRESPONSE'].fields_by_name['model']._serialized_options = b'\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_COPYMODELRESPONSE'].fields_by_name['model_version_id']._loaded_options = None
    _globals['_COPYMODELRESPONSE'].fields_by_name['model_version_id']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTMODELEVALUATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTMODELEVALUATIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_IMPORTMODELEVALUATIONREQUEST'].fields_by_name['model_evaluation']._loaded_options = None
    _globals['_IMPORTMODELEVALUATIONREQUEST'].fields_by_name['model_evaluation']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ModelEvaluation'
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESREQUEST'].fields_by_name['model_evaluation_slices']._loaded_options = None
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESREQUEST'].fields_by_name['model_evaluation_slices']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESRESPONSE'].fields_by_name['imported_model_evaluation_slices']._loaded_options = None
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESRESPONSE'].fields_by_name['imported_model_evaluation_slices']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\n.aiplatform.googleapis.com/ModelEvaluationSlice'
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSREQUEST'].fields_by_name['evaluated_annotations']._loaded_options = None
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSREQUEST'].fields_by_name['evaluated_annotations']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSRESPONSE'].fields_by_name['imported_evaluated_annotations_count']._loaded_options = None
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSRESPONSE'].fields_by_name['imported_evaluated_annotations_count']._serialized_options = b'\xe0A\x03'
    _globals['_GETMODELEVALUATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELEVALUATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ModelEvaluation'
    _globals['_LISTMODELEVALUATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMODELEVALUATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_GETMODELEVALUATIONSLICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELEVALUATIONSLICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.aiplatform.googleapis.com/ModelEvaluationSlice'
    _globals['_LISTMODELEVALUATIONSLICESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMODELEVALUATIONSLICESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ModelEvaluation'
    _globals['_MODELSERVICE']._loaded_options = None
    _globals['_MODELSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MODELSERVICE'].methods_by_name['UploadModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['UploadModel']._serialized_options = b'\xcaA3\n\x13UploadModelResponse\x12\x1cUploadModelOperationMetadata\xdaA\x0cparent,model\x82\xd3\xe4\x93\x026"1/v1/{parent=projects/*/locations/*}/models:upload:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02,\x12*/v1/{name=projects/*/locations/*/models/*}'
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02,\x12*/v1/{parent=projects/*/locations/*}/models'
    _globals['_MODELSERVICE'].methods_by_name['ListModelVersions']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModelVersions']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/{name=projects/*/locations/*/models/*}:listVersions'
    _globals['_MODELSERVICE'].methods_by_name['ListModelVersionCheckpoints']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModelVersionCheckpoints']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=projects/*/locations/*/models/*}:listCheckpoints'
    _globals['_MODELSERVICE'].methods_by_name['UpdateModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['UpdateModel']._serialized_options = b'\xdaA\x11model,update_mask\x82\xd3\xe4\x93\x02920/v1/{model.name=projects/*/locations/*/models/*}:\x05model'
    _globals['_MODELSERVICE'].methods_by_name['UpdateExplanationDataset']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['UpdateExplanationDataset']._serialized_options = b'\xcaAM\n UpdateExplanationDatasetResponse\x12)UpdateExplanationDatasetOperationMetadata\xdaA\x05model\x82\xd3\xe4\x93\x02I"D/v1/{model=projects/*/locations/*/models/*}:updateExplanationDataset:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['DeleteModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['DeleteModel']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02,**/v1/{name=projects/*/locations/*/models/*}'
    _globals['_MODELSERVICE'].methods_by_name['DeleteModelVersion']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['DeleteModelVersion']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v1/{name=projects/*/locations/*/models/*}:deleteVersion'
    _globals['_MODELSERVICE'].methods_by_name['MergeVersionAliases']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['MergeVersionAliases']._serialized_options = b'\xdaA\x14name,version_aliases\x82\xd3\xe4\x93\x02C">/v1/{name=projects/*/locations/*/models/*}:mergeVersionAliases:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['ExportModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ExportModel']._serialized_options = b'\xcaA3\n\x13ExportModelResponse\x12\x1cExportModelOperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/models/*}:export:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['CopyModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['CopyModel']._serialized_options = b'\xcaA/\n\x11CopyModelResponse\x12\x1aCopyModelOperationMetadata\xdaA\x13parent,source_model\x82\xd3\xe4\x93\x024"//v1/{parent=projects/*/locations/*}/models:copy:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['ImportModelEvaluation']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ImportModelEvaluation']._serialized_options = b'\xdaA\x17parent,model_evaluation\x82\xd3\xe4\x93\x02D"?/v1/{parent=projects/*/locations/*/models/*}/evaluations:import:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['BatchImportModelEvaluationSlices']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['BatchImportModelEvaluationSlices']._serialized_options = b'\xdaA\x1eparent,model_evaluation_slices\x82\xd3\xe4\x93\x02R"M/v1/{parent=projects/*/locations/*/models/*/evaluations/*}/slices:batchImport:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['BatchImportEvaluatedAnnotations']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['BatchImportEvaluatedAnnotations']._serialized_options = b'\xdaA\x1cparent,evaluated_annotations\x82\xd3\xe4\x93\x02T"O/v1/{parent=projects/*/locations/*/models/*/evaluations/*/slices/*}:batchImport:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['GetModelEvaluation']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['GetModelEvaluation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1/{name=projects/*/locations/*/models/*/evaluations/*}'
    _globals['_MODELSERVICE'].methods_by_name['ListModelEvaluations']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModelEvaluations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02:\x128/v1/{parent=projects/*/locations/*/models/*}/evaluations'
    _globals['_MODELSERVICE'].methods_by_name['GetModelEvaluationSlice']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['GetModelEvaluationSlice']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v1/{name=projects/*/locations/*/models/*/evaluations/*/slices/*}'
    _globals['_MODELSERVICE'].methods_by_name['ListModelEvaluationSlices']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModelEvaluationSlices']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1/{parent=projects/*/locations/*/models/*/evaluations/*}/slices'
    _globals['_UPLOADMODELREQUEST']._serialized_start = 674
    _globals['_UPLOADMODELREQUEST']._serialized_end = 888
    _globals['_UPLOADMODELOPERATIONMETADATA']._serialized_start = 890
    _globals['_UPLOADMODELOPERATIONMETADATA']._serialized_end = 1000
    _globals['_UPLOADMODELRESPONSE']._serialized_start = 1002
    _globals['_UPLOADMODELRESPONSE']._serialized_end = 1107
    _globals['_GETMODELREQUEST']._serialized_start = 1109
    _globals['_GETMODELREQUEST']._serialized_end = 1181
    _globals['_LISTMODELSREQUEST']._serialized_start = 1184
    _globals['_LISTMODELSREQUEST']._serialized_end = 1382
    _globals['_LISTMODELSRESPONSE']._serialized_start = 1384
    _globals['_LISTMODELSRESPONSE']._serialized_end = 1480
    _globals['_LISTMODELVERSIONSREQUEST']._serialized_start = 1483
    _globals['_LISTMODELVERSIONSREQUEST']._serialized_end = 1684
    _globals['_LISTMODELVERSIONSRESPONSE']._serialized_start = 1686
    _globals['_LISTMODELVERSIONSRESPONSE']._serialized_end = 1789
    _globals['_LISTMODELVERSIONCHECKPOINTSREQUEST']._serialized_start = 1792
    _globals['_LISTMODELVERSIONCHECKPOINTSREQUEST']._serialized_end = 1932
    _globals['_MODELVERSIONCHECKPOINT']._serialized_start = 1934
    _globals['_MODELVERSIONCHECKPOINT']._serialized_end = 2010
    _globals['_LISTMODELVERSIONCHECKPOINTSRESPONSE']._serialized_start = 2013
    _globals['_LISTMODELVERSIONCHECKPOINTSRESPONSE']._serialized_end = 2148
    _globals['_UPDATEMODELREQUEST']._serialized_start = 2151
    _globals['_UPDATEMODELREQUEST']._serialized_end = 2280
    _globals['_UPDATEEXPLANATIONDATASETREQUEST']._serialized_start = 2283
    _globals['_UPDATEEXPLANATIONDATASETREQUEST']._serialized_end = 2428
    _globals['_UPDATEEXPLANATIONDATASETOPERATIONMETADATA']._serialized_start = 2430
    _globals['_UPDATEEXPLANATIONDATASETOPERATIONMETADATA']._serialized_end = 2553
    _globals['_DELETEMODELREQUEST']._serialized_start = 2555
    _globals['_DELETEMODELREQUEST']._serialized_end = 2630
    _globals['_DELETEMODELVERSIONREQUEST']._serialized_start = 2632
    _globals['_DELETEMODELVERSIONREQUEST']._serialized_end = 2714
    _globals['_MERGEVERSIONALIASESREQUEST']._serialized_start = 2716
    _globals['_MERGEVERSIONALIASESREQUEST']._serialized_end = 2829
    _globals['_EXPORTMODELREQUEST']._serialized_start = 2832
    _globals['_EXPORTMODELREQUEST']._serialized_end = 3198
    _globals['_EXPORTMODELREQUEST_OUTPUTCONFIG']._serialized_start = 2999
    _globals['_EXPORTMODELREQUEST_OUTPUTCONFIG']._serialized_end = 3198
    _globals['_EXPORTMODELOPERATIONMETADATA']._serialized_start = 3201
    _globals['_EXPORTMODELOPERATIONMETADATA']._serialized_end = 3485
    _globals['_EXPORTMODELOPERATIONMETADATA_OUTPUTINFO']._serialized_start = 3408
    _globals['_EXPORTMODELOPERATIONMETADATA_OUTPUTINFO']._serialized_end = 3485
    _globals['_UPDATEEXPLANATIONDATASETRESPONSE']._serialized_start = 3487
    _globals['_UPDATEEXPLANATIONDATASETRESPONSE']._serialized_end = 3521
    _globals['_EXPORTMODELRESPONSE']._serialized_start = 3523
    _globals['_EXPORTMODELRESPONSE']._serialized_end = 3544
    _globals['_COPYMODELREQUEST']._serialized_start = 3547
    _globals['_COPYMODELREQUEST']._serialized_end = 3867
    _globals['_COPYMODELOPERATIONMETADATA']._serialized_start = 3869
    _globals['_COPYMODELOPERATIONMETADATA']._serialized_end = 3977
    _globals['_COPYMODELRESPONSE']._serialized_start = 3979
    _globals['_COPYMODELRESPONSE']._serialized_end = 4082
    _globals['_IMPORTMODELEVALUATIONREQUEST']._serialized_start = 4085
    _globals['_IMPORTMODELEVALUATIONREQUEST']._serialized_end = 4248
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESREQUEST']._serialized_start = 4251
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESREQUEST']._serialized_end = 4447
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESRESPONSE']._serialized_start = 4449
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESRESPONSE']._serialized_end = 4538
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSREQUEST']._serialized_start = 4541
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSREQUEST']._serialized_end = 4738
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSRESPONSE']._serialized_start = 4740
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSRESPONSE']._serialized_end = 4832
    _globals['_GETMODELEVALUATIONREQUEST']._serialized_start = 4834
    _globals['_GETMODELEVALUATIONREQUEST']._serialized_end = 4926
    _globals['_LISTMODELEVALUATIONSREQUEST']._serialized_start = 4929
    _globals['_LISTMODELEVALUATIONSREQUEST']._serialized_end = 5117
    _globals['_LISTMODELEVALUATIONSRESPONSE']._serialized_start = 5119
    _globals['_LISTMODELEVALUATIONSRESPONSE']._serialized_end = 5246
    _globals['_GETMODELEVALUATIONSLICEREQUEST']._serialized_start = 5248
    _globals['_GETMODELEVALUATIONSLICEREQUEST']._serialized_end = 5350
    _globals['_LISTMODELEVALUATIONSLICESREQUEST']._serialized_start = 5353
    _globals['_LISTMODELEVALUATIONSLICESREQUEST']._serialized_end = 5556
    _globals['_LISTMODELEVALUATIONSLICESRESPONSE']._serialized_start = 5559
    _globals['_LISTMODELEVALUATIONSLICESRESPONSE']._serialized_end = 5702
    _globals['_MODELSERVICE']._serialized_start = 5705
    _globals['_MODELSERVICE']._serialized_end = 10066