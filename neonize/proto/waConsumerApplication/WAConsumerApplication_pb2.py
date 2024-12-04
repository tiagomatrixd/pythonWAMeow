# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: waConsumerApplication/WAConsumerApplication.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'waConsumerApplication/WAConsumerApplication.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from waCommon import WACommon_pb2 as waCommon_dot_WACommon__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1waConsumerApplication/WAConsumerApplication.proto\x12\x15WAConsumerApplication\x1a\x17waCommon/WACommon.proto\"\xca,\n\x13\x43onsumerApplication\x12\x43\n\x07payload\x18\x01 \x01(\x0b\x32\x32.WAConsumerApplication.ConsumerApplication.Payload\x12\x45\n\x08metadata\x18\x02 \x01(\x0b\x32\x33.WAConsumerApplication.ConsumerApplication.Metadata\x1a\xcd\x02\n\x07Payload\x12\x45\n\x07\x63ontent\x18\x01 \x01(\x0b\x32\x32.WAConsumerApplication.ConsumerApplication.ContentH\x00\x12U\n\x0f\x61pplicationData\x18\x02 \x01(\x0b\x32:.WAConsumerApplication.ConsumerApplication.ApplicationDataH\x00\x12\x43\n\x06signal\x18\x03 \x01(\x0b\x32\x31.WAConsumerApplication.ConsumerApplication.SignalH\x00\x12T\n\x0bsubProtocol\x18\x04 \x01(\x0b\x32=.WAConsumerApplication.ConsumerApplication.SubProtocolPayloadH\x00\x42\t\n\x07payload\x1aH\n\x12SubProtocolPayload\x12\x32\n\x0b\x66utureProof\x18\x01 \x01(\x0e\x32\x1d.WACommon.FutureProofBehavior\x1a\x9d\x01\n\x08Metadata\x12\\\n\x0fspecialTextSize\x18\x01 \x01(\x0e\x32\x43.WAConsumerApplication.ConsumerApplication.Metadata.SpecialTextSize\"3\n\x0fSpecialTextSize\x12\t\n\x05SMALL\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\t\n\x05LARGE\x10\x03\x1a\x08\n\x06Signal\x1as\n\x0f\x41pplicationData\x12J\n\x06revoke\x18\x01 \x01(\x0b\x32\x38.WAConsumerApplication.ConsumerApplication.RevokeMessageH\x00\x42\x14\n\x12\x61pplicationContent\x1a\x9a\x0c\n\x07\x43ontent\x12,\n\x0bmessageText\x18\x01 \x01(\x0b\x32\x15.WACommon.MessageTextH\x00\x12O\n\x0cimageMessage\x18\x02 \x01(\x0b\x32\x37.WAConsumerApplication.ConsumerApplication.ImageMessageH\x00\x12S\n\x0e\x63ontactMessage\x18\x03 \x01(\x0b\x32\x39.WAConsumerApplication.ConsumerApplication.ContactMessageH\x00\x12U\n\x0flocationMessage\x18\x04 \x01(\x0b\x32:.WAConsumerApplication.ConsumerApplication.LocationMessageH\x00\x12]\n\x13\x65xtendedTextMessage\x18\x05 \x01(\x0b\x32>.WAConsumerApplication.ConsumerApplication.ExtendedTextMessageH\x00\x12X\n\x11statusTextMessage\x18\x06 \x01(\x0b\x32;.WAConsumerApplication.ConsumerApplication.StatusTextMesageH\x00\x12U\n\x0f\x64ocumentMessage\x18\x07 \x01(\x0b\x32:.WAConsumerApplication.ConsumerApplication.DocumentMessageH\x00\x12O\n\x0c\x61udioMessage\x18\x08 \x01(\x0b\x32\x37.WAConsumerApplication.ConsumerApplication.AudioMessageH\x00\x12O\n\x0cvideoMessage\x18\t \x01(\x0b\x32\x37.WAConsumerApplication.ConsumerApplication.VideoMessageH\x00\x12_\n\x14\x63ontactsArrayMessage\x18\n \x01(\x0b\x32?.WAConsumerApplication.ConsumerApplication.ContactsArrayMessageH\x00\x12]\n\x13liveLocationMessage\x18\x0b \x01(\x0b\x32>.WAConsumerApplication.ConsumerApplication.LiveLocationMessageH\x00\x12S\n\x0estickerMessage\x18\x0c \x01(\x0b\x32\x39.WAConsumerApplication.ConsumerApplication.StickerMessageH\x00\x12[\n\x12groupInviteMessage\x18\r \x01(\x0b\x32=.WAConsumerApplication.ConsumerApplication.GroupInviteMessageH\x00\x12U\n\x0fviewOnceMessage\x18\x0e \x01(\x0b\x32:.WAConsumerApplication.ConsumerApplication.ViewOnceMessageH\x00\x12U\n\x0freactionMessage\x18\x10 \x01(\x0b\x32:.WAConsumerApplication.ConsumerApplication.ReactionMessageH\x00\x12]\n\x13pollCreationMessage\x18\x11 \x01(\x0b\x32>.WAConsumerApplication.ConsumerApplication.PollCreationMessageH\x00\x12Y\n\x11pollUpdateMessage\x18\x12 \x01(\x0b\x32<.WAConsumerApplication.ConsumerApplication.PollUpdateMessageH\x00\x12M\n\x0b\x65\x64itMessage\x18\x13 \x01(\x0b\x32\x36.WAConsumerApplication.ConsumerApplication.EditMessageH\x00\x42\t\n\x07\x63ontent\x1am\n\x0b\x45\x64itMessage\x12!\n\x03key\x18\x01 \x01(\x0b\x32\x14.WACommon.MessageKey\x12&\n\x07message\x18\x02 \x01(\x0b\x32\x15.WACommon.MessageText\x12\x13\n\x0btimestampMS\x18\x03 \x01(\x03\x1a]\n\x14PollAddOptionMessage\x12\x45\n\npollOption\x18\x01 \x03(\x0b\x32\x31.WAConsumerApplication.ConsumerApplication.Option\x1a\x45\n\x0fPollVoteMessage\x12\x17\n\x0fselectedOptions\x18\x01 \x03(\x0c\x12\x19\n\x11senderTimestampMS\x18\x02 \x01(\x03\x1a\x31\n\x0cPollEncValue\x12\x12\n\nencPayload\x18\x01 \x01(\x0c\x12\r\n\x05\x65ncIV\x18\x02 \x01(\x0c\x1a\xdc\x01\n\x11PollUpdateMessage\x12\x34\n\x16pollCreationMessageKey\x18\x01 \x01(\x0b\x32\x14.WACommon.MessageKey\x12\x45\n\x04vote\x18\x02 \x01(\x0b\x32\x37.WAConsumerApplication.ConsumerApplication.PollEncValue\x12J\n\taddOption\x18\x03 \x01(\x0b\x32\x37.WAConsumerApplication.ConsumerApplication.PollEncValue\x1a\x97\x01\n\x13PollCreationMessage\x12\x0e\n\x06\x65ncKey\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x42\n\x07options\x18\x03 \x03(\x0b\x32\x31.WAConsumerApplication.ConsumerApplication.Option\x12\x1e\n\x16selectableOptionsCount\x18\x04 \x01(\r\x1a\x1c\n\x06Option\x12\x12\n\noptionName\x18\x01 \x01(\t\x1a\xa8\x01\n\x0fReactionMessage\x12!\n\x03key\x18\x01 \x01(\x0b\x32\x14.WACommon.MessageKey\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x13\n\x0bgroupingKey\x18\x03 \x01(\t\x12\x19\n\x11senderTimestampMS\x18\x04 \x01(\x03\x12%\n\x1dreactionMetadataDataclassData\x18\x05 \x01(\t\x12\r\n\x05style\x18\x06 \x01(\x05\x1a\x32\n\rRevokeMessage\x12!\n\x03key\x18\x01 \x01(\x0b\x32\x14.WACommon.MessageKey\x1a\xc6\x01\n\x0fViewOnceMessage\x12O\n\x0cimageMessage\x18\x01 \x01(\x0b\x32\x37.WAConsumerApplication.ConsumerApplication.ImageMessageH\x00\x12O\n\x0cvideoMessage\x18\x02 \x01(\x0b\x32\x37.WAConsumerApplication.ConsumerApplication.VideoMessageH\x00\x42\x11\n\x0fviewOnceContent\x1a\xa6\x01\n\x12GroupInviteMessage\x12\x10\n\x08groupJID\x18\x01 \x01(\t\x12\x12\n\ninviteCode\x18\x02 \x01(\t\x12\x18\n\x10inviteExpiration\x18\x03 \x01(\x03\x12\x11\n\tgroupName\x18\x04 \x01(\t\x12\x15\n\rJPEGThumbnail\x18\x05 \x01(\x0c\x12&\n\x07\x63\x61ption\x18\x06 \x01(\x0b\x32\x15.WACommon.MessageText\x1a\x89\x02\n\x13LiveLocationMessage\x12\x45\n\x08location\x18\x01 \x01(\x0b\x32\x33.WAConsumerApplication.ConsumerApplication.Location\x12\x18\n\x10\x61\x63\x63uracyInMeters\x18\x02 \x01(\r\x12\x12\n\nspeedInMps\x18\x03 \x01(\x02\x12)\n!degreesClockwiseFromMagneticNorth\x18\x04 \x01(\r\x12&\n\x07\x63\x61ption\x18\x05 \x01(\x0b\x32\x15.WACommon.MessageText\x12\x16\n\x0esequenceNumber\x18\x06 \x01(\x03\x12\x12\n\ntimeOffset\x18\x07 \x01(\r\x1ax\n\x14\x43ontactsArrayMessage\x12\x13\n\x0b\x64isplayName\x18\x01 \x01(\t\x12K\n\x08\x63ontacts\x18\x02 \x03(\x0b\x32\x39.WAConsumerApplication.ConsumerApplication.ContactMessage\x1a\x38\n\x0e\x43ontactMessage\x12&\n\x07\x63ontact\x18\x01 \x01(\x0b\x32\x15.WACommon.SubProtocol\x1a\xd6\x02\n\x10StatusTextMesage\x12L\n\x04text\x18\x01 \x01(\x0b\x32>.WAConsumerApplication.ConsumerApplication.ExtendedTextMessage\x12\x10\n\x08textArgb\x18\x06 \x01(\x07\x12\x16\n\x0e\x62\x61\x63kgroundArgb\x18\x07 \x01(\x07\x12R\n\x04\x66ont\x18\x08 \x01(\x0e\x32\x44.WAConsumerApplication.ConsumerApplication.StatusTextMesage.FontType\"v\n\x08\x46ontType\x12\x0e\n\nSANS_SERIF\x10\x00\x12\t\n\x05SERIF\x10\x01\x12\x13\n\x0fNORICAN_REGULAR\x10\x02\x12\x11\n\rBRYNDAN_WRITE\x10\x03\x12\x15\n\x11\x42\x45\x42\x41SNEUE_REGULAR\x10\x04\x12\x10\n\x0cOSWALD_HEAVY\x10\x05\x1a\xb8\x02\n\x13\x45xtendedTextMessage\x12#\n\x04text\x18\x01 \x01(\x0b\x32\x15.WACommon.MessageText\x12\x13\n\x0bmatchedText\x18\x02 \x01(\t\x12\x14\n\x0c\x63\x61nonicalURL\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12(\n\tthumbnail\x18\x06 \x01(\x0b\x32\x15.WACommon.SubProtocol\x12_\n\x0bpreviewType\x18\x07 \x01(\x0e\x32J.WAConsumerApplication.ConsumerApplication.ExtendedTextMessage.PreviewType\"\"\n\x0bPreviewType\x12\x08\n\x04NONE\x10\x00\x12\t\n\x05VIDEO\x10\x01\x1ai\n\x0fLocationMessage\x12\x45\n\x08location\x18\x01 \x01(\x0b\x32\x33.WAConsumerApplication.ConsumerApplication.Location\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x1a\x38\n\x0eStickerMessage\x12&\n\x07sticker\x18\x01 \x01(\x0b\x32\x15.WACommon.SubProtocol\x1aL\n\x0f\x44ocumentMessage\x12\'\n\x08\x64ocument\x18\x01 \x01(\x0b\x32\x15.WACommon.SubProtocol\x12\x10\n\x08\x66ileName\x18\x02 \x01(\t\x1a\\\n\x0cVideoMessage\x12$\n\x05video\x18\x01 \x01(\x0b\x32\x15.WACommon.SubProtocol\x12&\n\x07\x63\x61ption\x18\x02 \x01(\x0b\x32\x15.WACommon.MessageText\x1a\x41\n\x0c\x41udioMessage\x12$\n\x05\x61udio\x18\x01 \x01(\x0b\x32\x15.WACommon.SubProtocol\x12\x0b\n\x03PTT\x18\x02 \x01(\x08\x1a\\\n\x0cImageMessage\x12$\n\x05image\x18\x01 \x01(\x0b\x32\x15.WACommon.SubProtocol\x12&\n\x07\x63\x61ption\x18\x02 \x01(\x0b\x32\x15.WACommon.MessageText\x1a\xb5\x01\n\x15InteractiveAnnotation\x12G\n\x08location\x18\x02 \x01(\x0b\x32\x33.WAConsumerApplication.ConsumerApplication.LocationH\x00\x12I\n\x0fpolygonVertices\x18\x01 \x03(\x0b\x32\x30.WAConsumerApplication.ConsumerApplication.PointB\x08\n\x06\x61\x63tion\x1a\x1d\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x1aK\n\x08Location\x12\x17\n\x0f\x64\x65greesLatitude\x18\x01 \x01(\x01\x12\x18\n\x10\x64\x65greesLongitude\x18\x02 \x01(\x01\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a\x37\n\x0cMediaPayload\x12\'\n\x08protocol\x18\x01 \x01(\x0b\x32\x15.WACommon.SubProtocolB1Z/go.mau.fi/whatsmeow/proto/waConsumerApplication')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'waConsumerApplication.WAConsumerApplication_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z/go.mau.fi/whatsmeow/proto/waConsumerApplication'
  _globals['_CONSUMERAPPLICATION']._serialized_start=102
  _globals['_CONSUMERAPPLICATION']._serialized_end=5808
  _globals['_CONSUMERAPPLICATION_PAYLOAD']._serialized_start=266
  _globals['_CONSUMERAPPLICATION_PAYLOAD']._serialized_end=599
  _globals['_CONSUMERAPPLICATION_SUBPROTOCOLPAYLOAD']._serialized_start=601
  _globals['_CONSUMERAPPLICATION_SUBPROTOCOLPAYLOAD']._serialized_end=673
  _globals['_CONSUMERAPPLICATION_METADATA']._serialized_start=676
  _globals['_CONSUMERAPPLICATION_METADATA']._serialized_end=833
  _globals['_CONSUMERAPPLICATION_METADATA_SPECIALTEXTSIZE']._serialized_start=782
  _globals['_CONSUMERAPPLICATION_METADATA_SPECIALTEXTSIZE']._serialized_end=833
  _globals['_CONSUMERAPPLICATION_SIGNAL']._serialized_start=835
  _globals['_CONSUMERAPPLICATION_SIGNAL']._serialized_end=843
  _globals['_CONSUMERAPPLICATION_APPLICATIONDATA']._serialized_start=845
  _globals['_CONSUMERAPPLICATION_APPLICATIONDATA']._serialized_end=960
  _globals['_CONSUMERAPPLICATION_CONTENT']._serialized_start=963
  _globals['_CONSUMERAPPLICATION_CONTENT']._serialized_end=2525
  _globals['_CONSUMERAPPLICATION_EDITMESSAGE']._serialized_start=2527
  _globals['_CONSUMERAPPLICATION_EDITMESSAGE']._serialized_end=2636
  _globals['_CONSUMERAPPLICATION_POLLADDOPTIONMESSAGE']._serialized_start=2638
  _globals['_CONSUMERAPPLICATION_POLLADDOPTIONMESSAGE']._serialized_end=2731
  _globals['_CONSUMERAPPLICATION_POLLVOTEMESSAGE']._serialized_start=2733
  _globals['_CONSUMERAPPLICATION_POLLVOTEMESSAGE']._serialized_end=2802
  _globals['_CONSUMERAPPLICATION_POLLENCVALUE']._serialized_start=2804
  _globals['_CONSUMERAPPLICATION_POLLENCVALUE']._serialized_end=2853
  _globals['_CONSUMERAPPLICATION_POLLUPDATEMESSAGE']._serialized_start=2856
  _globals['_CONSUMERAPPLICATION_POLLUPDATEMESSAGE']._serialized_end=3076
  _globals['_CONSUMERAPPLICATION_POLLCREATIONMESSAGE']._serialized_start=3079
  _globals['_CONSUMERAPPLICATION_POLLCREATIONMESSAGE']._serialized_end=3230
  _globals['_CONSUMERAPPLICATION_OPTION']._serialized_start=3232
  _globals['_CONSUMERAPPLICATION_OPTION']._serialized_end=3260
  _globals['_CONSUMERAPPLICATION_REACTIONMESSAGE']._serialized_start=3263
  _globals['_CONSUMERAPPLICATION_REACTIONMESSAGE']._serialized_end=3431
  _globals['_CONSUMERAPPLICATION_REVOKEMESSAGE']._serialized_start=3433
  _globals['_CONSUMERAPPLICATION_REVOKEMESSAGE']._serialized_end=3483
  _globals['_CONSUMERAPPLICATION_VIEWONCEMESSAGE']._serialized_start=3486
  _globals['_CONSUMERAPPLICATION_VIEWONCEMESSAGE']._serialized_end=3684
  _globals['_CONSUMERAPPLICATION_GROUPINVITEMESSAGE']._serialized_start=3687
  _globals['_CONSUMERAPPLICATION_GROUPINVITEMESSAGE']._serialized_end=3853
  _globals['_CONSUMERAPPLICATION_LIVELOCATIONMESSAGE']._serialized_start=3856
  _globals['_CONSUMERAPPLICATION_LIVELOCATIONMESSAGE']._serialized_end=4121
  _globals['_CONSUMERAPPLICATION_CONTACTSARRAYMESSAGE']._serialized_start=4123
  _globals['_CONSUMERAPPLICATION_CONTACTSARRAYMESSAGE']._serialized_end=4243
  _globals['_CONSUMERAPPLICATION_CONTACTMESSAGE']._serialized_start=4245
  _globals['_CONSUMERAPPLICATION_CONTACTMESSAGE']._serialized_end=4301
  _globals['_CONSUMERAPPLICATION_STATUSTEXTMESAGE']._serialized_start=4304
  _globals['_CONSUMERAPPLICATION_STATUSTEXTMESAGE']._serialized_end=4646
  _globals['_CONSUMERAPPLICATION_STATUSTEXTMESAGE_FONTTYPE']._serialized_start=4528
  _globals['_CONSUMERAPPLICATION_STATUSTEXTMESAGE_FONTTYPE']._serialized_end=4646
  _globals['_CONSUMERAPPLICATION_EXTENDEDTEXTMESSAGE']._serialized_start=4649
  _globals['_CONSUMERAPPLICATION_EXTENDEDTEXTMESSAGE']._serialized_end=4961
  _globals['_CONSUMERAPPLICATION_EXTENDEDTEXTMESSAGE_PREVIEWTYPE']._serialized_start=4927
  _globals['_CONSUMERAPPLICATION_EXTENDEDTEXTMESSAGE_PREVIEWTYPE']._serialized_end=4961
  _globals['_CONSUMERAPPLICATION_LOCATIONMESSAGE']._serialized_start=4963
  _globals['_CONSUMERAPPLICATION_LOCATIONMESSAGE']._serialized_end=5068
  _globals['_CONSUMERAPPLICATION_STICKERMESSAGE']._serialized_start=5070
  _globals['_CONSUMERAPPLICATION_STICKERMESSAGE']._serialized_end=5126
  _globals['_CONSUMERAPPLICATION_DOCUMENTMESSAGE']._serialized_start=5128
  _globals['_CONSUMERAPPLICATION_DOCUMENTMESSAGE']._serialized_end=5204
  _globals['_CONSUMERAPPLICATION_VIDEOMESSAGE']._serialized_start=5206
  _globals['_CONSUMERAPPLICATION_VIDEOMESSAGE']._serialized_end=5298
  _globals['_CONSUMERAPPLICATION_AUDIOMESSAGE']._serialized_start=5300
  _globals['_CONSUMERAPPLICATION_AUDIOMESSAGE']._serialized_end=5365
  _globals['_CONSUMERAPPLICATION_IMAGEMESSAGE']._serialized_start=5367
  _globals['_CONSUMERAPPLICATION_IMAGEMESSAGE']._serialized_end=5459
  _globals['_CONSUMERAPPLICATION_INTERACTIVEANNOTATION']._serialized_start=5462
  _globals['_CONSUMERAPPLICATION_INTERACTIVEANNOTATION']._serialized_end=5643
  _globals['_CONSUMERAPPLICATION_POINT']._serialized_start=5645
  _globals['_CONSUMERAPPLICATION_POINT']._serialized_end=5674
  _globals['_CONSUMERAPPLICATION_LOCATION']._serialized_start=5676
  _globals['_CONSUMERAPPLICATION_LOCATION']._serialized_end=5751
  _globals['_CONSUMERAPPLICATION_MEDIAPAYLOAD']._serialized_start=5753
  _globals['_CONSUMERAPPLICATION_MEDIAPAYLOAD']._serialized_end=5808
# @@protoc_insertion_point(module_scope)
