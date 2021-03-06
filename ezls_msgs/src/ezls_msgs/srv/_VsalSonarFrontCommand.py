"""autogenerated by genpy from ezls_msgs/VsalSonarFrontCommandRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class VsalSonarFrontCommandRequest(genpy.Message):
  _md5sum = "b7de7224f302f82ed481be66be60c6f1"
  _type = "ezls_msgs/VsalSonarFrontCommandRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """









int32 command

uint8 state
uint8 enabledGroups
uint8 group0Init
uint8 group1Init
uint8 group2Init
uint8 group3Init
uint8 group4Init
uint8 group5Init
uint8 group6Init
uint8 group7Init


"""
  __slots__ = ['command','state','enabledGroups','group0Init','group1Init','group2Init','group3Init','group4Init','group5Init','group6Init','group7Init']
  _slot_types = ['int32','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       command,state,enabledGroups,group0Init,group1Init,group2Init,group3Init,group4Init,group5Init,group6Init,group7Init

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VsalSonarFrontCommandRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.command is None:
        self.command = 0
      if self.state is None:
        self.state = 0
      if self.enabledGroups is None:
        self.enabledGroups = 0
      if self.group0Init is None:
        self.group0Init = 0
      if self.group1Init is None:
        self.group1Init = 0
      if self.group2Init is None:
        self.group2Init = 0
      if self.group3Init is None:
        self.group3Init = 0
      if self.group4Init is None:
        self.group4Init = 0
      if self.group5Init is None:
        self.group5Init = 0
      if self.group6Init is None:
        self.group6Init = 0
      if self.group7Init is None:
        self.group7Init = 0
    else:
      self.command = 0
      self.state = 0
      self.enabledGroups = 0
      self.group0Init = 0
      self.group1Init = 0
      self.group2Init = 0
      self.group3Init = 0
      self.group4Init = 0
      self.group5Init = 0
      self.group6Init = 0
      self.group7Init = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_i10B.pack(_x.command, _x.state, _x.enabledGroups, _x.group0Init, _x.group1Init, _x.group2Init, _x.group3Init, _x.group4Init, _x.group5Init, _x.group6Init, _x.group7Init))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 14
      (_x.command, _x.state, _x.enabledGroups, _x.group0Init, _x.group1Init, _x.group2Init, _x.group3Init, _x.group4Init, _x.group5Init, _x.group6Init, _x.group7Init,) = _struct_i10B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_i10B.pack(_x.command, _x.state, _x.enabledGroups, _x.group0Init, _x.group1Init, _x.group2Init, _x.group3Init, _x.group4Init, _x.group5Init, _x.group6Init, _x.group7Init))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 14
      (_x.command, _x.state, _x.enabledGroups, _x.group0Init, _x.group1Init, _x.group2Init, _x.group3Init, _x.group4Init, _x.group5Init, _x.group6Init, _x.group7Init,) = _struct_i10B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i10B = struct.Struct("<i10B")
"""autogenerated by genpy from ezls_msgs/VsalSonarFrontCommandResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class VsalSonarFrontCommandResponse(genpy.Message):
  _md5sum = "358e233cde0c8a8bcfea4ce193f8fc15"
  _type = "ezls_msgs/VsalSonarFrontCommandResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """

bool success


"""
  __slots__ = ['success']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VsalSonarFrontCommandResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
    else:
      self.success = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_B.pack(self.success))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _struct_B.unpack(str[start:end])
      self.success = bool(self.success)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_B.pack(self.success))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _struct_B.unpack(str[start:end])
      self.success = bool(self.success)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
class VsalSonarFrontCommand(object):
  _type          = 'ezls_msgs/VsalSonarFrontCommand'
  _md5sum = 'd4e541c850f92b6469d920d39979715e'
  _request_class  = VsalSonarFrontCommandRequest
  _response_class = VsalSonarFrontCommandResponse
