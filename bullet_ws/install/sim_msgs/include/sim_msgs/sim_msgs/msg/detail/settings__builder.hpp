// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_msgs:msg/Settings.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__SETTINGS__BUILDER_HPP_
#define SIM_MSGS__MSG__DETAIL__SETTINGS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_msgs/msg/detail/settings__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_msgs
{

namespace msg
{

namespace builder
{

class Init_Settings_tangential_gain
{
public:
  explicit Init_Settings_tangential_gain(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  ::sim_msgs::msg::Settings tangential_gain(::sim_msgs::msg::Settings::_tangential_gain_type arg)
  {
    msg_.tangential_gain = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_goal_tolerance
{
public:
  explicit Init_Settings_goal_tolerance(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  Init_Settings_tangential_gain goal_tolerance(::sim_msgs::msg::Settings::_goal_tolerance_type arg)
  {
    msg_.goal_tolerance = std::move(arg);
    return Init_Settings_tangential_gain(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_repulsion_radius
{
public:
  explicit Init_Settings_repulsion_radius(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  Init_Settings_goal_tolerance repulsion_radius(::sim_msgs::msg::Settings::_repulsion_radius_type arg)
  {
    msg_.repulsion_radius = std::move(arg);
    return Init_Settings_goal_tolerance(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_repulsive_gain
{
public:
  explicit Init_Settings_repulsive_gain(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  Init_Settings_repulsion_radius repulsive_gain(::sim_msgs::msg::Settings::_repulsive_gain_type arg)
  {
    msg_.repulsive_gain = std::move(arg);
    return Init_Settings_repulsion_radius(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_attractive_gain
{
public:
  explicit Init_Settings_attractive_gain(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  Init_Settings_repulsive_gain attractive_gain(::sim_msgs::msg::Settings::_attractive_gain_type arg)
  {
    msg_.attractive_gain = std::move(arg);
    return Init_Settings_repulsive_gain(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_robot2
{
public:
  explicit Init_Settings_robot2(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  Init_Settings_attractive_gain robot2(::sim_msgs::msg::Settings::_robot2_type arg)
  {
    msg_.robot2 = std::move(arg);
    return Init_Settings_attractive_gain(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_robot1
{
public:
  explicit Init_Settings_robot1(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  Init_Settings_robot2 robot1(::sim_msgs::msg::Settings::_robot1_type arg)
  {
    msg_.robot1 = std::move(arg);
    return Init_Settings_robot2(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_robot0
{
public:
  explicit Init_Settings_robot0(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  Init_Settings_robot1 robot0(::sim_msgs::msg::Settings::_robot0_type arg)
  {
    msg_.robot0 = std::move(arg);
    return Init_Settings_robot1(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_exposure
{
public:
  explicit Init_Settings_exposure(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  Init_Settings_robot0 exposure(::sim_msgs::msg::Settings::_exposure_type arg)
  {
    msg_.exposure = std::move(arg);
    return Init_Settings_robot0(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_reset
{
public:
  explicit Init_Settings_reset(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  Init_Settings_exposure reset(::sim_msgs::msg::Settings::_reset_type arg)
  {
    msg_.reset = std::move(arg);
    return Init_Settings_exposure(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_local
{
public:
  explicit Init_Settings_local(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  Init_Settings_reset local(::sim_msgs::msg::Settings::_local_type arg)
  {
    msg_.local = std::move(arg);
    return Init_Settings_reset(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_team_side
{
public:
  explicit Init_Settings_team_side(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  Init_Settings_local team_side(::sim_msgs::msg::Settings::_team_side_type arg)
  {
    msg_.team_side = std::move(arg);
    return Init_Settings_local(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_team_color
{
public:
  Init_Settings_team_color()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Settings_team_side team_color(::sim_msgs::msg::Settings::_team_color_type arg)
  {
    msg_.team_color = std::move(arg);
    return Init_Settings_team_side(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_msgs::msg::Settings>()
{
  return sim_msgs::msg::builder::Init_Settings_team_color();
}

}  // namespace sim_msgs

#endif  // SIM_MSGS__MSG__DETAIL__SETTINGS__BUILDER_HPP_
