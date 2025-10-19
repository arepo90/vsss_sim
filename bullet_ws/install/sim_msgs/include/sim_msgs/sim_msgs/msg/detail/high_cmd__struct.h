// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_msgs:msg/HighCmd.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__HIGH_CMD__STRUCT_H_
#define SIM_MSGS__MSG__DETAIL__HIGH_CMD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/HighCmd in the package sim_msgs.
typedef struct sim_msgs__msg__HighCmd
{
  int32_t robot_id;
  int32_t skill;
  int32_t mod;
  double tgt_x;
  double tgt_y;
  double tgt_theta;
} sim_msgs__msg__HighCmd;

// Struct for a sequence of sim_msgs__msg__HighCmd.
typedef struct sim_msgs__msg__HighCmd__Sequence
{
  sim_msgs__msg__HighCmd * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_msgs__msg__HighCmd__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_MSGS__MSG__DETAIL__HIGH_CMD__STRUCT_H_
