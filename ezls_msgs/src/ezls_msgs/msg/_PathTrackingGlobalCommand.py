"""autogenerated by genpy from ezls_msgs/PathTrackingGlobalCommand.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import ezls_msgs.msg

class PathTrackingGlobalCommand(genpy.Message):
  _md5sum = "93996e017eb4a0dffa8a875d8d1275aa"
  _type = "ezls_msgs/PathTrackingGlobalCommand"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Timestamp of command
float64 timestamp

# Command ID
int32 command

# Number of waypoints in waypoint array
int32 numWaypoints

# Waypoint array
ezls_msgs/GlobalWaypoint3[] waypoints

================================================================================
MSG: ezls_msgs/GlobalWaypoint3
# Pose3 of waypoint
ezls_msgs/Pose3 pose

# ID of waypoint
int32 id

# Type of waypoint
uint32 type

# Is waypoint reached
bool reached

# Distance to be reached
float64 reachingDistance

#Event number
int32 event


================================================================================
MSG: ezls_msgs/Pose3
geometry_msgs/Vector3 position
geometry_msgs/Vector3 orientation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
"""
  __slots__ = ['timestamp','command','numWaypoints','waypoints']
  _slot_types = ['float64','int32','int32','ezls_msgs/GlobalWaypoint3[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp,command,numWaypoints,waypoints

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PathTrackingGlobalCommand, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timestamp is None:
        self.timestamp = 0.
      if self.command is None:
        self.command = 0
      if self.numWaypoints is None:
        self.numWaypoints = 0
      if self.waypoints is None:
        self.waypoints = []
    else:
      self.timestamp = 0.
      self.command = 0
      self.numWaypoints = 0
      self.waypoints = []

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
      buff.write(_struct_d2i.pack(_x.timestamp, _x.command, _x.numWaypoints))
      length = len(self.waypoints)
      buff.write(_struct_I.pack(length))
      for val1 in self.waypoints:
        _v1 = val1.pose
        _v2 = _v1.position
        _x = _v2
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v3 = _v1.orientation
        _x = _v3
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_struct_iIBdi.pack(_x.id, _x.type, _x.reached, _x.reachingDistance, _x.event))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.waypoints is None:
        self.waypoints = None
      end = 0
      _x = self
      start = end
      end += 16
      (_x.timestamp, _x.command, _x.numWaypoints,) = _struct_d2i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.waypoints = []
      for i in range(0, length):
        val1 = ezls_msgs.msg.GlobalWaypoint3()
        _v4 = val1.pose
        _v5 = _v4.position
        _x = _v5
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v6 = _v4.orientation
        _x = _v6
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _x = val1
        start = end
        end += 21
        (_x.id, _x.type, _x.reached, _x.reachingDistance, _x.event,) = _struct_iIBdi.unpack(str[start:end])
        val1.reached = bool(val1.reached)
        self.waypoints.append(val1)
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
      buff.write(_struct_d2i.pack(_x.timestamp, _x.command, _x.numWaypoints))
      length = len(self.waypoints)
      buff.write(_struct_I.pack(length))
      for val1 in self.waypoints:
        _v7 = val1.pose
        _v8 = _v7.position
        _x = _v8
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v9 = _v7.orientation
        _x = _v9
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_struct_iIBdi.pack(_x.id, _x.type, _x.reached, _x.reachingDistance, _x.event))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.waypoints is None:
        self.waypoints = None
      end = 0
      _x = self
      start = end
      end += 16
      (_x.timestamp, _x.command, _x.numWaypoints,) = _struct_d2i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.waypoints = []
      for i in range(0, length):
        val1 = ezls_msgs.msg.GlobalWaypoint3()
        _v10 = val1.pose
        _v11 = _v10.position
        _x = _v11
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v12 = _v10.orientation
        _x = _v12
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _x = val1
        start = end
        end += 21
        (_x.id, _x.type, _x.reached, _x.reachingDistance, _x.event,) = _struct_iIBdi.unpack(str[start:end])
        val1.reached = bool(val1.reached)
        self.waypoints.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_d2i = struct.Struct("<d2i")
_struct_iIBdi = struct.Struct("<iIBdi")
_struct_3d = struct.Struct("<3d")
