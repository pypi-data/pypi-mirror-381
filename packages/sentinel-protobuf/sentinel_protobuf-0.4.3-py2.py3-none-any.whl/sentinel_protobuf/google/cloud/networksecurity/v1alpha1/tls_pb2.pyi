from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GrpcEndpoint(_message.Message):
    __slots__ = ('target_uri',)
    TARGET_URI_FIELD_NUMBER: _ClassVar[int]
    target_uri: str

    def __init__(self, target_uri: _Optional[str]=...) -> None:
        ...

class ValidationCA(_message.Message):
    __slots__ = ('ca_cert_path', 'grpc_endpoint', 'certificate_provider_instance')
    CA_CERT_PATH_FIELD_NUMBER: _ClassVar[int]
    GRPC_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_PROVIDER_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    ca_cert_path: str
    grpc_endpoint: GrpcEndpoint
    certificate_provider_instance: CertificateProviderInstance

    def __init__(self, ca_cert_path: _Optional[str]=..., grpc_endpoint: _Optional[_Union[GrpcEndpoint, _Mapping]]=..., certificate_provider_instance: _Optional[_Union[CertificateProviderInstance, _Mapping]]=...) -> None:
        ...

class CertificateProviderInstance(_message.Message):
    __slots__ = ('plugin_instance',)
    PLUGIN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    plugin_instance: str

    def __init__(self, plugin_instance: _Optional[str]=...) -> None:
        ...

class CertificateProvider(_message.Message):
    __slots__ = ('local_filepath', 'grpc_endpoint', 'certificate_provider_instance')

    class TlsCertificateFiles(_message.Message):
        __slots__ = ('certificate_path', 'private_key_path')
        CERTIFICATE_PATH_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_KEY_PATH_FIELD_NUMBER: _ClassVar[int]
        certificate_path: str
        private_key_path: str

        def __init__(self, certificate_path: _Optional[str]=..., private_key_path: _Optional[str]=...) -> None:
            ...
    LOCAL_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    GRPC_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_PROVIDER_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    local_filepath: CertificateProvider.TlsCertificateFiles
    grpc_endpoint: GrpcEndpoint
    certificate_provider_instance: CertificateProviderInstance

    def __init__(self, local_filepath: _Optional[_Union[CertificateProvider.TlsCertificateFiles, _Mapping]]=..., grpc_endpoint: _Optional[_Union[GrpcEndpoint, _Mapping]]=..., certificate_provider_instance: _Optional[_Union[CertificateProviderInstance, _Mapping]]=...) -> None:
        ...