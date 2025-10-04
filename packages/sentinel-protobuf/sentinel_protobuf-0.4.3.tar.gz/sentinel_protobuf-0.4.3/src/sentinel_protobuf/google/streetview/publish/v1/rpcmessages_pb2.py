"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/streetview/publish/v1/rpcmessages.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.streetview.publish.v1 import resources_pb2 as google_dot_streetview_dot_publish_dot_v1_dot_resources__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/streetview/publish/v1/rpcmessages.proto\x12\x1cgoogle.streetview.publish.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\x1a,google/streetview/publish/v1/resources.proto"M\n\x12CreatePhotoRequest\x127\n\x05photo\x18\x01 \x01(\x0b2#.google.streetview.publish.v1.PhotoB\x03\xe0A\x02"{\n\x0fGetPhotoRequest\x12\x15\n\x08photo_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12:\n\x04view\x18\x02 \x01(\x0e2\'.google.streetview.publish.v1.PhotoViewB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"\x87\x01\n\x15BatchGetPhotosRequest\x12\x16\n\tphoto_ids\x18\x01 \x03(\tB\x03\xe0A\x02\x12:\n\x04view\x18\x02 \x01(\x0e2\'.google.streetview.publish.v1.PhotoViewB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x01"V\n\x16BatchGetPhotosResponse\x12<\n\x07results\x18\x01 \x03(\x0b2+.google.streetview.publish.v1.PhotoResponse"g\n\rPhotoResponse\x12"\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x122\n\x05photo\x18\x02 \x01(\x0b2#.google.streetview.publish.v1.Photo"\xb1\x01\n\x11ListPhotosRequest\x12:\n\x04view\x18\x01 \x01(\x0e2\'.google.streetview.publish.v1.PhotoViewB\x03\xe0A\x02\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18\x05 \x01(\tB\x03\xe0A\x01"b\n\x12ListPhotosResponse\x123\n\x06photos\x18\x01 \x03(\x0b2#.google.streetview.publish.v1.Photo\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x83\x01\n\x12UpdatePhotoRequest\x127\n\x05photo\x18\x01 \x01(\x0b2#.google.streetview.publish.v1.PhotoB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"p\n\x18BatchUpdatePhotosRequest\x12T\n\x15update_photo_requests\x18\x01 \x03(\x0b20.google.streetview.publish.v1.UpdatePhotoRequestB\x03\xe0A\x02"Y\n\x19BatchUpdatePhotosResponse\x12<\n\x07results\x18\x01 \x03(\x0b2+.google.streetview.publish.v1.PhotoResponse"+\n\x12DeletePhotoRequest\x12\x15\n\x08photo_id\x18\x01 \x01(\tB\x03\xe0A\x02"2\n\x18BatchDeletePhotosRequest\x12\x16\n\tphoto_ids\x18\x01 \x03(\tB\x03\xe0A\x02"\x80\x02\n\x1aCreatePhotoSequenceRequest\x12H\n\x0ephoto_sequence\x18\x01 \x01(\x0b2+.google.streetview.publish.v1.PhotoSequenceB\x03\xe0A\x02\x12[\n\ninput_type\x18\x02 \x01(\x0e2B.google.streetview.publish.v1.CreatePhotoSequenceRequest.InputTypeB\x03\xe0A\x02";\n\tInputType\x12\x1a\n\x16INPUT_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05VIDEO\x10\x01\x12\x07\n\x03XDM\x10\x02"\x83\x01\n\x17GetPhotoSequenceRequest\x12\x18\n\x0bsequence_id\x18\x01 \x01(\tB\x03\xe0A\x02\x129\n\x04view\x18\x02 \x01(\x0e2\'.google.streetview.publish.v1.PhotoViewB\x02\x18\x01\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x01"6\n\x1aDeletePhotoSequenceRequest\x12\x18\n\x0bsequence_id\x18\x01 \x01(\tB\x03\xe0A\x02"?\n\x19BatchDeletePhotosResponse\x12"\n\x06status\x18\x01 \x03(\x0b2\x12.google.rpc.Status"a\n\x19ListPhotoSequencesRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"m\n\x1aListPhotoSequencesResponse\x126\n\x0fphoto_sequences\x18\x01 \x03(\x0b2\x1d.google.longrunning.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*0\n\tPhotoView\x12\t\n\x05BASIC\x10\x00\x12\x18\n\x14INCLUDE_DOWNLOAD_URL\x10\x01B\x8a\x01\n(com.google.geo.ugc.streetview.publish.v1B\x1cStreetViewPublishRpcMessagesZ@cloud.google.com/go/streetview/publish/apiv1/publishpb;publishpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.streetview.publish.v1.rpcmessages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.geo.ugc.streetview.publish.v1B\x1cStreetViewPublishRpcMessagesZ@cloud.google.com/go/streetview/publish/apiv1/publishpb;publishpb'
    _globals['_CREATEPHOTOREQUEST'].fields_by_name['photo']._loaded_options = None
    _globals['_CREATEPHOTOREQUEST'].fields_by_name['photo']._serialized_options = b'\xe0A\x02'
    _globals['_GETPHOTOREQUEST'].fields_by_name['photo_id']._loaded_options = None
    _globals['_GETPHOTOREQUEST'].fields_by_name['photo_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETPHOTOREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_GETPHOTOREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHGETPHOTOSREQUEST'].fields_by_name['photo_ids']._loaded_options = None
    _globals['_BATCHGETPHOTOSREQUEST'].fields_by_name['photo_ids']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHGETPHOTOSREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_BATCHGETPHOTOSREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHGETPHOTOSREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_BATCHGETPHOTOSREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPHOTOSREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_LISTPHOTOSREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPHOTOSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPHOTOSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPHOTOSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPHOTOSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPHOTOSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTPHOTOSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPHOTOSREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_LISTPHOTOSREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEPHOTOREQUEST'].fields_by_name['photo']._loaded_options = None
    _globals['_UPDATEPHOTOREQUEST'].fields_by_name['photo']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPHOTOREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPHOTOREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHUPDATEPHOTOSREQUEST'].fields_by_name['update_photo_requests']._loaded_options = None
    _globals['_BATCHUPDATEPHOTOSREQUEST'].fields_by_name['update_photo_requests']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPHOTOREQUEST'].fields_by_name['photo_id']._loaded_options = None
    _globals['_DELETEPHOTOREQUEST'].fields_by_name['photo_id']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHDELETEPHOTOSREQUEST'].fields_by_name['photo_ids']._loaded_options = None
    _globals['_BATCHDELETEPHOTOSREQUEST'].fields_by_name['photo_ids']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPHOTOSEQUENCEREQUEST'].fields_by_name['photo_sequence']._loaded_options = None
    _globals['_CREATEPHOTOSEQUENCEREQUEST'].fields_by_name['photo_sequence']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPHOTOSEQUENCEREQUEST'].fields_by_name['input_type']._loaded_options = None
    _globals['_CREATEPHOTOSEQUENCEREQUEST'].fields_by_name['input_type']._serialized_options = b'\xe0A\x02'
    _globals['_GETPHOTOSEQUENCEREQUEST'].fields_by_name['sequence_id']._loaded_options = None
    _globals['_GETPHOTOSEQUENCEREQUEST'].fields_by_name['sequence_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETPHOTOSEQUENCEREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_GETPHOTOSEQUENCEREQUEST'].fields_by_name['view']._serialized_options = b'\x18\x01'
    _globals['_GETPHOTOSEQUENCEREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_GETPHOTOSEQUENCEREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPHOTOSEQUENCEREQUEST'].fields_by_name['sequence_id']._loaded_options = None
    _globals['_DELETEPHOTOSEQUENCEREQUEST'].fields_by_name['sequence_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPHOTOSEQUENCESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPHOTOSEQUENCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPHOTOSEQUENCESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPHOTOSEQUENCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPHOTOSEQUENCESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTPHOTOSEQUENCESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_PHOTOVIEW']._serialized_start = 2257
    _globals['_PHOTOVIEW']._serialized_end = 2305
    _globals['_CREATEPHOTOREQUEST']._serialized_start = 282
    _globals['_CREATEPHOTOREQUEST']._serialized_end = 359
    _globals['_GETPHOTOREQUEST']._serialized_start = 361
    _globals['_GETPHOTOREQUEST']._serialized_end = 484
    _globals['_BATCHGETPHOTOSREQUEST']._serialized_start = 487
    _globals['_BATCHGETPHOTOSREQUEST']._serialized_end = 622
    _globals['_BATCHGETPHOTOSRESPONSE']._serialized_start = 624
    _globals['_BATCHGETPHOTOSRESPONSE']._serialized_end = 710
    _globals['_PHOTORESPONSE']._serialized_start = 712
    _globals['_PHOTORESPONSE']._serialized_end = 815
    _globals['_LISTPHOTOSREQUEST']._serialized_start = 818
    _globals['_LISTPHOTOSREQUEST']._serialized_end = 995
    _globals['_LISTPHOTOSRESPONSE']._serialized_start = 997
    _globals['_LISTPHOTOSRESPONSE']._serialized_end = 1095
    _globals['_UPDATEPHOTOREQUEST']._serialized_start = 1098
    _globals['_UPDATEPHOTOREQUEST']._serialized_end = 1229
    _globals['_BATCHUPDATEPHOTOSREQUEST']._serialized_start = 1231
    _globals['_BATCHUPDATEPHOTOSREQUEST']._serialized_end = 1343
    _globals['_BATCHUPDATEPHOTOSRESPONSE']._serialized_start = 1345
    _globals['_BATCHUPDATEPHOTOSRESPONSE']._serialized_end = 1434
    _globals['_DELETEPHOTOREQUEST']._serialized_start = 1436
    _globals['_DELETEPHOTOREQUEST']._serialized_end = 1479
    _globals['_BATCHDELETEPHOTOSREQUEST']._serialized_start = 1481
    _globals['_BATCHDELETEPHOTOSREQUEST']._serialized_end = 1531
    _globals['_CREATEPHOTOSEQUENCEREQUEST']._serialized_start = 1534
    _globals['_CREATEPHOTOSEQUENCEREQUEST']._serialized_end = 1790
    _globals['_CREATEPHOTOSEQUENCEREQUEST_INPUTTYPE']._serialized_start = 1731
    _globals['_CREATEPHOTOSEQUENCEREQUEST_INPUTTYPE']._serialized_end = 1790
    _globals['_GETPHOTOSEQUENCEREQUEST']._serialized_start = 1793
    _globals['_GETPHOTOSEQUENCEREQUEST']._serialized_end = 1924
    _globals['_DELETEPHOTOSEQUENCEREQUEST']._serialized_start = 1926
    _globals['_DELETEPHOTOSEQUENCEREQUEST']._serialized_end = 1980
    _globals['_BATCHDELETEPHOTOSRESPONSE']._serialized_start = 1982
    _globals['_BATCHDELETEPHOTOSRESPONSE']._serialized_end = 2045
    _globals['_LISTPHOTOSEQUENCESREQUEST']._serialized_start = 2047
    _globals['_LISTPHOTOSEQUENCESREQUEST']._serialized_end = 2144
    _globals['_LISTPHOTOSEQUENCESRESPONSE']._serialized_start = 2146
    _globals['_LISTPHOTOSEQUENCESRESPONSE']._serialized_end = 2255