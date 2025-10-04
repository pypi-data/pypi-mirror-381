"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/project_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import common_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_common__pb2
from .....google.cloud.retail.v2alpha import project_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_project__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/retail/v2alpha/project_service.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/retail/v2alpha/common.proto\x1a)google/cloud/retail/v2alpha/project.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto"N\n\x11GetProjectRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#retail.googleapis.com/RetailProject"R\n\x12AcceptTermsRequest\x12<\n\x07project\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#retail.googleapis.com/RetailProject"\x9f\x01\n\x15EnrollSolutionRequest\x12D\n\x07project\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12@\n\x08solution\x18\x02 \x01(\x0e2).google.cloud.retail.v2alpha.SolutionTypeB\x03\xe0A\x02"^\n\x16EnrollSolutionResponse\x12D\n\x11enrolled_solution\x18\x01 \x01(\x0e2).google.cloud.retail.v2alpha.SolutionType"\x18\n\x16EnrollSolutionMetadata"c\n\x1cListEnrolledSolutionsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project"f\n\x1dListEnrolledSolutionsResponse\x12E\n\x12enrolled_solutions\x18\x01 \x03(\x0e2).google.cloud.retail.v2alpha.SolutionType"T\n\x17GetLoggingConfigRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#retail.googleapis.com/LoggingConfig"\x96\x01\n\x1aUpdateLoggingConfigRequest\x12G\n\x0elogging_config\x18\x01 \x01(\x0b2*.google.cloud.retail.v2alpha.LoggingConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"P\n\x15GetAlertConfigRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!retail.googleapis.com/AlertConfig"\x90\x01\n\x18UpdateAlertConfigRequest\x12C\n\x0calert_config\x18\x01 \x01(\x0b2(.google.cloud.retail.v2alpha.AlertConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask2\xab\r\n\x0eProjectService\x12\x9b\x01\n\nGetProject\x12..google.cloud.retail.v2alpha.GetProjectRequest\x1a$.google.cloud.retail.v2alpha.Project"7\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v2alpha/{name=projects/*/retailProject}\x12\xb2\x01\n\x0bAcceptTerms\x12/.google.cloud.retail.v2alpha.AcceptTermsRequest\x1a$.google.cloud.retail.v2alpha.Project"L\xdaA\x07project\x82\xd3\xe4\x93\x02<"7/v2alpha/{project=projects/*/retailProject}:acceptTerms:\x01*\x12\x88\x02\n\x0eEnrollSolution\x122.google.cloud.retail.v2alpha.EnrollSolutionRequest\x1a\x1d.google.longrunning.Operation"\xa2\x01\xcaAh\n2google.cloud.retail.v2alpha.EnrollSolutionResponse\x122google.cloud.retail.v2alpha.EnrollSolutionMetadata\x82\xd3\xe4\x93\x021",/v2alpha/{project=projects/*}:enrollSolution:\x01*\x12\xcf\x01\n\x15ListEnrolledSolutions\x129.google.cloud.retail.v2alpha.ListEnrolledSolutionsRequest\x1a:.google.cloud.retail.v2alpha.ListEnrolledSolutionsResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v2alpha/{parent=projects/*}:enrolledSolutions\x12\xad\x01\n\x10GetLoggingConfig\x124.google.cloud.retail.v2alpha.GetLoggingConfigRequest\x1a*.google.cloud.retail.v2alpha.LoggingConfig"7\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v2alpha/{name=projects/*/loggingConfig}\x12\xe8\x01\n\x13UpdateLoggingConfig\x127.google.cloud.retail.v2alpha.UpdateLoggingConfigRequest\x1a*.google.cloud.retail.v2alpha.LoggingConfig"l\xdaA\x1alogging_config,update_mask\x82\xd3\xe4\x93\x02I27/v2alpha/{logging_config.name=projects/*/loggingConfig}:\x0elogging_config\x12\xa5\x01\n\x0eGetAlertConfig\x122.google.cloud.retail.v2alpha.GetAlertConfigRequest\x1a(.google.cloud.retail.v2alpha.AlertConfig"5\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v2alpha/{name=projects/*/alertConfig}\x12\xda\x01\n\x11UpdateAlertConfig\x125.google.cloud.retail.v2alpha.UpdateAlertConfigRequest\x1a(.google.cloud.retail.v2alpha.AlertConfig"d\xdaA\x18alert_config,update_mask\x82\xd3\xe4\x93\x02C23/v2alpha/{alert_config.name=projects/*/alertConfig}:\x0calert_config\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd7\x01\n\x1fcom.google.cloud.retail.v2alphaB\x13ProjectServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.project_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x13ProjectServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_GETPROJECTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPROJECTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#retail.googleapis.com/RetailProject'
    _globals['_ACCEPTTERMSREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_ACCEPTTERMSREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02\xfaA%\n#retail.googleapis.com/RetailProject'
    _globals['_ENROLLSOLUTIONREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_ENROLLSOLUTIONREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_ENROLLSOLUTIONREQUEST'].fields_by_name['solution']._loaded_options = None
    _globals['_ENROLLSOLUTIONREQUEST'].fields_by_name['solution']._serialized_options = b'\xe0A\x02'
    _globals['_LISTENROLLEDSOLUTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENROLLEDSOLUTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_GETLOGGINGCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETLOGGINGCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#retail.googleapis.com/LoggingConfig'
    _globals['_UPDATELOGGINGCONFIGREQUEST'].fields_by_name['logging_config']._loaded_options = None
    _globals['_UPDATELOGGINGCONFIGREQUEST'].fields_by_name['logging_config']._serialized_options = b'\xe0A\x02'
    _globals['_GETALERTCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETALERTCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!retail.googleapis.com/AlertConfig'
    _globals['_UPDATEALERTCONFIGREQUEST'].fields_by_name['alert_config']._loaded_options = None
    _globals['_UPDATEALERTCONFIGREQUEST'].fields_by_name['alert_config']._serialized_options = b'\xe0A\x02'
    _globals['_PROJECTSERVICE']._loaded_options = None
    _globals['_PROJECTSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PROJECTSERVICE'].methods_by_name['GetProject']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['GetProject']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v2alpha/{name=projects/*/retailProject}'
    _globals['_PROJECTSERVICE'].methods_by_name['AcceptTerms']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['AcceptTerms']._serialized_options = b'\xdaA\x07project\x82\xd3\xe4\x93\x02<"7/v2alpha/{project=projects/*/retailProject}:acceptTerms:\x01*'
    _globals['_PROJECTSERVICE'].methods_by_name['EnrollSolution']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['EnrollSolution']._serialized_options = b'\xcaAh\n2google.cloud.retail.v2alpha.EnrollSolutionResponse\x122google.cloud.retail.v2alpha.EnrollSolutionMetadata\x82\xd3\xe4\x93\x021",/v2alpha/{project=projects/*}:enrollSolution:\x01*'
    _globals['_PROJECTSERVICE'].methods_by_name['ListEnrolledSolutions']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['ListEnrolledSolutions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v2alpha/{parent=projects/*}:enrolledSolutions'
    _globals['_PROJECTSERVICE'].methods_by_name['GetLoggingConfig']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['GetLoggingConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v2alpha/{name=projects/*/loggingConfig}'
    _globals['_PROJECTSERVICE'].methods_by_name['UpdateLoggingConfig']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['UpdateLoggingConfig']._serialized_options = b'\xdaA\x1alogging_config,update_mask\x82\xd3\xe4\x93\x02I27/v2alpha/{logging_config.name=projects/*/loggingConfig}:\x0elogging_config'
    _globals['_PROJECTSERVICE'].methods_by_name['GetAlertConfig']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['GetAlertConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v2alpha/{name=projects/*/alertConfig}'
    _globals['_PROJECTSERVICE'].methods_by_name['UpdateAlertConfig']._loaded_options = None
    _globals['_PROJECTSERVICE'].methods_by_name['UpdateAlertConfig']._serialized_options = b'\xdaA\x18alert_config,update_mask\x82\xd3\xe4\x93\x02C23/v2alpha/{alert_config.name=projects/*/alertConfig}:\x0calert_config'
    _globals['_GETPROJECTREQUEST']._serialized_start = 353
    _globals['_GETPROJECTREQUEST']._serialized_end = 431
    _globals['_ACCEPTTERMSREQUEST']._serialized_start = 433
    _globals['_ACCEPTTERMSREQUEST']._serialized_end = 515
    _globals['_ENROLLSOLUTIONREQUEST']._serialized_start = 518
    _globals['_ENROLLSOLUTIONREQUEST']._serialized_end = 677
    _globals['_ENROLLSOLUTIONRESPONSE']._serialized_start = 679
    _globals['_ENROLLSOLUTIONRESPONSE']._serialized_end = 773
    _globals['_ENROLLSOLUTIONMETADATA']._serialized_start = 775
    _globals['_ENROLLSOLUTIONMETADATA']._serialized_end = 799
    _globals['_LISTENROLLEDSOLUTIONSREQUEST']._serialized_start = 801
    _globals['_LISTENROLLEDSOLUTIONSREQUEST']._serialized_end = 900
    _globals['_LISTENROLLEDSOLUTIONSRESPONSE']._serialized_start = 902
    _globals['_LISTENROLLEDSOLUTIONSRESPONSE']._serialized_end = 1004
    _globals['_GETLOGGINGCONFIGREQUEST']._serialized_start = 1006
    _globals['_GETLOGGINGCONFIGREQUEST']._serialized_end = 1090
    _globals['_UPDATELOGGINGCONFIGREQUEST']._serialized_start = 1093
    _globals['_UPDATELOGGINGCONFIGREQUEST']._serialized_end = 1243
    _globals['_GETALERTCONFIGREQUEST']._serialized_start = 1245
    _globals['_GETALERTCONFIGREQUEST']._serialized_end = 1325
    _globals['_UPDATEALERTCONFIGREQUEST']._serialized_start = 1328
    _globals['_UPDATEALERTCONFIGREQUEST']._serialized_end = 1472
    _globals['_PROJECTSERVICE']._serialized_start = 1475
    _globals['_PROJECTSERVICE']._serialized_end = 3182