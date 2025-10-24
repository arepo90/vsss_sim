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
      this->team_color = false;
      this->team_side = false;
      this->local = false;
      this->reset = false;
      this->exposure = 0l;
      this->robot0 = 0l;
      this->robot1 = 0l;
      this->robot2 = 0l;
      this->attractive_gain = 0.0;
      this->repulsive_gain = 0.0;
      this->repulsion_radius = 0.0;
      this->goal_tolerance = 0.0;
      this->tangential_gain = 0.0;
      this->target_offset = 0.0;
      this->colinearity = 0.0;
    }
  }

  explicit Settings_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->team_color = false;
      this->team_side = false;
      this->local = false;
      this->reset = false;
      this->exposure = 0l;
      this->robot0 = 0l;
      this->robot1 = 0l;
      this->robot2 = 0l;
      this->attractive_gain = 0.0;
      this->repulsive_gain = 0.0;
      this->repulsion_radius = 0.0;
      this->goal_tolerance = 0.0;
      this->tangential_gain = 0.0;
      this->target_offset = 0.0;
      this->colinearity = 0.0;
    }
  }

  // field types and members
  using _team_color_type =
    bool;
  _team_color_type team_color;
  using _team_side_type =
    bool;
  _team_side_type team_side;
  using _local_type =
    bool;
  _local_type local;
  using _reset_type =
    bool;
  _reset_type reset;
  using _exposure_type =
    int32_t;
  _exposure_type exposure;
  using _robot0_type =
    int32_t;
  _robot0_type robot0;
  using _robot1_type =
    int32_t;
  _robot1_type robot1;
  using _robot2_type =
    int32_t;
  _robot2_type robot2;
  using _attractive_gain_type =
    double;
  _attractive_gain_type attractive_gain;
  using _repulsive_gain_type =
    double;
  _repulsive_gain_type repulsive_gain;
  using _repulsion_radius_type =
    double;
  _repulsion_radius_type repulsion_radius;
  using _goal_tolerance_type =
    double;
  _goal_tolerance_type goal_tolerance;
  using _tangential_gain_type =
    double;
  _tangential_gain_type tangential_gain;
  using _target_offset_type =
    double;
  _target_offset_type target_offset;
  using _colinearity_type =
    double;
  _colinearity_type colinearity;

  // setters for named parameter idiom
  Type & set__team_color(
    const bool & _arg)
  {
    this->team_color = _arg;
    return *this;
  }
  Type & set__team_side(
    const bool & _arg)
  {
    this->team_side = _arg;
    return *this;
  }
  Type & set__local(
    const bool & _arg)
  {
    this->local = _arg;
    return *this;
  }
  Type & set__reset(
    const bool & _arg)
  {
    this->reset = _arg;
    return *this;
  }
  Type & set__exposure(
    const int32_t & _arg)
  {
    this->exposure = _arg;
    return *this;
  }
  Type & set__robot0(
    const int32_t & _arg)
  {
    this->robot0 = _arg;
    return *this;
  }
  Type & set__robot1(
    const int32_t & _arg)
  {
    this->robot1 = _arg;
    return *this;
  }
  Type & set__robot2(
    const int32_t & _arg)
  {
    this->robot2 = _arg;
    return *this;
  }
  Type & set__attractive_gain(
    const double & _arg)
  {
    this->attractive_gain = _arg;
    return *this;
  }
  Type & set__repulsive_gain(
    const double & _arg)
  {
    this->repulsive_gain = _arg;
    return *this;
  }
  Type & set__repulsion_radius(
    const double & _arg)
  {
    this->repulsion_radius = _arg;
    return *this;
  }
  Type & set__goal_tolerance(
    const double & _arg)
  {
    this->goal_tolerance = _arg;
    return *this;
  }
  Type & set__tangential_gain(
    const double & _arg)
  {
    this->tangential_gain = _arg;
    return *this;
  }
  Type & set__target_offset(
    const double & _arg)
  {
    this->target_offset = _arg;
    return *this;
  }
  Type & set__colinearity(
    const double & _arg)
  {
    this->colinearity = _arg;
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
    if (this->team_color != other.team_color) {
      return false;
    }
    if (this->team_side != other.team_side) {
      return false;
    }
    if (this->local != other.local) {
      return false;
    }
    if (this->reset != other.reset) {
      return false;
    }
    if (this->exposure != other.exposure) {
      return false;
    }
    if (this->robot0 != other.robot0) {
      return false;
    }
    if (this->robot1 != other.robot1) {
      return false;
    }
    if (this->robot2 != other.robot2) {
      return false;
    }
    if (this->attractive_gain != other.attractive_gain) {
      return false;
    }
    if (this->repulsive_gain != other.repulsive_gain) {
      return false;
    }
    if (this->repulsion_radius != other.repulsion_radius) {
      return false;
    }
    if (this->goal_tolerance != other.goal_tolerance) {
      return false;
    }
    if (this->tangential_gain != other.tangential_gain) {
      return false;
    }
    if (this->target_offset != other.target_offset) {
      return false;
    }
    if (this->colinearity != other.colinearity) {
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
