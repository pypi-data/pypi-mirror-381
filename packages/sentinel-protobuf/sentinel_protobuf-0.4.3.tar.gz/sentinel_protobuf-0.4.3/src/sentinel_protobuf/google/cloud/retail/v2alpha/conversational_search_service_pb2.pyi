from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.retail.v2alpha import common_pb2 as _common_pb2
from google.cloud.retail.v2alpha import safety_pb2 as _safety_pb2
from google.cloud.retail.v2alpha import search_service_pb2 as _search_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConversationalSearchRequest(_message.Message):
    __slots__ = ('placement', 'branch', 'query', 'page_categories', 'conversation_id', 'search_params', 'visitor_id', 'user_info', 'conversational_filtering_spec', 'user_labels', 'safety_settings')

    class SearchParams(_message.Message):
        __slots__ = ('filter', 'canonical_filter', 'sort_by', 'boost_spec')
        FILTER_FIELD_NUMBER: _ClassVar[int]
        CANONICAL_FILTER_FIELD_NUMBER: _ClassVar[int]
        SORT_BY_FIELD_NUMBER: _ClassVar[int]
        BOOST_SPEC_FIELD_NUMBER: _ClassVar[int]
        filter: str
        canonical_filter: str
        sort_by: str
        boost_spec: _search_service_pb2.SearchRequest.BoostSpec

        def __init__(self, filter: _Optional[str]=..., canonical_filter: _Optional[str]=..., sort_by: _Optional[str]=..., boost_spec: _Optional[_Union[_search_service_pb2.SearchRequest.BoostSpec, _Mapping]]=...) -> None:
            ...

    class UserAnswer(_message.Message):
        __slots__ = ('text_answer', 'selected_answer')

        class SelectedAnswer(_message.Message):
            __slots__ = ('product_attribute_value',)
            PRODUCT_ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
            product_attribute_value: _search_service_pb2.ProductAttributeValue

            def __init__(self, product_attribute_value: _Optional[_Union[_search_service_pb2.ProductAttributeValue, _Mapping]]=...) -> None:
                ...
        TEXT_ANSWER_FIELD_NUMBER: _ClassVar[int]
        SELECTED_ANSWER_FIELD_NUMBER: _ClassVar[int]
        text_answer: str
        selected_answer: ConversationalSearchRequest.UserAnswer.SelectedAnswer

        def __init__(self, text_answer: _Optional[str]=..., selected_answer: _Optional[_Union[ConversationalSearchRequest.UserAnswer.SelectedAnswer, _Mapping]]=...) -> None:
            ...

    class ConversationalFilteringSpec(_message.Message):
        __slots__ = ('enable_conversational_filtering', 'user_answer', 'conversational_filtering_mode')

        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MODE_UNSPECIFIED: _ClassVar[ConversationalSearchRequest.ConversationalFilteringSpec.Mode]
            DISABLED: _ClassVar[ConversationalSearchRequest.ConversationalFilteringSpec.Mode]
            ENABLED: _ClassVar[ConversationalSearchRequest.ConversationalFilteringSpec.Mode]
            CONVERSATIONAL_FILTER_ONLY: _ClassVar[ConversationalSearchRequest.ConversationalFilteringSpec.Mode]
        MODE_UNSPECIFIED: ConversationalSearchRequest.ConversationalFilteringSpec.Mode
        DISABLED: ConversationalSearchRequest.ConversationalFilteringSpec.Mode
        ENABLED: ConversationalSearchRequest.ConversationalFilteringSpec.Mode
        CONVERSATIONAL_FILTER_ONLY: ConversationalSearchRequest.ConversationalFilteringSpec.Mode
        ENABLE_CONVERSATIONAL_FILTERING_FIELD_NUMBER: _ClassVar[int]
        USER_ANSWER_FIELD_NUMBER: _ClassVar[int]
        CONVERSATIONAL_FILTERING_MODE_FIELD_NUMBER: _ClassVar[int]
        enable_conversational_filtering: bool
        user_answer: ConversationalSearchRequest.UserAnswer
        conversational_filtering_mode: ConversationalSearchRequest.ConversationalFilteringSpec.Mode

        def __init__(self, enable_conversational_filtering: bool=..., user_answer: _Optional[_Union[ConversationalSearchRequest.UserAnswer, _Mapping]]=..., conversational_filtering_mode: _Optional[_Union[ConversationalSearchRequest.ConversationalFilteringSpec.Mode, str]]=...) -> None:
            ...

    class UserLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    PAGE_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    VISITOR_ID_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    CONVERSATIONAL_FILTERING_SPEC_FIELD_NUMBER: _ClassVar[int]
    USER_LABELS_FIELD_NUMBER: _ClassVar[int]
    SAFETY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    placement: str
    branch: str
    query: str
    page_categories: _containers.RepeatedScalarFieldContainer[str]
    conversation_id: str
    search_params: ConversationalSearchRequest.SearchParams
    visitor_id: str
    user_info: _common_pb2.UserInfo
    conversational_filtering_spec: ConversationalSearchRequest.ConversationalFilteringSpec
    user_labels: _containers.ScalarMap[str, str]
    safety_settings: _containers.RepeatedCompositeFieldContainer[_safety_pb2.SafetySetting]

    def __init__(self, placement: _Optional[str]=..., branch: _Optional[str]=..., query: _Optional[str]=..., page_categories: _Optional[_Iterable[str]]=..., conversation_id: _Optional[str]=..., search_params: _Optional[_Union[ConversationalSearchRequest.SearchParams, _Mapping]]=..., visitor_id: _Optional[str]=..., user_info: _Optional[_Union[_common_pb2.UserInfo, _Mapping]]=..., conversational_filtering_spec: _Optional[_Union[ConversationalSearchRequest.ConversationalFilteringSpec, _Mapping]]=..., user_labels: _Optional[_Mapping[str, str]]=..., safety_settings: _Optional[_Iterable[_Union[_safety_pb2.SafetySetting, _Mapping]]]=...) -> None:
        ...

class ConversationalSearchResponse(_message.Message):
    __slots__ = ('user_query_types', 'conversational_text_response', 'followup_question', 'conversation_id', 'refined_search', 'conversational_filtering_result', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ConversationalSearchResponse.State]
        STREAMING: _ClassVar[ConversationalSearchResponse.State]
        SUCCEEDED: _ClassVar[ConversationalSearchResponse.State]
    STATE_UNSPECIFIED: ConversationalSearchResponse.State
    STREAMING: ConversationalSearchResponse.State
    SUCCEEDED: ConversationalSearchResponse.State

    class FollowupQuestion(_message.Message):
        __slots__ = ('followup_question', 'suggested_answers')

        class SuggestedAnswer(_message.Message):
            __slots__ = ('product_attribute_value',)
            PRODUCT_ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
            product_attribute_value: _search_service_pb2.ProductAttributeValue

            def __init__(self, product_attribute_value: _Optional[_Union[_search_service_pb2.ProductAttributeValue, _Mapping]]=...) -> None:
                ...
        FOLLOWUP_QUESTION_FIELD_NUMBER: _ClassVar[int]
        SUGGESTED_ANSWERS_FIELD_NUMBER: _ClassVar[int]
        followup_question: str
        suggested_answers: _containers.RepeatedCompositeFieldContainer[ConversationalSearchResponse.FollowupQuestion.SuggestedAnswer]

        def __init__(self, followup_question: _Optional[str]=..., suggested_answers: _Optional[_Iterable[_Union[ConversationalSearchResponse.FollowupQuestion.SuggestedAnswer, _Mapping]]]=...) -> None:
            ...

    class RefinedSearch(_message.Message):
        __slots__ = ('query',)
        QUERY_FIELD_NUMBER: _ClassVar[int]
        query: str

        def __init__(self, query: _Optional[str]=...) -> None:
            ...

    class ConversationalFilteringResult(_message.Message):
        __slots__ = ('followup_question', 'additional_filter')

        class AdditionalFilter(_message.Message):
            __slots__ = ('product_attribute_value',)
            PRODUCT_ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
            product_attribute_value: _search_service_pb2.ProductAttributeValue

            def __init__(self, product_attribute_value: _Optional[_Union[_search_service_pb2.ProductAttributeValue, _Mapping]]=...) -> None:
                ...
        FOLLOWUP_QUESTION_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_FILTER_FIELD_NUMBER: _ClassVar[int]
        followup_question: ConversationalSearchResponse.FollowupQuestion
        additional_filter: ConversationalSearchResponse.ConversationalFilteringResult.AdditionalFilter

        def __init__(self, followup_question: _Optional[_Union[ConversationalSearchResponse.FollowupQuestion, _Mapping]]=..., additional_filter: _Optional[_Union[ConversationalSearchResponse.ConversationalFilteringResult.AdditionalFilter, _Mapping]]=...) -> None:
            ...
    USER_QUERY_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONVERSATIONAL_TEXT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    FOLLOWUP_QUESTION_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    REFINED_SEARCH_FIELD_NUMBER: _ClassVar[int]
    CONVERSATIONAL_FILTERING_RESULT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    user_query_types: _containers.RepeatedScalarFieldContainer[str]
    conversational_text_response: str
    followup_question: ConversationalSearchResponse.FollowupQuestion
    conversation_id: str
    refined_search: _containers.RepeatedCompositeFieldContainer[ConversationalSearchResponse.RefinedSearch]
    conversational_filtering_result: ConversationalSearchResponse.ConversationalFilteringResult
    state: ConversationalSearchResponse.State

    def __init__(self, user_query_types: _Optional[_Iterable[str]]=..., conversational_text_response: _Optional[str]=..., followup_question: _Optional[_Union[ConversationalSearchResponse.FollowupQuestion, _Mapping]]=..., conversation_id: _Optional[str]=..., refined_search: _Optional[_Iterable[_Union[ConversationalSearchResponse.RefinedSearch, _Mapping]]]=..., conversational_filtering_result: _Optional[_Union[ConversationalSearchResponse.ConversationalFilteringResult, _Mapping]]=..., state: _Optional[_Union[ConversationalSearchResponse.State, str]]=...) -> None:
        ...