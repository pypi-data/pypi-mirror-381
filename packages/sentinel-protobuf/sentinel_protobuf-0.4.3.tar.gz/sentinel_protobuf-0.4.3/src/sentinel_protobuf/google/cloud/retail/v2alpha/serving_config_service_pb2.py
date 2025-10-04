"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/serving_config_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import serving_config_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_serving__config__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/retail/v2alpha/serving_config_service.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/retail/v2alpha/serving_config.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xbc\x01\n\x1aCreateServingConfigRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12G\n\x0eserving_config\x18\x02 \x01(\x0b2*.google.cloud.retail.v2alpha.ServingConfigB\x03\xe0A\x02\x12\x1e\n\x11serving_config_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x96\x01\n\x1aUpdateServingConfigRequest\x12G\n\x0eserving_config\x18\x01 \x01(\x0b2*.google.cloud.retail.v2alpha.ServingConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"W\n\x1aDeleteServingConfigRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig"T\n\x17GetServingConfigRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig"\x83\x01\n\x19ListServingConfigsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"z\n\x1aListServingConfigsResponse\x12C\n\x0fserving_configs\x18\x01 \x03(\x0b2*.google.cloud.retail.v2alpha.ServingConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"q\n\x11AddControlRequest\x12C\n\x0eserving_config\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig\x12\x17\n\ncontrol_id\x18\x02 \x01(\tB\x03\xe0A\x02"t\n\x14RemoveControlRequest\x12C\n\x0eserving_config\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig\x12\x17\n\ncontrol_id\x18\x02 \x01(\tB\x03\xe0A\x022\x97\r\n\x14ServingConfigService\x12\x81\x02\n\x13CreateServingConfig\x127.google.cloud.retail.v2alpha.CreateServingConfigRequest\x1a*.google.cloud.retail.v2alpha.ServingConfig"\x84\x01\xdaA\'parent,serving_config,serving_config_id\x82\xd3\xe4\x93\x02T"B/v2alpha/{parent=projects/*/locations/*/catalogs/*}/servingConfigs:\x0eserving_config\x12\xb9\x01\n\x13DeleteServingConfig\x127.google.cloud.retail.v2alpha.DeleteServingConfigRequest\x1a\x16.google.protobuf.Empty"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D*B/v2alpha/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}\x12\x83\x02\n\x13UpdateServingConfig\x127.google.cloud.retail.v2alpha.UpdateServingConfigRequest\x1a*.google.cloud.retail.v2alpha.ServingConfig"\x86\x01\xdaA\x1aserving_config,update_mask\x82\xd3\xe4\x93\x02c2Q/v2alpha/{serving_config.name=projects/*/locations/*/catalogs/*/servingConfigs/*}:\x0eserving_config\x12\xc7\x01\n\x10GetServingConfig\x124.google.cloud.retail.v2alpha.GetServingConfigRequest\x1a*.google.cloud.retail.v2alpha.ServingConfig"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v2alpha/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}\x12\xda\x01\n\x12ListServingConfigs\x126.google.cloud.retail.v2alpha.ListServingConfigsRequest\x1a7.google.cloud.retail.v2alpha.ListServingConfigsResponse"S\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v2alpha/{parent=projects/*/locations/*/catalogs/*}/servingConfigs\x12\xdd\x01\n\nAddControl\x12..google.cloud.retail.v2alpha.AddControlRequest\x1a*.google.cloud.retail.v2alpha.ServingConfig"s\xdaA\x0eserving_config\x82\xd3\xe4\x93\x02\\"W/v2alpha/{serving_config=projects/*/locations/*/catalogs/*/servingConfigs/*}:addControl:\x01*\x12\xe6\x01\n\rRemoveControl\x121.google.cloud.retail.v2alpha.RemoveControlRequest\x1a*.google.cloud.retail.v2alpha.ServingConfig"v\xdaA\x0eserving_config\x82\xd3\xe4\x93\x02_"Z/v2alpha/{serving_config=projects/*/locations/*/catalogs/*/servingConfigs/*}:removeControl:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xdd\x01\n\x1fcom.google.cloud.retail.v2alphaB\x19ServingConfigServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.serving_config_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x19ServingConfigServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_CREATESERVINGCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESERVINGCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_CREATESERVINGCONFIGREQUEST'].fields_by_name['serving_config']._loaded_options = None
    _globals['_CREATESERVINGCONFIGREQUEST'].fields_by_name['serving_config']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESERVINGCONFIGREQUEST'].fields_by_name['serving_config_id']._loaded_options = None
    _globals['_CREATESERVINGCONFIGREQUEST'].fields_by_name['serving_config_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESERVINGCONFIGREQUEST'].fields_by_name['serving_config']._loaded_options = None
    _globals['_UPDATESERVINGCONFIGREQUEST'].fields_by_name['serving_config']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESERVINGCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESERVINGCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig'
    _globals['_GETSERVINGCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSERVINGCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig'
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_ADDCONTROLREQUEST'].fields_by_name['serving_config']._loaded_options = None
    _globals['_ADDCONTROLREQUEST'].fields_by_name['serving_config']._serialized_options = b'\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig'
    _globals['_ADDCONTROLREQUEST'].fields_by_name['control_id']._loaded_options = None
    _globals['_ADDCONTROLREQUEST'].fields_by_name['control_id']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVECONTROLREQUEST'].fields_by_name['serving_config']._loaded_options = None
    _globals['_REMOVECONTROLREQUEST'].fields_by_name['serving_config']._serialized_options = b'\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig'
    _globals['_REMOVECONTROLREQUEST'].fields_by_name['control_id']._loaded_options = None
    _globals['_REMOVECONTROLREQUEST'].fields_by_name['control_id']._serialized_options = b'\xe0A\x02'
    _globals['_SERVINGCONFIGSERVICE']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['CreateServingConfig']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['CreateServingConfig']._serialized_options = b'\xdaA\'parent,serving_config,serving_config_id\x82\xd3\xe4\x93\x02T"B/v2alpha/{parent=projects/*/locations/*/catalogs/*}/servingConfigs:\x0eserving_config'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['DeleteServingConfig']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['DeleteServingConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D*B/v2alpha/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['UpdateServingConfig']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['UpdateServingConfig']._serialized_options = b'\xdaA\x1aserving_config,update_mask\x82\xd3\xe4\x93\x02c2Q/v2alpha/{serving_config.name=projects/*/locations/*/catalogs/*/servingConfigs/*}:\x0eserving_config'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['GetServingConfig']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['GetServingConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v2alpha/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['ListServingConfigs']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['ListServingConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v2alpha/{parent=projects/*/locations/*/catalogs/*}/servingConfigs'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['AddControl']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['AddControl']._serialized_options = b'\xdaA\x0eserving_config\x82\xd3\xe4\x93\x02\\"W/v2alpha/{serving_config=projects/*/locations/*/catalogs/*/servingConfigs/*}:addControl:\x01*'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['RemoveControl']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['RemoveControl']._serialized_options = b'\xdaA\x0eserving_config\x82\xd3\xe4\x93\x02_"Z/v2alpha/{serving_config=projects/*/locations/*/catalogs/*/servingConfigs/*}:removeControl:\x01*'
    _globals['_CREATESERVINGCONFIGREQUEST']._serialized_start = 318
    _globals['_CREATESERVINGCONFIGREQUEST']._serialized_end = 506
    _globals['_UPDATESERVINGCONFIGREQUEST']._serialized_start = 509
    _globals['_UPDATESERVINGCONFIGREQUEST']._serialized_end = 659
    _globals['_DELETESERVINGCONFIGREQUEST']._serialized_start = 661
    _globals['_DELETESERVINGCONFIGREQUEST']._serialized_end = 748
    _globals['_GETSERVINGCONFIGREQUEST']._serialized_start = 750
    _globals['_GETSERVINGCONFIGREQUEST']._serialized_end = 834
    _globals['_LISTSERVINGCONFIGSREQUEST']._serialized_start = 837
    _globals['_LISTSERVINGCONFIGSREQUEST']._serialized_end = 968
    _globals['_LISTSERVINGCONFIGSRESPONSE']._serialized_start = 970
    _globals['_LISTSERVINGCONFIGSRESPONSE']._serialized_end = 1092
    _globals['_ADDCONTROLREQUEST']._serialized_start = 1094
    _globals['_ADDCONTROLREQUEST']._serialized_end = 1207
    _globals['_REMOVECONTROLREQUEST']._serialized_start = 1209
    _globals['_REMOVECONTROLREQUEST']._serialized_end = 1325
    _globals['_SERVINGCONFIGSERVICE']._serialized_start = 1328
    _globals['_SERVINGCONFIGSERVICE']._serialized_end = 3015