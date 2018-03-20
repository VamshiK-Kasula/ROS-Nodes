"""autogenerated by genpy from ezls_msgs/LMS_Command_SrvRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class LMS_Command_SrvRequest(genpy.Message):
  _md5sum = "a39970ddbef246cff37cfbb74e29d234"
  _type = "ezls_msgs/LMS_Command_SrvRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 timestamp



int32 command







int32 resolution

int32 range

int32 remissionMode

float64 tilt
float64 speed


int32 time
float64 minTilt
float64 maxTilt




int32[] minDistances



"""
  __slots__ = ['timestamp','command','resolution','range','remissionMode','tilt','speed','time','minTilt','maxTilt','minDistances']
  _slot_types = ['float64','int32','int32','int32','int32','float64','float64','int32','float64','float64','int32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timestamp,command,resolution,range,remissionMode,tilt,speed,time,minTilt,maxTilt,minDistances

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LMS_Command_SrvRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timestamp is None:
        self.timestamp = 0.
      if self.command is None:
        self.command = 0
      if self.resolution is None:
        self.resolution = 0
      if self.range is None:
        self.range = 0
      if self.remissionMode is None:
        self.remissionMode = 0
      if self.tilt is None:
        self.tilt = 0.
      if self.speed is None:
        self.speed = 0.
      if self.time is None:
        self.time = 0
      if self.minTilt is None:
        self.minTilt = 0.
      if self.maxTilt is None:
        self.maxTilt = 0.
      if self.minDistances is None:
        self.minDistances = []
    else:
      self.timestamp = 0.
      self.command = 0
      self.resolution = 0
      self.range = 0
      self.remissionMode = 0
      self.tilt = 0.
      self.speed = 0.
      self.time = 0
      self.minTilt = 0.
      self.maxTilt = 0.
      self.minDistances = []

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
      buff.write(_struct_d4i2di2d.pack(_x.timestamp, _x.command, _x.resolution, _x.range, _x.remissionMode, _x.tilt, _x.speed, _x.time, _x.minTilt, _x.maxTilt))
      length = len(self.minDistances)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.minDistances))
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
      end += 60
      (_x.timestamp, _x.command, _x.resolution, _x.range, _x.remissionMode, _x.tilt, _x.speed, _x.time, _x.minTilt, _x.maxTilt,) = _struct_d4i2di2d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.minDistances = struct.unpack(pattern, str[start:end])
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
      buff.write(_struct_d4i2di2d.pack(_x.timestamp, _x.command, _x.resolution, _x.range, _x.remissionMode, _x.tilt, _x.speed, _x.time, _x.minTilt, _x.maxTilt))
      length = len(self.minDistances)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.minDistances.tostring())
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
      end += 60
      (_x.timestamp, _x.command, _x.resolution, _x.range, _x.remissionMode, _x.tilt, _x.speed, _x.time, _x.minTilt, _x.maxTilt,) = _struct_d4i2di2d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.minDistances = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_d4i2di2d = struct.Struct("<d4i2di2d")
"""autogenerated by genpy from ezls_msgs/LMS_Command_SrvResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ezls_msgs.msg

class LMS_Command_SrvResponse(genpy.Message):
  _md5sum = "a8aecbf5ffbb09949fc62be436a64c66"
  _type = "ezls_msgs/LMS_Command_SrvResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """


float64 tilt


float64 minTilt


float64 maxTilt


int32[] minDistances


LmsConfiguration configuration



bool success


================================================================================
MSG: ezls_msgs/LmsConfiguration
# IP address of laser scanner.
string address

#IP port of laser scanner.
string port

# Type of laser scanner.
uint8 type

# Height over ground of the laser scanner coordinate system [in m].
float64 heightOverGround

# Correctional parameters used in cartesian coordinates transformation. //
# Winkel-Offset zwischen Laserscanner-Koordinatensystem und Welt-Koordinatensystem. Kann mit dem Tool LmsPoseCalibrator ermittelt werden.
float64 pitchOffset

# Winkel zwischen der Horizontalen und der Verbindungslinie der Koordinatensystemsurspruenge [in rad].
# 0.3723 ( entspricht: 21.33 deg / 180 deg * PI )
float64 corrAngle

# Abstand der Koordinatensystemsurspruenge [in m]. Wenn dieser Werte 0 ist wird der Korrekturterm in toCartesian() (mit corrAngle und corrDist) ignoriert.
# 191.10
float64 corrDist



"""
  __slots__ = ['tilt','minTilt','maxTilt','minDistances','configuration','success']
  _slot_types = ['float64','float64','float64','int32[]','ezls_msgs/LmsConfiguration','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       tilt,minTilt,maxTilt,minDistances,configuration,success

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LMS_Command_SrvResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.tilt is None:
        self.tilt = 0.
      if self.minTilt is None:
        self.minTilt = 0.
      if self.maxTilt is None:
        self.maxTilt = 0.
      if self.minDistances is None:
        self.minDistances = []
      if self.configuration is None:
        self.configuration = ezls_msgs.msg.LmsConfiguration()
      if self.success is None:
        self.success = False
    else:
      self.tilt = 0.
      self.minTilt = 0.
      self.maxTilt = 0.
      self.minDistances = []
      self.configuration = ezls_msgs.msg.LmsConfiguration()
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
      _x = self
      buff.write(_struct_3d.pack(_x.tilt, _x.minTilt, _x.maxTilt))
      length = len(self.minDistances)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.minDistances))
      _x = self.configuration.address
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.configuration.port
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B4dB.pack(_x.configuration.type, _x.configuration.heightOverGround, _x.configuration.pitchOffset, _x.configuration.corrAngle, _x.configuration.corrDist, _x.success))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.configuration is None:
        self.configuration = ezls_msgs.msg.LmsConfiguration()
      end = 0
      _x = self
      start = end
      end += 24
      (_x.tilt, _x.minTilt, _x.maxTilt,) = _struct_3d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.minDistances = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.configuration.address = str[start:end].decode('utf-8')
      else:
        self.configuration.address = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.configuration.port = str[start:end].decode('utf-8')
      else:
        self.configuration.port = str[start:end]
      _x = self
      start = end
      end += 34
      (_x.configuration.type, _x.configuration.heightOverGround, _x.configuration.pitchOffset, _x.configuration.corrAngle, _x.configuration.corrDist, _x.success,) = _struct_B4dB.unpack(str[start:end])
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
      _x = self
      buff.write(_struct_3d.pack(_x.tilt, _x.minTilt, _x.maxTilt))
      length = len(self.minDistances)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.minDistances.tostring())
      _x = self.configuration.address
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.configuration.port
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B4dB.pack(_x.configuration.type, _x.configuration.heightOverGround, _x.configuration.pitchOffset, _x.configuration.corrAngle, _x.configuration.corrDist, _x.success))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.configuration is None:
        self.configuration = ezls_msgs.msg.LmsConfiguration()
      end = 0
      _x = self
      start = end
      end += 24
      (_x.tilt, _x.minTilt, _x.maxTilt,) = _struct_3d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.minDistances = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.configuration.address = str[start:end].decode('utf-8')
      else:
        self.configuration.address = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.configuration.port = str[start:end].decode('utf-8')
      else:
        self.configuration.port = str[start:end]
      _x = self
      start = end
      end += 34
      (_x.configuration.type, _x.configuration.heightOverGround, _x.configuration.pitchOffset, _x.configuration.corrAngle, _x.configuration.corrDist, _x.success,) = _struct_B4dB.unpack(str[start:end])
      self.success = bool(self.success)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B4dB = struct.Struct("<B4dB")
_struct_3d = struct.Struct("<3d")
class LMS_Command_Srv(object):
  _type          = 'ezls_msgs/LMS_Command_Srv'
  _md5sum = 'c4128860268fe0526061e76ec24f445e'
  _request_class  = LMS_Command_SrvRequest
  _response_class = LMS_Command_SrvResponse