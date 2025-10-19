// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from sim_msgs:msg/HighCmd.idl
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
#include "sim_msgs/msg/detail/high_cmd__struct.h"
#include "sim_msgs/msg/detail/high_cmd__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool sim_msgs__msg__high_cmd__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[31];
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
    assert(strncmp("sim_msgs.msg._high_cmd.HighCmd", full_classname_dest, 30) == 0);
  }
  sim_msgs__msg__HighCmd * ros_message = _ros_message;
  {  // robot_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "robot_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->robot_id = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // skill
    PyObject * field = PyObject_GetAttrString(_pymsg, "skill");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->skill = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // mod
    PyObject * field = PyObject_GetAttrString(_pymsg, "mod");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->mod = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // tgt_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "tgt_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->tgt_x = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // tgt_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "tgt_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->tgt_y = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // tgt_theta
    PyObject * field = PyObject_GetAttrString(_pymsg, "tgt_theta");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->tgt_theta = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * sim_msgs__msg__high_cmd__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of HighCmd */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("sim_msgs.msg._high_cmd");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "HighCmd");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  sim_msgs__msg__HighCmd * ros_message = (sim_msgs__msg__HighCmd *)raw_ros_message;
  {  // robot_id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->robot_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "robot_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // skill
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->skill);
    {
      int rc = PyObject_SetAttrString(_pymessage, "skill", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // mod
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->mod);
    {
      int rc = PyObject_SetAttrString(_pymessage, "mod", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tgt_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->tgt_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tgt_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tgt_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->tgt_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tgt_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tgt_theta
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->tgt_theta);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tgt_theta", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
