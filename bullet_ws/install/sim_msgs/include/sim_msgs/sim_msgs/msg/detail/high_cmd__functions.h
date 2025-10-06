// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from sim_msgs:msg/HighCmd.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__HIGH_CMD__FUNCTIONS_H_
#define SIM_MSGS__MSG__DETAIL__HIGH_CMD__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "sim_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "sim_msgs/msg/detail/high_cmd__struct.h"

/// Initialize msg/HighCmd message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * sim_msgs__msg__HighCmd
 * )) before or use
 * sim_msgs__msg__HighCmd__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_msgs
bool
sim_msgs__msg__HighCmd__init(sim_msgs__msg__HighCmd * msg);

/// Finalize msg/HighCmd message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_msgs
void
sim_msgs__msg__HighCmd__fini(sim_msgs__msg__HighCmd * msg);

/// Create msg/HighCmd message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * sim_msgs__msg__HighCmd__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_msgs
sim_msgs__msg__HighCmd *
sim_msgs__msg__HighCmd__create();

/// Destroy msg/HighCmd message.
/**
 * It calls
 * sim_msgs__msg__HighCmd__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_msgs
void
sim_msgs__msg__HighCmd__destroy(sim_msgs__msg__HighCmd * msg);

/// Check for msg/HighCmd message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_msgs
bool
sim_msgs__msg__HighCmd__are_equal(const sim_msgs__msg__HighCmd * lhs, const sim_msgs__msg__HighCmd * rhs);

/// Copy a msg/HighCmd message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_msgs
bool
sim_msgs__msg__HighCmd__copy(
  const sim_msgs__msg__HighCmd * input,
  sim_msgs__msg__HighCmd * output);

/// Initialize array of msg/HighCmd messages.
/**
 * It allocates the memory for the number of elements and calls
 * sim_msgs__msg__HighCmd__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_msgs
bool
sim_msgs__msg__HighCmd__Sequence__init(sim_msgs__msg__HighCmd__Sequence * array, size_t size);

/// Finalize array of msg/HighCmd messages.
/**
 * It calls
 * sim_msgs__msg__HighCmd__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_msgs
void
sim_msgs__msg__HighCmd__Sequence__fini(sim_msgs__msg__HighCmd__Sequence * array);

/// Create array of msg/HighCmd messages.
/**
 * It allocates the memory for the array and calls
 * sim_msgs__msg__HighCmd__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_msgs
sim_msgs__msg__HighCmd__Sequence *
sim_msgs__msg__HighCmd__Sequence__create(size_t size);

/// Destroy array of msg/HighCmd messages.
/**
 * It calls
 * sim_msgs__msg__HighCmd__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_msgs
void
sim_msgs__msg__HighCmd__Sequence__destroy(sim_msgs__msg__HighCmd__Sequence * array);

/// Check for msg/HighCmd message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_msgs
bool
sim_msgs__msg__HighCmd__Sequence__are_equal(const sim_msgs__msg__HighCmd__Sequence * lhs, const sim_msgs__msg__HighCmd__Sequence * rhs);

/// Copy an array of msg/HighCmd messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_sim_msgs
bool
sim_msgs__msg__HighCmd__Sequence__copy(
  const sim_msgs__msg__HighCmd__Sequence * input,
  sim_msgs__msg__HighCmd__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SIM_MSGS__MSG__DETAIL__HIGH_CMD__FUNCTIONS_H_
