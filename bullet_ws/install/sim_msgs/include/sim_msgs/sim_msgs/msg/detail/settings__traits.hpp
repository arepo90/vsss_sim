// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_msgs:msg/Settings.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__SETTINGS__TRAITS_HPP_
#define SIM_MSGS__MSG__DETAIL__SETTINGS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_msgs/msg/detail/settings__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace sim_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Settings & msg,
  std::ostream & out)
{
  out << "{";
  // member: team_color
  {
    out << "team_color: ";
    rosidl_generator_traits::value_to_yaml(msg.team_color, out);
    out << ", ";
  }

  // member: team_side
  {
    out << "team_side: ";
    rosidl_generator_traits::value_to_yaml(msg.team_side, out);
    out << ", ";
  }

  // member: local
  {
    out << "local: ";
    rosidl_generator_traits::value_to_yaml(msg.local, out);
    out << ", ";
  }

  // member: reset
  {
    out << "reset: ";
    rosidl_generator_traits::value_to_yaml(msg.reset, out);
    out << ", ";
  }

  // member: exposure
  {
    out << "exposure: ";
    rosidl_generator_traits::value_to_yaml(msg.exposure, out);
    out << ", ";
  }

  // member: attractive_gain
  {
    out << "attractive_gain: ";
    rosidl_generator_traits::value_to_yaml(msg.attractive_gain, out);
    out << ", ";
  }

  // member: repulsive_gain
  {
    out << "repulsive_gain: ";
    rosidl_generator_traits::value_to_yaml(msg.repulsive_gain, out);
    out << ", ";
  }

  // member: repulsion_radius
  {
    out << "repulsion_radius: ";
    rosidl_generator_traits::value_to_yaml(msg.repulsion_radius, out);
    out << ", ";
  }

  // member: goal_tolerance
  {
    out << "goal_tolerance: ";
    rosidl_generator_traits::value_to_yaml(msg.goal_tolerance, out);
    out << ", ";
  }

  // member: tangential_gain
  {
    out << "tangential_gain: ";
    rosidl_generator_traits::value_to_yaml(msg.tangential_gain, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Settings & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: team_color
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "team_color: ";
    rosidl_generator_traits::value_to_yaml(msg.team_color, out);
    out << "\n";
  }

  // member: team_side
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "team_side: ";
    rosidl_generator_traits::value_to_yaml(msg.team_side, out);
    out << "\n";
  }

  // member: local
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "local: ";
    rosidl_generator_traits::value_to_yaml(msg.local, out);
    out << "\n";
  }

  // member: reset
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "reset: ";
    rosidl_generator_traits::value_to_yaml(msg.reset, out);
    out << "\n";
  }

  // member: exposure
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "exposure: ";
    rosidl_generator_traits::value_to_yaml(msg.exposure, out);
    out << "\n";
  }

  // member: attractive_gain
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "attractive_gain: ";
    rosidl_generator_traits::value_to_yaml(msg.attractive_gain, out);
    out << "\n";
  }

  // member: repulsive_gain
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "repulsive_gain: ";
    rosidl_generator_traits::value_to_yaml(msg.repulsive_gain, out);
    out << "\n";
  }

  // member: repulsion_radius
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "repulsion_radius: ";
    rosidl_generator_traits::value_to_yaml(msg.repulsion_radius, out);
    out << "\n";
  }

  // member: goal_tolerance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_tolerance: ";
    rosidl_generator_traits::value_to_yaml(msg.goal_tolerance, out);
    out << "\n";
  }

  // member: tangential_gain
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tangential_gain: ";
    rosidl_generator_traits::value_to_yaml(msg.tangential_gain, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Settings & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace sim_msgs

namespace rosidl_generator_traits
{

[[deprecated("use sim_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const sim_msgs::msg::Settings & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_msgs::msg::Settings & msg)
{
  return sim_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_msgs::msg::Settings>()
{
  return "sim_msgs::msg::Settings";
}

template<>
inline const char * name<sim_msgs::msg::Settings>()
{
  return "sim_msgs/msg/Settings";
}

template<>
struct has_fixed_size<sim_msgs::msg::Settings>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sim_msgs::msg::Settings>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sim_msgs::msg::Settings>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_MSGS__MSG__DETAIL__SETTINGS__TRAITS_HPP_
