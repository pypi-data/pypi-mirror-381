from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SigningAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNING_ALGORITHM_UNSPECIFIED: _ClassVar[SigningAlgorithm]
    RSASSA_PSS_SHA256: _ClassVar[SigningAlgorithm]
    RSASSA_PKCS1V15_SHA256: _ClassVar[SigningAlgorithm]
    ECDSA_P256_SHA256: _ClassVar[SigningAlgorithm]

class TokenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOKEN_TYPE_UNSPECIFIED: _ClassVar[TokenType]
    TOKEN_TYPE_OIDC: _ClassVar[TokenType]
    TOKEN_TYPE_PKI: _ClassVar[TokenType]
    TOKEN_TYPE_LIMITED_AWS: _ClassVar[TokenType]
    TOKEN_TYPE_AWS_PRINCIPALTAGS: _ClassVar[TokenType]

class SignatureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNATURE_TYPE_UNSPECIFIED: _ClassVar[SignatureType]
    SIGNATURE_TYPE_OIDC: _ClassVar[SignatureType]
    SIGNATURE_TYPE_PKI: _ClassVar[SignatureType]

class TokenProfile(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOKEN_PROFILE_UNSPECIFIED: _ClassVar[TokenProfile]
    TOKEN_PROFILE_DEFAULT_EAT: _ClassVar[TokenProfile]
    TOKEN_PROFILE_AWS: _ClassVar[TokenProfile]
SIGNING_ALGORITHM_UNSPECIFIED: SigningAlgorithm
RSASSA_PSS_SHA256: SigningAlgorithm
RSASSA_PKCS1V15_SHA256: SigningAlgorithm
ECDSA_P256_SHA256: SigningAlgorithm
TOKEN_TYPE_UNSPECIFIED: TokenType
TOKEN_TYPE_OIDC: TokenType
TOKEN_TYPE_PKI: TokenType
TOKEN_TYPE_LIMITED_AWS: TokenType
TOKEN_TYPE_AWS_PRINCIPALTAGS: TokenType
SIGNATURE_TYPE_UNSPECIFIED: SignatureType
SIGNATURE_TYPE_OIDC: SignatureType
SIGNATURE_TYPE_PKI: SignatureType
TOKEN_PROFILE_UNSPECIFIED: TokenProfile
TOKEN_PROFILE_DEFAULT_EAT: TokenProfile
TOKEN_PROFILE_AWS: TokenProfile

class Challenge(_message.Message):
    __slots__ = ('name', 'create_time', 'expire_time', 'used', 'tpm_nonce')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    TPM_NONCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    used: bool
    tpm_nonce: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., used: bool=..., tpm_nonce: _Optional[str]=...) -> None:
        ...

class CreateChallengeRequest(_message.Message):
    __slots__ = ('parent', 'challenge')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    challenge: Challenge

    def __init__(self, parent: _Optional[str]=..., challenge: _Optional[_Union[Challenge, _Mapping]]=...) -> None:
        ...

class VerifyAttestationRequest(_message.Message):
    __slots__ = ('td_ccel', 'sev_snp_attestation', 'challenge', 'gcp_credentials', 'tpm_attestation', 'confidential_space_info', 'token_options', 'attester')
    TD_CCEL_FIELD_NUMBER: _ClassVar[int]
    SEV_SNP_ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    GCP_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    TPM_ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENTIAL_SPACE_INFO_FIELD_NUMBER: _ClassVar[int]
    TOKEN_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ATTESTER_FIELD_NUMBER: _ClassVar[int]
    td_ccel: TdxCcelAttestation
    sev_snp_attestation: SevSnpAttestation
    challenge: str
    gcp_credentials: GcpCredentials
    tpm_attestation: TpmAttestation
    confidential_space_info: ConfidentialSpaceInfo
    token_options: TokenOptions
    attester: str

    def __init__(self, td_ccel: _Optional[_Union[TdxCcelAttestation, _Mapping]]=..., sev_snp_attestation: _Optional[_Union[SevSnpAttestation, _Mapping]]=..., challenge: _Optional[str]=..., gcp_credentials: _Optional[_Union[GcpCredentials, _Mapping]]=..., tpm_attestation: _Optional[_Union[TpmAttestation, _Mapping]]=..., confidential_space_info: _Optional[_Union[ConfidentialSpaceInfo, _Mapping]]=..., token_options: _Optional[_Union[TokenOptions, _Mapping]]=..., attester: _Optional[str]=...) -> None:
        ...

class TdxCcelAttestation(_message.Message):
    __slots__ = ('ccel_acpi_table', 'ccel_data', 'canonical_event_log', 'td_quote')
    CCEL_ACPI_TABLE_FIELD_NUMBER: _ClassVar[int]
    CCEL_DATA_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_EVENT_LOG_FIELD_NUMBER: _ClassVar[int]
    TD_QUOTE_FIELD_NUMBER: _ClassVar[int]
    ccel_acpi_table: bytes
    ccel_data: bytes
    canonical_event_log: bytes
    td_quote: bytes

    def __init__(self, ccel_acpi_table: _Optional[bytes]=..., ccel_data: _Optional[bytes]=..., canonical_event_log: _Optional[bytes]=..., td_quote: _Optional[bytes]=...) -> None:
        ...

class SevSnpAttestation(_message.Message):
    __slots__ = ('report', 'aux_blob')
    REPORT_FIELD_NUMBER: _ClassVar[int]
    AUX_BLOB_FIELD_NUMBER: _ClassVar[int]
    report: bytes
    aux_blob: bytes

    def __init__(self, report: _Optional[bytes]=..., aux_blob: _Optional[bytes]=...) -> None:
        ...

class VerifyAttestationResponse(_message.Message):
    __slots__ = ('oidc_claims_token', 'partial_errors')
    OIDC_CLAIMS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    oidc_claims_token: str
    partial_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, oidc_claims_token: _Optional[str]=..., partial_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...

class GcpCredentials(_message.Message):
    __slots__ = ('service_account_id_tokens',)
    SERVICE_ACCOUNT_ID_TOKENS_FIELD_NUMBER: _ClassVar[int]
    service_account_id_tokens: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, service_account_id_tokens: _Optional[_Iterable[str]]=...) -> None:
        ...

class TokenOptions(_message.Message):
    __slots__ = ('aws_principal_tags_options', 'audience', 'nonce', 'token_type')
    AWS_PRINCIPAL_TAGS_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    aws_principal_tags_options: AwsPrincipalTagsOptions
    audience: str
    nonce: _containers.RepeatedScalarFieldContainer[str]
    token_type: TokenType

    def __init__(self, aws_principal_tags_options: _Optional[_Union[AwsPrincipalTagsOptions, _Mapping]]=..., audience: _Optional[str]=..., nonce: _Optional[_Iterable[str]]=..., token_type: _Optional[_Union[TokenType, str]]=...) -> None:
        ...

class AwsPrincipalTagsOptions(_message.Message):
    __slots__ = ('allowed_principal_tags',)

    class AllowedPrincipalTags(_message.Message):
        __slots__ = ('container_image_signatures',)

        class ContainerImageSignatures(_message.Message):
            __slots__ = ('key_ids',)
            KEY_IDS_FIELD_NUMBER: _ClassVar[int]
            key_ids: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, key_ids: _Optional[_Iterable[str]]=...) -> None:
                ...
        CONTAINER_IMAGE_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
        container_image_signatures: AwsPrincipalTagsOptions.AllowedPrincipalTags.ContainerImageSignatures

        def __init__(self, container_image_signatures: _Optional[_Union[AwsPrincipalTagsOptions.AllowedPrincipalTags.ContainerImageSignatures, _Mapping]]=...) -> None:
            ...
    ALLOWED_PRINCIPAL_TAGS_FIELD_NUMBER: _ClassVar[int]
    allowed_principal_tags: AwsPrincipalTagsOptions.AllowedPrincipalTags

    def __init__(self, allowed_principal_tags: _Optional[_Union[AwsPrincipalTagsOptions.AllowedPrincipalTags, _Mapping]]=...) -> None:
        ...

class TpmAttestation(_message.Message):
    __slots__ = ('quotes', 'tcg_event_log', 'canonical_event_log', 'ak_cert', 'cert_chain')

    class Quote(_message.Message):
        __slots__ = ('hash_algo', 'pcr_values', 'raw_quote', 'raw_signature')

        class PcrValuesEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: bytes

            def __init__(self, key: _Optional[int]=..., value: _Optional[bytes]=...) -> None:
                ...
        HASH_ALGO_FIELD_NUMBER: _ClassVar[int]
        PCR_VALUES_FIELD_NUMBER: _ClassVar[int]
        RAW_QUOTE_FIELD_NUMBER: _ClassVar[int]
        RAW_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        hash_algo: int
        pcr_values: _containers.ScalarMap[int, bytes]
        raw_quote: bytes
        raw_signature: bytes

        def __init__(self, hash_algo: _Optional[int]=..., pcr_values: _Optional[_Mapping[int, bytes]]=..., raw_quote: _Optional[bytes]=..., raw_signature: _Optional[bytes]=...) -> None:
            ...
    QUOTES_FIELD_NUMBER: _ClassVar[int]
    TCG_EVENT_LOG_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_EVENT_LOG_FIELD_NUMBER: _ClassVar[int]
    AK_CERT_FIELD_NUMBER: _ClassVar[int]
    CERT_CHAIN_FIELD_NUMBER: _ClassVar[int]
    quotes: _containers.RepeatedCompositeFieldContainer[TpmAttestation.Quote]
    tcg_event_log: bytes
    canonical_event_log: bytes
    ak_cert: bytes
    cert_chain: _containers.RepeatedScalarFieldContainer[bytes]

    def __init__(self, quotes: _Optional[_Iterable[_Union[TpmAttestation.Quote, _Mapping]]]=..., tcg_event_log: _Optional[bytes]=..., canonical_event_log: _Optional[bytes]=..., ak_cert: _Optional[bytes]=..., cert_chain: _Optional[_Iterable[bytes]]=...) -> None:
        ...

class ConfidentialSpaceInfo(_message.Message):
    __slots__ = ('signed_entities',)
    SIGNED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    signed_entities: _containers.RepeatedCompositeFieldContainer[SignedEntity]

    def __init__(self, signed_entities: _Optional[_Iterable[_Union[SignedEntity, _Mapping]]]=...) -> None:
        ...

class SignedEntity(_message.Message):
    __slots__ = ('container_image_signatures',)
    CONTAINER_IMAGE_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    container_image_signatures: _containers.RepeatedCompositeFieldContainer[ContainerImageSignature]

    def __init__(self, container_image_signatures: _Optional[_Iterable[_Union[ContainerImageSignature, _Mapping]]]=...) -> None:
        ...

class ContainerImageSignature(_message.Message):
    __slots__ = ('payload', 'signature', 'public_key', 'sig_alg')
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SIG_ALG_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    signature: bytes
    public_key: bytes
    sig_alg: SigningAlgorithm

    def __init__(self, payload: _Optional[bytes]=..., signature: _Optional[bytes]=..., public_key: _Optional[bytes]=..., sig_alg: _Optional[_Union[SigningAlgorithm, str]]=...) -> None:
        ...

class VerifyConfidentialSpaceRequest(_message.Message):
    __slots__ = ('td_ccel', 'tpm_attestation', 'challenge', 'gcp_credentials', 'signed_entities', 'gce_shielded_identity', 'options')

    class ConfidentialSpaceOptions(_message.Message):
        __slots__ = ('aws_principal_tags_options', 'audience', 'token_profile', 'nonce', 'signature_type')
        AWS_PRINCIPAL_TAGS_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        AUDIENCE_FIELD_NUMBER: _ClassVar[int]
        TOKEN_PROFILE_FIELD_NUMBER: _ClassVar[int]
        NONCE_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_TYPE_FIELD_NUMBER: _ClassVar[int]
        aws_principal_tags_options: AwsPrincipalTagsOptions
        audience: str
        token_profile: TokenProfile
        nonce: _containers.RepeatedScalarFieldContainer[str]
        signature_type: SignatureType

        def __init__(self, aws_principal_tags_options: _Optional[_Union[AwsPrincipalTagsOptions, _Mapping]]=..., audience: _Optional[str]=..., token_profile: _Optional[_Union[TokenProfile, str]]=..., nonce: _Optional[_Iterable[str]]=..., signature_type: _Optional[_Union[SignatureType, str]]=...) -> None:
            ...
    TD_CCEL_FIELD_NUMBER: _ClassVar[int]
    TPM_ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    GCP_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    SIGNED_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    GCE_SHIELDED_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    td_ccel: TdxCcelAttestation
    tpm_attestation: TpmAttestation
    challenge: str
    gcp_credentials: GcpCredentials
    signed_entities: _containers.RepeatedCompositeFieldContainer[SignedEntity]
    gce_shielded_identity: GceShieldedIdentity
    options: VerifyConfidentialSpaceRequest.ConfidentialSpaceOptions

    def __init__(self, td_ccel: _Optional[_Union[TdxCcelAttestation, _Mapping]]=..., tpm_attestation: _Optional[_Union[TpmAttestation, _Mapping]]=..., challenge: _Optional[str]=..., gcp_credentials: _Optional[_Union[GcpCredentials, _Mapping]]=..., signed_entities: _Optional[_Iterable[_Union[SignedEntity, _Mapping]]]=..., gce_shielded_identity: _Optional[_Union[GceShieldedIdentity, _Mapping]]=..., options: _Optional[_Union[VerifyConfidentialSpaceRequest.ConfidentialSpaceOptions, _Mapping]]=...) -> None:
        ...

class GceShieldedIdentity(_message.Message):
    __slots__ = ('ak_cert', 'ak_cert_chain')
    AK_CERT_FIELD_NUMBER: _ClassVar[int]
    AK_CERT_CHAIN_FIELD_NUMBER: _ClassVar[int]
    ak_cert: bytes
    ak_cert_chain: _containers.RepeatedScalarFieldContainer[bytes]

    def __init__(self, ak_cert: _Optional[bytes]=..., ak_cert_chain: _Optional[_Iterable[bytes]]=...) -> None:
        ...

class VerifyConfidentialSpaceResponse(_message.Message):
    __slots__ = ('attestation_token', 'partial_errors')
    ATTESTATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    attestation_token: str
    partial_errors: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, attestation_token: _Optional[str]=..., partial_errors: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...

class VerifyConfidentialGkeRequest(_message.Message):
    __slots__ = ('tpm_attestation', 'challenge')
    TPM_ATTESTATION_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    tpm_attestation: TpmAttestation
    challenge: str

    def __init__(self, tpm_attestation: _Optional[_Union[TpmAttestation, _Mapping]]=..., challenge: _Optional[str]=...) -> None:
        ...

class VerifyConfidentialGkeResponse(_message.Message):
    __slots__ = ('attestation_token',)
    ATTESTATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    attestation_token: str

    def __init__(self, attestation_token: _Optional[str]=...) -> None:
        ...