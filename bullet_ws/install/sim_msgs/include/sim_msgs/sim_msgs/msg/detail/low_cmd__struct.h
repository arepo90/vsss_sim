// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_msgs:msg/LowCmd.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__LOW_CMD__STRUCT_H_
#define SIM_MSGS__MSG__DETAIL__LOW_CMD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/LowCmd in the package sim_msgs.
typedef struct sim_msgs__msg__LowCmd
{
  int32_t robot_id;
  bool local;
  double vx;
  double vy;
  double dtheta;
} sim_msgs__msg__LowCmd;

// Struct for a sequence of sim_msgs__msg__LowCmd.
typedef struct sim_msgs__msg__LowCmd__Sequence
{
  sim_msgs__msg__LowCmd * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_msgs__msg__LowCmd__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_MSGS__MSG__DETAIL__LOW_CMD__STRUCT_H_
