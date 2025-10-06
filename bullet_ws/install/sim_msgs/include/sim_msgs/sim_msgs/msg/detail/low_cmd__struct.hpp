// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_msgs:msg/LowCmd.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__LOW_CMD__STRUCT_HPP_
#define SIM_MSGS__MSG__DETAIL__LOW_CMD__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__sim_msgs__msg__LowCmd __attribute__((deprecated))
#else
# define DEPRECATED__sim_msgs__msg__LowCmd __declspec(deprecated)
#endif

namespace sim_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LowCmd_
{
  using Type = LowCmd_<ContainerAllocator>;

  explicit LowCmd_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->local = false;
      this->vx = 0.0;
      this->vy = 0.0;
      this->dtheta = 0.0;
    }
  }

  explicit LowCmd_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->local = false;
      this->vx = 0.0;
      this->vy = 0.0;
      this->dtheta = 0.0;
    }
  }

  // field types and members
  using _robot_id_type =
    int32_t;
  _robot_id_type robot_id;
  using _local_type =
    bool;
  _local_type local;
  using _vx_type =
    double;
  _vx_type vx;
  using _vy_type =
    double;
  _vy_type vy;
  using _dtheta_type =
    double;
  _dtheta_type dtheta;

  // setters for named parameter idiom
  Type & set__robot_id(
    const int32_t & _arg)
  {
    this->robot_id = _arg;
    return *this;
  }
  Type & set__local(
    const bool & _arg)
  {
    this->local = _arg;
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
  Type & set__dtheta(
    const double & _arg)
  {
    this->dtheta = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_msgs::msg::LowCmd_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_msgs::msg::LowCmd_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_msgs::msg::LowCmd_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_msgs::msg::LowCmd_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_msgs::msg::LowCmd_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::msg::LowCmd_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_msgs::msg::LowCmd_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::msg::LowCmd_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_msgs::msg::LowCmd_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_msgs::msg::LowCmd_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_msgs__msg__LowCmd
    std::shared_ptr<sim_msgs::msg::LowCmd_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_msgs__msg__LowCmd
    std::shared_ptr<sim_msgs::msg::LowCmd_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LowCmd_ & other) const
  {
    if (this->robot_id != other.robot_id) {
      return false;
    }
    if (this->local != other.local) {
      return false;
    }
    if (this->vx != other.vx) {
      return false;
    }
    if (this->vy != other.vy) {
      return false;
    }
    if (this->dtheta != other.dtheta) {
      return false;
    }
    return true;
  }
  bool operator!=(const LowCmd_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LowCmd_

// alias to use template instance with default allocator
using LowCmd =
  sim_msgs::msg::LowCmd_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sim_msgs

#endif  // SIM_MSGS__MSG__DETAIL__LOW_CMD__STRUCT_HPP_
