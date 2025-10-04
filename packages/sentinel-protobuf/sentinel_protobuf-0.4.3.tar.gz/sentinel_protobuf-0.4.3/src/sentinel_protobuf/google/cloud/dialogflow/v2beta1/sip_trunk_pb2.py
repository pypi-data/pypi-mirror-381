"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dialogflow/v2beta1/sip_trunk.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/dialogflow/v2beta1/sip_trunk.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x96\x01\n\x15CreateSipTrunkRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/SipTrunk\x12A\n\tsip_trunk\x18\x02 \x01(\x0b2).google.cloud.dialogflow.v2beta1.SipTrunkB\x03\xe0A\x02"Q\n\x15DeleteSipTrunkRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/SipTrunk"\x83\x01\n\x14ListSipTrunksRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/SipTrunk\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"o\n\x15ListSipTrunksResponse\x12=\n\nsip_trunks\x18\x01 \x03(\x0b2).google.cloud.dialogflow.v2beta1.SipTrunk\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"N\n\x12GetSipTrunkRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/SipTrunk"\x90\x01\n\x15UpdateSipTrunkRequest\x12A\n\tsip_trunk\x18\x01 \x01(\x0b2).google.cloud.dialogflow.v2beta1.SipTrunkB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\x9b\x02\n\x08SipTrunk\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1e\n\x11expected_hostname\x18\x02 \x03(\tB\x03\xe0A\x02\x12E\n\x0bconnections\x18\x03 \x03(\x0b2+.google.cloud.dialogflow.v2beta1.ConnectionB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x04 \x01(\tB\x03\xe0A\x01:z\xeaAw\n"dialogflow.googleapis.com/SipTrunk\x12<projects/{project}/locations/{location}/sipTrunks/{siptrunk}*\tsipTrunks2\x08sipTrunk"\x80\x07\n\nConnection\x12\x1a\n\rconnection_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12E\n\x05state\x18\x02 \x01(\x0e21.google.cloud.dialogflow.v2beta1.Connection.StateB\x03\xe0A\x03\x129\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03H\x00\x88\x01\x01\x12Y\n\rerror_details\x18\x04 \x01(\x0b28.google.cloud.dialogflow.v2beta1.Connection.ErrorDetailsB\x03\xe0A\x03H\x01\x88\x01\x01\x1a\xb5\x01\n\x0cErrorDetails\x12a\n\x11certificate_state\x18\x01 \x01(\x0e2<.google.cloud.dialogflow.v2beta1.Connection.CertificateStateB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1a\n\rerror_message\x18\x02 \x01(\tH\x01\x88\x01\x01B\x14\n\x12_certificate_stateB\x10\n\x0e_error_message"i\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tCONNECTED\x10\x01\x12\x10\n\x0cDISCONNECTED\x10\x02\x12\x19\n\x15AUTHENTICATION_FAILED\x10\x03\x12\r\n\tKEEPALIVE\x10\x04"\xb3\x02\n\x10CertificateState\x12!\n\x1dCERTIFICATE_STATE_UNSPECIFIED\x10\x00\x12\x15\n\x11CERTIFICATE_VALID\x10\x01\x12\x17\n\x13CERTIFICATE_INVALID\x10\x02\x12\x17\n\x13CERTIFICATE_EXPIRED\x10\x03\x12"\n\x1eCERTIFICATE_HOSTNAME_NOT_FOUND\x10\x04\x12\x1f\n\x1bCERTIFICATE_UNAUTHENTICATED\x10\x05\x12%\n!CERTIFICATE_TRUST_STORE_NOT_FOUND\x10\x06\x12\'\n#CERTIFICATE_HOSTNAME_INVALID_FORMAT\x10\x07\x12\x1e\n\x1aCERTIFICATE_QUOTA_EXCEEDED\x10\x08B\x0e\n\x0c_update_timeB\x10\n\x0e_error_details2\xd3\x08\n\tSipTrunks\x12\xcd\x01\n\x0eCreateSipTrunk\x126.google.cloud.dialogflow.v2beta1.CreateSipTrunkRequest\x1a).google.cloud.dialogflow.v2beta1.SipTrunk"X\xdaA\x10parent,sip_trunk\x82\xd3\xe4\x93\x02?"2/v2beta1/{parent=projects/*/locations/*}/sipTrunks:\tsip_trunk\x12\xa3\x01\n\x0eDeleteSipTrunk\x126.google.cloud.dialogflow.v2beta1.DeleteSipTrunkRequest\x1a\x16.google.protobuf.Empty"A\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v2beta1/{name=projects/*/locations/*/sipTrunks/*}\x12\xc3\x01\n\rListSipTrunks\x125.google.cloud.dialogflow.v2beta1.ListSipTrunksRequest\x1a6.google.cloud.dialogflow.v2beta1.ListSipTrunksResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v2beta1/{parent=projects/*/locations/*}/sipTrunks\x12\xb0\x01\n\x0bGetSipTrunk\x123.google.cloud.dialogflow.v2beta1.GetSipTrunkRequest\x1a).google.cloud.dialogflow.v2beta1.SipTrunk"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v2beta1/{name=projects/*/locations/*/sipTrunks/*}\x12\xdc\x01\n\x0eUpdateSipTrunk\x126.google.cloud.dialogflow.v2beta1.UpdateSipTrunkRequest\x1a).google.cloud.dialogflow.v2beta1.SipTrunk"g\xdaA\x15sip_trunk,update_mask\x82\xd3\xe4\x93\x02I2</v2beta1/{sip_trunk.name=projects/*/locations/*/sipTrunks/*}:\tsip_trunk\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa2\x01\n#com.google.cloud.dialogflow.v2beta1B\rSipTrunkProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2beta1.sip_trunk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.dialogflow.v2beta1B\rSipTrunkProtoP\x01ZCcloud.google.com/go/dialogflow/apiv2beta1/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2Beta1'
    _globals['_CREATESIPTRUNKREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESIPTRUNKREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/SipTrunk'
    _globals['_CREATESIPTRUNKREQUEST'].fields_by_name['sip_trunk']._loaded_options = None
    _globals['_CREATESIPTRUNKREQUEST'].fields_by_name['sip_trunk']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESIPTRUNKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESIPTRUNKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/SipTrunk'
    _globals['_LISTSIPTRUNKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSIPTRUNKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/SipTrunk'
    _globals['_LISTSIPTRUNKSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSIPTRUNKSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSIPTRUNKSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSIPTRUNKSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETSIPTRUNKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSIPTRUNKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/SipTrunk'
    _globals['_UPDATESIPTRUNKREQUEST'].fields_by_name['sip_trunk']._loaded_options = None
    _globals['_UPDATESIPTRUNKREQUEST'].fields_by_name['sip_trunk']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESIPTRUNKREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESIPTRUNKREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_SIPTRUNK'].fields_by_name['name']._loaded_options = None
    _globals['_SIPTRUNK'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SIPTRUNK'].fields_by_name['expected_hostname']._loaded_options = None
    _globals['_SIPTRUNK'].fields_by_name['expected_hostname']._serialized_options = b'\xe0A\x02'
    _globals['_SIPTRUNK'].fields_by_name['connections']._loaded_options = None
    _globals['_SIPTRUNK'].fields_by_name['connections']._serialized_options = b'\xe0A\x03'
    _globals['_SIPTRUNK'].fields_by_name['display_name']._loaded_options = None
    _globals['_SIPTRUNK'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_SIPTRUNK']._loaded_options = None
    _globals['_SIPTRUNK']._serialized_options = b'\xeaAw\n"dialogflow.googleapis.com/SipTrunk\x12<projects/{project}/locations/{location}/sipTrunks/{siptrunk}*\tsipTrunks2\x08sipTrunk'
    _globals['_CONNECTION_ERRORDETAILS'].fields_by_name['certificate_state']._loaded_options = None
    _globals['_CONNECTION_ERRORDETAILS'].fields_by_name['certificate_state']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['connection_id']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['connection_id']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['state']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['update_time']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['error_details']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['error_details']._serialized_options = b'\xe0A\x03'
    _globals['_SIPTRUNKS']._loaded_options = None
    _globals['_SIPTRUNKS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_SIPTRUNKS'].methods_by_name['CreateSipTrunk']._loaded_options = None
    _globals['_SIPTRUNKS'].methods_by_name['CreateSipTrunk']._serialized_options = b'\xdaA\x10parent,sip_trunk\x82\xd3\xe4\x93\x02?"2/v2beta1/{parent=projects/*/locations/*}/sipTrunks:\tsip_trunk'
    _globals['_SIPTRUNKS'].methods_by_name['DeleteSipTrunk']._loaded_options = None
    _globals['_SIPTRUNKS'].methods_by_name['DeleteSipTrunk']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v2beta1/{name=projects/*/locations/*/sipTrunks/*}'
    _globals['_SIPTRUNKS'].methods_by_name['ListSipTrunks']._loaded_options = None
    _globals['_SIPTRUNKS'].methods_by_name['ListSipTrunks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v2beta1/{parent=projects/*/locations/*}/sipTrunks'
    _globals['_SIPTRUNKS'].methods_by_name['GetSipTrunk']._loaded_options = None
    _globals['_SIPTRUNKS'].methods_by_name['GetSipTrunk']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v2beta1/{name=projects/*/locations/*/sipTrunks/*}'
    _globals['_SIPTRUNKS'].methods_by_name['UpdateSipTrunk']._loaded_options = None
    _globals['_SIPTRUNKS'].methods_by_name['UpdateSipTrunk']._serialized_options = b'\xdaA\x15sip_trunk,update_mask\x82\xd3\xe4\x93\x02I2</v2beta1/{sip_trunk.name=projects/*/locations/*/sipTrunks/*}:\tsip_trunk'
    _globals['_CREATESIPTRUNKREQUEST']._serialized_start = 296
    _globals['_CREATESIPTRUNKREQUEST']._serialized_end = 446
    _globals['_DELETESIPTRUNKREQUEST']._serialized_start = 448
    _globals['_DELETESIPTRUNKREQUEST']._serialized_end = 529
    _globals['_LISTSIPTRUNKSREQUEST']._serialized_start = 532
    _globals['_LISTSIPTRUNKSREQUEST']._serialized_end = 663
    _globals['_LISTSIPTRUNKSRESPONSE']._serialized_start = 665
    _globals['_LISTSIPTRUNKSRESPONSE']._serialized_end = 776
    _globals['_GETSIPTRUNKREQUEST']._serialized_start = 778
    _globals['_GETSIPTRUNKREQUEST']._serialized_end = 856
    _globals['_UPDATESIPTRUNKREQUEST']._serialized_start = 859
    _globals['_UPDATESIPTRUNKREQUEST']._serialized_end = 1003
    _globals['_SIPTRUNK']._serialized_start = 1006
    _globals['_SIPTRUNK']._serialized_end = 1289
    _globals['_CONNECTION']._serialized_start = 1292
    _globals['_CONNECTION']._serialized_end = 2188
    _globals['_CONNECTION_ERRORDETAILS']._serialized_start = 1556
    _globals['_CONNECTION_ERRORDETAILS']._serialized_end = 1737
    _globals['_CONNECTION_STATE']._serialized_start = 1739
    _globals['_CONNECTION_STATE']._serialized_end = 1844
    _globals['_CONNECTION_CERTIFICATESTATE']._serialized_start = 1847
    _globals['_CONNECTION_CERTIFICATESTATE']._serialized_end = 2154
    _globals['_SIPTRUNKS']._serialized_start = 2191
    _globals['_SIPTRUNKS']._serialized_end = 3298