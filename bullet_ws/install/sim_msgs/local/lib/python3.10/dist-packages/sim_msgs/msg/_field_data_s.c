// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from sim_msgs:msg/FieldData.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "sim_msgs/msg/detail/field_data__struct.h"
#include "sim_msgs/msg/detail/field_data__functions.h"

bool sim_msgs__msg__obj_data__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * sim_msgs__msg__obj_data__convert_to_py(void * raw_ros_message);
bool sim_msgs__msg__obj_data__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * sim_msgs__msg__obj_data__convert_to_py(void * raw_ros_message);
bool sim_msgs__msg__obj_data__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * sim_msgs__msg__obj_data__convert_to_py(void * raw_ros_message);
bool sim_msgs__msg__obj_data__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * sim_msgs__msg__obj_data__convert_to_py(void * raw_ros_message);
bool sim_msgs__msg__obj_data__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * sim_msgs__msg__obj_data__convert_to_py(void * raw_ros_message);
bool sim_msgs__msg__obj_data__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * sim_msgs__msg__obj_data__convert_to_py(void * raw_ros_message);
bool sim_msgs__msg__obj_data__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * sim_msgs__msg__obj_data__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool sim_msgs__msg__field_data__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[35];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("sim_msgs.msg._field_data.FieldData", full_classname_dest, 34) == 0);
  }
  sim_msgs__msg__FieldData * ros_message = _ros_message;
  {  // ball
    PyObject * field = PyObject_GetAttrString(_pymsg, "ball");
    if (!field) {
      return false;
    }
    if (!sim_msgs__msg__obj_data__convert_from_py(field, &ros_message->ball)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // robot0
    PyObject * field = PyObject_GetAttrString(_pymsg, "robot0");
    if (!field) {
      return false;
    }
    if (!sim_msgs__msg__obj_data__convert_from_py(field, &ros_message->robot0)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // robot1
    PyObject * field = PyObject_GetAttrString(_pymsg, "robot1");
    if (!field) {
      return false;
    }
    if (!sim_msgs__msg__obj_data__convert_from_py(field, &ros_message->robot1)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // robot2
    PyObject * field = PyObject_GetAttrString(_pymsg, "robot2");
    if (!field) {
      return false;
    }
    if (!sim_msgs__msg__obj_data__convert_from_py(field, &ros_message->robot2)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // robot3
    PyObject * field = PyObject_GetAttrString(_pymsg, "robot3");
    if (!field) {
      return false;
    }
    if (!sim_msgs__msg__obj_data__convert_from_py(field, &ros_message->robot3)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // robot4
    PyObject * field = PyObject_GetAttrString(_pymsg, "robot4");
    if (!field) {
      return false;
    }
    if (!sim_msgs__msg__obj_data__convert_from_py(field, &ros_message->robot4)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // robot5
    PyObject * field = PyObject_GetAttrString(_pymsg, "robot5");
    if (!field) {
      return false;
    }
    if (!sim_msgs__msg__obj_data__convert_from_py(field, &ros_message->robot5)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // score1
    PyObject * field = PyObject_GetAttrString(_pymsg, "score1");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->score1 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // score2
    PyObject * field = PyObject_GetAttrString(_pymsg, "score2");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->score2 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * sim_msgs__msg__field_data__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of FieldData */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("sim_msgs.msg._field_data");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "FieldData");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  sim_msgs__msg__FieldData * ros_message = (sim_msgs__msg__FieldData *)raw_ros_message;
  {  // ball
    PyObject * field = NULL;
    field = sim_msgs__msg__obj_data__convert_to_py(&ros_message->ball);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "ball", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // robot0
    PyObject * field = NULL;
    field = sim_msgs__msg__obj_data__convert_to_py(&ros_message->robot0);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "robot0", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // robot1
    PyObject * field = NULL;
    field = sim_msgs__msg__obj_data__convert_to_py(&ros_message->robot1);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "robot1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // robot2
    PyObject * field = NULL;
    field = sim_msgs__msg__obj_data__convert_to_py(&ros_message->robot2);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "robot2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // robot3
    PyObject * field = NULL;
    field = sim_msgs__msg__obj_data__convert_to_py(&ros_message->robot3);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "robot3", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // robot4
    PyObject * field = NULL;
    field = sim_msgs__msg__obj_data__convert_to_py(&ros_message->robot4);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "robot4", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // robot5
    PyObject * field = NULL;
    field = sim_msgs__msg__obj_data__convert_to_py(&ros_message->robot5);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "robot5", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // score1
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->score1);
    {
      int rc = PyObject_SetAttrString(_pymessage, "score1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // score2
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->score2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "score2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
