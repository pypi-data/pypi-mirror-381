from google.ads.googleads.v21.common import policy_pb2 as _policy_pb2
from google.ads.googleads.v21.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v21.resources import ad_pb2 as _ad_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MutateAdsRequest(_message.Message):
    __slots__ = ('customer_id', 'operations', 'partial_failure', 'response_content_type', 'validate_only')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[AdOperation]
    partial_failure: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType
    validate_only: bool

    def __init__(self, customer_id: _Optional[str]=..., operations: _Optional[_Iterable[_Union[AdOperation, _Mapping]]]=..., partial_failure: bool=..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]]=..., validate_only: bool=...) -> None:
        ...

class AdOperation(_message.Message):
    __slots__ = ('update_mask', 'policy_validation_parameter', 'update')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    POLICY_VALIDATION_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    policy_validation_parameter: _policy_pb2.PolicyValidationParameter
    update: _ad_pb2.Ad

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., policy_validation_parameter: _Optional[_Union[_policy_pb2.PolicyValidationParameter, _Mapping]]=..., update: _Optional[_Union[_ad_pb2.Ad, _Mapping]]=...) -> None:
        ...

class MutateAdsResponse(_message.Message):
    __slots__ = ('partial_failure_error', 'results')
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[MutateAdResult]

    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., results: _Optional[_Iterable[_Union[MutateAdResult, _Mapping]]]=...) -> None:
        ...

class MutateAdResult(_message.Message):
    __slots__ = ('resource_name', 'ad')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    ad: _ad_pb2.Ad

    def __init__(self, resource_name: _Optional[str]=..., ad: _Optional[_Union[_ad_pb2.Ad, _Mapping]]=...) -> None:
        ...