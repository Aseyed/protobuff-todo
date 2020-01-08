# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo/todo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todo/todo.proto',
  package='todo',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0ftodo/todo.proto\x12\x04todo\"\"\n\x04Task\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0c\n\x04\x64one\x18\x02 \x01(\x08\"%\n\x08TaskList\x12\x19\n\x05tasks\x18\x01 \x03(\x0b\x32\n.todo.Task\"\x14\n\x04Text\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x06\n\x04Void2N\n\x05Tasks\x12$\n\x04List\x12\n.todo.Void\x1a\x0e.todo.TaskList\"\x00\x12\x1f\n\x03\x41\x64\x64\x12\n.todo.Text\x1a\n.todo.Task\"\x00\x62\x06proto3')
)




_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='todo.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='todo.Task.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='done', full_name='todo.Task.done', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=25,
  serialized_end=59,
)


_TASKLIST = _descriptor.Descriptor(
  name='TaskList',
  full_name='todo.TaskList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='todo.TaskList.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=61,
  serialized_end=98,
)


_TEXT = _descriptor.Descriptor(
  name='Text',
  full_name='todo.Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='todo.Text.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=100,
  serialized_end=120,
)


_VOID = _descriptor.Descriptor(
  name='Void',
  full_name='todo.Void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=122,
  serialized_end=128,
)

_TASKLIST.fields_by_name['tasks'].message_type = _TASK
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['TaskList'] = _TASKLIST
DESCRIPTOR.message_types_by_name['Text'] = _TEXT
DESCRIPTOR.message_types_by_name['Void'] = _VOID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'todo.todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.Task)
  })
_sym_db.RegisterMessage(Task)

TaskList = _reflection.GeneratedProtocolMessageType('TaskList', (_message.Message,), {
  'DESCRIPTOR' : _TASKLIST,
  '__module__' : 'todo.todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.TaskList)
  })
_sym_db.RegisterMessage(TaskList)

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), {
  'DESCRIPTOR' : _TEXT,
  '__module__' : 'todo.todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.Text)
  })
_sym_db.RegisterMessage(Text)

Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), {
  'DESCRIPTOR' : _VOID,
  '__module__' : 'todo.todo_pb2'
  # @@protoc_insertion_point(class_scope:todo.Void)
  })
_sym_db.RegisterMessage(Void)



_TASKS = _descriptor.ServiceDescriptor(
  name='Tasks',
  full_name='todo.Tasks',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=130,
  serialized_end=208,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='todo.Tasks.List',
    index=0,
    containing_service=None,
    input_type=_VOID,
    output_type=_TASKLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Add',
    full_name='todo.Tasks.Add',
    index=1,
    containing_service=None,
    input_type=_TEXT,
    output_type=_TASK,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TASKS)

DESCRIPTOR.services_by_name['Tasks'] = _TASKS

# @@protoc_insertion_point(module_scope)