"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.financialservices.v1 import backtest_result_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2
from .....google.cloud.financialservices.v1 import dataset_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2
from .....google.cloud.financialservices.v1 import engine_config_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2
from .....google.cloud.financialservices.v1 import engine_version_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2
from .....google.cloud.financialservices.v1 import instance_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2
from .....google.cloud.financialservices.v1 import model_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2
from .....google.cloud.financialservices.v1 import prediction_result_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/financialservices/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class AMLStub(object):
    """The AML (Anti Money Laundering) service allows users to perform REST
    operations on aml.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListInstances = channel.unary_unary('/google.cloud.financialservices.v1.AML/ListInstances', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.ListInstancesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.ListInstancesResponse.FromString, _registered_method=True)
        self.GetInstance = channel.unary_unary('/google.cloud.financialservices.v1.AML/GetInstance', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.GetInstanceRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.Instance.FromString, _registered_method=True)
        self.CreateInstance = channel.unary_unary('/google.cloud.financialservices.v1.AML/CreateInstance', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.CreateInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateInstance = channel.unary_unary('/google.cloud.financialservices.v1.AML/UpdateInstance', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.UpdateInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteInstance = channel.unary_unary('/google.cloud.financialservices.v1.AML/DeleteInstance', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.DeleteInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ImportRegisteredParties = channel.unary_unary('/google.cloud.financialservices.v1.AML/ImportRegisteredParties', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.ImportRegisteredPartiesRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ExportRegisteredParties = channel.unary_unary('/google.cloud.financialservices.v1.AML/ExportRegisteredParties', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.ExportRegisteredPartiesRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListDatasets = channel.unary_unary('/google.cloud.financialservices.v1.AML/ListDatasets', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.ListDatasetsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.ListDatasetsResponse.FromString, _registered_method=True)
        self.GetDataset = channel.unary_unary('/google.cloud.financialservices.v1.AML/GetDataset', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.GetDatasetRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.Dataset.FromString, _registered_method=True)
        self.CreateDataset = channel.unary_unary('/google.cloud.financialservices.v1.AML/CreateDataset', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.CreateDatasetRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateDataset = channel.unary_unary('/google.cloud.financialservices.v1.AML/UpdateDataset', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.UpdateDatasetRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteDataset = channel.unary_unary('/google.cloud.financialservices.v1.AML/DeleteDataset', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.DeleteDatasetRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListModels = channel.unary_unary('/google.cloud.financialservices.v1.AML/ListModels', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.ListModelsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.ListModelsResponse.FromString, _registered_method=True)
        self.GetModel = channel.unary_unary('/google.cloud.financialservices.v1.AML/GetModel', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.GetModelRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.Model.FromString, _registered_method=True)
        self.CreateModel = channel.unary_unary('/google.cloud.financialservices.v1.AML/CreateModel', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.CreateModelRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateModel = channel.unary_unary('/google.cloud.financialservices.v1.AML/UpdateModel', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.UpdateModelRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ExportModelMetadata = channel.unary_unary('/google.cloud.financialservices.v1.AML/ExportModelMetadata', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.ExportModelMetadataRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteModel = channel.unary_unary('/google.cloud.financialservices.v1.AML/DeleteModel', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.DeleteModelRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListEngineConfigs = channel.unary_unary('/google.cloud.financialservices.v1.AML/ListEngineConfigs', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.ListEngineConfigsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.ListEngineConfigsResponse.FromString, _registered_method=True)
        self.GetEngineConfig = channel.unary_unary('/google.cloud.financialservices.v1.AML/GetEngineConfig', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.GetEngineConfigRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.EngineConfig.FromString, _registered_method=True)
        self.CreateEngineConfig = channel.unary_unary('/google.cloud.financialservices.v1.AML/CreateEngineConfig', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.CreateEngineConfigRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateEngineConfig = channel.unary_unary('/google.cloud.financialservices.v1.AML/UpdateEngineConfig', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.UpdateEngineConfigRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ExportEngineConfigMetadata = channel.unary_unary('/google.cloud.financialservices.v1.AML/ExportEngineConfigMetadata', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.ExportEngineConfigMetadataRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteEngineConfig = channel.unary_unary('/google.cloud.financialservices.v1.AML/DeleteEngineConfig', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.DeleteEngineConfigRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.GetEngineVersion = channel.unary_unary('/google.cloud.financialservices.v1.AML/GetEngineVersion', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2.GetEngineVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2.EngineVersion.FromString, _registered_method=True)
        self.ListEngineVersions = channel.unary_unary('/google.cloud.financialservices.v1.AML/ListEngineVersions', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2.ListEngineVersionsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2.ListEngineVersionsResponse.FromString, _registered_method=True)
        self.ListPredictionResults = channel.unary_unary('/google.cloud.financialservices.v1.AML/ListPredictionResults', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.ListPredictionResultsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.ListPredictionResultsResponse.FromString, _registered_method=True)
        self.GetPredictionResult = channel.unary_unary('/google.cloud.financialservices.v1.AML/GetPredictionResult', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.GetPredictionResultRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.PredictionResult.FromString, _registered_method=True)
        self.CreatePredictionResult = channel.unary_unary('/google.cloud.financialservices.v1.AML/CreatePredictionResult', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.CreatePredictionResultRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdatePredictionResult = channel.unary_unary('/google.cloud.financialservices.v1.AML/UpdatePredictionResult', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.UpdatePredictionResultRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ExportPredictionResultMetadata = channel.unary_unary('/google.cloud.financialservices.v1.AML/ExportPredictionResultMetadata', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.ExportPredictionResultMetadataRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeletePredictionResult = channel.unary_unary('/google.cloud.financialservices.v1.AML/DeletePredictionResult', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.DeletePredictionResultRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListBacktestResults = channel.unary_unary('/google.cloud.financialservices.v1.AML/ListBacktestResults', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.ListBacktestResultsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.ListBacktestResultsResponse.FromString, _registered_method=True)
        self.GetBacktestResult = channel.unary_unary('/google.cloud.financialservices.v1.AML/GetBacktestResult', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.GetBacktestResultRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.BacktestResult.FromString, _registered_method=True)
        self.CreateBacktestResult = channel.unary_unary('/google.cloud.financialservices.v1.AML/CreateBacktestResult', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.CreateBacktestResultRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateBacktestResult = channel.unary_unary('/google.cloud.financialservices.v1.AML/UpdateBacktestResult', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.UpdateBacktestResultRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ExportBacktestResultMetadata = channel.unary_unary('/google.cloud.financialservices.v1.AML/ExportBacktestResultMetadata', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.ExportBacktestResultMetadataRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteBacktestResult = channel.unary_unary('/google.cloud.financialservices.v1.AML/DeleteBacktestResult', request_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.DeleteBacktestResultRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)

class AMLServicer(object):
    """The AML (Anti Money Laundering) service allows users to perform REST
    operations on aml.
    """

    def ListInstances(self, request, context):
        """Lists instances.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInstance(self, request, context):
        """Gets an instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateInstance(self, request, context):
        """Creates an instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateInstance(self, request, context):
        """Updates the parameters of a single Instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteInstance(self, request, context):
        """Deletes an instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportRegisteredParties(self, request, context):
        """Imports the list of registered parties. See
        [Create and manage
        instances](https://cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances#import-registered-parties)
        for information on the input schema and response for this method.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportRegisteredParties(self, request, context):
        """Exports the list of registered parties. See
        [Create and manage
        instances](https://cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances#export-registered-parties)
        for information on the output schema for this method.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDatasets(self, request, context):
        """Lists datasets.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDataset(self, request, context):
        """Gets a dataset.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDataset(self, request, context):
        """Creates a dataset.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDataset(self, request, context):
        """Updates the parameters of a single Dataset.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDataset(self, request, context):
        """Deletes a dataset.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListModels(self, request, context):
        """Lists models.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetModel(self, request, context):
        """Gets a model.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateModel(self, request, context):
        """Creates a model.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateModel(self, request, context):
        """Updates the parameters of a single Model.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportModelMetadata(self, request, context):
        """Export governance information for a Model resource. For
        information on the exported fields, see
        [AML output data
        model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#model).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteModel(self, request, context):
        """Deletes a model.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEngineConfigs(self, request, context):
        """Lists engine configs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEngineConfig(self, request, context):
        """Gets an engine config.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateEngineConfig(self, request, context):
        """Creates an engine config.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEngineConfig(self, request, context):
        """Updates the parameters of a single EngineConfig.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportEngineConfigMetadata(self, request, context):
        """Export governance information for an EngineConfig resource. For
        information on the exported fields, see
        [AML output data
        model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#engine-config).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEngineConfig(self, request, context):
        """Deletes an engine config.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEngineVersion(self, request, context):
        """Gets a single EngineVersion.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEngineVersions(self, request, context):
        """Lists EngineVersions for given location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPredictionResults(self, request, context):
        """List PredictionResults.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPredictionResult(self, request, context):
        """Gets a PredictionResult.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePredictionResult(self, request, context):
        """Create a PredictionResult.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePredictionResult(self, request, context):
        """Updates the parameters of a single PredictionResult.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportPredictionResultMetadata(self, request, context):
        """Export governance information for a PredictionResult resource. For
        information on the exported fields, see
        [AML output data
        model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#prediction-results).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePredictionResult(self, request, context):
        """Deletes a PredictionResult.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBacktestResults(self, request, context):
        """List BacktestResults.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBacktestResult(self, request, context):
        """Gets a BacktestResult.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBacktestResult(self, request, context):
        """Create a BacktestResult.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBacktestResult(self, request, context):
        """Updates the parameters of a single BacktestResult.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportBacktestResultMetadata(self, request, context):
        """Export governance information for a BacktestResult resource. For
        information on the exported fields, see
        [AML output data
        model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#backtest-results).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBacktestResult(self, request, context):
        """Deletes a BacktestResult.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_AMLServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListInstances': grpc.unary_unary_rpc_method_handler(servicer.ListInstances, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.ListInstancesRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.ListInstancesResponse.SerializeToString), 'GetInstance': grpc.unary_unary_rpc_method_handler(servicer.GetInstance, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.GetInstanceRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.Instance.SerializeToString), 'CreateInstance': grpc.unary_unary_rpc_method_handler(servicer.CreateInstance, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.CreateInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateInstance': grpc.unary_unary_rpc_method_handler(servicer.UpdateInstance, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.UpdateInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteInstance': grpc.unary_unary_rpc_method_handler(servicer.DeleteInstance, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.DeleteInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ImportRegisteredParties': grpc.unary_unary_rpc_method_handler(servicer.ImportRegisteredParties, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.ImportRegisteredPartiesRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ExportRegisteredParties': grpc.unary_unary_rpc_method_handler(servicer.ExportRegisteredParties, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.ExportRegisteredPartiesRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListDatasets': grpc.unary_unary_rpc_method_handler(servicer.ListDatasets, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.ListDatasetsRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.ListDatasetsResponse.SerializeToString), 'GetDataset': grpc.unary_unary_rpc_method_handler(servicer.GetDataset, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.GetDatasetRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.Dataset.SerializeToString), 'CreateDataset': grpc.unary_unary_rpc_method_handler(servicer.CreateDataset, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.CreateDatasetRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateDataset': grpc.unary_unary_rpc_method_handler(servicer.UpdateDataset, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.UpdateDatasetRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteDataset': grpc.unary_unary_rpc_method_handler(servicer.DeleteDataset, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.DeleteDatasetRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListModels': grpc.unary_unary_rpc_method_handler(servicer.ListModels, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.ListModelsRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.ListModelsResponse.SerializeToString), 'GetModel': grpc.unary_unary_rpc_method_handler(servicer.GetModel, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.GetModelRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.Model.SerializeToString), 'CreateModel': grpc.unary_unary_rpc_method_handler(servicer.CreateModel, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.CreateModelRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateModel': grpc.unary_unary_rpc_method_handler(servicer.UpdateModel, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.UpdateModelRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ExportModelMetadata': grpc.unary_unary_rpc_method_handler(servicer.ExportModelMetadata, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.ExportModelMetadataRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteModel': grpc.unary_unary_rpc_method_handler(servicer.DeleteModel, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.DeleteModelRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListEngineConfigs': grpc.unary_unary_rpc_method_handler(servicer.ListEngineConfigs, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.ListEngineConfigsRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.ListEngineConfigsResponse.SerializeToString), 'GetEngineConfig': grpc.unary_unary_rpc_method_handler(servicer.GetEngineConfig, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.GetEngineConfigRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.EngineConfig.SerializeToString), 'CreateEngineConfig': grpc.unary_unary_rpc_method_handler(servicer.CreateEngineConfig, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.CreateEngineConfigRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateEngineConfig': grpc.unary_unary_rpc_method_handler(servicer.UpdateEngineConfig, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.UpdateEngineConfigRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ExportEngineConfigMetadata': grpc.unary_unary_rpc_method_handler(servicer.ExportEngineConfigMetadata, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.ExportEngineConfigMetadataRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteEngineConfig': grpc.unary_unary_rpc_method_handler(servicer.DeleteEngineConfig, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.DeleteEngineConfigRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'GetEngineVersion': grpc.unary_unary_rpc_method_handler(servicer.GetEngineVersion, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2.GetEngineVersionRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2.EngineVersion.SerializeToString), 'ListEngineVersions': grpc.unary_unary_rpc_method_handler(servicer.ListEngineVersions, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2.ListEngineVersionsRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2.ListEngineVersionsResponse.SerializeToString), 'ListPredictionResults': grpc.unary_unary_rpc_method_handler(servicer.ListPredictionResults, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.ListPredictionResultsRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.ListPredictionResultsResponse.SerializeToString), 'GetPredictionResult': grpc.unary_unary_rpc_method_handler(servicer.GetPredictionResult, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.GetPredictionResultRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.PredictionResult.SerializeToString), 'CreatePredictionResult': grpc.unary_unary_rpc_method_handler(servicer.CreatePredictionResult, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.CreatePredictionResultRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdatePredictionResult': grpc.unary_unary_rpc_method_handler(servicer.UpdatePredictionResult, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.UpdatePredictionResultRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ExportPredictionResultMetadata': grpc.unary_unary_rpc_method_handler(servicer.ExportPredictionResultMetadata, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.ExportPredictionResultMetadataRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeletePredictionResult': grpc.unary_unary_rpc_method_handler(servicer.DeletePredictionResult, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.DeletePredictionResultRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListBacktestResults': grpc.unary_unary_rpc_method_handler(servicer.ListBacktestResults, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.ListBacktestResultsRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.ListBacktestResultsResponse.SerializeToString), 'GetBacktestResult': grpc.unary_unary_rpc_method_handler(servicer.GetBacktestResult, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.GetBacktestResultRequest.FromString, response_serializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.BacktestResult.SerializeToString), 'CreateBacktestResult': grpc.unary_unary_rpc_method_handler(servicer.CreateBacktestResult, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.CreateBacktestResultRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateBacktestResult': grpc.unary_unary_rpc_method_handler(servicer.UpdateBacktestResult, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.UpdateBacktestResultRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ExportBacktestResultMetadata': grpc.unary_unary_rpc_method_handler(servicer.ExportBacktestResultMetadata, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.ExportBacktestResultMetadataRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteBacktestResult': grpc.unary_unary_rpc_method_handler(servicer.DeleteBacktestResult, request_deserializer=google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.DeleteBacktestResultRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.financialservices.v1.AML', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.financialservices.v1.AML', rpc_method_handlers)

class AML(object):
    """The AML (Anti Money Laundering) service allows users to perform REST
    operations on aml.
    """

    @staticmethod
    def ListInstances(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ListInstances', google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.ListInstancesRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.ListInstancesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/GetInstance', google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.GetInstanceRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.Instance.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/CreateInstance', google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.CreateInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/UpdateInstance', google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.UpdateInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/DeleteInstance', google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.DeleteInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ImportRegisteredParties(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ImportRegisteredParties', google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.ImportRegisteredPartiesRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ExportRegisteredParties(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ExportRegisteredParties', google_dot_cloud_dot_financialservices_dot_v1_dot_instance__pb2.ExportRegisteredPartiesRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListDatasets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ListDatasets', google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.ListDatasetsRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.ListDatasetsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetDataset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/GetDataset', google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.GetDatasetRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.Dataset.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateDataset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/CreateDataset', google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.CreateDatasetRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateDataset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/UpdateDataset', google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.UpdateDatasetRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteDataset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/DeleteDataset', google_dot_cloud_dot_financialservices_dot_v1_dot_dataset__pb2.DeleteDatasetRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListModels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ListModels', google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.ListModelsRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.ListModelsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetModel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/GetModel', google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.GetModelRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.Model.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateModel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/CreateModel', google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.CreateModelRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateModel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/UpdateModel', google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.UpdateModelRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ExportModelMetadata(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ExportModelMetadata', google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.ExportModelMetadataRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteModel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/DeleteModel', google_dot_cloud_dot_financialservices_dot_v1_dot_model__pb2.DeleteModelRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListEngineConfigs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ListEngineConfigs', google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.ListEngineConfigsRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.ListEngineConfigsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetEngineConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/GetEngineConfig', google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.GetEngineConfigRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.EngineConfig.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateEngineConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/CreateEngineConfig', google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.CreateEngineConfigRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateEngineConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/UpdateEngineConfig', google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.UpdateEngineConfigRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ExportEngineConfigMetadata(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ExportEngineConfigMetadata', google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.ExportEngineConfigMetadataRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteEngineConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/DeleteEngineConfig', google_dot_cloud_dot_financialservices_dot_v1_dot_engine__config__pb2.DeleteEngineConfigRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetEngineVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/GetEngineVersion', google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2.GetEngineVersionRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2.EngineVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListEngineVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ListEngineVersions', google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2.ListEngineVersionsRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_engine__version__pb2.ListEngineVersionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListPredictionResults(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ListPredictionResults', google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.ListPredictionResultsRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.ListPredictionResultsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetPredictionResult(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/GetPredictionResult', google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.GetPredictionResultRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.PredictionResult.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreatePredictionResult(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/CreatePredictionResult', google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.CreatePredictionResultRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdatePredictionResult(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/UpdatePredictionResult', google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.UpdatePredictionResultRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ExportPredictionResultMetadata(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ExportPredictionResultMetadata', google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.ExportPredictionResultMetadataRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeletePredictionResult(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/DeletePredictionResult', google_dot_cloud_dot_financialservices_dot_v1_dot_prediction__result__pb2.DeletePredictionResultRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListBacktestResults(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ListBacktestResults', google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.ListBacktestResultsRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.ListBacktestResultsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetBacktestResult(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/GetBacktestResult', google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.GetBacktestResultRequest.SerializeToString, google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.BacktestResult.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateBacktestResult(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/CreateBacktestResult', google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.CreateBacktestResultRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateBacktestResult(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/UpdateBacktestResult', google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.UpdateBacktestResultRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ExportBacktestResultMetadata(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/ExportBacktestResultMetadata', google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.ExportBacktestResultMetadataRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteBacktestResult(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.financialservices.v1.AML/DeleteBacktestResult', google_dot_cloud_dot_financialservices_dot_v1_dot_backtest__result__pb2.DeleteBacktestResultRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)