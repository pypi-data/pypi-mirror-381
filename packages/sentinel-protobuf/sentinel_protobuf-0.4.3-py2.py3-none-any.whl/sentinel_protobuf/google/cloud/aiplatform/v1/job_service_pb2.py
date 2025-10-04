"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/job_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import batch_prediction_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_batch__prediction__job__pb2
from .....google.cloud.aiplatform.v1 import custom_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_custom__job__pb2
from .....google.cloud.aiplatform.v1 import data_labeling_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_data__labeling__job__pb2
from .....google.cloud.aiplatform.v1 import hyperparameter_tuning_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_hyperparameter__tuning__job__pb2
from .....google.cloud.aiplatform.v1 import model_deployment_monitoring_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_model__deployment__monitoring__job__pb2
from .....google.cloud.aiplatform.v1 import nas_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_nas__job__pb2
from .....google.cloud.aiplatform.v1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/aiplatform/v1/job_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1/batch_prediction_job.proto\x1a+google/cloud/aiplatform/v1/custom_job.proto\x1a2google/cloud/aiplatform/v1/data_labeling_job.proto\x1a:google/cloud/aiplatform/v1/hyperparameter_tuning_job.proto\x1a@google/cloud/aiplatform/v1/model_deployment_monitoring_job.proto\x1a(google/cloud/aiplatform/v1/nas_job.proto\x1a*google/cloud/aiplatform/v1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x93\x01\n\x16CreateCustomJobRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12>\n\ncustom_job\x18\x02 \x01(\x0b2%.google.cloud.aiplatform.v1.CustomJobB\x03\xe0A\x02"P\n\x13GetCustomJobRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/CustomJob"\xb8\x01\n\x15ListCustomJobsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"m\n\x16ListCustomJobsResponse\x12:\n\x0bcustom_jobs\x18\x01 \x03(\x0b2%.google.cloud.aiplatform.v1.CustomJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"S\n\x16DeleteCustomJobRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/CustomJob"S\n\x16CancelCustomJobRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/CustomJob"\xa6\x01\n\x1cCreateDataLabelingJobRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12K\n\x11data_labeling_job\x18\x02 \x01(\x0b2+.google.cloud.aiplatform.v1.DataLabelingJobB\x03\xe0A\x02"\\\n\x19GetDataLabelingJobRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/DataLabelingJob"\xd0\x01\n\x1bListDataLabelingJobsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x10\n\x08order_by\x18\x06 \x01(\t"\x80\x01\n\x1cListDataLabelingJobsResponse\x12G\n\x12data_labeling_jobs\x18\x01 \x03(\x0b2+.google.cloud.aiplatform.v1.DataLabelingJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"_\n\x1cDeleteDataLabelingJobRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/DataLabelingJob"_\n\x1cCancelDataLabelingJobRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/DataLabelingJob"\xbe\x01\n$CreateHyperparameterTuningJobRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12[\n\x19hyperparameter_tuning_job\x18\x02 \x01(\x0b23.google.cloud.aiplatform.v1.HyperparameterTuningJobB\x03\xe0A\x02"l\n!GetHyperparameterTuningJobRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1aiplatform.googleapis.com/HyperparameterTuningJob"\xc6\x01\n#ListHyperparameterTuningJobsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x98\x01\n$ListHyperparameterTuningJobsResponse\x12W\n\x1ahyperparameter_tuning_jobs\x18\x01 \x03(\x0b23.google.cloud.aiplatform.v1.HyperparameterTuningJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"o\n$DeleteHyperparameterTuningJobRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1aiplatform.googleapis.com/HyperparameterTuningJob"o\n$CancelHyperparameterTuningJobRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1aiplatform.googleapis.com/HyperparameterTuningJob"\x8a\x01\n\x13CreateNasJobRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x128\n\x07nas_job\x18\x02 \x01(\x0b2".google.cloud.aiplatform.v1.NasJobB\x03\xe0A\x02"J\n\x10GetNasJobRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n aiplatform.googleapis.com/NasJob"\xb5\x01\n\x12ListNasJobsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"d\n\x13ListNasJobsResponse\x124\n\x08nas_jobs\x18\x01 \x03(\x0b2".google.cloud.aiplatform.v1.NasJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"M\n\x13DeleteNasJobRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n aiplatform.googleapis.com/NasJob"M\n\x13CancelNasJobRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n aiplatform.googleapis.com/NasJob"Z\n\x18GetNasTrialDetailRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/NasTrialDetail"}\n\x1aListNasTrialDetailsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n aiplatform.googleapis.com/NasJob\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"}\n\x1bListNasTrialDetailsResponse\x12E\n\x11nas_trial_details\x18\x01 \x03(\x0b2*.google.cloud.aiplatform.v1.NasTrialDetail\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xaf\x01\n\x1fCreateBatchPredictionJobRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12Q\n\x14batch_prediction_job\x18\x02 \x01(\x0b2..google.cloud.aiplatform.v1.BatchPredictionJobB\x03\xe0A\x02"b\n\x1cGetBatchPredictionJobRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/BatchPredictionJob"\xc1\x01\n\x1eListBatchPredictionJobsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x89\x01\n\x1fListBatchPredictionJobsResponse\x12M\n\x15batch_prediction_jobs\x18\x01 \x03(\x0b2..google.cloud.aiplatform.v1.BatchPredictionJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"e\n\x1fDeleteBatchPredictionJobRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/BatchPredictionJob"e\n\x1fCancelBatchPredictionJobRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/BatchPredictionJob"\xce\x01\n)CreateModelDeploymentMonitoringJobRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12f\n\x1fmodel_deployment_monitoring_job\x18\x02 \x01(\x0b28.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJobB\x03\xe0A\x02"\xef\x04\n4SearchModelDeploymentMonitoringStatsAnomaliesRequest\x12g\n\x1fmodel_deployment_monitoring_job\x18\x01 \x01(\tB>\xe0A\x02\xfaA8\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob\x12\x1e\n\x11deployed_model_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x14feature_display_name\x18\x03 \x01(\t\x12\x81\x01\n\nobjectives\x18\x04 \x03(\x0b2h.google.cloud.aiplatform.v1.SearchModelDeploymentMonitoringStatsAnomaliesRequest.StatsAnomaliesObjectiveB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\x12.\n\nstart_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x86\x01\n\x17StatsAnomaliesObjective\x12P\n\x04type\x18\x01 \x01(\x0e2B.google.cloud.aiplatform.v1.ModelDeploymentMonitoringObjectiveType\x12\x19\n\x11top_feature_count\x18\x04 \x01(\x05"\xa5\x01\n5SearchModelDeploymentMonitoringStatsAnomaliesResponse\x12S\n\x10monitoring_stats\x18\x01 \x03(\x0b29.google.cloud.aiplatform.v1.ModelMonitoringStatsAnomalies\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"v\n&GetModelDeploymentMonitoringJobRequest\x12L\n\x04name\x18\x01 \x01(\tB>\xe0A\x02\xfaA8\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob"\xcb\x01\n(ListModelDeploymentMonitoringJobsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xa8\x01\n)ListModelDeploymentMonitoringJobsResponse\x12b\n model_deployment_monitoring_jobs\x18\x01 \x03(\x0b28.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc9\x01\n)UpdateModelDeploymentMonitoringJobRequest\x12f\n\x1fmodel_deployment_monitoring_job\x18\x01 \x01(\x0b28.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJobB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"y\n)DeleteModelDeploymentMonitoringJobRequest\x12L\n\x04name\x18\x01 \x01(\tB>\xe0A\x02\xfaA8\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob"x\n(PauseModelDeploymentMonitoringJobRequest\x12L\n\x04name\x18\x01 \x01(\tB>\xe0A\x02\xfaA8\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob"y\n)ResumeModelDeploymentMonitoringJobRequest\x12L\n\x04name\x18\x01 \x01(\tB>\xe0A\x02\xfaA8\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob"\x85\x01\n3UpdateModelDeploymentMonitoringJobOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata2\xf0?\n\nJobService\x12\xc4\x01\n\x0fCreateCustomJob\x122.google.cloud.aiplatform.v1.CreateCustomJobRequest\x1a%.google.cloud.aiplatform.v1.CustomJob"V\xdaA\x11parent,custom_job\x82\xd3\xe4\x93\x02<"./v1/{parent=projects/*/locations/*}/customJobs:\ncustom_job\x12\xa5\x01\n\x0cGetCustomJob\x12/.google.cloud.aiplatform.v1.GetCustomJobRequest\x1a%.google.cloud.aiplatform.v1.CustomJob"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/customJobs/*}\x12\xb8\x01\n\x0eListCustomJobs\x121.google.cloud.aiplatform.v1.ListCustomJobsRequest\x1a2.google.cloud.aiplatform.v1.ListCustomJobsResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/customJobs\x12\xd6\x01\n\x0fDeleteCustomJob\x122.google.cloud.aiplatform.v1.DeleteCustomJobRequest\x1a\x1d.google.longrunning.Operation"p\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/customJobs/*}\x12\xa6\x01\n\x0fCancelCustomJob\x122.google.cloud.aiplatform.v1.CancelCustomJobRequest\x1a\x16.google.protobuf.Empty"G\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/locations/*/customJobs/*}:cancel:\x01*\x12\xea\x01\n\x15CreateDataLabelingJob\x128.google.cloud.aiplatform.v1.CreateDataLabelingJobRequest\x1a+.google.cloud.aiplatform.v1.DataLabelingJob"j\xdaA\x18parent,data_labeling_job\x82\xd3\xe4\x93\x02I"4/v1/{parent=projects/*/locations/*}/dataLabelingJobs:\x11data_labeling_job\x12\xbd\x01\n\x12GetDataLabelingJob\x125.google.cloud.aiplatform.v1.GetDataLabelingJobRequest\x1a+.google.cloud.aiplatform.v1.DataLabelingJob"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/dataLabelingJobs/*}\x12\xd0\x01\n\x14ListDataLabelingJobs\x127.google.cloud.aiplatform.v1.ListDataLabelingJobsRequest\x1a8.google.cloud.aiplatform.v1.ListDataLabelingJobsResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*}/dataLabelingJobs\x12\xe8\x01\n\x15DeleteDataLabelingJob\x128.google.cloud.aiplatform.v1.DeleteDataLabelingJobRequest\x1a\x1d.google.longrunning.Operation"v\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1/{name=projects/*/locations/*/dataLabelingJobs/*}\x12\xb8\x01\n\x15CancelDataLabelingJob\x128.google.cloud.aiplatform.v1.CancelDataLabelingJobRequest\x1a\x16.google.protobuf.Empty"M\xdaA\x04name\x82\xd3\xe4\x93\x02@";/v1/{name=projects/*/locations/*/dataLabelingJobs/*}:cancel:\x01*\x12\x9b\x02\n\x1dCreateHyperparameterTuningJob\x12@.google.cloud.aiplatform.v1.CreateHyperparameterTuningJobRequest\x1a3.google.cloud.aiplatform.v1.HyperparameterTuningJob"\x82\x01\xdaA parent,hyperparameter_tuning_job\x82\xd3\xe4\x93\x02Y"</v1/{parent=projects/*/locations/*}/hyperparameterTuningJobs:\x19hyperparameter_tuning_job\x12\xdd\x01\n\x1aGetHyperparameterTuningJob\x12=.google.cloud.aiplatform.v1.GetHyperparameterTuningJobRequest\x1a3.google.cloud.aiplatform.v1.HyperparameterTuningJob"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1/{name=projects/*/locations/*/hyperparameterTuningJobs/*}\x12\xf0\x01\n\x1cListHyperparameterTuningJobs\x12?.google.cloud.aiplatform.v1.ListHyperparameterTuningJobsRequest\x1a@.google.cloud.aiplatform.v1.ListHyperparameterTuningJobsResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1/{parent=projects/*/locations/*}/hyperparameterTuningJobs\x12\x80\x02\n\x1dDeleteHyperparameterTuningJob\x12@.google.cloud.aiplatform.v1.DeleteHyperparameterTuningJobRequest\x1a\x1d.google.longrunning.Operation"~\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1/{name=projects/*/locations/*/hyperparameterTuningJobs/*}\x12\xd0\x01\n\x1dCancelHyperparameterTuningJob\x12@.google.cloud.aiplatform.v1.CancelHyperparameterTuningJobRequest\x1a\x16.google.protobuf.Empty"U\xdaA\x04name\x82\xd3\xe4\x93\x02H"C/v1/{name=projects/*/locations/*/hyperparameterTuningJobs/*}:cancel:\x01*\x12\xb2\x01\n\x0cCreateNasJob\x12/.google.cloud.aiplatform.v1.CreateNasJobRequest\x1a".google.cloud.aiplatform.v1.NasJob"M\xdaA\x0eparent,nas_job\x82\xd3\xe4\x93\x026"+/v1/{parent=projects/*/locations/*}/nasJobs:\x07nas_job\x12\x99\x01\n\tGetNasJob\x12,.google.cloud.aiplatform.v1.GetNasJobRequest\x1a".google.cloud.aiplatform.v1.NasJob":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/locations/*/nasJobs/*}\x12\xac\x01\n\x0bListNasJobs\x12..google.cloud.aiplatform.v1.ListNasJobsRequest\x1a/.google.cloud.aiplatform.v1.ListNasJobsResponse"<\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=projects/*/locations/*}/nasJobs\x12\xcd\x01\n\x0cDeleteNasJob\x12/.google.cloud.aiplatform.v1.DeleteNasJobRequest\x1a\x1d.google.longrunning.Operation"m\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02-*+/v1/{name=projects/*/locations/*/nasJobs/*}\x12\x9d\x01\n\x0cCancelNasJob\x12/.google.cloud.aiplatform.v1.CancelNasJobRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/nasJobs/*}:cancel:\x01*\x12\xc3\x01\n\x11GetNasTrialDetail\x124.google.cloud.aiplatform.v1.GetNasTrialDetailRequest\x1a*.google.cloud.aiplatform.v1.NasTrialDetail"L\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/{name=projects/*/locations/*/nasJobs/*/nasTrialDetails/*}\x12\xd6\x01\n\x13ListNasTrialDetails\x126.google.cloud.aiplatform.v1.ListNasTrialDetailsRequest\x1a7.google.cloud.aiplatform.v1.ListNasTrialDetailsResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/locations/*/nasJobs/*}/nasTrialDetails\x12\xfc\x01\n\x18CreateBatchPredictionJob\x12;.google.cloud.aiplatform.v1.CreateBatchPredictionJobRequest\x1a..google.cloud.aiplatform.v1.BatchPredictionJob"s\xdaA\x1bparent,batch_prediction_job\x82\xd3\xe4\x93\x02O"7/v1/{parent=projects/*/locations/*}/batchPredictionJobs:\x14batch_prediction_job\x12\xc9\x01\n\x15GetBatchPredictionJob\x128.google.cloud.aiplatform.v1.GetBatchPredictionJobRequest\x1a..google.cloud.aiplatform.v1.BatchPredictionJob"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/{name=projects/*/locations/*/batchPredictionJobs/*}\x12\xdc\x01\n\x17ListBatchPredictionJobs\x12:.google.cloud.aiplatform.v1.ListBatchPredictionJobsRequest\x1a;.google.cloud.aiplatform.v1.ListBatchPredictionJobsResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1/{parent=projects/*/locations/*}/batchPredictionJobs\x12\xf1\x01\n\x18DeleteBatchPredictionJob\x12;.google.cloud.aiplatform.v1.DeleteBatchPredictionJobRequest\x1a\x1d.google.longrunning.Operation"y\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1/{name=projects/*/locations/*/batchPredictionJobs/*}\x12\xc1\x01\n\x18CancelBatchPredictionJob\x12;.google.cloud.aiplatform.v1.CancelBatchPredictionJobRequest\x1a\x16.google.protobuf.Empty"P\xdaA\x04name\x82\xd3\xe4\x93\x02C">/v1/{name=projects/*/locations/*/batchPredictionJobs/*}:cancel:\x01*\x12\xbb\x02\n"CreateModelDeploymentMonitoringJob\x12E.google.cloud.aiplatform.v1.CreateModelDeploymentMonitoringJobRequest\x1a8.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob"\x93\x01\xdaA&parent,model_deployment_monitoring_job\x82\xd3\xe4\x93\x02d"A/v1/{parent=projects/*/locations/*}/modelDeploymentMonitoringJobs:\x1fmodel_deployment_monitoring_job\x12\xa2\x03\n-SearchModelDeploymentMonitoringStatsAnomalies\x12P.google.cloud.aiplatform.v1.SearchModelDeploymentMonitoringStatsAnomaliesRequest\x1aQ.google.cloud.aiplatform.v1.SearchModelDeploymentMonitoringStatsAnomaliesResponse"\xcb\x01\xdaA1model_deployment_monitoring_job,deployed_model_id\x82\xd3\xe4\x93\x02\x90\x01"\x8a\x01/v1/{model_deployment_monitoring_job=projects/*/locations/*/modelDeploymentMonitoringJobs/*}:searchModelDeploymentMonitoringStatsAnomalies:\x01*\x12\xf1\x01\n\x1fGetModelDeploymentMonitoringJob\x12B.google.cloud.aiplatform.v1.GetModelDeploymentMonitoringJobRequest\x1a8.google.cloud.aiplatform.v1.ModelDeploymentMonitoringJob"P\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}\x12\x84\x02\n!ListModelDeploymentMonitoringJobs\x12D.google.cloud.aiplatform.v1.ListModelDeploymentMonitoringJobsRequest\x1aE.google.cloud.aiplatform.v1.ListModelDeploymentMonitoringJobsResponse"R\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1/{parent=projects/*/locations/*}/modelDeploymentMonitoringJobs\x12\x9c\x03\n"UpdateModelDeploymentMonitoringJob\x12E.google.cloud.aiplatform.v1.UpdateModelDeploymentMonitoringJobRequest\x1a\x1d.google.longrunning.Operation"\x8f\x02\xcaAS\n\x1cModelDeploymentMonitoringJob\x123UpdateModelDeploymentMonitoringJobOperationMetadata\xdaA+model_deployment_monitoring_job,update_mask\x82\xd3\xe4\x93\x02\x84\x012a/v1/{model_deployment_monitoring_job.name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}:\x1fmodel_deployment_monitoring_job\x12\x90\x02\n"DeleteModelDeploymentMonitoringJob\x12E.google.cloud.aiplatform.v1.DeleteModelDeploymentMonitoringJobRequest\x1a\x1d.google.longrunning.Operation"\x83\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02C*A/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}\x12\xdc\x01\n!PauseModelDeploymentMonitoringJob\x12D.google.cloud.aiplatform.v1.PauseModelDeploymentMonitoringJobRequest\x1a\x16.google.protobuf.Empty"Y\xdaA\x04name\x82\xd3\xe4\x93\x02L"G/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}:pause:\x01*\x12\xdf\x01\n"ResumeModelDeploymentMonitoringJob\x12E.google.cloud.aiplatform.v1.ResumeModelDeploymentMonitoringJobRequest\x1a\x16.google.protobuf.Empty"Z\xdaA\x04name\x82\xd3\xe4\x93\x02M"H/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}:resume:\x01*\x1a\x86\x01\xcaA\x19aiplatform.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xcd\x01\n\x1ecom.google.cloud.aiplatform.v1B\x0fJobServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.job_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x0fJobServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_CREATECUSTOMJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECUSTOMJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATECUSTOMJOBREQUEST'].fields_by_name['custom_job']._loaded_options = None
    _globals['_CREATECUSTOMJOBREQUEST'].fields_by_name['custom_job']._serialized_options = b'\xe0A\x02'
    _globals['_GETCUSTOMJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCUSTOMJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/CustomJob'
    _globals['_LISTCUSTOMJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCUSTOMJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETECUSTOMJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECUSTOMJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/CustomJob'
    _globals['_CANCELCUSTOMJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELCUSTOMJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/CustomJob'
    _globals['_CREATEDATALABELINGJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATALABELINGJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEDATALABELINGJOBREQUEST'].fields_by_name['data_labeling_job']._loaded_options = None
    _globals['_CREATEDATALABELINGJOBREQUEST'].fields_by_name['data_labeling_job']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATALABELINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATALABELINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/DataLabelingJob'
    _globals['_LISTDATALABELINGJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATALABELINGJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETEDATALABELINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATALABELINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/DataLabelingJob'
    _globals['_CANCELDATALABELINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELDATALABELINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/DataLabelingJob'
    _globals['_CREATEHYPERPARAMETERTUNINGJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEHYPERPARAMETERTUNINGJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEHYPERPARAMETERTUNINGJOBREQUEST'].fields_by_name['hyperparameter_tuning_job']._loaded_options = None
    _globals['_CREATEHYPERPARAMETERTUNINGJOBREQUEST'].fields_by_name['hyperparameter_tuning_job']._serialized_options = b'\xe0A\x02'
    _globals['_GETHYPERPARAMETERTUNINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETHYPERPARAMETERTUNINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1aiplatform.googleapis.com/HyperparameterTuningJob'
    _globals['_LISTHYPERPARAMETERTUNINGJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTHYPERPARAMETERTUNINGJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETEHYPERPARAMETERTUNINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEHYPERPARAMETERTUNINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1aiplatform.googleapis.com/HyperparameterTuningJob'
    _globals['_CANCELHYPERPARAMETERTUNINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELHYPERPARAMETERTUNINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1aiplatform.googleapis.com/HyperparameterTuningJob'
    _globals['_CREATENASJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATENASJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATENASJOBREQUEST'].fields_by_name['nas_job']._loaded_options = None
    _globals['_CREATENASJOBREQUEST'].fields_by_name['nas_job']._serialized_options = b'\xe0A\x02'
    _globals['_GETNASJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNASJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n aiplatform.googleapis.com/NasJob'
    _globals['_LISTNASJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTNASJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETENASJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETENASJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n aiplatform.googleapis.com/NasJob'
    _globals['_CANCELNASJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELNASJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n aiplatform.googleapis.com/NasJob'
    _globals['_GETNASTRIALDETAILREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNASTRIALDETAILREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/NasTrialDetail'
    _globals['_LISTNASTRIALDETAILSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTNASTRIALDETAILSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n aiplatform.googleapis.com/NasJob'
    _globals['_CREATEBATCHPREDICTIONJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBATCHPREDICTIONJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEBATCHPREDICTIONJOBREQUEST'].fields_by_name['batch_prediction_job']._loaded_options = None
    _globals['_CREATEBATCHPREDICTIONJOBREQUEST'].fields_by_name['batch_prediction_job']._serialized_options = b'\xe0A\x02'
    _globals['_GETBATCHPREDICTIONJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBATCHPREDICTIONJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/BatchPredictionJob'
    _globals['_LISTBATCHPREDICTIONJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBATCHPREDICTIONJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETEBATCHPREDICTIONJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBATCHPREDICTIONJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/BatchPredictionJob'
    _globals['_CANCELBATCHPREDICTIONJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELBATCHPREDICTIONJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/BatchPredictionJob'
    _globals['_CREATEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['model_deployment_monitoring_job']._loaded_options = None
    _globals['_CREATEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['model_deployment_monitoring_job']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHMODELDEPLOYMENTMONITORINGSTATSANOMALIESREQUEST'].fields_by_name['model_deployment_monitoring_job']._loaded_options = None
    _globals['_SEARCHMODELDEPLOYMENTMONITORINGSTATSANOMALIESREQUEST'].fields_by_name['model_deployment_monitoring_job']._serialized_options = b'\xe0A\x02\xfaA8\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob'
    _globals['_SEARCHMODELDEPLOYMENTMONITORINGSTATSANOMALIESREQUEST'].fields_by_name['deployed_model_id']._loaded_options = None
    _globals['_SEARCHMODELDEPLOYMENTMONITORINGSTATSANOMALIESREQUEST'].fields_by_name['deployed_model_id']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHMODELDEPLOYMENTMONITORINGSTATSANOMALIESREQUEST'].fields_by_name['objectives']._loaded_options = None
    _globals['_SEARCHMODELDEPLOYMENTMONITORINGSTATSANOMALIESREQUEST'].fields_by_name['objectives']._serialized_options = b'\xe0A\x02'
    _globals['_GETMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA8\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob'
    _globals['_LISTMODELDEPLOYMENTMONITORINGJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMODELDEPLOYMENTMONITORINGJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_UPDATEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['model_deployment_monitoring_job']._loaded_options = None
    _globals['_UPDATEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['model_deployment_monitoring_job']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA8\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob'
    _globals['_PAUSEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PAUSEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA8\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob'
    _globals['_RESUMEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMEMODELDEPLOYMENTMONITORINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA8\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob'
    _globals['_JOBSERVICE']._loaded_options = None
    _globals['_JOBSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_JOBSERVICE'].methods_by_name['CreateCustomJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CreateCustomJob']._serialized_options = b'\xdaA\x11parent,custom_job\x82\xd3\xe4\x93\x02<"./v1/{parent=projects/*/locations/*}/customJobs:\ncustom_job'
    _globals['_JOBSERVICE'].methods_by_name['GetCustomJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['GetCustomJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/customJobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['ListCustomJobs']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['ListCustomJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/customJobs'
    _globals['_JOBSERVICE'].methods_by_name['DeleteCustomJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['DeleteCustomJob']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/customJobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['CancelCustomJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CancelCustomJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/locations/*/customJobs/*}:cancel:\x01*'
    _globals['_JOBSERVICE'].methods_by_name['CreateDataLabelingJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CreateDataLabelingJob']._serialized_options = b'\xdaA\x18parent,data_labeling_job\x82\xd3\xe4\x93\x02I"4/v1/{parent=projects/*/locations/*}/dataLabelingJobs:\x11data_labeling_job'
    _globals['_JOBSERVICE'].methods_by_name['GetDataLabelingJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['GetDataLabelingJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/dataLabelingJobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['ListDataLabelingJobs']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['ListDataLabelingJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*}/dataLabelingJobs'
    _globals['_JOBSERVICE'].methods_by_name['DeleteDataLabelingJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['DeleteDataLabelingJob']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1/{name=projects/*/locations/*/dataLabelingJobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['CancelDataLabelingJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CancelDataLabelingJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@";/v1/{name=projects/*/locations/*/dataLabelingJobs/*}:cancel:\x01*'
    _globals['_JOBSERVICE'].methods_by_name['CreateHyperparameterTuningJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CreateHyperparameterTuningJob']._serialized_options = b'\xdaA parent,hyperparameter_tuning_job\x82\xd3\xe4\x93\x02Y"</v1/{parent=projects/*/locations/*}/hyperparameterTuningJobs:\x19hyperparameter_tuning_job'
    _globals['_JOBSERVICE'].methods_by_name['GetHyperparameterTuningJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['GetHyperparameterTuningJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1/{name=projects/*/locations/*/hyperparameterTuningJobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['ListHyperparameterTuningJobs']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['ListHyperparameterTuningJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1/{parent=projects/*/locations/*}/hyperparameterTuningJobs'
    _globals['_JOBSERVICE'].methods_by_name['DeleteHyperparameterTuningJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['DeleteHyperparameterTuningJob']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1/{name=projects/*/locations/*/hyperparameterTuningJobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['CancelHyperparameterTuningJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CancelHyperparameterTuningJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02H"C/v1/{name=projects/*/locations/*/hyperparameterTuningJobs/*}:cancel:\x01*'
    _globals['_JOBSERVICE'].methods_by_name['CreateNasJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CreateNasJob']._serialized_options = b'\xdaA\x0eparent,nas_job\x82\xd3\xe4\x93\x026"+/v1/{parent=projects/*/locations/*}/nasJobs:\x07nas_job'
    _globals['_JOBSERVICE'].methods_by_name['GetNasJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['GetNasJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1/{name=projects/*/locations/*/nasJobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['ListNasJobs']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['ListNasJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=projects/*/locations/*}/nasJobs'
    _globals['_JOBSERVICE'].methods_by_name['DeleteNasJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['DeleteNasJob']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02-*+/v1/{name=projects/*/locations/*/nasJobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['CancelNasJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CancelNasJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/nasJobs/*}:cancel:\x01*'
    _globals['_JOBSERVICE'].methods_by_name['GetNasTrialDetail']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['GetNasTrialDetail']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?\x12=/v1/{name=projects/*/locations/*/nasJobs/*/nasTrialDetails/*}'
    _globals['_JOBSERVICE'].methods_by_name['ListNasTrialDetails']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['ListNasTrialDetails']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/locations/*/nasJobs/*}/nasTrialDetails'
    _globals['_JOBSERVICE'].methods_by_name['CreateBatchPredictionJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CreateBatchPredictionJob']._serialized_options = b'\xdaA\x1bparent,batch_prediction_job\x82\xd3\xe4\x93\x02O"7/v1/{parent=projects/*/locations/*}/batchPredictionJobs:\x14batch_prediction_job'
    _globals['_JOBSERVICE'].methods_by_name['GetBatchPredictionJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['GetBatchPredictionJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/{name=projects/*/locations/*/batchPredictionJobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['ListBatchPredictionJobs']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['ListBatchPredictionJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1/{parent=projects/*/locations/*}/batchPredictionJobs'
    _globals['_JOBSERVICE'].methods_by_name['DeleteBatchPredictionJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['DeleteBatchPredictionJob']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1/{name=projects/*/locations/*/batchPredictionJobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['CancelBatchPredictionJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CancelBatchPredictionJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C">/v1/{name=projects/*/locations/*/batchPredictionJobs/*}:cancel:\x01*'
    _globals['_JOBSERVICE'].methods_by_name['CreateModelDeploymentMonitoringJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CreateModelDeploymentMonitoringJob']._serialized_options = b'\xdaA&parent,model_deployment_monitoring_job\x82\xd3\xe4\x93\x02d"A/v1/{parent=projects/*/locations/*}/modelDeploymentMonitoringJobs:\x1fmodel_deployment_monitoring_job'
    _globals['_JOBSERVICE'].methods_by_name['SearchModelDeploymentMonitoringStatsAnomalies']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['SearchModelDeploymentMonitoringStatsAnomalies']._serialized_options = b'\xdaA1model_deployment_monitoring_job,deployed_model_id\x82\xd3\xe4\x93\x02\x90\x01"\x8a\x01/v1/{model_deployment_monitoring_job=projects/*/locations/*/modelDeploymentMonitoringJobs/*}:searchModelDeploymentMonitoringStatsAnomalies:\x01*'
    _globals['_JOBSERVICE'].methods_by_name['GetModelDeploymentMonitoringJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['GetModelDeploymentMonitoringJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['ListModelDeploymentMonitoringJobs']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['ListModelDeploymentMonitoringJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1/{parent=projects/*/locations/*}/modelDeploymentMonitoringJobs'
    _globals['_JOBSERVICE'].methods_by_name['UpdateModelDeploymentMonitoringJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['UpdateModelDeploymentMonitoringJob']._serialized_options = b'\xcaAS\n\x1cModelDeploymentMonitoringJob\x123UpdateModelDeploymentMonitoringJobOperationMetadata\xdaA+model_deployment_monitoring_job,update_mask\x82\xd3\xe4\x93\x02\x84\x012a/v1/{model_deployment_monitoring_job.name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}:\x1fmodel_deployment_monitoring_job'
    _globals['_JOBSERVICE'].methods_by_name['DeleteModelDeploymentMonitoringJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['DeleteModelDeploymentMonitoringJob']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02C*A/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}'
    _globals['_JOBSERVICE'].methods_by_name['PauseModelDeploymentMonitoringJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['PauseModelDeploymentMonitoringJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02L"G/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}:pause:\x01*'
    _globals['_JOBSERVICE'].methods_by_name['ResumeModelDeploymentMonitoringJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['ResumeModelDeploymentMonitoringJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02M"H/v1/{name=projects/*/locations/*/modelDeploymentMonitoringJobs/*}:resume:\x01*'
    _globals['_CREATECUSTOMJOBREQUEST']._serialized_start = 689
    _globals['_CREATECUSTOMJOBREQUEST']._serialized_end = 836
    _globals['_GETCUSTOMJOBREQUEST']._serialized_start = 838
    _globals['_GETCUSTOMJOBREQUEST']._serialized_end = 918
    _globals['_LISTCUSTOMJOBSREQUEST']._serialized_start = 921
    _globals['_LISTCUSTOMJOBSREQUEST']._serialized_end = 1105
    _globals['_LISTCUSTOMJOBSRESPONSE']._serialized_start = 1107
    _globals['_LISTCUSTOMJOBSRESPONSE']._serialized_end = 1216
    _globals['_DELETECUSTOMJOBREQUEST']._serialized_start = 1218
    _globals['_DELETECUSTOMJOBREQUEST']._serialized_end = 1301
    _globals['_CANCELCUSTOMJOBREQUEST']._serialized_start = 1303
    _globals['_CANCELCUSTOMJOBREQUEST']._serialized_end = 1386
    _globals['_CREATEDATALABELINGJOBREQUEST']._serialized_start = 1389
    _globals['_CREATEDATALABELINGJOBREQUEST']._serialized_end = 1555
    _globals['_GETDATALABELINGJOBREQUEST']._serialized_start = 1557
    _globals['_GETDATALABELINGJOBREQUEST']._serialized_end = 1649
    _globals['_LISTDATALABELINGJOBSREQUEST']._serialized_start = 1652
    _globals['_LISTDATALABELINGJOBSREQUEST']._serialized_end = 1860
    _globals['_LISTDATALABELINGJOBSRESPONSE']._serialized_start = 1863
    _globals['_LISTDATALABELINGJOBSRESPONSE']._serialized_end = 1991
    _globals['_DELETEDATALABELINGJOBREQUEST']._serialized_start = 1993
    _globals['_DELETEDATALABELINGJOBREQUEST']._serialized_end = 2088
    _globals['_CANCELDATALABELINGJOBREQUEST']._serialized_start = 2090
    _globals['_CANCELDATALABELINGJOBREQUEST']._serialized_end = 2185
    _globals['_CREATEHYPERPARAMETERTUNINGJOBREQUEST']._serialized_start = 2188
    _globals['_CREATEHYPERPARAMETERTUNINGJOBREQUEST']._serialized_end = 2378
    _globals['_GETHYPERPARAMETERTUNINGJOBREQUEST']._serialized_start = 2380
    _globals['_GETHYPERPARAMETERTUNINGJOBREQUEST']._serialized_end = 2488
    _globals['_LISTHYPERPARAMETERTUNINGJOBSREQUEST']._serialized_start = 2491
    _globals['_LISTHYPERPARAMETERTUNINGJOBSREQUEST']._serialized_end = 2689
    _globals['_LISTHYPERPARAMETERTUNINGJOBSRESPONSE']._serialized_start = 2692
    _globals['_LISTHYPERPARAMETERTUNINGJOBSRESPONSE']._serialized_end = 2844
    _globals['_DELETEHYPERPARAMETERTUNINGJOBREQUEST']._serialized_start = 2846
    _globals['_DELETEHYPERPARAMETERTUNINGJOBREQUEST']._serialized_end = 2957
    _globals['_CANCELHYPERPARAMETERTUNINGJOBREQUEST']._serialized_start = 2959
    _globals['_CANCELHYPERPARAMETERTUNINGJOBREQUEST']._serialized_end = 3070
    _globals['_CREATENASJOBREQUEST']._serialized_start = 3073
    _globals['_CREATENASJOBREQUEST']._serialized_end = 3211
    _globals['_GETNASJOBREQUEST']._serialized_start = 3213
    _globals['_GETNASJOBREQUEST']._serialized_end = 3287
    _globals['_LISTNASJOBSREQUEST']._serialized_start = 3290
    _globals['_LISTNASJOBSREQUEST']._serialized_end = 3471
    _globals['_LISTNASJOBSRESPONSE']._serialized_start = 3473
    _globals['_LISTNASJOBSRESPONSE']._serialized_end = 3573
    _globals['_DELETENASJOBREQUEST']._serialized_start = 3575
    _globals['_DELETENASJOBREQUEST']._serialized_end = 3652
    _globals['_CANCELNASJOBREQUEST']._serialized_start = 3654
    _globals['_CANCELNASJOBREQUEST']._serialized_end = 3731
    _globals['_GETNASTRIALDETAILREQUEST']._serialized_start = 3733
    _globals['_GETNASTRIALDETAILREQUEST']._serialized_end = 3823
    _globals['_LISTNASTRIALDETAILSREQUEST']._serialized_start = 3825
    _globals['_LISTNASTRIALDETAILSREQUEST']._serialized_end = 3950
    _globals['_LISTNASTRIALDETAILSRESPONSE']._serialized_start = 3952
    _globals['_LISTNASTRIALDETAILSRESPONSE']._serialized_end = 4077
    _globals['_CREATEBATCHPREDICTIONJOBREQUEST']._serialized_start = 4080
    _globals['_CREATEBATCHPREDICTIONJOBREQUEST']._serialized_end = 4255
    _globals['_GETBATCHPREDICTIONJOBREQUEST']._serialized_start = 4257
    _globals['_GETBATCHPREDICTIONJOBREQUEST']._serialized_end = 4355
    _globals['_LISTBATCHPREDICTIONJOBSREQUEST']._serialized_start = 4358
    _globals['_LISTBATCHPREDICTIONJOBSREQUEST']._serialized_end = 4551
    _globals['_LISTBATCHPREDICTIONJOBSRESPONSE']._serialized_start = 4554
    _globals['_LISTBATCHPREDICTIONJOBSRESPONSE']._serialized_end = 4691
    _globals['_DELETEBATCHPREDICTIONJOBREQUEST']._serialized_start = 4693
    _globals['_DELETEBATCHPREDICTIONJOBREQUEST']._serialized_end = 4794
    _globals['_CANCELBATCHPREDICTIONJOBREQUEST']._serialized_start = 4796
    _globals['_CANCELBATCHPREDICTIONJOBREQUEST']._serialized_end = 4897
    _globals['_CREATEMODELDEPLOYMENTMONITORINGJOBREQUEST']._serialized_start = 4900
    _globals['_CREATEMODELDEPLOYMENTMONITORINGJOBREQUEST']._serialized_end = 5106
    _globals['_SEARCHMODELDEPLOYMENTMONITORINGSTATSANOMALIESREQUEST']._serialized_start = 5109
    _globals['_SEARCHMODELDEPLOYMENTMONITORINGSTATSANOMALIESREQUEST']._serialized_end = 5732
    _globals['_SEARCHMODELDEPLOYMENTMONITORINGSTATSANOMALIESREQUEST_STATSANOMALIESOBJECTIVE']._serialized_start = 5598
    _globals['_SEARCHMODELDEPLOYMENTMONITORINGSTATSANOMALIESREQUEST_STATSANOMALIESOBJECTIVE']._serialized_end = 5732
    _globals['_SEARCHMODELDEPLOYMENTMONITORINGSTATSANOMALIESRESPONSE']._serialized_start = 5735
    _globals['_SEARCHMODELDEPLOYMENTMONITORINGSTATSANOMALIESRESPONSE']._serialized_end = 5900
    _globals['_GETMODELDEPLOYMENTMONITORINGJOBREQUEST']._serialized_start = 5902
    _globals['_GETMODELDEPLOYMENTMONITORINGJOBREQUEST']._serialized_end = 6020
    _globals['_LISTMODELDEPLOYMENTMONITORINGJOBSREQUEST']._serialized_start = 6023
    _globals['_LISTMODELDEPLOYMENTMONITORINGJOBSREQUEST']._serialized_end = 6226
    _globals['_LISTMODELDEPLOYMENTMONITORINGJOBSRESPONSE']._serialized_start = 6229
    _globals['_LISTMODELDEPLOYMENTMONITORINGJOBSRESPONSE']._serialized_end = 6397
    _globals['_UPDATEMODELDEPLOYMENTMONITORINGJOBREQUEST']._serialized_start = 6400
    _globals['_UPDATEMODELDEPLOYMENTMONITORINGJOBREQUEST']._serialized_end = 6601
    _globals['_DELETEMODELDEPLOYMENTMONITORINGJOBREQUEST']._serialized_start = 6603
    _globals['_DELETEMODELDEPLOYMENTMONITORINGJOBREQUEST']._serialized_end = 6724
    _globals['_PAUSEMODELDEPLOYMENTMONITORINGJOBREQUEST']._serialized_start = 6726
    _globals['_PAUSEMODELDEPLOYMENTMONITORINGJOBREQUEST']._serialized_end = 6846
    _globals['_RESUMEMODELDEPLOYMENTMONITORINGJOBREQUEST']._serialized_start = 6848
    _globals['_RESUMEMODELDEPLOYMENTMONITORINGJOBREQUEST']._serialized_end = 6969
    _globals['_UPDATEMODELDEPLOYMENTMONITORINGJOBOPERATIONMETADATA']._serialized_start = 6972
    _globals['_UPDATEMODELDEPLOYMENTMONITORINGJOBOPERATIONMETADATA']._serialized_end = 7105
    _globals['_JOBSERVICE']._serialized_start = 7108
    _globals['_JOBSERVICE']._serialized_end = 15284