"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/grounded_generation_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import grounding_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_grounding__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/cloud/discoveryengine/v1beta/grounded_generation_service.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a3google/cloud/discoveryengine/v1beta/grounding.proto"\x9d\x01\n\x19GroundedGenerationContent\x12\x0c\n\x04role\x18\x01 \x01(\t\x12R\n\x05parts\x18\x02 \x03(\x0b2C.google.cloud.discoveryengine.v1beta.GroundedGenerationContent.Part\x1a\x1e\n\x04Part\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00B\x06\n\x04data"\x82\x14\n\x1eGenerateGroundedContentRequest\x12A\n\x08location\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Location\x12Z\n\x12system_instruction\x18\x05 \x01(\x0b2>.google.cloud.discoveryengine.v1beta.GroundedGenerationContent\x12P\n\x08contents\x18\x02 \x03(\x0b2>.google.cloud.discoveryengine.v1beta.GroundedGenerationContent\x12k\n\x0fgeneration_spec\x18\x03 \x01(\x0b2R.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest.GenerationSpec\x12i\n\x0egrounding_spec\x18\x04 \x01(\x0b2Q.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest.GroundingSpec\x12h\n\x0buser_labels\x18\x06 \x03(\x0b2S.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest.UserLabelsEntry\x1a\xbf\x02\n\x0eGenerationSpec\x12\x10\n\x08model_id\x18\x03 \x01(\t\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x18\n\x0btemperature\x18\x04 \x01(\x02H\x00\x88\x01\x01\x12\x12\n\x05top_p\x18\x05 \x01(\x02H\x01\x88\x01\x01\x12\x12\n\x05top_k\x18\x07 \x01(\x05H\x02\x88\x01\x01\x12\x1e\n\x11frequency_penalty\x18\x08 \x01(\x02H\x03\x88\x01\x01\x12\x1d\n\x10presence_penalty\x18\t \x01(\x02H\x04\x88\x01\x01\x12\x1e\n\x11max_output_tokens\x18\n \x01(\x05H\x05\x88\x01\x01B\x0e\n\x0c_temperatureB\x08\n\x06_top_pB\x08\n\x06_top_kB\x14\n\x12_frequency_penaltyB\x13\n\x11_presence_penaltyB\x14\n\x12_max_output_tokens\x1a\xc4\x03\n\x1dDynamicRetrievalConfiguration\x12\x8e\x01\n\tpredictor\x18\x01 \x01(\x0b2{.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor\x1a\x91\x02\n\x19DynamicRetrievalPredictor\x12\x95\x01\n\x07version\x18\x01 \x01(\x0e2\x83\x01.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest.DynamicRetrievalConfiguration.DynamicRetrievalPredictor.Version\x12\x16\n\tthreshold\x18\x02 \x01(\x02H\x00\x88\x01\x01"6\n\x07Version\x12\x17\n\x13VERSION_UNSPECIFIED\x10\x00\x12\x12\n\x0eV1_INDEPENDENT\x10\x01B\x0c\n\n_threshold\x1a\xef\x07\n\x0fGroundingSource\x12y\n\rinline_source\x18\x01 \x01(\x0b2`.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest.GroundingSource.InlineSourceH\x00\x12y\n\rsearch_source\x18\x02 \x01(\x0b2`.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest.GroundingSource.SearchSourceH\x00\x12\x86\x01\n\x14google_search_source\x18\x03 \x01(\x0b2f.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest.GroundingSource.GoogleSearchSourceH\x00\x1a\x95\x02\n\x0cInlineSource\x12K\n\x0fgrounding_facts\x18\x01 \x03(\x0b22.google.cloud.discoveryengine.v1beta.GroundingFact\x12\x84\x01\n\nattributes\x18\x02 \x03(\x0b2p.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest.GroundingSource.InlineSource.AttributesEntry\x1a1\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a\x98\x01\n\x0cSearchSource\x12I\n\x0eserving_config\x18\x01 \x01(\tB1\xfaA.\n,discoveryengine.googleapis.com/ServingConfig\x12\x18\n\x10max_result_count\x18\x02 \x01(\x05\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x13\n\x0bsafe_search\x18\x05 \x01(\x08\x1a\x9f\x01\n\x12GoogleSearchSource\x12\x88\x01\n\x18dynamic_retrieval_config\x18\x02 \x01(\x0b2a.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest.DynamicRetrievalConfigurationB\x03\xe0A\x01B\x08\n\x06source\x1a\x7f\n\rGroundingSpec\x12n\n\x11grounding_sources\x18\x01 \x03(\x0b2S.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest.GroundingSource\x1a1\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x98\x10\n\x1fGenerateGroundedContentResponse\x12b\n\ncandidates\x18\x01 \x03(\x0b2N.google.cloud.discoveryengine.v1beta.GenerateGroundedContentResponse.Candidate\x1a\x90\x0f\n\tCandidate\x12\r\n\x05index\x18\x01 \x01(\x05\x12O\n\x07content\x18\x02 \x01(\x0b2>.google.cloud.discoveryengine.v1beta.GroundedGenerationContent\x12\x1c\n\x0fgrounding_score\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12|\n\x12grounding_metadata\x18\x04 \x01(\x0b2`.google.cloud.discoveryengine.v1beta.GenerateGroundedContentResponse.Candidate.GroundingMetadata\x1a\xf2\x0c\n\x11GroundingMetadata\x12\x8e\x01\n\x12retrieval_metadata\x18\x05 \x03(\x0b2r.google.cloud.discoveryengine.v1beta.GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata\x12F\n\x0esupport_chunks\x18\x01 \x03(\x0b2..google.cloud.discoveryengine.v1beta.FactChunk\x12\x1a\n\x12web_search_queries\x18\x03 \x03(\t\x12\x8d\x01\n\x12search_entry_point\x18\x04 \x01(\x0b2q.google.cloud.discoveryengine.v1beta.GenerateGroundedContentResponse.Candidate.GroundingMetadata.SearchEntryPoint\x12\x8c\x01\n\x11grounding_support\x18\x02 \x03(\x0b2q.google.cloud.discoveryengine.v1beta.GenerateGroundedContentResponse.Candidate.GroundingMetadata.GroundingSupport\x1a\xaf\x03\n\x11RetrievalMetadata\x12\x89\x01\n\x06source\x18\x01 \x01(\x0e2y.google.cloud.discoveryengine.v1beta.GenerateGroundedContentResponse.Candidate.GroundingMetadata.RetrievalMetadata.Source\x12\x9d\x01\n\x1adynamic_retrieval_metadata\x18\x02 \x01(\x0b2y.google.cloud.discoveryengine.v1beta.GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalMetadata"n\n\x06Source\x12\x16\n\x12SOURCE_UNSPECIFIED\x10\x00\x12\x14\n\x10VERTEX_AI_SEARCH\x10\x01\x12\x11\n\rGOOGLE_SEARCH\x10\x03\x12\x12\n\x0eINLINE_CONTENT\x10\x02\x12\x0f\n\x0bGOOGLE_MAPS\x10\x04\x1a\xbc\x01\n\x18DynamicRetrievalMetadata\x12\x9f\x01\n\x12predictor_metadata\x18\x01 \x01(\x0b2\x82\x01.google.cloud.discoveryengine.v1beta.GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata\x1a\xa2\x02\n!DynamicRetrievalPredictorMetadata\x12\x9c\x01\n\x07version\x18\x01 \x01(\x0e2\x8a\x01.google.cloud.discoveryengine.v1beta.GenerateGroundedContentResponse.Candidate.GroundingMetadata.DynamicRetrievalPredictorMetadata.Version\x12\x17\n\nprediction\x18\x02 \x01(\x02H\x00\x88\x01\x01"6\n\x07Version\x12\x17\n\x13VERSION_UNSPECIFIED\x10\x00\x12\x12\n\x0eV1_INDEPENDENT\x10\x01B\r\n\x0b_prediction\x1a>\n\x10SearchEntryPoint\x12\x18\n\x10rendered_content\x18\x01 \x01(\t\x12\x10\n\x08sdk_blob\x18\x02 \x01(\x0c\x1as\n\x10GroundingSupport\x12\x12\n\nclaim_text\x18\x01 \x01(\t\x12\x1d\n\x15support_chunk_indices\x18\x03 \x03(\x05\x12\x1a\n\rsupport_score\x18\x02 \x01(\x02H\x00\x88\x01\x01B\x10\n\x0e_support_scoreB\x12\n\x10_grounding_score"L\n\x12CheckGroundingSpec\x12\x1f\n\x12citation_threshold\x18\x01 \x01(\x01H\x00\x88\x01\x01B\x15\n\x13_citation_threshold"\xab\x03\n\x15CheckGroundingRequest\x12P\n\x10grounding_config\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.discoveryengine.googleapis.com/GroundingConfig\x12\x18\n\x10answer_candidate\x18\x02 \x01(\t\x12A\n\x05facts\x18\x03 \x03(\x0b22.google.cloud.discoveryengine.v1beta.GroundingFact\x12O\n\x0egrounding_spec\x18\x04 \x01(\x0b27.google.cloud.discoveryengine.v1beta.CheckGroundingSpec\x12_\n\x0buser_labels\x18\x05 \x03(\x0b2J.google.cloud.discoveryengine.v1beta.CheckGroundingRequest.UserLabelsEntry\x1a1\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xbc\x04\n\x16CheckGroundingResponse\x12\x1a\n\rsupport_score\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12D\n\x0ccited_chunks\x18\x03 \x03(\x0b2..google.cloud.discoveryengine.v1beta.FactChunk\x12h\n\x0bcited_facts\x18\x06 \x03(\x0b2S.google.cloud.discoveryengine.v1beta.CheckGroundingResponse.CheckGroundingFactChunk\x12Q\n\x06claims\x18\x04 \x03(\x0b2A.google.cloud.discoveryengine.v1beta.CheckGroundingResponse.Claim\x1a-\n\x17CheckGroundingFactChunk\x12\x12\n\nchunk_text\x18\x01 \x01(\t\x1a\xc1\x01\n\x05Claim\x12\x16\n\tstart_pos\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07end_pos\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x12\n\nclaim_text\x18\x03 \x01(\t\x12\x18\n\x10citation_indices\x18\x04 \x03(\x05\x12%\n\x18grounding_check_required\x18\x06 \x01(\x08H\x02\x88\x01\x01B\x0c\n\n_start_posB\n\n\x08_end_posB\x1b\n\x19_grounding_check_requiredB\x10\n\x0e_support_score2\xcc\x06\n\x19GroundedGenerationService\x12\x82\x02\n\x1dStreamGenerateGroundedContent\x12C.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest\x1aD.google.cloud.discoveryengine.v1beta.GenerateGroundedContentResponse"R\x82\xd3\xe4\x93\x02L"G/v1beta/{location=projects/*/locations/*}:streamGenerateGroundedContent:\x01*(\x010\x01\x12\xf2\x01\n\x17GenerateGroundedContent\x12C.google.cloud.discoveryengine.v1beta.GenerateGroundedContentRequest\x1aD.google.cloud.discoveryengine.v1beta.GenerateGroundedContentResponse"L\x82\xd3\xe4\x93\x02F"A/v1beta/{location=projects/*/locations/*}:generateGroundedContent:\x01*\x12\xe0\x01\n\x0eCheckGrounding\x12:.google.cloud.discoveryengine.v1beta.CheckGroundingRequest\x1a;.google.cloud.discoveryengine.v1beta.CheckGroundingResponse"U\x82\xd3\xe4\x93\x02O"J/v1beta/{grounding_config=projects/*/locations/*/groundingConfigs/*}:check:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa5\x02\n\'com.google.cloud.discoveryengine.v1betaB\x1eGroundedGenerationServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.grounded_generation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x1eGroundedGenerationServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_INLINESOURCE_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_INLINESOURCE_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_SEARCHSOURCE'].fields_by_name['serving_config']._loaded_options = None
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_SEARCHSOURCE'].fields_by_name['serving_config']._serialized_options = b'\xfaA.\n,discoveryengine.googleapis.com/ServingConfig'
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_GOOGLESEARCHSOURCE'].fields_by_name['dynamic_retrieval_config']._loaded_options = None
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_GOOGLESEARCHSOURCE'].fields_by_name['dynamic_retrieval_config']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_USERLABELSENTRY']._loaded_options = None
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_USERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_GENERATEGROUNDEDCONTENTREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_GENERATEGROUNDEDCONTENTREQUEST'].fields_by_name['location']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Location"
    _globals['_CHECKGROUNDINGREQUEST_USERLABELSENTRY']._loaded_options = None
    _globals['_CHECKGROUNDINGREQUEST_USERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CHECKGROUNDINGREQUEST'].fields_by_name['grounding_config']._loaded_options = None
    _globals['_CHECKGROUNDINGREQUEST'].fields_by_name['grounding_config']._serialized_options = b'\xe0A\x02\xfaA0\n.discoveryengine.googleapis.com/GroundingConfig'
    _globals['_GROUNDEDGENERATIONSERVICE']._loaded_options = None
    _globals['_GROUNDEDGENERATIONSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_GROUNDEDGENERATIONSERVICE'].methods_by_name['StreamGenerateGroundedContent']._loaded_options = None
    _globals['_GROUNDEDGENERATIONSERVICE'].methods_by_name['StreamGenerateGroundedContent']._serialized_options = b'\x82\xd3\xe4\x93\x02L"G/v1beta/{location=projects/*/locations/*}:streamGenerateGroundedContent:\x01*'
    _globals['_GROUNDEDGENERATIONSERVICE'].methods_by_name['GenerateGroundedContent']._loaded_options = None
    _globals['_GROUNDEDGENERATIONSERVICE'].methods_by_name['GenerateGroundedContent']._serialized_options = b'\x82\xd3\xe4\x93\x02F"A/v1beta/{location=projects/*/locations/*}:generateGroundedContent:\x01*'
    _globals['_GROUNDEDGENERATIONSERVICE'].methods_by_name['CheckGrounding']._loaded_options = None
    _globals['_GROUNDEDGENERATIONSERVICE'].methods_by_name['CheckGrounding']._serialized_options = b'\x82\xd3\xe4\x93\x02O"J/v1beta/{grounding_config=projects/*/locations/*/groundingConfigs/*}:check:\x01*'
    _globals['_GROUNDEDGENERATIONCONTENT']._serialized_start = 279
    _globals['_GROUNDEDGENERATIONCONTENT']._serialized_end = 436
    _globals['_GROUNDEDGENERATIONCONTENT_PART']._serialized_start = 406
    _globals['_GROUNDEDGENERATIONCONTENT_PART']._serialized_end = 436
    _globals['_GENERATEGROUNDEDCONTENTREQUEST']._serialized_start = 439
    _globals['_GENERATEGROUNDEDCONTENTREQUEST']._serialized_end = 3001
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GENERATIONSPEC']._serialized_start = 1037
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GENERATIONSPEC']._serialized_end = 1356
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_DYNAMICRETRIEVALCONFIGURATION']._serialized_start = 1359
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_DYNAMICRETRIEVALCONFIGURATION']._serialized_end = 1811
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_DYNAMICRETRIEVALCONFIGURATION_DYNAMICRETRIEVALPREDICTOR']._serialized_start = 1538
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_DYNAMICRETRIEVALCONFIGURATION_DYNAMICRETRIEVALPREDICTOR']._serialized_end = 1811
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_DYNAMICRETRIEVALCONFIGURATION_DYNAMICRETRIEVALPREDICTOR_VERSION']._serialized_start = 1743
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_DYNAMICRETRIEVALCONFIGURATION_DYNAMICRETRIEVALPREDICTOR_VERSION']._serialized_end = 1797
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE']._serialized_start = 1814
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE']._serialized_end = 2821
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_INLINESOURCE']._serialized_start = 2217
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_INLINESOURCE']._serialized_end = 2494
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_INLINESOURCE_ATTRIBUTESENTRY']._serialized_start = 2445
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_INLINESOURCE_ATTRIBUTESENTRY']._serialized_end = 2494
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_SEARCHSOURCE']._serialized_start = 2497
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_SEARCHSOURCE']._serialized_end = 2649
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_GOOGLESEARCHSOURCE']._serialized_start = 2652
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSOURCE_GOOGLESEARCHSOURCE']._serialized_end = 2811
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSPEC']._serialized_start = 2823
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_GROUNDINGSPEC']._serialized_end = 2950
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_USERLABELSENTRY']._serialized_start = 2952
    _globals['_GENERATEGROUNDEDCONTENTREQUEST_USERLABELSENTRY']._serialized_end = 3001
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE']._serialized_start = 3004
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE']._serialized_end = 5076
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE']._serialized_start = 3140
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE']._serialized_end = 5076
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA']._serialized_start = 3406
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA']._serialized_end = 5056
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_RETRIEVALMETADATA']._serialized_start = 3960
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_RETRIEVALMETADATA']._serialized_end = 4391
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_RETRIEVALMETADATA_SOURCE']._serialized_start = 4281
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_RETRIEVALMETADATA_SOURCE']._serialized_end = 4391
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_DYNAMICRETRIEVALMETADATA']._serialized_start = 4394
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_DYNAMICRETRIEVALMETADATA']._serialized_end = 4582
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_DYNAMICRETRIEVALPREDICTORMETADATA']._serialized_start = 4585
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_DYNAMICRETRIEVALPREDICTORMETADATA']._serialized_end = 4875
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_DYNAMICRETRIEVALPREDICTORMETADATA_VERSION']._serialized_start = 1743
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_DYNAMICRETRIEVALPREDICTORMETADATA_VERSION']._serialized_end = 1797
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_SEARCHENTRYPOINT']._serialized_start = 4877
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_SEARCHENTRYPOINT']._serialized_end = 4939
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_GROUNDINGSUPPORT']._serialized_start = 4941
    _globals['_GENERATEGROUNDEDCONTENTRESPONSE_CANDIDATE_GROUNDINGMETADATA_GROUNDINGSUPPORT']._serialized_end = 5056
    _globals['_CHECKGROUNDINGSPEC']._serialized_start = 5078
    _globals['_CHECKGROUNDINGSPEC']._serialized_end = 5154
    _globals['_CHECKGROUNDINGREQUEST']._serialized_start = 5157
    _globals['_CHECKGROUNDINGREQUEST']._serialized_end = 5584
    _globals['_CHECKGROUNDINGREQUEST_USERLABELSENTRY']._serialized_start = 2952
    _globals['_CHECKGROUNDINGREQUEST_USERLABELSENTRY']._serialized_end = 3001
    _globals['_CHECKGROUNDINGRESPONSE']._serialized_start = 5587
    _globals['_CHECKGROUNDINGRESPONSE']._serialized_end = 6159
    _globals['_CHECKGROUNDINGRESPONSE_CHECKGROUNDINGFACTCHUNK']._serialized_start = 5900
    _globals['_CHECKGROUNDINGRESPONSE_CHECKGROUNDINGFACTCHUNK']._serialized_end = 5945
    _globals['_CHECKGROUNDINGRESPONSE_CLAIM']._serialized_start = 5948
    _globals['_CHECKGROUNDINGRESPONSE_CLAIM']._serialized_end = 6141
    _globals['_GROUNDEDGENERATIONSERVICE']._serialized_start = 6162
    _globals['_GROUNDEDGENERATIONSERVICE']._serialized_end = 7006