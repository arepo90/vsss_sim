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
  {  // team_color
    PyObject * field = PyObject_GetAttrString(_pymsg, "team_color");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->team_color = (Py_True == field);
    Py_DECREF(field);
  }
  {  // team_side
    PyObject * field = PyObject_GetAttrString(_pymsg, "team_side");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->team_side = (Py_True == field);
    Py_DECREF(field);
  }
  {  // local
    PyObject * field = PyObject_GetAttrString(_pymsg, "local");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->local = (Py_True == field);
    Py_DECREF(field);
  }
  {  // reset
    PyObject * field = PyObject_GetAttrString(_pymsg, "reset");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->reset = (Py_True == field);
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
  {  // robot0
    PyObject * field = PyObject_GetAttrString(_pymsg, "robot0");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->robot0 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // robot1
    PyObject * field = PyObject_GetAttrString(_pymsg, "robot1");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->robot1 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // robot2
    PyObject * field = PyObject_GetAttrString(_pymsg, "robot2");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->robot2 = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // attractive_gain
    PyObject * field = PyObject_GetAttrString(_pymsg, "attractive_gain");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->attractive_gain = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // repulsive_gain
    PyObject * field = PyObject_GetAttrString(_pymsg, "repulsive_gain");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->repulsive_gain = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // repulsion_radius
    PyObject * field = PyObject_GetAttrString(_pymsg, "repulsion_radius");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->repulsion_radius = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // goal_tolerance
    PyObject * field = PyObject_GetAttrString(_pymsg, "goal_tolerance");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->goal_tolerance = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // tangential_gain
    PyObject * field = PyObject_GetAttrString(_pymsg, "tangential_gain");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->tangential_gain = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // target_offset
    PyObject * field = PyObject_GetAttrString(_pymsg, "target_offset");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->target_offset = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // colinearity
    PyObject * field = PyObject_GetAttrString(_pymsg, "colinearity");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->colinearity = PyFloat_AS_DOUBLE(field);
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
  {  // team_color
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->team_color ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "team_color", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // team_side
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->team_side ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "team_side", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // local
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->local ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "local", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // reset
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->reset ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "reset", field);
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
  {  // robot0
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->robot0);
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
    field = PyLong_FromLong(ros_message->robot1);
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
    field = PyLong_FromLong(ros_message->robot2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "robot2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // attractive_gain
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->attractive_gain);
    {
      int rc = PyObject_SetAttrString(_pymessage, "attractive_gain", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // repulsive_gain
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->repulsive_gain);
    {
      int rc = PyObject_SetAttrString(_pymessage, "repulsive_gain", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // repulsion_radius
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->repulsion_radius);
    {
      int rc = PyObject_SetAttrString(_pymessage, "repulsion_radius", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // goal_tolerance
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->goal_tolerance);
    {
      int rc = PyObject_SetAttrString(_pymessage, "goal_tolerance", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tangential_gain
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->tangential_gain);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tangential_gain", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // target_offset
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->target_offset);
    {
      int rc = PyObject_SetAttrString(_pymessage, "target_offset", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // colinearity
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->colinearity);
    {
      int rc = PyObject_SetAttrString(_pymessage, "colinearity", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
