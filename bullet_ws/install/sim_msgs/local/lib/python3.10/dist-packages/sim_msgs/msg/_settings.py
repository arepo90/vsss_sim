# generated from rosidl_generator_py/resource/_idl.py.em
# with input from sim_msgs:msg/Settings.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Settings(type):
    """Metaclass of message 'Settings'."""

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
                'sim_msgs.msg.Settings')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__settings
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__settings
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__settings
            cls._TYPE_SUPPORT = module.type_support_msg__msg__settings
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__settings

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Settings(metaclass=Metaclass_Settings):
    """Message class 'Settings'."""

    __slots__ = [
        '_team_color',
        '_team_side',
        '_local',
        '_reset',
        '_exposure',
        '_robot0',
        '_robot1',
        '_robot2',
        '_attractive_gain',
        '_repulsive_gain',
        '_repulsion_radius',
        '_goal_tolerance',
        '_tangential_gain',
    ]

    _fields_and_field_types = {
        'team_color': 'boolean',
        'team_side': 'boolean',
        'local': 'boolean',
        'reset': 'boolean',
        'exposure': 'int32',
        'robot0': 'int32',
        'robot1': 'int32',
        'robot2': 'int32',
        'attractive_gain': 'double',
        'repulsive_gain': 'double',
        'repulsion_radius': 'double',
        'goal_tolerance': 'double',
        'tangential_gain': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.team_color = kwargs.get('team_color', bool())
        self.team_side = kwargs.get('team_side', bool())
        self.local = kwargs.get('local', bool())
        self.reset = kwargs.get('reset', bool())
        self.exposure = kwargs.get('exposure', int())
        self.robot0 = kwargs.get('robot0', int())
        self.robot1 = kwargs.get('robot1', int())
        self.robot2 = kwargs.get('robot2', int())
        self.attractive_gain = kwargs.get('attractive_gain', float())
        self.repulsive_gain = kwargs.get('repulsive_gain', float())
        self.repulsion_radius = kwargs.get('repulsion_radius', float())
        self.goal_tolerance = kwargs.get('goal_tolerance', float())
        self.tangential_gain = kwargs.get('tangential_gain', float())

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
        if self.team_color != other.team_color:
            return False
        if self.team_side != other.team_side:
            return False
        if self.local != other.local:
            return False
        if self.reset != other.reset:
            return False
        if self.exposure != other.exposure:
            return False
        if self.robot0 != other.robot0:
            return False
        if self.robot1 != other.robot1:
            return False
        if self.robot2 != other.robot2:
            return False
        if self.attractive_gain != other.attractive_gain:
            return False
        if self.repulsive_gain != other.repulsive_gain:
            return False
        if self.repulsion_radius != other.repulsion_radius:
            return False
        if self.goal_tolerance != other.goal_tolerance:
            return False
        if self.tangential_gain != other.tangential_gain:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def team_color(self):
        """Message field 'team_color'."""
        return self._team_color

    @team_color.setter
    def team_color(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'team_color' field must be of type 'bool'"
        self._team_color = value

    @builtins.property
    def team_side(self):
        """Message field 'team_side'."""
        return self._team_side

    @team_side.setter
    def team_side(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'team_side' field must be of type 'bool'"
        self._team_side = value

    @builtins.property
    def local(self):
        """Message field 'local'."""
        return self._local

    @local.setter
    def local(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'local' field must be of type 'bool'"
        self._local = value

    @builtins.property
    def reset(self):
        """Message field 'reset'."""
        return self._reset

    @reset.setter
    def reset(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'reset' field must be of type 'bool'"
        self._reset = value

    @builtins.property
    def exposure(self):
        """Message field 'exposure'."""
        return self._exposure

    @exposure.setter
    def exposure(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'exposure' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'exposure' field must be an integer in [-2147483648, 2147483647]"
        self._exposure = value

    @builtins.property
    def robot0(self):
        """Message field 'robot0'."""
        return self._robot0

    @robot0.setter
    def robot0(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'robot0' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'robot0' field must be an integer in [-2147483648, 2147483647]"
        self._robot0 = value

    @builtins.property
    def robot1(self):
        """Message field 'robot1'."""
        return self._robot1

    @robot1.setter
    def robot1(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'robot1' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'robot1' field must be an integer in [-2147483648, 2147483647]"
        self._robot1 = value

    @builtins.property
    def robot2(self):
        """Message field 'robot2'."""
        return self._robot2

    @robot2.setter
    def robot2(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'robot2' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'robot2' field must be an integer in [-2147483648, 2147483647]"
        self._robot2 = value

    @builtins.property
    def attractive_gain(self):
        """Message field 'attractive_gain'."""
        return self._attractive_gain

    @attractive_gain.setter
    def attractive_gain(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'attractive_gain' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'attractive_gain' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._attractive_gain = value

    @builtins.property
    def repulsive_gain(self):
        """Message field 'repulsive_gain'."""
        return self._repulsive_gain

    @repulsive_gain.setter
    def repulsive_gain(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'repulsive_gain' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'repulsive_gain' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._repulsive_gain = value

    @builtins.property
    def repulsion_radius(self):
        """Message field 'repulsion_radius'."""
        return self._repulsion_radius

    @repulsion_radius.setter
    def repulsion_radius(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'repulsion_radius' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'repulsion_radius' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._repulsion_radius = value

    @builtins.property
    def goal_tolerance(self):
        """Message field 'goal_tolerance'."""
        return self._goal_tolerance

    @goal_tolerance.setter
    def goal_tolerance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'goal_tolerance' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'goal_tolerance' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._goal_tolerance = value

    @builtins.property
    def tangential_gain(self):
        """Message field 'tangential_gain'."""
        return self._tangential_gain

    @tangential_gain.setter
    def tangential_gain(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'tangential_gain' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'tangential_gain' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._tangential_gain = value
