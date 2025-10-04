from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionPeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_PERIOD_UNSPECIFIED: _ClassVar[SubscriptionPeriod]
    MONTH: _ClassVar[SubscriptionPeriod]
    YEAR: _ClassVar[SubscriptionPeriod]

class AgeGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AGE_GROUP_UNSPECIFIED: _ClassVar[AgeGroup]
    ADULT: _ClassVar[AgeGroup]
    KIDS: _ClassVar[AgeGroup]
    TODDLER: _ClassVar[AgeGroup]
    INFANT: _ClassVar[AgeGroup]
    NEWBORN: _ClassVar[AgeGroup]

class Availability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AVAILABILITY_UNSPECIFIED: _ClassVar[Availability]
    IN_STOCK: _ClassVar[Availability]
    OUT_OF_STOCK: _ClassVar[Availability]
    PREORDER: _ClassVar[Availability]
    LIMITED_AVAILABILITY: _ClassVar[Availability]
    BACKORDER: _ClassVar[Availability]

class Condition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONDITION_UNSPECIFIED: _ClassVar[Condition]
    NEW: _ClassVar[Condition]
    USED: _ClassVar[Condition]
    REFURBISHED: _ClassVar[Condition]

class Gender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GENDER_UNSPECIFIED: _ClassVar[Gender]
    MALE: _ClassVar[Gender]
    FEMALE: _ClassVar[Gender]
    UNISEX: _ClassVar[Gender]

class CreditType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CREDIT_TYPE_UNSPECIFIED: _ClassVar[CreditType]
    FINANCE: _ClassVar[CreditType]
    LEASE: _ClassVar[CreditType]

class SizeSystem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIZE_SYSTEM_UNSPECIFIED: _ClassVar[SizeSystem]
    AU: _ClassVar[SizeSystem]
    BR: _ClassVar[SizeSystem]
    CN: _ClassVar[SizeSystem]
    DE: _ClassVar[SizeSystem]
    EU: _ClassVar[SizeSystem]
    FR: _ClassVar[SizeSystem]
    IT: _ClassVar[SizeSystem]
    JP: _ClassVar[SizeSystem]
    MEX: _ClassVar[SizeSystem]
    UK: _ClassVar[SizeSystem]
    US: _ClassVar[SizeSystem]

class SizeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIZE_TYPE_UNSPECIFIED: _ClassVar[SizeType]
    REGULAR: _ClassVar[SizeType]
    PETITE: _ClassVar[SizeType]
    MATERNITY: _ClassVar[SizeType]
    BIG: _ClassVar[SizeType]
    TALL: _ClassVar[SizeType]
    PLUS: _ClassVar[SizeType]

class EnergyEfficiencyClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENERGY_EFFICIENCY_CLASS_UNSPECIFIED: _ClassVar[EnergyEfficiencyClass]
    APPP: _ClassVar[EnergyEfficiencyClass]
    APP: _ClassVar[EnergyEfficiencyClass]
    AP: _ClassVar[EnergyEfficiencyClass]
    A: _ClassVar[EnergyEfficiencyClass]
    B: _ClassVar[EnergyEfficiencyClass]
    C: _ClassVar[EnergyEfficiencyClass]
    D: _ClassVar[EnergyEfficiencyClass]
    E: _ClassVar[EnergyEfficiencyClass]
    F: _ClassVar[EnergyEfficiencyClass]
    G: _ClassVar[EnergyEfficiencyClass]

class PickupMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PICKUP_METHOD_UNSPECIFIED: _ClassVar[PickupMethod]
    NOT_SUPPORTED: _ClassVar[PickupMethod]
    BUY: _ClassVar[PickupMethod]
    RESERVE: _ClassVar[PickupMethod]
    SHIP_TO_STORE: _ClassVar[PickupMethod]

class PickupSla(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PICKUP_SLA_UNSPECIFIED: _ClassVar[PickupSla]
    SAME_DAY: _ClassVar[PickupSla]
    NEXT_DAY: _ClassVar[PickupSla]
    TWO_DAY: _ClassVar[PickupSla]
    THREE_DAY: _ClassVar[PickupSla]
    FOUR_DAY: _ClassVar[PickupSla]
    FIVE_DAY: _ClassVar[PickupSla]
    SIX_DAY: _ClassVar[PickupSla]
    MULTI_WEEK: _ClassVar[PickupSla]

class Pause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAUSE_UNSPECIFIED: _ClassVar[Pause]
    ADS: _ClassVar[Pause]
    ALL: _ClassVar[Pause]

class CertificationAuthority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CERTIFICATION_AUTHORITY_UNSPECIFIED: _ClassVar[CertificationAuthority]
    ADEME: _ClassVar[CertificationAuthority]
    BMWK: _ClassVar[CertificationAuthority]
    EPA: _ClassVar[CertificationAuthority]
    EC: _ClassVar[CertificationAuthority]

class CertificationName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CERTIFICATION_NAME_UNSPECIFIED: _ClassVar[CertificationName]
    ENERGY_STAR: _ClassVar[CertificationName]
    ENERGY_STAR_MOST_EFFICIENT: _ClassVar[CertificationName]
    EPREL: _ClassVar[CertificationName]
    EU_ECOLABEL: _ClassVar[CertificationName]
    VEHICLE_ENERGY_EFFICIENCY: _ClassVar[CertificationName]
    VEHICLE_ENERGY_EFFICIENCY_DISCHARGED_BATTERY: _ClassVar[CertificationName]

class DigitalSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIGITAL_SOURCE_TYPE_UNSPECIFIED: _ClassVar[DigitalSourceType]
    TRAINED_ALGORITHMIC_MEDIA: _ClassVar[DigitalSourceType]
    DEFAULT: _ClassVar[DigitalSourceType]
SUBSCRIPTION_PERIOD_UNSPECIFIED: SubscriptionPeriod
MONTH: SubscriptionPeriod
YEAR: SubscriptionPeriod
AGE_GROUP_UNSPECIFIED: AgeGroup
ADULT: AgeGroup
KIDS: AgeGroup
TODDLER: AgeGroup
INFANT: AgeGroup
NEWBORN: AgeGroup
AVAILABILITY_UNSPECIFIED: Availability
IN_STOCK: Availability
OUT_OF_STOCK: Availability
PREORDER: Availability
LIMITED_AVAILABILITY: Availability
BACKORDER: Availability
CONDITION_UNSPECIFIED: Condition
NEW: Condition
USED: Condition
REFURBISHED: Condition
GENDER_UNSPECIFIED: Gender
MALE: Gender
FEMALE: Gender
UNISEX: Gender
CREDIT_TYPE_UNSPECIFIED: CreditType
FINANCE: CreditType
LEASE: CreditType
SIZE_SYSTEM_UNSPECIFIED: SizeSystem
AU: SizeSystem
BR: SizeSystem
CN: SizeSystem
DE: SizeSystem
EU: SizeSystem
FR: SizeSystem
IT: SizeSystem
JP: SizeSystem
MEX: SizeSystem
UK: SizeSystem
US: SizeSystem
SIZE_TYPE_UNSPECIFIED: SizeType
REGULAR: SizeType
PETITE: SizeType
MATERNITY: SizeType
BIG: SizeType
TALL: SizeType
PLUS: SizeType
ENERGY_EFFICIENCY_CLASS_UNSPECIFIED: EnergyEfficiencyClass
APPP: EnergyEfficiencyClass
APP: EnergyEfficiencyClass
AP: EnergyEfficiencyClass
A: EnergyEfficiencyClass
B: EnergyEfficiencyClass
C: EnergyEfficiencyClass
D: EnergyEfficiencyClass
E: EnergyEfficiencyClass
F: EnergyEfficiencyClass
G: EnergyEfficiencyClass
PICKUP_METHOD_UNSPECIFIED: PickupMethod
NOT_SUPPORTED: PickupMethod
BUY: PickupMethod
RESERVE: PickupMethod
SHIP_TO_STORE: PickupMethod
PICKUP_SLA_UNSPECIFIED: PickupSla
SAME_DAY: PickupSla
NEXT_DAY: PickupSla
TWO_DAY: PickupSla
THREE_DAY: PickupSla
FOUR_DAY: PickupSla
FIVE_DAY: PickupSla
SIX_DAY: PickupSla
MULTI_WEEK: PickupSla
PAUSE_UNSPECIFIED: Pause
ADS: Pause
ALL: Pause
CERTIFICATION_AUTHORITY_UNSPECIFIED: CertificationAuthority
ADEME: CertificationAuthority
BMWK: CertificationAuthority
EPA: CertificationAuthority
EC: CertificationAuthority
CERTIFICATION_NAME_UNSPECIFIED: CertificationName
ENERGY_STAR: CertificationName
ENERGY_STAR_MOST_EFFICIENT: CertificationName
EPREL: CertificationName
EU_ECOLABEL: CertificationName
VEHICLE_ENERGY_EFFICIENCY: CertificationName
VEHICLE_ENERGY_EFFICIENCY_DISCHARGED_BATTERY: CertificationName
DIGITAL_SOURCE_TYPE_UNSPECIFIED: DigitalSourceType
TRAINED_ALGORITHMIC_MEDIA: DigitalSourceType
DEFAULT: DigitalSourceType

class ProductAttributes(_message.Message):
    __slots__ = ('identifier_exists', 'is_bundle', 'title', 'description', 'link', 'mobile_link', 'canonical_link', 'image_link', 'additional_image_links', 'expiration_date', 'disclosure_date', 'adult', 'age_group', 'availability', 'availability_date', 'brand', 'color', 'condition', 'gender', 'google_product_category', 'gtins', 'item_group_id', 'material', 'mpn', 'pattern', 'price', 'maximum_retail_price', 'installment', 'subscription_cost', 'loyalty_points', 'loyalty_programs', 'product_types', 'sale_price', 'sale_price_effective_date', 'sell_on_google_quantity', 'product_height', 'product_length', 'product_width', 'product_weight', 'shipping', 'free_shipping_threshold', 'shipping_weight', 'shipping_length', 'shipping_width', 'shipping_height', 'max_handling_time', 'min_handling_time', 'shipping_label', 'transit_time_label', 'size', 'size_system', 'size_types', 'energy_efficiency_class', 'min_energy_efficiency_class', 'max_energy_efficiency_class', 'unit_pricing_measure', 'unit_pricing_base_measure', 'multipack', 'ads_grouping', 'ads_labels', 'ads_redirect', 'cost_of_goods_sold', 'product_details', 'product_highlights', 'display_ads_id', 'display_ads_similar_ids', 'display_ads_title', 'display_ads_link', 'display_ads_value', 'promotion_ids', 'pickup_method', 'pickup_sla', 'link_template', 'mobile_link_template', 'custom_label_0', 'custom_label_1', 'custom_label_2', 'custom_label_3', 'custom_label_4', 'included_destinations', 'excluded_destinations', 'shopping_ads_excluded_countries', 'external_seller_id', 'pause', 'lifestyle_image_links', 'cloud_export_additional_properties', 'virtual_model_link', 'certifications', 'structured_title', 'structured_description', 'auto_pricing_min_price', 'sustainability_incentives')
    IDENTIFIER_EXISTS_FIELD_NUMBER: _ClassVar[int]
    IS_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    MOBILE_LINK_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_LINK_FIELD_NUMBER: _ClassVar[int]
    IMAGE_LINK_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_IMAGE_LINKS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    DISCLOSURE_DATE_FIELD_NUMBER: _ClassVar[int]
    ADULT_FIELD_NUMBER: _ClassVar[int]
    AGE_GROUP_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_DATE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_PRODUCT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    GTINS_FIELD_NUMBER: _ClassVar[int]
    ITEM_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_FIELD_NUMBER: _ClassVar[int]
    MPN_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_RETAIL_PRICE_FIELD_NUMBER: _ClassVar[int]
    INSTALLMENT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_COST_FIELD_NUMBER: _ClassVar[int]
    LOYALTY_POINTS_FIELD_NUMBER: _ClassVar[int]
    LOYALTY_PROGRAMS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_TYPES_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_EFFECTIVE_DATE_FIELD_NUMBER: _ClassVar[int]
    SELL_ON_GOOGLE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_FIELD_NUMBER: _ClassVar[int]
    FREE_SHIPPING_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_WIDTH_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAX_HANDLING_TIME_FIELD_NUMBER: _ClassVar[int]
    MIN_HANDLING_TIME_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_LABEL_FIELD_NUMBER: _ClassVar[int]
    TRANSIT_TIME_LABEL_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SIZE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    SIZE_TYPES_FIELD_NUMBER: _ClassVar[int]
    ENERGY_EFFICIENCY_CLASS_FIELD_NUMBER: _ClassVar[int]
    MIN_ENERGY_EFFICIENCY_CLASS_FIELD_NUMBER: _ClassVar[int]
    MAX_ENERGY_EFFICIENCY_CLASS_FIELD_NUMBER: _ClassVar[int]
    UNIT_PRICING_MEASURE_FIELD_NUMBER: _ClassVar[int]
    UNIT_PRICING_BASE_MEASURE_FIELD_NUMBER: _ClassVar[int]
    MULTIPACK_FIELD_NUMBER: _ClassVar[int]
    ADS_GROUPING_FIELD_NUMBER: _ClassVar[int]
    ADS_LABELS_FIELD_NUMBER: _ClassVar[int]
    ADS_REDIRECT_FIELD_NUMBER: _ClassVar[int]
    COST_OF_GOODS_SOLD_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_HIGHLIGHTS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ADS_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ADS_SIMILAR_IDS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ADS_TITLE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ADS_LINK_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ADS_VALUE_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_IDS_FIELD_NUMBER: _ClassVar[int]
    PICKUP_METHOD_FIELD_NUMBER: _ClassVar[int]
    PICKUP_SLA_FIELD_NUMBER: _ClassVar[int]
    LINK_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    MOBILE_LINK_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL_0_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL_1_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL_2_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL_3_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LABEL_4_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    SHOPPING_ADS_EXCLUDED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_SELLER_ID_FIELD_NUMBER: _ClassVar[int]
    PAUSE_FIELD_NUMBER: _ClassVar[int]
    LIFESTYLE_IMAGE_LINKS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_EXPORT_ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_MODEL_LINK_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_TITLE_FIELD_NUMBER: _ClassVar[int]
    STRUCTURED_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AUTO_PRICING_MIN_PRICE_FIELD_NUMBER: _ClassVar[int]
    SUSTAINABILITY_INCENTIVES_FIELD_NUMBER: _ClassVar[int]
    identifier_exists: bool
    is_bundle: bool
    title: str
    description: str
    link: str
    mobile_link: str
    canonical_link: str
    image_link: str
    additional_image_links: _containers.RepeatedScalarFieldContainer[str]
    expiration_date: _timestamp_pb2.Timestamp
    disclosure_date: _timestamp_pb2.Timestamp
    adult: bool
    age_group: AgeGroup
    availability: Availability
    availability_date: _timestamp_pb2.Timestamp
    brand: str
    color: str
    condition: Condition
    gender: Gender
    google_product_category: str
    gtins: _containers.RepeatedScalarFieldContainer[str]
    item_group_id: str
    material: str
    mpn: str
    pattern: str
    price: _types_pb2.Price
    maximum_retail_price: _types_pb2.Price
    installment: ProductInstallment
    subscription_cost: SubscriptionCost
    loyalty_points: LoyaltyPoints
    loyalty_programs: _containers.RepeatedCompositeFieldContainer[LoyaltyProgram]
    product_types: _containers.RepeatedScalarFieldContainer[str]
    sale_price: _types_pb2.Price
    sale_price_effective_date: _interval_pb2.Interval
    sell_on_google_quantity: int
    product_height: ProductDimension
    product_length: ProductDimension
    product_width: ProductDimension
    product_weight: ProductWeight
    shipping: _containers.RepeatedCompositeFieldContainer[Shipping]
    free_shipping_threshold: _containers.RepeatedCompositeFieldContainer[FreeShippingThreshold]
    shipping_weight: ShippingWeight
    shipping_length: ShippingDimension
    shipping_width: ShippingDimension
    shipping_height: ShippingDimension
    max_handling_time: int
    min_handling_time: int
    shipping_label: str
    transit_time_label: str
    size: str
    size_system: SizeSystem
    size_types: _containers.RepeatedScalarFieldContainer[SizeType]
    energy_efficiency_class: EnergyEfficiencyClass
    min_energy_efficiency_class: EnergyEfficiencyClass
    max_energy_efficiency_class: EnergyEfficiencyClass
    unit_pricing_measure: UnitPricingMeasure
    unit_pricing_base_measure: UnitPricingBaseMeasure
    multipack: int
    ads_grouping: str
    ads_labels: _containers.RepeatedScalarFieldContainer[str]
    ads_redirect: str
    cost_of_goods_sold: _types_pb2.Price
    product_details: _containers.RepeatedCompositeFieldContainer[ProductDetail]
    product_highlights: _containers.RepeatedScalarFieldContainer[str]
    display_ads_id: str
    display_ads_similar_ids: _containers.RepeatedScalarFieldContainer[str]
    display_ads_title: str
    display_ads_link: str
    display_ads_value: float
    promotion_ids: _containers.RepeatedScalarFieldContainer[str]
    pickup_method: PickupMethod
    pickup_sla: PickupSla
    link_template: str
    mobile_link_template: str
    custom_label_0: str
    custom_label_1: str
    custom_label_2: str
    custom_label_3: str
    custom_label_4: str
    included_destinations: _containers.RepeatedScalarFieldContainer[_types_pb2.Destination.DestinationEnum]
    excluded_destinations: _containers.RepeatedScalarFieldContainer[_types_pb2.Destination.DestinationEnum]
    shopping_ads_excluded_countries: _containers.RepeatedScalarFieldContainer[str]
    external_seller_id: str
    pause: Pause
    lifestyle_image_links: _containers.RepeatedScalarFieldContainer[str]
    cloud_export_additional_properties: _containers.RepeatedCompositeFieldContainer[CloudExportAdditionalProperties]
    virtual_model_link: str
    certifications: _containers.RepeatedCompositeFieldContainer[ProductCertification]
    structured_title: StructuredTitle
    structured_description: StructuredDescription
    auto_pricing_min_price: _types_pb2.Price
    sustainability_incentives: _containers.RepeatedCompositeFieldContainer[ProductSustainabilityIncentive]

    def __init__(self, identifier_exists: bool=..., is_bundle: bool=..., title: _Optional[str]=..., description: _Optional[str]=..., link: _Optional[str]=..., mobile_link: _Optional[str]=..., canonical_link: _Optional[str]=..., image_link: _Optional[str]=..., additional_image_links: _Optional[_Iterable[str]]=..., expiration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., disclosure_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., adult: bool=..., age_group: _Optional[_Union[AgeGroup, str]]=..., availability: _Optional[_Union[Availability, str]]=..., availability_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., brand: _Optional[str]=..., color: _Optional[str]=..., condition: _Optional[_Union[Condition, str]]=..., gender: _Optional[_Union[Gender, str]]=..., google_product_category: _Optional[str]=..., gtins: _Optional[_Iterable[str]]=..., item_group_id: _Optional[str]=..., material: _Optional[str]=..., mpn: _Optional[str]=..., pattern: _Optional[str]=..., price: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., maximum_retail_price: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., installment: _Optional[_Union[ProductInstallment, _Mapping]]=..., subscription_cost: _Optional[_Union[SubscriptionCost, _Mapping]]=..., loyalty_points: _Optional[_Union[LoyaltyPoints, _Mapping]]=..., loyalty_programs: _Optional[_Iterable[_Union[LoyaltyProgram, _Mapping]]]=..., product_types: _Optional[_Iterable[str]]=..., sale_price: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., sale_price_effective_date: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., sell_on_google_quantity: _Optional[int]=..., product_height: _Optional[_Union[ProductDimension, _Mapping]]=..., product_length: _Optional[_Union[ProductDimension, _Mapping]]=..., product_width: _Optional[_Union[ProductDimension, _Mapping]]=..., product_weight: _Optional[_Union[ProductWeight, _Mapping]]=..., shipping: _Optional[_Iterable[_Union[Shipping, _Mapping]]]=..., free_shipping_threshold: _Optional[_Iterable[_Union[FreeShippingThreshold, _Mapping]]]=..., shipping_weight: _Optional[_Union[ShippingWeight, _Mapping]]=..., shipping_length: _Optional[_Union[ShippingDimension, _Mapping]]=..., shipping_width: _Optional[_Union[ShippingDimension, _Mapping]]=..., shipping_height: _Optional[_Union[ShippingDimension, _Mapping]]=..., max_handling_time: _Optional[int]=..., min_handling_time: _Optional[int]=..., shipping_label: _Optional[str]=..., transit_time_label: _Optional[str]=..., size: _Optional[str]=..., size_system: _Optional[_Union[SizeSystem, str]]=..., size_types: _Optional[_Iterable[_Union[SizeType, str]]]=..., energy_efficiency_class: _Optional[_Union[EnergyEfficiencyClass, str]]=..., min_energy_efficiency_class: _Optional[_Union[EnergyEfficiencyClass, str]]=..., max_energy_efficiency_class: _Optional[_Union[EnergyEfficiencyClass, str]]=..., unit_pricing_measure: _Optional[_Union[UnitPricingMeasure, _Mapping]]=..., unit_pricing_base_measure: _Optional[_Union[UnitPricingBaseMeasure, _Mapping]]=..., multipack: _Optional[int]=..., ads_grouping: _Optional[str]=..., ads_labels: _Optional[_Iterable[str]]=..., ads_redirect: _Optional[str]=..., cost_of_goods_sold: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., product_details: _Optional[_Iterable[_Union[ProductDetail, _Mapping]]]=..., product_highlights: _Optional[_Iterable[str]]=..., display_ads_id: _Optional[str]=..., display_ads_similar_ids: _Optional[_Iterable[str]]=..., display_ads_title: _Optional[str]=..., display_ads_link: _Optional[str]=..., display_ads_value: _Optional[float]=..., promotion_ids: _Optional[_Iterable[str]]=..., pickup_method: _Optional[_Union[PickupMethod, str]]=..., pickup_sla: _Optional[_Union[PickupSla, str]]=..., link_template: _Optional[str]=..., mobile_link_template: _Optional[str]=..., custom_label_0: _Optional[str]=..., custom_label_1: _Optional[str]=..., custom_label_2: _Optional[str]=..., custom_label_3: _Optional[str]=..., custom_label_4: _Optional[str]=..., included_destinations: _Optional[_Iterable[_Union[_types_pb2.Destination.DestinationEnum, str]]]=..., excluded_destinations: _Optional[_Iterable[_Union[_types_pb2.Destination.DestinationEnum, str]]]=..., shopping_ads_excluded_countries: _Optional[_Iterable[str]]=..., external_seller_id: _Optional[str]=..., pause: _Optional[_Union[Pause, str]]=..., lifestyle_image_links: _Optional[_Iterable[str]]=..., cloud_export_additional_properties: _Optional[_Iterable[_Union[CloudExportAdditionalProperties, _Mapping]]]=..., virtual_model_link: _Optional[str]=..., certifications: _Optional[_Iterable[_Union[ProductCertification, _Mapping]]]=..., structured_title: _Optional[_Union[StructuredTitle, _Mapping]]=..., structured_description: _Optional[_Union[StructuredDescription, _Mapping]]=..., auto_pricing_min_price: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., sustainability_incentives: _Optional[_Iterable[_Union[ProductSustainabilityIncentive, _Mapping]]]=...) -> None:
        ...

class ShippingWeight(_message.Message):
    __slots__ = ('value', 'unit')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: str

    def __init__(self, value: _Optional[float]=..., unit: _Optional[str]=...) -> None:
        ...

class ShippingDimension(_message.Message):
    __slots__ = ('value', 'unit')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: str

    def __init__(self, value: _Optional[float]=..., unit: _Optional[str]=...) -> None:
        ...

class UnitPricingBaseMeasure(_message.Message):
    __slots__ = ('value', 'unit')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: int
    unit: str

    def __init__(self, value: _Optional[int]=..., unit: _Optional[str]=...) -> None:
        ...

class UnitPricingMeasure(_message.Message):
    __slots__ = ('value', 'unit')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: str

    def __init__(self, value: _Optional[float]=..., unit: _Optional[str]=...) -> None:
        ...

class SubscriptionCost(_message.Message):
    __slots__ = ('period', 'period_length', 'amount')
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    PERIOD_LENGTH_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    period: SubscriptionPeriod
    period_length: int
    amount: _types_pb2.Price

    def __init__(self, period: _Optional[_Union[SubscriptionPeriod, str]]=..., period_length: _Optional[int]=..., amount: _Optional[_Union[_types_pb2.Price, _Mapping]]=...) -> None:
        ...

class ProductInstallment(_message.Message):
    __slots__ = ('months', 'amount', 'downpayment', 'credit_type')
    MONTHS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DOWNPAYMENT_FIELD_NUMBER: _ClassVar[int]
    CREDIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    months: int
    amount: _types_pb2.Price
    downpayment: _types_pb2.Price
    credit_type: CreditType

    def __init__(self, months: _Optional[int]=..., amount: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., downpayment: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., credit_type: _Optional[_Union[CreditType, str]]=...) -> None:
        ...

class LoyaltyPoints(_message.Message):
    __slots__ = ('name', 'points_value', 'ratio')
    NAME_FIELD_NUMBER: _ClassVar[int]
    POINTS_VALUE_FIELD_NUMBER: _ClassVar[int]
    RATIO_FIELD_NUMBER: _ClassVar[int]
    name: str
    points_value: int
    ratio: float

    def __init__(self, name: _Optional[str]=..., points_value: _Optional[int]=..., ratio: _Optional[float]=...) -> None:
        ...

class LoyaltyProgram(_message.Message):
    __slots__ = ('program_label', 'tier_label', 'price', 'cashback_for_future_use', 'loyalty_points', 'member_price_effective_date', 'shipping_label')
    PROGRAM_LABEL_FIELD_NUMBER: _ClassVar[int]
    TIER_LABEL_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CASHBACK_FOR_FUTURE_USE_FIELD_NUMBER: _ClassVar[int]
    LOYALTY_POINTS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_PRICE_EFFECTIVE_DATE_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_LABEL_FIELD_NUMBER: _ClassVar[int]
    program_label: str
    tier_label: str
    price: _types_pb2.Price
    cashback_for_future_use: _types_pb2.Price
    loyalty_points: int
    member_price_effective_date: _interval_pb2.Interval
    shipping_label: str

    def __init__(self, program_label: _Optional[str]=..., tier_label: _Optional[str]=..., price: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., cashback_for_future_use: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., loyalty_points: _Optional[int]=..., member_price_effective_date: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., shipping_label: _Optional[str]=...) -> None:
        ...

class Shipping(_message.Message):
    __slots__ = ('price', 'country', 'region', 'service', 'location_id', 'location_group_name', 'postal_code', 'min_handling_time', 'max_handling_time', 'min_transit_time', 'max_transit_time')
    PRICE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    MIN_HANDLING_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_HANDLING_TIME_FIELD_NUMBER: _ClassVar[int]
    MIN_TRANSIT_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_TRANSIT_TIME_FIELD_NUMBER: _ClassVar[int]
    price: _types_pb2.Price
    country: str
    region: str
    service: str
    location_id: int
    location_group_name: str
    postal_code: str
    min_handling_time: int
    max_handling_time: int
    min_transit_time: int
    max_transit_time: int

    def __init__(self, price: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., country: _Optional[str]=..., region: _Optional[str]=..., service: _Optional[str]=..., location_id: _Optional[int]=..., location_group_name: _Optional[str]=..., postal_code: _Optional[str]=..., min_handling_time: _Optional[int]=..., max_handling_time: _Optional[int]=..., min_transit_time: _Optional[int]=..., max_transit_time: _Optional[int]=...) -> None:
        ...

class FreeShippingThreshold(_message.Message):
    __slots__ = ('country', 'price_threshold')
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PRICE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    country: str
    price_threshold: _types_pb2.Price

    def __init__(self, country: _Optional[str]=..., price_threshold: _Optional[_Union[_types_pb2.Price, _Mapping]]=...) -> None:
        ...

class ProductDetail(_message.Message):
    __slots__ = ('section_name', 'attribute_name', 'attribute_value')
    SECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
    section_name: str
    attribute_name: str
    attribute_value: str

    def __init__(self, section_name: _Optional[str]=..., attribute_name: _Optional[str]=..., attribute_value: _Optional[str]=...) -> None:
        ...

class ProductCertification(_message.Message):
    __slots__ = ('certification_authority', 'certification_name', 'certification_code', 'certification_value')
    CERTIFICATION_AUTHORITY_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATION_NAME_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    certification_authority: CertificationAuthority
    certification_name: CertificationName
    certification_code: str
    certification_value: str

    def __init__(self, certification_authority: _Optional[_Union[CertificationAuthority, str]]=..., certification_name: _Optional[_Union[CertificationName, str]]=..., certification_code: _Optional[str]=..., certification_value: _Optional[str]=...) -> None:
        ...

class StructuredTitle(_message.Message):
    __slots__ = ('digital_source_type', 'content')
    DIGITAL_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    digital_source_type: DigitalSourceType
    content: str

    def __init__(self, digital_source_type: _Optional[_Union[DigitalSourceType, str]]=..., content: _Optional[str]=...) -> None:
        ...

class StructuredDescription(_message.Message):
    __slots__ = ('digital_source_type', 'content')
    DIGITAL_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    digital_source_type: DigitalSourceType
    content: str

    def __init__(self, digital_source_type: _Optional[_Union[DigitalSourceType, str]]=..., content: _Optional[str]=...) -> None:
        ...

class ProductDimension(_message.Message):
    __slots__ = ('value', 'unit')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: str

    def __init__(self, value: _Optional[float]=..., unit: _Optional[str]=...) -> None:
        ...

class ProductWeight(_message.Message):
    __slots__ = ('value', 'unit')
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    value: float
    unit: str

    def __init__(self, value: _Optional[float]=..., unit: _Optional[str]=...) -> None:
        ...

class ProductStatus(_message.Message):
    __slots__ = ('destination_statuses', 'item_level_issues', 'creation_date', 'last_update_date', 'google_expiration_date')

    class DestinationStatus(_message.Message):
        __slots__ = ('reporting_context', 'approved_countries', 'pending_countries', 'disapproved_countries')
        REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        APPROVED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
        PENDING_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
        DISAPPROVED_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
        reporting_context: _types_pb2.ReportingContext.ReportingContextEnum
        approved_countries: _containers.RepeatedScalarFieldContainer[str]
        pending_countries: _containers.RepeatedScalarFieldContainer[str]
        disapproved_countries: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, reporting_context: _Optional[_Union[_types_pb2.ReportingContext.ReportingContextEnum, str]]=..., approved_countries: _Optional[_Iterable[str]]=..., pending_countries: _Optional[_Iterable[str]]=..., disapproved_countries: _Optional[_Iterable[str]]=...) -> None:
            ...

    class ItemLevelIssue(_message.Message):
        __slots__ = ('code', 'severity', 'resolution', 'attribute', 'reporting_context', 'description', 'detail', 'documentation', 'applicable_countries')

        class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SEVERITY_UNSPECIFIED: _ClassVar[ProductStatus.ItemLevelIssue.Severity]
            NOT_IMPACTED: _ClassVar[ProductStatus.ItemLevelIssue.Severity]
            DEMOTED: _ClassVar[ProductStatus.ItemLevelIssue.Severity]
            DISAPPROVED: _ClassVar[ProductStatus.ItemLevelIssue.Severity]
        SEVERITY_UNSPECIFIED: ProductStatus.ItemLevelIssue.Severity
        NOT_IMPACTED: ProductStatus.ItemLevelIssue.Severity
        DEMOTED: ProductStatus.ItemLevelIssue.Severity
        DISAPPROVED: ProductStatus.ItemLevelIssue.Severity
        CODE_FIELD_NUMBER: _ClassVar[int]
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
        REPORTING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
        APPLICABLE_COUNTRIES_FIELD_NUMBER: _ClassVar[int]
        code: str
        severity: ProductStatus.ItemLevelIssue.Severity
        resolution: str
        attribute: str
        reporting_context: _types_pb2.ReportingContext.ReportingContextEnum
        description: str
        detail: str
        documentation: str
        applicable_countries: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, code: _Optional[str]=..., severity: _Optional[_Union[ProductStatus.ItemLevelIssue.Severity, str]]=..., resolution: _Optional[str]=..., attribute: _Optional[str]=..., reporting_context: _Optional[_Union[_types_pb2.ReportingContext.ReportingContextEnum, str]]=..., description: _Optional[str]=..., detail: _Optional[str]=..., documentation: _Optional[str]=..., applicable_countries: _Optional[_Iterable[str]]=...) -> None:
            ...
    DESTINATION_STATUSES_FIELD_NUMBER: _ClassVar[int]
    ITEM_LEVEL_ISSUES_FIELD_NUMBER: _ClassVar[int]
    CREATION_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_DATE_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    destination_statuses: _containers.RepeatedCompositeFieldContainer[ProductStatus.DestinationStatus]
    item_level_issues: _containers.RepeatedCompositeFieldContainer[ProductStatus.ItemLevelIssue]
    creation_date: _timestamp_pb2.Timestamp
    last_update_date: _timestamp_pb2.Timestamp
    google_expiration_date: _timestamp_pb2.Timestamp

    def __init__(self, destination_statuses: _Optional[_Iterable[_Union[ProductStatus.DestinationStatus, _Mapping]]]=..., item_level_issues: _Optional[_Iterable[_Union[ProductStatus.ItemLevelIssue, _Mapping]]]=..., creation_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_update_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., google_expiration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CloudExportAdditionalProperties(_message.Message):
    __slots__ = ('property_name', 'text_value', 'bool_value', 'int_value', 'float_value', 'min_value', 'max_value', 'unit_code')
    PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    UNIT_CODE_FIELD_NUMBER: _ClassVar[int]
    property_name: str
    text_value: _containers.RepeatedScalarFieldContainer[str]
    bool_value: bool
    int_value: _containers.RepeatedScalarFieldContainer[int]
    float_value: _containers.RepeatedScalarFieldContainer[float]
    min_value: float
    max_value: float
    unit_code: str

    def __init__(self, property_name: _Optional[str]=..., text_value: _Optional[_Iterable[str]]=..., bool_value: bool=..., int_value: _Optional[_Iterable[int]]=..., float_value: _Optional[_Iterable[float]]=..., min_value: _Optional[float]=..., max_value: _Optional[float]=..., unit_code: _Optional[str]=...) -> None:
        ...

class ProductSustainabilityIncentive(_message.Message):
    __slots__ = ('amount', 'percentage', 'type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[ProductSustainabilityIncentive.Type]
        EV_TAX_CREDIT: _ClassVar[ProductSustainabilityIncentive.Type]
        EV_PRICE_DISCOUNT: _ClassVar[ProductSustainabilityIncentive.Type]
    TYPE_UNSPECIFIED: ProductSustainabilityIncentive.Type
    EV_TAX_CREDIT: ProductSustainabilityIncentive.Type
    EV_PRICE_DISCOUNT: ProductSustainabilityIncentive.Type
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    amount: _types_pb2.Price
    percentage: float
    type: ProductSustainabilityIncentive.Type

    def __init__(self, amount: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., percentage: _Optional[float]=..., type: _Optional[_Union[ProductSustainabilityIncentive.Type, str]]=...) -> None:
        ...

class AutomatedDiscounts(_message.Message):
    __slots__ = ('prior_price', 'prior_price_progressive', 'gad_price')
    PRIOR_PRICE_FIELD_NUMBER: _ClassVar[int]
    PRIOR_PRICE_PROGRESSIVE_FIELD_NUMBER: _ClassVar[int]
    GAD_PRICE_FIELD_NUMBER: _ClassVar[int]
    prior_price: _types_pb2.Price
    prior_price_progressive: _types_pb2.Price
    gad_price: _types_pb2.Price

    def __init__(self, prior_price: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., prior_price_progressive: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., gad_price: _Optional[_Union[_types_pb2.Price, _Mapping]]=...) -> None:
        ...