from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssistAnswer(_message.Message):
    __slots__ = ('name', 'state', 'replies', 'assist_skipped_reasons')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[AssistAnswer.State]
        IN_PROGRESS: _ClassVar[AssistAnswer.State]
        FAILED: _ClassVar[AssistAnswer.State]
        SUCCEEDED: _ClassVar[AssistAnswer.State]
        SKIPPED: _ClassVar[AssistAnswer.State]
    STATE_UNSPECIFIED: AssistAnswer.State
    IN_PROGRESS: AssistAnswer.State
    FAILED: AssistAnswer.State
    SUCCEEDED: AssistAnswer.State
    SKIPPED: AssistAnswer.State

    class AssistSkippedReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ASSIST_SKIPPED_REASON_UNSPECIFIED: _ClassVar[AssistAnswer.AssistSkippedReason]
        NON_ASSIST_SEEKING_QUERY_IGNORED: _ClassVar[AssistAnswer.AssistSkippedReason]
        CUSTOMER_POLICY_VIOLATION: _ClassVar[AssistAnswer.AssistSkippedReason]
    ASSIST_SKIPPED_REASON_UNSPECIFIED: AssistAnswer.AssistSkippedReason
    NON_ASSIST_SEEKING_QUERY_IGNORED: AssistAnswer.AssistSkippedReason
    CUSTOMER_POLICY_VIOLATION: AssistAnswer.AssistSkippedReason

    class Reply(_message.Message):
        __slots__ = ('grounded_content',)
        GROUNDED_CONTENT_FIELD_NUMBER: _ClassVar[int]
        grounded_content: AssistantGroundedContent

        def __init__(self, grounded_content: _Optional[_Union[AssistantGroundedContent, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REPLIES_FIELD_NUMBER: _ClassVar[int]
    ASSIST_SKIPPED_REASONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: AssistAnswer.State
    replies: _containers.RepeatedCompositeFieldContainer[AssistAnswer.Reply]
    assist_skipped_reasons: _containers.RepeatedScalarFieldContainer[AssistAnswer.AssistSkippedReason]

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[AssistAnswer.State, str]]=..., replies: _Optional[_Iterable[_Union[AssistAnswer.Reply, _Mapping]]]=..., assist_skipped_reasons: _Optional[_Iterable[_Union[AssistAnswer.AssistSkippedReason, str]]]=...) -> None:
        ...

class AssistantContent(_message.Message):
    __slots__ = ('text', 'inline_data', 'file', 'executable_code', 'code_execution_result', 'role', 'thought')

    class Blob(_message.Message):
        __slots__ = ('mime_type', 'data')
        MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        mime_type: str
        data: bytes

        def __init__(self, mime_type: _Optional[str]=..., data: _Optional[bytes]=...) -> None:
            ...

    class File(_message.Message):
        __slots__ = ('mime_type', 'file_id')
        MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
        FILE_ID_FIELD_NUMBER: _ClassVar[int]
        mime_type: str
        file_id: str

        def __init__(self, mime_type: _Optional[str]=..., file_id: _Optional[str]=...) -> None:
            ...

    class ExecutableCode(_message.Message):
        __slots__ = ('code',)
        CODE_FIELD_NUMBER: _ClassVar[int]
        code: str

        def __init__(self, code: _Optional[str]=...) -> None:
            ...

    class CodeExecutionResult(_message.Message):
        __slots__ = ('outcome', 'output')

        class Outcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            OUTCOME_UNSPECIFIED: _ClassVar[AssistantContent.CodeExecutionResult.Outcome]
            OUTCOME_OK: _ClassVar[AssistantContent.CodeExecutionResult.Outcome]
            OUTCOME_FAILED: _ClassVar[AssistantContent.CodeExecutionResult.Outcome]
            OUTCOME_DEADLINE_EXCEEDED: _ClassVar[AssistantContent.CodeExecutionResult.Outcome]
        OUTCOME_UNSPECIFIED: AssistantContent.CodeExecutionResult.Outcome
        OUTCOME_OK: AssistantContent.CodeExecutionResult.Outcome
        OUTCOME_FAILED: AssistantContent.CodeExecutionResult.Outcome
        OUTCOME_DEADLINE_EXCEEDED: AssistantContent.CodeExecutionResult.Outcome
        OUTCOME_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        outcome: AssistantContent.CodeExecutionResult.Outcome
        output: str

        def __init__(self, outcome: _Optional[_Union[AssistantContent.CodeExecutionResult.Outcome, str]]=..., output: _Optional[str]=...) -> None:
            ...
    TEXT_FIELD_NUMBER: _ClassVar[int]
    INLINE_DATA_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    EXECUTABLE_CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_EXECUTION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    THOUGHT_FIELD_NUMBER: _ClassVar[int]
    text: str
    inline_data: AssistantContent.Blob
    file: AssistantContent.File
    executable_code: AssistantContent.ExecutableCode
    code_execution_result: AssistantContent.CodeExecutionResult
    role: str
    thought: bool

    def __init__(self, text: _Optional[str]=..., inline_data: _Optional[_Union[AssistantContent.Blob, _Mapping]]=..., file: _Optional[_Union[AssistantContent.File, _Mapping]]=..., executable_code: _Optional[_Union[AssistantContent.ExecutableCode, _Mapping]]=..., code_execution_result: _Optional[_Union[AssistantContent.CodeExecutionResult, _Mapping]]=..., role: _Optional[str]=..., thought: bool=...) -> None:
        ...

class AssistantGroundedContent(_message.Message):
    __slots__ = ('text_grounding_metadata', 'content')

    class TextGroundingMetadata(_message.Message):
        __slots__ = ('segments', 'references')

        class Segment(_message.Message):
            __slots__ = ('start_index', 'end_index', 'reference_indices', 'grounding_score', 'text')
            START_INDEX_FIELD_NUMBER: _ClassVar[int]
            END_INDEX_FIELD_NUMBER: _ClassVar[int]
            REFERENCE_INDICES_FIELD_NUMBER: _ClassVar[int]
            GROUNDING_SCORE_FIELD_NUMBER: _ClassVar[int]
            TEXT_FIELD_NUMBER: _ClassVar[int]
            start_index: int
            end_index: int
            reference_indices: _containers.RepeatedScalarFieldContainer[int]
            grounding_score: float
            text: str

            def __init__(self, start_index: _Optional[int]=..., end_index: _Optional[int]=..., reference_indices: _Optional[_Iterable[int]]=..., grounding_score: _Optional[float]=..., text: _Optional[str]=...) -> None:
                ...

        class Reference(_message.Message):
            __slots__ = ('content', 'document_metadata')

            class DocumentMetadata(_message.Message):
                __slots__ = ('document', 'uri', 'title', 'page_identifier', 'domain')
                DOCUMENT_FIELD_NUMBER: _ClassVar[int]
                URI_FIELD_NUMBER: _ClassVar[int]
                TITLE_FIELD_NUMBER: _ClassVar[int]
                PAGE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
                DOMAIN_FIELD_NUMBER: _ClassVar[int]
                document: str
                uri: str
                title: str
                page_identifier: str
                domain: str

                def __init__(self, document: _Optional[str]=..., uri: _Optional[str]=..., title: _Optional[str]=..., page_identifier: _Optional[str]=..., domain: _Optional[str]=...) -> None:
                    ...
            CONTENT_FIELD_NUMBER: _ClassVar[int]
            DOCUMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
            content: str
            document_metadata: AssistantGroundedContent.TextGroundingMetadata.Reference.DocumentMetadata

            def __init__(self, content: _Optional[str]=..., document_metadata: _Optional[_Union[AssistantGroundedContent.TextGroundingMetadata.Reference.DocumentMetadata, _Mapping]]=...) -> None:
                ...
        SEGMENTS_FIELD_NUMBER: _ClassVar[int]
        REFERENCES_FIELD_NUMBER: _ClassVar[int]
        segments: _containers.RepeatedCompositeFieldContainer[AssistantGroundedContent.TextGroundingMetadata.Segment]
        references: _containers.RepeatedCompositeFieldContainer[AssistantGroundedContent.TextGroundingMetadata.Reference]

        def __init__(self, segments: _Optional[_Iterable[_Union[AssistantGroundedContent.TextGroundingMetadata.Segment, _Mapping]]]=..., references: _Optional[_Iterable[_Union[AssistantGroundedContent.TextGroundingMetadata.Reference, _Mapping]]]=...) -> None:
            ...
    TEXT_GROUNDING_METADATA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    text_grounding_metadata: AssistantGroundedContent.TextGroundingMetadata
    content: AssistantContent

    def __init__(self, text_grounding_metadata: _Optional[_Union[AssistantGroundedContent.TextGroundingMetadata, _Mapping]]=..., content: _Optional[_Union[AssistantContent, _Mapping]]=...) -> None:
        ...