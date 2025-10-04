"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/apps/events/subscriptions/v1beta/subscription_resource.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/apps/events/subscriptions/v1beta/subscription_resource.proto\x12\'google.apps.events.subscriptions.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfd\n\n\x0cSubscription\x12`\n\rdrive_options\x18\x14 \x01(\x0b2B.google.apps.events.subscriptions.v1beta.Subscription.DriveOptionsB\x03\xe0A\x01H\x00\x126\n\x0bexpire_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x07H\x01\x12-\n\x03ttl\x18\x0e \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x04H\x01\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x03uid\x18\x02 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12%\n\x0ftarget_resource\x18\x04 \x01(\tB\x0c\xe0A\x05\xe0A\x02\xfaA\x03\n\x01*\x12\x1b\n\x0bevent_types\x18\x05 \x03(\tB\x06\xe0A\x02\xe0A\x06\x12U\n\x0fpayload_options\x18\x06 \x01(\x0b27.google.apps.events.subscriptions.v1beta.PayloadOptionsB\x03\xe0A\x01\x12d\n\x15notification_endpoint\x18\x07 \x01(\x0b2=.google.apps.events.subscriptions.v1beta.NotificationEndpointB\x06\xe0A\x02\xe0A\x05\x12O\n\x05state\x18\x08 \x01(\x0e2;.google.apps.events.subscriptions.v1beta.Subscription.StateB\x03\xe0A\x03\x12_\n\x11suspension_reason\x18\x12 \x01(\x0e2?.google.apps.events.subscriptions.v1beta.Subscription.ErrorTypeB\x03\xe0A\x03\x12<\n\tauthority\x18\n \x01(\tB)\xe0A\x03\xfaA#\n!cloudidentity.googleapis.com/User\x124\n\x0bcreate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0breconciling\x18\x0f \x01(\x08B\x03\xe0A\x03\x12\x11\n\x04etag\x18\x11 \x01(\tB\x03\xe0A\x01\x1a3\n\x0cDriveOptions\x12#\n\x13include_descendants\x18\x01 \x01(\x08B\x06\xe0A\x01\xe0A\x05"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\r\n\tSUSPENDED\x10\x02\x12\x0b\n\x07DELETED\x10\x03"\xd9\x01\n\tErrorType\x12\x1a\n\x16ERROR_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12USER_SCOPE_REVOKED\x10\x01\x12\x14\n\x10RESOURCE_DELETED\x10\x02\x12\x1e\n\x1aUSER_AUTHORIZATION_FAILURE\x10\x03\x12\x1e\n\x1aENDPOINT_PERMISSION_DENIED\x10\x04\x12\x16\n\x12ENDPOINT_NOT_FOUND\x10\x06\x12\x1f\n\x1bENDPOINT_RESOURCE_EXHAUSTED\x10\x07\x12\t\n\x05OTHER\x10\x05:n\xeaAk\n+workspaceevents.googleapis.com/Subscription\x12\x1csubscriptions/{subscription}*\rsubscriptions2\x0csubscriptionR\x01\x01B\x16\n\x14subscription_optionsB\x0c\n\nexpiration"d\n\x0ePayloadOptions\x12\x1d\n\x10include_resource\x18\x01 \x01(\x08B\x03\xe0A\x01\x123\n\nfield_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"_\n\x14NotificationEndpoint\x12;\n\x0cpubsub_topic\x18\x01 \x01(\tB#\xe0A\x05\xfaA\x1d\n\x1bpubsub.googleapis.com/TopicH\x00B\n\n\x08endpointB\x9c\x03\n+com.google.apps.events.subscriptions.v1betaB\x19SubscriptionResourceProtoP\x01ZWcloud.google.com/go/apps/events/subscriptions/apiv1beta/subscriptionspb;subscriptionspb\xaa\x02\'Google.Apps.Events.Subscriptions.V1Beta\xca\x02\'Google\\Apps\\Events\\Subscriptions\\V1beta\xea\x02+Google::Apps::Events::Subscriptions::V1beta\xeaA1\n!cloudidentity.googleapis.com/User\x12\x0cusers/{user}\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.events.subscriptions.v1beta.subscription_resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.apps.events.subscriptions.v1betaB\x19SubscriptionResourceProtoP\x01ZWcloud.google.com/go/apps/events/subscriptions/apiv1beta/subscriptionspb;subscriptionspb\xaa\x02'Google.Apps.Events.Subscriptions.V1Beta\xca\x02'Google\\Apps\\Events\\Subscriptions\\V1beta\xea\x02+Google::Apps::Events::Subscriptions::V1beta\xeaA1\n!cloudidentity.googleapis.com/User\x12\x0cusers/{user}\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}"
    _globals['_SUBSCRIPTION_DRIVEOPTIONS'].fields_by_name['include_descendants']._loaded_options = None
    _globals['_SUBSCRIPTION_DRIVEOPTIONS'].fields_by_name['include_descendants']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_SUBSCRIPTION'].fields_by_name['drive_options']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['drive_options']._serialized_options = b'\xe0A\x01'
    _globals['_SUBSCRIPTION'].fields_by_name['expire_time']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x07'
    _globals['_SUBSCRIPTION'].fields_by_name['ttl']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['ttl']._serialized_options = b'\xe0A\x04'
    _globals['_SUBSCRIPTION'].fields_by_name['name']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SUBSCRIPTION'].fields_by_name['uid']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_SUBSCRIPTION'].fields_by_name['target_resource']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['target_resource']._serialized_options = b'\xe0A\x05\xe0A\x02\xfaA\x03\n\x01*'
    _globals['_SUBSCRIPTION'].fields_by_name['event_types']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['event_types']._serialized_options = b'\xe0A\x02\xe0A\x06'
    _globals['_SUBSCRIPTION'].fields_by_name['payload_options']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['payload_options']._serialized_options = b'\xe0A\x01'
    _globals['_SUBSCRIPTION'].fields_by_name['notification_endpoint']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['notification_endpoint']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_SUBSCRIPTION'].fields_by_name['state']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_SUBSCRIPTION'].fields_by_name['suspension_reason']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['suspension_reason']._serialized_options = b'\xe0A\x03'
    _globals['_SUBSCRIPTION'].fields_by_name['authority']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['authority']._serialized_options = b'\xe0A\x03\xfaA#\n!cloudidentity.googleapis.com/User'
    _globals['_SUBSCRIPTION'].fields_by_name['create_time']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SUBSCRIPTION'].fields_by_name['update_time']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SUBSCRIPTION'].fields_by_name['reconciling']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['reconciling']._serialized_options = b'\xe0A\x03'
    _globals['_SUBSCRIPTION'].fields_by_name['etag']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_SUBSCRIPTION']._loaded_options = None
    _globals['_SUBSCRIPTION']._serialized_options = b'\xeaAk\n+workspaceevents.googleapis.com/Subscription\x12\x1csubscriptions/{subscription}*\rsubscriptions2\x0csubscriptionR\x01\x01'
    _globals['_PAYLOADOPTIONS'].fields_by_name['include_resource']._loaded_options = None
    _globals['_PAYLOADOPTIONS'].fields_by_name['include_resource']._serialized_options = b'\xe0A\x01'
    _globals['_PAYLOADOPTIONS'].fields_by_name['field_mask']._loaded_options = None
    _globals['_PAYLOADOPTIONS'].fields_by_name['field_mask']._serialized_options = b'\xe0A\x01'
    _globals['_NOTIFICATIONENDPOINT'].fields_by_name['pubsub_topic']._loaded_options = None
    _globals['_NOTIFICATIONENDPOINT'].fields_by_name['pubsub_topic']._serialized_options = b'\xe0A\x05\xfaA\x1d\n\x1bpubsub.googleapis.com/Topic'
    _globals['_SUBSCRIPTION']._serialized_start = 301
    _globals['_SUBSCRIPTION']._serialized_end = 1706
    _globals['_SUBSCRIPTION_DRIVEOPTIONS']._serialized_start = 1213
    _globals['_SUBSCRIPTION_DRIVEOPTIONS']._serialized_end = 1264
    _globals['_SUBSCRIPTION_STATE']._serialized_start = 1266
    _globals['_SUBSCRIPTION_STATE']._serialized_end = 1336
    _globals['_SUBSCRIPTION_ERRORTYPE']._serialized_start = 1339
    _globals['_SUBSCRIPTION_ERRORTYPE']._serialized_end = 1556
    _globals['_PAYLOADOPTIONS']._serialized_start = 1708
    _globals['_PAYLOADOPTIONS']._serialized_end = 1808
    _globals['_NOTIFICATIONENDPOINT']._serialized_start = 1810
    _globals['_NOTIFICATIONENDPOINT']._serialized_end = 1905