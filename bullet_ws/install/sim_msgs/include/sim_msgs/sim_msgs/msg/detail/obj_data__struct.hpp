// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_msgs:msg/ObjData.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__OBJ_DATA__STRUCT_HPP_
#define SIM_MSGS__MSG__DETAIL__OBJ_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__sim_msgs__msg__ObjData __attribute__((deprecated))
#else
# define DEPRECATED__sim_msgs__msg__ObjData __declspec(deprecated)
#endif

namespace sim_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ObjData_
{
  using Type = ObjData_<ContainerAllocator>;

  explicit ObjData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->obj_id = 0l;
      this->current = false;
      this->x = 0.0;
      this->y = 0.0;
      this->theta = 0.0;
      this->vx = 0.0;
      this->vy = 0.0;
      this->w = 0.0;
    }
  }

  explicit ObjData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->obj_id = 0l;
      this->current = false;
      this->x = 0.0;
      this->y = 0.0;
      this->theta = 0.0;
      this->vx = 0.0;
      this->vy = 0.0;
      this->w = 0.0;
    }
  }

  // field types and members
  using _obj_id_type =
    int32_t;
  _obj_id_type obj_id;
  using _current_type =
    bool;
  _current_type current;
  using _x_type =
    double;
  _x_type x;
  using _y_type =
    double;
  _y_type y;
  using _theta_type =
    double;
  _theta_type theta;
  using _vx_type =
    double;
  _vx_type vx;
  using _vy_type =
    double;
  _vy_type vy;
  using _w_type =
    double;
  _w_type w;

  // setters for named parameter idiom
  Type & set__obj_id(
    const int32_t & _arg)
  {
    this->obj_id = _arg;
    return *this;
  }
  Type & set__current(
    const bool & _arg)
  {
    this->current = _arg;
    return *this;
  }
  Type & set__x(
    const double & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const double & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__theta(
    const double & _arg)
  {
    this->theta = _arg;
    return *this;
  }
  Type & set__vx(
    const double & _arg)
  {
    this->vx = _arg;
    return *this;
  }
  Type & set__vy(
    const double & _arg)
  {
    this->vy = _arg;
    return *this;
  }
  Type & set__w(
    const double & _arg)
  {
    this->w = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_msgs::msg::ObjData_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_msgs::msg::ObjData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_msgs::msg::ObjData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_msgs::msg::ObjData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_msgs::msg::ObjData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::msg::ObjData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_msgs::msg::ObjData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::msg::ObjData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_msgs::msg::ObjData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_msgs::msg::ObjData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_msgs__msg__ObjData
    std::shared_ptr<sim_msgs::msg::ObjData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_msgs__msg__ObjData
    std::shared_ptr<sim_msgs::msg::ObjData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ObjData_ & other) const
  {
    if (this->obj_id != other.obj_id) {
      return false;
    }
    if (this->current != other.current) {
      return false;
    }
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->theta != other.theta) {
      return false;
    }
    if (this->vx != other.vx) {
      return false;
    }
    if (this->vy != other.vy) {
      return false;
    }
    if (this->w != other.w) {
      return false;
    }
    return true;
  }
  bool operator!=(const ObjData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ObjData_

// alias to use template instance with default allocator
using ObjData =
  sim_msgs::msg::ObjData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sim_msgs

#endif  // SIM_MSGS__MSG__DETAIL__OBJ_DATA__STRUCT_HPP_
