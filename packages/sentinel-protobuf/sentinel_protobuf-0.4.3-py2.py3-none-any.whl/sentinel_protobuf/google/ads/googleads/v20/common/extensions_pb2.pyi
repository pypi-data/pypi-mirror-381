from google.ads.googleads.v20.common import custom_parameter_pb2 as _custom_parameter_pb2
from google.ads.googleads.v20.enums import call_conversion_reporting_state_pb2 as _call_conversion_reporting_state_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CallFeedItem(_message.Message):
    __slots__ = ('phone_number', 'country_code', 'call_tracking_enabled', 'call_conversion_action', 'call_conversion_tracking_disabled', 'call_conversion_reporting_state')
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    CALL_TRACKING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CALL_CONVERSION_ACTION_FIELD_NUMBER: _ClassVar[int]
    CALL_CONVERSION_TRACKING_DISABLED_FIELD_NUMBER: _ClassVar[int]
    CALL_CONVERSION_REPORTING_STATE_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    country_code: str
    call_tracking_enabled: bool
    call_conversion_action: str
    call_conversion_tracking_disabled: bool
    call_conversion_reporting_state: _call_conversion_reporting_state_pb2.CallConversionReportingStateEnum.CallConversionReportingState

    def __init__(self, phone_number: _Optional[str]=..., country_code: _Optional[str]=..., call_tracking_enabled: bool=..., call_conversion_action: _Optional[str]=..., call_conversion_tracking_disabled: bool=..., call_conversion_reporting_state: _Optional[_Union[_call_conversion_reporting_state_pb2.CallConversionReportingStateEnum.CallConversionReportingState, str]]=...) -> None:
        ...

class CalloutFeedItem(_message.Message):
    __slots__ = ('callout_text',)
    CALLOUT_TEXT_FIELD_NUMBER: _ClassVar[int]
    callout_text: str

    def __init__(self, callout_text: _Optional[str]=...) -> None:
        ...

class SitelinkFeedItem(_message.Message):
    __slots__ = ('link_text', 'line1', 'line2', 'final_urls', 'final_mobile_urls', 'tracking_url_template', 'url_custom_parameters', 'final_url_suffix')
    LINK_TEXT_FIELD_NUMBER: _ClassVar[int]
    LINE1_FIELD_NUMBER: _ClassVar[int]
    LINE2_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_MOBILE_URLS_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    URL_CUSTOM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    FINAL_URL_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    link_text: str
    line1: str
    line2: str
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    final_mobile_urls: _containers.RepeatedScalarFieldContainer[str]
    tracking_url_template: str
    url_custom_parameters: _containers.RepeatedCompositeFieldContainer[_custom_parameter_pb2.CustomParameter]
    final_url_suffix: str

    def __init__(self, link_text: _Optional[str]=..., line1: _Optional[str]=..., line2: _Optional[str]=..., final_urls: _Optional[_Iterable[str]]=..., final_mobile_urls: _Optional[_Iterable[str]]=..., tracking_url_template: _Optional[str]=..., url_custom_parameters: _Optional[_Iterable[_Union[_custom_parameter_pb2.CustomParameter, _Mapping]]]=..., final_url_suffix: _Optional[str]=...) -> None:
        ...