// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_msgs:msg/HighCmd.idl
// generated code does not contain a copyright notice
#include "sim_msgs/msg/detail/high_cmd__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
sim_msgs__msg__HighCmd__init(sim_msgs__msg__HighCmd * msg)
{
  if (!msg) {
    return false;
  }
  // robot_id
  // skill
  // mod
  // tgt_x
  // tgt_y
  // tgt_theta
  return true;
}

void
sim_msgs__msg__HighCmd__fini(sim_msgs__msg__HighCmd * msg)
{
  if (!msg) {
    return;
  }
  // robot_id
  // skill
  // mod
  // tgt_x
  // tgt_y
  // tgt_theta
}

bool
sim_msgs__msg__HighCmd__are_equal(const sim_msgs__msg__HighCmd * lhs, const sim_msgs__msg__HighCmd * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // robot_id
  if (lhs->robot_id != rhs->robot_id) {
    return false;
  }
  // skill
  if (lhs->skill != rhs->skill) {
    return false;
  }
  // mod
  if (lhs->mod != rhs->mod) {
    return false;
  }
  // tgt_x
  if (lhs->tgt_x != rhs->tgt_x) {
    return false;
  }
  // tgt_y
  if (lhs->tgt_y != rhs->tgt_y) {
    return false;
  }
  // tgt_theta
  if (lhs->tgt_theta != rhs->tgt_theta) {
    return false;
  }
  return true;
}

bool
sim_msgs__msg__HighCmd__copy(
  const sim_msgs__msg__HighCmd * input,
  sim_msgs__msg__HighCmd * output)
{
  if (!input || !output) {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // skill
  output->skill = input->skill;
  // mod
  output->mod = input->mod;
  // tgt_x
  output->tgt_x = input->tgt_x;
  // tgt_y
  output->tgt_y = input->tgt_y;
  // tgt_theta
  output->tgt_theta = input->tgt_theta;
  return true;
}

sim_msgs__msg__HighCmd *
sim_msgs__msg__HighCmd__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__msg__HighCmd * msg = (sim_msgs__msg__HighCmd *)allocator.allocate(sizeof(sim_msgs__msg__HighCmd), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_msgs__msg__HighCmd));
  bool success = sim_msgs__msg__HighCmd__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_msgs__msg__HighCmd__destroy(sim_msgs__msg__HighCmd * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_msgs__msg__HighCmd__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_msgs__msg__HighCmd__Sequence__init(sim_msgs__msg__HighCmd__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__msg__HighCmd * data = NULL;

  if (size) {
    data = (sim_msgs__msg__HighCmd *)allocator.zero_allocate(size, sizeof(sim_msgs__msg__HighCmd), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_msgs__msg__HighCmd__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_msgs__msg__HighCmd__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
sim_msgs__msg__HighCmd__Sequence__fini(sim_msgs__msg__HighCmd__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      sim_msgs__msg__HighCmd__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

sim_msgs__msg__HighCmd__Sequence *
sim_msgs__msg__HighCmd__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__msg__HighCmd__Sequence * array = (sim_msgs__msg__HighCmd__Sequence *)allocator.allocate(sizeof(sim_msgs__msg__HighCmd__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_msgs__msg__HighCmd__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_msgs__msg__HighCmd__Sequence__destroy(sim_msgs__msg__HighCmd__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_msgs__msg__HighCmd__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_msgs__msg__HighCmd__Sequence__are_equal(const sim_msgs__msg__HighCmd__Sequence * lhs, const sim_msgs__msg__HighCmd__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_msgs__msg__HighCmd__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_msgs__msg__HighCmd__Sequence__copy(
  const sim_msgs__msg__HighCmd__Sequence * input,
  sim_msgs__msg__HighCmd__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_msgs__msg__HighCmd);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_msgs__msg__HighCmd * data =
      (sim_msgs__msg__HighCmd *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_msgs__msg__HighCmd__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_msgs__msg__HighCmd__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_msgs__msg__HighCmd__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
