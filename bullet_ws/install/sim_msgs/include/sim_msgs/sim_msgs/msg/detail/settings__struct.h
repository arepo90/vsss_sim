// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_msgs:msg/Settings.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__SETTINGS__STRUCT_H_
#define SIM_MSGS__MSG__DETAIL__SETTINGS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Settings in the package sim_msgs.
typedef struct sim_msgs__msg__Settings
{
  bool friendly_color;
  bool friendly_side;
  int32_t exposure;
} sim_msgs__msg__Settings;

// Struct for a sequence of sim_msgs__msg__Settings.
typedef struct sim_msgs__msg__Settings__Sequence
{
  sim_msgs__msg__Settings * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_msgs__msg__Settings__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_MSGS__MSG__DETAIL__SETTINGS__STRUCT_H_
