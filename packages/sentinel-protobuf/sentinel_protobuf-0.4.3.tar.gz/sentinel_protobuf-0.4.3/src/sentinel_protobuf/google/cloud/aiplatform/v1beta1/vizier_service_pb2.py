"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/vizier_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.cloud.aiplatform.v1beta1 import study_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_study__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/aiplatform/v1beta1/vizier_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a+google/cloud/aiplatform/v1beta1/study.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"H\n\x0fGetStudyRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Study"\x8b\x01\n\x12CreateStudyRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12:\n\x05study\x18\x02 \x01(\x0b2&.google.cloud.aiplatform.v1beta1.StudyB\x03\xe0A\x02"\x80\x01\n\x12ListStudiesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01"g\n\x13ListStudiesResponse\x127\n\x07studies\x18\x01 \x03(\x0b2&.google.cloud.aiplatform.v1beta1.Study\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"K\n\x12DeleteStudyRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Study"j\n\x12LookupStudyRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02"\xcc\x01\n\x14SuggestTrialsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Study\x12\x1d\n\x10suggestion_count\x18\x02 \x01(\x05B\x03\xe0A\x02\x12\x16\n\tclient_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12D\n\x08contexts\x18\x04 \x03(\x0b2-.google.cloud.aiplatform.v1beta1.TrialContextB\x03\xe0A\x01"\xf0\x01\n\x15SuggestTrialsResponse\x126\n\x06trials\x18\x01 \x03(\x0b2&.google.cloud.aiplatform.v1beta1.Trial\x12A\n\x0bstudy_state\x18\x02 \x01(\x0e2,.google.cloud.aiplatform.v1beta1.Study.State\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x7f\n\x15SuggestTrialsMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12\x11\n\tclient_id\x18\x02 \x01(\t"\x89\x01\n\x12CreateTrialRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Study\x12:\n\x05trial\x18\x02 \x01(\x0b2&.google.cloud.aiplatform.v1beta1.TrialB\x03\xe0A\x02"H\n\x0fGetTrialRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Trial"}\n\x11ListTrialsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Study\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01"e\n\x12ListTrialsResponse\x126\n\x06trials\x18\x01 \x03(\x0b2&.google.cloud.aiplatform.v1beta1.Trial\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa1\x01\n\x1aAddTrialMeasurementRequest\x12;\n\ntrial_name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Trial\x12F\n\x0bmeasurement\x18\x03 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.MeasurementB\x03\xe0A\x02"\xda\x01\n\x14CompleteTrialRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Trial\x12L\n\x11final_measurement\x18\x02 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.MeasurementB\x03\xe0A\x01\x12\x1d\n\x10trial_infeasible\x18\x03 \x01(\x08B\x03\xe0A\x01\x12\x1e\n\x11infeasible_reason\x18\x04 \x01(\tB\x03\xe0A\x01"K\n\x12DeleteTrialRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Trial"b\n#CheckTrialEarlyStoppingStateRequest\x12;\n\ntrial_name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Trial";\n$CheckTrialEarlyStoppingStateResponse\x12\x13\n\x0bshould_stop\x18\x01 \x01(\x08"\x9a\x01\n%CheckTrialEarlyStoppingStateMetatdata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12\r\n\x05study\x18\x02 \x01(\t\x12\r\n\x05trial\x18\x03 \x01(\t"I\n\x10StopTrialRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Trial"S\n\x18ListOptimalTrialsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Study"[\n\x19ListOptimalTrialsResponse\x12>\n\x0eoptimal_trials\x18\x01 \x03(\x0b2&.google.cloud.aiplatform.v1beta1.Trial2\xa1\x18\n\rVizierService\x12\xba\x01\n\x0bCreateStudy\x123.google.cloud.aiplatform.v1beta1.CreateStudyRequest\x1a&.google.cloud.aiplatform.v1beta1.Study"N\xdaA\x0cparent,study\x82\xd3\xe4\x93\x029"0/v1beta1/{parent=projects/*/locations/*}/studies:\x05study\x12\xa5\x01\n\x08GetStudy\x120.google.cloud.aiplatform.v1beta1.GetStudyRequest\x1a&.google.cloud.aiplatform.v1beta1.Study"?\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1beta1/{name=projects/*/locations/*/studies/*}\x12\xbb\x01\n\x0bListStudies\x123.google.cloud.aiplatform.v1beta1.ListStudiesRequest\x1a4.google.cloud.aiplatform.v1beta1.ListStudiesResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1beta1/{parent=projects/*/locations/*}/studies\x12\x9b\x01\n\x0bDeleteStudy\x123.google.cloud.aiplatform.v1beta1.DeleteStudyRequest\x1a\x16.google.protobuf.Empty"?\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1beta1/{name=projects/*/locations/*/studies/*}\x12\xb7\x01\n\x0bLookupStudy\x123.google.cloud.aiplatform.v1beta1.LookupStudyRequest\x1a&.google.cloud.aiplatform.v1beta1.Study"K\xdaA\x06parent\x82\xd3\xe4\x93\x02<"7/v1beta1/{parent=projects/*/locations/*}/studies:lookup:\x01*\x12\xe4\x01\n\rSuggestTrials\x125.google.cloud.aiplatform.v1beta1.SuggestTrialsRequest\x1a\x1d.google.longrunning.Operation"}\xcaA.\n\x15SuggestTrialsResponse\x12\x15SuggestTrialsMetadata\x82\xd3\xe4\x93\x02F"A/v1beta1/{parent=projects/*/locations/*/studies/*}/trials:suggest:\x01*\x12\xc3\x01\n\x0bCreateTrial\x123.google.cloud.aiplatform.v1beta1.CreateTrialRequest\x1a&.google.cloud.aiplatform.v1beta1.Trial"W\xdaA\x0cparent,trial\x82\xd3\xe4\x93\x02B"9/v1beta1/{parent=projects/*/locations/*/studies/*}/trials:\x05trial\x12\xae\x01\n\x08GetTrial\x120.google.cloud.aiplatform.v1beta1.GetTrialRequest\x1a&.google.cloud.aiplatform.v1beta1.Trial"H\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1beta1/{name=projects/*/locations/*/studies/*/trials/*}\x12\xc1\x01\n\nListTrials\x122.google.cloud.aiplatform.v1beta1.ListTrialsRequest\x1a3.google.cloud.aiplatform.v1beta1.ListTrialsResponse"J\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1beta1/{parent=projects/*/locations/*/studies/*}/trials\x12\xda\x01\n\x13AddTrialMeasurement\x12;.google.cloud.aiplatform.v1beta1.AddTrialMeasurementRequest\x1a&.google.cloud.aiplatform.v1beta1.Trial"^\x82\xd3\xe4\x93\x02X"S/v1beta1/{trial_name=projects/*/locations/*/studies/*/trials/*}:addTrialMeasurement:\x01*\x12\xbd\x01\n\rCompleteTrial\x125.google.cloud.aiplatform.v1beta1.CompleteTrialRequest\x1a&.google.cloud.aiplatform.v1beta1.Trial"M\x82\xd3\xe4\x93\x02G"B/v1beta1/{name=projects/*/locations/*/studies/*/trials/*}:complete:\x01*\x12\xa4\x01\n\x0bDeleteTrial\x123.google.cloud.aiplatform.v1beta1.DeleteTrialRequest\x1a\x16.google.protobuf.Empty"H\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1beta1/{name=projects/*/locations/*/studies/*/trials/*}\x12\xbd\x02\n\x1cCheckTrialEarlyStoppingState\x12D.google.cloud.aiplatform.v1beta1.CheckTrialEarlyStoppingStateRequest\x1a\x1d.google.longrunning.Operation"\xb7\x01\xcaAM\n$CheckTrialEarlyStoppingStateResponse\x12%CheckTrialEarlyStoppingStateMetatdata\x82\xd3\xe4\x93\x02a"\\/v1beta1/{trial_name=projects/*/locations/*/studies/*/trials/*}:checkTrialEarlyStoppingState:\x01*\x12\xb1\x01\n\tStopTrial\x121.google.cloud.aiplatform.v1beta1.StopTrialRequest\x1a&.google.cloud.aiplatform.v1beta1.Trial"I\x82\xd3\xe4\x93\x02C">/v1beta1/{name=projects/*/locations/*/studies/*/trials/*}:stop:\x01*\x12\xeb\x01\n\x11ListOptimalTrials\x129.google.cloud.aiplatform.v1beta1.ListOptimalTrialsRequest\x1a:.google.cloud.aiplatform.v1beta1.ListOptimalTrialsResponse"_\xdaA\x06parent\x82\xd3\xe4\x93\x02P"K/v1beta1/{parent=projects/*/locations/*/studies/*}/trials:listOptimalTrials:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe9\x01\n#com.google.cloud.aiplatform.v1beta1B\x12VizierServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.vizier_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x12VizierServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_GETSTUDYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSTUDYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Study'
    _globals['_CREATESTUDYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESTUDYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATESTUDYREQUEST'].fields_by_name['study']._loaded_options = None
    _globals['_CREATESTUDYREQUEST'].fields_by_name['study']._serialized_options = b'\xe0A\x02'
    _globals['_LISTSTUDIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSTUDIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTSTUDIESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSTUDIESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSTUDIESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSTUDIESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_DELETESTUDYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESTUDYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Study'
    _globals['_LOOKUPSTUDYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LOOKUPSTUDYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LOOKUPSTUDYREQUEST'].fields_by_name['display_name']._loaded_options = None
    _globals['_LOOKUPSTUDYREQUEST'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_SUGGESTTRIALSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SUGGESTTRIALSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Study'
    _globals['_SUGGESTTRIALSREQUEST'].fields_by_name['suggestion_count']._loaded_options = None
    _globals['_SUGGESTTRIALSREQUEST'].fields_by_name['suggestion_count']._serialized_options = b'\xe0A\x02'
    _globals['_SUGGESTTRIALSREQUEST'].fields_by_name['client_id']._loaded_options = None
    _globals['_SUGGESTTRIALSREQUEST'].fields_by_name['client_id']._serialized_options = b'\xe0A\x02'
    _globals['_SUGGESTTRIALSREQUEST'].fields_by_name['contexts']._loaded_options = None
    _globals['_SUGGESTTRIALSREQUEST'].fields_by_name['contexts']._serialized_options = b'\xe0A\x01'
    _globals['_CREATETRIALREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETRIALREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Study'
    _globals['_CREATETRIALREQUEST'].fields_by_name['trial']._loaded_options = None
    _globals['_CREATETRIALREQUEST'].fields_by_name['trial']._serialized_options = b'\xe0A\x02'
    _globals['_GETTRIALREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTRIALREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Trial'
    _globals['_LISTTRIALSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTRIALSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Study'
    _globals['_LISTTRIALSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTTRIALSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTRIALSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTTRIALSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_ADDTRIALMEASUREMENTREQUEST'].fields_by_name['trial_name']._loaded_options = None
    _globals['_ADDTRIALMEASUREMENTREQUEST'].fields_by_name['trial_name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Trial'
    _globals['_ADDTRIALMEASUREMENTREQUEST'].fields_by_name['measurement']._loaded_options = None
    _globals['_ADDTRIALMEASUREMENTREQUEST'].fields_by_name['measurement']._serialized_options = b'\xe0A\x02'
    _globals['_COMPLETETRIALREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_COMPLETETRIALREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Trial'
    _globals['_COMPLETETRIALREQUEST'].fields_by_name['final_measurement']._loaded_options = None
    _globals['_COMPLETETRIALREQUEST'].fields_by_name['final_measurement']._serialized_options = b'\xe0A\x01'
    _globals['_COMPLETETRIALREQUEST'].fields_by_name['trial_infeasible']._loaded_options = None
    _globals['_COMPLETETRIALREQUEST'].fields_by_name['trial_infeasible']._serialized_options = b'\xe0A\x01'
    _globals['_COMPLETETRIALREQUEST'].fields_by_name['infeasible_reason']._loaded_options = None
    _globals['_COMPLETETRIALREQUEST'].fields_by_name['infeasible_reason']._serialized_options = b'\xe0A\x01'
    _globals['_DELETETRIALREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETRIALREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Trial'
    _globals['_CHECKTRIALEARLYSTOPPINGSTATEREQUEST'].fields_by_name['trial_name']._loaded_options = None
    _globals['_CHECKTRIALEARLYSTOPPINGSTATEREQUEST'].fields_by_name['trial_name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Trial'
    _globals['_STOPTRIALREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STOPTRIALREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Trial'
    _globals['_LISTOPTIMALTRIALSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTOPTIMALTRIALSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Study'
    _globals['_VIZIERSERVICE']._loaded_options = None
    _globals['_VIZIERSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_VIZIERSERVICE'].methods_by_name['CreateStudy']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['CreateStudy']._serialized_options = b'\xdaA\x0cparent,study\x82\xd3\xe4\x93\x029"0/v1beta1/{parent=projects/*/locations/*}/studies:\x05study'
    _globals['_VIZIERSERVICE'].methods_by_name['GetStudy']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['GetStudy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1beta1/{name=projects/*/locations/*/studies/*}'
    _globals['_VIZIERSERVICE'].methods_by_name['ListStudies']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['ListStudies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1beta1/{parent=projects/*/locations/*}/studies'
    _globals['_VIZIERSERVICE'].methods_by_name['DeleteStudy']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['DeleteStudy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1beta1/{name=projects/*/locations/*/studies/*}'
    _globals['_VIZIERSERVICE'].methods_by_name['LookupStudy']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['LookupStudy']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02<"7/v1beta1/{parent=projects/*/locations/*}/studies:lookup:\x01*'
    _globals['_VIZIERSERVICE'].methods_by_name['SuggestTrials']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['SuggestTrials']._serialized_options = b'\xcaA.\n\x15SuggestTrialsResponse\x12\x15SuggestTrialsMetadata\x82\xd3\xe4\x93\x02F"A/v1beta1/{parent=projects/*/locations/*/studies/*}/trials:suggest:\x01*'
    _globals['_VIZIERSERVICE'].methods_by_name['CreateTrial']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['CreateTrial']._serialized_options = b'\xdaA\x0cparent,trial\x82\xd3\xe4\x93\x02B"9/v1beta1/{parent=projects/*/locations/*/studies/*}/trials:\x05trial'
    _globals['_VIZIERSERVICE'].methods_by_name['GetTrial']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['GetTrial']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1beta1/{name=projects/*/locations/*/studies/*/trials/*}'
    _globals['_VIZIERSERVICE'].methods_by_name['ListTrials']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['ListTrials']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1beta1/{parent=projects/*/locations/*/studies/*}/trials'
    _globals['_VIZIERSERVICE'].methods_by_name['AddTrialMeasurement']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['AddTrialMeasurement']._serialized_options = b'\x82\xd3\xe4\x93\x02X"S/v1beta1/{trial_name=projects/*/locations/*/studies/*/trials/*}:addTrialMeasurement:\x01*'
    _globals['_VIZIERSERVICE'].methods_by_name['CompleteTrial']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['CompleteTrial']._serialized_options = b'\x82\xd3\xe4\x93\x02G"B/v1beta1/{name=projects/*/locations/*/studies/*/trials/*}:complete:\x01*'
    _globals['_VIZIERSERVICE'].methods_by_name['DeleteTrial']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['DeleteTrial']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1beta1/{name=projects/*/locations/*/studies/*/trials/*}'
    _globals['_VIZIERSERVICE'].methods_by_name['CheckTrialEarlyStoppingState']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['CheckTrialEarlyStoppingState']._serialized_options = b'\xcaAM\n$CheckTrialEarlyStoppingStateResponse\x12%CheckTrialEarlyStoppingStateMetatdata\x82\xd3\xe4\x93\x02a"\\/v1beta1/{trial_name=projects/*/locations/*/studies/*/trials/*}:checkTrialEarlyStoppingState:\x01*'
    _globals['_VIZIERSERVICE'].methods_by_name['StopTrial']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['StopTrial']._serialized_options = b'\x82\xd3\xe4\x93\x02C">/v1beta1/{name=projects/*/locations/*/studies/*/trials/*}:stop:\x01*'
    _globals['_VIZIERSERVICE'].methods_by_name['ListOptimalTrials']._loaded_options = None
    _globals['_VIZIERSERVICE'].methods_by_name['ListOptimalTrials']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02P"K/v1beta1/{parent=projects/*/locations/*/studies/*}/trials:listOptimalTrials:\x01*'
    _globals['_GETSTUDYREQUEST']._serialized_start = 397
    _globals['_GETSTUDYREQUEST']._serialized_end = 469
    _globals['_CREATESTUDYREQUEST']._serialized_start = 472
    _globals['_CREATESTUDYREQUEST']._serialized_end = 611
    _globals['_LISTSTUDIESREQUEST']._serialized_start = 614
    _globals['_LISTSTUDIESREQUEST']._serialized_end = 742
    _globals['_LISTSTUDIESRESPONSE']._serialized_start = 744
    _globals['_LISTSTUDIESRESPONSE']._serialized_end = 847
    _globals['_DELETESTUDYREQUEST']._serialized_start = 849
    _globals['_DELETESTUDYREQUEST']._serialized_end = 924
    _globals['_LOOKUPSTUDYREQUEST']._serialized_start = 926
    _globals['_LOOKUPSTUDYREQUEST']._serialized_end = 1032
    _globals['_SUGGESTTRIALSREQUEST']._serialized_start = 1035
    _globals['_SUGGESTTRIALSREQUEST']._serialized_end = 1239
    _globals['_SUGGESTTRIALSRESPONSE']._serialized_start = 1242
    _globals['_SUGGESTTRIALSRESPONSE']._serialized_end = 1482
    _globals['_SUGGESTTRIALSMETADATA']._serialized_start = 1484
    _globals['_SUGGESTTRIALSMETADATA']._serialized_end = 1611
    _globals['_CREATETRIALREQUEST']._serialized_start = 1614
    _globals['_CREATETRIALREQUEST']._serialized_end = 1751
    _globals['_GETTRIALREQUEST']._serialized_start = 1753
    _globals['_GETTRIALREQUEST']._serialized_end = 1825
    _globals['_LISTTRIALSREQUEST']._serialized_start = 1827
    _globals['_LISTTRIALSREQUEST']._serialized_end = 1952
    _globals['_LISTTRIALSRESPONSE']._serialized_start = 1954
    _globals['_LISTTRIALSRESPONSE']._serialized_end = 2055
    _globals['_ADDTRIALMEASUREMENTREQUEST']._serialized_start = 2058
    _globals['_ADDTRIALMEASUREMENTREQUEST']._serialized_end = 2219
    _globals['_COMPLETETRIALREQUEST']._serialized_start = 2222
    _globals['_COMPLETETRIALREQUEST']._serialized_end = 2440
    _globals['_DELETETRIALREQUEST']._serialized_start = 2442
    _globals['_DELETETRIALREQUEST']._serialized_end = 2517
    _globals['_CHECKTRIALEARLYSTOPPINGSTATEREQUEST']._serialized_start = 2519
    _globals['_CHECKTRIALEARLYSTOPPINGSTATEREQUEST']._serialized_end = 2617
    _globals['_CHECKTRIALEARLYSTOPPINGSTATERESPONSE']._serialized_start = 2619
    _globals['_CHECKTRIALEARLYSTOPPINGSTATERESPONSE']._serialized_end = 2678
    _globals['_CHECKTRIALEARLYSTOPPINGSTATEMETATDATA']._serialized_start = 2681
    _globals['_CHECKTRIALEARLYSTOPPINGSTATEMETATDATA']._serialized_end = 2835
    _globals['_STOPTRIALREQUEST']._serialized_start = 2837
    _globals['_STOPTRIALREQUEST']._serialized_end = 2910
    _globals['_LISTOPTIMALTRIALSREQUEST']._serialized_start = 2912
    _globals['_LISTOPTIMALTRIALSREQUEST']._serialized_end = 2995
    _globals['_LISTOPTIMALTRIALSRESPONSE']._serialized_start = 2997
    _globals['_LISTOPTIMALTRIALSRESPONSE']._serialized_end = 3088
    _globals['_VIZIERSERVICE']._serialized_start = 3091
    _globals['_VIZIERSERVICE']._serialized_end = 6196