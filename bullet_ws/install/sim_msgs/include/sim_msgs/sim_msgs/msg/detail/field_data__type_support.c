// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from sim_msgs:msg/FieldData.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "sim_msgs/msg/detail/field_data__rosidl_typesupport_introspection_c.h"
#include "sim_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "sim_msgs/msg/detail/field_data__functions.h"
#include "sim_msgs/msg/detail/field_data__struct.h"


// Include directives for member types
// Member `ball`
// Member `team0`
// Member `team1`
// Member `team2`
// Member `op0`
// Member `op1`
// Member `op2`
#include "sim_msgs/msg/obj_data.h"
// Member `ball`
// Member `team0`
// Member `team1`
// Member `team2`
// Member `op0`
// Member `op1`
// Member `op2`
#include "sim_msgs/msg/detail/obj_data__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  sim_msgs__msg__FieldData__init(message_memory);
}

void sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_fini_function(void * message_memory)
{
  sim_msgs__msg__FieldData__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_member_array[9] = {
  {
    "ball",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__FieldData, ball),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "team0",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__FieldData, team0),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "team1",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__FieldData, team1),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "team2",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__FieldData, team2),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "op0",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__FieldData, op0),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "op1",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__FieldData, op1),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "op2",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__FieldData, op2),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "score1",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__FieldData, score1),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "score2",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sim_msgs__msg__FieldData, score2),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_members = {
  "sim_msgs__msg",  // message namespace
  "FieldData",  // message name
  9,  // number of fields
  sizeof(sim_msgs__msg__FieldData),
  sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_member_array,  // message members
  sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_init_function,  // function to initialize message memory (memory has to be allocated)
  sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_type_support_handle = {
  0,
  &sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_sim_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_msgs, msg, FieldData)() {
  sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_msgs, msg, ObjData)();
  sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_msgs, msg, ObjData)();
  sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_msgs, msg, ObjData)();
  sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_msgs, msg, ObjData)();
  sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_member_array[4].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_msgs, msg, ObjData)();
  sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_member_array[5].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_msgs, msg, ObjData)();
  sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_member_array[6].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, sim_msgs, msg, ObjData)();
  if (!sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_type_support_handle.typesupport_identifier) {
    sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &sim_msgs__msg__FieldData__rosidl_typesupport_introspection_c__FieldData_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
