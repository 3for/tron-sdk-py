# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tron_sdk_py/proto/core/contract/shield_contract.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'tron_sdk_py/proto/core/contract/shield_contract.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5tron_sdk_py/proto/core/contract/shield_contract.proto\x12\x08protocol\"#\n\x12\x41uthenticationPath\x12\r\n\x05value\x18\x01 \x03(\x08\"c\n\nMerklePath\x12:\n\x14\x61uthentication_paths\x18\x01 \x03(\x0b\x32\x1c.protocol.AuthenticationPath\x12\r\n\x05index\x18\x02 \x03(\x08\x12\n\n\x02rt\x18\x03 \x01(\x0c\"*\n\x0bOutputPoint\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\r\n\x05index\x18\x02 \x01(\x05\"O\n\x0fOutputPointInfo\x12)\n\nout_points\x18\x01 \x03(\x0b\x32\x15.protocol.OutputPoint\x12\x11\n\tblock_num\x18\x02 \x01(\x05\"\x1f\n\x0cPedersenHash\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\"\x8d\x01\n\x15IncrementalMerkleTree\x12$\n\x04left\x18\x01 \x01(\x0b\x32\x16.protocol.PedersenHash\x12%\n\x05right\x18\x02 \x01(\x0b\x32\x16.protocol.PedersenHash\x12\'\n\x07parents\x18\x03 \x03(\x0b\x32\x16.protocol.PedersenHash\"\xf1\x01\n\x18IncrementalMerkleVoucher\x12-\n\x04tree\x18\x01 \x01(\x0b\x32\x1f.protocol.IncrementalMerkleTree\x12&\n\x06\x66illed\x18\x02 \x03(\x0b\x32\x16.protocol.PedersenHash\x12/\n\x06\x63ursor\x18\x03 \x01(\x0b\x32\x1f.protocol.IncrementalMerkleTree\x12\x14\n\x0c\x63ursor_depth\x18\x04 \x01(\x03\x12\n\n\x02rt\x18\x05 \x01(\x0c\x12+\n\x0coutput_point\x18\n \x01(\x0b\x32\x15.protocol.OutputPoint\"c\n\x1cIncrementalMerkleVoucherInfo\x12\x34\n\x08vouchers\x18\x01 \x03(\x0b\x32\".protocol.IncrementalMerkleVoucher\x12\r\n\x05paths\x18\x02 \x03(\x0c\"\x8f\x01\n\x10SpendDescription\x12\x18\n\x10value_commitment\x18\x01 \x01(\x0c\x12\x0e\n\x06\x61nchor\x18\x02 \x01(\x0c\x12\x11\n\tnullifier\x18\x03 \x01(\x0c\x12\n\n\x02rk\x18\x04 \x01(\x0c\x12\x0f\n\x07zkproof\x18\x05 \x01(\x0c\x12!\n\x19spend_authority_signature\x18\x06 \x01(\x0c\"\x83\x01\n\x12ReceiveDescription\x12\x18\n\x10value_commitment\x18\x01 \x01(\x0c\x12\x17\n\x0fnote_commitment\x18\x02 \x01(\x0c\x12\x0b\n\x03\x65pk\x18\x03 \x01(\x0c\x12\r\n\x05\x63_enc\x18\x04 \x01(\x0c\x12\r\n\x05\x63_out\x18\x05 \x01(\x0c\x12\x0f\n\x07zkproof\x18\x06 \x01(\x0c\"\x91\x02\n\x18ShieldedTransferContract\x12 \n\x18transparent_from_address\x18\x01 \x01(\x0c\x12\x13\n\x0b\x66rom_amount\x18\x02 \x01(\x03\x12\x35\n\x11spend_description\x18\x03 \x03(\x0b\x32\x1a.protocol.SpendDescription\x12\x39\n\x13receive_description\x18\x04 \x03(\x0b\x32\x1c.protocol.ReceiveDescription\x12\x19\n\x11\x62inding_signature\x18\x05 \x01(\x0c\x12\x1e\n\x16transparent_to_address\x18\x06 \x01(\x0c\x12\x11\n\tto_amount\x18\x07 \x01(\x03\x42\x45\n\x18org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tron_sdk_py.proto.core.contract.shield_contract_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/core'
  _globals['_AUTHENTICATIONPATH']._serialized_start=67
  _globals['_AUTHENTICATIONPATH']._serialized_end=102
  _globals['_MERKLEPATH']._serialized_start=104
  _globals['_MERKLEPATH']._serialized_end=203
  _globals['_OUTPUTPOINT']._serialized_start=205
  _globals['_OUTPUTPOINT']._serialized_end=247
  _globals['_OUTPUTPOINTINFO']._serialized_start=249
  _globals['_OUTPUTPOINTINFO']._serialized_end=328
  _globals['_PEDERSENHASH']._serialized_start=330
  _globals['_PEDERSENHASH']._serialized_end=361
  _globals['_INCREMENTALMERKLETREE']._serialized_start=364
  _globals['_INCREMENTALMERKLETREE']._serialized_end=505
  _globals['_INCREMENTALMERKLEVOUCHER']._serialized_start=508
  _globals['_INCREMENTALMERKLEVOUCHER']._serialized_end=749
  _globals['_INCREMENTALMERKLEVOUCHERINFO']._serialized_start=751
  _globals['_INCREMENTALMERKLEVOUCHERINFO']._serialized_end=850
  _globals['_SPENDDESCRIPTION']._serialized_start=853
  _globals['_SPENDDESCRIPTION']._serialized_end=996
  _globals['_RECEIVEDESCRIPTION']._serialized_start=999
  _globals['_RECEIVEDESCRIPTION']._serialized_end=1130
  _globals['_SHIELDEDTRANSFERCONTRACT']._serialized_start=1133
  _globals['_SHIELDEDTRANSFERCONTRACT']._serialized_end=1406
# @@protoc_insertion_point(module_scope)
