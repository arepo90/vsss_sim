// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_msgs:msg/ObjData.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__OBJ_DATA__STRUCT_H_
#define SIM_MSGS__MSG__DETAIL__OBJ_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/ObjData in the package sim_msgs.
typedef struct sim_msgs__msg__ObjData
{
  int32_t obj_id;
  bool current;
  double x;
  double y;
  double theta;
  double vx;
  double vy;
  double w;
} sim_msgs__msg__ObjData;

// Struct for a sequence of sim_msgs__msg__ObjData.
typedef struct sim_msgs__msg__ObjData__Sequence
{
  sim_msgs__msg__ObjData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_msgs__msg__ObjData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_MSGS__MSG__DETAIL__OBJ_DATA__STRUCT_H_
