"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2beta/model_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2beta import model_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_model__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/retail/v2beta/model_service.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/retail/v2beta/model.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x98\x01\n\x12CreateModelRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x125\n\x05model\x18\x02 \x01(\x0b2!.google.cloud.retail.v2beta.ModelB\x03\xe0A\x02\x12\x14\n\x07dry_run\x18\x03 \x01(\x08B\x03\xe0A\x01"\x81\x01\n\x12UpdateModelRequest\x125\n\x05model\x18\x01 \x01(\x0b2!.google.cloud.retail.v2beta.ModelB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"D\n\x0fGetModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bretail.googleapis.com/Model"F\n\x11PauseModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bretail.googleapis.com/Model"\'\n\x12ResumeModelRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"{\n\x11ListModelsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"G\n\x12DeleteModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bretail.googleapis.com/Model"`\n\x12ListModelsResponse\x121\n\x06models\x18\x01 \x03(\x0b2!.google.cloud.retail.v2beta.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"E\n\x10TuneModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bretail.googleapis.com/Model"$\n\x13CreateModelMetadata\x12\r\n\x05model\x18\x01 \x01(\t""\n\x11TuneModelMetadata\x12\r\n\x05model\x18\x01 \x01(\t"\x13\n\x11TuneModelResponse2\xa9\r\n\x0cModelService\x12\x8b\x02\n\x0bCreateModel\x12..google.cloud.retail.v2beta.CreateModelRequest\x1a\x1d.google.longrunning.Operation"\xac\x01\xcaAR\n google.cloud.retail.v2beta.Model\x12.google.cloud.retail.v2beta.CreateModelMetadata\xdaA\x0cparent,model\x82\xd3\xe4\x93\x02B"9/v2beta/{parent=projects/*/locations/*/catalogs/*}/models:\x05model\x12\xa4\x01\n\x08GetModel\x12+.google.cloud.retail.v2beta.GetModelRequest\x1a!.google.cloud.retail.v2beta.Model"H\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v2beta/{name=projects/*/locations/*/catalogs/*/models/*}\x12\xb1\x01\n\nPauseModel\x12-.google.cloud.retail.v2beta.PauseModelRequest\x1a!.google.cloud.retail.v2beta.Model"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D"?/v2beta/{name=projects/*/locations/*/catalogs/*/models/*}:pause:\x01*\x12\xb4\x01\n\x0bResumeModel\x12..google.cloud.retail.v2beta.ResumeModelRequest\x1a!.google.cloud.retail.v2beta.Model"R\xdaA\x04name\x82\xd3\xe4\x93\x02E"@/v2beta/{name=projects/*/locations/*/catalogs/*/models/*}:resume:\x01*\x12\x9f\x01\n\x0bDeleteModel\x12..google.cloud.retail.v2beta.DeleteModelRequest\x1a\x16.google.protobuf.Empty"H\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v2beta/{name=projects/*/locations/*/catalogs/*/models/*}\x12\xb7\x01\n\nListModels\x12-.google.cloud.retail.v2beta.ListModelsRequest\x1a..google.cloud.retail.v2beta.ListModelsResponse"J\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v2beta/{parent=projects/*/locations/*/catalogs/*}/models\x12\xc4\x01\n\x0bUpdateModel\x12..google.cloud.retail.v2beta.UpdateModelRequest\x1a!.google.cloud.retail.v2beta.Model"b\xdaA\x11model,update_mask\x82\xd3\xe4\x93\x02H2?/v2beta/{model.name=projects/*/locations/*/catalogs/*/models/*}:\x05model\x12\x8a\x02\n\tTuneModel\x12,.google.cloud.retail.v2beta.TuneModelRequest\x1a\x1d.google.longrunning.Operation"\xaf\x01\xcaA\\\n,google.cloud.retail.v2beta.TuneModelResponse\x12,google.cloud.retail.v2beta.TuneModelMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02C">/v2beta/{name=projects/*/locations/*/catalogs/*/models/*}:tune:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd0\x01\n\x1ecom.google.cloud.retail.v2betaB\x11ModelServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.model_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x11ModelServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
    _globals['_CREATEMODELREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMODELREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_CREATEMODELREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_CREATEMODELREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMODELREQUEST'].fields_by_name['dry_run']._loaded_options = None
    _globals['_CREATEMODELREQUEST'].fields_by_name['dry_run']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEMODELREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_UPDATEMODELREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMODELREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMODELREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_GETMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bretail.googleapis.com/Model'
    _globals['_PAUSEMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PAUSEMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bretail.googleapis.com/Model'
    _globals['_RESUMEMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMEMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_LISTMODELSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMODELSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_LISTMODELSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTMODELSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMODELSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTMODELSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bretail.googleapis.com/Model'
    _globals['_TUNEMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_TUNEMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1bretail.googleapis.com/Model'
    _globals['_MODELSERVICE']._loaded_options = None
    _globals['_MODELSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MODELSERVICE'].methods_by_name['CreateModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['CreateModel']._serialized_options = b'\xcaAR\n google.cloud.retail.v2beta.Model\x12.google.cloud.retail.v2beta.CreateModelMetadata\xdaA\x0cparent,model\x82\xd3\xe4\x93\x02B"9/v2beta/{parent=projects/*/locations/*/catalogs/*}/models:\x05model'
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v2beta/{name=projects/*/locations/*/catalogs/*/models/*}'
    _globals['_MODELSERVICE'].methods_by_name['PauseModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['PauseModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D"?/v2beta/{name=projects/*/locations/*/catalogs/*/models/*}:pause:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['ResumeModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ResumeModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E"@/v2beta/{name=projects/*/locations/*/catalogs/*/models/*}:resume:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['DeleteModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['DeleteModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v2beta/{name=projects/*/locations/*/catalogs/*/models/*}'
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v2beta/{parent=projects/*/locations/*/catalogs/*}/models'
    _globals['_MODELSERVICE'].methods_by_name['UpdateModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['UpdateModel']._serialized_options = b'\xdaA\x11model,update_mask\x82\xd3\xe4\x93\x02H2?/v2beta/{model.name=projects/*/locations/*/catalogs/*/models/*}:\x05model'
    _globals['_MODELSERVICE'].methods_by_name['TuneModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['TuneModel']._serialized_options = b'\xcaA\\\n,google.cloud.retail.v2beta.TuneModelResponse\x12,google.cloud.retail.v2beta.TuneModelMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02C">/v2beta/{name=projects/*/locations/*/catalogs/*/models/*}:tune:\x01*'
    _globals['_CREATEMODELREQUEST']._serialized_start = 334
    _globals['_CREATEMODELREQUEST']._serialized_end = 486
    _globals['_UPDATEMODELREQUEST']._serialized_start = 489
    _globals['_UPDATEMODELREQUEST']._serialized_end = 618
    _globals['_GETMODELREQUEST']._serialized_start = 620
    _globals['_GETMODELREQUEST']._serialized_end = 688
    _globals['_PAUSEMODELREQUEST']._serialized_start = 690
    _globals['_PAUSEMODELREQUEST']._serialized_end = 760
    _globals['_RESUMEMODELREQUEST']._serialized_start = 762
    _globals['_RESUMEMODELREQUEST']._serialized_end = 801
    _globals['_LISTMODELSREQUEST']._serialized_start = 803
    _globals['_LISTMODELSREQUEST']._serialized_end = 926
    _globals['_DELETEMODELREQUEST']._serialized_start = 928
    _globals['_DELETEMODELREQUEST']._serialized_end = 999
    _globals['_LISTMODELSRESPONSE']._serialized_start = 1001
    _globals['_LISTMODELSRESPONSE']._serialized_end = 1097
    _globals['_TUNEMODELREQUEST']._serialized_start = 1099
    _globals['_TUNEMODELREQUEST']._serialized_end = 1168
    _globals['_CREATEMODELMETADATA']._serialized_start = 1170
    _globals['_CREATEMODELMETADATA']._serialized_end = 1206
    _globals['_TUNEMODELMETADATA']._serialized_start = 1208
    _globals['_TUNEMODELMETADATA']._serialized_end = 1242
    _globals['_TUNEMODELRESPONSE']._serialized_start = 1244
    _globals['_TUNEMODELRESPONSE']._serialized_end = 1263
    _globals['_MODELSERVICE']._serialized_start = 1266
    _globals['_MODELSERVICE']._serialized_end = 2971