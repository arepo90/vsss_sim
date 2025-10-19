// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_msgs:msg/HighCmd.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__HIGH_CMD__STRUCT_HPP_
#define SIM_MSGS__MSG__DETAIL__HIGH_CMD__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__sim_msgs__msg__HighCmd __attribute__((deprecated))
#else
# define DEPRECATED__sim_msgs__msg__HighCmd __declspec(deprecated)
#endif

namespace sim_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct HighCmd_
{
  using Type = HighCmd_<ContainerAllocator>;

  explicit HighCmd_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->skill = 0l;
      this->mod = 0l;
      this->tgt_x = 0.0;
      this->tgt_y = 0.0;
      this->tgt_theta = 0.0;
    }
  }

  explicit HighCmd_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->skill = 0l;
      this->mod = 0l;
      this->tgt_x = 0.0;
      this->tgt_y = 0.0;
      this->tgt_theta = 0.0;
    }
  }

  // field types and members
  using _robot_id_type =
    int32_t;
  _robot_id_type robot_id;
  using _skill_type =
    int32_t;
  _skill_type skill;
  using _mod_type =
    int32_t;
  _mod_type mod;
  using _tgt_x_type =
    double;
  _tgt_x_type tgt_x;
  using _tgt_y_type =
    double;
  _tgt_y_type tgt_y;
  using _tgt_theta_type =
    double;
  _tgt_theta_type tgt_theta;

  // setters for named parameter idiom
  Type & set__robot_id(
    const int32_t & _arg)
  {
    this->robot_id = _arg;
    return *this;
  }
  Type & set__skill(
    const int32_t & _arg)
  {
    this->skill = _arg;
    return *this;
  }
  Type & set__mod(
    const int32_t & _arg)
  {
    this->mod = _arg;
    return *this;
  }
  Type & set__tgt_x(
    const double & _arg)
  {
    this->tgt_x = _arg;
    return *this;
  }
  Type & set__tgt_y(
    const double & _arg)
  {
    this->tgt_y = _arg;
    return *this;
  }
  Type & set__tgt_theta(
    const double & _arg)
  {
    this->tgt_theta = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_msgs::msg::HighCmd_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_msgs::msg::HighCmd_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_msgs::msg::HighCmd_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_msgs::msg::HighCmd_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_msgs::msg::HighCmd_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::msg::HighCmd_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_msgs::msg::HighCmd_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::msg::HighCmd_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_msgs::msg::HighCmd_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_msgs::msg::HighCmd_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_msgs__msg__HighCmd
    std::shared_ptr<sim_msgs::msg::HighCmd_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_msgs__msg__HighCmd
    std::shared_ptr<sim_msgs::msg::HighCmd_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const HighCmd_ & other) const
  {
    if (this->robot_id != other.robot_id) {
      return false;
    }
    if (this->skill != other.skill) {
      return false;
    }
    if (this->mod != other.mod) {
      return false;
    }
    if (this->tgt_x != other.tgt_x) {
      return false;
    }
    if (this->tgt_y != other.tgt_y) {
      return false;
    }
    if (this->tgt_theta != other.tgt_theta) {
      return false;
    }
    return true;
  }
  bool operator!=(const HighCmd_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct HighCmd_

// alias to use template instance with default allocator
using HighCmd =
  sim_msgs::msg::HighCmd_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sim_msgs

#endif  // SIM_MSGS__MSG__DETAIL__HIGH_CMD__STRUCT_HPP_
