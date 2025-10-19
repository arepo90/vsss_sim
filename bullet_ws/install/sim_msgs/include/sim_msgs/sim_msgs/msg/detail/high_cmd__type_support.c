// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from sim_msgs:msg/HighCmd.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "sim_msgs/msg/detail/high_cmd__rosidl_typesupport_introspection_c.h"
#include "sim_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "sim_msgs/msg/detail/high_cmd__functions.h"
#include "sim_msgs/msg/detail/high_cmd__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void sim_msgs__msg__HighCmd__rosidl_typesupport_introspection_c__HighCmd_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sim_msgs__msg__HighCmd__init(message_memory);
}

void sim_msgs__msg__HighCmd__rosidl_typesupport_introspection_c__HighCmd_fini_function(void * message_memory)
{
  sim_msgs__msg__HighCmd__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember sim_msgs__msg__HighCmd__rosidl_typesupport_introspection_c__HighCmd_message_member_array[6] = {
  {
    "robot_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__HighCmd, robot_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "skill",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__HighCmd, skill),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "mod",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__HighCmd, mod),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "tgt_x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__HighCmd, tgt_x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "tgt_y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__HighCmd, tgt_y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "tgt_theta",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__HighCmd, tgt_theta),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sim_msgs__msg__HighCmd__rosidl_typesupport_introspection_c__HighCmd_message_members = {
  "sim_msgs__msg",  // message namespace
  "HighCmd",  // message name
  6,  // number of fields
  sizeof(sim_msgs__msg__HighCmd),
  sim_msgs__msg__HighCmd__rosidl_typesupport_introspection_c__HighCmd_message_member_array,  // message members
  sim_msgs__msg__HighCmd__rosidl_typesupport_introspection_c__HighCmd_init_function,  // function to initialize message memory (memory has to be allocated)
  sim_msgs__msg__HighCmd__rosidl_typesupport_introspection_c__HighCmd_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sim_msgs__msg__HighCmd__rosidl_typesupport_introspection_c__HighCmd_message_type_support_handle = {
  0,
  &sim_msgs__msg__HighCmd__rosidl_typesupport_introspection_c__HighCmd_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sim_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_msgs, msg, HighCmd)() {
  if (!sim_msgs__msg__HighCmd__rosidl_typesupport_introspection_c__HighCmd_message_type_support_handle.typesupport_identifier) {
    sim_msgs__msg__HighCmd__rosidl_typesupport_introspection_c__HighCmd_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sim_msgs__msg__HighCmd__rosidl_typesupport_introspection_c__HighCmd_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
