"""autogenerated by genpy from ezls_msgs/LmsScanlineOutput.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import ezls_msgs.msg

class LmsScanlineOutput(genpy.Message):
  _md5sum = "4c0b8e408250b4fe88cf119673bd869f"
  _type = "ezls_msgs/LmsScanlineOutput"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Output Scanlines
LmsScanline[] scanlines

================================================================================
MSG: ezls_msgs/LmsScanline
# Defines the telegram number of this scanline.
int32 telegrNumber

# Defines the count of complete auto tilt movements.
int32 autoTiltCount

# Defines movement direction of auto tilt movement. True=FromBottomToTop False=FromTopToBottom.
bool autoTiltDirUp

# Zeitstempel der Daten. Die Zeitbasis dieses Zeitstempels ist die des LMS-Serverboards.
uint32 timestamp

# Zeitstempel der Daten [in Sekunden]. Die Zeitbasis dieses Zeitstempels ist die lokalen Systems und wird bei Objekterzeugung gesetzt.
float64 localTimestamp

# Anzahl der aufgenommenen Werte.
uint32 numDistValues

# Entfernungsmaximum dieses Scans [in m].
int32 range

# Startwinkel des Schwenkvorgangs, entspricht erstem Eintrag des Arrays tiltValues[] [in rad].
float64 tiltBegin

# Endwinkel des Schwenkvorgangs, entspricht letztem Eintrag des Arrays tiltValues[] [in rad].
float64 tiltEnd

# Zeigt an, welcher der Interlace Modi verwendet wird.
int32 interlaceMode

# Offset dieser Scanline in Grad * 100 [in deg].
int32 interlaceOffset

# Gibt an, ob der Remissionsmodus aktiv ist (0=aus, 1=an).
int32 remissionMode

# Distanzwerte [in millimeter].
int32[181] distanceValues

# Tiltwerte [in rad].
float64[181] tiltValues

# Remissionswerte.
int32[181] remissionValues

# Zeigt an, ob kartesische Koordinaten fuer diese Scanline vorhanden sind.
bool hasCartesianPoints

# Kartesische Koordinaten dieser Scanline [in meter].
geometry_msgs/Vector3[181] cartesianPoints


# Correctional parameters used in cartesian coordinates transformation. //

# Winkel-Offset zwischen Laserscanner-Koordinatensystem und Welt-Koordinatensystem. Kann mit dem Tool LmsPoseCalibrator ermittelt werden.
float64 pitchOffset

# Winkel zwischen der Horizontalen und der Verbindungslinie der Koordinatensystemsurspruenge [in rad].
# 0.3723 ( entspricht: 21.33 deg / 180 deg * PI )
float64 corrAngle

# Abstand der Koordinatensystemsurspruenge [in m]. Wenn dieser Werte 0 ist wird der Korrekturterm in toCartesian() (mit corrAngle und corrDist) ignoriert.
# 191.10
float64 corrDist


================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
"""
  __slots__ = ['scanlines']
  _slot_types = ['ezls_msgs/LmsScanline[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       scanlines

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LmsScanlineOutput, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.scanlines is None:
        self.scanlines = []
    else:
      self.scanlines = []

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
      length = len(self.scanlines)
      buff.write(_struct_I.pack(length))
      for val1 in self.scanlines:
        _x = val1
        buff.write(_struct_2iBIdIi2d3i.pack(_x.telegrNumber, _x.autoTiltCount, _x.autoTiltDirUp, _x.timestamp, _x.localTimestamp, _x.numDistValues, _x.range, _x.tiltBegin, _x.tiltEnd, _x.interlaceMode, _x.interlaceOffset, _x.remissionMode))
        buff.write(_struct_181i.pack(*val1.distanceValues))
        buff.write(_struct_181d.pack(*val1.tiltValues))
        buff.write(_struct_181i.pack(*val1.remissionValues))
        buff.write(_struct_B.pack(val1.hasCartesianPoints))
        for val2 in val1.cartesianPoints:
          _x = val2
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_struct_3d.pack(_x.pitchOffset, _x.corrAngle, _x.corrDist))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.scanlines is None:
        self.scanlines = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.scanlines = []
      for i in range(0, length):
        val1 = ezls_msgs.msg.LmsScanline()
        _x = val1
        start = end
        end += 57
        (_x.telegrNumber, _x.autoTiltCount, _x.autoTiltDirUp, _x.timestamp, _x.localTimestamp, _x.numDistValues, _x.range, _x.tiltBegin, _x.tiltEnd, _x.interlaceMode, _x.interlaceOffset, _x.remissionMode,) = _struct_2iBIdIi2d3i.unpack(str[start:end])
        val1.autoTiltDirUp = bool(val1.autoTiltDirUp)
        start = end
        end += 724
        val1.distanceValues = _struct_181i.unpack(str[start:end])
        start = end
        end += 1448
        val1.tiltValues = _struct_181d.unpack(str[start:end])
        start = end
        end += 724
        val1.remissionValues = _struct_181i.unpack(str[start:end])
        start = end
        end += 1
        (val1.hasCartesianPoints,) = _struct_B.unpack(str[start:end])
        val1.hasCartesianPoints = bool(val1.hasCartesianPoints)
        val1.cartesianPoints = []
        for i in range(0, 181):
          val2 = geometry_msgs.msg.Vector3()
          _x = val2
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          val1.cartesianPoints.append(val2)
        _x = val1
        start = end
        end += 24
        (_x.pitchOffset, _x.corrAngle, _x.corrDist,) = _struct_3d.unpack(str[start:end])
        self.scanlines.append(val1)
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
      length = len(self.scanlines)
      buff.write(_struct_I.pack(length))
      for val1 in self.scanlines:
        _x = val1
        buff.write(_struct_2iBIdIi2d3i.pack(_x.telegrNumber, _x.autoTiltCount, _x.autoTiltDirUp, _x.timestamp, _x.localTimestamp, _x.numDistValues, _x.range, _x.tiltBegin, _x.tiltEnd, _x.interlaceMode, _x.interlaceOffset, _x.remissionMode))
        buff.write(val1.distanceValues.tostring())
        buff.write(val1.tiltValues.tostring())
        buff.write(val1.remissionValues.tostring())
        buff.write(_struct_B.pack(val1.hasCartesianPoints))
        for val2 in val1.cartesianPoints:
          _x = val2
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_struct_3d.pack(_x.pitchOffset, _x.corrAngle, _x.corrDist))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.scanlines is None:
        self.scanlines = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.scanlines = []
      for i in range(0, length):
        val1 = ezls_msgs.msg.LmsScanline()
        _x = val1
        start = end
        end += 57
        (_x.telegrNumber, _x.autoTiltCount, _x.autoTiltDirUp, _x.timestamp, _x.localTimestamp, _x.numDistValues, _x.range, _x.tiltBegin, _x.tiltEnd, _x.interlaceMode, _x.interlaceOffset, _x.remissionMode,) = _struct_2iBIdIi2d3i.unpack(str[start:end])
        val1.autoTiltDirUp = bool(val1.autoTiltDirUp)
        start = end
        end += 724
        val1.distanceValues = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=181)
        start = end
        end += 1448
        val1.tiltValues = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=181)
        start = end
        end += 724
        val1.remissionValues = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=181)
        start = end
        end += 1
        (val1.hasCartesianPoints,) = _struct_B.unpack(str[start:end])
        val1.hasCartesianPoints = bool(val1.hasCartesianPoints)
        val1.cartesianPoints = []
        for i in range(0, 181):
          val2 = geometry_msgs.msg.Vector3()
          _x = val2
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          val1.cartesianPoints.append(val2)
        _x = val1
        start = end
        end += 24
        (_x.pitchOffset, _x.corrAngle, _x.corrDist,) = _struct_3d.unpack(str[start:end])
        self.scanlines.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_181d = struct.Struct("<181d")
_struct_B = struct.Struct("<B")
_struct_2iBIdIi2d3i = struct.Struct("<2iBIdIi2d3i")
_struct_181i = struct.Struct("<181i")
_struct_3d = struct.Struct("<3d")
