"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.kms.v1 import resources_pb2 as google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2
from .....google.cloud.kms.v1 import service_pb2 as google_dot_cloud_dot_kms_dot_v1_dot_service__pb2
GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/kms/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class KeyManagementServiceStub(object):
    """Google Cloud Key Management Service

    Manages cryptographic keys and operations using those keys. Implements a REST
    model with the following objects:

    * [KeyRing][google.cloud.kms.v1.KeyRing]
    * [CryptoKey][google.cloud.kms.v1.CryptoKey]
    * [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
    * [ImportJob][google.cloud.kms.v1.ImportJob]

    If you are using manual gRPC libraries, see
    [Using gRPC with Cloud KMS](https://cloud.google.com/kms/docs/grpc).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListKeyRings = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/ListKeyRings', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListKeyRingsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListKeyRingsResponse.FromString, _registered_method=True)
        self.ListCryptoKeys = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/ListCryptoKeys', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListCryptoKeysRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListCryptoKeysResponse.FromString, _registered_method=True)
        self.ListCryptoKeyVersions = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/ListCryptoKeyVersions', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListCryptoKeyVersionsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListCryptoKeyVersionsResponse.FromString, _registered_method=True)
        self.ListImportJobs = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/ListImportJobs', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListImportJobsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListImportJobsResponse.FromString, _registered_method=True)
        self.GetKeyRing = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/GetKeyRing', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetKeyRingRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.KeyRing.FromString, _registered_method=True)
        self.GetCryptoKey = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/GetCryptoKey', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetCryptoKeyRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKey.FromString, _registered_method=True)
        self.GetCryptoKeyVersion = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/GetCryptoKeyVersion', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetCryptoKeyVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.FromString, _registered_method=True)
        self.GetPublicKey = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/GetPublicKey', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetPublicKeyRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.PublicKey.FromString, _registered_method=True)
        self.GetImportJob = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/GetImportJob', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetImportJobRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.ImportJob.FromString, _registered_method=True)
        self.CreateKeyRing = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/CreateKeyRing', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.CreateKeyRingRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.KeyRing.FromString, _registered_method=True)
        self.CreateCryptoKey = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/CreateCryptoKey', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.CreateCryptoKeyRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKey.FromString, _registered_method=True)
        self.CreateCryptoKeyVersion = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/CreateCryptoKeyVersion', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.CreateCryptoKeyVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.FromString, _registered_method=True)
        self.ImportCryptoKeyVersion = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/ImportCryptoKeyVersion', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ImportCryptoKeyVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.FromString, _registered_method=True)
        self.CreateImportJob = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/CreateImportJob', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.CreateImportJobRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.ImportJob.FromString, _registered_method=True)
        self.UpdateCryptoKey = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/UpdateCryptoKey', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.UpdateCryptoKeyRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKey.FromString, _registered_method=True)
        self.UpdateCryptoKeyVersion = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/UpdateCryptoKeyVersion', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.UpdateCryptoKeyVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.FromString, _registered_method=True)
        self.UpdateCryptoKeyPrimaryVersion = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/UpdateCryptoKeyPrimaryVersion', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.UpdateCryptoKeyPrimaryVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKey.FromString, _registered_method=True)
        self.DestroyCryptoKeyVersion = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/DestroyCryptoKeyVersion', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DestroyCryptoKeyVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.FromString, _registered_method=True)
        self.RestoreCryptoKeyVersion = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/RestoreCryptoKeyVersion', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RestoreCryptoKeyVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.FromString, _registered_method=True)
        self.Encrypt = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/Encrypt', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.EncryptRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.EncryptResponse.FromString, _registered_method=True)
        self.Decrypt = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/Decrypt', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DecryptRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DecryptResponse.FromString, _registered_method=True)
        self.RawEncrypt = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/RawEncrypt', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RawEncryptRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RawEncryptResponse.FromString, _registered_method=True)
        self.RawDecrypt = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/RawDecrypt', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RawDecryptRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RawDecryptResponse.FromString, _registered_method=True)
        self.AsymmetricSign = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/AsymmetricSign', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.AsymmetricSignRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.AsymmetricSignResponse.FromString, _registered_method=True)
        self.AsymmetricDecrypt = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/AsymmetricDecrypt', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.AsymmetricDecryptRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.AsymmetricDecryptResponse.FromString, _registered_method=True)
        self.MacSign = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/MacSign', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.MacSignRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.MacSignResponse.FromString, _registered_method=True)
        self.MacVerify = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/MacVerify', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.MacVerifyRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.MacVerifyResponse.FromString, _registered_method=True)
        self.Decapsulate = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/Decapsulate', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DecapsulateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DecapsulateResponse.FromString, _registered_method=True)
        self.GenerateRandomBytes = channel.unary_unary('/google.cloud.kms.v1.KeyManagementService/GenerateRandomBytes', request_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GenerateRandomBytesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GenerateRandomBytesResponse.FromString, _registered_method=True)

class KeyManagementServiceServicer(object):
    """Google Cloud Key Management Service

    Manages cryptographic keys and operations using those keys. Implements a REST
    model with the following objects:

    * [KeyRing][google.cloud.kms.v1.KeyRing]
    * [CryptoKey][google.cloud.kms.v1.CryptoKey]
    * [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
    * [ImportJob][google.cloud.kms.v1.ImportJob]

    If you are using manual gRPC libraries, see
    [Using gRPC with Cloud KMS](https://cloud.google.com/kms/docs/grpc).
    """

    def ListKeyRings(self, request, context):
        """Lists [KeyRings][google.cloud.kms.v1.KeyRing].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCryptoKeys(self, request, context):
        """Lists [CryptoKeys][google.cloud.kms.v1.CryptoKey].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCryptoKeyVersions(self, request, context):
        """Lists [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListImportJobs(self, request, context):
        """Lists [ImportJobs][google.cloud.kms.v1.ImportJob].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetKeyRing(self, request, context):
        """Returns metadata for a given [KeyRing][google.cloud.kms.v1.KeyRing].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCryptoKey(self, request, context):
        """Returns metadata for a given [CryptoKey][google.cloud.kms.v1.CryptoKey], as
        well as its [primary][google.cloud.kms.v1.CryptoKey.primary]
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCryptoKeyVersion(self, request, context):
        """Returns metadata for a given
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPublicKey(self, request, context):
        """Returns the public key for the given
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]. The
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] must be
        [ASYMMETRIC_SIGN][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ASYMMETRIC_SIGN]
        or
        [ASYMMETRIC_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ASYMMETRIC_DECRYPT].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetImportJob(self, request, context):
        """Returns metadata for a given [ImportJob][google.cloud.kms.v1.ImportJob].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateKeyRing(self, request, context):
        """Create a new [KeyRing][google.cloud.kms.v1.KeyRing] in a given Project and
        Location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCryptoKey(self, request, context):
        """Create a new [CryptoKey][google.cloud.kms.v1.CryptoKey] within a
        [KeyRing][google.cloud.kms.v1.KeyRing].

        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] and
        [CryptoKey.version_template.algorithm][google.cloud.kms.v1.CryptoKeyVersionTemplate.algorithm]
        are required.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCryptoKeyVersion(self, request, context):
        """Create a new [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] in a
        [CryptoKey][google.cloud.kms.v1.CryptoKey].

        The server will assign the next sequential id. If unset,
        [state][google.cloud.kms.v1.CryptoKeyVersion.state] will be set to
        [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportCryptoKeyVersion(self, request, context):
        """Import wrapped key material into a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].

        All requests must specify a [CryptoKey][google.cloud.kms.v1.CryptoKey]. If
        a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] is additionally
        specified in the request, key material will be reimported into that
        version. Otherwise, a new version will be created, and will be assigned the
        next sequential id within the [CryptoKey][google.cloud.kms.v1.CryptoKey].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateImportJob(self, request, context):
        """Create a new [ImportJob][google.cloud.kms.v1.ImportJob] within a
        [KeyRing][google.cloud.kms.v1.KeyRing].

        [ImportJob.import_method][google.cloud.kms.v1.ImportJob.import_method] is
        required.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCryptoKey(self, request, context):
        """Update a [CryptoKey][google.cloud.kms.v1.CryptoKey].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCryptoKeyVersion(self, request, context):
        """Update a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]'s
        metadata.

        [state][google.cloud.kms.v1.CryptoKeyVersion.state] may be changed between
        [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
        and
        [DISABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DISABLED]
        using this method. See
        [DestroyCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DestroyCryptoKeyVersion]
        and
        [RestoreCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersion]
        to move between other states.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCryptoKeyPrimaryVersion(self, request, context):
        """Update the version of a [CryptoKey][google.cloud.kms.v1.CryptoKey] that
        will be used in
        [Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt].

        Returns an error if called on a key whose purpose is not
        [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DestroyCryptoKeyVersion(self, request, context):
        """Schedule a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] for
        destruction.

        Upon calling this method,
        [CryptoKeyVersion.state][google.cloud.kms.v1.CryptoKeyVersion.state] will
        be set to
        [DESTROY_SCHEDULED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROY_SCHEDULED],
        and [destroy_time][google.cloud.kms.v1.CryptoKeyVersion.destroy_time] will
        be set to the time
        [destroy_scheduled_duration][google.cloud.kms.v1.CryptoKey.destroy_scheduled_duration]
        in the future. At that time, the
        [state][google.cloud.kms.v1.CryptoKeyVersion.state] will automatically
        change to
        [DESTROYED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROYED],
        and the key material will be irrevocably destroyed.

        Before the
        [destroy_time][google.cloud.kms.v1.CryptoKeyVersion.destroy_time] is
        reached,
        [RestoreCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersion]
        may be called to reverse the process.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RestoreCryptoKeyVersion(self, request, context):
        """Restore a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] in the
        [DESTROY_SCHEDULED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROY_SCHEDULED]
        state.

        Upon restoration of the CryptoKeyVersion,
        [state][google.cloud.kms.v1.CryptoKeyVersion.state] will be set to
        [DISABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DISABLED],
        and [destroy_time][google.cloud.kms.v1.CryptoKeyVersion.destroy_time] will
        be cleared.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Encrypt(self, request, context):
        """Encrypts data, so that it can only be recovered by a call to
        [Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt]. The
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] must be
        [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Decrypt(self, request, context):
        """Decrypts data that was protected by
        [Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt]. The
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] must be
        [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RawEncrypt(self, request, context):
        """Encrypts data using portable cryptographic primitives. Most users should
        choose [Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt] and
        [Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt] rather than
        their raw counterparts. The
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] must be
        [RAW_ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.RAW_ENCRYPT_DECRYPT].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RawDecrypt(self, request, context):
        """Decrypts data that was originally encrypted using a raw cryptographic
        mechanism. The [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose]
        must be
        [RAW_ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.RAW_ENCRYPT_DECRYPT].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AsymmetricSign(self, request, context):
        """Signs data using a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
        with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose]
        ASYMMETRIC_SIGN, producing a signature that can be verified with the public
        key retrieved from
        [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AsymmetricDecrypt(self, request, context):
        """Decrypts data that was encrypted with a public key retrieved from
        [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey]
        corresponding to a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
        with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose]
        ASYMMETRIC_DECRYPT.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MacSign(self, request, context):
        """Signs data using a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
        with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] MAC,
        producing a tag that can be verified by another source with the same key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MacVerify(self, request, context):
        """Verifies MAC tag using a
        [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] with
        [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose] MAC, and returns
        a response that indicates whether or not the verification was successful.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Decapsulate(self, request, context):
        """Decapsulates data that was encapsulated with a public key retrieved from
        [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey]
        corresponding to a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
        with [CryptoKey.purpose][google.cloud.kms.v1.CryptoKey.purpose]
        KEY_ENCAPSULATION.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateRandomBytes(self, request, context):
        """Generate random bytes using the Cloud KMS randomness source in the provided
        location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_KeyManagementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListKeyRings': grpc.unary_unary_rpc_method_handler(servicer.ListKeyRings, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListKeyRingsRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListKeyRingsResponse.SerializeToString), 'ListCryptoKeys': grpc.unary_unary_rpc_method_handler(servicer.ListCryptoKeys, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListCryptoKeysRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListCryptoKeysResponse.SerializeToString), 'ListCryptoKeyVersions': grpc.unary_unary_rpc_method_handler(servicer.ListCryptoKeyVersions, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListCryptoKeyVersionsRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListCryptoKeyVersionsResponse.SerializeToString), 'ListImportJobs': grpc.unary_unary_rpc_method_handler(servicer.ListImportJobs, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListImportJobsRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListImportJobsResponse.SerializeToString), 'GetKeyRing': grpc.unary_unary_rpc_method_handler(servicer.GetKeyRing, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetKeyRingRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.KeyRing.SerializeToString), 'GetCryptoKey': grpc.unary_unary_rpc_method_handler(servicer.GetCryptoKey, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetCryptoKeyRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKey.SerializeToString), 'GetCryptoKeyVersion': grpc.unary_unary_rpc_method_handler(servicer.GetCryptoKeyVersion, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetCryptoKeyVersionRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.SerializeToString), 'GetPublicKey': grpc.unary_unary_rpc_method_handler(servicer.GetPublicKey, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetPublicKeyRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.PublicKey.SerializeToString), 'GetImportJob': grpc.unary_unary_rpc_method_handler(servicer.GetImportJob, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetImportJobRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.ImportJob.SerializeToString), 'CreateKeyRing': grpc.unary_unary_rpc_method_handler(servicer.CreateKeyRing, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.CreateKeyRingRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.KeyRing.SerializeToString), 'CreateCryptoKey': grpc.unary_unary_rpc_method_handler(servicer.CreateCryptoKey, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.CreateCryptoKeyRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKey.SerializeToString), 'CreateCryptoKeyVersion': grpc.unary_unary_rpc_method_handler(servicer.CreateCryptoKeyVersion, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.CreateCryptoKeyVersionRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.SerializeToString), 'ImportCryptoKeyVersion': grpc.unary_unary_rpc_method_handler(servicer.ImportCryptoKeyVersion, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ImportCryptoKeyVersionRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.SerializeToString), 'CreateImportJob': grpc.unary_unary_rpc_method_handler(servicer.CreateImportJob, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.CreateImportJobRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.ImportJob.SerializeToString), 'UpdateCryptoKey': grpc.unary_unary_rpc_method_handler(servicer.UpdateCryptoKey, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.UpdateCryptoKeyRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKey.SerializeToString), 'UpdateCryptoKeyVersion': grpc.unary_unary_rpc_method_handler(servicer.UpdateCryptoKeyVersion, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.UpdateCryptoKeyVersionRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.SerializeToString), 'UpdateCryptoKeyPrimaryVersion': grpc.unary_unary_rpc_method_handler(servicer.UpdateCryptoKeyPrimaryVersion, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.UpdateCryptoKeyPrimaryVersionRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKey.SerializeToString), 'DestroyCryptoKeyVersion': grpc.unary_unary_rpc_method_handler(servicer.DestroyCryptoKeyVersion, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DestroyCryptoKeyVersionRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.SerializeToString), 'RestoreCryptoKeyVersion': grpc.unary_unary_rpc_method_handler(servicer.RestoreCryptoKeyVersion, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RestoreCryptoKeyVersionRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.SerializeToString), 'Encrypt': grpc.unary_unary_rpc_method_handler(servicer.Encrypt, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.EncryptRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.EncryptResponse.SerializeToString), 'Decrypt': grpc.unary_unary_rpc_method_handler(servicer.Decrypt, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DecryptRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DecryptResponse.SerializeToString), 'RawEncrypt': grpc.unary_unary_rpc_method_handler(servicer.RawEncrypt, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RawEncryptRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RawEncryptResponse.SerializeToString), 'RawDecrypt': grpc.unary_unary_rpc_method_handler(servicer.RawDecrypt, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RawDecryptRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RawDecryptResponse.SerializeToString), 'AsymmetricSign': grpc.unary_unary_rpc_method_handler(servicer.AsymmetricSign, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.AsymmetricSignRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.AsymmetricSignResponse.SerializeToString), 'AsymmetricDecrypt': grpc.unary_unary_rpc_method_handler(servicer.AsymmetricDecrypt, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.AsymmetricDecryptRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.AsymmetricDecryptResponse.SerializeToString), 'MacSign': grpc.unary_unary_rpc_method_handler(servicer.MacSign, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.MacSignRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.MacSignResponse.SerializeToString), 'MacVerify': grpc.unary_unary_rpc_method_handler(servicer.MacVerify, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.MacVerifyRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.MacVerifyResponse.SerializeToString), 'Decapsulate': grpc.unary_unary_rpc_method_handler(servicer.Decapsulate, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DecapsulateRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DecapsulateResponse.SerializeToString), 'GenerateRandomBytes': grpc.unary_unary_rpc_method_handler(servicer.GenerateRandomBytes, request_deserializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GenerateRandomBytesRequest.FromString, response_serializer=google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GenerateRandomBytesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.kms.v1.KeyManagementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.kms.v1.KeyManagementService', rpc_method_handlers)

class KeyManagementService(object):
    """Google Cloud Key Management Service

    Manages cryptographic keys and operations using those keys. Implements a REST
    model with the following objects:

    * [KeyRing][google.cloud.kms.v1.KeyRing]
    * [CryptoKey][google.cloud.kms.v1.CryptoKey]
    * [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
    * [ImportJob][google.cloud.kms.v1.ImportJob]

    If you are using manual gRPC libraries, see
    [Using gRPC with Cloud KMS](https://cloud.google.com/kms/docs/grpc).
    """

    @staticmethod
    def ListKeyRings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/ListKeyRings', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListKeyRingsRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListKeyRingsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListCryptoKeys(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/ListCryptoKeys', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListCryptoKeysRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListCryptoKeysResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListCryptoKeyVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/ListCryptoKeyVersions', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListCryptoKeyVersionsRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListCryptoKeyVersionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListImportJobs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/ListImportJobs', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListImportJobsRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ListImportJobsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetKeyRing(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/GetKeyRing', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetKeyRingRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.KeyRing.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCryptoKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/GetCryptoKey', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetCryptoKeyRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKey.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCryptoKeyVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/GetCryptoKeyVersion', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetCryptoKeyVersionRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetPublicKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/GetPublicKey', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetPublicKeyRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.PublicKey.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetImportJob(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/GetImportJob', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GetImportJobRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.ImportJob.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateKeyRing(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/CreateKeyRing', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.CreateKeyRingRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.KeyRing.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateCryptoKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/CreateCryptoKey', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.CreateCryptoKeyRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKey.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateCryptoKeyVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/CreateCryptoKeyVersion', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.CreateCryptoKeyVersionRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ImportCryptoKeyVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/ImportCryptoKeyVersion', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.ImportCryptoKeyVersionRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateImportJob(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/CreateImportJob', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.CreateImportJobRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.ImportJob.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCryptoKey(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/UpdateCryptoKey', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.UpdateCryptoKeyRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKey.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCryptoKeyVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/UpdateCryptoKeyVersion', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.UpdateCryptoKeyVersionRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateCryptoKeyPrimaryVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/UpdateCryptoKeyPrimaryVersion', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.UpdateCryptoKeyPrimaryVersionRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKey.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DestroyCryptoKeyVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/DestroyCryptoKeyVersion', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DestroyCryptoKeyVersionRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RestoreCryptoKeyVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/RestoreCryptoKeyVersion', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RestoreCryptoKeyVersionRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_resources__pb2.CryptoKeyVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def Encrypt(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/Encrypt', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.EncryptRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.EncryptResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def Decrypt(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/Decrypt', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DecryptRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DecryptResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RawEncrypt(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/RawEncrypt', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RawEncryptRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RawEncryptResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def RawDecrypt(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/RawDecrypt', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RawDecryptRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.RawDecryptResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def AsymmetricSign(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/AsymmetricSign', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.AsymmetricSignRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.AsymmetricSignResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def AsymmetricDecrypt(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/AsymmetricDecrypt', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.AsymmetricDecryptRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.AsymmetricDecryptResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def MacSign(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/MacSign', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.MacSignRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.MacSignResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def MacVerify(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/MacVerify', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.MacVerifyRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.MacVerifyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def Decapsulate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/Decapsulate', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DecapsulateRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.DecapsulateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GenerateRandomBytes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.kms.v1.KeyManagementService/GenerateRandomBytes', google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GenerateRandomBytesRequest.SerializeToString, google_dot_cloud_dot_kms_dot_v1_dot_service__pb2.GenerateRandomBytesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)