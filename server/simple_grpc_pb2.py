# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simple_grpc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11simple_grpc.proto\x12\nsimplegrpc\"\x18\n\x08HelloReq\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1b\n\x08HelloRes\x12\x0f\n\x07message\x18\x01 \x01(\t2\xc6\x01\n\nSimpleGrpc\x12\x38\n\x08SayHello\x12\x14.simplegrpc.HelloReq\x1a\x14.simplegrpc.HelloRes\"\x00\x12@\n\x0eSayHelloToMany\x12\x14.simplegrpc.HelloReq\x1a\x14.simplegrpc.HelloRes\"\x00(\x01\x12<\n\nCheckInbox\x12\x14.simplegrpc.HelloReq\x1a\x14.simplegrpc.HelloRes\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simple_grpc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQ._serialized_start=33
  _HELLOREQ._serialized_end=57
  _HELLORES._serialized_start=59
  _HELLORES._serialized_end=86
  _SIMPLEGRPC._serialized_start=89
  _SIMPLEGRPC._serialized_end=287
# @@protoc_insertion_point(module_scope)
