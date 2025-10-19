# generated from rosidl_generator_py/resource/_idl.py.em
# with input from sim_msgs:msg/HighCmd.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_HighCmd(type):
    """Metaclass of message 'HighCmd'."""

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
                'sim_msgs.msg.HighCmd')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__high_cmd
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__high_cmd
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__high_cmd
            cls._TYPE_SUPPORT = module.type_support_msg__msg__high_cmd
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__high_cmd

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class HighCmd(metaclass=Metaclass_HighCmd):
    """Message class 'HighCmd'."""

    __slots__ = [
        '_robot_id',
        '_skill',
        '_mod',
        '_tgt_x',
        '_tgt_y',
        '_tgt_theta',
    ]

    _fields_and_field_types = {
        'robot_id': 'int32',
        'skill': 'int32',
        'mod': 'int32',
        'tgt_x': 'double',
        'tgt_y': 'double',
        'tgt_theta': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.robot_id = kwargs.get('robot_id', int())
        self.skill = kwargs.get('skill', int())
        self.mod = kwargs.get('mod', int())
        self.tgt_x = kwargs.get('tgt_x', float())
        self.tgt_y = kwargs.get('tgt_y', float())
        self.tgt_theta = kwargs.get('tgt_theta', float())

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
        if self.robot_id != other.robot_id:
            return False
        if self.skill != other.skill:
            return False
        if self.mod != other.mod:
            return False
        if self.tgt_x != other.tgt_x:
            return False
        if self.tgt_y != other.tgt_y:
            return False
        if self.tgt_theta != other.tgt_theta:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def robot_id(self):
        """Message field 'robot_id'."""
        return self._robot_id

    @robot_id.setter
    def robot_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'robot_id' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'robot_id' field must be an integer in [-2147483648, 2147483647]"
        self._robot_id = value

    @builtins.property
    def skill(self):
        """Message field 'skill'."""
        return self._skill

    @skill.setter
    def skill(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'skill' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'skill' field must be an integer in [-2147483648, 2147483647]"
        self._skill = value

    @builtins.property
    def mod(self):
        """Message field 'mod'."""
        return self._mod

    @mod.setter
    def mod(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'mod' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'mod' field must be an integer in [-2147483648, 2147483647]"
        self._mod = value

    @builtins.property
    def tgt_x(self):
        """Message field 'tgt_x'."""
        return self._tgt_x

    @tgt_x.setter
    def tgt_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'tgt_x' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'tgt_x' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._tgt_x = value

    @builtins.property
    def tgt_y(self):
        """Message field 'tgt_y'."""
        return self._tgt_y

    @tgt_y.setter
    def tgt_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'tgt_y' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'tgt_y' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._tgt_y = value

    @builtins.property
    def tgt_theta(self):
        """Message field 'tgt_theta'."""
        return self._tgt_theta

    @tgt_theta.setter
    def tgt_theta(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'tgt_theta' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'tgt_theta' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._tgt_theta = value
