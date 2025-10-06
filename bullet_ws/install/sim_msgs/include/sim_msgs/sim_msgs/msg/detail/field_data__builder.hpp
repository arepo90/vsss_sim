// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_msgs:msg/FieldData.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__FIELD_DATA__BUILDER_HPP_
#define SIM_MSGS__MSG__DETAIL__FIELD_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_msgs/msg/detail/field_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_msgs
{

namespace msg
{

namespace builder
{

class Init_FieldData_score2
{
public:
  explicit Init_FieldData_score2(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  ::sim_msgs::msg::FieldData score2(::sim_msgs::msg::FieldData::_score2_type arg)
  {
    msg_.score2 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_score1
{
public:
  explicit Init_FieldData_score1(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_score2 score1(::sim_msgs::msg::FieldData::_score1_type arg)
  {
    msg_.score1 = std::move(arg);
    return Init_FieldData_score2(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_robot5
{
public:
  explicit Init_FieldData_robot5(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_score1 robot5(::sim_msgs::msg::FieldData::_robot5_type arg)
  {
    msg_.robot5 = std::move(arg);
    return Init_FieldData_score1(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_robot4
{
public:
  explicit Init_FieldData_robot4(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_robot5 robot4(::sim_msgs::msg::FieldData::_robot4_type arg)
  {
    msg_.robot4 = std::move(arg);
    return Init_FieldData_robot5(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_robot3
{
public:
  explicit Init_FieldData_robot3(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_robot4 robot3(::sim_msgs::msg::FieldData::_robot3_type arg)
  {
    msg_.robot3 = std::move(arg);
    return Init_FieldData_robot4(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_robot2
{
public:
  explicit Init_FieldData_robot2(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_robot3 robot2(::sim_msgs::msg::FieldData::_robot2_type arg)
  {
    msg_.robot2 = std::move(arg);
    return Init_FieldData_robot3(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_robot1
{
public:
  explicit Init_FieldData_robot1(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_robot2 robot1(::sim_msgs::msg::FieldData::_robot1_type arg)
  {
    msg_.robot1 = std::move(arg);
    return Init_FieldData_robot2(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_robot0
{
public:
  explicit Init_FieldData_robot0(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_robot1 robot0(::sim_msgs::msg::FieldData::_robot0_type arg)
  {
    msg_.robot0 = std::move(arg);
    return Init_FieldData_robot1(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_ball
{
public:
  Init_FieldData_ball()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FieldData_robot0 ball(::sim_msgs::msg::FieldData::_ball_type arg)
  {
    msg_.ball = std::move(arg);
    return Init_FieldData_robot0(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_msgs::msg::FieldData>()
{
  return sim_msgs::msg::builder::Init_FieldData_ball();
}

}  // namespace sim_msgs

#endif  // SIM_MSGS__MSG__DETAIL__FIELD_DATA__BUILDER_HPP_
