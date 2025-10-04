"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/netapp/v1/replication.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.netapp.v1 import common_pb2 as google_dot_cloud_dot_netapp_dot_v1_dot_common__pb2
from .....google.cloud.netapp.v1 import volume_pb2 as google_dot_cloud_dot_netapp_dot_v1_dot_volume__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/netapp/v1/replication.proto\x12\x16google.cloud.netapp.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/netapp/v1/common.proto\x1a#google/cloud/netapp/v1/volume.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd4\x04\n\rTransferStats\x12\x1b\n\x0etransfer_bytes\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12?\n\x17total_transfer_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationH\x01\x88\x01\x01\x12 \n\x13last_transfer_bytes\x18\x03 \x01(\x03H\x02\x88\x01\x01\x12>\n\x16last_transfer_duration\x18\x04 \x01(\x0b2\x19.google.protobuf.DurationH\x03\x88\x01\x01\x124\n\x0clag_duration\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationH\x04\x88\x01\x01\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampH\x05\x88\x01\x01\x12?\n\x16last_transfer_end_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampH\x06\x88\x01\x01\x12 \n\x13last_transfer_error\x18\x08 \x01(\tH\x07\x88\x01\x01B\x11\n\x0f_transfer_bytesB\x1a\n\x18_total_transfer_durationB\x16\n\x14_last_transfer_bytesB\x19\n\x17_last_transfer_durationB\x0f\n\r_lag_durationB\x0e\n\x0c_update_timeB\x19\n\x17_last_transfer_end_timeB\x16\n\x14_last_transfer_error"\xc2\x10\n\x0bReplication\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12=\n\x05state\x18\x02 \x01(\x0e2).google.cloud.netapp.v1.Replication.StateB\x03\xe0A\x03\x12\x1a\n\rstate_details\x18\x03 \x01(\tB\x03\xe0A\x03\x12F\n\x04role\x18\x04 \x01(\x0e23.google.cloud.netapp.v1.Replication.ReplicationRoleB\x03\xe0A\x03\x12Z\n\x14replication_schedule\x18\x05 \x01(\x0e27.google.cloud.netapp.v1.Replication.ReplicationScheduleB\x03\xe0A\x02\x12J\n\x0cmirror_state\x18\x06 \x01(\x0e2/.google.cloud.netapp.v1.Replication.MirrorStateB\x03\xe0A\x03\x12\x19\n\x07healthy\x18\x08 \x01(\x08B\x03\xe0A\x03H\x00\x88\x01\x01\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12@\n\x12destination_volume\x18\n \x01(\tB$\xe0A\x03\xfaA\x1e\n\x1cnetapp.googleapis.com/Volume\x12B\n\x0etransfer_stats\x18\x0b \x01(\x0b2%.google.cloud.netapp.v1.TransferStatsB\x03\xe0A\x03\x12?\n\x06labels\x18\x0c \x03(\x0b2/.google.cloud.netapp.v1.Replication.LabelsEntry\x12\x18\n\x0bdescription\x18\r \x01(\tH\x01\x88\x01\x01\x12b\n\x1ddestination_volume_parameters\x18\x0e \x01(\x0b23.google.cloud.netapp.v1.DestinationVolumeParametersB\x06\xe0A\x04\xe0A\x02\x12;\n\rsource_volume\x18\x0f \x01(\tB$\xe0A\x03\xfaA\x1e\n\x1cnetapp.googleapis.com/Volume\x12Q\n\x16hybrid_peering_details\x18\x10 \x01(\x0b2,.google.cloud.netapp.v1.HybridPeeringDetailsB\x03\xe0A\x03\x12\x1d\n\x10cluster_location\x18\x12 \x01(\tB\x03\xe0A\x01\x12_\n\x17hybrid_replication_type\x18\x13 \x01(\x0e29.google.cloud.netapp.v1.Replication.HybridReplicationTypeB\x03\xe0A\x03\x12S\n hybrid_replication_user_commands\x18\x14 \x01(\x0b2$.google.cloud.netapp.v1.UserCommandsB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xd3\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x05\x12\t\n\x05ERROR\x10\x06\x12\x1b\n\x17PENDING_CLUSTER_PEERING\x10\x08\x12\x17\n\x13PENDING_SVM_PEERING\x10\t\x12\x19\n\x15PENDING_REMOTE_RESYNC\x10\n\x12"\n\x1eEXTERNALLY_MANAGED_REPLICATION\x10\x0b"P\n\x0fReplicationRole\x12 \n\x1cREPLICATION_ROLE_UNSPECIFIED\x10\x00\x12\n\n\x06SOURCE\x10\x01\x12\x0f\n\x0bDESTINATION\x10\x02"h\n\x13ReplicationSchedule\x12$\n REPLICATION_SCHEDULE_UNSPECIFIED\x10\x00\x12\x14\n\x10EVERY_10_MINUTES\x10\x01\x12\n\n\x06HOURLY\x10\x02\x12\t\n\x05DAILY\x10\x03"\xbc\x01\n\x0bMirrorState\x12\x1c\n\x18MIRROR_STATE_UNSPECIFIED\x10\x00\x12\r\n\tPREPARING\x10\x01\x12\x0c\n\x08MIRRORED\x10\x02\x12\x0b\n\x07STOPPED\x10\x03\x12\x10\n\x0cTRANSFERRING\x10\x04\x12\x19\n\x15BASELINE_TRANSFERRING\x10\x05\x12\x0b\n\x07ABORTED\x10\x06\x12\x16\n\x12EXTERNALLY_MANAGED\x10\x07\x12\x13\n\x0fPENDING_PEERING\x10\x08"\xa3\x01\n\x15HybridReplicationType\x12\'\n#HYBRID_REPLICATION_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tMIGRATION\x10\x01\x12\x1a\n\x16CONTINUOUS_REPLICATION\x10\x02\x12\x16\n\x12ONPREM_REPLICATION\x10\x03\x12\x1e\n\x1aREVERSE_ONPREM_REPLICATION\x10\x04:\x97\x01\xeaA\x93\x01\n!netapp.googleapis.com/Replication\x12Sprojects/{project}/locations/{location}/volumes/{volume}/replications/{replication}*\x0creplications2\x0breplicationB\n\n\x08_healthyB\x0e\n\x0c_description"\xf6\x01\n\x14HybridPeeringDetails\x12\x16\n\tsubnet_ip\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07command\x18\x02 \x01(\tB\x03\xe0A\x03\x12<\n\x13command_expiry_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x17\n\npassphrase\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10peer_volume_name\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1e\n\x11peer_cluster_name\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rpeer_svm_name\x18\x07 \x01(\tB\x03\xe0A\x03"\x9d\x01\n\x17ListReplicationsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!netapp.googleapis.com/Replication\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\x0e\n\x06filter\x18\x05 \x01(\t"\x83\x01\n\x18ListReplicationsResponse\x129\n\x0creplications\x18\x01 \x03(\x0b2#.google.cloud.netapp.v1.Replication\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"P\n\x15GetReplicationRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication"\x8b\x02\n\x1bDestinationVolumeParameters\x12?\n\x0cstorage_pool\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/StoragePool\x12\x11\n\tvolume_id\x18\x02 \x01(\t\x12\x12\n\nshare_name\x18\x03 \x01(\t\x12\x18\n\x0bdescription\x18\x04 \x01(\tH\x00\x88\x01\x01\x12G\n\x0etiering_policy\x18\x05 \x01(\x0b2%.google.cloud.netapp.v1.TieringPolicyB\x03\xe0A\x01H\x01\x88\x01\x01B\x0e\n\x0c_descriptionB\x11\n\x0f_tiering_policy"\xb1\x01\n\x18CreateReplicationRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!netapp.googleapis.com/Replication\x12=\n\x0breplication\x18\x02 \x01(\x0b2#.google.cloud.netapp.v1.ReplicationB\x03\xe0A\x02\x12\x1b\n\x0ereplication_id\x18\x03 \x01(\tB\x03\xe0A\x02"S\n\x18DeleteReplicationRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication"\x8f\x01\n\x18UpdateReplicationRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12=\n\x0breplication\x18\x02 \x01(\x0b2#.google.cloud.netapp.v1.ReplicationB\x03\xe0A\x02"`\n\x16StopReplicationRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication\x12\r\n\x05force\x18\x02 \x01(\x08"S\n\x18ResumeReplicationRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication"]\n"ReverseReplicationDirectionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication"\xcd\x01\n\x17EstablishPeeringRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication\x12\x1e\n\x11peer_cluster_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rpeer_svm_name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11peer_ip_addresses\x18\x04 \x03(\tB\x03\xe0A\x01\x12\x1d\n\x10peer_volume_name\x18\x05 \x01(\tB\x03\xe0A\x02"Q\n\x16SyncReplicationRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/ReplicationB\xb2\x01\n\x1acom.google.cloud.netapp.v1B\x10ReplicationProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.netapp.v1.replication_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.netapp.v1B\x10ReplicationProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1'
    _globals['_REPLICATION_LABELSENTRY']._loaded_options = None
    _globals['_REPLICATION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_REPLICATION'].fields_by_name['name']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_REPLICATION'].fields_by_name['state']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATION'].fields_by_name['state_details']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['state_details']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATION'].fields_by_name['role']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['role']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATION'].fields_by_name['replication_schedule']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['replication_schedule']._serialized_options = b'\xe0A\x02'
    _globals['_REPLICATION'].fields_by_name['mirror_state']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['mirror_state']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATION'].fields_by_name['healthy']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['healthy']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATION'].fields_by_name['destination_volume']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['destination_volume']._serialized_options = b'\xe0A\x03\xfaA\x1e\n\x1cnetapp.googleapis.com/Volume'
    _globals['_REPLICATION'].fields_by_name['transfer_stats']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['transfer_stats']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATION'].fields_by_name['destination_volume_parameters']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['destination_volume_parameters']._serialized_options = b'\xe0A\x04\xe0A\x02'
    _globals['_REPLICATION'].fields_by_name['source_volume']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['source_volume']._serialized_options = b'\xe0A\x03\xfaA\x1e\n\x1cnetapp.googleapis.com/Volume'
    _globals['_REPLICATION'].fields_by_name['hybrid_peering_details']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['hybrid_peering_details']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATION'].fields_by_name['cluster_location']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['cluster_location']._serialized_options = b'\xe0A\x01'
    _globals['_REPLICATION'].fields_by_name['hybrid_replication_type']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['hybrid_replication_type']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATION'].fields_by_name['hybrid_replication_user_commands']._loaded_options = None
    _globals['_REPLICATION'].fields_by_name['hybrid_replication_user_commands']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATION']._loaded_options = None
    _globals['_REPLICATION']._serialized_options = b'\xeaA\x93\x01\n!netapp.googleapis.com/Replication\x12Sprojects/{project}/locations/{location}/volumes/{volume}/replications/{replication}*\x0creplications2\x0breplication'
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['subnet_ip']._loaded_options = None
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['subnet_ip']._serialized_options = b'\xe0A\x03'
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['command']._loaded_options = None
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['command']._serialized_options = b'\xe0A\x03'
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['command_expiry_time']._loaded_options = None
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['command_expiry_time']._serialized_options = b'\xe0A\x03'
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['passphrase']._loaded_options = None
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['passphrase']._serialized_options = b'\xe0A\x03'
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['peer_volume_name']._loaded_options = None
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['peer_volume_name']._serialized_options = b'\xe0A\x03'
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['peer_cluster_name']._loaded_options = None
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['peer_cluster_name']._serialized_options = b'\xe0A\x03'
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['peer_svm_name']._loaded_options = None
    _globals['_HYBRIDPEERINGDETAILS'].fields_by_name['peer_svm_name']._serialized_options = b'\xe0A\x03'
    _globals['_LISTREPLICATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREPLICATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!netapp.googleapis.com/Replication'
    _globals['_GETREPLICATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREPLICATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication'
    _globals['_DESTINATIONVOLUMEPARAMETERS'].fields_by_name['storage_pool']._loaded_options = None
    _globals['_DESTINATIONVOLUMEPARAMETERS'].fields_by_name['storage_pool']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/StoragePool'
    _globals['_DESTINATIONVOLUMEPARAMETERS'].fields_by_name['tiering_policy']._loaded_options = None
    _globals['_DESTINATIONVOLUMEPARAMETERS'].fields_by_name['tiering_policy']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEREPLICATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREPLICATIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!netapp.googleapis.com/Replication'
    _globals['_CREATEREPLICATIONREQUEST'].fields_by_name['replication']._loaded_options = None
    _globals['_CREATEREPLICATIONREQUEST'].fields_by_name['replication']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEREPLICATIONREQUEST'].fields_by_name['replication_id']._loaded_options = None
    _globals['_CREATEREPLICATIONREQUEST'].fields_by_name['replication_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEREPLICATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEREPLICATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication'
    _globals['_UPDATEREPLICATIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEREPLICATIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEREPLICATIONREQUEST'].fields_by_name['replication']._loaded_options = None
    _globals['_UPDATEREPLICATIONREQUEST'].fields_by_name['replication']._serialized_options = b'\xe0A\x02'
    _globals['_STOPREPLICATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STOPREPLICATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication'
    _globals['_RESUMEREPLICATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMEREPLICATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication'
    _globals['_REVERSEREPLICATIONDIRECTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REVERSEREPLICATIONDIRECTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication'
    _globals['_ESTABLISHPEERINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ESTABLISHPEERINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication'
    _globals['_ESTABLISHPEERINGREQUEST'].fields_by_name['peer_cluster_name']._loaded_options = None
    _globals['_ESTABLISHPEERINGREQUEST'].fields_by_name['peer_cluster_name']._serialized_options = b'\xe0A\x02'
    _globals['_ESTABLISHPEERINGREQUEST'].fields_by_name['peer_svm_name']._loaded_options = None
    _globals['_ESTABLISHPEERINGREQUEST'].fields_by_name['peer_svm_name']._serialized_options = b'\xe0A\x02'
    _globals['_ESTABLISHPEERINGREQUEST'].fields_by_name['peer_ip_addresses']._loaded_options = None
    _globals['_ESTABLISHPEERINGREQUEST'].fields_by_name['peer_ip_addresses']._serialized_options = b'\xe0A\x01'
    _globals['_ESTABLISHPEERINGREQUEST'].fields_by_name['peer_volume_name']._loaded_options = None
    _globals['_ESTABLISHPEERINGREQUEST'].fields_by_name['peer_volume_name']._serialized_options = b'\xe0A\x02'
    _globals['_SYNCREPLICATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SYNCREPLICATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/Replication'
    _globals['_TRANSFERSTATS']._serialized_start = 302
    _globals['_TRANSFERSTATS']._serialized_end = 898
    _globals['_REPLICATION']._serialized_start = 901
    _globals['_REPLICATION']._serialized_end = 3015
    _globals['_REPLICATION_LABELSENTRY']._serialized_start = 2029
    _globals['_REPLICATION_LABELSENTRY']._serialized_end = 2074
    _globals['_REPLICATION_STATE']._serialized_start = 2077
    _globals['_REPLICATION_STATE']._serialized_end = 2288
    _globals['_REPLICATION_REPLICATIONROLE']._serialized_start = 2290
    _globals['_REPLICATION_REPLICATIONROLE']._serialized_end = 2370
    _globals['_REPLICATION_REPLICATIONSCHEDULE']._serialized_start = 2372
    _globals['_REPLICATION_REPLICATIONSCHEDULE']._serialized_end = 2476
    _globals['_REPLICATION_MIRRORSTATE']._serialized_start = 2479
    _globals['_REPLICATION_MIRRORSTATE']._serialized_end = 2667
    _globals['_REPLICATION_HYBRIDREPLICATIONTYPE']._serialized_start = 2670
    _globals['_REPLICATION_HYBRIDREPLICATIONTYPE']._serialized_end = 2833
    _globals['_HYBRIDPEERINGDETAILS']._serialized_start = 3018
    _globals['_HYBRIDPEERINGDETAILS']._serialized_end = 3264
    _globals['_LISTREPLICATIONSREQUEST']._serialized_start = 3267
    _globals['_LISTREPLICATIONSREQUEST']._serialized_end = 3424
    _globals['_LISTREPLICATIONSRESPONSE']._serialized_start = 3427
    _globals['_LISTREPLICATIONSRESPONSE']._serialized_end = 3558
    _globals['_GETREPLICATIONREQUEST']._serialized_start = 3560
    _globals['_GETREPLICATIONREQUEST']._serialized_end = 3640
    _globals['_DESTINATIONVOLUMEPARAMETERS']._serialized_start = 3643
    _globals['_DESTINATIONVOLUMEPARAMETERS']._serialized_end = 3910
    _globals['_CREATEREPLICATIONREQUEST']._serialized_start = 3913
    _globals['_CREATEREPLICATIONREQUEST']._serialized_end = 4090
    _globals['_DELETEREPLICATIONREQUEST']._serialized_start = 4092
    _globals['_DELETEREPLICATIONREQUEST']._serialized_end = 4175
    _globals['_UPDATEREPLICATIONREQUEST']._serialized_start = 4178
    _globals['_UPDATEREPLICATIONREQUEST']._serialized_end = 4321
    _globals['_STOPREPLICATIONREQUEST']._serialized_start = 4323
    _globals['_STOPREPLICATIONREQUEST']._serialized_end = 4419
    _globals['_RESUMEREPLICATIONREQUEST']._serialized_start = 4421
    _globals['_RESUMEREPLICATIONREQUEST']._serialized_end = 4504
    _globals['_REVERSEREPLICATIONDIRECTIONREQUEST']._serialized_start = 4506
    _globals['_REVERSEREPLICATIONDIRECTIONREQUEST']._serialized_end = 4599
    _globals['_ESTABLISHPEERINGREQUEST']._serialized_start = 4602
    _globals['_ESTABLISHPEERINGREQUEST']._serialized_end = 4807
    _globals['_SYNCREPLICATIONREQUEST']._serialized_start = 4809
    _globals['_SYNCREPLICATIONREQUEST']._serialized_end = 4890