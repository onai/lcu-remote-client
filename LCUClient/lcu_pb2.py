# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lcu.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tlcu.proto\x1a\x1egoogle/protobuf/wrappers.proto\"s\n\x10LcuClientMessage\x12$\n\x0clcu_announce\x18\x01 \x01(\x0b\x32\x0c.LcuAnnounceH\x00\x12+\n\x0elcu_status_req\x18\x02 \x01(\x0b\x32\x11.LcuStatusRequestH\x00\x42\x0c\n\nlcu_client\"\x80\x01\n\x12LcuResponseMessage\x12\x1b\n\x07success\x18\x01 \x01(\x0b\x32\x08.SuccessH\x00\x12\x1b\n\x07\x66\x61ilure\x18\x02 \x01(\x0b\x32\x08.FailureH\x00\x12 \n\nlcu_status\x18\x03 \x01(\x0b\x32\n.LcuStatusH\x00\x42\x0e\n\x0clcu_response\"j\n\x0bLcuAnnounce\x12(\n\x02id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x12\n\x10LcuStatusRequest\"\t\n\x07Success\"7\n\x07\x46\x61ilure\x12,\n\x06reason\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"0\n\tLcuStatus\x12#\n\rlcu_announces\x18\x01 \x03(\x0b\x32\x0c.LcuAnnounceb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lcu_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LCUCLIENTMESSAGE._serialized_start=45
  _LCUCLIENTMESSAGE._serialized_end=160
  _LCURESPONSEMESSAGE._serialized_start=163
  _LCURESPONSEMESSAGE._serialized_end=291
  _LCUANNOUNCE._serialized_start=293
  _LCUANNOUNCE._serialized_end=399
  _LCUSTATUSREQUEST._serialized_start=401
  _LCUSTATUSREQUEST._serialized_end=419
  _SUCCESS._serialized_start=421
  _SUCCESS._serialized_end=430
  _FAILURE._serialized_start=432
  _FAILURE._serialized_end=487
  _LCUSTATUS._serialized_start=489
  _LCUSTATUS._serialized_end=537
# @@protoc_insertion_point(module_scope)
