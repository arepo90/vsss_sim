// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_msgs:msg/ObjData.idl
// generated code does not contain a copyright notice
#include "sim_msgs/msg/detail/obj_data__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
sim_msgs__msg__ObjData__init(sim_msgs__msg__ObjData * msg)
{
  if (!msg) {
    return false;
  }
  // obj_id
  // current
  // x
  // y
  // theta
  // vx
  // vy
  // w
  return true;
}

void
sim_msgs__msg__ObjData__fini(sim_msgs__msg__ObjData * msg)
{
  if (!msg) {
    return;
  }
  // obj_id
  // current
  // x
  // y
  // theta
  // vx
  // vy
  // w
}

bool
sim_msgs__msg__ObjData__are_equal(const sim_msgs__msg__ObjData * lhs, const sim_msgs__msg__ObjData * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // obj_id
  if (lhs->obj_id != rhs->obj_id) {
    return false;
  }
  // current
  if (lhs->current != rhs->current) {
    return false;
  }
  // x
  if (lhs->x != rhs->x) {
    return false;
  }
  // y
  if (lhs->y != rhs->y) {
    return false;
  }
  // theta
  if (lhs->theta != rhs->theta) {
    return false;
  }
  // vx
  if (lhs->vx != rhs->vx) {
    return false;
  }
  // vy
  if (lhs->vy != rhs->vy) {
    return false;
  }
  // w
  if (lhs->w != rhs->w) {
    return false;
  }
  return true;
}

bool
sim_msgs__msg__ObjData__copy(
  const sim_msgs__msg__ObjData * input,
  sim_msgs__msg__ObjData * output)
{
  if (!input || !output) {
    return false;
  }
  // obj_id
  output->obj_id = input->obj_id;
  // current
  output->current = input->current;
  // x
  output->x = input->x;
  // y
  output->y = input->y;
  // theta
  output->theta = input->theta;
  // vx
  output->vx = input->vx;
  // vy
  output->vy = input->vy;
  // w
  output->w = input->w;
  return true;
}

sim_msgs__msg__ObjData *
sim_msgs__msg__ObjData__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__msg__ObjData * msg = (sim_msgs__msg__ObjData *)allocator.allocate(sizeof(sim_msgs__msg__ObjData), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_msgs__msg__ObjData));
  bool success = sim_msgs__msg__ObjData__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_msgs__msg__ObjData__destroy(sim_msgs__msg__ObjData * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_msgs__msg__ObjData__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_msgs__msg__ObjData__Sequence__init(sim_msgs__msg__ObjData__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__msg__ObjData * data = NULL;

  if (size) {
    data = (sim_msgs__msg__ObjData *)allocator.zero_allocate(size, sizeof(sim_msgs__msg__ObjData), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_msgs__msg__ObjData__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_msgs__msg__ObjData__fini(&data[i - 1]);
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
sim_msgs__msg__ObjData__Sequence__fini(sim_msgs__msg__ObjData__Sequence * array)
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
      sim_msgs__msg__ObjData__fini(&array->data[i]);
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

sim_msgs__msg__ObjData__Sequence *
sim_msgs__msg__ObjData__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__msg__ObjData__Sequence * array = (sim_msgs__msg__ObjData__Sequence *)allocator.allocate(sizeof(sim_msgs__msg__ObjData__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_msgs__msg__ObjData__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_msgs__msg__ObjData__Sequence__destroy(sim_msgs__msg__ObjData__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_msgs__msg__ObjData__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_msgs__msg__ObjData__Sequence__are_equal(const sim_msgs__msg__ObjData__Sequence * lhs, const sim_msgs__msg__ObjData__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_msgs__msg__ObjData__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_msgs__msg__ObjData__Sequence__copy(
  const sim_msgs__msg__ObjData__Sequence * input,
  sim_msgs__msg__ObjData__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_msgs__msg__ObjData);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_msgs__msg__ObjData * data =
      (sim_msgs__msg__ObjData *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_msgs__msg__ObjData__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_msgs__msg__ObjData__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_msgs__msg__ObjData__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
