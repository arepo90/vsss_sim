// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from sim_msgs:srv/Controller.idl
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
#include "sim_msgs/srv/detail/controller__struct.h"
#include "sim_msgs/srv/detail/controller__functions.h"

bool sim_msgs__msg__high_cmd__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * sim_msgs__msg__high_cmd__convert_to_py(void * raw_ros_message);
bool sim_msgs__msg__high_cmd__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * sim_msgs__msg__high_cmd__convert_to_py(void * raw_ros_message);
bool sim_msgs__msg__high_cmd__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * sim_msgs__msg__high_cmd__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool sim_msgs__srv__controller__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[44];
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
    assert(strncmp("sim_msgs.srv._controller.Controller_Request", full_classname_dest, 43) == 0);
  }
  sim_msgs__srv__Controller_Request * ros_message = _ros_message;
  {  // state
    PyObject * field = PyObject_GetAttrString(_pymsg, "state");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->state = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // team0
    PyObject * field = PyObject_GetAttrString(_pymsg, "team0");
    if (!field) {
      return false;
    }
    if (!sim_msgs__msg__high_cmd__convert_from_py(field, &ros_message->team0)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // team1
    PyObject * field = PyObject_GetAttrString(_pymsg, "team1");
    if (!field) {
      return false;
    }
    if (!sim_msgs__msg__high_cmd__convert_from_py(field, &ros_message->team1)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // team2
    PyObject * field = PyObject_GetAttrString(_pymsg, "team2");
    if (!field) {
      return false;
    }
    if (!sim_msgs__msg__high_cmd__convert_from_py(field, &ros_message->team2)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * sim_msgs__srv__controller__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Controller_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("sim_msgs.srv._controller");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Controller_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  sim_msgs__srv__Controller_Request * ros_message = (sim_msgs__srv__Controller_Request *)raw_ros_message;
  {  // state
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->state);
    {
      int rc = PyObject_SetAttrString(_pymessage, "state", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // team0
    PyObject * field = NULL;
    field = sim_msgs__msg__high_cmd__convert_to_py(&ros_message->team0);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "team0", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // team1
    PyObject * field = NULL;
    field = sim_msgs__msg__high_cmd__convert_to_py(&ros_message->team1);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "team1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // team2
    PyObject * field = NULL;
    field = sim_msgs__msg__high_cmd__convert_to_py(&ros_message->team2);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "team2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "sim_msgs/srv/detail/controller__struct.h"
// already included above
// #include "sim_msgs/srv/detail/controller__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool sim_msgs__srv__controller__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[45];
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
    assert(strncmp("sim_msgs.srv._controller.Controller_Response", full_classname_dest, 44) == 0);
  }
  sim_msgs__srv__Controller_Response * ros_message = _ros_message;
  {  // success
    PyObject * field = PyObject_GetAttrString(_pymsg, "success");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->success = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * sim_msgs__srv__controller__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Controller_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("sim_msgs.srv._controller");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Controller_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  sim_msgs__srv__Controller_Response * ros_message = (sim_msgs__srv__Controller_Response *)raw_ros_message;
  {  // success
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->success ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "success", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
