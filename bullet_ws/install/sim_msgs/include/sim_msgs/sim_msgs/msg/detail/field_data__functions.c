// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_msgs:msg/FieldData.idl
// generated code does not contain a copyright notice
#include "sim_msgs/msg/detail/field_data__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `ball`
// Member `robot0`
// Member `robot1`
// Member `robot2`
// Member `robot3`
// Member `robot4`
// Member `robot5`
#include "sim_msgs/msg/detail/obj_data__functions.h"

bool
sim_msgs__msg__FieldData__init(sim_msgs__msg__FieldData * msg)
{
  if (!msg) {
    return false;
  }
  // ball
  if (!sim_msgs__msg__ObjData__init(&msg->ball)) {
    sim_msgs__msg__FieldData__fini(msg);
    return false;
  }
  // robot0
  if (!sim_msgs__msg__ObjData__init(&msg->robot0)) {
    sim_msgs__msg__FieldData__fini(msg);
    return false;
  }
  // robot1
  if (!sim_msgs__msg__ObjData__init(&msg->robot1)) {
    sim_msgs__msg__FieldData__fini(msg);
    return false;
  }
  // robot2
  if (!sim_msgs__msg__ObjData__init(&msg->robot2)) {
    sim_msgs__msg__FieldData__fini(msg);
    return false;
  }
  // robot3
  if (!sim_msgs__msg__ObjData__init(&msg->robot3)) {
    sim_msgs__msg__FieldData__fini(msg);
    return false;
  }
  // robot4
  if (!sim_msgs__msg__ObjData__init(&msg->robot4)) {
    sim_msgs__msg__FieldData__fini(msg);
    return false;
  }
  // robot5
  if (!sim_msgs__msg__ObjData__init(&msg->robot5)) {
    sim_msgs__msg__FieldData__fini(msg);
    return false;
  }
  // score1
  // score2
  return true;
}

void
sim_msgs__msg__FieldData__fini(sim_msgs__msg__FieldData * msg)
{
  if (!msg) {
    return;
  }
  // ball
  sim_msgs__msg__ObjData__fini(&msg->ball);
  // robot0
  sim_msgs__msg__ObjData__fini(&msg->robot0);
  // robot1
  sim_msgs__msg__ObjData__fini(&msg->robot1);
  // robot2
  sim_msgs__msg__ObjData__fini(&msg->robot2);
  // robot3
  sim_msgs__msg__ObjData__fini(&msg->robot3);
  // robot4
  sim_msgs__msg__ObjData__fini(&msg->robot4);
  // robot5
  sim_msgs__msg__ObjData__fini(&msg->robot5);
  // score1
  // score2
}

bool
sim_msgs__msg__FieldData__are_equal(const sim_msgs__msg__FieldData * lhs, const sim_msgs__msg__FieldData * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // ball
  if (!sim_msgs__msg__ObjData__are_equal(
      &(lhs->ball), &(rhs->ball)))
  {
    return false;
  }
  // robot0
  if (!sim_msgs__msg__ObjData__are_equal(
      &(lhs->robot0), &(rhs->robot0)))
  {
    return false;
  }
  // robot1
  if (!sim_msgs__msg__ObjData__are_equal(
      &(lhs->robot1), &(rhs->robot1)))
  {
    return false;
  }
  // robot2
  if (!sim_msgs__msg__ObjData__are_equal(
      &(lhs->robot2), &(rhs->robot2)))
  {
    return false;
  }
  // robot3
  if (!sim_msgs__msg__ObjData__are_equal(
      &(lhs->robot3), &(rhs->robot3)))
  {
    return false;
  }
  // robot4
  if (!sim_msgs__msg__ObjData__are_equal(
      &(lhs->robot4), &(rhs->robot4)))
  {
    return false;
  }
  // robot5
  if (!sim_msgs__msg__ObjData__are_equal(
      &(lhs->robot5), &(rhs->robot5)))
  {
    return false;
  }
  // score1
  if (lhs->score1 != rhs->score1) {
    return false;
  }
  // score2
  if (lhs->score2 != rhs->score2) {
    return false;
  }
  return true;
}

bool
sim_msgs__msg__FieldData__copy(
  const sim_msgs__msg__FieldData * input,
  sim_msgs__msg__FieldData * output)
{
  if (!input || !output) {
    return false;
  }
  // ball
  if (!sim_msgs__msg__ObjData__copy(
      &(input->ball), &(output->ball)))
  {
    return false;
  }
  // robot0
  if (!sim_msgs__msg__ObjData__copy(
      &(input->robot0), &(output->robot0)))
  {
    return false;
  }
  // robot1
  if (!sim_msgs__msg__ObjData__copy(
      &(input->robot1), &(output->robot1)))
  {
    return false;
  }
  // robot2
  if (!sim_msgs__msg__ObjData__copy(
      &(input->robot2), &(output->robot2)))
  {
    return false;
  }
  // robot3
  if (!sim_msgs__msg__ObjData__copy(
      &(input->robot3), &(output->robot3)))
  {
    return false;
  }
  // robot4
  if (!sim_msgs__msg__ObjData__copy(
      &(input->robot4), &(output->robot4)))
  {
    return false;
  }
  // robot5
  if (!sim_msgs__msg__ObjData__copy(
      &(input->robot5), &(output->robot5)))
  {
    return false;
  }
  // score1
  output->score1 = input->score1;
  // score2
  output->score2 = input->score2;
  return true;
}

sim_msgs__msg__FieldData *
sim_msgs__msg__FieldData__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__msg__FieldData * msg = (sim_msgs__msg__FieldData *)allocator.allocate(sizeof(sim_msgs__msg__FieldData), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_msgs__msg__FieldData));
  bool success = sim_msgs__msg__FieldData__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_msgs__msg__FieldData__destroy(sim_msgs__msg__FieldData * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_msgs__msg__FieldData__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_msgs__msg__FieldData__Sequence__init(sim_msgs__msg__FieldData__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__msg__FieldData * data = NULL;

  if (size) {
    data = (sim_msgs__msg__FieldData *)allocator.zero_allocate(size, sizeof(sim_msgs__msg__FieldData), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_msgs__msg__FieldData__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_msgs__msg__FieldData__fini(&data[i - 1]);
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
sim_msgs__msg__FieldData__Sequence__fini(sim_msgs__msg__FieldData__Sequence * array)
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
      sim_msgs__msg__FieldData__fini(&array->data[i]);
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

sim_msgs__msg__FieldData__Sequence *
sim_msgs__msg__FieldData__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__msg__FieldData__Sequence * array = (sim_msgs__msg__FieldData__Sequence *)allocator.allocate(sizeof(sim_msgs__msg__FieldData__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_msgs__msg__FieldData__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_msgs__msg__FieldData__Sequence__destroy(sim_msgs__msg__FieldData__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_msgs__msg__FieldData__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_msgs__msg__FieldData__Sequence__are_equal(const sim_msgs__msg__FieldData__Sequence * lhs, const sim_msgs__msg__FieldData__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_msgs__msg__FieldData__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_msgs__msg__FieldData__Sequence__copy(
  const sim_msgs__msg__FieldData__Sequence * input,
  sim_msgs__msg__FieldData__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_msgs__msg__FieldData);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_msgs__msg__FieldData * data =
      (sim_msgs__msg__FieldData *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_msgs__msg__FieldData__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_msgs__msg__FieldData__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_msgs__msg__FieldData__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
