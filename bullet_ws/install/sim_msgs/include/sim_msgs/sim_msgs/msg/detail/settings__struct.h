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
  bool team_color;
  bool team_side;
  bool local;
  bool reset;
  int32_t exposure;
  int32_t robot0;
  int32_t robot1;
  int32_t robot2;
  double attractive_gain;
  double repulsive_gain;
  double repulsion_radius;
  double goal_tolerance;
  double tangential_gain;
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
