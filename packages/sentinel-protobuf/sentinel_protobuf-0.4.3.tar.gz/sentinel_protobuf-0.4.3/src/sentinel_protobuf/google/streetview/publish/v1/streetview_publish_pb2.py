"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/streetview/publish/v1/streetview_publish.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from .....google.streetview.publish.v1 import resources_pb2 as google_dot_streetview_dot_publish_dot_v1_dot_resources__pb2
from .....google.streetview.publish.v1 import rpcmessages_pb2 as google_dot_streetview_dot_publish_dot_v1_dot_rpcmessages__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/streetview/publish/v1/streetview_publish.proto\x12\x1cgoogle.streetview.publish.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a,google/streetview/publish/v1/resources.proto\x1a.google/streetview/publish/v1/rpcmessages.proto2\xce\x12\n\x18StreetViewPublishService\x12p\n\x0bStartUpload\x12\x16.google.protobuf.Empty\x1a\'.google.streetview.publish.v1.UploadRef" \x82\xd3\xe4\x93\x02\x1a"\x15/v1/photo:startUpload:\x01*\x12\x86\x01\n\x0bCreatePhoto\x120.google.streetview.publish.v1.CreatePhotoRequest\x1a#.google.streetview.publish.v1.Photo" \xdaA\x05photo\x82\xd3\xe4\x93\x02\x12"\t/v1/photo:\x05photo\x12\x8c\x01\n\x08GetPhoto\x12-.google.streetview.publish.v1.GetPhotoRequest\x1a#.google.streetview.publish.v1.Photo",\xdaA\rphoto_id,view\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/photo/{photo_id}\x12\xa9\x01\n\x0eBatchGetPhotos\x123.google.streetview.publish.v1.BatchGetPhotosRequest\x1a4.google.streetview.publish.v1.BatchGetPhotosResponse",\xdaA\x0eview,photo_ids\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/photos:batchGet\x12\x91\x01\n\nListPhotos\x12/.google.streetview.publish.v1.ListPhotosRequest\x1a0.google.streetview.publish.v1.ListPhotosResponse" \xdaA\x0bview,filter\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/photos\x12\xa6\x01\n\x0bUpdatePhoto\x120.google.streetview.publish.v1.UpdatePhotoRequest\x1a#.google.streetview.publish.v1.Photo"@\xdaA\x11photo,update_mask\x82\xd3\xe4\x93\x02&\x1a\x1d/v1/photo/{photo.photo_id.id}:\x05photo\x12\xbf\x01\n\x11BatchUpdatePhotos\x126.google.streetview.publish.v1.BatchUpdatePhotosRequest\x1a7.google.streetview.publish.v1.BatchUpdatePhotosResponse"9\xdaA\x15update_photo_requests\x82\xd3\xe4\x93\x02\x1b"\x16/v1/photos:batchUpdate:\x01*\x12\x80\x01\n\x0bDeletePhoto\x120.google.streetview.publish.v1.DeletePhotoRequest\x1a\x16.google.protobuf.Empty"\'\xdaA\x08photo_id\x82\xd3\xe4\x93\x02\x16*\x14/v1/photo/{photo_id}\x12\xb3\x01\n\x11BatchDeletePhotos\x126.google.streetview.publish.v1.BatchDeletePhotosRequest\x1a7.google.streetview.publish.v1.BatchDeletePhotosResponse"-\xdaA\tphoto_ids\x82\xd3\xe4\x93\x02\x1b"\x16/v1/photos:batchDelete:\x01*\x12\x85\x01\n\x18StartPhotoSequenceUpload\x12\x16.google.protobuf.Empty\x1a\'.google.streetview.publish.v1.UploadRef"(\x82\xd3\xe4\x93\x02""\x1d/v1/photoSequence:startUpload:\x01*\x12\xde\x01\n\x13CreatePhotoSequence\x128.google.streetview.publish.v1.CreatePhotoSequenceRequest\x1a\x1d.google.longrunning.Operation"n\xcaA&\n\rPhotoSequence\x12\x15google.protobuf.Empty\xdaA\x19photo_sequence,input_type\x82\xd3\xe4\x93\x02#"\x11/v1/photoSequence:\x0ephoto_sequence\x12\xba\x01\n\x10GetPhotoSequence\x125.google.streetview.publish.v1.GetPhotoSequenceRequest\x1a\x1d.google.longrunning.Operation"P\xcaA&\n\rPhotoSequence\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02!\x12\x1f/v1/photoSequence/{sequence_id}\x12\xa3\x01\n\x12ListPhotoSequences\x127.google.streetview.publish.v1.ListPhotoSequencesRequest\x1a8.google.streetview.publish.v1.ListPhotoSequencesResponse"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/photoSequences\x12\x9e\x01\n\x13DeletePhotoSequence\x128.google.streetview.publish.v1.DeletePhotoSequenceRequest\x1a\x16.google.protobuf.Empty"5\xdaA\x0bsequence_id\x82\xd3\xe4\x93\x02!*\x1f/v1/photoSequence/{sequence_id}\x1aW\xcaA streetviewpublish.googleapis.com\xd2A1https://www.googleapis.com/auth/streetviewpublishB\xc3\x01\n(com.google.geo.ugc.streetview.publish.v1B\x11StreetViewPublishZ@cloud.google.com/go/streetview/publish/apiv1/publishpb;publishpb\xeaAA\n)streetviewpublish.googleapis.com/Contract\x12\x14contracts/{contract}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.streetview.publish.v1.streetview_publish_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.geo.ugc.streetview.publish.v1B\x11StreetViewPublishZ@cloud.google.com/go/streetview/publish/apiv1/publishpb;publishpb\xeaAA\n)streetviewpublish.googleapis.com/Contract\x12\x14contracts/{contract}'
    _globals['_STREETVIEWPUBLISHSERVICE']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE']._serialized_options = b'\xcaA streetviewpublish.googleapis.com\xd2A1https://www.googleapis.com/auth/streetviewpublish'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['StartUpload']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['StartUpload']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a"\x15/v1/photo:startUpload:\x01*'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['CreatePhoto']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['CreatePhoto']._serialized_options = b'\xdaA\x05photo\x82\xd3\xe4\x93\x02\x12"\t/v1/photo:\x05photo'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['GetPhoto']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['GetPhoto']._serialized_options = b'\xdaA\rphoto_id,view\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/photo/{photo_id}'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['BatchGetPhotos']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['BatchGetPhotos']._serialized_options = b'\xdaA\x0eview,photo_ids\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/photos:batchGet'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['ListPhotos']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['ListPhotos']._serialized_options = b'\xdaA\x0bview,filter\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/photos'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['UpdatePhoto']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['UpdatePhoto']._serialized_options = b'\xdaA\x11photo,update_mask\x82\xd3\xe4\x93\x02&\x1a\x1d/v1/photo/{photo.photo_id.id}:\x05photo'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['BatchUpdatePhotos']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['BatchUpdatePhotos']._serialized_options = b'\xdaA\x15update_photo_requests\x82\xd3\xe4\x93\x02\x1b"\x16/v1/photos:batchUpdate:\x01*'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['DeletePhoto']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['DeletePhoto']._serialized_options = b'\xdaA\x08photo_id\x82\xd3\xe4\x93\x02\x16*\x14/v1/photo/{photo_id}'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['BatchDeletePhotos']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['BatchDeletePhotos']._serialized_options = b'\xdaA\tphoto_ids\x82\xd3\xe4\x93\x02\x1b"\x16/v1/photos:batchDelete:\x01*'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['StartPhotoSequenceUpload']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['StartPhotoSequenceUpload']._serialized_options = b'\x82\xd3\xe4\x93\x02""\x1d/v1/photoSequence:startUpload:\x01*'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['CreatePhotoSequence']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['CreatePhotoSequence']._serialized_options = b'\xcaA&\n\rPhotoSequence\x12\x15google.protobuf.Empty\xdaA\x19photo_sequence,input_type\x82\xd3\xe4\x93\x02#"\x11/v1/photoSequence:\x0ephoto_sequence'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['GetPhotoSequence']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['GetPhotoSequence']._serialized_options = b'\xcaA&\n\rPhotoSequence\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02!\x12\x1f/v1/photoSequence/{sequence_id}'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['ListPhotoSequences']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['ListPhotoSequences']._serialized_options = b'\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/photoSequences'
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['DeletePhotoSequence']._loaded_options = None
    _globals['_STREETVIEWPUBLISHSERVICE'].methods_by_name['DeletePhotoSequence']._serialized_options = b'\xdaA\x0bsequence_id\x82\xd3\xe4\x93\x02!*\x1f/v1/photoSequence/{sequence_id}'
    _globals['_STREETVIEWPUBLISHSERVICE']._serialized_start = 330
    _globals['_STREETVIEWPUBLISHSERVICE']._serialized_end = 2712