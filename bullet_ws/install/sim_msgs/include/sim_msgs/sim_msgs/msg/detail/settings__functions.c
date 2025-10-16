// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_msgs:msg/Settings.idl
// generated code does not contain a copyright notice
#include "sim_msgs/msg/detail/settings__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
sim_msgs__msg__Settings__init(sim_msgs__msg__Settings * msg)
{
  if (!msg) {
    return false;
  }
  // friendly_color
  // friendly_side
  // exposure
  return true;
}

void
sim_msgs__msg__Settings__fini(sim_msgs__msg__Settings * msg)
{
  if (!msg) {
    return;
  }
  // friendly_color
  // friendly_side
  // exposure
}

bool
sim_msgs__msg__Settings__are_equal(const sim_msgs__msg__Settings * lhs, const sim_msgs__msg__Settings * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // friendly_color
  if (lhs->friendly_color != rhs->friendly_color) {
    return false;
  }
  // friendly_side
  if (lhs->friendly_side != rhs->friendly_side) {
    return false;
  }
  // exposure
  if (lhs->exposure != rhs->exposure) {
    return false;
  }
  return true;
}

bool
sim_msgs__msg__Settings__copy(
  const sim_msgs__msg__Settings * input,
  sim_msgs__msg__Settings * output)
{
  if (!input || !output) {
    return false;
  }
  // friendly_color
  output->friendly_color = input->friendly_color;
  // friendly_side
  output->friendly_side = input->friendly_side;
  // exposure
  output->exposure = input->exposure;
  return true;
}

sim_msgs__msg__Settings *
sim_msgs__msg__Settings__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__msg__Settings * msg = (sim_msgs__msg__Settings *)allocator.allocate(sizeof(sim_msgs__msg__Settings), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_msgs__msg__Settings));
  bool success = sim_msgs__msg__Settings__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_msgs__msg__Settings__destroy(sim_msgs__msg__Settings * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_msgs__msg__Settings__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_msgs__msg__Settings__Sequence__init(sim_msgs__msg__Settings__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__msg__Settings * data = NULL;

  if (size) {
    data = (sim_msgs__msg__Settings *)allocator.zero_allocate(size, sizeof(sim_msgs__msg__Settings), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_msgs__msg__Settings__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_msgs__msg__Settings__fini(&data[i - 1]);
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
sim_msgs__msg__Settings__Sequence__fini(sim_msgs__msg__Settings__Sequence * array)
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
      sim_msgs__msg__Settings__fini(&array->data[i]);
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

sim_msgs__msg__Settings__Sequence *
sim_msgs__msg__Settings__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__msg__Settings__Sequence * array = (sim_msgs__msg__Settings__Sequence *)allocator.allocate(sizeof(sim_msgs__msg__Settings__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_msgs__msg__Settings__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_msgs__msg__Settings__Sequence__destroy(sim_msgs__msg__Settings__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_msgs__msg__Settings__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_msgs__msg__Settings__Sequence__are_equal(const sim_msgs__msg__Settings__Sequence * lhs, const sim_msgs__msg__Settings__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_msgs__msg__Settings__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_msgs__msg__Settings__Sequence__copy(
  const sim_msgs__msg__Settings__Sequence * input,
  sim_msgs__msg__Settings__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_msgs__msg__Settings);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_msgs__msg__Settings * data =
      (sim_msgs__msg__Settings *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_msgs__msg__Settings__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_msgs__msg__Settings__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_msgs__msg__Settings__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
