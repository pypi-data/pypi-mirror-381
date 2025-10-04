from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TermsOfServiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TERMS_OF_SERVICE_STATUS_UNSPECIFIED: _ClassVar[TermsOfServiceStatus]
    ACCEPTED: _ClassVar[TermsOfServiceStatus]
    REJECTED: _ClassVar[TermsOfServiceStatus]
TERMS_OF_SERVICE_STATUS_UNSPECIFIED: TermsOfServiceStatus
ACCEPTED: TermsOfServiceStatus
REJECTED: TermsOfServiceStatus

class TermsOfService(_message.Message):
    __slots__ = ('customer_match_terms_of_service_status',)
    CUSTOMER_MATCH_TERMS_OF_SERVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
    customer_match_terms_of_service_status: TermsOfServiceStatus

    def __init__(self, customer_match_terms_of_service_status: _Optional[_Union[TermsOfServiceStatus, str]]=...) -> None:
        ...