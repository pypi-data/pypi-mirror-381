from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import api_auth_pb2 as _api_auth_pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1 import io_pb2 as _io_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RagEmbeddingModelConfig(_message.Message):
    __slots__ = ('vertex_prediction_endpoint',)

    class VertexPredictionEndpoint(_message.Message):
        __slots__ = ('endpoint', 'model', 'model_version_id')
        ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        MODEL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
        endpoint: str
        model: str
        model_version_id: str

        def __init__(self, endpoint: _Optional[str]=..., model: _Optional[str]=..., model_version_id: _Optional[str]=...) -> None:
            ...
    VERTEX_PREDICTION_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    vertex_prediction_endpoint: RagEmbeddingModelConfig.VertexPredictionEndpoint

    def __init__(self, vertex_prediction_endpoint: _Optional[_Union[RagEmbeddingModelConfig.VertexPredictionEndpoint, _Mapping]]=...) -> None:
        ...

class RagVectorDbConfig(_message.Message):
    __slots__ = ('rag_managed_db', 'pinecone', 'vertex_vector_search', 'api_auth', 'rag_embedding_model_config')

    class RagManagedDb(_message.Message):
        __slots__ = ('knn', 'ann')

        class KNN(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class ANN(_message.Message):
            __slots__ = ('tree_depth', 'leaf_count')
            TREE_DEPTH_FIELD_NUMBER: _ClassVar[int]
            LEAF_COUNT_FIELD_NUMBER: _ClassVar[int]
            tree_depth: int
            leaf_count: int

            def __init__(self, tree_depth: _Optional[int]=..., leaf_count: _Optional[int]=...) -> None:
                ...
        KNN_FIELD_NUMBER: _ClassVar[int]
        ANN_FIELD_NUMBER: _ClassVar[int]
        knn: RagVectorDbConfig.RagManagedDb.KNN
        ann: RagVectorDbConfig.RagManagedDb.ANN

        def __init__(self, knn: _Optional[_Union[RagVectorDbConfig.RagManagedDb.KNN, _Mapping]]=..., ann: _Optional[_Union[RagVectorDbConfig.RagManagedDb.ANN, _Mapping]]=...) -> None:
            ...

    class Pinecone(_message.Message):
        __slots__ = ('index_name',)
        INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
        index_name: str

        def __init__(self, index_name: _Optional[str]=...) -> None:
            ...

    class VertexVectorSearch(_message.Message):
        __slots__ = ('index_endpoint', 'index')
        INDEX_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        index_endpoint: str
        index: str

        def __init__(self, index_endpoint: _Optional[str]=..., index: _Optional[str]=...) -> None:
            ...
    RAG_MANAGED_DB_FIELD_NUMBER: _ClassVar[int]
    PINECONE_FIELD_NUMBER: _ClassVar[int]
    VERTEX_VECTOR_SEARCH_FIELD_NUMBER: _ClassVar[int]
    API_AUTH_FIELD_NUMBER: _ClassVar[int]
    RAG_EMBEDDING_MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    rag_managed_db: RagVectorDbConfig.RagManagedDb
    pinecone: RagVectorDbConfig.Pinecone
    vertex_vector_search: RagVectorDbConfig.VertexVectorSearch
    api_auth: _api_auth_pb2.ApiAuth
    rag_embedding_model_config: RagEmbeddingModelConfig

    def __init__(self, rag_managed_db: _Optional[_Union[RagVectorDbConfig.RagManagedDb, _Mapping]]=..., pinecone: _Optional[_Union[RagVectorDbConfig.Pinecone, _Mapping]]=..., vertex_vector_search: _Optional[_Union[RagVectorDbConfig.VertexVectorSearch, _Mapping]]=..., api_auth: _Optional[_Union[_api_auth_pb2.ApiAuth, _Mapping]]=..., rag_embedding_model_config: _Optional[_Union[RagEmbeddingModelConfig, _Mapping]]=...) -> None:
        ...

class FileStatus(_message.Message):
    __slots__ = ('state', 'error_status')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[FileStatus.State]
        ACTIVE: _ClassVar[FileStatus.State]
        ERROR: _ClassVar[FileStatus.State]
    STATE_UNSPECIFIED: FileStatus.State
    ACTIVE: FileStatus.State
    ERROR: FileStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_STATUS_FIELD_NUMBER: _ClassVar[int]
    state: FileStatus.State
    error_status: str

    def __init__(self, state: _Optional[_Union[FileStatus.State, str]]=..., error_status: _Optional[str]=...) -> None:
        ...

class VertexAiSearchConfig(_message.Message):
    __slots__ = ('serving_config',)
    SERVING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    serving_config: str

    def __init__(self, serving_config: _Optional[str]=...) -> None:
        ...

class CorpusStatus(_message.Message):
    __slots__ = ('state', 'error_status')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[CorpusStatus.State]
        INITIALIZED: _ClassVar[CorpusStatus.State]
        ACTIVE: _ClassVar[CorpusStatus.State]
        ERROR: _ClassVar[CorpusStatus.State]
    UNKNOWN: CorpusStatus.State
    INITIALIZED: CorpusStatus.State
    ACTIVE: CorpusStatus.State
    ERROR: CorpusStatus.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_STATUS_FIELD_NUMBER: _ClassVar[int]
    state: CorpusStatus.State
    error_status: str

    def __init__(self, state: _Optional[_Union[CorpusStatus.State, str]]=..., error_status: _Optional[str]=...) -> None:
        ...

class RagCorpus(_message.Message):
    __slots__ = ('vector_db_config', 'vertex_ai_search_config', 'name', 'display_name', 'description', 'create_time', 'update_time', 'corpus_status', 'encryption_spec')
    VECTOR_DB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VERTEX_AI_SEARCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CORPUS_STATUS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    vector_db_config: RagVectorDbConfig
    vertex_ai_search_config: VertexAiSearchConfig
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    corpus_status: CorpusStatus
    encryption_spec: _encryption_spec_pb2.EncryptionSpec

    def __init__(self, vector_db_config: _Optional[_Union[RagVectorDbConfig, _Mapping]]=..., vertex_ai_search_config: _Optional[_Union[VertexAiSearchConfig, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., corpus_status: _Optional[_Union[CorpusStatus, _Mapping]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=...) -> None:
        ...

class RagFile(_message.Message):
    __slots__ = ('gcs_source', 'google_drive_source', 'direct_upload_source', 'slack_source', 'jira_source', 'share_point_sources', 'name', 'display_name', 'description', 'create_time', 'update_time', 'file_status')
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_DRIVE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DIRECT_UPLOAD_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SLACK_SOURCE_FIELD_NUMBER: _ClassVar[int]
    JIRA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SHARE_POINT_SOURCES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FILE_STATUS_FIELD_NUMBER: _ClassVar[int]
    gcs_source: _io_pb2.GcsSource
    google_drive_source: _io_pb2.GoogleDriveSource
    direct_upload_source: _io_pb2.DirectUploadSource
    slack_source: _io_pb2.SlackSource
    jira_source: _io_pb2.JiraSource
    share_point_sources: _io_pb2.SharePointSources
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    file_status: FileStatus

    def __init__(self, gcs_source: _Optional[_Union[_io_pb2.GcsSource, _Mapping]]=..., google_drive_source: _Optional[_Union[_io_pb2.GoogleDriveSource, _Mapping]]=..., direct_upload_source: _Optional[_Union[_io_pb2.DirectUploadSource, _Mapping]]=..., slack_source: _Optional[_Union[_io_pb2.SlackSource, _Mapping]]=..., jira_source: _Optional[_Union[_io_pb2.JiraSource, _Mapping]]=..., share_point_sources: _Optional[_Union[_io_pb2.SharePointSources, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., file_status: _Optional[_Union[FileStatus, _Mapping]]=...) -> None:
        ...

class RagChunk(_message.Message):
    __slots__ = ('text', 'page_span')

    class PageSpan(_message.Message):
        __slots__ = ('first_page', 'last_page')
        FIRST_PAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_PAGE_FIELD_NUMBER: _ClassVar[int]
        first_page: int
        last_page: int

        def __init__(self, first_page: _Optional[int]=..., last_page: _Optional[int]=...) -> None:
            ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SPAN_FIELD_NUMBER: _ClassVar[int]
    text: str
    page_span: RagChunk.PageSpan

    def __init__(self, text: _Optional[str]=..., page_span: _Optional[_Union[RagChunk.PageSpan, _Mapping]]=...) -> None:
        ...

class RagFileChunkingConfig(_message.Message):
    __slots__ = ('fixed_length_chunking',)

    class FixedLengthChunking(_message.Message):
        __slots__ = ('chunk_size', 'chunk_overlap')
        CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
        CHUNK_OVERLAP_FIELD_NUMBER: _ClassVar[int]
        chunk_size: int
        chunk_overlap: int

        def __init__(self, chunk_size: _Optional[int]=..., chunk_overlap: _Optional[int]=...) -> None:
            ...
    FIXED_LENGTH_CHUNKING_FIELD_NUMBER: _ClassVar[int]
    fixed_length_chunking: RagFileChunkingConfig.FixedLengthChunking

    def __init__(self, fixed_length_chunking: _Optional[_Union[RagFileChunkingConfig.FixedLengthChunking, _Mapping]]=...) -> None:
        ...

class RagFileTransformationConfig(_message.Message):
    __slots__ = ('rag_file_chunking_config',)
    RAG_FILE_CHUNKING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    rag_file_chunking_config: RagFileChunkingConfig

    def __init__(self, rag_file_chunking_config: _Optional[_Union[RagFileChunkingConfig, _Mapping]]=...) -> None:
        ...

class RagFileParsingConfig(_message.Message):
    __slots__ = ('layout_parser', 'llm_parser')

    class LayoutParser(_message.Message):
        __slots__ = ('processor_name', 'max_parsing_requests_per_min')
        PROCESSOR_NAME_FIELD_NUMBER: _ClassVar[int]
        MAX_PARSING_REQUESTS_PER_MIN_FIELD_NUMBER: _ClassVar[int]
        processor_name: str
        max_parsing_requests_per_min: int

        def __init__(self, processor_name: _Optional[str]=..., max_parsing_requests_per_min: _Optional[int]=...) -> None:
            ...

    class LlmParser(_message.Message):
        __slots__ = ('model_name', 'max_parsing_requests_per_min', 'custom_parsing_prompt')
        MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
        MAX_PARSING_REQUESTS_PER_MIN_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_PARSING_PROMPT_FIELD_NUMBER: _ClassVar[int]
        model_name: str
        max_parsing_requests_per_min: int
        custom_parsing_prompt: str

        def __init__(self, model_name: _Optional[str]=..., max_parsing_requests_per_min: _Optional[int]=..., custom_parsing_prompt: _Optional[str]=...) -> None:
            ...
    LAYOUT_PARSER_FIELD_NUMBER: _ClassVar[int]
    LLM_PARSER_FIELD_NUMBER: _ClassVar[int]
    layout_parser: RagFileParsingConfig.LayoutParser
    llm_parser: RagFileParsingConfig.LlmParser

    def __init__(self, layout_parser: _Optional[_Union[RagFileParsingConfig.LayoutParser, _Mapping]]=..., llm_parser: _Optional[_Union[RagFileParsingConfig.LlmParser, _Mapping]]=...) -> None:
        ...

class UploadRagFileConfig(_message.Message):
    __slots__ = ('rag_file_transformation_config',)
    RAG_FILE_TRANSFORMATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    rag_file_transformation_config: RagFileTransformationConfig

    def __init__(self, rag_file_transformation_config: _Optional[_Union[RagFileTransformationConfig, _Mapping]]=...) -> None:
        ...

class ImportRagFilesConfig(_message.Message):
    __slots__ = ('gcs_source', 'google_drive_source', 'slack_source', 'jira_source', 'share_point_sources', 'partial_failure_gcs_sink', 'partial_failure_bigquery_sink', 'import_result_gcs_sink', 'import_result_bigquery_sink', 'rag_file_transformation_config', 'rag_file_parsing_config', 'max_embedding_requests_per_min', 'rebuild_ann_index')
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_DRIVE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SLACK_SOURCE_FIELD_NUMBER: _ClassVar[int]
    JIRA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SHARE_POINT_SOURCES_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_GCS_SINK_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_BIGQUERY_SINK_FIELD_NUMBER: _ClassVar[int]
    IMPORT_RESULT_GCS_SINK_FIELD_NUMBER: _ClassVar[int]
    IMPORT_RESULT_BIGQUERY_SINK_FIELD_NUMBER: _ClassVar[int]
    RAG_FILE_TRANSFORMATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RAG_FILE_PARSING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAX_EMBEDDING_REQUESTS_PER_MIN_FIELD_NUMBER: _ClassVar[int]
    REBUILD_ANN_INDEX_FIELD_NUMBER: _ClassVar[int]
    gcs_source: _io_pb2.GcsSource
    google_drive_source: _io_pb2.GoogleDriveSource
    slack_source: _io_pb2.SlackSource
    jira_source: _io_pb2.JiraSource
    share_point_sources: _io_pb2.SharePointSources
    partial_failure_gcs_sink: _io_pb2.GcsDestination
    partial_failure_bigquery_sink: _io_pb2.BigQueryDestination
    import_result_gcs_sink: _io_pb2.GcsDestination
    import_result_bigquery_sink: _io_pb2.BigQueryDestination
    rag_file_transformation_config: RagFileTransformationConfig
    rag_file_parsing_config: RagFileParsingConfig
    max_embedding_requests_per_min: int
    rebuild_ann_index: bool

    def __init__(self, gcs_source: _Optional[_Union[_io_pb2.GcsSource, _Mapping]]=..., google_drive_source: _Optional[_Union[_io_pb2.GoogleDriveSource, _Mapping]]=..., slack_source: _Optional[_Union[_io_pb2.SlackSource, _Mapping]]=..., jira_source: _Optional[_Union[_io_pb2.JiraSource, _Mapping]]=..., share_point_sources: _Optional[_Union[_io_pb2.SharePointSources, _Mapping]]=..., partial_failure_gcs_sink: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]]=..., partial_failure_bigquery_sink: _Optional[_Union[_io_pb2.BigQueryDestination, _Mapping]]=..., import_result_gcs_sink: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]]=..., import_result_bigquery_sink: _Optional[_Union[_io_pb2.BigQueryDestination, _Mapping]]=..., rag_file_transformation_config: _Optional[_Union[RagFileTransformationConfig, _Mapping]]=..., rag_file_parsing_config: _Optional[_Union[RagFileParsingConfig, _Mapping]]=..., max_embedding_requests_per_min: _Optional[int]=..., rebuild_ann_index: bool=...) -> None:
        ...

class RagManagedDbConfig(_message.Message):
    __slots__ = ('scaled', 'basic', 'unprovisioned')

    class Scaled(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Basic(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class Unprovisioned(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    SCALED_FIELD_NUMBER: _ClassVar[int]
    BASIC_FIELD_NUMBER: _ClassVar[int]
    UNPROVISIONED_FIELD_NUMBER: _ClassVar[int]
    scaled: RagManagedDbConfig.Scaled
    basic: RagManagedDbConfig.Basic
    unprovisioned: RagManagedDbConfig.Unprovisioned

    def __init__(self, scaled: _Optional[_Union[RagManagedDbConfig.Scaled, _Mapping]]=..., basic: _Optional[_Union[RagManagedDbConfig.Basic, _Mapping]]=..., unprovisioned: _Optional[_Union[RagManagedDbConfig.Unprovisioned, _Mapping]]=...) -> None:
        ...

class RagEngineConfig(_message.Message):
    __slots__ = ('name', 'rag_managed_db_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RAG_MANAGED_DB_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    rag_managed_db_config: RagManagedDbConfig

    def __init__(self, name: _Optional[str]=..., rag_managed_db_config: _Optional[_Union[RagManagedDbConfig, _Mapping]]=...) -> None:
        ...