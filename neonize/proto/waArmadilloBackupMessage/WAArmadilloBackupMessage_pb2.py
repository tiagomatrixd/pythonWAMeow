# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: waArmadilloBackupMessage/WAArmadilloBackupMessage.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n7waArmadilloBackupMessage/WAArmadilloBackupMessage.proto\x12\x18WAArmadilloBackupMessage"\xfc\x02\n\rBackupMessage\x12\x42\n\x08metadata\x18\x01 \x01(\x0b\x32\x30.WAArmadilloBackupMessage.BackupMessage.Metadata\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x1a\x95\x02\n\x08Metadata\x12\x10\n\x08senderID\x18\x01 \x01(\t\x12\x11\n\tmessageID\x18\x02 \x01(\t\x12\x13\n\x0btimestampMS\x18\x03 \x01(\x03\x12[\n\x10\x66rankingMetadata\x18\x04 \x01(\x0b\x32\x41.WAArmadilloBackupMessage.BackupMessage.Metadata.FrankingMetadata\x12\x16\n\x0epayloadVersion\x18\x05 \x01(\x05\x12\x1b\n\x13\x66utureProofBehavior\x18\x06 \x01(\x05\x1a=\n\x10\x46rankingMetadata\x12\x13\n\x0b\x66rankingTag\x18\x03 \x01(\x0c\x12\x14\n\x0creportingTag\x18\x04 \x01(\x0c\x42\x34Z2go.mau.fi/whatsmeow/proto/waArmadilloBackupMessage'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "waArmadilloBackupMessage.WAArmadilloBackupMessage_pb2", _globals
)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"Z2go.mau.fi/whatsmeow/proto/waArmadilloBackupMessage"
    _globals["_BACKUPMESSAGE"]._serialized_start = 86
    _globals["_BACKUPMESSAGE"]._serialized_end = 466
    _globals["_BACKUPMESSAGE_METADATA"]._serialized_start = 189
    _globals["_BACKUPMESSAGE_METADATA"]._serialized_end = 466
    _globals["_BACKUPMESSAGE_METADATA_FRANKINGMETADATA"]._serialized_start = 405
    _globals["_BACKUPMESSAGE_METADATA_FRANKINGMETADATA"]._serialized_end = 466
# @@protoc_insertion_point(module_scope)
