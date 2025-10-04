"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/streetview/publish/v1/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/streetview/publish/v1/resources.proto\x12\x1cgoogle.streetview.publish.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18google/type/latlng.proto"0\n\tUploadRef\x12\x14\n\nupload_url\x18\x01 \x01(\tH\x00B\r\n\x0bfile_source"\x15\n\x07PhotoId\x12\n\n\x02id\x18\x01 \x01(\t"/\n\x05Level\x12\x13\n\x06number\x18\x01 \x01(\x01B\x03\xe0A\x01\x12\x11\n\x04name\x18\x02 \x01(\tB\x03\xe0A\x02"\x83\x02\n\x04Pose\x12)\n\x0clat_lng_pair\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12\x10\n\x08altitude\x18\x02 \x01(\x01\x12\x0f\n\x07heading\x18\x03 \x01(\x01\x12\r\n\x05pitch\x18\x04 \x01(\x01\x12\x0c\n\x04roll\x18\x05 \x01(\x01\x12C\n\x1fgps_record_timestamp_unix_epoch\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x122\n\x05level\x18\x07 \x01(\x0b2#.google.streetview.publish.v1.Level\x12\x17\n\x0faccuracy_meters\x18\t \x01(\x02"\xb3\x02\n\x03Imu\x12D\n\x0baccel_mpsps\x18\x01 \x03(\x0b2/.google.streetview.publish.v1.Imu.Measurement3d\x12A\n\x08gyro_rps\x18\x02 \x03(\x0b2/.google.streetview.publish.v1.Imu.Measurement3d\x12?\n\x06mag_ut\x18\x03 \x03(\x0b2/.google.streetview.publish.v1.Imu.Measurement3d\x1ab\n\rMeasurement3d\x120\n\x0ccapture_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\t\n\x01z\x18\x04 \x01(\x02"H\n\x05Place\x12\x10\n\x08place_id\x18\x01 \x01(\t\x12\x11\n\x04name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x03"H\n\nConnection\x12:\n\x06target\x18\x01 \x01(\x0b2%.google.streetview.publish.v1.PhotoIdB\x03\xe0A\x02"\xcd\x07\n\x05Photo\x12?\n\x08photo_id\x18\x01 \x01(\x0b2%.google.streetview.publish.v1.PhotoIdB\x06\xe0A\x02\xe0A\x03\x12F\n\x10upload_reference\x18\x02 \x01(\x0b2\'.google.streetview.publish.v1.UploadRefB\x03\xe0A\x04\x12\x19\n\x0cdownload_url\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rthumbnail_url\x18\t \x01(\tB\x03\xe0A\x03\x12\x17\n\nshare_link\x18\x0b \x01(\tB\x03\xe0A\x03\x125\n\x04pose\x18\x04 \x01(\x0b2".google.streetview.publish.v1.PoseB\x03\xe0A\x01\x12B\n\x0bconnections\x18\x05 \x03(\x0b2(.google.streetview.publish.v1.ConnectionB\x03\xe0A\x01\x125\n\x0ccapture_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x124\n\x0bupload_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x128\n\x06places\x18\x07 \x03(\x0b2#.google.streetview.publish.v1.PlaceB\x03\xe0A\x01\x12\x17\n\nview_count\x18\n \x01(\x03B\x03\xe0A\x03\x12P\n\x0ftransfer_status\x18\x0c \x01(\x0e22.google.streetview.publish.v1.Photo.TransferStatusB\x03\xe0A\x03\x12W\n\x13maps_publish_status\x18\r \x01(\x0e25.google.streetview.publish.v1.Photo.MapsPublishStatusB\x03\xe0A\x03"\xa5\x01\n\x0eTransferStatus\x12\x1b\n\x17TRANSFER_STATUS_UNKNOWN\x10\x00\x12\x15\n\x11NEVER_TRANSFERRED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\r\n\tCOMPLETED\x10\x03\x12\x0c\n\x08REJECTED\x10\x04\x12\x0b\n\x07EXPIRED\x10\x05\x12\r\n\tCANCELLED\x10\x06\x12\x19\n\x15RECEIVED_VIA_TRANSFER\x10\x07"]\n\x11MapsPublishStatus\x12#\n\x1fUNSPECIFIED_MAPS_PUBLISH_STATUS\x10\x00\x12\r\n\tPUBLISHED\x10\x01\x12\x14\n\x10REJECTED_UNKNOWN\x10\x02"\xb3\x07\n\rPhotoSequence\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x03\x128\n\x06photos\x18\x02 \x03(\x0b2#.google.streetview.publish.v1.PhotoB\x03\xe0A\x03\x12F\n\x10upload_reference\x18\x03 \x01(\x0b2\'.google.streetview.publish.v1.UploadRefB\x03\xe0A\x04\x12>\n\x15capture_time_override\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x124\n\x0bupload_time\x18\x12 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12A\n\x10raw_gps_timeline\x18\x07 \x03(\x0b2".google.streetview.publish.v1.PoseB\x03\xe0A\x04\x12N\n\ngps_source\x18\x08 \x01(\x0e25.google.streetview.publish.v1.PhotoSequence.GpsSourceB\x03\xe0A\x04\x123\n\x03imu\x18\x0b \x01(\x0b2!.google.streetview.publish.v1.ImuB\x03\xe0A\x04\x12L\n\x10processing_state\x18\x0c \x01(\x0e2-.google.streetview.publish.v1.ProcessingStateB\x03\xe0A\x03\x12R\n\x0efailure_reason\x18\r \x01(\x0e25.google.streetview.publish.v1.ProcessingFailureReasonB\x03\xe0A\x03\x12T\n\x0ffailure_details\x18\x17 \x01(\x0b26.google.streetview.publish.v1.ProcessingFailureDetailsB\x03\xe0A\x03\x12\x1c\n\x0fdistance_meters\x18\x10 \x01(\x01B\x03\xe0A\x03\x12H\n\x0fsequence_bounds\x18\x14 \x01(\x0b2*.google.streetview.publish.v1.LatLngBoundsB\x03\xe0A\x03\x12\x17\n\nview_count\x18\x15 \x01(\x03B\x03\xe0A\x03\x12\x15\n\x08filename\x18\x16 \x01(\tB\x03\xe0A\x03"A\n\tGpsSource\x12\x12\n\x0ePHOTO_SEQUENCE\x10\x00\x12 \n\x1cCAMERA_MOTION_METADATA_TRACK\x10\x01"^\n\x0cLatLngBounds\x12&\n\tsouthwest\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12&\n\tnortheast\x18\x02 \x01(\x0b2\x13.google.type.LatLng"\xeb\x03\n\x18ProcessingFailureDetails\x12_\n\x18insufficient_gps_details\x18\x01 \x01(\x0b2;.google.streetview.publish.v1.InsufficientGpsFailureDetailsH\x00\x12V\n\x14gps_data_gap_details\x18\x02 \x01(\x0b26.google.streetview.publish.v1.GpsDataGapFailureDetailsH\x00\x12V\n\x14imu_data_gap_details\x18\x03 \x01(\x0b26.google.streetview.publish.v1.ImuDataGapFailureDetailsH\x00\x12W\n\x14not_outdoors_details\x18\x04 \x01(\x0b27.google.streetview.publish.v1.NotOutdoorsFailureDetailsH\x00\x12Z\n\x16no_overlap_gps_details\x18\x05 \x01(\x0b28.google.streetview.publish.v1.NoOverlapGpsFailureDetailsH\x00B\t\n\x07details"S\n\x1dInsufficientGpsFailureDetails\x12\x1d\n\x10gps_points_found\x18\x01 \x01(\x05H\x00\x88\x01\x01B\x13\n\x11_gps_points_found"\xac\x01\n\x18GpsDataGapFailureDetails\x124\n\x0cgap_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x88\x01\x01\x126\n\x0egap_start_time\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationH\x01\x88\x01\x01B\x0f\n\r_gap_durationB\x11\n\x0f_gap_start_time"\xac\x01\n\x18ImuDataGapFailureDetails\x124\n\x0cgap_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x88\x01\x01\x126\n\x0egap_start_time\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationH\x01\x88\x01\x01B\x0f\n\r_gap_durationB\x11\n\x0f_gap_start_time"^\n\x19NotOutdoorsFailureDetails\x122\n\nstart_time\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationH\x00\x88\x01\x01B\r\n\x0b_start_time"\xcc\x02\n\x1aNoOverlapGpsFailureDetails\x127\n\x0egps_start_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x125\n\x0cgps_end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x129\n\x10video_start_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampH\x02\x88\x01\x01\x127\n\x0evideo_end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampH\x03\x88\x01\x01B\x11\n\x0f_gps_start_timeB\x0f\n\r_gps_end_timeB\x13\n\x11_video_start_timeB\x11\n\x0f_video_end_time*k\n\x0fProcessingState\x12 \n\x1cPROCESSING_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\r\n\tPROCESSED\x10\x03\x12\n\n\x06FAILED\x10\x04*\xca\x04\n\x17ProcessingFailureReason\x12)\n%PROCESSING_FAILURE_REASON_UNSPECIFIED\x10\x00\x12\x12\n\x0eLOW_RESOLUTION\x10\x01\x12\r\n\tDUPLICATE\x10\x02\x12\x14\n\x10INSUFFICIENT_GPS\x10\x03\x12\x12\n\x0eNO_OVERLAP_GPS\x10\x04\x12\x0f\n\x0bINVALID_GPS\x10\x05\x12\x1e\n\x1aFAILED_TO_REFINE_POSITIONS\x10\x06\x12\x0c\n\x08TAKEDOWN\x10\x07\x12\x11\n\rCORRUPT_VIDEO\x10\x08\x12\x0c\n\x08INTERNAL\x10\t\x12\x18\n\x14INVALID_VIDEO_FORMAT\x10\n\x12\x1c\n\x18INVALID_VIDEO_DIMENSIONS\x10\x0b\x12\x18\n\x14INVALID_CAPTURE_TIME\x10\x0c\x12\x10\n\x0cGPS_DATA_GAP\x10\r\x12\r\n\tJUMPY_GPS\x10\x0e\x12\x0f\n\x0bINVALID_IMU\x10\x0f\x12\x14\n\x10INSUFFICIENT_IMU\x10\x15\x12$\n INSUFFICIENT_OVERLAP_TIME_SERIES\x10\x16\x12\x10\n\x0cIMU_DATA_GAP\x10\x10\x12\x16\n\x12UNSUPPORTED_CAMERA\x10\x11\x12\x10\n\x0cNOT_OUTDOORS\x10\x12\x12\x1d\n\x19INSUFFICIENT_VIDEO_FRAMES\x10\x13\x12\x19\n\x15INSUFFICIENT_MOVEMENT\x10\x14\x12\r\n\tMAST_DOWN\x10\x1b\x12\x12\n\x0eCAMERA_COVERED\x10\x1cB\x88\x01\n(com.google.geo.ugc.streetview.publish.v1B\x1aStreetViewPublishResourcesZ@cloud.google.com/go/streetview/publish/apiv1/publishpb;publishpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.streetview.publish.v1.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.geo.ugc.streetview.publish.v1B\x1aStreetViewPublishResourcesZ@cloud.google.com/go/streetview/publish/apiv1/publishpb;publishpb'
    _globals['_LEVEL'].fields_by_name['number']._loaded_options = None
    _globals['_LEVEL'].fields_by_name['number']._serialized_options = b'\xe0A\x01'
    _globals['_LEVEL'].fields_by_name['name']._loaded_options = None
    _globals['_LEVEL'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_PLACE'].fields_by_name['name']._loaded_options = None
    _globals['_PLACE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PLACE'].fields_by_name['language_code']._loaded_options = None
    _globals['_PLACE'].fields_by_name['language_code']._serialized_options = b'\xe0A\x03'
    _globals['_CONNECTION'].fields_by_name['target']._loaded_options = None
    _globals['_CONNECTION'].fields_by_name['target']._serialized_options = b'\xe0A\x02'
    _globals['_PHOTO'].fields_by_name['photo_id']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['photo_id']._serialized_options = b'\xe0A\x02\xe0A\x03'
    _globals['_PHOTO'].fields_by_name['upload_reference']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['upload_reference']._serialized_options = b'\xe0A\x04'
    _globals['_PHOTO'].fields_by_name['download_url']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['download_url']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTO'].fields_by_name['thumbnail_url']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['thumbnail_url']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTO'].fields_by_name['share_link']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['share_link']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTO'].fields_by_name['pose']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['pose']._serialized_options = b'\xe0A\x01'
    _globals['_PHOTO'].fields_by_name['connections']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['connections']._serialized_options = b'\xe0A\x01'
    _globals['_PHOTO'].fields_by_name['capture_time']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['capture_time']._serialized_options = b'\xe0A\x01'
    _globals['_PHOTO'].fields_by_name['upload_time']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['upload_time']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTO'].fields_by_name['places']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['places']._serialized_options = b'\xe0A\x01'
    _globals['_PHOTO'].fields_by_name['view_count']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['view_count']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTO'].fields_by_name['transfer_status']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['transfer_status']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTO'].fields_by_name['maps_publish_status']._loaded_options = None
    _globals['_PHOTO'].fields_by_name['maps_publish_status']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTOSEQUENCE'].fields_by_name['id']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTOSEQUENCE'].fields_by_name['photos']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['photos']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTOSEQUENCE'].fields_by_name['upload_reference']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['upload_reference']._serialized_options = b'\xe0A\x04'
    _globals['_PHOTOSEQUENCE'].fields_by_name['capture_time_override']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['capture_time_override']._serialized_options = b'\xe0A\x01'
    _globals['_PHOTOSEQUENCE'].fields_by_name['upload_time']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['upload_time']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTOSEQUENCE'].fields_by_name['raw_gps_timeline']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['raw_gps_timeline']._serialized_options = b'\xe0A\x04'
    _globals['_PHOTOSEQUENCE'].fields_by_name['gps_source']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['gps_source']._serialized_options = b'\xe0A\x04'
    _globals['_PHOTOSEQUENCE'].fields_by_name['imu']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['imu']._serialized_options = b'\xe0A\x04'
    _globals['_PHOTOSEQUENCE'].fields_by_name['processing_state']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['processing_state']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTOSEQUENCE'].fields_by_name['failure_reason']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['failure_reason']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTOSEQUENCE'].fields_by_name['failure_details']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['failure_details']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTOSEQUENCE'].fields_by_name['distance_meters']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['distance_meters']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTOSEQUENCE'].fields_by_name['sequence_bounds']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['sequence_bounds']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTOSEQUENCE'].fields_by_name['view_count']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['view_count']._serialized_options = b'\xe0A\x03'
    _globals['_PHOTOSEQUENCE'].fields_by_name['filename']._loaded_options = None
    _globals['_PHOTOSEQUENCE'].fields_by_name['filename']._serialized_options = b'\xe0A\x03'
    _globals['_PROCESSINGSTATE']._serialized_start = 4453
    _globals['_PROCESSINGSTATE']._serialized_end = 4560
    _globals['_PROCESSINGFAILUREREASON']._serialized_start = 4563
    _globals['_PROCESSINGFAILUREREASON']._serialized_end = 5149
    _globals['_UPLOADREF']._serialized_start = 229
    _globals['_UPLOADREF']._serialized_end = 277
    _globals['_PHOTOID']._serialized_start = 279
    _globals['_PHOTOID']._serialized_end = 300
    _globals['_LEVEL']._serialized_start = 302
    _globals['_LEVEL']._serialized_end = 349
    _globals['_POSE']._serialized_start = 352
    _globals['_POSE']._serialized_end = 611
    _globals['_IMU']._serialized_start = 614
    _globals['_IMU']._serialized_end = 921
    _globals['_IMU_MEASUREMENT3D']._serialized_start = 823
    _globals['_IMU_MEASUREMENT3D']._serialized_end = 921
    _globals['_PLACE']._serialized_start = 923
    _globals['_PLACE']._serialized_end = 995
    _globals['_CONNECTION']._serialized_start = 997
    _globals['_CONNECTION']._serialized_end = 1069
    _globals['_PHOTO']._serialized_start = 1072
    _globals['_PHOTO']._serialized_end = 2045
    _globals['_PHOTO_TRANSFERSTATUS']._serialized_start = 1785
    _globals['_PHOTO_TRANSFERSTATUS']._serialized_end = 1950
    _globals['_PHOTO_MAPSPUBLISHSTATUS']._serialized_start = 1952
    _globals['_PHOTO_MAPSPUBLISHSTATUS']._serialized_end = 2045
    _globals['_PHOTOSEQUENCE']._serialized_start = 2048
    _globals['_PHOTOSEQUENCE']._serialized_end = 2995
    _globals['_PHOTOSEQUENCE_GPSSOURCE']._serialized_start = 2930
    _globals['_PHOTOSEQUENCE_GPSSOURCE']._serialized_end = 2995
    _globals['_LATLNGBOUNDS']._serialized_start = 2997
    _globals['_LATLNGBOUNDS']._serialized_end = 3091
    _globals['_PROCESSINGFAILUREDETAILS']._serialized_start = 3094
    _globals['_PROCESSINGFAILUREDETAILS']._serialized_end = 3585
    _globals['_INSUFFICIENTGPSFAILUREDETAILS']._serialized_start = 3587
    _globals['_INSUFFICIENTGPSFAILUREDETAILS']._serialized_end = 3670
    _globals['_GPSDATAGAPFAILUREDETAILS']._serialized_start = 3673
    _globals['_GPSDATAGAPFAILUREDETAILS']._serialized_end = 3845
    _globals['_IMUDATAGAPFAILUREDETAILS']._serialized_start = 3848
    _globals['_IMUDATAGAPFAILUREDETAILS']._serialized_end = 4020
    _globals['_NOTOUTDOORSFAILUREDETAILS']._serialized_start = 4022
    _globals['_NOTOUTDOORSFAILUREDETAILS']._serialized_end = 4116
    _globals['_NOOVERLAPGPSFAILUREDETAILS']._serialized_start = 4119
    _globals['_NOOVERLAPGPSFAILUREDETAILS']._serialized_end = 4451