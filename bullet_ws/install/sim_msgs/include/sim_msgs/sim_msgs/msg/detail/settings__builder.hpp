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

class Init_Settings_exposure
{
public:
  explicit Init_Settings_exposure(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  ::sim_msgs::msg::Settings exposure(::sim_msgs::msg::Settings::_exposure_type arg)
  {
    msg_.exposure = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_friendly_side
{
public:
  explicit Init_Settings_friendly_side(::sim_msgs::msg::Settings & msg)
  : msg_(msg)
  {}
  Init_Settings_exposure friendly_side(::sim_msgs::msg::Settings::_friendly_side_type arg)
  {
    msg_.friendly_side = std::move(arg);
    return Init_Settings_exposure(msg_);
  }

private:
  ::sim_msgs::msg::Settings msg_;
};

class Init_Settings_friendly_color
{
public:
  Init_Settings_friendly_color()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Settings_friendly_side friendly_color(::sim_msgs::msg::Settings::_friendly_color_type arg)
  {
    msg_.friendly_color = std::move(arg);
    return Init_Settings_friendly_side(msg_);
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
  return sim_msgs::msg::builder::Init_Settings_friendly_color();
}

}  // namespace sim_msgs

#endif  // SIM_MSGS__MSG__DETAIL__SETTINGS__BUILDER_HPP_
