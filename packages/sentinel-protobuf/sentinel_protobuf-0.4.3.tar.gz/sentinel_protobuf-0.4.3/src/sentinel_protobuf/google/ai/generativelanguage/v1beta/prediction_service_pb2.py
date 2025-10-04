"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1beta/prediction_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ai/generativelanguage/v1beta/prediction_service.proto\x12#google.ai.generativelanguage.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1cgoogle/protobuf/struct.proto"\xb1\x01\n\x0ePredictRequest\x12>\n\x05model\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'generativelanguage.googleapis.com/Model\x12.\n\tinstances\x18\x02 \x03(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x02\x12/\n\nparameters\x18\x03 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x01"\xbc\x01\n\x19PredictLongRunningRequest\x12>\n\x05model\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'generativelanguage.googleapis.com/Model\x12.\n\tinstances\x18\x02 \x03(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x02\x12/\n\nparameters\x18\x03 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x01">\n\x0fPredictResponse\x12+\n\x0bpredictions\x18\x01 \x03(\x0b2\x16.google.protobuf.Value"\x87\x01\n\x1aPredictLongRunningResponse\x12]\n\x17generate_video_response\x18\x01 \x01(\x0b2:.google.ai.generativelanguage.v1beta.GenerateVideoResponseH\x00B\n\n\x08response"\x1c\n\x1aPredictLongRunningMetadata"L\n\x05Media\x12;\n\x05video\x18\x01 \x01(\x0b2*.google.ai.generativelanguage.v1beta.VideoH\x00B\x06\n\x04type"2\n\x05Video\x12\x0f\n\x05video\x18\x01 \x01(\x0cH\x00\x12\r\n\x03uri\x18\x02 \x01(\tH\x00B\t\n\x07content"\xa4\x01\n\x15GenerateVideoResponse\x12E\n\x11generated_samples\x18\x01 \x03(\x0b2*.google.ai.generativelanguage.v1beta.Media\x12 \n\x18rai_media_filtered_count\x18\x02 \x01(\x05\x12"\n\x1arai_media_filtered_reasons\x18\x03 \x03(\t2\xeb\x03\n\x11PredictionService\x12\xb3\x01\n\x07Predict\x123.google.ai.generativelanguage.v1beta.PredictRequest\x1a4.google.ai.generativelanguage.v1beta.PredictResponse"=\xdaA\x0fmodel,instances\x82\xd3\xe4\x93\x02%" /v1beta/{model=models/*}:predict:\x01*\x12\xf9\x01\n\x12PredictLongRunning\x12>.google.ai.generativelanguage.v1beta.PredictLongRunningRequest\x1a\x1d.google.longrunning.Operation"\x83\x01\xcaA8\n\x1aPredictLongRunningResponse\x12\x1aPredictLongRunningMetadata\xdaA\x0fmodel,instances\x82\xd3\xe4\x93\x020"+/v1beta/{model=models/*}:predictLongRunning:\x01*\x1a$\xcaA!generativelanguage.googleapis.comB\xa2\x01\n\'com.google.ai.generativelanguage.v1betaB\x16PredictionServiceProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta.prediction_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.ai.generativelanguage.v1betaB\x16PredictionServiceProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepb"
    _globals['_PREDICTREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['model']._serialized_options = b"\xe0A\x02\xfaA)\n'generativelanguage.googleapis.com/Model"
    _globals['_PREDICTREQUEST'].fields_by_name['instances']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['instances']._serialized_options = b'\xe0A\x02'
    _globals['_PREDICTREQUEST'].fields_by_name['parameters']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_PREDICTLONGRUNNINGREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_PREDICTLONGRUNNINGREQUEST'].fields_by_name['model']._serialized_options = b"\xe0A\x02\xfaA)\n'generativelanguage.googleapis.com/Model"
    _globals['_PREDICTLONGRUNNINGREQUEST'].fields_by_name['instances']._loaded_options = None
    _globals['_PREDICTLONGRUNNINGREQUEST'].fields_by_name['instances']._serialized_options = b'\xe0A\x02'
    _globals['_PREDICTLONGRUNNINGREQUEST'].fields_by_name['parameters']._loaded_options = None
    _globals['_PREDICTLONGRUNNINGREQUEST'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_PREDICTIONSERVICE']._loaded_options = None
    _globals['_PREDICTIONSERVICE']._serialized_options = b'\xcaA!generativelanguage.googleapis.com'
    _globals['_PREDICTIONSERVICE'].methods_by_name['Predict']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['Predict']._serialized_options = b'\xdaA\x0fmodel,instances\x82\xd3\xe4\x93\x02%" /v1beta/{model=models/*}:predict:\x01*'
    _globals['_PREDICTIONSERVICE'].methods_by_name['PredictLongRunning']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['PredictLongRunning']._serialized_options = b'\xcaA8\n\x1aPredictLongRunningResponse\x12\x1aPredictLongRunningMetadata\xdaA\x0fmodel,instances\x82\xd3\xe4\x93\x020"+/v1beta/{model=models/*}:predictLongRunning:\x01*'
    _globals['_PREDICTREQUEST']._serialized_start = 284
    _globals['_PREDICTREQUEST']._serialized_end = 461
    _globals['_PREDICTLONGRUNNINGREQUEST']._serialized_start = 464
    _globals['_PREDICTLONGRUNNINGREQUEST']._serialized_end = 652
    _globals['_PREDICTRESPONSE']._serialized_start = 654
    _globals['_PREDICTRESPONSE']._serialized_end = 716
    _globals['_PREDICTLONGRUNNINGRESPONSE']._serialized_start = 719
    _globals['_PREDICTLONGRUNNINGRESPONSE']._serialized_end = 854
    _globals['_PREDICTLONGRUNNINGMETADATA']._serialized_start = 856
    _globals['_PREDICTLONGRUNNINGMETADATA']._serialized_end = 884
    _globals['_MEDIA']._serialized_start = 886
    _globals['_MEDIA']._serialized_end = 962
    _globals['_VIDEO']._serialized_start = 964
    _globals['_VIDEO']._serialized_end = 1014
    _globals['_GENERATEVIDEORESPONSE']._serialized_start = 1017
    _globals['_GENERATEVIDEORESPONSE']._serialized_end = 1181
    _globals['_PREDICTIONSERVICE']._serialized_start = 1184
    _globals['_PREDICTIONSERVICE']._serialized_end = 1675