"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/evaluated_annotation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.aiplatform.v1beta1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_explanation__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/aiplatform/v1beta1/evaluated_annotation.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a1google/cloud/aiplatform/v1beta1/explanation.proto\x1a\x1cgoogle/protobuf/struct.proto"\xf4\x04\n\x13EvaluatedAnnotation\x12_\n\x04type\x18\x01 \x01(\x0e2L.google.cloud.aiplatform.v1beta1.EvaluatedAnnotation.EvaluatedAnnotationTypeB\x03\xe0A\x03\x120\n\x0bpredictions\x18\x02 \x03(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x03\x122\n\rground_truths\x18\x03 \x03(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x03\x126\n\x11data_item_payload\x18\x05 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x03\x12(\n\x1bevaluated_data_item_view_id\x18\x06 \x01(\tB\x03\xe0A\x03\x12U\n\x0cexplanations\x18\x08 \x03(\x0b2?.google.cloud.aiplatform.v1beta1.EvaluatedAnnotationExplanation\x12\\\n\x1aerror_analysis_annotations\x18\t \x03(\x0b28.google.cloud.aiplatform.v1beta1.ErrorAnalysisAnnotation"\x7f\n\x17EvaluatedAnnotationType\x12)\n%EVALUATED_ANNOTATION_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rTRUE_POSITIVE\x10\x01\x12\x12\n\x0eFALSE_POSITIVE\x10\x02\x12\x12\n\x0eFALSE_NEGATIVE\x10\x03"}\n\x1eEvaluatedAnnotationExplanation\x12\x18\n\x10explanation_type\x18\x01 \x01(\t\x12A\n\x0bexplanation\x18\x02 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.Explanation"\xb9\x03\n\x17ErrorAnalysisAnnotation\x12a\n\x10attributed_items\x18\x01 \x03(\x0b2G.google.cloud.aiplatform.v1beta1.ErrorAnalysisAnnotation.AttributedItem\x12V\n\nquery_type\x18\x02 \x01(\x0e2B.google.cloud.aiplatform.v1beta1.ErrorAnalysisAnnotation.QueryType\x12\x15\n\routlier_score\x18\x03 \x01(\x01\x12\x19\n\x11outlier_threshold\x18\x04 \x01(\x01\x1aD\n\x0eAttributedItem\x12 \n\x18annotation_resource_name\x18\x01 \x01(\t\x12\x10\n\x08distance\x18\x02 \x01(\x01"k\n\tQueryType\x12\x1a\n\x16QUERY_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bALL_SIMILAR\x10\x01\x12\x16\n\x12SAME_CLASS_SIMILAR\x10\x02\x12\x19\n\x15SAME_CLASS_DISSIMILAR\x10\x03B\xef\x01\n#com.google.cloud.aiplatform.v1beta1B\x18EvaluatedAnnotationProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.evaluated_annotation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x18EvaluatedAnnotationProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_EVALUATEDANNOTATION'].fields_by_name['type']._loaded_options = None
    _globals['_EVALUATEDANNOTATION'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_EVALUATEDANNOTATION'].fields_by_name['predictions']._loaded_options = None
    _globals['_EVALUATEDANNOTATION'].fields_by_name['predictions']._serialized_options = b'\xe0A\x03'
    _globals['_EVALUATEDANNOTATION'].fields_by_name['ground_truths']._loaded_options = None
    _globals['_EVALUATEDANNOTATION'].fields_by_name['ground_truths']._serialized_options = b'\xe0A\x03'
    _globals['_EVALUATEDANNOTATION'].fields_by_name['data_item_payload']._loaded_options = None
    _globals['_EVALUATEDANNOTATION'].fields_by_name['data_item_payload']._serialized_options = b'\xe0A\x03'
    _globals['_EVALUATEDANNOTATION'].fields_by_name['evaluated_data_item_view_id']._loaded_options = None
    _globals['_EVALUATEDANNOTATION'].fields_by_name['evaluated_data_item_view_id']._serialized_options = b'\xe0A\x03'
    _globals['_EVALUATEDANNOTATION']._serialized_start = 210
    _globals['_EVALUATEDANNOTATION']._serialized_end = 838
    _globals['_EVALUATEDANNOTATION_EVALUATEDANNOTATIONTYPE']._serialized_start = 711
    _globals['_EVALUATEDANNOTATION_EVALUATEDANNOTATIONTYPE']._serialized_end = 838
    _globals['_EVALUATEDANNOTATIONEXPLANATION']._serialized_start = 840
    _globals['_EVALUATEDANNOTATIONEXPLANATION']._serialized_end = 965
    _globals['_ERRORANALYSISANNOTATION']._serialized_start = 968
    _globals['_ERRORANALYSISANNOTATION']._serialized_end = 1409
    _globals['_ERRORANALYSISANNOTATION_ATTRIBUTEDITEM']._serialized_start = 1232
    _globals['_ERRORANALYSISANNOTATION_ATTRIBUTEDITEM']._serialized_end = 1300
    _globals['_ERRORANALYSISANNOTATION_QUERYTYPE']._serialized_start = 1302
    _globals['_ERRORANALYSISANNOTATION_QUERYTYPE']._serialized_end = 1409