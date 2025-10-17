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

class Init_FieldData_op2
{
public:
  explicit Init_FieldData_op2(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_score1 op2(::sim_msgs::msg::FieldData::_op2_type arg)
  {
    msg_.op2 = std::move(arg);
    return Init_FieldData_score1(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_op1
{
public:
  explicit Init_FieldData_op1(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_op2 op1(::sim_msgs::msg::FieldData::_op1_type arg)
  {
    msg_.op1 = std::move(arg);
    return Init_FieldData_op2(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_op0
{
public:
  explicit Init_FieldData_op0(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_op1 op0(::sim_msgs::msg::FieldData::_op0_type arg)
  {
    msg_.op0 = std::move(arg);
    return Init_FieldData_op1(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_team2
{
public:
  explicit Init_FieldData_team2(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_op0 team2(::sim_msgs::msg::FieldData::_team2_type arg)
  {
    msg_.team2 = std::move(arg);
    return Init_FieldData_op0(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_team1
{
public:
  explicit Init_FieldData_team1(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_team2 team1(::sim_msgs::msg::FieldData::_team1_type arg)
  {
    msg_.team1 = std::move(arg);
    return Init_FieldData_team2(msg_);
  }

private:
  ::sim_msgs::msg::FieldData msg_;
};

class Init_FieldData_team0
{
public:
  explicit Init_FieldData_team0(::sim_msgs::msg::FieldData & msg)
  : msg_(msg)
  {}
  Init_FieldData_team1 team0(::sim_msgs::msg::FieldData::_team0_type arg)
  {
    msg_.team0 = std::move(arg);
    return Init_FieldData_team1(msg_);
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
  Init_FieldData_team0 ball(::sim_msgs::msg::FieldData::_ball_type arg)
  {
    msg_.ball = std::move(arg);
    return Init_FieldData_team0(msg_);
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
