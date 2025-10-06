// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_msgs:msg/LowCmd.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__LOW_CMD__TRAITS_HPP_
#define SIM_MSGS__MSG__DETAIL__LOW_CMD__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_msgs/msg/detail/low_cmd__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace sim_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const LowCmd & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_id
  {
    out << "robot_id: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_id, out);
    out << ", ";
  }

  // member: local
  {
    out << "local: ";
    rosidl_generator_traits::value_to_yaml(msg.local, out);
    out << ", ";
  }

  // member: vx
  {
    out << "vx: ";
    rosidl_generator_traits::value_to_yaml(msg.vx, out);
    out << ", ";
  }

  // member: vy
  {
    out << "vy: ";
    rosidl_generator_traits::value_to_yaml(msg.vy, out);
    out << ", ";
  }

  // member: dtheta
  {
    out << "dtheta: ";
    rosidl_generator_traits::value_to_yaml(msg.dtheta, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const LowCmd & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: robot_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_id: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_id, out);
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

  // member: vx
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vx: ";
    rosidl_generator_traits::value_to_yaml(msg.vx, out);
    out << "\n";
  }

  // member: vy
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vy: ";
    rosidl_generator_traits::value_to_yaml(msg.vy, out);
    out << "\n";
  }

  // member: dtheta
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "dtheta: ";
    rosidl_generator_traits::value_to_yaml(msg.dtheta, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const LowCmd & msg, bool use_flow_style = false)
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
  const sim_msgs::msg::LowCmd & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_msgs::msg::LowCmd & msg)
{
  return sim_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_msgs::msg::LowCmd>()
{
  return "sim_msgs::msg::LowCmd";
}

template<>
inline const char * name<sim_msgs::msg::LowCmd>()
{
  return "sim_msgs/msg/LowCmd";
}

template<>
struct has_fixed_size<sim_msgs::msg::LowCmd>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sim_msgs::msg::LowCmd>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sim_msgs::msg::LowCmd>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_MSGS__MSG__DETAIL__LOW_CMD__TRAITS_HPP_
