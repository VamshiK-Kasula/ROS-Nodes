"""autogenerated by genpy from ezls_msgs/Event_SrvRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ezls_msgs.msg

class Event_SrvRequest(genpy.Message):
  _md5sum = "de7fc5e3818cc03b3a6d919b27ecb095"
  _type = "ezls_msgs/Event_SrvRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """ezls_msgs/Event event

================================================================================
MSG: ezls_msgs/Event
# ID of this event.
uint32 id

# Timestamp of this event [in seconds].
float64 timestamp

# Indicates if this event is addressed to a specific group.
bool isAddressed

# ID of the adressed group.
uint32 addressee

# Priority of this event.
int32 priority

# Satisfaction data structure [at the moment only a floating point value].
float64 satisfaction

"""
  __slots__ = ['event']
  _slot_types = ['ezls_msgs/Event']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       event

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Event_SrvRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.event is None:
        self.event = ezls_msgs.msg.Event()
    else:
      self.event = ezls_msgs.msg.Event()

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
      buff.write(_struct_IdBIid.pack(_x.event.id, _x.event.timestamp, _x.event.isAddressed, _x.event.addressee, _x.event.priority, _x.event.satisfaction))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.event is None:
        self.event = ezls_msgs.msg.Event()
      end = 0
      _x = self
      start = end
      end += 29
      (_x.event.id, _x.event.timestamp, _x.event.isAddressed, _x.event.addressee, _x.event.priority, _x.event.satisfaction,) = _struct_IdBIid.unpack(str[start:end])
      self.event.isAddressed = bool(self.event.isAddressed)
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
      buff.write(_struct_IdBIid.pack(_x.event.id, _x.event.timestamp, _x.event.isAddressed, _x.event.addressee, _x.event.priority, _x.event.satisfaction))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.event is None:
        self.event = ezls_msgs.msg.Event()
      end = 0
      _x = self
      start = end
      end += 29
      (_x.event.id, _x.event.timestamp, _x.event.isAddressed, _x.event.addressee, _x.event.priority, _x.event.satisfaction,) = _struct_IdBIid.unpack(str[start:end])
      self.event.isAddressed = bool(self.event.isAddressed)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_IdBIid = struct.Struct("<IdBIid")
"""autogenerated by genpy from ezls_msgs/Event_SrvResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Event_SrvResponse(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "ezls_msgs/Event_SrvResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """


"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Event_SrvResponse, self).__init__(*args, **kwds)

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
      pass
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
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
      pass
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
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
class Event_Srv(object):
  _type          = 'ezls_msgs/Event_Srv'
  _md5sum = 'de7fc5e3818cc03b3a6d919b27ecb095'
  _request_class  = Event_SrvRequest
  _response_class = Event_SrvResponse
