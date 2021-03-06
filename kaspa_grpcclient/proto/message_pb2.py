# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from kaspa_grpcclient.proto import rpc_pb2 as proto_dot_rpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proto/message.proto\x12\tprotowire\x1a\x0fproto/rpc.proto\"\xc6\x02\n\rKaspadMessage\x12\x43\n\x12submitBlockRequest\x18\xeb\x07 \x01(\x0b\x32$.protowire.SubmitBlockRequestMessageH\x00\x12\x45\n\x13submitBlockResponse\x18\xec\x07 \x01(\x0b\x32%.protowire.SubmitBlockResponseMessageH\x00\x12M\n\x17getBlockTemplateRequest\x18\xed\x07 \x01(\x0b\x32).protowire.GetBlockTemplateRequestMessageH\x00\x12O\n\x18getBlockTemplateResponse\x18\xee\x07 \x01(\x0b\x32*.protowire.GetBlockTemplateResponseMessageH\x00\x42\t\n\x07payload2P\n\x03RPC\x12I\n\rMessageStream\x12\x18.protowire.KaspadMessage\x1a\x18.protowire.KaspadMessage\"\x00(\x01\x30\x01\x42&Z$github.com/kaspanet/kaspad/protowireb\x06proto3')



_KASPADMESSAGE = DESCRIPTOR.message_types_by_name['KaspadMessage']
KaspadMessage = _reflection.GeneratedProtocolMessageType('KaspadMessage', (_message.Message,), {
  'DESCRIPTOR' : _KASPADMESSAGE,
  '__module__' : 'proto.message_pb2'
  # @@protoc_insertion_point(class_scope:protowire.KaspadMessage)
  })
_sym_db.RegisterMessage(KaspadMessage)

_RPC = DESCRIPTOR.services_by_name['RPC']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/kaspanet/kaspad/protowire'
  _KASPADMESSAGE._serialized_start=52
  _KASPADMESSAGE._serialized_end=378
  _RPC._serialized_start=380
  _RPC._serialized_end=460
# @@protoc_insertion_point(module_scope)
