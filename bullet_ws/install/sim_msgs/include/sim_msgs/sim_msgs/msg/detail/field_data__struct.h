// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from sim_msgs:msg/FieldData.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__FIELD_DATA__STRUCT_H_
#define SIM_MSGS__MSG__DETAIL__FIELD_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'ball'
// Member 'team0'
// Member 'team1'
// Member 'team2'
// Member 'op0'
// Member 'op1'
// Member 'op2'
#include "sim_msgs/msg/detail/obj_data__struct.h"

/// Struct defined in msg/FieldData in the package sim_msgs.
typedef struct sim_msgs__msg__FieldData
{
  sim_msgs__msg__ObjData ball;
  sim_msgs__msg__ObjData team0;
  sim_msgs__msg__ObjData team1;
  sim_msgs__msg__ObjData team2;
  sim_msgs__msg__ObjData op0;
  sim_msgs__msg__ObjData op1;
  sim_msgs__msg__ObjData op2;
  int32_t score1;
  int32_t score2;
} sim_msgs__msg__FieldData;

// Struct for a sequence of sim_msgs__msg__FieldData.
typedef struct sim_msgs__msg__FieldData__Sequence
{
  sim_msgs__msg__FieldData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} sim_msgs__msg__FieldData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SIM_MSGS__MSG__DETAIL__FIELD_DATA__STRUCT_H_
