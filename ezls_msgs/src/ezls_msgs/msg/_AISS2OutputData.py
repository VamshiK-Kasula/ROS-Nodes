"""autogenerated by genpy from ezls_msgs/AISS2OutputData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ezls_msgs.msg

class AISS2OutputData(genpy.Message):
  _md5sum = "3c5c9a124c800c7cc5e8dfa8364e6f79"
  _type = "ezls_msgs/AISS2OutputData"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """IMURawData[] data_vector

================================================================================
MSG: ezls_msgs/IMURawData
uint32 timestamp

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
  __slots__ = ['data_vector']
  _slot_types = ['ezls_msgs/IMURawData[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       data_vector

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AISS2OutputData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.data_vector is None:
        self.data_vector = []
    else:
      self.data_vector = []

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
      length = len(self.data_vector)
      buff.write(_struct_I.pack(length))
      for val1 in self.data_vector:
        buff.write(_struct_I.pack(val1.timestamp))
        for val2 in val1.accSens:
          _x = val2
          buff.write(_struct_7i.pack(_x.vcc, _x.acc_x, _x.acc_y, _x.temp, _x.roll, _x.pitch, _x.state))
        for val2 in val1.gyrSens:
          _x = val2
          buff.write(_struct_2i.pack(_x.rot, _x.temp))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.data_vector is None:
        self.data_vector = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data_vector = []
      for i in range(0, length):
        val1 = ezls_msgs.msg.IMURawData()
        start = end
        end += 4
        (val1.timestamp,) = _struct_I.unpack(str[start:end])
        val1.accSens = []
        for i in range(0, 2):
          val2 = ezls_msgs.msg.ADIS16201RawData()
          _x = val2
          start = end
          end += 28
          (_x.vcc, _x.acc_x, _x.acc_y, _x.temp, _x.roll, _x.pitch, _x.state,) = _struct_7i.unpack(str[start:end])
          val1.accSens.append(val2)
        val1.gyrSens = []
        for i in range(0, 3):
          val2 = ezls_msgs.msg.ADIS16100RawData()
          _x = val2
          start = end
          end += 8
          (_x.rot, _x.temp,) = _struct_2i.unpack(str[start:end])
          val1.gyrSens.append(val2)
        self.data_vector.append(val1)
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
      length = len(self.data_vector)
      buff.write(_struct_I.pack(length))
      for val1 in self.data_vector:
        buff.write(_struct_I.pack(val1.timestamp))
        for val2 in val1.accSens:
          _x = val2
          buff.write(_struct_7i.pack(_x.vcc, _x.acc_x, _x.acc_y, _x.temp, _x.roll, _x.pitch, _x.state))
        for val2 in val1.gyrSens:
          _x = val2
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
      if self.data_vector is None:
        self.data_vector = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data_vector = []
      for i in range(0, length):
        val1 = ezls_msgs.msg.IMURawData()
        start = end
        end += 4
        (val1.timestamp,) = _struct_I.unpack(str[start:end])
        val1.accSens = []
        for i in range(0, 2):
          val2 = ezls_msgs.msg.ADIS16201RawData()
          _x = val2
          start = end
          end += 28
          (_x.vcc, _x.acc_x, _x.acc_y, _x.temp, _x.roll, _x.pitch, _x.state,) = _struct_7i.unpack(str[start:end])
          val1.accSens.append(val2)
        val1.gyrSens = []
        for i in range(0, 3):
          val2 = ezls_msgs.msg.ADIS16100RawData()
          _x = val2
          start = end
          end += 8
          (_x.rot, _x.temp,) = _struct_2i.unpack(str[start:end])
          val1.gyrSens.append(val2)
        self.data_vector.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2i = struct.Struct("<2i")
_struct_7i = struct.Struct("<7i")
