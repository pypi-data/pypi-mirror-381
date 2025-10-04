from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PubSubSubscription(_message.Message):
    __slots__ = ('name', 'push_config', 'bigquery_config', 'cloud_storage_config', 'ack_deadline_seconds', 'retain_acked_messages', 'message_retention_duration', 'labels', 'enable_message_ordering', 'expiration_policy', 'filter', 'dead_letter_policy', 'retry_policy', 'detached', 'enable_exactly_once_delivery', 'message_transforms')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUSH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLOUD_STORAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACK_DEADLINE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    RETAIN_ACKED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_RETENTION_DURATION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MESSAGE_ORDERING_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_POLICY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DEAD_LETTER_POLICY_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    DETACHED_FIELD_NUMBER: _ClassVar[int]
    ENABLE_EXACTLY_ONCE_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TRANSFORMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    push_config: PushConfig
    bigquery_config: BigQueryConfig
    cloud_storage_config: CloudStorageConfig
    ack_deadline_seconds: int
    retain_acked_messages: bool
    message_retention_duration: _duration_pb2.Duration
    labels: _containers.ScalarMap[str, str]
    enable_message_ordering: bool
    expiration_policy: ExpirationPolicy
    filter: str
    dead_letter_policy: DeadLetterPolicy
    retry_policy: RetryPolicy
    detached: bool
    enable_exactly_once_delivery: bool
    message_transforms: _containers.RepeatedCompositeFieldContainer[MessageTransform]

    def __init__(self, name: _Optional[str]=..., push_config: _Optional[_Union[PushConfig, _Mapping]]=..., bigquery_config: _Optional[_Union[BigQueryConfig, _Mapping]]=..., cloud_storage_config: _Optional[_Union[CloudStorageConfig, _Mapping]]=..., ack_deadline_seconds: _Optional[int]=..., retain_acked_messages: bool=..., message_retention_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., enable_message_ordering: bool=..., expiration_policy: _Optional[_Union[ExpirationPolicy, _Mapping]]=..., filter: _Optional[str]=..., dead_letter_policy: _Optional[_Union[DeadLetterPolicy, _Mapping]]=..., retry_policy: _Optional[_Union[RetryPolicy, _Mapping]]=..., detached: bool=..., enable_exactly_once_delivery: bool=..., message_transforms: _Optional[_Iterable[_Union[MessageTransform, _Mapping]]]=...) -> None:
        ...

class RetryPolicy(_message.Message):
    __slots__ = ('minimum_backoff', 'maximum_backoff')
    MINIMUM_BACKOFF_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_BACKOFF_FIELD_NUMBER: _ClassVar[int]
    minimum_backoff: _duration_pb2.Duration
    maximum_backoff: _duration_pb2.Duration

    def __init__(self, minimum_backoff: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., maximum_backoff: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class DeadLetterPolicy(_message.Message):
    __slots__ = ('dead_letter_topic', 'max_delivery_attempts')
    DEAD_LETTER_TOPIC_FIELD_NUMBER: _ClassVar[int]
    MAX_DELIVERY_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    dead_letter_topic: str
    max_delivery_attempts: int

    def __init__(self, dead_letter_topic: _Optional[str]=..., max_delivery_attempts: _Optional[int]=...) -> None:
        ...

class ExpirationPolicy(_message.Message):
    __slots__ = ('ttl',)
    TTL_FIELD_NUMBER: _ClassVar[int]
    ttl: _duration_pb2.Duration

    def __init__(self, ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class PushConfig(_message.Message):
    __slots__ = ('oidc_token', 'pubsub_wrapper', 'no_wrapper', 'push_endpoint', 'attributes')

    class OidcToken(_message.Message):
        __slots__ = ('service_account_email', 'audience')
        SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
        AUDIENCE_FIELD_NUMBER: _ClassVar[int]
        service_account_email: str
        audience: str

        def __init__(self, service_account_email: _Optional[str]=..., audience: _Optional[str]=...) -> None:
            ...

    class PubsubWrapper(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class NoWrapper(_message.Message):
        __slots__ = ('write_metadata',)
        WRITE_METADATA_FIELD_NUMBER: _ClassVar[int]
        write_metadata: bool

        def __init__(self, write_metadata: bool=...) -> None:
            ...

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    OIDC_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    NO_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    PUSH_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    oidc_token: PushConfig.OidcToken
    pubsub_wrapper: PushConfig.PubsubWrapper
    no_wrapper: PushConfig.NoWrapper
    push_endpoint: str
    attributes: _containers.ScalarMap[str, str]

    def __init__(self, oidc_token: _Optional[_Union[PushConfig.OidcToken, _Mapping]]=..., pubsub_wrapper: _Optional[_Union[PushConfig.PubsubWrapper, _Mapping]]=..., no_wrapper: _Optional[_Union[PushConfig.NoWrapper, _Mapping]]=..., push_endpoint: _Optional[str]=..., attributes: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class BigQueryConfig(_message.Message):
    __slots__ = ('table', 'use_topic_schema', 'write_metadata', 'drop_unknown_fields', 'use_table_schema', 'service_account_email')
    TABLE_FIELD_NUMBER: _ClassVar[int]
    USE_TOPIC_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    WRITE_METADATA_FIELD_NUMBER: _ClassVar[int]
    DROP_UNKNOWN_FIELDS_FIELD_NUMBER: _ClassVar[int]
    USE_TABLE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    table: str
    use_topic_schema: bool
    write_metadata: bool
    drop_unknown_fields: bool
    use_table_schema: bool
    service_account_email: str

    def __init__(self, table: _Optional[str]=..., use_topic_schema: bool=..., write_metadata: bool=..., drop_unknown_fields: bool=..., use_table_schema: bool=..., service_account_email: _Optional[str]=...) -> None:
        ...

class CloudStorageConfig(_message.Message):
    __slots__ = ('text_config', 'avro_config', 'bucket', 'filename_prefix', 'filename_suffix', 'filename_datetime_format', 'max_duration', 'max_bytes', 'max_messages', 'service_account_email')

    class TextConfig(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class AvroConfig(_message.Message):
        __slots__ = ('write_metadata', 'use_topic_schema')
        WRITE_METADATA_FIELD_NUMBER: _ClassVar[int]
        USE_TOPIC_SCHEMA_FIELD_NUMBER: _ClassVar[int]
        write_metadata: bool
        use_topic_schema: bool

        def __init__(self, write_metadata: bool=..., use_topic_schema: bool=...) -> None:
            ...
    TEXT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AVRO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    FILENAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    FILENAME_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    FILENAME_DATETIME_FORMAT_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    text_config: CloudStorageConfig.TextConfig
    avro_config: CloudStorageConfig.AvroConfig
    bucket: str
    filename_prefix: str
    filename_suffix: str
    filename_datetime_format: str
    max_duration: _duration_pb2.Duration
    max_bytes: int
    max_messages: int
    service_account_email: str

    def __init__(self, text_config: _Optional[_Union[CloudStorageConfig.TextConfig, _Mapping]]=..., avro_config: _Optional[_Union[CloudStorageConfig.AvroConfig, _Mapping]]=..., bucket: _Optional[str]=..., filename_prefix: _Optional[str]=..., filename_suffix: _Optional[str]=..., filename_datetime_format: _Optional[str]=..., max_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., max_bytes: _Optional[int]=..., max_messages: _Optional[int]=..., service_account_email: _Optional[str]=...) -> None:
        ...

class MessageTransform(_message.Message):
    __slots__ = ('javascript_udf', 'enabled', 'disabled')
    JAVASCRIPT_UDF_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    javascript_udf: JavaScriptUDF
    enabled: bool
    disabled: bool

    def __init__(self, javascript_udf: _Optional[_Union[JavaScriptUDF, _Mapping]]=..., enabled: bool=..., disabled: bool=...) -> None:
        ...

class JavaScriptUDF(_message.Message):
    __slots__ = ('function_name', 'code')
    FUNCTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    function_name: str
    code: str

    def __init__(self, function_name: _Optional[str]=..., code: _Optional[str]=...) -> None:
        ...