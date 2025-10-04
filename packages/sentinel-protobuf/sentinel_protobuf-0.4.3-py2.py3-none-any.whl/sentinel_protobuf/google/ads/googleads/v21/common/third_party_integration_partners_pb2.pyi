from google.ads.googleads.v21.enums import third_party_brand_lift_integration_partner_pb2 as _third_party_brand_lift_integration_partner_pb2
from google.ads.googleads.v21.enums import third_party_brand_safety_integration_partner_pb2 as _third_party_brand_safety_integration_partner_pb2
from google.ads.googleads.v21.enums import third_party_reach_integration_partner_pb2 as _third_party_reach_integration_partner_pb2
from google.ads.googleads.v21.enums import third_party_viewability_integration_partner_pb2 as _third_party_viewability_integration_partner_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomerThirdPartyIntegrationPartners(_message.Message):
    __slots__ = ('viewability_integration_partners', 'brand_lift_integration_partners', 'brand_safety_integration_partners', 'reach_integration_partners')
    VIEWABILITY_INTEGRATION_PARTNERS_FIELD_NUMBER: _ClassVar[int]
    BRAND_LIFT_INTEGRATION_PARTNERS_FIELD_NUMBER: _ClassVar[int]
    BRAND_SAFETY_INTEGRATION_PARTNERS_FIELD_NUMBER: _ClassVar[int]
    REACH_INTEGRATION_PARTNERS_FIELD_NUMBER: _ClassVar[int]
    viewability_integration_partners: _containers.RepeatedCompositeFieldContainer[CustomerThirdPartyViewabilityIntegrationPartner]
    brand_lift_integration_partners: _containers.RepeatedCompositeFieldContainer[CustomerThirdPartyBrandLiftIntegrationPartner]
    brand_safety_integration_partners: _containers.RepeatedCompositeFieldContainer[CustomerThirdPartyBrandSafetyIntegrationPartner]
    reach_integration_partners: _containers.RepeatedCompositeFieldContainer[CustomerThirdPartyReachIntegrationPartner]

    def __init__(self, viewability_integration_partners: _Optional[_Iterable[_Union[CustomerThirdPartyViewabilityIntegrationPartner, _Mapping]]]=..., brand_lift_integration_partners: _Optional[_Iterable[_Union[CustomerThirdPartyBrandLiftIntegrationPartner, _Mapping]]]=..., brand_safety_integration_partners: _Optional[_Iterable[_Union[CustomerThirdPartyBrandSafetyIntegrationPartner, _Mapping]]]=..., reach_integration_partners: _Optional[_Iterable[_Union[CustomerThirdPartyReachIntegrationPartner, _Mapping]]]=...) -> None:
        ...

class CustomerThirdPartyViewabilityIntegrationPartner(_message.Message):
    __slots__ = ('viewability_integration_partner', 'allow_share_cost')
    VIEWABILITY_INTEGRATION_PARTNER_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SHARE_COST_FIELD_NUMBER: _ClassVar[int]
    viewability_integration_partner: _third_party_viewability_integration_partner_pb2.ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner
    allow_share_cost: bool

    def __init__(self, viewability_integration_partner: _Optional[_Union[_third_party_viewability_integration_partner_pb2.ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner, str]]=..., allow_share_cost: bool=...) -> None:
        ...

class CustomerThirdPartyBrandSafetyIntegrationPartner(_message.Message):
    __slots__ = ('brand_safety_integration_partner',)
    BRAND_SAFETY_INTEGRATION_PARTNER_FIELD_NUMBER: _ClassVar[int]
    brand_safety_integration_partner: _third_party_brand_safety_integration_partner_pb2.ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner

    def __init__(self, brand_safety_integration_partner: _Optional[_Union[_third_party_brand_safety_integration_partner_pb2.ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner, str]]=...) -> None:
        ...

class CustomerThirdPartyBrandLiftIntegrationPartner(_message.Message):
    __slots__ = ('brand_lift_integration_partner', 'allow_share_cost')
    BRAND_LIFT_INTEGRATION_PARTNER_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SHARE_COST_FIELD_NUMBER: _ClassVar[int]
    brand_lift_integration_partner: _third_party_brand_lift_integration_partner_pb2.ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner
    allow_share_cost: bool

    def __init__(self, brand_lift_integration_partner: _Optional[_Union[_third_party_brand_lift_integration_partner_pb2.ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner, str]]=..., allow_share_cost: bool=...) -> None:
        ...

class CustomerThirdPartyReachIntegrationPartner(_message.Message):
    __slots__ = ('reach_integration_partner', 'allow_share_cost')
    REACH_INTEGRATION_PARTNER_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SHARE_COST_FIELD_NUMBER: _ClassVar[int]
    reach_integration_partner: _third_party_reach_integration_partner_pb2.ThirdPartyReachIntegrationPartnerEnum.ThirdPartyReachIntegrationPartner
    allow_share_cost: bool

    def __init__(self, reach_integration_partner: _Optional[_Union[_third_party_reach_integration_partner_pb2.ThirdPartyReachIntegrationPartnerEnum.ThirdPartyReachIntegrationPartner, str]]=..., allow_share_cost: bool=...) -> None:
        ...

class CampaignThirdPartyIntegrationPartners(_message.Message):
    __slots__ = ('viewability_integration_partners', 'brand_lift_integration_partners', 'brand_safety_integration_partners', 'reach_integration_partners')
    VIEWABILITY_INTEGRATION_PARTNERS_FIELD_NUMBER: _ClassVar[int]
    BRAND_LIFT_INTEGRATION_PARTNERS_FIELD_NUMBER: _ClassVar[int]
    BRAND_SAFETY_INTEGRATION_PARTNERS_FIELD_NUMBER: _ClassVar[int]
    REACH_INTEGRATION_PARTNERS_FIELD_NUMBER: _ClassVar[int]
    viewability_integration_partners: _containers.RepeatedCompositeFieldContainer[CampaignThirdPartyViewabilityIntegrationPartner]
    brand_lift_integration_partners: _containers.RepeatedCompositeFieldContainer[CampaignThirdPartyBrandLiftIntegrationPartner]
    brand_safety_integration_partners: _containers.RepeatedCompositeFieldContainer[CampaignThirdPartyBrandSafetyIntegrationPartner]
    reach_integration_partners: _containers.RepeatedCompositeFieldContainer[CampaignThirdPartyReachIntegrationPartner]

    def __init__(self, viewability_integration_partners: _Optional[_Iterable[_Union[CampaignThirdPartyViewabilityIntegrationPartner, _Mapping]]]=..., brand_lift_integration_partners: _Optional[_Iterable[_Union[CampaignThirdPartyBrandLiftIntegrationPartner, _Mapping]]]=..., brand_safety_integration_partners: _Optional[_Iterable[_Union[CampaignThirdPartyBrandSafetyIntegrationPartner, _Mapping]]]=..., reach_integration_partners: _Optional[_Iterable[_Union[CampaignThirdPartyReachIntegrationPartner, _Mapping]]]=...) -> None:
        ...

class CampaignThirdPartyViewabilityIntegrationPartner(_message.Message):
    __slots__ = ('viewability_integration_partner', 'viewability_integration_partner_data', 'share_cost')
    VIEWABILITY_INTEGRATION_PARTNER_FIELD_NUMBER: _ClassVar[int]
    VIEWABILITY_INTEGRATION_PARTNER_DATA_FIELD_NUMBER: _ClassVar[int]
    SHARE_COST_FIELD_NUMBER: _ClassVar[int]
    viewability_integration_partner: _third_party_viewability_integration_partner_pb2.ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner
    viewability_integration_partner_data: ThirdPartyIntegrationPartnerData
    share_cost: bool

    def __init__(self, viewability_integration_partner: _Optional[_Union[_third_party_viewability_integration_partner_pb2.ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner, str]]=..., viewability_integration_partner_data: _Optional[_Union[ThirdPartyIntegrationPartnerData, _Mapping]]=..., share_cost: bool=...) -> None:
        ...

class CampaignThirdPartyBrandSafetyIntegrationPartner(_message.Message):
    __slots__ = ('brand_safety_integration_partner', 'brand_safety_integration_partner_data')
    BRAND_SAFETY_INTEGRATION_PARTNER_FIELD_NUMBER: _ClassVar[int]
    BRAND_SAFETY_INTEGRATION_PARTNER_DATA_FIELD_NUMBER: _ClassVar[int]
    brand_safety_integration_partner: _third_party_brand_safety_integration_partner_pb2.ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner
    brand_safety_integration_partner_data: ThirdPartyIntegrationPartnerData

    def __init__(self, brand_safety_integration_partner: _Optional[_Union[_third_party_brand_safety_integration_partner_pb2.ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner, str]]=..., brand_safety_integration_partner_data: _Optional[_Union[ThirdPartyIntegrationPartnerData, _Mapping]]=...) -> None:
        ...

class CampaignThirdPartyBrandLiftIntegrationPartner(_message.Message):
    __slots__ = ('brand_lift_integration_partner', 'brand_lift_integration_partner_data', 'share_cost')
    BRAND_LIFT_INTEGRATION_PARTNER_FIELD_NUMBER: _ClassVar[int]
    BRAND_LIFT_INTEGRATION_PARTNER_DATA_FIELD_NUMBER: _ClassVar[int]
    SHARE_COST_FIELD_NUMBER: _ClassVar[int]
    brand_lift_integration_partner: _third_party_brand_lift_integration_partner_pb2.ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner
    brand_lift_integration_partner_data: ThirdPartyIntegrationPartnerData
    share_cost: bool

    def __init__(self, brand_lift_integration_partner: _Optional[_Union[_third_party_brand_lift_integration_partner_pb2.ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner, str]]=..., brand_lift_integration_partner_data: _Optional[_Union[ThirdPartyIntegrationPartnerData, _Mapping]]=..., share_cost: bool=...) -> None:
        ...

class CampaignThirdPartyReachIntegrationPartner(_message.Message):
    __slots__ = ('reach_integration_partner', 'reach_integration_partner_data', 'share_cost')
    REACH_INTEGRATION_PARTNER_FIELD_NUMBER: _ClassVar[int]
    REACH_INTEGRATION_PARTNER_DATA_FIELD_NUMBER: _ClassVar[int]
    SHARE_COST_FIELD_NUMBER: _ClassVar[int]
    reach_integration_partner: _third_party_reach_integration_partner_pb2.ThirdPartyReachIntegrationPartnerEnum.ThirdPartyReachIntegrationPartner
    reach_integration_partner_data: ThirdPartyIntegrationPartnerData
    share_cost: bool

    def __init__(self, reach_integration_partner: _Optional[_Union[_third_party_reach_integration_partner_pb2.ThirdPartyReachIntegrationPartnerEnum.ThirdPartyReachIntegrationPartner, str]]=..., reach_integration_partner_data: _Optional[_Union[ThirdPartyIntegrationPartnerData, _Mapping]]=..., share_cost: bool=...) -> None:
        ...

class ThirdPartyIntegrationPartnerData(_message.Message):
    __slots__ = ('client_id', 'third_party_placement_id')
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    THIRD_PARTY_PLACEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    third_party_placement_id: str

    def __init__(self, client_id: _Optional[str]=..., third_party_placement_id: _Optional[str]=...) -> None:
        ...