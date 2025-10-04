from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.geminidataanalytics.v1beta import context_pb2 as _context_pb2
from google.cloud.geminidataanalytics.v1beta import conversation_pb2 as _conversation_pb2
from google.cloud.geminidataanalytics.v1beta import credentials_pb2 as _credentials_pb2
from google.cloud.geminidataanalytics.v1beta import datasource_pb2 as _datasource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListMessagesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListMessagesResponse(_message.Message):
    __slots__ = ('messages', 'next_page_token')
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[StorageMessage]
    next_page_token: str

    def __init__(self, messages: _Optional[_Iterable[_Union[StorageMessage, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class StorageMessage(_message.Message):
    __slots__ = ('message_id', 'message')
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    message: Message

    def __init__(self, message_id: _Optional[str]=..., message: _Optional[_Union[Message, _Mapping]]=...) -> None:
        ...

class ChatRequest(_message.Message):
    __slots__ = ('inline_context', 'conversation_reference', 'data_agent_context', 'project', 'parent', 'messages')
    INLINE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DATA_AGENT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    inline_context: _context_pb2.Context
    conversation_reference: ConversationReference
    data_agent_context: DataAgentContext
    project: str
    parent: str
    messages: _containers.RepeatedCompositeFieldContainer[Message]

    def __init__(self, inline_context: _Optional[_Union[_context_pb2.Context, _Mapping]]=..., conversation_reference: _Optional[_Union[ConversationReference, _Mapping]]=..., data_agent_context: _Optional[_Union[DataAgentContext, _Mapping]]=..., project: _Optional[str]=..., parent: _Optional[str]=..., messages: _Optional[_Iterable[_Union[Message, _Mapping]]]=...) -> None:
        ...

class DataAgentContext(_message.Message):
    __slots__ = ('data_agent', 'credentials', 'context_version')

    class ContextVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTEXT_VERSION_UNSPECIFIED: _ClassVar[DataAgentContext.ContextVersion]
        STAGING: _ClassVar[DataAgentContext.ContextVersion]
        PUBLISHED: _ClassVar[DataAgentContext.ContextVersion]
    CONTEXT_VERSION_UNSPECIFIED: DataAgentContext.ContextVersion
    STAGING: DataAgentContext.ContextVersion
    PUBLISHED: DataAgentContext.ContextVersion
    DATA_AGENT_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_VERSION_FIELD_NUMBER: _ClassVar[int]
    data_agent: str
    credentials: _credentials_pb2.Credentials
    context_version: DataAgentContext.ContextVersion

    def __init__(self, data_agent: _Optional[str]=..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]]=..., context_version: _Optional[_Union[DataAgentContext.ContextVersion, str]]=...) -> None:
        ...

class ConversationReference(_message.Message):
    __slots__ = ('conversation', 'data_agent_context')
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    DATA_AGENT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    conversation: str
    data_agent_context: DataAgentContext

    def __init__(self, conversation: _Optional[str]=..., data_agent_context: _Optional[_Union[DataAgentContext, _Mapping]]=...) -> None:
        ...

class Message(_message.Message):
    __slots__ = ('user_message', 'system_message', 'timestamp', 'message_id')
    USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    user_message: UserMessage
    system_message: SystemMessage
    timestamp: _timestamp_pb2.Timestamp
    message_id: str

    def __init__(self, user_message: _Optional[_Union[UserMessage, _Mapping]]=..., system_message: _Optional[_Union[SystemMessage, _Mapping]]=..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., message_id: _Optional[str]=...) -> None:
        ...

class UserMessage(_message.Message):
    __slots__ = ('text',)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str

    def __init__(self, text: _Optional[str]=...) -> None:
        ...

class SystemMessage(_message.Message):
    __slots__ = ('text', 'schema', 'data', 'analysis', 'chart', 'error', 'group_id')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    CHART_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    text: TextMessage
    schema: SchemaMessage
    data: DataMessage
    analysis: AnalysisMessage
    chart: ChartMessage
    error: ErrorMessage
    group_id: int

    def __init__(self, text: _Optional[_Union[TextMessage, _Mapping]]=..., schema: _Optional[_Union[SchemaMessage, _Mapping]]=..., data: _Optional[_Union[DataMessage, _Mapping]]=..., analysis: _Optional[_Union[AnalysisMessage, _Mapping]]=..., chart: _Optional[_Union[ChartMessage, _Mapping]]=..., error: _Optional[_Union[ErrorMessage, _Mapping]]=..., group_id: _Optional[int]=...) -> None:
        ...

class TextMessage(_message.Message):
    __slots__ = ('parts',)
    PARTS_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, parts: _Optional[_Iterable[str]]=...) -> None:
        ...

class SchemaMessage(_message.Message):
    __slots__ = ('query', 'result')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    query: SchemaQuery
    result: SchemaResult

    def __init__(self, query: _Optional[_Union[SchemaQuery, _Mapping]]=..., result: _Optional[_Union[SchemaResult, _Mapping]]=...) -> None:
        ...

class SchemaQuery(_message.Message):
    __slots__ = ('question',)
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    question: str

    def __init__(self, question: _Optional[str]=...) -> None:
        ...

class SchemaResult(_message.Message):
    __slots__ = ('datasources',)
    DATASOURCES_FIELD_NUMBER: _ClassVar[int]
    datasources: _containers.RepeatedCompositeFieldContainer[_datasource_pb2.Datasource]

    def __init__(self, datasources: _Optional[_Iterable[_Union[_datasource_pb2.Datasource, _Mapping]]]=...) -> None:
        ...

class DataMessage(_message.Message):
    __slots__ = ('query', 'generated_sql', 'result', 'generated_looker_query', 'big_query_job')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    GENERATED_SQL_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    GENERATED_LOOKER_QUERY_FIELD_NUMBER: _ClassVar[int]
    BIG_QUERY_JOB_FIELD_NUMBER: _ClassVar[int]
    query: DataQuery
    generated_sql: str
    result: DataResult
    generated_looker_query: LookerQuery
    big_query_job: BigQueryJob

    def __init__(self, query: _Optional[_Union[DataQuery, _Mapping]]=..., generated_sql: _Optional[str]=..., result: _Optional[_Union[DataResult, _Mapping]]=..., generated_looker_query: _Optional[_Union[LookerQuery, _Mapping]]=..., big_query_job: _Optional[_Union[BigQueryJob, _Mapping]]=...) -> None:
        ...

class LookerQuery(_message.Message):
    __slots__ = ('model', 'explore', 'fields', 'filters', 'sorts', 'limit')

    class Filter(_message.Message):
        __slots__ = ('field', 'value')
        FIELD_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        field: str
        value: str

        def __init__(self, field: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MODEL_FIELD_NUMBER: _ClassVar[int]
    EXPLORE_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORTS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    model: str
    explore: str
    fields: _containers.RepeatedScalarFieldContainer[str]
    filters: _containers.RepeatedCompositeFieldContainer[LookerQuery.Filter]
    sorts: _containers.RepeatedScalarFieldContainer[str]
    limit: str

    def __init__(self, model: _Optional[str]=..., explore: _Optional[str]=..., fields: _Optional[_Iterable[str]]=..., filters: _Optional[_Iterable[_Union[LookerQuery.Filter, _Mapping]]]=..., sorts: _Optional[_Iterable[str]]=..., limit: _Optional[str]=...) -> None:
        ...

class DataQuery(_message.Message):
    __slots__ = ('question', 'name', 'datasources')
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATASOURCES_FIELD_NUMBER: _ClassVar[int]
    question: str
    name: str
    datasources: _containers.RepeatedCompositeFieldContainer[_datasource_pb2.Datasource]

    def __init__(self, question: _Optional[str]=..., name: _Optional[str]=..., datasources: _Optional[_Iterable[_Union[_datasource_pb2.Datasource, _Mapping]]]=...) -> None:
        ...

class DataResult(_message.Message):
    __slots__ = ('name', 'schema', 'data')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    schema: _datasource_pb2.Schema
    data: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]

    def __init__(self, name: _Optional[str]=..., schema: _Optional[_Union[_datasource_pb2.Schema, _Mapping]]=..., data: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]]=...) -> None:
        ...

class BigQueryJob(_message.Message):
    __slots__ = ('project_id', 'job_id', 'location', 'destination_table', 'schema')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TABLE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    location: str
    destination_table: _datasource_pb2.BigQueryTableReference
    schema: _datasource_pb2.Schema

    def __init__(self, project_id: _Optional[str]=..., job_id: _Optional[str]=..., location: _Optional[str]=..., destination_table: _Optional[_Union[_datasource_pb2.BigQueryTableReference, _Mapping]]=..., schema: _Optional[_Union[_datasource_pb2.Schema, _Mapping]]=...) -> None:
        ...

class AnalysisMessage(_message.Message):
    __slots__ = ('query', 'progress_event')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_EVENT_FIELD_NUMBER: _ClassVar[int]
    query: AnalysisQuery
    progress_event: AnalysisEvent

    def __init__(self, query: _Optional[_Union[AnalysisQuery, _Mapping]]=..., progress_event: _Optional[_Union[AnalysisEvent, _Mapping]]=...) -> None:
        ...

class AnalysisQuery(_message.Message):
    __slots__ = ('question', 'data_result_names')
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    DATA_RESULT_NAMES_FIELD_NUMBER: _ClassVar[int]
    question: str
    data_result_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, question: _Optional[str]=..., data_result_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class AnalysisEvent(_message.Message):
    __slots__ = ('planner_reasoning', 'coder_instruction', 'code', 'execution_output', 'execution_error', 'result_vega_chart_json', 'result_natural_language', 'result_csv_data', 'result_reference_data', 'error')
    PLANNER_REASONING_FIELD_NUMBER: _ClassVar[int]
    CODER_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULT_VEGA_CHART_JSON_FIELD_NUMBER: _ClassVar[int]
    RESULT_NATURAL_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_CSV_DATA_FIELD_NUMBER: _ClassVar[int]
    RESULT_REFERENCE_DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    planner_reasoning: str
    coder_instruction: str
    code: str
    execution_output: str
    execution_error: str
    result_vega_chart_json: str
    result_natural_language: str
    result_csv_data: str
    result_reference_data: str
    error: str

    def __init__(self, planner_reasoning: _Optional[str]=..., coder_instruction: _Optional[str]=..., code: _Optional[str]=..., execution_output: _Optional[str]=..., execution_error: _Optional[str]=..., result_vega_chart_json: _Optional[str]=..., result_natural_language: _Optional[str]=..., result_csv_data: _Optional[str]=..., result_reference_data: _Optional[str]=..., error: _Optional[str]=...) -> None:
        ...

class ChartMessage(_message.Message):
    __slots__ = ('query', 'result')
    QUERY_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    query: ChartQuery
    result: ChartResult

    def __init__(self, query: _Optional[_Union[ChartQuery, _Mapping]]=..., result: _Optional[_Union[ChartResult, _Mapping]]=...) -> None:
        ...

class ChartQuery(_message.Message):
    __slots__ = ('instructions', 'data_result_name')
    INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_RESULT_NAME_FIELD_NUMBER: _ClassVar[int]
    instructions: str
    data_result_name: str

    def __init__(self, instructions: _Optional[str]=..., data_result_name: _Optional[str]=...) -> None:
        ...

class ChartResult(_message.Message):
    __slots__ = ('vega_config', 'image')
    VEGA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    vega_config: _struct_pb2.Struct
    image: Blob

    def __init__(self, vega_config: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., image: _Optional[_Union[Blob, _Mapping]]=...) -> None:
        ...

class ErrorMessage(_message.Message):
    __slots__ = ('text',)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str

    def __init__(self, text: _Optional[str]=...) -> None:
        ...

class Blob(_message.Message):
    __slots__ = ('mime_type', 'data')
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    data: bytes

    def __init__(self, mime_type: _Optional[str]=..., data: _Optional[bytes]=...) -> None:
        ...