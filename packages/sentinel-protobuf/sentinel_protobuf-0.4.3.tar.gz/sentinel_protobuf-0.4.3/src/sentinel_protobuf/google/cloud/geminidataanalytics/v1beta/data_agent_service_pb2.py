"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/geminidataanalytics/v1beta/data_agent_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.geminidataanalytics.v1beta import data_agent_pb2 as google_dot_cloud_dot_geminidataanalytics_dot_v1beta_dot_data__agent__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/cloud/geminidataanalytics/v1beta/data_agent_service.proto\x12\'google.cloud.geminidataanalytics.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/geminidataanalytics/v1beta/data_agent.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd5\x01\n\x15ListDataAgentsRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,geminidataanalytics.googleapis.com/DataAgent\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cshow_deleted\x18\x06 \x01(\x08B\x03\xe0A\x01"\x94\x01\n\x16ListDataAgentsResponse\x12G\n\x0bdata_agents\x18\x01 \x03(\x0b22.google.cloud.geminidataanalytics.v1beta.DataAgent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x18\n\x0bunreachable\x18\x03 \x03(\tB\x03\xe0A\x06"\xb7\x03\n\x1fListAccessibleDataAgentsRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,geminidataanalytics.googleapis.com/DataAgent\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cshow_deleted\x18\x06 \x01(\x08B\x03\xe0A\x01\x12s\n\x0ecreator_filter\x18\x07 \x01(\x0e2V.google.cloud.geminidataanalytics.v1beta.ListAccessibleDataAgentsRequest.CreatorFilterB\x03\xe0A\x01"a\n\rCreatorFilter\x12\x1e\n\x1aCREATOR_FILTER_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x10\n\x0cCREATOR_ONLY\x10\x02\x12\x14\n\x10NOT_CREATOR_ONLY\x10\x03"\x9e\x01\n ListAccessibleDataAgentsResponse\x12G\n\x0bdata_agents\x18\x01 \x03(\x0b22.google.cloud.geminidataanalytics.v1beta.DataAgent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x18\n\x0bunreachable\x18\x03 \x03(\tB\x03\xe0A\x06"Y\n\x13GetDataAgentRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,geminidataanalytics.googleapis.com/DataAgent"\xe8\x01\n\x16CreateDataAgentRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,geminidataanalytics.googleapis.com/DataAgent\x12\x1a\n\rdata_agent_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12K\n\ndata_agent\x18\x03 \x01(\x0b22.google.cloud.geminidataanalytics.v1beta.DataAgentB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xbc\x01\n\x16UpdateDataAgentRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12K\n\ndata_agent\x18\x02 \x01(\x0b22.google.cloud.geminidataanalytics.v1beta.DataAgentB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"}\n\x16DeleteDataAgentRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,geminidataanalytics.googleapis.com/DataAgent\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xc3\x0e\n\x10DataAgentService\x12\xd6\x01\n\x0eListDataAgents\x12>.google.cloud.geminidataanalytics.v1beta.ListDataAgentsRequest\x1a?.google.cloud.geminidataanalytics.v1beta.ListDataAgentsResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1beta/{parent=projects/*/locations/*}/dataAgents\x12\x83\x02\n\x18ListAccessibleDataAgents\x12H.google.cloud.geminidataanalytics.v1beta.ListAccessibleDataAgentsRequest\x1aI.google.cloud.geminidataanalytics.v1beta.ListAccessibleDataAgentsResponse"R\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1beta/{parent=projects/*/locations/*}/dataAgents:listAccessible\x12\xc3\x01\n\x0cGetDataAgent\x12<.google.cloud.geminidataanalytics.v1beta.GetDataAgentRequest\x1a2.google.cloud.geminidataanalytics.v1beta.DataAgent"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1beta/{name=projects/*/locations/*/dataAgents/*}\x12\xfd\x01\n\x0fCreateDataAgent\x12?.google.cloud.geminidataanalytics.v1beta.CreateDataAgentRequest\x1a\x1d.google.longrunning.Operation"\x89\x01\xcaA\x1e\n\tDataAgent\x12\x11OperationMetadata\xdaA\x1fparent,data_agent,data_agent_id\x82\xd3\xe4\x93\x02@"2/v1beta/{parent=projects/*/locations/*}/dataAgents:\ndata_agent\x12\xff\x01\n\x0fUpdateDataAgent\x12?.google.cloud.geminidataanalytics.v1beta.UpdateDataAgentRequest\x1a\x1d.google.longrunning.Operation"\x8b\x01\xcaA\x1e\n\tDataAgent\x12\x11OperationMetadata\xdaA\x16data_agent,update_mask\x82\xd3\xe4\x93\x02K2=/v1beta/{data_agent.name=projects/*/locations/*/dataAgents/*}:\ndata_agent\x12\xe1\x01\n\x0fDeleteDataAgent\x12?.google.cloud.geminidataanalytics.v1beta.DeleteDataAgentRequest\x1a\x1d.google.longrunning.Operation"n\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1beta/{name=projects/*/locations/*/dataAgents/*}\x12\xa4\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"Y\xdaA\x08resource\x82\xd3\xe4\x93\x02H"C/v1beta/{resource=projects/*/locations/*/dataAgents/*}:getIamPolicy:\x01*\x12\xa4\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"Y\xdaA\x08resource\x82\xd3\xe4\x93\x02H"C/v1beta/{resource=projects/*/locations/*/dataAgents/*}:setIamPolicy:\x01*\x1aV\xcaA"geminidataanalytics.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa6\x02\n+com.google.cloud.geminidataanalytics.v1betaB\x15DataAgentServiceProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02\'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02\'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.geminidataanalytics.v1beta.data_agent_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.geminidataanalytics.v1betaB\x15DataAgentServiceProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1beta"
    _globals['_LISTDATAAGENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATAAGENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,geminidataanalytics.googleapis.com/DataAgent'
    _globals['_LISTDATAAGENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDATAAGENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATAAGENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDATAAGENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATAAGENTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTDATAAGENTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATAAGENTSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTDATAAGENTSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATAAGENTSREQUEST'].fields_by_name['show_deleted']._loaded_options = None
    _globals['_LISTDATAAGENTSREQUEST'].fields_by_name['show_deleted']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATAAGENTSRESPONSE'].fields_by_name['unreachable']._loaded_options = None
    _globals['_LISTDATAAGENTSRESPONSE'].fields_by_name['unreachable']._serialized_options = b'\xe0A\x06'
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,geminidataanalytics.googleapis.com/DataAgent'
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['show_deleted']._loaded_options = None
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['show_deleted']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['creator_filter']._loaded_options = None
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST'].fields_by_name['creator_filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCESSIBLEDATAAGENTSRESPONSE'].fields_by_name['unreachable']._loaded_options = None
    _globals['_LISTACCESSIBLEDATAAGENTSRESPONSE'].fields_by_name['unreachable']._serialized_options = b'\xe0A\x06'
    _globals['_GETDATAAGENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATAAGENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,geminidataanalytics.googleapis.com/DataAgent'
    _globals['_CREATEDATAAGENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATAAGENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,geminidataanalytics.googleapis.com/DataAgent'
    _globals['_CREATEDATAAGENTREQUEST'].fields_by_name['data_agent_id']._loaded_options = None
    _globals['_CREATEDATAAGENTREQUEST'].fields_by_name['data_agent_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEDATAAGENTREQUEST'].fields_by_name['data_agent']._loaded_options = None
    _globals['_CREATEDATAAGENTREQUEST'].fields_by_name['data_agent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATAAGENTREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEDATAAGENTREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_UPDATEDATAAGENTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDATAAGENTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEDATAAGENTREQUEST'].fields_by_name['data_agent']._loaded_options = None
    _globals['_UPDATEDATAAGENTREQUEST'].fields_by_name['data_agent']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATAAGENTREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEDATAAGENTREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_DELETEDATAAGENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATAAGENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,geminidataanalytics.googleapis.com/DataAgent'
    _globals['_DELETEDATAAGENTREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEDATAAGENTREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_DATAAGENTSERVICE']._loaded_options = None
    _globals['_DATAAGENTSERVICE']._serialized_options = b'\xcaA"geminidataanalytics.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATAAGENTSERVICE'].methods_by_name['ListDataAgents']._loaded_options = None
    _globals['_DATAAGENTSERVICE'].methods_by_name['ListDataAgents']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1beta/{parent=projects/*/locations/*}/dataAgents'
    _globals['_DATAAGENTSERVICE'].methods_by_name['ListAccessibleDataAgents']._loaded_options = None
    _globals['_DATAAGENTSERVICE'].methods_by_name['ListAccessibleDataAgents']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1beta/{parent=projects/*/locations/*}/dataAgents:listAccessible'
    _globals['_DATAAGENTSERVICE'].methods_by_name['GetDataAgent']._loaded_options = None
    _globals['_DATAAGENTSERVICE'].methods_by_name['GetDataAgent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1beta/{name=projects/*/locations/*/dataAgents/*}'
    _globals['_DATAAGENTSERVICE'].methods_by_name['CreateDataAgent']._loaded_options = None
    _globals['_DATAAGENTSERVICE'].methods_by_name['CreateDataAgent']._serialized_options = b'\xcaA\x1e\n\tDataAgent\x12\x11OperationMetadata\xdaA\x1fparent,data_agent,data_agent_id\x82\xd3\xe4\x93\x02@"2/v1beta/{parent=projects/*/locations/*}/dataAgents:\ndata_agent'
    _globals['_DATAAGENTSERVICE'].methods_by_name['UpdateDataAgent']._loaded_options = None
    _globals['_DATAAGENTSERVICE'].methods_by_name['UpdateDataAgent']._serialized_options = b'\xcaA\x1e\n\tDataAgent\x12\x11OperationMetadata\xdaA\x16data_agent,update_mask\x82\xd3\xe4\x93\x02K2=/v1beta/{data_agent.name=projects/*/locations/*/dataAgents/*}:\ndata_agent'
    _globals['_DATAAGENTSERVICE'].methods_by_name['DeleteDataAgent']._loaded_options = None
    _globals['_DATAAGENTSERVICE'].methods_by_name['DeleteDataAgent']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1beta/{name=projects/*/locations/*/dataAgents/*}'
    _globals['_DATAAGENTSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_DATAAGENTSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02H"C/v1beta/{resource=projects/*/locations/*/dataAgents/*}:getIamPolicy:\x01*'
    _globals['_DATAAGENTSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_DATAAGENTSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02H"C/v1beta/{resource=projects/*/locations/*/dataAgents/*}:setIamPolicy:\x01*'
    _globals['_LISTDATAAGENTSREQUEST']._serialized_start = 505
    _globals['_LISTDATAAGENTSREQUEST']._serialized_end = 718
    _globals['_LISTDATAAGENTSRESPONSE']._serialized_start = 721
    _globals['_LISTDATAAGENTSRESPONSE']._serialized_end = 869
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST']._serialized_start = 872
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST']._serialized_end = 1311
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST_CREATORFILTER']._serialized_start = 1214
    _globals['_LISTACCESSIBLEDATAAGENTSREQUEST_CREATORFILTER']._serialized_end = 1311
    _globals['_LISTACCESSIBLEDATAAGENTSRESPONSE']._serialized_start = 1314
    _globals['_LISTACCESSIBLEDATAAGENTSRESPONSE']._serialized_end = 1472
    _globals['_GETDATAAGENTREQUEST']._serialized_start = 1474
    _globals['_GETDATAAGENTREQUEST']._serialized_end = 1563
    _globals['_CREATEDATAAGENTREQUEST']._serialized_start = 1566
    _globals['_CREATEDATAAGENTREQUEST']._serialized_end = 1798
    _globals['_UPDATEDATAAGENTREQUEST']._serialized_start = 1801
    _globals['_UPDATEDATAAGENTREQUEST']._serialized_end = 1989
    _globals['_DELETEDATAAGENTREQUEST']._serialized_start = 1991
    _globals['_DELETEDATAAGENTREQUEST']._serialized_end = 2116
    _globals['_OPERATIONMETADATA']._serialized_start = 2119
    _globals['_OPERATIONMETADATA']._serialized_end = 2375
    _globals['_DATAAGENTSERVICE']._serialized_start = 2378
    _globals['_DATAAGENTSERVICE']._serialized_end = 4237