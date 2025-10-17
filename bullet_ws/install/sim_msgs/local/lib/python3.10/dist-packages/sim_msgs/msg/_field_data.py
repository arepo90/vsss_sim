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
        '_team0',
        '_team1',
        '_team2',
        '_op0',
        '_op1',
        '_op2',
        '_score1',
        '_score2',
    ]

    _fields_and_field_types = {
        'ball': 'sim_msgs/ObjData',
        'team0': 'sim_msgs/ObjData',
        'team1': 'sim_msgs/ObjData',
        'team2': 'sim_msgs/ObjData',
        'op0': 'sim_msgs/ObjData',
        'op1': 'sim_msgs/ObjData',
        'op2': 'sim_msgs/ObjData',
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
        self.team0 = kwargs.get('team0', ObjData())
        from sim_msgs.msg import ObjData
        self.team1 = kwargs.get('team1', ObjData())
        from sim_msgs.msg import ObjData
        self.team2 = kwargs.get('team2', ObjData())
        from sim_msgs.msg import ObjData
        self.op0 = kwargs.get('op0', ObjData())
        from sim_msgs.msg import ObjData
        self.op1 = kwargs.get('op1', ObjData())
        from sim_msgs.msg import ObjData
        self.op2 = kwargs.get('op2', ObjData())
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
        if self.team0 != other.team0:
            return False
        if self.team1 != other.team1:
            return False
        if self.team2 != other.team2:
            return False
        if self.op0 != other.op0:
            return False
        if self.op1 != other.op1:
            return False
        if self.op2 != other.op2:
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
    def team0(self):
        """Message field 'team0'."""
        return self._team0

    @team0.setter
    def team0(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'team0' field must be a sub message of type 'ObjData'"
        self._team0 = value

    @builtins.property
    def team1(self):
        """Message field 'team1'."""
        return self._team1

    @team1.setter
    def team1(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'team1' field must be a sub message of type 'ObjData'"
        self._team1 = value

    @builtins.property
    def team2(self):
        """Message field 'team2'."""
        return self._team2

    @team2.setter
    def team2(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'team2' field must be a sub message of type 'ObjData'"
        self._team2 = value

    @builtins.property
    def op0(self):
        """Message field 'op0'."""
        return self._op0

    @op0.setter
    def op0(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'op0' field must be a sub message of type 'ObjData'"
        self._op0 = value

    @builtins.property
    def op1(self):
        """Message field 'op1'."""
        return self._op1

    @op1.setter
    def op1(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'op1' field must be a sub message of type 'ObjData'"
        self._op1 = value

    @builtins.property
    def op2(self):
        """Message field 'op2'."""
        return self._op2

    @op2.setter
    def op2(self, value):
        if __debug__:
            from sim_msgs.msg import ObjData
            assert \
                isinstance(value, ObjData), \
                "The 'op2' field must be a sub message of type 'ObjData'"
        self._op2 = value

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
