// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_msgs:msg/LowCmd.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__LOW_CMD__BUILDER_HPP_
#define SIM_MSGS__MSG__DETAIL__LOW_CMD__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_msgs/msg/detail/low_cmd__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_msgs
{

namespace msg
{

namespace builder
{

class Init_LowCmd_dtheta
{
public:
  explicit Init_LowCmd_dtheta(::sim_msgs::msg::LowCmd & msg)
  : msg_(msg)
  {}
  ::sim_msgs::msg::LowCmd dtheta(::sim_msgs::msg::LowCmd::_dtheta_type arg)
  {
    msg_.dtheta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_msgs::msg::LowCmd msg_;
};

class Init_LowCmd_vy
{
public:
  explicit Init_LowCmd_vy(::sim_msgs::msg::LowCmd & msg)
  : msg_(msg)
  {}
  Init_LowCmd_dtheta vy(::sim_msgs::msg::LowCmd::_vy_type arg)
  {
    msg_.vy = std::move(arg);
    return Init_LowCmd_dtheta(msg_);
  }

private:
  ::sim_msgs::msg::LowCmd msg_;
};

class Init_LowCmd_vx
{
public:
  explicit Init_LowCmd_vx(::sim_msgs::msg::LowCmd & msg)
  : msg_(msg)
  {}
  Init_LowCmd_vy vx(::sim_msgs::msg::LowCmd::_vx_type arg)
  {
    msg_.vx = std::move(arg);
    return Init_LowCmd_vy(msg_);
  }

private:
  ::sim_msgs::msg::LowCmd msg_;
};

class Init_LowCmd_local
{
public:
  explicit Init_LowCmd_local(::sim_msgs::msg::LowCmd & msg)
  : msg_(msg)
  {}
  Init_LowCmd_vx local(::sim_msgs::msg::LowCmd::_local_type arg)
  {
    msg_.local = std::move(arg);
    return Init_LowCmd_vx(msg_);
  }

private:
  ::sim_msgs::msg::LowCmd msg_;
};

class Init_LowCmd_robot_id
{
public:
  Init_LowCmd_robot_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LowCmd_local robot_id(::sim_msgs::msg::LowCmd::_robot_id_type arg)
  {
    msg_.robot_id = std::move(arg);
    return Init_LowCmd_local(msg_);
  }

private:
  ::sim_msgs::msg::LowCmd msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_msgs::msg::LowCmd>()
{
  return sim_msgs::msg::builder::Init_LowCmd_robot_id();
}

}  // namespace sim_msgs

#endif  // SIM_MSGS__MSG__DETAIL__LOW_CMD__BUILDER_HPP_
