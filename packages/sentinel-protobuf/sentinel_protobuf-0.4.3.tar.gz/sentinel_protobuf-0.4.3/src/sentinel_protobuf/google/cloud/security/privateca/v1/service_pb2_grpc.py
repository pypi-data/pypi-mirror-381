"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ......google.cloud.security.privateca.v1 import resources_pb2 as google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2
from ......google.cloud.security.privateca.v1 import service_pb2 as google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/security/privateca/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class CertificateAuthorityServiceStub(object):
    """[Certificate Authority
    Service][google.cloud.security.privateca.v1.CertificateAuthorityService]
    manages private certificate authorities and issued certificates.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateCertificate = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificate', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.CreateCertificateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.Certificate.FromString, _registered_method=True)
        self.GetCertificate = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificate', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCertificateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.Certificate.FromString, _registered_method=True)
        self.ListCertificates = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificates', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificatesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificatesResponse.FromString, _registered_method=True)
        self.RevokeCertificate = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/RevokeCertificate', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.RevokeCertificateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.Certificate.FromString, _registered_method=True)
        self.UpdateCertificate = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificate', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCertificateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.Certificate.FromString, _registered_method=True)
        self.ActivateCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/ActivateCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ActivateCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.CreateCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.CreateCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DisableCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/DisableCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.DisableCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.EnableCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/EnableCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.EnableCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.FetchCertificateAuthorityCsr = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/FetchCertificateAuthorityCsr', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.FetchCertificateAuthorityCsrRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.FetchCertificateAuthorityCsrResponse.FromString, _registered_method=True)
        self.GetCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.CertificateAuthority.FromString, _registered_method=True)
        self.ListCertificateAuthorities = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateAuthorities', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateAuthoritiesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateAuthoritiesResponse.FromString, _registered_method=True)
        self.UndeleteCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/UndeleteCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UndeleteCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.DeleteCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateCertificateAuthority = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateAuthority', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCertificateAuthorityRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.CreateCaPool = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCaPool', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.CreateCaPoolRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateCaPool = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCaPool', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCaPoolRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.GetCaPool = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCaPool', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCaPoolRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.CaPool.FromString, _registered_method=True)
        self.ListCaPools = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCaPools', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCaPoolsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCaPoolsResponse.FromString, _registered_method=True)
        self.DeleteCaPool = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCaPool', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.DeleteCaPoolRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.FetchCaCerts = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/FetchCaCerts', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.FetchCaCertsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.FetchCaCertsResponse.FromString, _registered_method=True)
        self.GetCertificateRevocationList = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateRevocationList', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCertificateRevocationListRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.CertificateRevocationList.FromString, _registered_method=True)
        self.ListCertificateRevocationLists = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateRevocationLists', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateRevocationListsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateRevocationListsResponse.FromString, _registered_method=True)
        self.UpdateCertificateRevocationList = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateRevocationList', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCertificateRevocationListRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.CreateCertificateTemplate = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificateTemplate', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.CreateCertificateTemplateRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteCertificateTemplate = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCertificateTemplate', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.DeleteCertificateTemplateRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.GetCertificateTemplate = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateTemplate', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCertificateTemplateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.CertificateTemplate.FromString, _registered_method=True)
        self.ListCertificateTemplates = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateTemplates', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateTemplatesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateTemplatesResponse.FromString, _registered_method=True)
        self.UpdateCertificateTemplate = channel.unary_unary('/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateTemplate', request_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCertificateTemplateRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)

class CertificateAuthorityServiceServicer(object):
    """[Certificate Authority
    Service][google.cloud.security.privateca.v1.CertificateAuthorityService]
    manages private certificate authorities and issued certificates.
    """

    def CreateCertificate(self, request, context):
        """Create a new [Certificate][google.cloud.security.privateca.v1.Certificate]
        in a given Project, Location from a particular
        [CaPool][google.cloud.security.privateca.v1.CaPool].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCertificate(self, request, context):
        """Returns a [Certificate][google.cloud.security.privateca.v1.Certificate].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCertificates(self, request, context):
        """Lists [Certificates][google.cloud.security.privateca.v1.Certificate].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevokeCertificate(self, request, context):
        """Revoke a [Certificate][google.cloud.security.privateca.v1.Certificate].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCertificate(self, request, context):
        """Update a [Certificate][google.cloud.security.privateca.v1.Certificate].
        Currently, the only field you can update is the
        [labels][google.cloud.security.privateca.v1.Certificate.labels] field.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActivateCertificateAuthority(self, request, context):
        """Activate a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        that is in state
        [AWAITING_USER_ACTIVATION][google.cloud.security.privateca.v1.CertificateAuthority.State.AWAITING_USER_ACTIVATION]
        and is of type
        [SUBORDINATE][google.cloud.security.privateca.v1.CertificateAuthority.Type.SUBORDINATE].
        After the parent Certificate Authority signs a certificate signing request
        from
        [FetchCertificateAuthorityCsr][google.cloud.security.privateca.v1.CertificateAuthorityService.FetchCertificateAuthorityCsr],
        this method can complete the activation process.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCertificateAuthority(self, request, context):
        """Create a new
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        in a given Project and Location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableCertificateAuthority(self, request, context):
        """Disable a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableCertificateAuthority(self, request, context):
        """Enable a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchCertificateAuthorityCsr(self, request, context):
        """Fetch a certificate signing request (CSR) from a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        that is in state
        [AWAITING_USER_ACTIVATION][google.cloud.security.privateca.v1.CertificateAuthority.State.AWAITING_USER_ACTIVATION]
        and is of type
        [SUBORDINATE][google.cloud.security.privateca.v1.CertificateAuthority.Type.SUBORDINATE].
        The CSR must then be signed by the desired parent Certificate Authority,
        which could be another
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        resource, or could be an on-prem certificate authority. See also
        [ActivateCertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthorityService.ActivateCertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCertificateAuthority(self, request, context):
        """Returns a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCertificateAuthorities(self, request, context):
        """Lists
        [CertificateAuthorities][google.cloud.security.privateca.v1.CertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UndeleteCertificateAuthority(self, request, context):
        """Undelete a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority]
        that has been deleted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCertificateAuthority(self, request, context):
        """Delete a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCertificateAuthority(self, request, context):
        """Update a
        [CertificateAuthority][google.cloud.security.privateca.v1.CertificateAuthority].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCaPool(self, request, context):
        """Create a [CaPool][google.cloud.security.privateca.v1.CaPool].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCaPool(self, request, context):
        """Update a [CaPool][google.cloud.security.privateca.v1.CaPool].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCaPool(self, request, context):
        """Returns a [CaPool][google.cloud.security.privateca.v1.CaPool].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCaPools(self, request, context):
        """Lists [CaPools][google.cloud.security.privateca.v1.CaPool].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCaPool(self, request, context):
        """Delete a [CaPool][google.cloud.security.privateca.v1.CaPool].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchCaCerts(self, request, context):
        """FetchCaCerts returns the current trust anchor for the
        [CaPool][google.cloud.security.privateca.v1.CaPool]. This will include CA
        certificate chains for all certificate authorities in the ENABLED,
        DISABLED, or STAGED states.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCertificateRevocationList(self, request, context):
        """Returns a
        [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCertificateRevocationLists(self, request, context):
        """Lists
        [CertificateRevocationLists][google.cloud.security.privateca.v1.CertificateRevocationList].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCertificateRevocationList(self, request, context):
        """Update a
        [CertificateRevocationList][google.cloud.security.privateca.v1.CertificateRevocationList].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCertificateTemplate(self, request, context):
        """Create a new
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate]
        in a given Project and Location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCertificateTemplate(self, request, context):
        """DeleteCertificateTemplate deletes a
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCertificateTemplate(self, request, context):
        """Returns a
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCertificateTemplates(self, request, context):
        """Lists
        [CertificateTemplates][google.cloud.security.privateca.v1.CertificateTemplate].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCertificateTemplate(self, request, context):
        """Update a
        [CertificateTemplate][google.cloud.security.privateca.v1.CertificateTemplate].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_CertificateAuthorityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateCertificate': grpc.unary_unary_rpc_method_handler(servicer.CreateCertificate, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.CreateCertificateRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.Certificate.SerializeToString), 'GetCertificate': grpc.unary_unary_rpc_method_handler(servicer.GetCertificate, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCertificateRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.Certificate.SerializeToString), 'ListCertificates': grpc.unary_unary_rpc_method_handler(servicer.ListCertificates, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificatesRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificatesResponse.SerializeToString), 'RevokeCertificate': grpc.unary_unary_rpc_method_handler(servicer.RevokeCertificate, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.RevokeCertificateRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.Certificate.SerializeToString), 'UpdateCertificate': grpc.unary_unary_rpc_method_handler(servicer.UpdateCertificate, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCertificateRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.Certificate.SerializeToString), 'ActivateCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.ActivateCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ActivateCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'CreateCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.CreateCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.CreateCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DisableCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.DisableCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.DisableCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'EnableCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.EnableCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.EnableCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'FetchCertificateAuthorityCsr': grpc.unary_unary_rpc_method_handler(servicer.FetchCertificateAuthorityCsr, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.FetchCertificateAuthorityCsrRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.FetchCertificateAuthorityCsrResponse.SerializeToString), 'GetCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.GetCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCertificateAuthorityRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.CertificateAuthority.SerializeToString), 'ListCertificateAuthorities': grpc.unary_unary_rpc_method_handler(servicer.ListCertificateAuthorities, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateAuthoritiesRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateAuthoritiesResponse.SerializeToString), 'UndeleteCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.UndeleteCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UndeleteCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.DeleteCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.DeleteCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateCertificateAuthority': grpc.unary_unary_rpc_method_handler(servicer.UpdateCertificateAuthority, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCertificateAuthorityRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'CreateCaPool': grpc.unary_unary_rpc_method_handler(servicer.CreateCaPool, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.CreateCaPoolRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateCaPool': grpc.unary_unary_rpc_method_handler(servicer.UpdateCaPool, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCaPoolRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'GetCaPool': grpc.unary_unary_rpc_method_handler(servicer.GetCaPool, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCaPoolRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.CaPool.SerializeToString), 'ListCaPools': grpc.unary_unary_rpc_method_handler(servicer.ListCaPools, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCaPoolsRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCaPoolsResponse.SerializeToString), 'DeleteCaPool': grpc.unary_unary_rpc_method_handler(servicer.DeleteCaPool, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.DeleteCaPoolRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'FetchCaCerts': grpc.unary_unary_rpc_method_handler(servicer.FetchCaCerts, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.FetchCaCertsRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.FetchCaCertsResponse.SerializeToString), 'GetCertificateRevocationList': grpc.unary_unary_rpc_method_handler(servicer.GetCertificateRevocationList, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCertificateRevocationListRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.CertificateRevocationList.SerializeToString), 'ListCertificateRevocationLists': grpc.unary_unary_rpc_method_handler(servicer.ListCertificateRevocationLists, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateRevocationListsRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateRevocationListsResponse.SerializeToString), 'UpdateCertificateRevocationList': grpc.unary_unary_rpc_method_handler(servicer.UpdateCertificateRevocationList, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCertificateRevocationListRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'CreateCertificateTemplate': grpc.unary_unary_rpc_method_handler(servicer.CreateCertificateTemplate, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.CreateCertificateTemplateRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteCertificateTemplate': grpc.unary_unary_rpc_method_handler(servicer.DeleteCertificateTemplate, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.DeleteCertificateTemplateRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'GetCertificateTemplate': grpc.unary_unary_rpc_method_handler(servicer.GetCertificateTemplate, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCertificateTemplateRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.CertificateTemplate.SerializeToString), 'ListCertificateTemplates': grpc.unary_unary_rpc_method_handler(servicer.ListCertificateTemplates, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateTemplatesRequest.FromString, response_serializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateTemplatesResponse.SerializeToString), 'UpdateCertificateTemplate': grpc.unary_unary_rpc_method_handler(servicer.UpdateCertificateTemplate, request_deserializer=google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCertificateTemplateRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.security.privateca.v1.CertificateAuthorityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.security.privateca.v1.CertificateAuthorityService', rpc_method_handlers)

class CertificateAuthorityService(object):
    """[Certificate Authority
    Service][google.cloud.security.privateca.v1.CertificateAuthorityService]
    manages private certificate authorities and issued certificates.
    """

    @staticmethod
    def CreateCertificate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificate', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.CreateCertificateRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.Certificate.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCertificate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificate', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCertificateRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.Certificate.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListCertificates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificates', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificatesRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificatesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RevokeCertificate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/RevokeCertificate', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.RevokeCertificateRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.Certificate.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCertificate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificate', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCertificateRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.Certificate.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ActivateCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/ActivateCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ActivateCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.CreateCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DisableCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/DisableCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.DisableCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def EnableCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/EnableCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.EnableCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def FetchCertificateAuthorityCsr(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/FetchCertificateAuthorityCsr', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.FetchCertificateAuthorityCsrRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.FetchCertificateAuthorityCsrResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCertificateAuthorityRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.CertificateAuthority.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListCertificateAuthorities(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateAuthorities', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateAuthoritiesRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateAuthoritiesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UndeleteCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/UndeleteCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UndeleteCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.DeleteCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCertificateAuthority(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateAuthority', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCertificateAuthorityRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateCaPool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCaPool', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.CreateCaPoolRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCaPool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCaPool', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCaPoolRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCaPool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCaPool', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCaPoolRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.CaPool.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListCaPools(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCaPools', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCaPoolsRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCaPoolsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteCaPool(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCaPool', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.DeleteCaPoolRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def FetchCaCerts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/FetchCaCerts', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.FetchCaCertsRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.FetchCaCertsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCertificateRevocationList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateRevocationList', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCertificateRevocationListRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.CertificateRevocationList.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListCertificateRevocationLists(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateRevocationLists', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateRevocationListsRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateRevocationListsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCertificateRevocationList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateRevocationList', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCertificateRevocationListRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateCertificateTemplate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificateTemplate', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.CreateCertificateTemplateRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteCertificateTemplate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCertificateTemplate', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.DeleteCertificateTemplateRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCertificateTemplate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateTemplate', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.GetCertificateTemplateRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_resources__pb2.CertificateTemplate.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListCertificateTemplates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateTemplates', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateTemplatesRequest.SerializeToString, google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.ListCertificateTemplatesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCertificateTemplate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateTemplate', google_dot_cloud_dot_security_dot_privateca_dot_v1_dot_service__pb2.UpdateCertificateTemplateRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)