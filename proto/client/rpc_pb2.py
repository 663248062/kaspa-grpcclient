# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\trpc.proto\x12\tprotowire\"\x1b\n\x08RPCError\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x9b\x01\n\x08RpcBlock\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.protowire.RpcBlockHeader\x12/\n\x0ctransactions\x18\x02 \x03(\x0b\x32\x19.protowire.RpcTransaction\x12\x33\n\x0bverboseData\x18\x03 \x01(\x0b\x32\x1e.protowire.RpcBlockVerboseData\"\x9e\x02\n\x0eRpcBlockHeader\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x30\n\x07parents\x18\x0c \x03(\x0b\x32\x1f.protowire.RpcBlockLevelParents\x12\x16\n\x0ehashMerkleRoot\x18\x03 \x01(\t\x12\x1c\n\x14\x61\x63\x63\x65ptedIdMerkleRoot\x18\x04 \x01(\t\x12\x16\n\x0eutxoCommitment\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x03\x12\x0c\n\x04\x62its\x18\x07 \x01(\r\x12\r\n\x05nonce\x18\x08 \x01(\x04\x12\x10\n\x08\x64\x61\x61Score\x18\t \x01(\x04\x12\x10\n\x08\x62lueWork\x18\n \x01(\t\x12\x14\n\x0cpruningPoint\x18\x0e \x01(\t\x12\x11\n\tblueScore\x18\r \x01(\x04\",\n\x14RpcBlockLevelParents\x12\x14\n\x0cparentHashes\x18\x01 \x03(\t\"\xfb\x01\n\x13RpcBlockVerboseData\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x12\n\ndifficulty\x18\x0b \x01(\x01\x12\x1a\n\x12selectedParentHash\x18\r \x01(\t\x12\x16\n\x0etransactionIds\x18\x0e \x03(\t\x12\x14\n\x0cisHeaderOnly\x18\x0f \x01(\x08\x12\x11\n\tblueScore\x18\x10 \x01(\x04\x12\x16\n\x0e\x63hildrenHashes\x18\x11 \x03(\t\x12\x1b\n\x13mergeSetBluesHashes\x18\x12 \x03(\t\x12\x1a\n\x12mergeSetRedsHashes\x18\x13 \x03(\t\x12\x14\n\x0cisChainBlock\x18\x14 \x01(\x08\"\x84\x02\n\x0eRpcTransaction\x12\x0f\n\x07version\x18\x01 \x01(\r\x12.\n\x06inputs\x18\x02 \x03(\x0b\x32\x1e.protowire.RpcTransactionInput\x12\x30\n\x07outputs\x18\x03 \x03(\x0b\x32\x1f.protowire.RpcTransactionOutput\x12\x10\n\x08lockTime\x18\x04 \x01(\x04\x12\x14\n\x0csubnetworkId\x18\x05 \x01(\t\x12\x0b\n\x03gas\x18\x06 \x01(\x04\x12\x0f\n\x07payload\x18\x08 \x01(\t\x12\x39\n\x0bverboseData\x18\t \x01(\x0b\x32$.protowire.RpcTransactionVerboseData\"\xc6\x01\n\x13RpcTransactionInput\x12\x30\n\x10previousOutpoint\x18\x01 \x01(\x0b\x32\x16.protowire.RpcOutpoint\x12\x17\n\x0fsignatureScript\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x12\x12\n\nsigOpCount\x18\x05 \x01(\r\x12>\n\x0bverboseData\x18\x04 \x01(\x0b\x32).protowire.RpcTransactionInputVerboseData\">\n\x12RpcScriptPublicKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x17\n\x0fscriptPublicKey\x18\x02 \x01(\t\"\x9f\x01\n\x14RpcTransactionOutput\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x04\x12\x36\n\x0fscriptPublicKey\x18\x02 \x01(\x0b\x32\x1d.protowire.RpcScriptPublicKey\x12?\n\x0bverboseData\x18\x03 \x01(\x0b\x32*.protowire.RpcTransactionOutputVerboseData\"3\n\x0bRpcOutpoint\x12\x15\n\rtransactionId\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\r\"\x81\x01\n\x0cRpcUtxoEntry\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x04\x12\x36\n\x0fscriptPublicKey\x18\x02 \x01(\x0b\x32\x1d.protowire.RpcScriptPublicKey\x12\x15\n\rblockDaaScore\x18\x03 \x01(\x04\x12\x12\n\nisCoinbase\x18\x04 \x01(\x08\"t\n\x19RpcTransactionVerboseData\x12\x15\n\rtransactionId\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\t\x12\x0c\n\x04mass\x18\x04 \x01(\x04\x12\x11\n\tblockHash\x18\x0c \x01(\t\x12\x11\n\tblockTime\x18\x0e \x01(\x04\" \n\x1eRpcTransactionInputVerboseData\"^\n\x1fRpcTransactionOutputVerboseData\x12\x1b\n\x13scriptPublicKeyType\x18\x05 \x01(\t\x12\x1e\n\x16scriptPublicKeyAddress\x18\x06 \x01(\t\"Z\n\x19SubmitBlockRequestMessage\x12\"\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x13.protowire.RpcBlock\x12\x19\n\x11\x61llowNonDAABlocks\x18\x03 \x01(\x08\"\xc7\x01\n\x1aSubmitBlockResponseMessage\x12H\n\x0crejectReason\x18\x01 \x01(\x0e\x32\x32.protowire.SubmitBlockResponseMessage.RejectReason\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCError\":\n\x0cRejectReason\x12\x08\n\x04NONE\x10\x00\x12\x11\n\rBLOCK_INVALID\x10\x01\x12\r\n\tIS_IN_IBD\x10\x02\"G\n\x1eGetBlockTemplateRequestMessage\x12\x12\n\npayAddress\x18\x01 \x01(\t\x12\x11\n\textraData\x18\x02 \x01(\t\"|\n\x1fGetBlockTemplateResponseMessage\x12\"\n\x05\x62lock\x18\x03 \x01(\x0b\x32\x13.protowire.RpcBlock\x12\x10\n\x08isSynced\x18\x02 \x01(\x08\x12#\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\x13.protowire.RPCErrorB&Z$github.com/kaspanet/kaspad/protowireb\x06proto3')



_RPCERROR = DESCRIPTOR.message_types_by_name['RPCError']
_RPCBLOCK = DESCRIPTOR.message_types_by_name['RpcBlock']
_RPCBLOCKHEADER = DESCRIPTOR.message_types_by_name['RpcBlockHeader']
_RPCBLOCKLEVELPARENTS = DESCRIPTOR.message_types_by_name['RpcBlockLevelParents']
_RPCBLOCKVERBOSEDATA = DESCRIPTOR.message_types_by_name['RpcBlockVerboseData']
_RPCTRANSACTION = DESCRIPTOR.message_types_by_name['RpcTransaction']
_RPCTRANSACTIONINPUT = DESCRIPTOR.message_types_by_name['RpcTransactionInput']
_RPCSCRIPTPUBLICKEY = DESCRIPTOR.message_types_by_name['RpcScriptPublicKey']
_RPCTRANSACTIONOUTPUT = DESCRIPTOR.message_types_by_name['RpcTransactionOutput']
_RPCOUTPOINT = DESCRIPTOR.message_types_by_name['RpcOutpoint']
_RPCUTXOENTRY = DESCRIPTOR.message_types_by_name['RpcUtxoEntry']
_RPCTRANSACTIONVERBOSEDATA = DESCRIPTOR.message_types_by_name['RpcTransactionVerboseData']
_RPCTRANSACTIONINPUTVERBOSEDATA = DESCRIPTOR.message_types_by_name['RpcTransactionInputVerboseData']
_RPCTRANSACTIONOUTPUTVERBOSEDATA = DESCRIPTOR.message_types_by_name['RpcTransactionOutputVerboseData']
_SUBMITBLOCKREQUESTMESSAGE = DESCRIPTOR.message_types_by_name['SubmitBlockRequestMessage']
_SUBMITBLOCKRESPONSEMESSAGE = DESCRIPTOR.message_types_by_name['SubmitBlockResponseMessage']
_GETBLOCKTEMPLATEREQUESTMESSAGE = DESCRIPTOR.message_types_by_name['GetBlockTemplateRequestMessage']
_GETBLOCKTEMPLATERESPONSEMESSAGE = DESCRIPTOR.message_types_by_name['GetBlockTemplateResponseMessage']
_SUBMITBLOCKRESPONSEMESSAGE_REJECTREASON = _SUBMITBLOCKRESPONSEMESSAGE.enum_types_by_name['RejectReason']
RPCError = _reflection.GeneratedProtocolMessageType('RPCError', (_message.Message,), {
  'DESCRIPTOR' : _RPCERROR,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RPCError)
  })
_sym_db.RegisterMessage(RPCError)

RpcBlock = _reflection.GeneratedProtocolMessageType('RpcBlock', (_message.Message,), {
  'DESCRIPTOR' : _RPCBLOCK,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcBlock)
  })
_sym_db.RegisterMessage(RpcBlock)

RpcBlockHeader = _reflection.GeneratedProtocolMessageType('RpcBlockHeader', (_message.Message,), {
  'DESCRIPTOR' : _RPCBLOCKHEADER,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcBlockHeader)
  })
_sym_db.RegisterMessage(RpcBlockHeader)

RpcBlockLevelParents = _reflection.GeneratedProtocolMessageType('RpcBlockLevelParents', (_message.Message,), {
  'DESCRIPTOR' : _RPCBLOCKLEVELPARENTS,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcBlockLevelParents)
  })
_sym_db.RegisterMessage(RpcBlockLevelParents)

RpcBlockVerboseData = _reflection.GeneratedProtocolMessageType('RpcBlockVerboseData', (_message.Message,), {
  'DESCRIPTOR' : _RPCBLOCKVERBOSEDATA,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcBlockVerboseData)
  })
_sym_db.RegisterMessage(RpcBlockVerboseData)

RpcTransaction = _reflection.GeneratedProtocolMessageType('RpcTransaction', (_message.Message,), {
  'DESCRIPTOR' : _RPCTRANSACTION,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcTransaction)
  })
_sym_db.RegisterMessage(RpcTransaction)

RpcTransactionInput = _reflection.GeneratedProtocolMessageType('RpcTransactionInput', (_message.Message,), {
  'DESCRIPTOR' : _RPCTRANSACTIONINPUT,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcTransactionInput)
  })
_sym_db.RegisterMessage(RpcTransactionInput)

RpcScriptPublicKey = _reflection.GeneratedProtocolMessageType('RpcScriptPublicKey', (_message.Message,), {
  'DESCRIPTOR' : _RPCSCRIPTPUBLICKEY,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcScriptPublicKey)
  })
_sym_db.RegisterMessage(RpcScriptPublicKey)

RpcTransactionOutput = _reflection.GeneratedProtocolMessageType('RpcTransactionOutput', (_message.Message,), {
  'DESCRIPTOR' : _RPCTRANSACTIONOUTPUT,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcTransactionOutput)
  })
_sym_db.RegisterMessage(RpcTransactionOutput)

RpcOutpoint = _reflection.GeneratedProtocolMessageType('RpcOutpoint', (_message.Message,), {
  'DESCRIPTOR' : _RPCOUTPOINT,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcOutpoint)
  })
_sym_db.RegisterMessage(RpcOutpoint)

RpcUtxoEntry = _reflection.GeneratedProtocolMessageType('RpcUtxoEntry', (_message.Message,), {
  'DESCRIPTOR' : _RPCUTXOENTRY,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcUtxoEntry)
  })
_sym_db.RegisterMessage(RpcUtxoEntry)

RpcTransactionVerboseData = _reflection.GeneratedProtocolMessageType('RpcTransactionVerboseData', (_message.Message,), {
  'DESCRIPTOR' : _RPCTRANSACTIONVERBOSEDATA,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcTransactionVerboseData)
  })
_sym_db.RegisterMessage(RpcTransactionVerboseData)

RpcTransactionInputVerboseData = _reflection.GeneratedProtocolMessageType('RpcTransactionInputVerboseData', (_message.Message,), {
  'DESCRIPTOR' : _RPCTRANSACTIONINPUTVERBOSEDATA,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcTransactionInputVerboseData)
  })
_sym_db.RegisterMessage(RpcTransactionInputVerboseData)

RpcTransactionOutputVerboseData = _reflection.GeneratedProtocolMessageType('RpcTransactionOutputVerboseData', (_message.Message,), {
  'DESCRIPTOR' : _RPCTRANSACTIONOUTPUTVERBOSEDATA,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.RpcTransactionOutputVerboseData)
  })
_sym_db.RegisterMessage(RpcTransactionOutputVerboseData)

SubmitBlockRequestMessage = _reflection.GeneratedProtocolMessageType('SubmitBlockRequestMessage', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITBLOCKREQUESTMESSAGE,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.SubmitBlockRequestMessage)
  })
_sym_db.RegisterMessage(SubmitBlockRequestMessage)

SubmitBlockResponseMessage = _reflection.GeneratedProtocolMessageType('SubmitBlockResponseMessage', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITBLOCKRESPONSEMESSAGE,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.SubmitBlockResponseMessage)
  })
_sym_db.RegisterMessage(SubmitBlockResponseMessage)

GetBlockTemplateRequestMessage = _reflection.GeneratedProtocolMessageType('GetBlockTemplateRequestMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKTEMPLATEREQUESTMESSAGE,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.GetBlockTemplateRequestMessage)
  })
_sym_db.RegisterMessage(GetBlockTemplateRequestMessage)

GetBlockTemplateResponseMessage = _reflection.GeneratedProtocolMessageType('GetBlockTemplateResponseMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCKTEMPLATERESPONSEMESSAGE,
  '__module__' : 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:protowire.GetBlockTemplateResponseMessage)
  })
_sym_db.RegisterMessage(GetBlockTemplateResponseMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/kaspanet/kaspad/protowire'
  _RPCERROR._serialized_start=24
  _RPCERROR._serialized_end=51
  _RPCBLOCK._serialized_start=54
  _RPCBLOCK._serialized_end=209
  _RPCBLOCKHEADER._serialized_start=212
  _RPCBLOCKHEADER._serialized_end=498
  _RPCBLOCKLEVELPARENTS._serialized_start=500
  _RPCBLOCKLEVELPARENTS._serialized_end=544
  _RPCBLOCKVERBOSEDATA._serialized_start=547
  _RPCBLOCKVERBOSEDATA._serialized_end=798
  _RPCTRANSACTION._serialized_start=801
  _RPCTRANSACTION._serialized_end=1061
  _RPCTRANSACTIONINPUT._serialized_start=1064
  _RPCTRANSACTIONINPUT._serialized_end=1262
  _RPCSCRIPTPUBLICKEY._serialized_start=1264
  _RPCSCRIPTPUBLICKEY._serialized_end=1326
  _RPCTRANSACTIONOUTPUT._serialized_start=1329
  _RPCTRANSACTIONOUTPUT._serialized_end=1488
  _RPCOUTPOINT._serialized_start=1490
  _RPCOUTPOINT._serialized_end=1541
  _RPCUTXOENTRY._serialized_start=1544
  _RPCUTXOENTRY._serialized_end=1673
  _RPCTRANSACTIONVERBOSEDATA._serialized_start=1675
  _RPCTRANSACTIONVERBOSEDATA._serialized_end=1791
  _RPCTRANSACTIONINPUTVERBOSEDATA._serialized_start=1793
  _RPCTRANSACTIONINPUTVERBOSEDATA._serialized_end=1825
  _RPCTRANSACTIONOUTPUTVERBOSEDATA._serialized_start=1827
  _RPCTRANSACTIONOUTPUTVERBOSEDATA._serialized_end=1921
  _SUBMITBLOCKREQUESTMESSAGE._serialized_start=1923
  _SUBMITBLOCKREQUESTMESSAGE._serialized_end=2013
  _SUBMITBLOCKRESPONSEMESSAGE._serialized_start=2016
  _SUBMITBLOCKRESPONSEMESSAGE._serialized_end=2215
  _SUBMITBLOCKRESPONSEMESSAGE_REJECTREASON._serialized_start=2157
  _SUBMITBLOCKRESPONSEMESSAGE_REJECTREASON._serialized_end=2215
  _GETBLOCKTEMPLATEREQUESTMESSAGE._serialized_start=2217
  _GETBLOCKTEMPLATEREQUESTMESSAGE._serialized_end=2288
  _GETBLOCKTEMPLATERESPONSEMESSAGE._serialized_start=2290
  _GETBLOCKTEMPLATERESPONSEMESSAGE._serialized_end=2414
# @@protoc_insertion_point(module_scope)
