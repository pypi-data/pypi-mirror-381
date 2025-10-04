from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1 import assist_answer_pb2 as _assist_answer_pb2
from google.cloud.discoveryengine.v1 import search_service_pb2 as _search_service_pb2
from google.cloud.discoveryengine.v1 import session_pb2 as _session_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssistUserMetadata(_message.Message):
    __slots__ = ('time_zone', 'preferred_language_code')
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    time_zone: str
    preferred_language_code: str

    def __init__(self, time_zone: _Optional[str]=..., preferred_language_code: _Optional[str]=...) -> None:
        ...

class StreamAssistRequest(_message.Message):
    __slots__ = ('name', 'query', 'session', 'user_metadata', 'tools_spec', 'generation_spec')

    class ToolsSpec(_message.Message):
        __slots__ = ('vertex_ai_search_spec', 'web_grounding_spec', 'image_generation_spec', 'video_generation_spec')

        class VertexAiSearchSpec(_message.Message):
            __slots__ = ('data_store_specs', 'filter')
            DATA_STORE_SPECS_FIELD_NUMBER: _ClassVar[int]
            FILTER_FIELD_NUMBER: _ClassVar[int]
            data_store_specs: _containers.RepeatedCompositeFieldContainer[_search_service_pb2.SearchRequest.DataStoreSpec]
            filter: str

            def __init__(self, data_store_specs: _Optional[_Iterable[_Union[_search_service_pb2.SearchRequest.DataStoreSpec, _Mapping]]]=..., filter: _Optional[str]=...) -> None:
                ...

        class WebGroundingSpec(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class ImageGenerationSpec(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class VideoGenerationSpec(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...
        VERTEX_AI_SEARCH_SPEC_FIELD_NUMBER: _ClassVar[int]
        WEB_GROUNDING_SPEC_FIELD_NUMBER: _ClassVar[int]
        IMAGE_GENERATION_SPEC_FIELD_NUMBER: _ClassVar[int]
        VIDEO_GENERATION_SPEC_FIELD_NUMBER: _ClassVar[int]
        vertex_ai_search_spec: StreamAssistRequest.ToolsSpec.VertexAiSearchSpec
        web_grounding_spec: StreamAssistRequest.ToolsSpec.WebGroundingSpec
        image_generation_spec: StreamAssistRequest.ToolsSpec.ImageGenerationSpec
        video_generation_spec: StreamAssistRequest.ToolsSpec.VideoGenerationSpec

        def __init__(self, vertex_ai_search_spec: _Optional[_Union[StreamAssistRequest.ToolsSpec.VertexAiSearchSpec, _Mapping]]=..., web_grounding_spec: _Optional[_Union[StreamAssistRequest.ToolsSpec.WebGroundingSpec, _Mapping]]=..., image_generation_spec: _Optional[_Union[StreamAssistRequest.ToolsSpec.ImageGenerationSpec, _Mapping]]=..., video_generation_spec: _Optional[_Union[StreamAssistRequest.ToolsSpec.VideoGenerationSpec, _Mapping]]=...) -> None:
            ...

    class GenerationSpec(_message.Message):
        __slots__ = ('model_id',)
        MODEL_ID_FIELD_NUMBER: _ClassVar[int]
        model_id: str

        def __init__(self, model_id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    USER_METADATA_FIELD_NUMBER: _ClassVar[int]
    TOOLS_SPEC_FIELD_NUMBER: _ClassVar[int]
    GENERATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    query: _session_pb2.Query
    session: str
    user_metadata: AssistUserMetadata
    tools_spec: StreamAssistRequest.ToolsSpec
    generation_spec: StreamAssistRequest.GenerationSpec

    def __init__(self, name: _Optional[str]=..., query: _Optional[_Union[_session_pb2.Query, _Mapping]]=..., session: _Optional[str]=..., user_metadata: _Optional[_Union[AssistUserMetadata, _Mapping]]=..., tools_spec: _Optional[_Union[StreamAssistRequest.ToolsSpec, _Mapping]]=..., generation_spec: _Optional[_Union[StreamAssistRequest.GenerationSpec, _Mapping]]=...) -> None:
        ...

class StreamAssistResponse(_message.Message):
    __slots__ = ('answer', 'session_info', 'assist_token')

    class SessionInfo(_message.Message):
        __slots__ = ('session',)
        SESSION_FIELD_NUMBER: _ClassVar[int]
        session: str

        def __init__(self, session: _Optional[str]=...) -> None:
            ...
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    ASSIST_TOKEN_FIELD_NUMBER: _ClassVar[int]
    answer: _assist_answer_pb2.AssistAnswer
    session_info: StreamAssistResponse.SessionInfo
    assist_token: str

    def __init__(self, answer: _Optional[_Union[_assist_answer_pb2.AssistAnswer, _Mapping]]=..., session_info: _Optional[_Union[StreamAssistResponse.SessionInfo, _Mapping]]=..., assist_token: _Optional[str]=...) -> None:
        ...