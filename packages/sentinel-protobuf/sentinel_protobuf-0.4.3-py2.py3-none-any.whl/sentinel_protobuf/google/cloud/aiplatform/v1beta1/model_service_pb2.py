"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/model_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import evaluated_annotation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_evaluated__annotation__pb2
from .....google.cloud.aiplatform.v1beta1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_explanation__pb2
from .....google.cloud.aiplatform.v1beta1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_io__pb2
from .....google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_machine__resources__pb2
from .....google.cloud.aiplatform.v1beta1 import model_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__pb2
from .....google.cloud.aiplatform.v1beta1 import model_evaluation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__evaluation__pb2
from .....google.cloud.aiplatform.v1beta1 import model_evaluation_slice_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__evaluation__slice__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/aiplatform/v1beta1/model_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a:google/cloud/aiplatform/v1beta1/evaluated_annotation.proto\x1a1google/cloud/aiplatform/v1beta1/explanation.proto\x1a(google/cloud/aiplatform/v1beta1/io.proto\x1a7google/cloud/aiplatform/v1beta1/machine_resources.proto\x1a+google/cloud/aiplatform/v1beta1/model.proto\x1a6google/cloud/aiplatform/v1beta1/model_evaluation.proto\x1a<google/cloud/aiplatform/v1beta1/model_evaluation_slice.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xdb\x01\n\x12UploadModelRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x19\n\x0cparent_model\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08model_id\x18\x05 \x01(\tB\x03\xe0A\x01\x12:\n\x05model\x18\x02 \x01(\x0b2&.google.cloud.aiplatform.v1beta1.ModelB\x03\xe0A\x02\x12\x1c\n\x0fservice_account\x18\x06 \x01(\tB\x03\xe0A\x01"s\n\x1cUploadModelOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"i\n\x13UploadModelResponse\x123\n\x05model\x18\x01 \x01(\tB$\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x1d\n\x10model_version_id\x18\x02 \x01(\tB\x03\xe0A\x03"H\n\x0fGetModelRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model"\xb4\x01\n\x11ListModelsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"e\n\x12ListModelsResponse\x126\n\x06models\x18\x01 \x03(\x0b2&.google.cloud.aiplatform.v1beta1.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc9\x01\n\x18ListModelVersionsRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x10\n\x08order_by\x18\x06 \x01(\t"l\n\x19ListModelVersionsResponse\x126\n\x06models\x18\x01 \x03(\x0b2&.google.cloud.aiplatform.v1beta1.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8c\x01\n"ListModelVersionCheckpointsRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"L\n\x16ModelVersionCheckpoint\x12\x15\n\rcheckpoint_id\x18\x01 \x01(\t\x12\r\n\x05epoch\x18\x02 \x01(\x03\x12\x0c\n\x04step\x18\x03 \x01(\x03"\x8c\x01\n#ListModelVersionCheckpointsResponse\x12L\n\x0bcheckpoints\x18\x01 \x03(\x0b27.google.cloud.aiplatform.v1beta1.ModelVersionCheckpoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x86\x01\n\x12UpdateModelRequest\x12:\n\x05model\x18\x01 \x01(\x0b2&.google.cloud.aiplatform.v1beta1.ModelB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\x96\x01\n\x1fUpdateExplanationDatasetRequest\x126\n\x05model\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12;\n\x08examples\x18\x02 \x01(\x0b2).google.cloud.aiplatform.v1beta1.Examples"\x80\x01\n)UpdateExplanationDatasetOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"K\n\x12DeleteModelRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model"R\n\x19DeleteModelVersionRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model"q\n\x1aMergeVersionAliasesRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x1c\n\x0fversion_aliases\x18\x02 \x03(\tB\x03\xe0A\x02"\xfd\x02\n\x12ExportModelRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\\\n\routput_config\x18\x02 \x01(\x0b2@.google.cloud.aiplatform.v1beta1.ExportModelRequest.OutputConfigB\x03\xe0A\x02\x1a\xd1\x01\n\x0cOutputConfig\x12\x18\n\x10export_format_id\x18\x01 \x01(\t\x12M\n\x14artifact_destination\x18\x03 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.GcsDestination\x12X\n\x11image_destination\x18\x04 \x01(\x0b2=.google.cloud.aiplatform.v1beta1.ContainerRegistryDestination"\xa6\x02\n\x1cExportModelOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12b\n\x0boutput_info\x18\x02 \x01(\x0b2H.google.cloud.aiplatform.v1beta1.ExportModelOperationMetadata.OutputInfoB\x03\xe0A\x03\x1aM\n\nOutputInfo\x12 \n\x13artifact_output_uri\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10image_output_uri\x18\x03 \x01(\tB\x03\xe0A\x03""\n UpdateExplanationDatasetResponse"\x15\n\x13ExportModelResponse"\xc5\x02\n\x10CopyModelRequest\x12\x17\n\x08model_id\x18\x04 \x01(\tB\x03\xe0A\x01H\x00\x12?\n\x0cparent_model\x18\x05 \x01(\tB\'\xe0A\x01\xfaA!\n\x1faiplatform.googleapis.com/ModelH\x00\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12=\n\x0csource_model\x18\x02 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12H\n\x0fencryption_spec\x18\x03 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpecB\x13\n\x11destination_model"q\n\x1aCopyModelOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"g\n\x11CopyModelResponse\x123\n\x05model\x18\x01 \x01(\tB$\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x1d\n\x10model_version_id\x18\x02 \x01(\tB\x03\xe0A\x03"\xa8\x01\n\x1cImportModelEvaluationRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12O\n\x10model_evaluation\x18\x02 \x01(\x0b20.google.cloud.aiplatform.v1beta1.ModelEvaluationB\x03\xe0A\x02"\xc9\x01\n\'BatchImportModelEvaluationSlicesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ModelEvaluation\x12[\n\x17model_evaluation_slices\x18\x02 \x03(\x0b25.google.cloud.aiplatform.v1beta1.ModelEvaluationSliceB\x03\xe0A\x02"Y\n(BatchImportModelEvaluationSlicesResponse\x12-\n imported_model_evaluation_slices\x18\x01 \x03(\tB\x03\xe0A\x03"\xca\x01\n&BatchImportEvaluatedAnnotationsRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.aiplatform.googleapis.com/ModelEvaluationSlice\x12X\n\x15evaluated_annotations\x18\x02 \x03(\x0b24.google.cloud.aiplatform.v1beta1.EvaluatedAnnotationB\x03\xe0A\x02"\\\n\'BatchImportEvaluatedAnnotationsResponse\x121\n$imported_evaluated_annotations_count\x18\x01 \x01(\x05B\x03\xe0A\x03"\\\n\x19GetModelEvaluationRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ModelEvaluation"\xbc\x01\n\x1bListModelEvaluationsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x84\x01\n\x1cListModelEvaluationsResponse\x12K\n\x11model_evaluations\x18\x01 \x03(\x0b20.google.cloud.aiplatform.v1beta1.ModelEvaluation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"f\n\x1eGetModelEvaluationSliceRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.aiplatform.googleapis.com/ModelEvaluationSlice"\xcb\x01\n ListModelEvaluationSlicesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ModelEvaluation\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x94\x01\n!ListModelEvaluationSlicesResponse\x12V\n\x17model_evaluation_slices\x18\x01 \x03(\x0b25.google.cloud.aiplatform.v1beta1.ModelEvaluationSlice\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xaf\x01\n\x14RecommendSpecRequest\x129\n\x06parent\x18\x02 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x14\n\x07gcs_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\'\n\x1acheck_machine_availability\x18\x03 \x01(\x08B\x03\xe0A\x01\x12\x1d\n\x10check_user_quota\x18\x04 \x01(\x08B\x03\xe0A\x01"\xa0\x06\n\x15RecommendSpecResponse\x12\x17\n\nbase_model\x18\x01 \x01(\tB\x03\xe0A\x03\x12c\n\x0frecommendations\x18\x03 \x03(\x0b2E.google.cloud.aiplatform.v1beta1.RecommendSpecResponse.RecommendationB\x03\xe0A\x03\x12g\n\x05specs\x18\x02 \x03(\x0b2S.google.cloud.aiplatform.v1beta1.RecommendSpecResponse.MachineAndModelContainerSpecB\x03\xe0A\x03\x1a\xb9\x01\n\x1cMachineAndModelContainerSpec\x12G\n\x0cmachine_spec\x18\x01 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.MachineSpecB\x03\xe0A\x03\x12P\n\x0econtainer_spec\x18\x02 \x01(\x0b23.google.cloud.aiplatform.v1beta1.ModelContainerSpecB\x03\xe0A\x03\x1a\xe3\x02\n\x0eRecommendation\x12\x0e\n\x06region\x18\x01 \x01(\t\x12f\n\x04spec\x18\x02 \x01(\x0b2S.google.cloud.aiplatform.v1beta1.RecommendSpecResponse.MachineAndModelContainerSpecB\x03\xe0A\x03\x12o\n\x10user_quota_state\x18\x03 \x01(\x0e2P.google.cloud.aiplatform.v1beta1.RecommendSpecResponse.Recommendation.QuotaStateB\x03\xe0A\x03"h\n\nQuotaState\x12\x1b\n\x17QUOTA_STATE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aQUOTA_STATE_USER_HAS_QUOTA\x10\x01\x12\x1d\n\x19QUOTA_STATE_NO_USER_QUOTA\x10\x022\xcc%\n\x0cModelService\x12\xea\x01\n\x0bUploadModel\x123.google.cloud.aiplatform.v1beta1.UploadModelRequest\x1a\x1d.google.longrunning.Operation"\x86\x01\xcaA3\n\x13UploadModelResponse\x12\x1cUploadModelOperationMetadata\xdaA\x0cparent,model\x82\xd3\xe4\x93\x02;"6/v1beta1/{parent=projects/*/locations/*}/models:upload:\x01*\x12\xa4\x01\n\x08GetModel\x120.google.cloud.aiplatform.v1beta1.GetModelRequest\x1a&.google.cloud.aiplatform.v1beta1.Model">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1beta1/{name=projects/*/locations/*/models/*}\x12\xb7\x01\n\nListModels\x122.google.cloud.aiplatform.v1beta1.ListModelsRequest\x1a3.google.cloud.aiplatform.v1beta1.ListModelsResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1beta1/{parent=projects/*/locations/*}/models\x12\xd7\x01\n\x11ListModelVersions\x129.google.cloud.aiplatform.v1beta1.ListModelVersionsRequest\x1a:.google.cloud.aiplatform.v1beta1.ListModelVersionsResponse"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1beta1/{name=projects/*/locations/*/models/*}:listVersions\x12\xf8\x01\n\x1bListModelVersionCheckpoints\x12C.google.cloud.aiplatform.v1beta1.ListModelVersionCheckpointsRequest\x1aD.google.cloud.aiplatform.v1beta1.ListModelVersionCheckpointsResponse"N\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/v1beta1/{name=projects/*/locations/*/models/*}:listCheckpoints\x12\xc4\x01\n\x0bUpdateModel\x123.google.cloud.aiplatform.v1beta1.UpdateModelRequest\x1a&.google.cloud.aiplatform.v1beta1.Model"X\xdaA\x11model,update_mask\x82\xd3\xe4\x93\x02>25/v1beta1/{model.name=projects/*/locations/*/models/*}:\x05model\x12\xaa\x02\n\x18UpdateExplanationDataset\x12@.google.cloud.aiplatform.v1beta1.UpdateExplanationDatasetRequest\x1a\x1d.google.longrunning.Operation"\xac\x01\xcaAM\n UpdateExplanationDatasetResponse\x12)UpdateExplanationDatasetOperationMetadata\xdaA\x05model\x82\xd3\xe4\x93\x02N"I/v1beta1/{model=projects/*/locations/*/models/*}:updateExplanationDataset:\x01*\x12\xd4\x01\n\x0bDeleteModel\x123.google.cloud.aiplatform.v1beta1.DeleteModelRequest\x1a\x1d.google.longrunning.Operation"q\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1beta1/{name=projects/*/locations/*/models/*}\x12\xf0\x01\n\x12DeleteModelVersion\x12:.google.cloud.aiplatform.v1beta1.DeleteModelVersionRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02?*=/v1beta1/{name=projects/*/locations/*/models/*}:deleteVersion\x12\xe1\x01\n\x13MergeVersionAliases\x12;.google.cloud.aiplatform.v1beta1.MergeVersionAliasesRequest\x1a&.google.cloud.aiplatform.v1beta1.Model"e\xdaA\x14name,version_aliases\x82\xd3\xe4\x93\x02H"C/v1beta1/{name=projects/*/locations/*/models/*}:mergeVersionAliases:\x01*\x12\xf0\x01\n\x0bExportModel\x123.google.cloud.aiplatform.v1beta1.ExportModelRequest\x1a\x1d.google.longrunning.Operation"\x8c\x01\xcaA3\n\x13ExportModelResponse\x12\x1cExportModelOperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x02;"6/v1beta1/{name=projects/*/locations/*/models/*}:export:\x01*\x12\xe7\x01\n\tCopyModel\x121.google.cloud.aiplatform.v1beta1.CopyModelRequest\x1a\x1d.google.longrunning.Operation"\x87\x01\xcaA/\n\x11CopyModelResponse\x12\x1aCopyModelOperationMetadata\xdaA\x13parent,source_model\x82\xd3\xe4\x93\x029"4/v1beta1/{parent=projects/*/locations/*}/models:copy:\x01*\x12\xf3\x01\n\x15ImportModelEvaluation\x12=.google.cloud.aiplatform.v1beta1.ImportModelEvaluationRequest\x1a0.google.cloud.aiplatform.v1beta1.ModelEvaluation"i\xdaA\x17parent,model_evaluation\x82\xd3\xe4\x93\x02I"D/v1beta1/{parent=projects/*/locations/*/models/*}/evaluations:import:\x01*\x12\xb7\x02\n BatchImportModelEvaluationSlices\x12H.google.cloud.aiplatform.v1beta1.BatchImportModelEvaluationSlicesRequest\x1aI.google.cloud.aiplatform.v1beta1.BatchImportModelEvaluationSlicesResponse"~\xdaA\x1eparent,model_evaluation_slices\x82\xd3\xe4\x93\x02W"R/v1beta1/{parent=projects/*/locations/*/models/*/evaluations/*}/slices:batchImport:\x01*\x12\xb4\x02\n\x1fBatchImportEvaluatedAnnotations\x12G.google.cloud.aiplatform.v1beta1.BatchImportEvaluatedAnnotationsRequest\x1aH.google.cloud.aiplatform.v1beta1.BatchImportEvaluatedAnnotationsResponse"~\xdaA\x1cparent,evaluated_annotations\x82\xd3\xe4\x93\x02Y"T/v1beta1/{parent=projects/*/locations/*/models/*/evaluations/*/slices/*}:batchImport:\x01*\x12\xd0\x01\n\x12GetModelEvaluation\x12:.google.cloud.aiplatform.v1beta1.GetModelEvaluationRequest\x1a0.google.cloud.aiplatform.v1beta1.ModelEvaluation"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*}\x12\xe3\x01\n\x14ListModelEvaluations\x12<.google.cloud.aiplatform.v1beta1.ListModelEvaluationsRequest\x1a=.google.cloud.aiplatform.v1beta1.ListModelEvaluationsResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1beta1/{parent=projects/*/locations/*/models/*}/evaluations\x12\xe8\x01\n\x17GetModelEvaluationSlice\x12?.google.cloud.aiplatform.v1beta1.GetModelEvaluationSliceRequest\x1a5.google.cloud.aiplatform.v1beta1.ModelEvaluationSlice"U\xdaA\x04name\x82\xd3\xe4\x93\x02H\x12F/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/slices/*}\x12\xfb\x01\n\x19ListModelEvaluationSlices\x12A.google.cloud.aiplatform.v1beta1.ListModelEvaluationSlicesRequest\x1aB.google.cloud.aiplatform.v1beta1.ListModelEvaluationSlicesResponse"W\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v1beta1/{parent=projects/*/locations/*/models/*/evaluations/*}/slices\x12\xc1\x01\n\rRecommendSpec\x125.google.cloud.aiplatform.v1beta1.RecommendSpecRequest\x1a6.google.cloud.aiplatform.v1beta1.RecommendSpecResponse"A\x82\xd3\xe4\x93\x02;"6/v1beta1/{parent=projects/*/locations/*}:recommendSpec:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe8\x01\n#com.google.cloud.aiplatform.v1beta1B\x11ModelServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.model_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x11ModelServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
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
    _globals['_RECOMMENDSPECREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RECOMMENDSPECREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_RECOMMENDSPECREQUEST'].fields_by_name['gcs_uri']._loaded_options = None
    _globals['_RECOMMENDSPECREQUEST'].fields_by_name['gcs_uri']._serialized_options = b'\xe0A\x02'
    _globals['_RECOMMENDSPECREQUEST'].fields_by_name['check_machine_availability']._loaded_options = None
    _globals['_RECOMMENDSPECREQUEST'].fields_by_name['check_machine_availability']._serialized_options = b'\xe0A\x01'
    _globals['_RECOMMENDSPECREQUEST'].fields_by_name['check_user_quota']._loaded_options = None
    _globals['_RECOMMENDSPECREQUEST'].fields_by_name['check_user_quota']._serialized_options = b'\xe0A\x01'
    _globals['_RECOMMENDSPECRESPONSE_MACHINEANDMODELCONTAINERSPEC'].fields_by_name['machine_spec']._loaded_options = None
    _globals['_RECOMMENDSPECRESPONSE_MACHINEANDMODELCONTAINERSPEC'].fields_by_name['machine_spec']._serialized_options = b'\xe0A\x03'
    _globals['_RECOMMENDSPECRESPONSE_MACHINEANDMODELCONTAINERSPEC'].fields_by_name['container_spec']._loaded_options = None
    _globals['_RECOMMENDSPECRESPONSE_MACHINEANDMODELCONTAINERSPEC'].fields_by_name['container_spec']._serialized_options = b'\xe0A\x03'
    _globals['_RECOMMENDSPECRESPONSE_RECOMMENDATION'].fields_by_name['spec']._loaded_options = None
    _globals['_RECOMMENDSPECRESPONSE_RECOMMENDATION'].fields_by_name['spec']._serialized_options = b'\xe0A\x03'
    _globals['_RECOMMENDSPECRESPONSE_RECOMMENDATION'].fields_by_name['user_quota_state']._loaded_options = None
    _globals['_RECOMMENDSPECRESPONSE_RECOMMENDATION'].fields_by_name['user_quota_state']._serialized_options = b'\xe0A\x03'
    _globals['_RECOMMENDSPECRESPONSE'].fields_by_name['base_model']._loaded_options = None
    _globals['_RECOMMENDSPECRESPONSE'].fields_by_name['base_model']._serialized_options = b'\xe0A\x03'
    _globals['_RECOMMENDSPECRESPONSE'].fields_by_name['recommendations']._loaded_options = None
    _globals['_RECOMMENDSPECRESPONSE'].fields_by_name['recommendations']._serialized_options = b'\xe0A\x03'
    _globals['_RECOMMENDSPECRESPONSE'].fields_by_name['specs']._loaded_options = None
    _globals['_RECOMMENDSPECRESPONSE'].fields_by_name['specs']._serialized_options = b'\xe0A\x03'
    _globals['_MODELSERVICE']._loaded_options = None
    _globals['_MODELSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MODELSERVICE'].methods_by_name['UploadModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['UploadModel']._serialized_options = b'\xcaA3\n\x13UploadModelResponse\x12\x1cUploadModelOperationMetadata\xdaA\x0cparent,model\x82\xd3\xe4\x93\x02;"6/v1beta1/{parent=projects/*/locations/*}/models:upload:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1beta1/{name=projects/*/locations/*/models/*}'
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1beta1/{parent=projects/*/locations/*}/models'
    _globals['_MODELSERVICE'].methods_by_name['ListModelVersions']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModelVersions']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1beta1/{name=projects/*/locations/*/models/*}:listVersions'
    _globals['_MODELSERVICE'].methods_by_name['ListModelVersionCheckpoints']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModelVersionCheckpoints']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/v1beta1/{name=projects/*/locations/*/models/*}:listCheckpoints'
    _globals['_MODELSERVICE'].methods_by_name['UpdateModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['UpdateModel']._serialized_options = b'\xdaA\x11model,update_mask\x82\xd3\xe4\x93\x02>25/v1beta1/{model.name=projects/*/locations/*/models/*}:\x05model'
    _globals['_MODELSERVICE'].methods_by_name['UpdateExplanationDataset']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['UpdateExplanationDataset']._serialized_options = b'\xcaAM\n UpdateExplanationDatasetResponse\x12)UpdateExplanationDatasetOperationMetadata\xdaA\x05model\x82\xd3\xe4\x93\x02N"I/v1beta1/{model=projects/*/locations/*/models/*}:updateExplanationDataset:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['DeleteModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['DeleteModel']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1beta1/{name=projects/*/locations/*/models/*}'
    _globals['_MODELSERVICE'].methods_by_name['DeleteModelVersion']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['DeleteModelVersion']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02?*=/v1beta1/{name=projects/*/locations/*/models/*}:deleteVersion'
    _globals['_MODELSERVICE'].methods_by_name['MergeVersionAliases']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['MergeVersionAliases']._serialized_options = b'\xdaA\x14name,version_aliases\x82\xd3\xe4\x93\x02H"C/v1beta1/{name=projects/*/locations/*/models/*}:mergeVersionAliases:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['ExportModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ExportModel']._serialized_options = b'\xcaA3\n\x13ExportModelResponse\x12\x1cExportModelOperationMetadata\xdaA\x12name,output_config\x82\xd3\xe4\x93\x02;"6/v1beta1/{name=projects/*/locations/*/models/*}:export:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['CopyModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['CopyModel']._serialized_options = b'\xcaA/\n\x11CopyModelResponse\x12\x1aCopyModelOperationMetadata\xdaA\x13parent,source_model\x82\xd3\xe4\x93\x029"4/v1beta1/{parent=projects/*/locations/*}/models:copy:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['ImportModelEvaluation']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ImportModelEvaluation']._serialized_options = b'\xdaA\x17parent,model_evaluation\x82\xd3\xe4\x93\x02I"D/v1beta1/{parent=projects/*/locations/*/models/*}/evaluations:import:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['BatchImportModelEvaluationSlices']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['BatchImportModelEvaluationSlices']._serialized_options = b'\xdaA\x1eparent,model_evaluation_slices\x82\xd3\xe4\x93\x02W"R/v1beta1/{parent=projects/*/locations/*/models/*/evaluations/*}/slices:batchImport:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['BatchImportEvaluatedAnnotations']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['BatchImportEvaluatedAnnotations']._serialized_options = b'\xdaA\x1cparent,evaluated_annotations\x82\xd3\xe4\x93\x02Y"T/v1beta1/{parent=projects/*/locations/*/models/*/evaluations/*/slices/*}:batchImport:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['GetModelEvaluation']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['GetModelEvaluation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*}'
    _globals['_MODELSERVICE'].methods_by_name['ListModelEvaluations']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModelEvaluations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1beta1/{parent=projects/*/locations/*/models/*}/evaluations'
    _globals['_MODELSERVICE'].methods_by_name['GetModelEvaluationSlice']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['GetModelEvaluationSlice']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02H\x12F/v1beta1/{name=projects/*/locations/*/models/*/evaluations/*/slices/*}'
    _globals['_MODELSERVICE'].methods_by_name['ListModelEvaluationSlices']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModelEvaluationSlices']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v1beta1/{parent=projects/*/locations/*/models/*/evaluations/*}/slices'
    _globals['_MODELSERVICE'].methods_by_name['RecommendSpec']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['RecommendSpec']._serialized_options = b'\x82\xd3\xe4\x93\x02;"6/v1beta1/{parent=projects/*/locations/*}:recommendSpec:\x01*'
    _globals['_UPLOADMODELREQUEST']._serialized_start = 781
    _globals['_UPLOADMODELREQUEST']._serialized_end = 1000
    _globals['_UPLOADMODELOPERATIONMETADATA']._serialized_start = 1002
    _globals['_UPLOADMODELOPERATIONMETADATA']._serialized_end = 1117
    _globals['_UPLOADMODELRESPONSE']._serialized_start = 1119
    _globals['_UPLOADMODELRESPONSE']._serialized_end = 1224
    _globals['_GETMODELREQUEST']._serialized_start = 1226
    _globals['_GETMODELREQUEST']._serialized_end = 1298
    _globals['_LISTMODELSREQUEST']._serialized_start = 1301
    _globals['_LISTMODELSREQUEST']._serialized_end = 1481
    _globals['_LISTMODELSRESPONSE']._serialized_start = 1483
    _globals['_LISTMODELSRESPONSE']._serialized_end = 1584
    _globals['_LISTMODELVERSIONSREQUEST']._serialized_start = 1587
    _globals['_LISTMODELVERSIONSREQUEST']._serialized_end = 1788
    _globals['_LISTMODELVERSIONSRESPONSE']._serialized_start = 1790
    _globals['_LISTMODELVERSIONSRESPONSE']._serialized_end = 1898
    _globals['_LISTMODELVERSIONCHECKPOINTSREQUEST']._serialized_start = 1901
    _globals['_LISTMODELVERSIONCHECKPOINTSREQUEST']._serialized_end = 2041
    _globals['_MODELVERSIONCHECKPOINT']._serialized_start = 2043
    _globals['_MODELVERSIONCHECKPOINT']._serialized_end = 2119
    _globals['_LISTMODELVERSIONCHECKPOINTSRESPONSE']._serialized_start = 2122
    _globals['_LISTMODELVERSIONCHECKPOINTSRESPONSE']._serialized_end = 2262
    _globals['_UPDATEMODELREQUEST']._serialized_start = 2265
    _globals['_UPDATEMODELREQUEST']._serialized_end = 2399
    _globals['_UPDATEEXPLANATIONDATASETREQUEST']._serialized_start = 2402
    _globals['_UPDATEEXPLANATIONDATASETREQUEST']._serialized_end = 2552
    _globals['_UPDATEEXPLANATIONDATASETOPERATIONMETADATA']._serialized_start = 2555
    _globals['_UPDATEEXPLANATIONDATASETOPERATIONMETADATA']._serialized_end = 2683
    _globals['_DELETEMODELREQUEST']._serialized_start = 2685
    _globals['_DELETEMODELREQUEST']._serialized_end = 2760
    _globals['_DELETEMODELVERSIONREQUEST']._serialized_start = 2762
    _globals['_DELETEMODELVERSIONREQUEST']._serialized_end = 2844
    _globals['_MERGEVERSIONALIASESREQUEST']._serialized_start = 2846
    _globals['_MERGEVERSIONALIASESREQUEST']._serialized_end = 2959
    _globals['_EXPORTMODELREQUEST']._serialized_start = 2962
    _globals['_EXPORTMODELREQUEST']._serialized_end = 3343
    _globals['_EXPORTMODELREQUEST_OUTPUTCONFIG']._serialized_start = 3134
    _globals['_EXPORTMODELREQUEST_OUTPUTCONFIG']._serialized_end = 3343
    _globals['_EXPORTMODELOPERATIONMETADATA']._serialized_start = 3346
    _globals['_EXPORTMODELOPERATIONMETADATA']._serialized_end = 3640
    _globals['_EXPORTMODELOPERATIONMETADATA_OUTPUTINFO']._serialized_start = 3563
    _globals['_EXPORTMODELOPERATIONMETADATA_OUTPUTINFO']._serialized_end = 3640
    _globals['_UPDATEEXPLANATIONDATASETRESPONSE']._serialized_start = 3642
    _globals['_UPDATEEXPLANATIONDATASETRESPONSE']._serialized_end = 3676
    _globals['_EXPORTMODELRESPONSE']._serialized_start = 3678
    _globals['_EXPORTMODELRESPONSE']._serialized_end = 3699
    _globals['_COPYMODELREQUEST']._serialized_start = 3702
    _globals['_COPYMODELREQUEST']._serialized_end = 4027
    _globals['_COPYMODELOPERATIONMETADATA']._serialized_start = 4029
    _globals['_COPYMODELOPERATIONMETADATA']._serialized_end = 4142
    _globals['_COPYMODELRESPONSE']._serialized_start = 4144
    _globals['_COPYMODELRESPONSE']._serialized_end = 4247
    _globals['_IMPORTMODELEVALUATIONREQUEST']._serialized_start = 4250
    _globals['_IMPORTMODELEVALUATIONREQUEST']._serialized_end = 4418
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESREQUEST']._serialized_start = 4421
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESREQUEST']._serialized_end = 4622
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESRESPONSE']._serialized_start = 4624
    _globals['_BATCHIMPORTMODELEVALUATIONSLICESRESPONSE']._serialized_end = 4713
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSREQUEST']._serialized_start = 4716
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSREQUEST']._serialized_end = 4918
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSRESPONSE']._serialized_start = 4920
    _globals['_BATCHIMPORTEVALUATEDANNOTATIONSRESPONSE']._serialized_end = 5012
    _globals['_GETMODELEVALUATIONREQUEST']._serialized_start = 5014
    _globals['_GETMODELEVALUATIONREQUEST']._serialized_end = 5106
    _globals['_LISTMODELEVALUATIONSREQUEST']._serialized_start = 5109
    _globals['_LISTMODELEVALUATIONSREQUEST']._serialized_end = 5297
    _globals['_LISTMODELEVALUATIONSRESPONSE']._serialized_start = 5300
    _globals['_LISTMODELEVALUATIONSRESPONSE']._serialized_end = 5432
    _globals['_GETMODELEVALUATIONSLICEREQUEST']._serialized_start = 5434
    _globals['_GETMODELEVALUATIONSLICEREQUEST']._serialized_end = 5536
    _globals['_LISTMODELEVALUATIONSLICESREQUEST']._serialized_start = 5539
    _globals['_LISTMODELEVALUATIONSLICESREQUEST']._serialized_end = 5742
    _globals['_LISTMODELEVALUATIONSLICESRESPONSE']._serialized_start = 5745
    _globals['_LISTMODELEVALUATIONSLICESRESPONSE']._serialized_end = 5893
    _globals['_RECOMMENDSPECREQUEST']._serialized_start = 5896
    _globals['_RECOMMENDSPECREQUEST']._serialized_end = 6071
    _globals['_RECOMMENDSPECRESPONSE']._serialized_start = 6074
    _globals['_RECOMMENDSPECRESPONSE']._serialized_end = 6874
    _globals['_RECOMMENDSPECRESPONSE_MACHINEANDMODELCONTAINERSPEC']._serialized_start = 6331
    _globals['_RECOMMENDSPECRESPONSE_MACHINEANDMODELCONTAINERSPEC']._serialized_end = 6516
    _globals['_RECOMMENDSPECRESPONSE_RECOMMENDATION']._serialized_start = 6519
    _globals['_RECOMMENDSPECRESPONSE_RECOMMENDATION']._serialized_end = 6874
    _globals['_RECOMMENDSPECRESPONSE_RECOMMENDATION_QUOTASTATE']._serialized_start = 6770
    _globals['_RECOMMENDSPECRESPONSE_RECOMMENDATION_QUOTASTATE']._serialized_end = 6874
    _globals['_MODELSERVICE']._serialized_start = 6877
    _globals['_MODELSERVICE']._serialized_end = 11689