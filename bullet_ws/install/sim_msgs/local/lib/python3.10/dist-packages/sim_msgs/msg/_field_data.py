# generated from rosidl_generator_py/resource/_idl.py.em
# with input from sim_msgs:msg/FieldData.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FieldData(type):
    """Metaclass of message 'FieldData'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('sim_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'sim_msgs.msg.FieldData')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__field_data
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__field_data
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__field_data
            cls._TYPE_SUPPORT = module.type_support_msg__msg__field_data
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__field_data

            from sim_msgs.msg import ObjData
            if ObjData.__class__._TYPE_SUPPORT is None:
                ObjData.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class FieldData(metaclass=Metaclass_FieldData):
    """Message class 'FieldData'."""

    __slots__ = [
        '_ball',
        '_robot0',
        '_robot1',
        '_robot2',
        '_robot3',
        '_robot4',
        '_robot5',
        '_score1',
        '_score2',
    ]

    _fields_and_field_types = {
        'ball': 'sim_msgs/ObjData',
        'robot0': 'sim_msgs/ObjData',
        'robot1': 'sim_msgs/ObjData',
        'robot2': 'sim_msgs/ObjData',
        'robot3': 'sim_msgs/ObjData',
        'robot4': 'sim_msgs/ObjData',
        'robot5': 'sim_msgs/ObjData',
        'score1': 'int32',
        'score2': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['sim_msgs', 'msg'], 'ObjData'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sim_msgs', 'msg'], 'ObjData'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sim_msgs', 'msg'], 'ObjData'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sim_msgs', 'msg'], 'ObjData'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sim_msgs', 'msg'], 'ObjData'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sim_msgs', 'msg'], 'ObjData'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['sim_msgs', 'msg'], 'ObjData'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from sim_msgs.msg import ObjData
        self.ball = kwargs.get('ball', ObjData())
        from sim_msgs.msg import ObjData
        self.robot0 = kwargs.get('robot0', ObjData())
        from sim_msgs.msg import ObjData
        self.robot1 = kwargs.get('robot1', ObjData())
        from sim_msgs.msg import ObjData
        self.robot2 = kwargs.get('robot2', ObjData())
        from sim_msgs.msg import ObjData
        self.robot3 = kwargs.get('robot3', ObjData())
        from sim_msgs.msg import ObjData
        self.robot4 = kwargs.get('robot4', ObjData())
        from sim_msgs.msg import ObjData
        self.robot5 = kwargs.get('robot5', ObjData())
        self.score1 = kwargs.get('score1', int())
        self.score2 = kwargs.get('score2', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.ball != other.ball:
            return False
        if self.robot0 != other.robot0:
            return False
        if self.robot1 != other.robot1:
            return False
        if self.robot2 != other.robot2:
            return False
        if self.robot3 != other.robot3:
            return False
        if self.robot4 != other.robot4:
            return False
        if self.robot5 != other.robot5:
            return False
        if self.score1 != other.score1:
            return False
        if self.score2 != other.score2:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def ball(self):
        """Message field 'ball'."""
        return self._ball

    @ball.setter
    def ball(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'ball' field must be a sub message of type 'ObjData'"
        self._ball = value

    @builtins.property
    def robot0(self):
        """Message field 'robot0'."""
        return self._robot0

    @robot0.setter
    def robot0(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'robot0' field must be a sub message of type 'ObjData'"
        self._robot0 = value

    @builtins.property
    def robot1(self):
        """Message field 'robot1'."""
        return self._robot1

    @robot1.setter
    def robot1(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'robot1' field must be a sub message of type 'ObjData'"
        self._robot1 = value

    @builtins.property
    def robot2(self):
        """Message field 'robot2'."""
        return self._robot2

    @robot2.setter
    def robot2(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'robot2' field must be a sub message of type 'ObjData'"
        self._robot2 = value

    @builtins.property
    def robot3(self):
        """Message field 'robot3'."""
        return self._robot3

    @robot3.setter
    def robot3(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'robot3' field must be a sub message of type 'ObjData'"
        self._robot3 = value

    @builtins.property
    def robot4(self):
        """Message field 'robot4'."""
        return self._robot4

    @robot4.setter
    def robot4(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'robot4' field must be a sub message of type 'ObjData'"
        self._robot4 = value

    @builtins.property
    def robot5(self):
        """Message field 'robot5'."""
        return self._robot5

    @robot5.setter
    def robot5(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'robot5' field must be a sub message of type 'ObjData'"
        self._robot5 = value

    @builtins.property
    def score1(self):
        """Message field 'score1'."""
        return self._score1

    @score1.setter
    def score1(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'score1' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'score1' field must be an integer in [-2147483648, 2147483647]"
        self._score1 = value

    @builtins.property
    def score2(self):
        """Message field 'score2'."""
        return self._score2

    @score2.setter
    def score2(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'score2' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'score2' field must be an integer in [-2147483648, 2147483647]"
        self._score2 = value
