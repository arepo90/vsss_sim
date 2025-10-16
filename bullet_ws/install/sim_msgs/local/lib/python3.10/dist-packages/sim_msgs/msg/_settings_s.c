// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from sim_msgs:msg/Settings.idl
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
#include "sim_msgs/msg/detail/settings__struct.h"
#include "sim_msgs/msg/detail/settings__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool sim_msgs__msg__settings__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[32];
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
    assert(strncmp("sim_msgs.msg._settings.Settings", full_classname_dest, 31) == 0);
  }
  sim_msgs__msg__Settings * ros_message = _ros_message;
  {  // friendly_color
    PyObject * field = PyObject_GetAttrString(_pymsg, "friendly_color");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->friendly_color = (Py_True == field);
    Py_DECREF(field);
  }
  {  // friendly_side
    PyObject * field = PyObject_GetAttrString(_pymsg, "friendly_side");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->friendly_side = (Py_True == field);
    Py_DECREF(field);
  }
  {  // exposure
    PyObject * field = PyObject_GetAttrString(_pymsg, "exposure");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->exposure = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * sim_msgs__msg__settings__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Settings */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("sim_msgs.msg._settings");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Settings");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  sim_msgs__msg__Settings * ros_message = (sim_msgs__msg__Settings *)raw_ros_message;
  {  // friendly_color
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->friendly_color ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "friendly_color", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // friendly_side
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->friendly_side ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "friendly_side", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // exposure
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->exposure);
    {
      int rc = PyObject_SetAttrString(_pymessage, "exposure", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
