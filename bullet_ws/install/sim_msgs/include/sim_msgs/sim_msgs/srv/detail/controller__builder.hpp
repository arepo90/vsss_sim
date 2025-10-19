// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_msgs:srv/Controller.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__SRV__DETAIL__CONTROLLER__BUILDER_HPP_
#define SIM_MSGS__SRV__DETAIL__CONTROLLER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_msgs/srv/detail/controller__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_msgs
{

namespace srv
{

namespace builder
{

class Init_Controller_Request_team2
{
public:
  explicit Init_Controller_Request_team2(::sim_msgs::srv::Controller_Request & msg)
  : msg_(msg)
  {}
  ::sim_msgs::srv::Controller_Request team2(::sim_msgs::srv::Controller_Request::_team2_type arg)
  {
    msg_.team2 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_msgs::srv::Controller_Request msg_;
};

class Init_Controller_Request_team1
{
public:
  explicit Init_Controller_Request_team1(::sim_msgs::srv::Controller_Request & msg)
  : msg_(msg)
  {}
  Init_Controller_Request_team2 team1(::sim_msgs::srv::Controller_Request::_team1_type arg)
  {
    msg_.team1 = std::move(arg);
    return Init_Controller_Request_team2(msg_);
  }

private:
  ::sim_msgs::srv::Controller_Request msg_;
};

class Init_Controller_Request_team0
{
public:
  explicit Init_Controller_Request_team0(::sim_msgs::srv::Controller_Request & msg)
  : msg_(msg)
  {}
  Init_Controller_Request_team1 team0(::sim_msgs::srv::Controller_Request::_team0_type arg)
  {
    msg_.team0 = std::move(arg);
    return Init_Controller_Request_team1(msg_);
  }

private:
  ::sim_msgs::srv::Controller_Request msg_;
};

class Init_Controller_Request_state
{
public:
  Init_Controller_Request_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Controller_Request_team0 state(::sim_msgs::srv::Controller_Request::_state_type arg)
  {
    msg_.state = std::move(arg);
    return Init_Controller_Request_team0(msg_);
  }

private:
  ::sim_msgs::srv::Controller_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_msgs::srv::Controller_Request>()
{
  return sim_msgs::srv::builder::Init_Controller_Request_state();
}

}  // namespace sim_msgs


namespace sim_msgs
{

namespace srv
{

namespace builder
{

class Init_Controller_Response_success
{
public:
  Init_Controller_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::sim_msgs::srv::Controller_Response success(::sim_msgs::srv::Controller_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_msgs::srv::Controller_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_msgs::srv::Controller_Response>()
{
  return sim_msgs::srv::builder::Init_Controller_Response_success();
}

}  // namespace sim_msgs

#endif  // SIM_MSGS__SRV__DETAIL__CONTROLLER__BUILDER_HPP_
