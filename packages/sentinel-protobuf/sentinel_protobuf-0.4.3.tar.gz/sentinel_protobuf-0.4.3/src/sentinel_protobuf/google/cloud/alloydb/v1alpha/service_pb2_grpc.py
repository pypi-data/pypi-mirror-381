"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.alloydb.v1alpha import resources_pb2 as google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2
from .....google.cloud.alloydb.v1alpha import service_pb2 as google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/alloydb/v1alpha/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class AlloyDBAdminStub(object):
    """Service describing handlers for resources
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListClusters = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ListClusters', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListClustersRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListClustersResponse.FromString, _registered_method=True)
        self.GetCluster = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/GetCluster', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetClusterRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.Cluster.FromString, _registered_method=True)
        self.CreateCluster = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateCluster', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateCluster = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/UpdateCluster', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpdateClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ExportCluster = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ExportCluster', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ExportClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ImportCluster = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ImportCluster', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ImportClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpgradeCluster = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/UpgradeCluster', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpgradeClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteCluster = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/DeleteCluster', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.DeleteClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.PromoteCluster = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/PromoteCluster', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.PromoteClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.SwitchoverCluster = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/SwitchoverCluster', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.SwitchoverClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.RestoreCluster = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/RestoreCluster', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.RestoreClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.CreateSecondaryCluster = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateSecondaryCluster', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateSecondaryClusterRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListInstances = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ListInstances', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListInstancesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListInstancesResponse.FromString, _registered_method=True)
        self.GetInstance = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/GetInstance', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetInstanceRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.Instance.FromString, _registered_method=True)
        self.CreateInstance = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateInstance', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.CreateSecondaryInstance = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateSecondaryInstance', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateSecondaryInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.BatchCreateInstances = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/BatchCreateInstances', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.BatchCreateInstancesRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateInstance = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/UpdateInstance', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpdateInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteInstance = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/DeleteInstance', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.DeleteInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.FailoverInstance = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/FailoverInstance', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.FailoverInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.InjectFault = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/InjectFault', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.InjectFaultRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.RestartInstance = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/RestartInstance', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.RestartInstanceRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ExecuteSql = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ExecuteSql', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ExecuteSqlRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ExecuteSqlResponse.FromString, _registered_method=True)
        self.ListBackups = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ListBackups', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListBackupsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListBackupsResponse.FromString, _registered_method=True)
        self.GetBackup = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/GetBackup', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetBackupRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.Backup.FromString, _registered_method=True)
        self.CreateBackup = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateBackup', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateBackupRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateBackup = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/UpdateBackup', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpdateBackupRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteBackup = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/DeleteBackup', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.DeleteBackupRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListSupportedDatabaseFlags = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ListSupportedDatabaseFlags', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListSupportedDatabaseFlagsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListSupportedDatabaseFlagsResponse.FromString, _registered_method=True)
        self.GenerateClientCertificate = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/GenerateClientCertificate', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GenerateClientCertificateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GenerateClientCertificateResponse.FromString, _registered_method=True)
        self.GetConnectionInfo = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/GetConnectionInfo', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetConnectionInfoRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.ConnectionInfo.FromString, _registered_method=True)
        self.ListUsers = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ListUsers', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListUsersRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListUsersResponse.FromString, _registered_method=True)
        self.GetUser = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/GetUser', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetUserRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.User.FromString, _registered_method=True)
        self.CreateUser = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateUser', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateUserRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.User.FromString, _registered_method=True)
        self.UpdateUser = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/UpdateUser', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpdateUserRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.User.FromString, _registered_method=True)
        self.DeleteUser = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/DeleteUser', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.DeleteUserRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.ListDatabases = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ListDatabases', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListDatabasesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListDatabasesResponse.FromString, _registered_method=True)
        self.CreateDatabase = channel.unary_unary('/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateDatabase', request_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateDatabaseRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.Database.FromString, _registered_method=True)

class AlloyDBAdminServicer(object):
    """Service describing handlers for resources
    """

    def ListClusters(self, request, context):
        """Lists Clusters in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCluster(self, request, context):
        """Gets details of a single Cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCluster(self, request, context):
        """Creates a new Cluster in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCluster(self, request, context):
        """Updates the parameters of a single Cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportCluster(self, request, context):
        """Exports data from the cluster.
        Imperative only.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportCluster(self, request, context):
        """Imports data to the cluster.
        Imperative only.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpgradeCluster(self, request, context):
        """Upgrades a single Cluster.
        Imperative only.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCluster(self, request, context):
        """Deletes a single Cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PromoteCluster(self, request, context):
        """Promotes a SECONDARY cluster. This turns down replication
        from the PRIMARY cluster and promotes a secondary cluster
        into its own standalone cluster.
        Imperative only.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SwitchoverCluster(self, request, context):
        """Switches the roles of PRIMARY and SECONDARY clusters without any data loss.
        This promotes the SECONDARY cluster to PRIMARY and sets up the original
        PRIMARY cluster to replicate from this newly promoted cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RestoreCluster(self, request, context):
        """Creates a new Cluster in a given project and location, with a volume
        restored from the provided source, either a backup ID or a point-in-time
        and a source cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSecondaryCluster(self, request, context):
        """Creates a cluster of type SECONDARY in the given location using
        the primary cluster as the source.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListInstances(self, request, context):
        """Lists Instances in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInstance(self, request, context):
        """Gets details of a single Instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateInstance(self, request, context):
        """Creates a new Instance in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSecondaryInstance(self, request, context):
        """Creates a new SECONDARY Instance in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchCreateInstances(self, request, context):
        """Creates new instances under the given project, location and cluster.
        There can be only one primary instance in a cluster. If the primary
        instance exists in the cluster as well as this request, then API will
        throw an error.
        The primary instance should exist before any read pool instance is
        created. If the primary instance is a part of the request payload, then
        the API will take care of creating instances in the correct order.
        This method is here to support Google-internal use cases, and is not meant
        for external customers to consume. Please do not start relying on it; its
        behavior is subject to change without notice.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateInstance(self, request, context):
        """Updates the parameters of a single Instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteInstance(self, request, context):
        """Deletes a single Instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FailoverInstance(self, request, context):
        """Forces a Failover for a highly available instance.
        Failover promotes the HA standby instance as the new primary.
        Imperative only.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InjectFault(self, request, context):
        """Injects fault in an instance.
        Imperative only.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RestartInstance(self, request, context):
        """Restart an Instance in a cluster.
        Imperative only.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteSql(self, request, context):
        """Executes a SQL statement in a database inside an AlloyDB instance.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBackups(self, request, context):
        """Lists Backups in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBackup(self, request, context):
        """Gets details of a single Backup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBackup(self, request, context):
        """Creates a new Backup in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBackup(self, request, context):
        """Updates the parameters of a single Backup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBackup(self, request, context):
        """Deletes a single Backup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSupportedDatabaseFlags(self, request, context):
        """Lists SupportedDatabaseFlags for a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateClientCertificate(self, request, context):
        """Generate a client certificate signed by a Cluster CA.
        The sole purpose of this endpoint is to support AlloyDB connectors and the
        Auth Proxy client. The endpoint's behavior is subject to change without
        notice, so do not rely on its behavior remaining constant. Future changes
        will not break AlloyDB connectors or the Auth Proxy client.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConnectionInfo(self, request, context):
        """Get instance metadata used for a connection.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsers(self, request, context):
        """Lists Users in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Gets details of a single User.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Creates a new User in a given project, location, and cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Updates the parameters of a single User.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Deletes a single User.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDatabases(self, request, context):
        """Lists Databases in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDatabase(self, request, context):
        """Creates a new Database in a given project, location, and cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_AlloyDBAdminServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListClusters': grpc.unary_unary_rpc_method_handler(servicer.ListClusters, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListClustersRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListClustersResponse.SerializeToString), 'GetCluster': grpc.unary_unary_rpc_method_handler(servicer.GetCluster, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetClusterRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.Cluster.SerializeToString), 'CreateCluster': grpc.unary_unary_rpc_method_handler(servicer.CreateCluster, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateCluster': grpc.unary_unary_rpc_method_handler(servicer.UpdateCluster, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpdateClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ExportCluster': grpc.unary_unary_rpc_method_handler(servicer.ExportCluster, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ExportClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ImportCluster': grpc.unary_unary_rpc_method_handler(servicer.ImportCluster, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ImportClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpgradeCluster': grpc.unary_unary_rpc_method_handler(servicer.UpgradeCluster, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpgradeClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteCluster': grpc.unary_unary_rpc_method_handler(servicer.DeleteCluster, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.DeleteClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'PromoteCluster': grpc.unary_unary_rpc_method_handler(servicer.PromoteCluster, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.PromoteClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'SwitchoverCluster': grpc.unary_unary_rpc_method_handler(servicer.SwitchoverCluster, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.SwitchoverClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'RestoreCluster': grpc.unary_unary_rpc_method_handler(servicer.RestoreCluster, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.RestoreClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'CreateSecondaryCluster': grpc.unary_unary_rpc_method_handler(servicer.CreateSecondaryCluster, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateSecondaryClusterRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListInstances': grpc.unary_unary_rpc_method_handler(servicer.ListInstances, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListInstancesRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListInstancesResponse.SerializeToString), 'GetInstance': grpc.unary_unary_rpc_method_handler(servicer.GetInstance, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetInstanceRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.Instance.SerializeToString), 'CreateInstance': grpc.unary_unary_rpc_method_handler(servicer.CreateInstance, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'CreateSecondaryInstance': grpc.unary_unary_rpc_method_handler(servicer.CreateSecondaryInstance, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateSecondaryInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'BatchCreateInstances': grpc.unary_unary_rpc_method_handler(servicer.BatchCreateInstances, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.BatchCreateInstancesRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateInstance': grpc.unary_unary_rpc_method_handler(servicer.UpdateInstance, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpdateInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteInstance': grpc.unary_unary_rpc_method_handler(servicer.DeleteInstance, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.DeleteInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'FailoverInstance': grpc.unary_unary_rpc_method_handler(servicer.FailoverInstance, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.FailoverInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'InjectFault': grpc.unary_unary_rpc_method_handler(servicer.InjectFault, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.InjectFaultRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'RestartInstance': grpc.unary_unary_rpc_method_handler(servicer.RestartInstance, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.RestartInstanceRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ExecuteSql': grpc.unary_unary_rpc_method_handler(servicer.ExecuteSql, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ExecuteSqlRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ExecuteSqlResponse.SerializeToString), 'ListBackups': grpc.unary_unary_rpc_method_handler(servicer.ListBackups, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListBackupsRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListBackupsResponse.SerializeToString), 'GetBackup': grpc.unary_unary_rpc_method_handler(servicer.GetBackup, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetBackupRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.Backup.SerializeToString), 'CreateBackup': grpc.unary_unary_rpc_method_handler(servicer.CreateBackup, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateBackupRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateBackup': grpc.unary_unary_rpc_method_handler(servicer.UpdateBackup, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpdateBackupRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteBackup': grpc.unary_unary_rpc_method_handler(servicer.DeleteBackup, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.DeleteBackupRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListSupportedDatabaseFlags': grpc.unary_unary_rpc_method_handler(servicer.ListSupportedDatabaseFlags, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListSupportedDatabaseFlagsRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListSupportedDatabaseFlagsResponse.SerializeToString), 'GenerateClientCertificate': grpc.unary_unary_rpc_method_handler(servicer.GenerateClientCertificate, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GenerateClientCertificateRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GenerateClientCertificateResponse.SerializeToString), 'GetConnectionInfo': grpc.unary_unary_rpc_method_handler(servicer.GetConnectionInfo, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetConnectionInfoRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.ConnectionInfo.SerializeToString), 'ListUsers': grpc.unary_unary_rpc_method_handler(servicer.ListUsers, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListUsersRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListUsersResponse.SerializeToString), 'GetUser': grpc.unary_unary_rpc_method_handler(servicer.GetUser, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetUserRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.User.SerializeToString), 'CreateUser': grpc.unary_unary_rpc_method_handler(servicer.CreateUser, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateUserRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.User.SerializeToString), 'UpdateUser': grpc.unary_unary_rpc_method_handler(servicer.UpdateUser, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpdateUserRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.User.SerializeToString), 'DeleteUser': grpc.unary_unary_rpc_method_handler(servicer.DeleteUser, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.DeleteUserRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'ListDatabases': grpc.unary_unary_rpc_method_handler(servicer.ListDatabases, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListDatabasesRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListDatabasesResponse.SerializeToString), 'CreateDatabase': grpc.unary_unary_rpc_method_handler(servicer.CreateDatabase, request_deserializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateDatabaseRequest.FromString, response_serializer=google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.Database.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.alloydb.v1alpha.AlloyDBAdmin', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.alloydb.v1alpha.AlloyDBAdmin', rpc_method_handlers)

class AlloyDBAdmin(object):
    """Service describing handlers for resources
    """

    @staticmethod
    def ListClusters(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ListClusters', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListClustersRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListClustersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/GetCluster', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetClusterRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.Cluster.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateCluster', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/UpdateCluster', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpdateClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ExportCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ExportCluster', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ExportClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ImportCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ImportCluster', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ImportClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpgradeCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/UpgradeCluster', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpgradeClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/DeleteCluster', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.DeleteClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def PromoteCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/PromoteCluster', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.PromoteClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SwitchoverCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/SwitchoverCluster', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.SwitchoverClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RestoreCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/RestoreCluster', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.RestoreClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateSecondaryCluster(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateSecondaryCluster', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateSecondaryClusterRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListInstances(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ListInstances', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListInstancesRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListInstancesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/GetInstance', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetInstanceRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.Instance.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateInstance', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateSecondaryInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateSecondaryInstance', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateSecondaryInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def BatchCreateInstances(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/BatchCreateInstances', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.BatchCreateInstancesRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/UpdateInstance', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpdateInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/DeleteInstance', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.DeleteInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def FailoverInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/FailoverInstance', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.FailoverInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def InjectFault(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/InjectFault', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.InjectFaultRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RestartInstance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/RestartInstance', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.RestartInstanceRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ExecuteSql(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ExecuteSql', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ExecuteSqlRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ExecuteSqlResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListBackups(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ListBackups', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListBackupsRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListBackupsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetBackup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/GetBackup', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetBackupRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.Backup.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateBackup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateBackup', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateBackupRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateBackup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/UpdateBackup', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpdateBackupRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteBackup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/DeleteBackup', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.DeleteBackupRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListSupportedDatabaseFlags(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ListSupportedDatabaseFlags', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListSupportedDatabaseFlagsRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListSupportedDatabaseFlagsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GenerateClientCertificate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/GenerateClientCertificate', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GenerateClientCertificateRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GenerateClientCertificateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetConnectionInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/GetConnectionInfo', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetConnectionInfoRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.ConnectionInfo.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListUsers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ListUsers', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListUsersRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListUsersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/GetUser', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.GetUserRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.User.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateUser', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateUserRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.User.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/UpdateUser', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.UpdateUserRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.User.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteUser(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/DeleteUser', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.DeleteUserRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListDatabases(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/ListDatabases', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListDatabasesRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.ListDatabasesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateDatabase(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.alloydb.v1alpha.AlloyDBAdmin/CreateDatabase', google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2.CreateDatabaseRequest.SerializeToString, google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2.Database.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)