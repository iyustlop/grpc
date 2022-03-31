# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sales_records.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sales_records.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13sales_records.proto\"\r\n\x0b\x45mptyMesage\"\'\n\x18PingSalesRecordsResponse\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\t2K\n\x0cSalesRecords\x12;\n\x10PingSalesRecords\x12\x0c.EmptyMesage\x1a\x19.PingSalesRecordsResponseb\x06proto3'
)




_EMPTYMESAGE = _descriptor.Descriptor(
  name='EmptyMesage',
  full_name='EmptyMesage',
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
  serialized_start=23,
  serialized_end=36,
)


_PINGSALESRECORDSRESPONSE = _descriptor.Descriptor(
  name='PingSalesRecordsResponse',
  full_name='PingSalesRecordsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='PingSalesRecordsResponse.ack', index=0,
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
  serialized_start=38,
  serialized_end=77,
)

DESCRIPTOR.message_types_by_name['EmptyMesage'] = _EMPTYMESAGE
DESCRIPTOR.message_types_by_name['PingSalesRecordsResponse'] = _PINGSALESRECORDSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyMesage = _reflection.GeneratedProtocolMessageType('EmptyMesage', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYMESAGE,
  '__module__' : 'sales_records_pb2'
  # @@protoc_insertion_point(class_scope:EmptyMesage)
  })
_sym_db.RegisterMessage(EmptyMesage)

PingSalesRecordsResponse = _reflection.GeneratedProtocolMessageType('PingSalesRecordsResponse', (_message.Message,), {
  'DESCRIPTOR' : _PINGSALESRECORDSRESPONSE,
  '__module__' : 'sales_records_pb2'
  # @@protoc_insertion_point(class_scope:PingSalesRecordsResponse)
  })
_sym_db.RegisterMessage(PingSalesRecordsResponse)



_SALESRECORDS = _descriptor.ServiceDescriptor(
  name='SalesRecords',
  full_name='SalesRecords',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=79,
  serialized_end=154,
  methods=[
  _descriptor.MethodDescriptor(
    name='PingSalesRecords',
    full_name='SalesRecords.PingSalesRecords',
    index=0,
    containing_service=None,
    input_type=_EMPTYMESAGE,
    output_type=_PINGSALESRECORDSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SALESRECORDS)

DESCRIPTOR.services_by_name['SalesRecords'] = _SALESRECORDS

# @@protoc_insertion_point(module_scope)
