// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_msgs:srv/Reset.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__SRV__DETAIL__RESET__STRUCT_H_
#define SIM_MSGS__SRV__DETAIL__RESET__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'settings'
#include "sim_msgs/msg/detail/field_data__struct.h"

/// Struct defined in srv/Reset in the package sim_msgs.
typedef struct sim_msgs__srv__Reset_Request
{
  sim_msgs__msg__FieldData settings;
} sim_msgs__srv__Reset_Request;

// Struct for a sequence of sim_msgs__srv__Reset_Request.
typedef struct sim_msgs__srv__Reset_Request__Sequence
{
  sim_msgs__srv__Reset_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_msgs__srv__Reset_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Reset in the package sim_msgs.
typedef struct sim_msgs__srv__Reset_Response
{
  bool success;
} sim_msgs__srv__Reset_Response;

// Struct for a sequence of sim_msgs__srv__Reset_Response.
typedef struct sim_msgs__srv__Reset_Response__Sequence
{
  sim_msgs__srv__Reset_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_msgs__srv__Reset_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_MSGS__SRV__DETAIL__RESET__STRUCT_H_
