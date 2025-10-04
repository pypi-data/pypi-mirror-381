"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/explanation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.aiplatform.v1 import explanation_metadata_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_explanation__metadata__pb2
from .....google.cloud.aiplatform.v1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_io__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/aiplatform/v1/explanation.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a5google/cloud/aiplatform/v1/explanation_metadata.proto\x1a#google/cloud/aiplatform/v1/io.proto\x1a\x1cgoogle/protobuf/struct.proto"\x8f\x01\n\x0bExplanation\x12B\n\x0cattributions\x18\x01 \x03(\x0b2\'.google.cloud.aiplatform.v1.AttributionB\x03\xe0A\x03\x12<\n\tneighbors\x18\x02 \x03(\x0b2$.google.cloud.aiplatform.v1.NeighborB\x03\xe0A\x03"[\n\x10ModelExplanation\x12G\n\x11mean_attributions\x18\x01 \x03(\x0b2\'.google.cloud.aiplatform.v1.AttributionB\x03\xe0A\x03"\x89\x02\n\x0bAttribution\x12"\n\x15baseline_output_value\x18\x01 \x01(\x01B\x03\xe0A\x03\x12"\n\x15instance_output_value\x18\x02 \x01(\x01B\x03\xe0A\x03\x129\n\x14feature_attributions\x18\x03 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x03\x12\x19\n\x0coutput_index\x18\x04 \x03(\x05B\x03\xe0A\x03\x12 \n\x13output_display_name\x18\x05 \x01(\tB\x03\xe0A\x03\x12 \n\x13approximation_error\x18\x06 \x01(\x01B\x03\xe0A\x03\x12\x18\n\x0boutput_name\x18\x07 \x01(\tB\x03\xe0A\x03"D\n\x08Neighbor\x12\x18\n\x0bneighbor_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1e\n\x11neighbor_distance\x18\x02 \x01(\x01B\x03\xe0A\x03"\xa5\x01\n\x0fExplanationSpec\x12J\n\nparameters\x18\x01 \x01(\x0b21.google.cloud.aiplatform.v1.ExplanationParametersB\x03\xe0A\x02\x12F\n\x08metadata\x18\x02 \x01(\x0b2/.google.cloud.aiplatform.v1.ExplanationMetadataB\x03\xe0A\x01"\xad\x03\n\x15ExplanationParameters\x12\\\n\x1bsampled_shapley_attribution\x18\x01 \x01(\x0b25.google.cloud.aiplatform.v1.SampledShapleyAttributionH\x00\x12f\n integrated_gradients_attribution\x18\x02 \x01(\x0b2:.google.cloud.aiplatform.v1.IntegratedGradientsAttributionH\x00\x12G\n\x10xrai_attribution\x18\x03 \x01(\x0b2+.google.cloud.aiplatform.v1.XraiAttributionH\x00\x128\n\x08examples\x18\x07 \x01(\x0b2$.google.cloud.aiplatform.v1.ExamplesH\x00\x12\r\n\x05top_k\x18\x04 \x01(\x05\x122\n\x0eoutput_indices\x18\x05 \x01(\x0b2\x1a.google.protobuf.ListValueB\x08\n\x06method"4\n\x19SampledShapleyAttribution\x12\x17\n\npath_count\x18\x01 \x01(\x05B\x03\xe0A\x02"\xd1\x01\n\x1eIntegratedGradientsAttribution\x12\x17\n\nstep_count\x18\x01 \x01(\x05B\x03\xe0A\x02\x12H\n\x12smooth_grad_config\x18\x02 \x01(\x0b2,.google.cloud.aiplatform.v1.SmoothGradConfig\x12L\n\x14blur_baseline_config\x18\x03 \x01(\x0b2..google.cloud.aiplatform.v1.BlurBaselineConfig"\xc2\x01\n\x0fXraiAttribution\x12\x17\n\nstep_count\x18\x01 \x01(\x05B\x03\xe0A\x02\x12H\n\x12smooth_grad_config\x18\x02 \x01(\x0b2,.google.cloud.aiplatform.v1.SmoothGradConfig\x12L\n\x14blur_baseline_config\x18\x03 \x01(\x0b2..google.cloud.aiplatform.v1.BlurBaselineConfig"\xa9\x01\n\x10SmoothGradConfig\x12\x15\n\x0bnoise_sigma\x18\x01 \x01(\x02H\x00\x12L\n\x13feature_noise_sigma\x18\x02 \x01(\x0b2-.google.cloud.aiplatform.v1.FeatureNoiseSigmaH\x00\x12\x1a\n\x12noisy_sample_count\x18\x03 \x01(\x05B\x14\n\x12GradientNoiseSigma"\xa1\x01\n\x11FeatureNoiseSigma\x12W\n\x0bnoise_sigma\x18\x01 \x03(\x0b2B.google.cloud.aiplatform.v1.FeatureNoiseSigma.NoiseSigmaForFeature\x1a3\n\x14NoiseSigmaForFeature\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05sigma\x18\x02 \x01(\x02",\n\x12BlurBaselineConfig\x12\x16\n\x0emax_blur_sigma\x18\x01 \x01(\x02"\xe2\x03\n\x08Examples\x12S\n\x12example_gcs_source\x18\x05 \x01(\x0b25.google.cloud.aiplatform.v1.Examples.ExampleGcsSourceH\x00\x12@\n\x1enearest_neighbor_search_config\x18\x02 \x01(\x0b2\x16.google.protobuf.ValueH\x01\x126\n\x07presets\x18\x04 \x01(\x0b2#.google.cloud.aiplatform.v1.PresetsH\x01\x12\x16\n\x0eneighbor_count\x18\x03 \x01(\x05\x1a\xda\x01\n\x10ExampleGcsSource\x12U\n\x0bdata_format\x18\x01 \x01(\x0e2@.google.cloud.aiplatform.v1.Examples.ExampleGcsSource.DataFormat\x129\n\ngcs_source\x18\x02 \x01(\x0b2%.google.cloud.aiplatform.v1.GcsSource"4\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\t\n\x05JSONL\x10\x01B\x08\n\x06sourceB\x08\n\x06config"\xfa\x01\n\x07Presets\x12=\n\x05query\x18\x01 \x01(\x0e2).google.cloud.aiplatform.v1.Presets.QueryH\x00\x88\x01\x01\x12>\n\x08modality\x18\x02 \x01(\x0e2,.google.cloud.aiplatform.v1.Presets.Modality"\x1e\n\x05Query\x12\x0b\n\x07PRECISE\x10\x00\x12\x08\n\x04FAST\x10\x01"F\n\x08Modality\x12\x18\n\x14MODALITY_UNSPECIFIED\x10\x00\x12\t\n\x05IMAGE\x10\x01\x12\x08\n\x04TEXT\x10\x02\x12\x0b\n\x07TABULAR\x10\x03B\x08\n\x06_query"\xf4\x01\n\x17ExplanationSpecOverride\x12E\n\nparameters\x18\x01 \x01(\x0b21.google.cloud.aiplatform.v1.ExplanationParameters\x12I\n\x08metadata\x18\x02 \x01(\x0b27.google.cloud.aiplatform.v1.ExplanationMetadataOverride\x12G\n\x11examples_override\x18\x03 \x01(\x0b2,.google.cloud.aiplatform.v1.ExamplesOverride"\xbf\x02\n\x1bExplanationMetadataOverride\x12X\n\x06inputs\x18\x01 \x03(\x0b2C.google.cloud.aiplatform.v1.ExplanationMetadataOverride.InputsEntryB\x03\xe0A\x02\x1aH\n\x15InputMetadataOverride\x12/\n\x0finput_baselines\x18\x01 \x03(\x0b2\x16.google.protobuf.Value\x1a|\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\\\n\x05value\x18\x02 \x01(\x0b2M.google.cloud.aiplatform.v1.ExplanationMetadataOverride.InputMetadataOverride:\x028\x01"\xc6\x02\n\x10ExamplesOverride\x12\x16\n\x0eneighbor_count\x18\x01 \x01(\x05\x12\x16\n\x0ecrowding_count\x18\x02 \x01(\x05\x12O\n\x0crestrictions\x18\x03 \x03(\x0b29.google.cloud.aiplatform.v1.ExamplesRestrictionsNamespace\x12\x19\n\x11return_embeddings\x18\x04 \x01(\x08\x12L\n\x0bdata_format\x18\x05 \x01(\x0e27.google.cloud.aiplatform.v1.ExamplesOverride.DataFormat"H\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\r\n\tINSTANCES\x10\x01\x12\x0e\n\nEMBEDDINGS\x10\x02"T\n\x1dExamplesRestrictionsNamespace\x12\x16\n\x0enamespace_name\x18\x01 \x01(\t\x12\r\n\x05allow\x18\x02 \x03(\t\x12\x0c\n\x04deny\x18\x03 \x03(\tB\xce\x01\n\x1ecom.google.cloud.aiplatform.v1B\x10ExplanationProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.explanation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x10ExplanationProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_EXPLANATION'].fields_by_name['attributions']._loaded_options = None
    _globals['_EXPLANATION'].fields_by_name['attributions']._serialized_options = b'\xe0A\x03'
    _globals['_EXPLANATION'].fields_by_name['neighbors']._loaded_options = None
    _globals['_EXPLANATION'].fields_by_name['neighbors']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEXPLANATION'].fields_by_name['mean_attributions']._loaded_options = None
    _globals['_MODELEXPLANATION'].fields_by_name['mean_attributions']._serialized_options = b'\xe0A\x03'
    _globals['_ATTRIBUTION'].fields_by_name['baseline_output_value']._loaded_options = None
    _globals['_ATTRIBUTION'].fields_by_name['baseline_output_value']._serialized_options = b'\xe0A\x03'
    _globals['_ATTRIBUTION'].fields_by_name['instance_output_value']._loaded_options = None
    _globals['_ATTRIBUTION'].fields_by_name['instance_output_value']._serialized_options = b'\xe0A\x03'
    _globals['_ATTRIBUTION'].fields_by_name['feature_attributions']._loaded_options = None
    _globals['_ATTRIBUTION'].fields_by_name['feature_attributions']._serialized_options = b'\xe0A\x03'
    _globals['_ATTRIBUTION'].fields_by_name['output_index']._loaded_options = None
    _globals['_ATTRIBUTION'].fields_by_name['output_index']._serialized_options = b'\xe0A\x03'
    _globals['_ATTRIBUTION'].fields_by_name['output_display_name']._loaded_options = None
    _globals['_ATTRIBUTION'].fields_by_name['output_display_name']._serialized_options = b'\xe0A\x03'
    _globals['_ATTRIBUTION'].fields_by_name['approximation_error']._loaded_options = None
    _globals['_ATTRIBUTION'].fields_by_name['approximation_error']._serialized_options = b'\xe0A\x03'
    _globals['_ATTRIBUTION'].fields_by_name['output_name']._loaded_options = None
    _globals['_ATTRIBUTION'].fields_by_name['output_name']._serialized_options = b'\xe0A\x03'
    _globals['_NEIGHBOR'].fields_by_name['neighbor_id']._loaded_options = None
    _globals['_NEIGHBOR'].fields_by_name['neighbor_id']._serialized_options = b'\xe0A\x03'
    _globals['_NEIGHBOR'].fields_by_name['neighbor_distance']._loaded_options = None
    _globals['_NEIGHBOR'].fields_by_name['neighbor_distance']._serialized_options = b'\xe0A\x03'
    _globals['_EXPLANATIONSPEC'].fields_by_name['parameters']._loaded_options = None
    _globals['_EXPLANATIONSPEC'].fields_by_name['parameters']._serialized_options = b'\xe0A\x02'
    _globals['_EXPLANATIONSPEC'].fields_by_name['metadata']._loaded_options = None
    _globals['_EXPLANATIONSPEC'].fields_by_name['metadata']._serialized_options = b'\xe0A\x01'
    _globals['_SAMPLEDSHAPLEYATTRIBUTION'].fields_by_name['path_count']._loaded_options = None
    _globals['_SAMPLEDSHAPLEYATTRIBUTION'].fields_by_name['path_count']._serialized_options = b'\xe0A\x02'
    _globals['_INTEGRATEDGRADIENTSATTRIBUTION'].fields_by_name['step_count']._loaded_options = None
    _globals['_INTEGRATEDGRADIENTSATTRIBUTION'].fields_by_name['step_count']._serialized_options = b'\xe0A\x02'
    _globals['_XRAIATTRIBUTION'].fields_by_name['step_count']._loaded_options = None
    _globals['_XRAIATTRIBUTION'].fields_by_name['step_count']._serialized_options = b'\xe0A\x02'
    _globals['_EXPLANATIONMETADATAOVERRIDE_INPUTSENTRY']._loaded_options = None
    _globals['_EXPLANATIONMETADATAOVERRIDE_INPUTSENTRY']._serialized_options = b'8\x01'
    _globals['_EXPLANATIONMETADATAOVERRIDE'].fields_by_name['inputs']._loaded_options = None
    _globals['_EXPLANATIONMETADATAOVERRIDE'].fields_by_name['inputs']._serialized_options = b'\xe0A\x02'
    _globals['_EXPLANATION']._serialized_start = 232
    _globals['_EXPLANATION']._serialized_end = 375
    _globals['_MODELEXPLANATION']._serialized_start = 377
    _globals['_MODELEXPLANATION']._serialized_end = 468
    _globals['_ATTRIBUTION']._serialized_start = 471
    _globals['_ATTRIBUTION']._serialized_end = 736
    _globals['_NEIGHBOR']._serialized_start = 738
    _globals['_NEIGHBOR']._serialized_end = 806
    _globals['_EXPLANATIONSPEC']._serialized_start = 809
    _globals['_EXPLANATIONSPEC']._serialized_end = 974
    _globals['_EXPLANATIONPARAMETERS']._serialized_start = 977
    _globals['_EXPLANATIONPARAMETERS']._serialized_end = 1406
    _globals['_SAMPLEDSHAPLEYATTRIBUTION']._serialized_start = 1408
    _globals['_SAMPLEDSHAPLEYATTRIBUTION']._serialized_end = 1460
    _globals['_INTEGRATEDGRADIENTSATTRIBUTION']._serialized_start = 1463
    _globals['_INTEGRATEDGRADIENTSATTRIBUTION']._serialized_end = 1672
    _globals['_XRAIATTRIBUTION']._serialized_start = 1675
    _globals['_XRAIATTRIBUTION']._serialized_end = 1869
    _globals['_SMOOTHGRADCONFIG']._serialized_start = 1872
    _globals['_SMOOTHGRADCONFIG']._serialized_end = 2041
    _globals['_FEATURENOISESIGMA']._serialized_start = 2044
    _globals['_FEATURENOISESIGMA']._serialized_end = 2205
    _globals['_FEATURENOISESIGMA_NOISESIGMAFORFEATURE']._serialized_start = 2154
    _globals['_FEATURENOISESIGMA_NOISESIGMAFORFEATURE']._serialized_end = 2205
    _globals['_BLURBASELINECONFIG']._serialized_start = 2207
    _globals['_BLURBASELINECONFIG']._serialized_end = 2251
    _globals['_EXAMPLES']._serialized_start = 2254
    _globals['_EXAMPLES']._serialized_end = 2736
    _globals['_EXAMPLES_EXAMPLEGCSSOURCE']._serialized_start = 2498
    _globals['_EXAMPLES_EXAMPLEGCSSOURCE']._serialized_end = 2716
    _globals['_EXAMPLES_EXAMPLEGCSSOURCE_DATAFORMAT']._serialized_start = 2664
    _globals['_EXAMPLES_EXAMPLEGCSSOURCE_DATAFORMAT']._serialized_end = 2716
    _globals['_PRESETS']._serialized_start = 2739
    _globals['_PRESETS']._serialized_end = 2989
    _globals['_PRESETS_QUERY']._serialized_start = 2877
    _globals['_PRESETS_QUERY']._serialized_end = 2907
    _globals['_PRESETS_MODALITY']._serialized_start = 2909
    _globals['_PRESETS_MODALITY']._serialized_end = 2979
    _globals['_EXPLANATIONSPECOVERRIDE']._serialized_start = 2992
    _globals['_EXPLANATIONSPECOVERRIDE']._serialized_end = 3236
    _globals['_EXPLANATIONMETADATAOVERRIDE']._serialized_start = 3239
    _globals['_EXPLANATIONMETADATAOVERRIDE']._serialized_end = 3558
    _globals['_EXPLANATIONMETADATAOVERRIDE_INPUTMETADATAOVERRIDE']._serialized_start = 3360
    _globals['_EXPLANATIONMETADATAOVERRIDE_INPUTMETADATAOVERRIDE']._serialized_end = 3432
    _globals['_EXPLANATIONMETADATAOVERRIDE_INPUTSENTRY']._serialized_start = 3434
    _globals['_EXPLANATIONMETADATAOVERRIDE_INPUTSENTRY']._serialized_end = 3558
    _globals['_EXAMPLESOVERRIDE']._serialized_start = 3561
    _globals['_EXAMPLESOVERRIDE']._serialized_end = 3887
    _globals['_EXAMPLESOVERRIDE_DATAFORMAT']._serialized_start = 3815
    _globals['_EXAMPLESOVERRIDE_DATAFORMAT']._serialized_end = 3887
    _globals['_EXAMPLESRESTRICTIONSNAMESPACE']._serialized_start = 3889
    _globals['_EXAMPLESRESTRICTIONSNAMESPACE']._serialized_end = 3973