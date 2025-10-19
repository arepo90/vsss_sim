// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_msgs:srv/Reset.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__SRV__DETAIL__RESET__BUILDER_HPP_
#define SIM_MSGS__SRV__DETAIL__RESET__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_msgs/srv/detail/reset__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_msgs
{

namespace srv
{

namespace builder
{

class Init_Reset_Request_settings
{
public:
  Init_Reset_Request_settings()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::sim_msgs::srv::Reset_Request settings(::sim_msgs::srv::Reset_Request::_settings_type arg)
  {
    msg_.settings = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_msgs::srv::Reset_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_msgs::srv::Reset_Request>()
{
  return sim_msgs::srv::builder::Init_Reset_Request_settings();
}

}  // namespace sim_msgs


namespace sim_msgs
{

namespace srv
{

namespace builder
{

class Init_Reset_Response_success
{
public:
  Init_Reset_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::sim_msgs::srv::Reset_Response success(::sim_msgs::srv::Reset_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_msgs::srv::Reset_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_msgs::srv::Reset_Response>()
{
  return sim_msgs::srv::builder::Init_Reset_Response_success();
}

}  // namespace sim_msgs

#endif  // SIM_MSGS__SRV__DETAIL__RESET__BUILDER_HPP_
