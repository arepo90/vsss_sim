// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_msgs:msg/HighCmd.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__HIGH_CMD__BUILDER_HPP_
#define SIM_MSGS__MSG__DETAIL__HIGH_CMD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_msgs/msg/detail/high_cmd__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_msgs
{

namespace msg
{

namespace builder
{

class Init_HighCmd_tgt_theta
{
public:
  explicit Init_HighCmd_tgt_theta(::sim_msgs::msg::HighCmd & msg)
  : msg_(msg)
  {}
  ::sim_msgs::msg::HighCmd tgt_theta(::sim_msgs::msg::HighCmd::_tgt_theta_type arg)
  {
    msg_.tgt_theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_msgs::msg::HighCmd msg_;
};

class Init_HighCmd_tgt_y
{
public:
  explicit Init_HighCmd_tgt_y(::sim_msgs::msg::HighCmd & msg)
  : msg_(msg)
  {}
  Init_HighCmd_tgt_theta tgt_y(::sim_msgs::msg::HighCmd::_tgt_y_type arg)
  {
    msg_.tgt_y = std::move(arg);
    return Init_HighCmd_tgt_theta(msg_);
  }

private:
  ::sim_msgs::msg::HighCmd msg_;
};

class Init_HighCmd_tgt_x
{
public:
  explicit Init_HighCmd_tgt_x(::sim_msgs::msg::HighCmd & msg)
  : msg_(msg)
  {}
  Init_HighCmd_tgt_y tgt_x(::sim_msgs::msg::HighCmd::_tgt_x_type arg)
  {
    msg_.tgt_x = std::move(arg);
    return Init_HighCmd_tgt_y(msg_);
  }

private:
  ::sim_msgs::msg::HighCmd msg_;
};

class Init_HighCmd_mod
{
public:
  explicit Init_HighCmd_mod(::sim_msgs::msg::HighCmd & msg)
  : msg_(msg)
  {}
  Init_HighCmd_tgt_x mod(::sim_msgs::msg::HighCmd::_mod_type arg)
  {
    msg_.mod = std::move(arg);
    return Init_HighCmd_tgt_x(msg_);
  }

private:
  ::sim_msgs::msg::HighCmd msg_;
};

class Init_HighCmd_skill
{
public:
  explicit Init_HighCmd_skill(::sim_msgs::msg::HighCmd & msg)
  : msg_(msg)
  {}
  Init_HighCmd_mod skill(::sim_msgs::msg::HighCmd::_skill_type arg)
  {
    msg_.skill = std::move(arg);
    return Init_HighCmd_mod(msg_);
  }

private:
  ::sim_msgs::msg::HighCmd msg_;
};

class Init_HighCmd_robot_id
{
public:
  Init_HighCmd_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_HighCmd_skill robot_id(::sim_msgs::msg::HighCmd::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_HighCmd_skill(msg_);
  }

private:
  ::sim_msgs::msg::HighCmd msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_msgs::msg::HighCmd>()
{
  return sim_msgs::msg::builder::Init_HighCmd_robot_id();
}

}  // namespace sim_msgs

#endif  // SIM_MSGS__MSG__DETAIL__HIGH_CMD__BUILDER_HPP_
