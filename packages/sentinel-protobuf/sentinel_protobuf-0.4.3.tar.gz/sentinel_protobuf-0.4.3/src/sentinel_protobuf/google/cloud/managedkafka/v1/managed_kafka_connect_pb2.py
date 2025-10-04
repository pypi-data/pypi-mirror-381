"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/managedkafka/v1/managed_kafka_connect.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.managedkafka.v1 import resources_pb2 as google_dot_cloud_dot_managedkafka_dot_v1_dot_resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/managedkafka/v1/managed_kafka_connect.proto\x12\x1cgoogle.cloud.managedkafka.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/managedkafka/v1/resources.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\\\n\x18GetConnectClusterRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*managedkafka.googleapis.com/ConnectCluster"\xef\x01\n\x1bCreateConnectClusterRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*managedkafka.googleapis.com/ConnectCluster\x12\x1f\n\x12connect_cluster_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12J\n\x0fconnect_cluster\x18\x03 \x01(\x0b2,.google.cloud.managedkafka.v1.ConnectClusterB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xc0\x01\n\x1bUpdateConnectClusterRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12J\n\x0fconnect_cluster\x18\x02 \x01(\x0b2,.google.cloud.managedkafka.v1.ConnectClusterB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x80\x01\n\x1bDeleteConnectClusterRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*managedkafka.googleapis.com/ConnectCluster\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\xbd\x01\n\x1aListConnectClustersRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*managedkafka.googleapis.com/ConnectCluster\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x93\x01\n\x1bListConnectClustersResponse\x12F\n\x10connect_clusters\x18\x01 \x03(\x0b2,.google.cloud.managedkafka.v1.ConnectCluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"R\n\x13GetConnectorRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%managedkafka.googleapis.com/Connector"\xb3\x01\n\x16CreateConnectorRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%managedkafka.googleapis.com/Connector\x12\x19\n\x0cconnector_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12?\n\tconnector\x18\x03 \x01(\x0b2\'.google.cloud.managedkafka.v1.ConnectorB\x03\xe0A\x02"\x8f\x01\n\x16UpdateConnectorRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12?\n\tconnector\x18\x02 \x01(\x0b2\'.google.cloud.managedkafka.v1.ConnectorB\x03\xe0A\x02"U\n\x16DeleteConnectorRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%managedkafka.googleapis.com/Connector"\x87\x01\n\x15ListConnectorsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%managedkafka.googleapis.com/Connector\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"n\n\x16ListConnectorsResponse\x12;\n\nconnectors\x18\x01 \x03(\x0b2\'.google.cloud.managedkafka.v1.Connector\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"T\n\x15PauseConnectorRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%managedkafka.googleapis.com/Connector"\x18\n\x16PauseConnectorResponse"U\n\x16ResumeConnectorRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%managedkafka.googleapis.com/Connector"\x19\n\x17ResumeConnectorResponse"V\n\x17RestartConnectorRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%managedkafka.googleapis.com/Connector"\x1a\n\x18RestartConnectorResponse"S\n\x14StopConnectorRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%managedkafka.googleapis.com/Connector"\x17\n\x15StopConnectorResponse2\x83\x19\n\x13ManagedKafkaConnect\x12\xd0\x01\n\x13ListConnectClusters\x128.google.cloud.managedkafka.v1.ListConnectClustersRequest\x1a9.google.cloud.managedkafka.v1.ListConnectClustersResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=projects/*/locations/*}/connectClusters\x12\xbd\x01\n\x11GetConnectCluster\x126.google.cloud.managedkafka.v1.GetConnectClusterRequest\x1a,.google.cloud.managedkafka.v1.ConnectCluster"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/connectClusters/*}\x12\x91\x02\n\x14CreateConnectCluster\x129.google.cloud.managedkafka.v1.CreateConnectClusterRequest\x1a\x1d.google.longrunning.Operation"\x9e\x01\xcaA#\n\x0eConnectCluster\x12\x11OperationMetadata\xdaA)parent,connect_cluster,connect_cluster_id\x82\xd3\xe4\x93\x02F"3/v1/{parent=projects/*/locations/*}/connectClusters:\x0fconnect_cluster\x12\x93\x02\n\x14UpdateConnectCluster\x129.google.cloud.managedkafka.v1.UpdateConnectClusterRequest\x1a\x1d.google.longrunning.Operation"\xa0\x01\xcaA#\n\x0eConnectCluster\x12\x11OperationMetadata\xdaA\x1bconnect_cluster,update_mask\x82\xd3\xe4\x93\x02V2C/v1/{connect_cluster.name=projects/*/locations/*/connectClusters/*}:\x0fconnect_cluster\x12\xe1\x01\n\x14DeleteConnectCluster\x129.google.cloud.managedkafka.v1.DeleteConnectClusterRequest\x1a\x1d.google.longrunning.Operation"o\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=projects/*/locations/*/connectClusters/*}\x12\xce\x01\n\x0eListConnectors\x123.google.cloud.managedkafka.v1.ListConnectorsRequest\x1a4.google.cloud.managedkafka.v1.ListConnectorsResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1/{parent=projects/*/locations/*/connectClusters/*}/connectors\x12\xbb\x01\n\x0cGetConnector\x121.google.cloud.managedkafka.v1.GetConnectorRequest\x1a\'.google.cloud.managedkafka.v1.Connector"O\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1/{name=projects/*/locations/*/connectClusters/*/connectors/*}\x12\xe5\x01\n\x0fCreateConnector\x124.google.cloud.managedkafka.v1.CreateConnectorRequest\x1a\'.google.cloud.managedkafka.v1.Connector"s\xdaA\x1dparent,connector,connector_id\x82\xd3\xe4\x93\x02M"@/v1/{parent=projects/*/locations/*/connectClusters/*}/connectors:\tconnector\x12\xe7\x01\n\x0fUpdateConnector\x124.google.cloud.managedkafka.v1.UpdateConnectorRequest\x1a\'.google.cloud.managedkafka.v1.Connector"u\xdaA\x15connector,update_mask\x82\xd3\xe4\x93\x02W2J/v1/{connector.name=projects/*/locations/*/connectClusters/*/connectors/*}:\tconnector\x12\xb0\x01\n\x0fDeleteConnector\x124.google.cloud.managedkafka.v1.DeleteConnectorRequest\x1a\x16.google.protobuf.Empty"O\xdaA\x04name\x82\xd3\xe4\x93\x02B*@/v1/{name=projects/*/locations/*/connectClusters/*/connectors/*}\x12\xd5\x01\n\x0ePauseConnector\x123.google.cloud.managedkafka.v1.PauseConnectorRequest\x1a4.google.cloud.managedkafka.v1.PauseConnectorResponse"X\xdaA\x04name\x82\xd3\xe4\x93\x02K"F/v1/{name=projects/*/locations/*/connectClusters/*/connectors/*}:pause:\x01*\x12\xd9\x01\n\x0fResumeConnector\x124.google.cloud.managedkafka.v1.ResumeConnectorRequest\x1a5.google.cloud.managedkafka.v1.ResumeConnectorResponse"Y\xdaA\x04name\x82\xd3\xe4\x93\x02L"G/v1/{name=projects/*/locations/*/connectClusters/*/connectors/*}:resume:\x01*\x12\xdd\x01\n\x10RestartConnector\x125.google.cloud.managedkafka.v1.RestartConnectorRequest\x1a6.google.cloud.managedkafka.v1.RestartConnectorResponse"Z\xdaA\x04name\x82\xd3\xe4\x93\x02M"H/v1/{name=projects/*/locations/*/connectClusters/*/connectors/*}:restart:\x01*\x12\xd1\x01\n\rStopConnector\x122.google.cloud.managedkafka.v1.StopConnectorRequest\x1a3.google.cloud.managedkafka.v1.StopConnectorResponse"W\xdaA\x04name\x82\xd3\xe4\x93\x02J"E/v1/{name=projects/*/locations/*/connectClusters/*/connectors/*}:stop:\x01*\x1aO\xcaA\x1bmanagedkafka.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe4\x01\n com.google.cloud.managedkafka.v1B\x18ManagedKafkaConnectProtoP\x01ZDcloud.google.com/go/managedkafka/apiv1/managedkafkapb;managedkafkapb\xaa\x02\x1cGoogle.Cloud.ManagedKafka.V1\xca\x02\x1cGoogle\\Cloud\\ManagedKafka\\V1\xea\x02\x1fGoogle::Cloud::ManagedKafka::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.managedkafka.v1.managed_kafka_connect_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.managedkafka.v1B\x18ManagedKafkaConnectProtoP\x01ZDcloud.google.com/go/managedkafka/apiv1/managedkafkapb;managedkafkapb\xaa\x02\x1cGoogle.Cloud.ManagedKafka.V1\xca\x02\x1cGoogle\\Cloud\\ManagedKafka\\V1\xea\x02\x1fGoogle::Cloud::ManagedKafka::V1'
    _globals['_GETCONNECTCLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONNECTCLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*managedkafka.googleapis.com/ConnectCluster'
    _globals['_CREATECONNECTCLUSTERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONNECTCLUSTERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*managedkafka.googleapis.com/ConnectCluster'
    _globals['_CREATECONNECTCLUSTERREQUEST'].fields_by_name['connect_cluster_id']._loaded_options = None
    _globals['_CREATECONNECTCLUSTERREQUEST'].fields_by_name['connect_cluster_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONNECTCLUSTERREQUEST'].fields_by_name['connect_cluster']._loaded_options = None
    _globals['_CREATECONNECTCLUSTERREQUEST'].fields_by_name['connect_cluster']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONNECTCLUSTERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATECONNECTCLUSTERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_UPDATECONNECTCLUSTERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONNECTCLUSTERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTCLUSTERREQUEST'].fields_by_name['connect_cluster']._loaded_options = None
    _globals['_UPDATECONNECTCLUSTERREQUEST'].fields_by_name['connect_cluster']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTCLUSTERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATECONNECTCLUSTERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_DELETECONNECTCLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONNECTCLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*managedkafka.googleapis.com/ConnectCluster'
    _globals['_DELETECONNECTCLUSTERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETECONNECTCLUSTERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_LISTCONNECTCLUSTERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONNECTCLUSTERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*managedkafka.googleapis.com/ConnectCluster'
    _globals['_LISTCONNECTCLUSTERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONNECTCLUSTERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONNECTCLUSTERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONNECTCLUSTERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONNECTCLUSTERSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCONNECTCLUSTERSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONNECTCLUSTERSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTCONNECTCLUSTERSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETCONNECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONNECTORREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%managedkafka.googleapis.com/Connector"
    _globals['_CREATECONNECTORREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONNECTORREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%managedkafka.googleapis.com/Connector"
    _globals['_CREATECONNECTORREQUEST'].fields_by_name['connector_id']._loaded_options = None
    _globals['_CREATECONNECTORREQUEST'].fields_by_name['connector_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONNECTORREQUEST'].fields_by_name['connector']._loaded_options = None
    _globals['_CREATECONNECTORREQUEST'].fields_by_name['connector']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTORREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONNECTORREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTORREQUEST'].fields_by_name['connector']._loaded_options = None
    _globals['_UPDATECONNECTORREQUEST'].fields_by_name['connector']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECONNECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONNECTORREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%managedkafka.googleapis.com/Connector"
    _globals['_LISTCONNECTORSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONNECTORSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%managedkafka.googleapis.com/Connector"
    _globals['_LISTCONNECTORSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONNECTORSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONNECTORSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONNECTORSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_PAUSECONNECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PAUSECONNECTORREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%managedkafka.googleapis.com/Connector"
    _globals['_RESUMECONNECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMECONNECTORREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%managedkafka.googleapis.com/Connector"
    _globals['_RESTARTCONNECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESTARTCONNECTORREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%managedkafka.googleapis.com/Connector"
    _globals['_STOPCONNECTORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STOPCONNECTORREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%managedkafka.googleapis.com/Connector"
    _globals['_MANAGEDKAFKACONNECT']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT']._serialized_options = b'\xcaA\x1bmanagedkafka.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['ListConnectClusters']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['ListConnectClusters']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=projects/*/locations/*}/connectClusters'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['GetConnectCluster']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['GetConnectCluster']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/connectClusters/*}'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['CreateConnectCluster']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['CreateConnectCluster']._serialized_options = b'\xcaA#\n\x0eConnectCluster\x12\x11OperationMetadata\xdaA)parent,connect_cluster,connect_cluster_id\x82\xd3\xe4\x93\x02F"3/v1/{parent=projects/*/locations/*}/connectClusters:\x0fconnect_cluster'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['UpdateConnectCluster']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['UpdateConnectCluster']._serialized_options = b'\xcaA#\n\x0eConnectCluster\x12\x11OperationMetadata\xdaA\x1bconnect_cluster,update_mask\x82\xd3\xe4\x93\x02V2C/v1/{connect_cluster.name=projects/*/locations/*/connectClusters/*}:\x0fconnect_cluster'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['DeleteConnectCluster']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['DeleteConnectCluster']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=projects/*/locations/*/connectClusters/*}'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['ListConnectors']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['ListConnectors']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1/{parent=projects/*/locations/*/connectClusters/*}/connectors'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['GetConnector']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['GetConnector']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1/{name=projects/*/locations/*/connectClusters/*/connectors/*}'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['CreateConnector']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['CreateConnector']._serialized_options = b'\xdaA\x1dparent,connector,connector_id\x82\xd3\xe4\x93\x02M"@/v1/{parent=projects/*/locations/*/connectClusters/*}/connectors:\tconnector'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['UpdateConnector']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['UpdateConnector']._serialized_options = b'\xdaA\x15connector,update_mask\x82\xd3\xe4\x93\x02W2J/v1/{connector.name=projects/*/locations/*/connectClusters/*/connectors/*}:\tconnector'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['DeleteConnector']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['DeleteConnector']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B*@/v1/{name=projects/*/locations/*/connectClusters/*/connectors/*}'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['PauseConnector']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['PauseConnector']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02K"F/v1/{name=projects/*/locations/*/connectClusters/*/connectors/*}:pause:\x01*'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['ResumeConnector']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['ResumeConnector']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02L"G/v1/{name=projects/*/locations/*/connectClusters/*/connectors/*}:resume:\x01*'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['RestartConnector']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['RestartConnector']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02M"H/v1/{name=projects/*/locations/*/connectClusters/*/connectors/*}:restart:\x01*'
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['StopConnector']._loaded_options = None
    _globals['_MANAGEDKAFKACONNECT'].methods_by_name['StopConnector']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02J"E/v1/{name=projects/*/locations/*/connectClusters/*/connectors/*}:stop:\x01*'
    _globals['_GETCONNECTCLUSTERREQUEST']._serialized_start = 380
    _globals['_GETCONNECTCLUSTERREQUEST']._serialized_end = 472
    _globals['_CREATECONNECTCLUSTERREQUEST']._serialized_start = 475
    _globals['_CREATECONNECTCLUSTERREQUEST']._serialized_end = 714
    _globals['_UPDATECONNECTCLUSTERREQUEST']._serialized_start = 717
    _globals['_UPDATECONNECTCLUSTERREQUEST']._serialized_end = 909
    _globals['_DELETECONNECTCLUSTERREQUEST']._serialized_start = 912
    _globals['_DELETECONNECTCLUSTERREQUEST']._serialized_end = 1040
    _globals['_LISTCONNECTCLUSTERSREQUEST']._serialized_start = 1043
    _globals['_LISTCONNECTCLUSTERSREQUEST']._serialized_end = 1232
    _globals['_LISTCONNECTCLUSTERSRESPONSE']._serialized_start = 1235
    _globals['_LISTCONNECTCLUSTERSRESPONSE']._serialized_end = 1382
    _globals['_GETCONNECTORREQUEST']._serialized_start = 1384
    _globals['_GETCONNECTORREQUEST']._serialized_end = 1466
    _globals['_CREATECONNECTORREQUEST']._serialized_start = 1469
    _globals['_CREATECONNECTORREQUEST']._serialized_end = 1648
    _globals['_UPDATECONNECTORREQUEST']._serialized_start = 1651
    _globals['_UPDATECONNECTORREQUEST']._serialized_end = 1794
    _globals['_DELETECONNECTORREQUEST']._serialized_start = 1796
    _globals['_DELETECONNECTORREQUEST']._serialized_end = 1881
    _globals['_LISTCONNECTORSREQUEST']._serialized_start = 1884
    _globals['_LISTCONNECTORSREQUEST']._serialized_end = 2019
    _globals['_LISTCONNECTORSRESPONSE']._serialized_start = 2021
    _globals['_LISTCONNECTORSRESPONSE']._serialized_end = 2131
    _globals['_PAUSECONNECTORREQUEST']._serialized_start = 2133
    _globals['_PAUSECONNECTORREQUEST']._serialized_end = 2217
    _globals['_PAUSECONNECTORRESPONSE']._serialized_start = 2219
    _globals['_PAUSECONNECTORRESPONSE']._serialized_end = 2243
    _globals['_RESUMECONNECTORREQUEST']._serialized_start = 2245
    _globals['_RESUMECONNECTORREQUEST']._serialized_end = 2330
    _globals['_RESUMECONNECTORRESPONSE']._serialized_start = 2332
    _globals['_RESUMECONNECTORRESPONSE']._serialized_end = 2357
    _globals['_RESTARTCONNECTORREQUEST']._serialized_start = 2359
    _globals['_RESTARTCONNECTORREQUEST']._serialized_end = 2445
    _globals['_RESTARTCONNECTORRESPONSE']._serialized_start = 2447
    _globals['_RESTARTCONNECTORRESPONSE']._serialized_end = 2473
    _globals['_STOPCONNECTORREQUEST']._serialized_start = 2475
    _globals['_STOPCONNECTORREQUEST']._serialized_end = 2558
    _globals['_STOPCONNECTORRESPONSE']._serialized_start = 2560
    _globals['_STOPCONNECTORRESPONSE']._serialized_end = 2583
    _globals['_MANAGEDKAFKACONNECT']._serialized_start = 2586
    _globals['_MANAGEDKAFKACONNECT']._serialized_end = 5789