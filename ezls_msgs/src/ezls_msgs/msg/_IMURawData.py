"""autogenerated by genpy from ezls_msgs/IMURawData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ezls_msgs.msg

class IMURawData(genpy.Message):
  _md5sum = "5901965d914e0bc7cb8eb617f1e4263c"
  _type = "ezls_msgs/IMURawData"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint32 timestamp

ADIS16201RawData[2] accSens
ADIS16100RawData[3] gyrSens

================================================================================
MSG: ezls_msgs/ADIS16201RawData
int32 vcc
int32 acc_x
int32 acc_y
int32 temp
int32 roll
int32 pitch
int32 state

================================================================================
MSG: ezls_msgs/ADIS16100RawData
int32 rot
int32 temp

"""
  __slots__ = ['timestamp','accSens','gyrSens']
  _slot_types = ['uint32','ezls_msgs/ADIS16201RawData[2]','ezls_msgs/ADIS16100RawData[3]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp,accSens,gyrSens

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(IMURawData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timestamp is None:
        self.timestamp = 0
      if self.accSens is None:
        self.accSens = [ezls_msgs.msg.ADIS16201RawData(),ezls_msgs.msg.ADIS16201RawData()]
      if self.gyrSens is None:
        self.gyrSens = [ezls_msgs.msg.ADIS16100RawData(),ezls_msgs.msg.ADIS16100RawData(),ezls_msgs.msg.ADIS16100RawData()]
    else:
      self.timestamp = 0
      self.accSens = [ezls_msgs.msg.ADIS16201RawData(),ezls_msgs.msg.ADIS16201RawData()]
      self.gyrSens = [ezls_msgs.msg.ADIS16100RawData(),ezls_msgs.msg.ADIS16100RawData(),ezls_msgs.msg.ADIS16100RawData()]

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
      buff.write(_struct_I.pack(self.timestamp))
      for val1 in self.accSens:
        _x = val1
        buff.write(_struct_7i.pack(_x.vcc, _x.acc_x, _x.acc_y, _x.temp, _x.roll, _x.pitch, _x.state))
      for val1 in self.gyrSens:
        _x = val1
        buff.write(_struct_2i.pack(_x.rot, _x.temp))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.accSens is None:
        self.accSens = None
      if self.gyrSens is None:
        self.gyrSens = None
      end = 0
      start = end
      end += 4
      (self.timestamp,) = _struct_I.unpack(str[start:end])
      self.accSens = []
      for i in range(0, 2):
        val1 = ezls_msgs.msg.ADIS16201RawData()
        _x = val1
        start = end
        end += 28
        (_x.vcc, _x.acc_x, _x.acc_y, _x.temp, _x.roll, _x.pitch, _x.state,) = _struct_7i.unpack(str[start:end])
        self.accSens.append(val1)
      self.gyrSens = []
      for i in range(0, 3):
        val1 = ezls_msgs.msg.ADIS16100RawData()
        _x = val1
        start = end
        end += 8
        (_x.rot, _x.temp,) = _struct_2i.unpack(str[start:end])
        self.gyrSens.append(val1)
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
      buff.write(_struct_I.pack(self.timestamp))
      for val1 in self.accSens:
        _x = val1
        buff.write(_struct_7i.pack(_x.vcc, _x.acc_x, _x.acc_y, _x.temp, _x.roll, _x.pitch, _x.state))
      for val1 in self.gyrSens:
        _x = val1
        buff.write(_struct_2i.pack(_x.rot, _x.temp))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.accSens is None:
        self.accSens = None
      if self.gyrSens is None:
        self.gyrSens = None
      end = 0
      start = end
      end += 4
      (self.timestamp,) = _struct_I.unpack(str[start:end])
      self.accSens = []
      for i in range(0, 2):
        val1 = ezls_msgs.msg.ADIS16201RawData()
        _x = val1
        start = end
        end += 28
        (_x.vcc, _x.acc_x, _x.acc_y, _x.temp, _x.roll, _x.pitch, _x.state,) = _struct_7i.unpack(str[start:end])
        self.accSens.append(val1)
      self.gyrSens = []
      for i in range(0, 3):
        val1 = ezls_msgs.msg.ADIS16100RawData()
        _x = val1
        start = end
        end += 8
        (_x.rot, _x.temp,) = _struct_2i.unpack(str[start:end])
        self.gyrSens.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2i = struct.Struct("<2i")
_struct_7i = struct.Struct("<7i")
