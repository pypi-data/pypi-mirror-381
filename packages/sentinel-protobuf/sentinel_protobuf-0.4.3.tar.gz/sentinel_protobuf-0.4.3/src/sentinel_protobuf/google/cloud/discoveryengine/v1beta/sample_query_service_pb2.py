"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/sample_query_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import import_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_import__config__pb2
from .....google.cloud.discoveryengine.v1beta import sample_query_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_sample__query__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/discoveryengine/v1beta/sample_query_service.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a7google/cloud/discoveryengine/v1beta/import_config.proto\x1a6google/cloud/discoveryengine/v1beta/sample_query.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"Y\n\x15GetSampleQueryRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*discoveryengine.googleapis.com/SampleQuery"\x88\x01\n\x18ListSampleQueriesRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-discoveryengine.googleapis.com/SampleQuerySet\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"~\n\x19ListSampleQueriesResponse\x12H\n\x0esample_queries\x18\x01 \x03(\x0b20.google.cloud.discoveryengine.v1beta.SampleQuery\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xcc\x01\n\x18CreateSampleQueryRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-discoveryengine.googleapis.com/SampleQuerySet\x12K\n\x0csample_query\x18\x02 \x01(\x0b20.google.cloud.discoveryengine.v1beta.SampleQueryB\x03\xe0A\x02\x12\x1c\n\x0fsample_query_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x98\x01\n\x18UpdateSampleQueryRequest\x12K\n\x0csample_query\x18\x01 \x01(\x0b20.google.cloud.discoveryengine.v1beta.SampleQueryB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\\\n\x18DeleteSampleQueryRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*discoveryengine.googleapis.com/SampleQuery2\xeb\x0c\n\x12SampleQueryService\x12\xd6\x01\n\x0eGetSampleQuery\x12:.google.cloud.discoveryengine.v1beta.GetSampleQueryRequest\x1a0.google.cloud.discoveryengine.v1beta.SampleQuery"V\xdaA\x04name\x82\xd3\xe4\x93\x02I\x12G/v1beta/{name=projects/*/locations/*/sampleQuerySets/*/sampleQueries/*}\x12\xec\x01\n\x11ListSampleQueries\x12=.google.cloud.discoveryengine.v1beta.ListSampleQueriesRequest\x1a>.google.cloud.discoveryengine.v1beta.ListSampleQueriesResponse"X\xdaA\x06parent\x82\xd3\xe4\x93\x02I\x12G/v1beta/{parent=projects/*/locations/*/sampleQuerySets/*}/sampleQueries\x12\x8a\x02\n\x11CreateSampleQuery\x12=.google.cloud.discoveryengine.v1beta.CreateSampleQueryRequest\x1a0.google.cloud.discoveryengine.v1beta.SampleQuery"\x83\x01\xdaA#parent,sample_query,sample_query_id\x82\xd3\xe4\x93\x02W"G/v1beta/{parent=projects/*/locations/*/sampleQuerySets/*}/sampleQueries:\x0csample_query\x12\x8c\x02\n\x11UpdateSampleQuery\x12=.google.cloud.discoveryengine.v1beta.UpdateSampleQueryRequest\x1a0.google.cloud.discoveryengine.v1beta.SampleQuery"\x85\x01\xdaA\x18sample_query,update_mask\x82\xd3\xe4\x93\x02d2T/v1beta/{sample_query.name=projects/*/locations/*/sampleQuerySets/*/sampleQueries/*}:\x0csample_query\x12\xc2\x01\n\x11DeleteSampleQuery\x12=.google.cloud.discoveryengine.v1beta.DeleteSampleQueryRequest\x1a\x16.google.protobuf.Empty"V\xdaA\x04name\x82\xd3\xe4\x93\x02I*G/v1beta/{name=projects/*/locations/*/sampleQuerySets/*/sampleQueries/*}\x12\xd7\x02\n\x13ImportSampleQueries\x12?.google.cloud.discoveryengine.v1beta.ImportSampleQueriesRequest\x1a\x1d.google.longrunning.Operation"\xdf\x01\xcaA\x82\x01\n?google.cloud.discoveryengine.v1beta.ImportSampleQueriesResponse\x12?google.cloud.discoveryengine.v1beta.ImportSampleQueriesMetadata\x82\xd3\xe4\x93\x02S"N/v1beta/{parent=projects/*/locations/*/sampleQuerySets/*}/sampleQueries:import:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9e\x02\n\'com.google.cloud.discoveryengine.v1betaB\x17SampleQueryServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.sample_query_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x17SampleQueryServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_GETSAMPLEQUERYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSAMPLEQUERYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*discoveryengine.googleapis.com/SampleQuery'
    _globals['_LISTSAMPLEQUERIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSAMPLEQUERIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\n-discoveryengine.googleapis.com/SampleQuerySet'
    _globals['_CREATESAMPLEQUERYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESAMPLEQUERYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\n-discoveryengine.googleapis.com/SampleQuerySet'
    _globals['_CREATESAMPLEQUERYREQUEST'].fields_by_name['sample_query']._loaded_options = None
    _globals['_CREATESAMPLEQUERYREQUEST'].fields_by_name['sample_query']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESAMPLEQUERYREQUEST'].fields_by_name['sample_query_id']._loaded_options = None
    _globals['_CREATESAMPLEQUERYREQUEST'].fields_by_name['sample_query_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESAMPLEQUERYREQUEST'].fields_by_name['sample_query']._loaded_options = None
    _globals['_UPDATESAMPLEQUERYREQUEST'].fields_by_name['sample_query']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESAMPLEQUERYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESAMPLEQUERYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*discoveryengine.googleapis.com/SampleQuery'
    _globals['_SAMPLEQUERYSERVICE']._loaded_options = None
    _globals['_SAMPLEQUERYSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SAMPLEQUERYSERVICE'].methods_by_name['GetSampleQuery']._loaded_options = None
    _globals['_SAMPLEQUERYSERVICE'].methods_by_name['GetSampleQuery']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02I\x12G/v1beta/{name=projects/*/locations/*/sampleQuerySets/*/sampleQueries/*}'
    _globals['_SAMPLEQUERYSERVICE'].methods_by_name['ListSampleQueries']._loaded_options = None
    _globals['_SAMPLEQUERYSERVICE'].methods_by_name['ListSampleQueries']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02I\x12G/v1beta/{parent=projects/*/locations/*/sampleQuerySets/*}/sampleQueries'
    _globals['_SAMPLEQUERYSERVICE'].methods_by_name['CreateSampleQuery']._loaded_options = None
    _globals['_SAMPLEQUERYSERVICE'].methods_by_name['CreateSampleQuery']._serialized_options = b'\xdaA#parent,sample_query,sample_query_id\x82\xd3\xe4\x93\x02W"G/v1beta/{parent=projects/*/locations/*/sampleQuerySets/*}/sampleQueries:\x0csample_query'
    _globals['_SAMPLEQUERYSERVICE'].methods_by_name['UpdateSampleQuery']._loaded_options = None
    _globals['_SAMPLEQUERYSERVICE'].methods_by_name['UpdateSampleQuery']._serialized_options = b'\xdaA\x18sample_query,update_mask\x82\xd3\xe4\x93\x02d2T/v1beta/{sample_query.name=projects/*/locations/*/sampleQuerySets/*/sampleQueries/*}:\x0csample_query'
    _globals['_SAMPLEQUERYSERVICE'].methods_by_name['DeleteSampleQuery']._loaded_options = None
    _globals['_SAMPLEQUERYSERVICE'].methods_by_name['DeleteSampleQuery']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02I*G/v1beta/{name=projects/*/locations/*/sampleQuerySets/*/sampleQueries/*}'
    _globals['_SAMPLEQUERYSERVICE'].methods_by_name['ImportSampleQueries']._loaded_options = None
    _globals['_SAMPLEQUERYSERVICE'].methods_by_name['ImportSampleQueries']._serialized_options = b'\xcaA\x82\x01\n?google.cloud.discoveryengine.v1beta.ImportSampleQueriesResponse\x12?google.cloud.discoveryengine.v1beta.ImportSampleQueriesMetadata\x82\xd3\xe4\x93\x02S"N/v1beta/{parent=projects/*/locations/*/sampleQuerySets/*}/sampleQueries:import:\x01*'
    _globals['_GETSAMPLEQUERYREQUEST']._serialized_start = 431
    _globals['_GETSAMPLEQUERYREQUEST']._serialized_end = 520
    _globals['_LISTSAMPLEQUERIESREQUEST']._serialized_start = 523
    _globals['_LISTSAMPLEQUERIESREQUEST']._serialized_end = 659
    _globals['_LISTSAMPLEQUERIESRESPONSE']._serialized_start = 661
    _globals['_LISTSAMPLEQUERIESRESPONSE']._serialized_end = 787
    _globals['_CREATESAMPLEQUERYREQUEST']._serialized_start = 790
    _globals['_CREATESAMPLEQUERYREQUEST']._serialized_end = 994
    _globals['_UPDATESAMPLEQUERYREQUEST']._serialized_start = 997
    _globals['_UPDATESAMPLEQUERYREQUEST']._serialized_end = 1149
    _globals['_DELETESAMPLEQUERYREQUEST']._serialized_start = 1151
    _globals['_DELETESAMPLEQUERYREQUEST']._serialized_end = 1243
    _globals['_SAMPLEQUERYSERVICE']._serialized_start = 1246
    _globals['_SAMPLEQUERYSERVICE']._serialized_end = 2889