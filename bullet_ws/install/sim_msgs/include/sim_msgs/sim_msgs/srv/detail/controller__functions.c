// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from sim_msgs:srv/Controller.idl
// generated code does not contain a copyright notice
#include "sim_msgs/srv/detail/controller__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `team0`
// Member `team1`
// Member `team2`
#include "sim_msgs/msg/detail/high_cmd__functions.h"

bool
sim_msgs__srv__Controller_Request__init(sim_msgs__srv__Controller_Request * msg)
{
  if (!msg) {
    return false;
  }
  // state
  // team0
  if (!sim_msgs__msg__HighCmd__init(&msg->team0)) {
    sim_msgs__srv__Controller_Request__fini(msg);
    return false;
  }
  // team1
  if (!sim_msgs__msg__HighCmd__init(&msg->team1)) {
    sim_msgs__srv__Controller_Request__fini(msg);
    return false;
  }
  // team2
  if (!sim_msgs__msg__HighCmd__init(&msg->team2)) {
    sim_msgs__srv__Controller_Request__fini(msg);
    return false;
  }
  return true;
}

void
sim_msgs__srv__Controller_Request__fini(sim_msgs__srv__Controller_Request * msg)
{
  if (!msg) {
    return;
  }
  // state
  // team0
  sim_msgs__msg__HighCmd__fini(&msg->team0);
  // team1
  sim_msgs__msg__HighCmd__fini(&msg->team1);
  // team2
  sim_msgs__msg__HighCmd__fini(&msg->team2);
}

bool
sim_msgs__srv__Controller_Request__are_equal(const sim_msgs__srv__Controller_Request * lhs, const sim_msgs__srv__Controller_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // state
  if (lhs->state != rhs->state) {
    return false;
  }
  // team0
  if (!sim_msgs__msg__HighCmd__are_equal(
      &(lhs->team0), &(rhs->team0)))
  {
    return false;
  }
  // team1
  if (!sim_msgs__msg__HighCmd__are_equal(
      &(lhs->team1), &(rhs->team1)))
  {
    return false;
  }
  // team2
  if (!sim_msgs__msg__HighCmd__are_equal(
      &(lhs->team2), &(rhs->team2)))
  {
    return false;
  }
  return true;
}

bool
sim_msgs__srv__Controller_Request__copy(
  const sim_msgs__srv__Controller_Request * input,
  sim_msgs__srv__Controller_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // state
  output->state = input->state;
  // team0
  if (!sim_msgs__msg__HighCmd__copy(
      &(input->team0), &(output->team0)))
  {
    return false;
  }
  // team1
  if (!sim_msgs__msg__HighCmd__copy(
      &(input->team1), &(output->team1)))
  {
    return false;
  }
  // team2
  if (!sim_msgs__msg__HighCmd__copy(
      &(input->team2), &(output->team2)))
  {
    return false;
  }
  return true;
}

sim_msgs__srv__Controller_Request *
sim_msgs__srv__Controller_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__srv__Controller_Request * msg = (sim_msgs__srv__Controller_Request *)allocator.allocate(sizeof(sim_msgs__srv__Controller_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_msgs__srv__Controller_Request));
  bool success = sim_msgs__srv__Controller_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_msgs__srv__Controller_Request__destroy(sim_msgs__srv__Controller_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_msgs__srv__Controller_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_msgs__srv__Controller_Request__Sequence__init(sim_msgs__srv__Controller_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__srv__Controller_Request * data = NULL;

  if (size) {
    data = (sim_msgs__srv__Controller_Request *)allocator.zero_allocate(size, sizeof(sim_msgs__srv__Controller_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_msgs__srv__Controller_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_msgs__srv__Controller_Request__fini(&data[i - 1]);
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
sim_msgs__srv__Controller_Request__Sequence__fini(sim_msgs__srv__Controller_Request__Sequence * array)
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
      sim_msgs__srv__Controller_Request__fini(&array->data[i]);
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

sim_msgs__srv__Controller_Request__Sequence *
sim_msgs__srv__Controller_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__srv__Controller_Request__Sequence * array = (sim_msgs__srv__Controller_Request__Sequence *)allocator.allocate(sizeof(sim_msgs__srv__Controller_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_msgs__srv__Controller_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_msgs__srv__Controller_Request__Sequence__destroy(sim_msgs__srv__Controller_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_msgs__srv__Controller_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_msgs__srv__Controller_Request__Sequence__are_equal(const sim_msgs__srv__Controller_Request__Sequence * lhs, const sim_msgs__srv__Controller_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_msgs__srv__Controller_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_msgs__srv__Controller_Request__Sequence__copy(
  const sim_msgs__srv__Controller_Request__Sequence * input,
  sim_msgs__srv__Controller_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_msgs__srv__Controller_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_msgs__srv__Controller_Request * data =
      (sim_msgs__srv__Controller_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_msgs__srv__Controller_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_msgs__srv__Controller_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_msgs__srv__Controller_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
sim_msgs__srv__Controller_Response__init(sim_msgs__srv__Controller_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  return true;
}

void
sim_msgs__srv__Controller_Response__fini(sim_msgs__srv__Controller_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
}

bool
sim_msgs__srv__Controller_Response__are_equal(const sim_msgs__srv__Controller_Response * lhs, const sim_msgs__srv__Controller_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
sim_msgs__srv__Controller_Response__copy(
  const sim_msgs__srv__Controller_Response * input,
  sim_msgs__srv__Controller_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  return true;
}

sim_msgs__srv__Controller_Response *
sim_msgs__srv__Controller_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__srv__Controller_Response * msg = (sim_msgs__srv__Controller_Response *)allocator.allocate(sizeof(sim_msgs__srv__Controller_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(sim_msgs__srv__Controller_Response));
  bool success = sim_msgs__srv__Controller_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
sim_msgs__srv__Controller_Response__destroy(sim_msgs__srv__Controller_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    sim_msgs__srv__Controller_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
sim_msgs__srv__Controller_Response__Sequence__init(sim_msgs__srv__Controller_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__srv__Controller_Response * data = NULL;

  if (size) {
    data = (sim_msgs__srv__Controller_Response *)allocator.zero_allocate(size, sizeof(sim_msgs__srv__Controller_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = sim_msgs__srv__Controller_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        sim_msgs__srv__Controller_Response__fini(&data[i - 1]);
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
sim_msgs__srv__Controller_Response__Sequence__fini(sim_msgs__srv__Controller_Response__Sequence * array)
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
      sim_msgs__srv__Controller_Response__fini(&array->data[i]);
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

sim_msgs__srv__Controller_Response__Sequence *
sim_msgs__srv__Controller_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  sim_msgs__srv__Controller_Response__Sequence * array = (sim_msgs__srv__Controller_Response__Sequence *)allocator.allocate(sizeof(sim_msgs__srv__Controller_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = sim_msgs__srv__Controller_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
sim_msgs__srv__Controller_Response__Sequence__destroy(sim_msgs__srv__Controller_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    sim_msgs__srv__Controller_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
sim_msgs__srv__Controller_Response__Sequence__are_equal(const sim_msgs__srv__Controller_Response__Sequence * lhs, const sim_msgs__srv__Controller_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!sim_msgs__srv__Controller_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
sim_msgs__srv__Controller_Response__Sequence__copy(
  const sim_msgs__srv__Controller_Response__Sequence * input,
  sim_msgs__srv__Controller_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(sim_msgs__srv__Controller_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    sim_msgs__srv__Controller_Response * data =
      (sim_msgs__srv__Controller_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!sim_msgs__srv__Controller_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          sim_msgs__srv__Controller_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!sim_msgs__srv__Controller_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
