"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networksecurity/v1alpha1/tls.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/networksecurity/v1alpha1/tls.proto\x12%google.cloud.networksecurity.v1alpha1\x1a\x1fgoogle/api/field_behavior.proto"\'\n\x0cGrpcEndpoint\x12\x17\n\ntarget_uri\x18\x01 \x01(\tB\x03\xe0A\x02"\xe9\x01\n\x0cValidationCA\x12\x16\n\x0cca_cert_path\x18\x01 \x01(\tH\x00\x12L\n\rgrpc_endpoint\x18\x02 \x01(\x0b23.google.cloud.networksecurity.v1alpha1.GrpcEndpointH\x00\x12k\n\x1dcertificate_provider_instance\x18\x03 \x01(\x0b2B.google.cloud.networksecurity.v1alpha1.CertificateProviderInstanceH\x00B\x06\n\x04type";\n\x1bCertificateProviderInstance\x12\x1c\n\x0fplugin_instance\x18\x01 \x01(\tB\x03\xe0A\x02"\x97\x03\n\x13CertificateProvider\x12h\n\x0elocal_filepath\x18\x01 \x01(\x0b2N.google.cloud.networksecurity.v1alpha1.CertificateProvider.TlsCertificateFilesH\x00\x12L\n\rgrpc_endpoint\x18\x02 \x01(\x0b23.google.cloud.networksecurity.v1alpha1.GrpcEndpointH\x00\x12k\n\x1dcertificate_provider_instance\x18\x03 \x01(\x0b2B.google.cloud.networksecurity.v1alpha1.CertificateProviderInstanceH\x00\x1aS\n\x13TlsCertificateFiles\x12\x1d\n\x10certificate_path\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10private_key_path\x18\x02 \x01(\tB\x03\xe0A\x02B\x06\n\x04typeB\x87\x02\n)com.google.cloud.networksecurity.v1alpha1B\x08TlsProtoP\x01ZScloud.google.com/go/networksecurity/apiv1alpha1/networksecuritypb;networksecuritypb\xaa\x02%Google.Cloud.NetworkSecurity.V1Alpha1\xca\x02%Google\\Cloud\\NetworkSecurity\\V1alpha1\xea\x02(Google::Cloud::NetworkSecurity::V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networksecurity.v1alpha1.tls_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.networksecurity.v1alpha1B\x08TlsProtoP\x01ZScloud.google.com/go/networksecurity/apiv1alpha1/networksecuritypb;networksecuritypb\xaa\x02%Google.Cloud.NetworkSecurity.V1Alpha1\xca\x02%Google\\Cloud\\NetworkSecurity\\V1alpha1\xea\x02(Google::Cloud::NetworkSecurity::V1alpha1'
    _globals['_GRPCENDPOINT'].fields_by_name['target_uri']._loaded_options = None
    _globals['_GRPCENDPOINT'].fields_by_name['target_uri']._serialized_options = b'\xe0A\x02'
    _globals['_CERTIFICATEPROVIDERINSTANCE'].fields_by_name['plugin_instance']._loaded_options = None
    _globals['_CERTIFICATEPROVIDERINSTANCE'].fields_by_name['plugin_instance']._serialized_options = b'\xe0A\x02'
    _globals['_CERTIFICATEPROVIDER_TLSCERTIFICATEFILES'].fields_by_name['certificate_path']._loaded_options = None
    _globals['_CERTIFICATEPROVIDER_TLSCERTIFICATEFILES'].fields_by_name['certificate_path']._serialized_options = b'\xe0A\x02'
    _globals['_CERTIFICATEPROVIDER_TLSCERTIFICATEFILES'].fields_by_name['private_key_path']._loaded_options = None
    _globals['_CERTIFICATEPROVIDER_TLSCERTIFICATEFILES'].fields_by_name['private_key_path']._serialized_options = b'\xe0A\x02'
    _globals['_GRPCENDPOINT']._serialized_start = 123
    _globals['_GRPCENDPOINT']._serialized_end = 162
    _globals['_VALIDATIONCA']._serialized_start = 165
    _globals['_VALIDATIONCA']._serialized_end = 398
    _globals['_CERTIFICATEPROVIDERINSTANCE']._serialized_start = 400
    _globals['_CERTIFICATEPROVIDERINSTANCE']._serialized_end = 459
    _globals['_CERTIFICATEPROVIDER']._serialized_start = 462
    _globals['_CERTIFICATEPROVIDER']._serialized_end = 869
    _globals['_CERTIFICATEPROVIDER_TLSCERTIFICATEFILES']._serialized_start = 778
    _globals['_CERTIFICATEPROVIDER_TLSCERTIFICATEFILES']._serialized_end = 861