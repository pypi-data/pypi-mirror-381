"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1alpha/model_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ai.generativelanguage.v1alpha import model_pb2 as google_dot_ai_dot_generativelanguage_dot_v1alpha_dot_model__pb2
from .....google.ai.generativelanguage.v1alpha import tuned_model_pb2 as google_dot_ai_dot_generativelanguage_dot_v1alpha_dot_tuned__model__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ai/generativelanguage/v1alpha/model_service.proto\x12$google.ai.generativelanguage.v1alpha\x1a0google/ai/generativelanguage/v1alpha/model.proto\x1a6google/ai/generativelanguage/v1alpha/tuned_model.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"P\n\x0fGetModelRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'generativelanguage.googleapis.com/Model":\n\x11ListModelsRequest\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"j\n\x12ListModelsResponse\x12;\n\x06models\x18\x01 \x03(\x0b2+.google.ai.generativelanguage.v1alpha.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Z\n\x14GetTunedModelRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,generativelanguage.googleapis.com/TunedModel"^\n\x16ListTunedModelsRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x01"z\n\x17ListTunedModelsResponse\x12F\n\x0ctuned_models\x18\x01 \x03(\x0b20.google.ai.generativelanguage.v1alpha.TunedModel\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9a\x01\n\x17CreateTunedModelRequest\x12 \n\x0etuned_model_id\x18\x01 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12J\n\x0btuned_model\x18\x02 \x01(\x0b20.google.ai.generativelanguage.v1alpha.TunedModelB\x03\xe0A\x02B\x11\n\x0f_tuned_model_id"\xf4\x01\n\x18CreateTunedModelMetadata\x12F\n\x0btuned_model\x18\x05 \x01(\tB1\xfaA.\n,generativelanguage.googleapis.com/TunedModel\x12\x13\n\x0btotal_steps\x18\x01 \x01(\x05\x12\x17\n\x0fcompleted_steps\x18\x02 \x01(\x05\x12\x19\n\x11completed_percent\x18\x03 \x01(\x02\x12G\n\tsnapshots\x18\x04 \x03(\x0b24.google.ai.generativelanguage.v1alpha.TuningSnapshot"\x9b\x01\n\x17UpdateTunedModelRequest\x12J\n\x0btuned_model\x18\x01 \x01(\x0b20.google.ai.generativelanguage.v1alpha.TunedModelB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"]\n\x17DeleteTunedModelRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,generativelanguage.googleapis.com/TunedModel2\xe0\n\n\x0cModelService\x12\x97\x01\n\x08GetModel\x125.google.ai.generativelanguage.v1alpha.GetModelRequest\x1a+.google.ai.generativelanguage.v1alpha.Model"\'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1alpha/{name=models/*}\x12\xaf\x01\n\nListModels\x127.google.ai.generativelanguage.v1alpha.ListModelsRequest\x1a8.google.ai.generativelanguage.v1alpha.ListModelsResponse".\xdaA\x14page_size,page_token\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1alpha/models\x12\xab\x01\n\rGetTunedModel\x12:.google.ai.generativelanguage.v1alpha.GetTunedModelRequest\x1a0.google.ai.generativelanguage.v1alpha.TunedModel",\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1alpha/{name=tunedModels/*}\x12\xc3\x01\n\x0fListTunedModels\x12<.google.ai.generativelanguage.v1alpha.ListTunedModelsRequest\x1a=.google.ai.generativelanguage.v1alpha.ListTunedModelsResponse"3\xdaA\x14page_size,page_token\x82\xd3\xe4\x93\x02\x16\x12\x14/v1alpha/tunedModels\x12\xef\x01\n\x10CreateTunedModel\x12=.google.ai.generativelanguage.v1alpha.CreateTunedModelRequest\x1a\x1d.google.longrunning.Operation"}\xcaA&\n\nTunedModel\x12\x18CreateTunedModelMetadata\xdaA\x0btuned_model\xdaA\x1atuned_model_id,tuned_model\x82\xd3\xe4\x93\x02#"\x14/v1alpha/tunedModels:\x0btuned_model\x12\xdd\x01\n\x10UpdateTunedModel\x12=.google.ai.generativelanguage.v1alpha.UpdateTunedModelRequest\x1a0.google.ai.generativelanguage.v1alpha.TunedModel"X\xdaA\x17tuned_model,update_mask\x82\xd3\xe4\x93\x0282)/v1alpha/{tuned_model.name=tunedModels/*}:\x0btuned_model\x12\x97\x01\n\x10DeleteTunedModel\x12=.google.ai.generativelanguage.v1alpha.DeleteTunedModelRequest\x1a\x16.google.protobuf.Empty",\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f*\x1d/v1alpha/{name=tunedModels/*}\x1a$\xcaA!generativelanguage.googleapis.comB\x9f\x01\n(com.google.ai.generativelanguage.v1alphaB\x11ModelServiceProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1alpha/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1alpha.model_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ai.generativelanguage.v1alphaB\x11ModelServiceProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1alpha/generativelanguagepb;generativelanguagepb'
    _globals['_GETMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'generativelanguage.googleapis.com/Model"
    _globals['_GETTUNEDMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTUNEDMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,generativelanguage.googleapis.com/TunedModel'
    _globals['_LISTTUNEDMODELSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTTUNEDMODELSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTUNEDMODELSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTTUNEDMODELSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTUNEDMODELSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTTUNEDMODELSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_CREATETUNEDMODELREQUEST'].fields_by_name['tuned_model_id']._loaded_options = None
    _globals['_CREATETUNEDMODELREQUEST'].fields_by_name['tuned_model_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATETUNEDMODELREQUEST'].fields_by_name['tuned_model']._loaded_options = None
    _globals['_CREATETUNEDMODELREQUEST'].fields_by_name['tuned_model']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETUNEDMODELMETADATA'].fields_by_name['tuned_model']._loaded_options = None
    _globals['_CREATETUNEDMODELMETADATA'].fields_by_name['tuned_model']._serialized_options = b'\xfaA.\n,generativelanguage.googleapis.com/TunedModel'
    _globals['_UPDATETUNEDMODELREQUEST'].fields_by_name['tuned_model']._loaded_options = None
    _globals['_UPDATETUNEDMODELREQUEST'].fields_by_name['tuned_model']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETUNEDMODELREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATETUNEDMODELREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETETUNEDMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETUNEDMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,generativelanguage.googleapis.com/TunedModel'
    _globals['_MODELSERVICE']._loaded_options = None
    _globals['_MODELSERVICE']._serialized_options = b'\xcaA!generativelanguage.googleapis.com'
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1alpha/{name=models/*}'
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._serialized_options = b'\xdaA\x14page_size,page_token\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1alpha/models'
    _globals['_MODELSERVICE'].methods_by_name['GetTunedModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['GetTunedModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1alpha/{name=tunedModels/*}'
    _globals['_MODELSERVICE'].methods_by_name['ListTunedModels']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListTunedModels']._serialized_options = b'\xdaA\x14page_size,page_token\x82\xd3\xe4\x93\x02\x16\x12\x14/v1alpha/tunedModels'
    _globals['_MODELSERVICE'].methods_by_name['CreateTunedModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['CreateTunedModel']._serialized_options = b'\xcaA&\n\nTunedModel\x12\x18CreateTunedModelMetadata\xdaA\x0btuned_model\xdaA\x1atuned_model_id,tuned_model\x82\xd3\xe4\x93\x02#"\x14/v1alpha/tunedModels:\x0btuned_model'
    _globals['_MODELSERVICE'].methods_by_name['UpdateTunedModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['UpdateTunedModel']._serialized_options = b'\xdaA\x17tuned_model,update_mask\x82\xd3\xe4\x93\x0282)/v1alpha/{tuned_model.name=tunedModels/*}:\x0btuned_model'
    _globals['_MODELSERVICE'].methods_by_name['DeleteTunedModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['DeleteTunedModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1f*\x1d/v1alpha/{name=tunedModels/*}'
    _globals['_GETMODELREQUEST']._serialized_start = 419
    _globals['_GETMODELREQUEST']._serialized_end = 499
    _globals['_LISTMODELSREQUEST']._serialized_start = 501
    _globals['_LISTMODELSREQUEST']._serialized_end = 559
    _globals['_LISTMODELSRESPONSE']._serialized_start = 561
    _globals['_LISTMODELSRESPONSE']._serialized_end = 667
    _globals['_GETTUNEDMODELREQUEST']._serialized_start = 669
    _globals['_GETTUNEDMODELREQUEST']._serialized_end = 759
    _globals['_LISTTUNEDMODELSREQUEST']._serialized_start = 761
    _globals['_LISTTUNEDMODELSREQUEST']._serialized_end = 855
    _globals['_LISTTUNEDMODELSRESPONSE']._serialized_start = 857
    _globals['_LISTTUNEDMODELSRESPONSE']._serialized_end = 979
    _globals['_CREATETUNEDMODELREQUEST']._serialized_start = 982
    _globals['_CREATETUNEDMODELREQUEST']._serialized_end = 1136
    _globals['_CREATETUNEDMODELMETADATA']._serialized_start = 1139
    _globals['_CREATETUNEDMODELMETADATA']._serialized_end = 1383
    _globals['_UPDATETUNEDMODELREQUEST']._serialized_start = 1386
    _globals['_UPDATETUNEDMODELREQUEST']._serialized_end = 1541
    _globals['_DELETETUNEDMODELREQUEST']._serialized_start = 1543
    _globals['_DELETETUNEDMODELREQUEST']._serialized_end = 1636
    _globals['_MODELSERVICE']._serialized_start = 1639
    _globals['_MODELSERVICE']._serialized_end = 3015