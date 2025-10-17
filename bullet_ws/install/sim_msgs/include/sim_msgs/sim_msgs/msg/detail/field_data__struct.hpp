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
// Member 'team0'
// Member 'team1'
// Member 'team2'
// Member 'op0'
// Member 'op1'
// Member 'op2'
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
    team0(_init),
    team1(_init),
    team2(_init),
    op0(_init),
    op1(_init),
    op2(_init)
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
    team0(_alloc, _init),
    team1(_alloc, _init),
    team2(_alloc, _init),
    op0(_alloc, _init),
    op1(_alloc, _init),
    op2(_alloc, _init)
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
  using _team0_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _team0_type team0;
  using _team1_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _team1_type team1;
  using _team2_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _team2_type team2;
  using _op0_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _op0_type op0;
  using _op1_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _op1_type op1;
  using _op2_type =
    sim_msgs::msg::ObjData_<ContainerAllocator>;
  _op2_type op2;
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
  Type & set__team0(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->team0 = _arg;
    return *this;
  }
  Type & set__team1(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->team1 = _arg;
    return *this;
  }
  Type & set__team2(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->team2 = _arg;
    return *this;
  }
  Type & set__op0(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->op0 = _arg;
    return *this;
  }
  Type & set__op1(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->op1 = _arg;
    return *this;
  }
  Type & set__op2(
    const sim_msgs::msg::ObjData_<ContainerAllocator> & _arg)
  {
    this->op2 = _arg;
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
    if (this->team0 != other.team0) {
      return false;
    }
    if (this->team1 != other.team1) {
      return false;
    }
    if (this->team2 != other.team2) {
      return false;
    }
    if (this->op0 != other.op0) {
      return false;
    }
    if (this->op1 != other.op1) {
      return false;
    }
    if (this->op2 != other.op2) {
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
