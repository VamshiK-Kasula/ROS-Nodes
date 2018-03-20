"""autogenerated by genpy from ezls_msgs/LocalObstacleAvoidanceInputData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class LocalObstacleAvoidanceInputData(genpy.Message):
  _md5sum = "74b0c754b31b23a12fa22fa1727c93cb"
  _type = "ezls_msgs/LocalObstacleAvoidanceInputData"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header

# reference yaw [rad] in [-pi, pi]
float64 reference_path_yaw
# reference speed [m/s]
float64 reference_speed

# current (measured) steering-yaw [rad] in [-pi, pi]
float64 current_path_yaw
# robot's current speed [m/s]
float64 current_speed

# The requested direction of travel: 1 == forwards; -1 == backwards
int8 reference_direction

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['header','reference_path_yaw','reference_speed','current_path_yaw','current_speed','reference_direction']
  _slot_types = ['std_msgs/Header','float64','float64','float64','float64','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,reference_path_yaw,reference_speed,current_path_yaw,current_speed,reference_direction

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LocalObstacleAvoidanceInputData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.reference_path_yaw is None:
        self.reference_path_yaw = 0.
      if self.reference_speed is None:
        self.reference_speed = 0.
      if self.current_path_yaw is None:
        self.current_path_yaw = 0.
      if self.current_speed is None:
        self.current_speed = 0.
      if self.reference_direction is None:
        self.reference_direction = 0
    else:
      self.header = std_msgs.msg.Header()
      self.reference_path_yaw = 0.
      self.reference_speed = 0.
      self.current_path_yaw = 0.
      self.current_speed = 0.
      self.reference_direction = 0

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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4db.pack(_x.reference_path_yaw, _x.reference_speed, _x.current_path_yaw, _x.current_speed, _x.reference_direction))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 33
      (_x.reference_path_yaw, _x.reference_speed, _x.current_path_yaw, _x.current_speed, _x.reference_direction,) = _struct_4db.unpack(str[start:end])
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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_4db.pack(_x.reference_path_yaw, _x.reference_speed, _x.current_path_yaw, _x.current_speed, _x.reference_direction))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 33
      (_x.reference_path_yaw, _x.reference_speed, _x.current_path_yaw, _x.current_speed, _x.reference_direction,) = _struct_4db.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4db = struct.Struct("<4db")
_struct_3I = struct.Struct("<3I")
