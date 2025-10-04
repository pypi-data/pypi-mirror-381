"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2/model_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2 import model_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_model__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/retail/v2/model_service.proto\x12\x16google.cloud.retail.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a"google/cloud/retail/v2/model.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x94\x01\n\x12CreateModelRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x121\n\x05model\x18\x02 \x01(\x0b2\x1d.google.cloud.retail.v2.ModelB\x03\xe0A\x02\x12\x14\n\x07dry_run\x18\x03 \x01(\x08B\x03\xe0A\x01"}\n\x12UpdateModelRequest\x121\n\x05model\x18\x01 \x01(\x0b2\x1d.google.cloud.retail.v2.ModelB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"D\n\x0fGetModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bretail.googleapis.com/Model"F\n\x11PauseModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bretail.googleapis.com/Model"\'\n\x12ResumeModelRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"{\n\x11ListModelsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"G\n\x12DeleteModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bretail.googleapis.com/Model"\\\n\x12ListModelsResponse\x12-\n\x06models\x18\x01 \x03(\x0b2\x1d.google.cloud.retail.v2.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"E\n\x10TuneModelRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1bretail.googleapis.com/Model"$\n\x13CreateModelMetadata\x12\r\n\x05model\x18\x01 \x01(\t""\n\x11TuneModelMetadata\x12\r\n\x05model\x18\x01 \x01(\t"\x13\n\x11TuneModelResponse2\xc5\x0c\n\x0cModelService\x12\xfb\x01\n\x0bCreateModel\x12*.google.cloud.retail.v2.CreateModelRequest\x1a\x1d.google.longrunning.Operation"\xa0\x01\xcaAJ\n\x1cgoogle.cloud.retail.v2.Model\x12*google.cloud.retail.v2.CreateModelMetadata\xdaA\x0cparent,model\x82\xd3\xe4\x93\x02>"5/v2/{parent=projects/*/locations/*/catalogs/*}/models:\x05model\x12\x98\x01\n\x08GetModel\x12\'.google.cloud.retail.v2.GetModelRequest\x1a\x1d.google.cloud.retail.v2.Model"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v2/{name=projects/*/locations/*/catalogs/*/models/*}\x12\xa5\x01\n\nPauseModel\x12).google.cloud.retail.v2.PauseModelRequest\x1a\x1d.google.cloud.retail.v2.Model"M\xdaA\x04name\x82\xd3\xe4\x93\x02@";/v2/{name=projects/*/locations/*/catalogs/*/models/*}:pause:\x01*\x12\xa8\x01\n\x0bResumeModel\x12*.google.cloud.retail.v2.ResumeModelRequest\x1a\x1d.google.cloud.retail.v2.Model"N\xdaA\x04name\x82\xd3\xe4\x93\x02A"</v2/{name=projects/*/locations/*/catalogs/*/models/*}:resume:\x01*\x12\x97\x01\n\x0bDeleteModel\x12*.google.cloud.retail.v2.DeleteModelRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v2/{name=projects/*/locations/*/catalogs/*/models/*}\x12\xab\x01\n\nListModels\x12).google.cloud.retail.v2.ListModelsRequest\x1a*.google.cloud.retail.v2.ListModelsResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v2/{parent=projects/*/locations/*/catalogs/*}/models\x12\xb8\x01\n\x0bUpdateModel\x12*.google.cloud.retail.v2.UpdateModelRequest\x1a\x1d.google.cloud.retail.v2.Model"^\xdaA\x11model,update_mask\x82\xd3\xe4\x93\x02D2;/v2/{model.name=projects/*/locations/*/catalogs/*/models/*}:\x05model\x12\xfa\x01\n\tTuneModel\x12(.google.cloud.retail.v2.TuneModelRequest\x1a\x1d.google.longrunning.Operation"\xa3\x01\xcaAT\n(google.cloud.retail.v2.TuneModelResponse\x12(google.cloud.retail.v2.TuneModelMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02?":/v2/{name=projects/*/locations/*/catalogs/*/models/*}:tune:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xbc\x01\n\x1acom.google.cloud.retail.v2B\x11ModelServiceProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2.model_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.retail.v2B\x11ModelServiceProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2'
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
    _globals['_MODELSERVICE'].methods_by_name['CreateModel']._serialized_options = b'\xcaAJ\n\x1cgoogle.cloud.retail.v2.Model\x12*google.cloud.retail.v2.CreateModelMetadata\xdaA\x0cparent,model\x82\xd3\xe4\x93\x02>"5/v2/{parent=projects/*/locations/*/catalogs/*}/models:\x05model'
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v2/{name=projects/*/locations/*/catalogs/*/models/*}'
    _globals['_MODELSERVICE'].methods_by_name['PauseModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['PauseModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@";/v2/{name=projects/*/locations/*/catalogs/*/models/*}:pause:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['ResumeModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ResumeModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A"</v2/{name=projects/*/locations/*/catalogs/*/models/*}:resume:\x01*'
    _globals['_MODELSERVICE'].methods_by_name['DeleteModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['DeleteModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v2/{name=projects/*/locations/*/catalogs/*/models/*}'
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v2/{parent=projects/*/locations/*/catalogs/*}/models'
    _globals['_MODELSERVICE'].methods_by_name['UpdateModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['UpdateModel']._serialized_options = b'\xdaA\x11model,update_mask\x82\xd3\xe4\x93\x02D2;/v2/{model.name=projects/*/locations/*/catalogs/*/models/*}:\x05model'
    _globals['_MODELSERVICE'].methods_by_name['TuneModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['TuneModel']._serialized_options = b'\xcaAT\n(google.cloud.retail.v2.TuneModelResponse\x12(google.cloud.retail.v2.TuneModelMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02?":/v2/{name=projects/*/locations/*/catalogs/*/models/*}:tune:\x01*'
    _globals['_CREATEMODELREQUEST']._serialized_start = 322
    _globals['_CREATEMODELREQUEST']._serialized_end = 470
    _globals['_UPDATEMODELREQUEST']._serialized_start = 472
    _globals['_UPDATEMODELREQUEST']._serialized_end = 597
    _globals['_GETMODELREQUEST']._serialized_start = 599
    _globals['_GETMODELREQUEST']._serialized_end = 667
    _globals['_PAUSEMODELREQUEST']._serialized_start = 669
    _globals['_PAUSEMODELREQUEST']._serialized_end = 739
    _globals['_RESUMEMODELREQUEST']._serialized_start = 741
    _globals['_RESUMEMODELREQUEST']._serialized_end = 780
    _globals['_LISTMODELSREQUEST']._serialized_start = 782
    _globals['_LISTMODELSREQUEST']._serialized_end = 905
    _globals['_DELETEMODELREQUEST']._serialized_start = 907
    _globals['_DELETEMODELREQUEST']._serialized_end = 978
    _globals['_LISTMODELSRESPONSE']._serialized_start = 980
    _globals['_LISTMODELSRESPONSE']._serialized_end = 1072
    _globals['_TUNEMODELREQUEST']._serialized_start = 1074
    _globals['_TUNEMODELREQUEST']._serialized_end = 1143
    _globals['_CREATEMODELMETADATA']._serialized_start = 1145
    _globals['_CREATEMODELMETADATA']._serialized_end = 1181
    _globals['_TUNEMODELMETADATA']._serialized_start = 1183
    _globals['_TUNEMODELMETADATA']._serialized_end = 1217
    _globals['_TUNEMODELRESPONSE']._serialized_start = 1219
    _globals['_TUNEMODELRESPONSE']._serialized_end = 1238
    _globals['_MODELSERVICE']._serialized_start = 1241
    _globals['_MODELSERVICE']._serialized_end = 2846