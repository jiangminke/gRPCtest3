# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello_grpc1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello_grpc1.proto',
  package='test',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11hello_grpc1.proto\x12\x04test\"*\n\rHelloDeweiReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\"\xe2\x01\n\x0fHelloDeweiReply\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x31\n\x06number\x18\x04 \x03(\x0b\x32!.test.HelloDeweiReply.NumberEntry\x1aY\n\x0bNumberEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.test.HelloDeweiReply.HelloTestReplyNunber:\x02\x38\x01\x1a\x31\n\x14HelloTestReplyNunber\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x03\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xb0\x01\n\x0cHelloTestReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\t\x12.\n\x06number\x18\x04 \x03(\x0b\x32\x1e.test.HelloTestReq.NumberEntry\x1aG\n\x0bNumberEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.test.HelloTestReqNunber:\x02\x38\x01\"B\n\x12HelloTestReqNunber\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x11\n\tis_active\x18\x03 \x01(\x08\"\x10\n\x0eHelloTestReply\"+\n\x1bTestClientRecvStreamRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\".\n\x1cTestClientRecvStreamResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"+\n\x1bTestClientsendStreamRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\'\n\x17TestTwoWayStreamRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\".\n\x1cTestClientsendStreamResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"*\n\x18TestTwoWayStreamResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2\xa4\x03\n\x08\x42ilibili\x12:\n\nHelloDewei\x12\x13.test.HelloDeweiReq\x1a\x15.test.HelloDeweiReply\"\x00\x12;\n\tHelloTest\x12\x12.test.HelloTestReq\x1a\x14.test.HelloTestReply\"\x00(\x01\x30\x01\x12\x61\n\x14TestClientRecvStream\x12!.test.TestClientRecvStreamRequest\x1a\".test.TestClientRecvStreamResponse\"\x00\x30\x01\x12\x63\n\x14TestClientsendStream\x12!.test.TestClientsendStreamRequest\x1a\".test.TestClientsendStreamResponse\"\x00(\x01\x30\x01\x12W\n\x10TestTwoWayStream\x12\x1d.test.TestTwoWayStreamRequest\x1a\x1e.test.TestTwoWayStreamResponse\"\x00(\x01\x30\x01\x62\x06proto3'
)




_HELLODEWEIREQ = _descriptor.Descriptor(
  name='HelloDeweiReq',
  full_name='test.HelloDeweiReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test.HelloDeweiReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='test.HelloDeweiReq.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=69,
)


_HELLODEWEIREPLY_NUMBERENTRY = _descriptor.Descriptor(
  name='NumberEntry',
  full_name='test.HelloDeweiReply.NumberEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test.HelloDeweiReply.NumberEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='test.HelloDeweiReply.NumberEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=247,
)

_HELLODEWEIREPLY_HELLOTESTREPLYNUNBER = _descriptor.Descriptor(
  name='HelloTestReplyNunber',
  full_name='test.HelloDeweiReply.HelloTestReplyNunber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='age', full_name='test.HelloDeweiReply.HelloTestReplyNunber.age', index=0,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='test.HelloDeweiReply.HelloTestReplyNunber.name', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=298,
)

_HELLODEWEIREPLY = _descriptor.Descriptor(
  name='HelloDeweiReply',
  full_name='test.HelloDeweiReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.HelloDeweiReply.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number', full_name='test.HelloDeweiReply.number', index=1,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HELLODEWEIREPLY_NUMBERENTRY, _HELLODEWEIREPLY_HELLOTESTREPLYNUNBER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=298,
)


_HELLOTESTREQ_NUMBERENTRY = _descriptor.Descriptor(
  name='NumberEntry',
  full_name='test.HelloTestReq.NumberEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='test.HelloTestReq.NumberEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='test.HelloTestReq.NumberEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=477,
)

_HELLOTESTREQ = _descriptor.Descriptor(
  name='HelloTestReq',
  full_name='test.HelloTestReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test.HelloTestReq.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='test.HelloTestReq.age', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='test.HelloTestReq.data', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number', full_name='test.HelloTestReq.number', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HELLOTESTREQ_NUMBERENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=301,
  serialized_end=477,
)


_HELLOTESTREQNUNBER = _descriptor.Descriptor(
  name='HelloTestReqNunber',
  full_name='test.HelloTestReqNunber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='test.HelloTestReqNunber.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='age', full_name='test.HelloTestReqNunber.age', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_active', full_name='test.HelloTestReqNunber.is_active', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=479,
  serialized_end=545,
)


_HELLOTESTREPLY = _descriptor.Descriptor(
  name='HelloTestReply',
  full_name='test.HelloTestReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=547,
  serialized_end=563,
)


_TESTCLIENTRECVSTREAMREQUEST = _descriptor.Descriptor(
  name='TestClientRecvStreamRequest',
  full_name='test.TestClientRecvStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.TestClientRecvStreamRequest.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=565,
  serialized_end=608,
)


_TESTCLIENTRECVSTREAMRESPONSE = _descriptor.Descriptor(
  name='TestClientRecvStreamResponse',
  full_name='test.TestClientRecvStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.TestClientRecvStreamResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=656,
)


_TESTCLIENTSENDSTREAMREQUEST = _descriptor.Descriptor(
  name='TestClientsendStreamRequest',
  full_name='test.TestClientsendStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.TestClientsendStreamRequest.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=658,
  serialized_end=701,
)


_TESTTWOWAYSTREAMREQUEST = _descriptor.Descriptor(
  name='TestTwoWayStreamRequest',
  full_name='test.TestTwoWayStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='test.TestTwoWayStreamRequest.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=703,
  serialized_end=742,
)


_TESTCLIENTSENDSTREAMRESPONSE = _descriptor.Descriptor(
  name='TestClientsendStreamResponse',
  full_name='test.TestClientsendStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.TestClientsendStreamResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=744,
  serialized_end=790,
)


_TESTTWOWAYSTREAMRESPONSE = _descriptor.Descriptor(
  name='TestTwoWayStreamResponse',
  full_name='test.TestTwoWayStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='test.TestTwoWayStreamResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=792,
  serialized_end=834,
)

_HELLODEWEIREPLY_NUMBERENTRY.fields_by_name['value'].message_type = _HELLODEWEIREPLY_HELLOTESTREPLYNUNBER
_HELLODEWEIREPLY_NUMBERENTRY.containing_type = _HELLODEWEIREPLY
_HELLODEWEIREPLY_HELLOTESTREPLYNUNBER.containing_type = _HELLODEWEIREPLY
_HELLODEWEIREPLY.fields_by_name['number'].message_type = _HELLODEWEIREPLY_NUMBERENTRY
_HELLOTESTREQ_NUMBERENTRY.fields_by_name['value'].message_type = _HELLOTESTREQNUNBER
_HELLOTESTREQ_NUMBERENTRY.containing_type = _HELLOTESTREQ
_HELLOTESTREQ.fields_by_name['number'].message_type = _HELLOTESTREQ_NUMBERENTRY
DESCRIPTOR.message_types_by_name['HelloDeweiReq'] = _HELLODEWEIREQ
DESCRIPTOR.message_types_by_name['HelloDeweiReply'] = _HELLODEWEIREPLY
DESCRIPTOR.message_types_by_name['HelloTestReq'] = _HELLOTESTREQ
DESCRIPTOR.message_types_by_name['HelloTestReqNunber'] = _HELLOTESTREQNUNBER
DESCRIPTOR.message_types_by_name['HelloTestReply'] = _HELLOTESTREPLY
DESCRIPTOR.message_types_by_name['TestClientRecvStreamRequest'] = _TESTCLIENTRECVSTREAMREQUEST
DESCRIPTOR.message_types_by_name['TestClientRecvStreamResponse'] = _TESTCLIENTRECVSTREAMRESPONSE
DESCRIPTOR.message_types_by_name['TestClientsendStreamRequest'] = _TESTCLIENTSENDSTREAMREQUEST
DESCRIPTOR.message_types_by_name['TestTwoWayStreamRequest'] = _TESTTWOWAYSTREAMREQUEST
DESCRIPTOR.message_types_by_name['TestClientsendStreamResponse'] = _TESTCLIENTSENDSTREAMRESPONSE
DESCRIPTOR.message_types_by_name['TestTwoWayStreamResponse'] = _TESTTWOWAYSTREAMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloDeweiReq = _reflection.GeneratedProtocolMessageType('HelloDeweiReq', (_message.Message,), {
  'DESCRIPTOR' : _HELLODEWEIREQ,
  '__module__' : 'hello_grpc1_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloDeweiReq)
  })
_sym_db.RegisterMessage(HelloDeweiReq)

HelloDeweiReply = _reflection.GeneratedProtocolMessageType('HelloDeweiReply', (_message.Message,), {

  'NumberEntry' : _reflection.GeneratedProtocolMessageType('NumberEntry', (_message.Message,), {
    'DESCRIPTOR' : _HELLODEWEIREPLY_NUMBERENTRY,
    '__module__' : 'hello_grpc1_pb2'
    # @@protoc_insertion_point(class_scope:test.HelloDeweiReply.NumberEntry)
    })
  ,

  'HelloTestReplyNunber' : _reflection.GeneratedProtocolMessageType('HelloTestReplyNunber', (_message.Message,), {
    'DESCRIPTOR' : _HELLODEWEIREPLY_HELLOTESTREPLYNUNBER,
    '__module__' : 'hello_grpc1_pb2'
    # @@protoc_insertion_point(class_scope:test.HelloDeweiReply.HelloTestReplyNunber)
    })
  ,
  'DESCRIPTOR' : _HELLODEWEIREPLY,
  '__module__' : 'hello_grpc1_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloDeweiReply)
  })
_sym_db.RegisterMessage(HelloDeweiReply)
_sym_db.RegisterMessage(HelloDeweiReply.NumberEntry)
_sym_db.RegisterMessage(HelloDeweiReply.HelloTestReplyNunber)

HelloTestReq = _reflection.GeneratedProtocolMessageType('HelloTestReq', (_message.Message,), {

  'NumberEntry' : _reflection.GeneratedProtocolMessageType('NumberEntry', (_message.Message,), {
    'DESCRIPTOR' : _HELLOTESTREQ_NUMBERENTRY,
    '__module__' : 'hello_grpc1_pb2'
    # @@protoc_insertion_point(class_scope:test.HelloTestReq.NumberEntry)
    })
  ,
  'DESCRIPTOR' : _HELLOTESTREQ,
  '__module__' : 'hello_grpc1_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloTestReq)
  })
_sym_db.RegisterMessage(HelloTestReq)
_sym_db.RegisterMessage(HelloTestReq.NumberEntry)

HelloTestReqNunber = _reflection.GeneratedProtocolMessageType('HelloTestReqNunber', (_message.Message,), {
  'DESCRIPTOR' : _HELLOTESTREQNUNBER,
  '__module__' : 'hello_grpc1_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloTestReqNunber)
  })
_sym_db.RegisterMessage(HelloTestReqNunber)

HelloTestReply = _reflection.GeneratedProtocolMessageType('HelloTestReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOTESTREPLY,
  '__module__' : 'hello_grpc1_pb2'
  # @@protoc_insertion_point(class_scope:test.HelloTestReply)
  })
_sym_db.RegisterMessage(HelloTestReply)

TestClientRecvStreamRequest = _reflection.GeneratedProtocolMessageType('TestClientRecvStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTCLIENTRECVSTREAMREQUEST,
  '__module__' : 'hello_grpc1_pb2'
  # @@protoc_insertion_point(class_scope:test.TestClientRecvStreamRequest)
  })
_sym_db.RegisterMessage(TestClientRecvStreamRequest)

TestClientRecvStreamResponse = _reflection.GeneratedProtocolMessageType('TestClientRecvStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTCLIENTRECVSTREAMRESPONSE,
  '__module__' : 'hello_grpc1_pb2'
  # @@protoc_insertion_point(class_scope:test.TestClientRecvStreamResponse)
  })
_sym_db.RegisterMessage(TestClientRecvStreamResponse)

TestClientsendStreamRequest = _reflection.GeneratedProtocolMessageType('TestClientsendStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTCLIENTSENDSTREAMREQUEST,
  '__module__' : 'hello_grpc1_pb2'
  # @@protoc_insertion_point(class_scope:test.TestClientsendStreamRequest)
  })
_sym_db.RegisterMessage(TestClientsendStreamRequest)

TestTwoWayStreamRequest = _reflection.GeneratedProtocolMessageType('TestTwoWayStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTTWOWAYSTREAMREQUEST,
  '__module__' : 'hello_grpc1_pb2'
  # @@protoc_insertion_point(class_scope:test.TestTwoWayStreamRequest)
  })
_sym_db.RegisterMessage(TestTwoWayStreamRequest)

TestClientsendStreamResponse = _reflection.GeneratedProtocolMessageType('TestClientsendStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTCLIENTSENDSTREAMRESPONSE,
  '__module__' : 'hello_grpc1_pb2'
  # @@protoc_insertion_point(class_scope:test.TestClientsendStreamResponse)
  })
_sym_db.RegisterMessage(TestClientsendStreamResponse)

TestTwoWayStreamResponse = _reflection.GeneratedProtocolMessageType('TestTwoWayStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTTWOWAYSTREAMRESPONSE,
  '__module__' : 'hello_grpc1_pb2'
  # @@protoc_insertion_point(class_scope:test.TestTwoWayStreamResponse)
  })
_sym_db.RegisterMessage(TestTwoWayStreamResponse)


_HELLODEWEIREPLY_NUMBERENTRY._options = None
_HELLOTESTREQ_NUMBERENTRY._options = None

_BILIBILI = _descriptor.ServiceDescriptor(
  name='Bilibili',
  full_name='test.Bilibili',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=837,
  serialized_end=1257,
  methods=[
  _descriptor.MethodDescriptor(
    name='HelloDewei',
    full_name='test.Bilibili.HelloDewei',
    index=0,
    containing_service=None,
    input_type=_HELLODEWEIREQ,
    output_type=_HELLODEWEIREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HelloTest',
    full_name='test.Bilibili.HelloTest',
    index=1,
    containing_service=None,
    input_type=_HELLOTESTREQ,
    output_type=_HELLOTESTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestClientRecvStream',
    full_name='test.Bilibili.TestClientRecvStream',
    index=2,
    containing_service=None,
    input_type=_TESTCLIENTRECVSTREAMREQUEST,
    output_type=_TESTCLIENTRECVSTREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestClientsendStream',
    full_name='test.Bilibili.TestClientsendStream',
    index=3,
    containing_service=None,
    input_type=_TESTCLIENTSENDSTREAMREQUEST,
    output_type=_TESTCLIENTSENDSTREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestTwoWayStream',
    full_name='test.Bilibili.TestTwoWayStream',
    index=4,
    containing_service=None,
    input_type=_TESTTWOWAYSTREAMREQUEST,
    output_type=_TESTTWOWAYSTREAMRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BILIBILI)

DESCRIPTOR.services_by_name['Bilibili'] = _BILIBILI

# @@protoc_insertion_point(module_scope)
