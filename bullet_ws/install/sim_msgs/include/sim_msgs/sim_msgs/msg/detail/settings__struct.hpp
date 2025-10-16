// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_msgs:msg/Settings.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__SETTINGS__STRUCT_HPP_
#define SIM_MSGS__MSG__DETAIL__SETTINGS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__sim_msgs__msg__Settings __attribute__((deprecated))
#else
# define DEPRECATED__sim_msgs__msg__Settings __declspec(deprecated)
#endif

namespace sim_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Settings_
{
  using Type = Settings_<ContainerAllocator>;

  explicit Settings_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->friendly_color = false;
      this->friendly_side = false;
      this->exposure = 0l;
    }
  }

  explicit Settings_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->friendly_color = false;
      this->friendly_side = false;
      this->exposure = 0l;
    }
  }

  // field types and members
  using _friendly_color_type =
    bool;
  _friendly_color_type friendly_color;
  using _friendly_side_type =
    bool;
  _friendly_side_type friendly_side;
  using _exposure_type =
    int32_t;
  _exposure_type exposure;

  // setters for named parameter idiom
  Type & set__friendly_color(
    const bool & _arg)
  {
    this->friendly_color = _arg;
    return *this;
  }
  Type & set__friendly_side(
    const bool & _arg)
  {
    this->friendly_side = _arg;
    return *this;
  }
  Type & set__exposure(
    const int32_t & _arg)
  {
    this->exposure = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_msgs::msg::Settings_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_msgs::msg::Settings_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_msgs::msg::Settings_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_msgs::msg::Settings_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_msgs::msg::Settings_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::msg::Settings_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_msgs::msg::Settings_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::msg::Settings_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_msgs::msg::Settings_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_msgs::msg::Settings_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_msgs__msg__Settings
    std::shared_ptr<sim_msgs::msg::Settings_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_msgs__msg__Settings
    std::shared_ptr<sim_msgs::msg::Settings_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Settings_ & other) const
  {
    if (this->friendly_color != other.friendly_color) {
      return false;
    }
    if (this->friendly_side != other.friendly_side) {
      return false;
    }
    if (this->exposure != other.exposure) {
      return false;
    }
    return true;
  }
  bool operator!=(const Settings_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Settings_

// alias to use template instance with default allocator
using Settings =
  sim_msgs::msg::Settings_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sim_msgs

#endif  // SIM_MSGS__MSG__DETAIL__SETTINGS__STRUCT_HPP_
