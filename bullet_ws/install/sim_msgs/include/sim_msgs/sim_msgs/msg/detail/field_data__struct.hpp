// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_msgs:msg/FieldData.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__FIELD_DATA__STRUCT_HPP_
#define SIM_MSGS__MSG__DETAIL__FIELD_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'ball'
// Member 'robot0'
// Member 'robot1'
// Member 'robot2'
// Member 'robot3'
// Member 'robot4'
// Member 'robot5'
#include "sim_msgs/msg/detail/obj_data__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__sim_msgs__msg__FieldData __attribute__((deprecated))
#else
# define DEPRECATED__sim_msgs__msg__FieldData __declspec(deprecated)
#endif

namespace sim_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FieldData_
{
  using Type = FieldData_<ContainerAllocator>;

  explicit FieldData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ball(_init),
    robot0(_init),
    robot1(_init),
    robot2(_init),
    robot3(_init),
    robot4(_init),
    robot5(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->score1 = 0l;
      this->score2 = 0l;
    }
  }

  explicit FieldData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : ball(_alloc, _init),
    robot0(_alloc, _init),
    robot1(_alloc, _init),
    robot2(_alloc, _init),
    robot3(_alloc, _init),
    robot4(_alloc, _init),
    robot5(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->score1 = 0l;
      this->score2 = 0l;
    }
  }

  // field types and members
  using _ball_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _ball_type ball;
  using _robot0_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _robot0_type robot0;
  using _robot1_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _robot1_type robot1;
  using _robot2_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _robot2_type robot2;
  using _robot3_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _robot3_type robot3;
  using _robot4_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _robot4_type robot4;
  using _robot5_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _robot5_type robot5;
  using _score1_type =
    int32_t;
  _score1_type score1;
  using _score2_type =
    int32_t;
  _score2_type score2;

  // setters for named parameter idiom
  Type & set__ball(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->ball = _arg;
    return *this;
  }
  Type & set__robot0(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->robot0 = _arg;
    return *this;
  }
  Type & set__robot1(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->robot1 = _arg;
    return *this;
  }
  Type & set__robot2(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->robot2 = _arg;
    return *this;
  }
  Type & set__robot3(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->robot3 = _arg;
    return *this;
  }
  Type & set__robot4(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->robot4 = _arg;
    return *this;
  }
  Type & set__robot5(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->robot5 = _arg;
    return *this;
  }
  Type & set__score1(
    const int32_t & _arg)
  {
    this->score1 = _arg;
    return *this;
  }
  Type & set__score2(
    const int32_t & _arg)
  {
    this->score2 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_msgs::msg::FieldData_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_msgs::msg::FieldData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_msgs::msg::FieldData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_msgs::msg::FieldData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_msgs::msg::FieldData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::msg::FieldData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_msgs::msg::FieldData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::msg::FieldData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_msgs::msg::FieldData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_msgs::msg::FieldData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_msgs__msg__FieldData
    std::shared_ptr<sim_msgs::msg::FieldData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_msgs__msg__FieldData
    std::shared_ptr<sim_msgs::msg::FieldData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FieldData_ & other) const
  {
    if (this->ball != other.ball) {
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
    if (this->robot3 != other.robot3) {
      return false;
    }
    if (this->robot4 != other.robot4) {
      return false;
    }
    if (this->robot5 != other.robot5) {
      return false;
    }
    if (this->score1 != other.score1) {
      return false;
    }
    if (this->score2 != other.score2) {
      return false;
    }
    return true;
  }
  bool operator!=(const FieldData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FieldData_

// alias to use template instance with default allocator
using FieldData =
  sim_msgs::msg::FieldData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace sim_msgs

#endif  // SIM_MSGS__MSG__DETAIL__FIELD_DATA__STRUCT_HPP_
