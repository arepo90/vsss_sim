// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_msgs:msg/HighCmd.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__HIGH_CMD__TRAITS_HPP_
#define SIM_MSGS__MSG__DETAIL__HIGH_CMD__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_msgs/msg/detail/high_cmd__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace sim_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const HighCmd & msg,
  std::ostream & out)
{
  out << "{";
  // member: robot_id
  {
    out << "robot_id: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_id, out);
    out << ", ";
  }

  // member: skill
  {
    out << "skill: ";
    rosidl_generator_traits::value_to_yaml(msg.skill, out);
    out << ", ";
  }

  // member: mod
  {
    out << "mod: ";
    rosidl_generator_traits::value_to_yaml(msg.mod, out);
    out << ", ";
  }

  // member: tgt_x
  {
    out << "tgt_x: ";
    rosidl_generator_traits::value_to_yaml(msg.tgt_x, out);
    out << ", ";
  }

  // member: tgt_y
  {
    out << "tgt_y: ";
    rosidl_generator_traits::value_to_yaml(msg.tgt_y, out);
    out << ", ";
  }

  // member: tgt_theta
  {
    out << "tgt_theta: ";
    rosidl_generator_traits::value_to_yaml(msg.tgt_theta, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const HighCmd & msg,
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

  // member: skill
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "skill: ";
    rosidl_generator_traits::value_to_yaml(msg.skill, out);
    out << "\n";
  }

  // member: mod
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "mod: ";
    rosidl_generator_traits::value_to_yaml(msg.mod, out);
    out << "\n";
  }

  // member: tgt_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tgt_x: ";
    rosidl_generator_traits::value_to_yaml(msg.tgt_x, out);
    out << "\n";
  }

  // member: tgt_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tgt_y: ";
    rosidl_generator_traits::value_to_yaml(msg.tgt_y, out);
    out << "\n";
  }

  // member: tgt_theta
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tgt_theta: ";
    rosidl_generator_traits::value_to_yaml(msg.tgt_theta, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const HighCmd & msg, bool use_flow_style = false)
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
  const sim_msgs::msg::HighCmd & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_msgs::msg::HighCmd & msg)
{
  return sim_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_msgs::msg::HighCmd>()
{
  return "sim_msgs::msg::HighCmd";
}

template<>
inline const char * name<sim_msgs::msg::HighCmd>()
{
  return "sim_msgs/msg/HighCmd";
}

template<>
struct has_fixed_size<sim_msgs::msg::HighCmd>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sim_msgs::msg::HighCmd>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sim_msgs::msg::HighCmd>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_MSGS__MSG__DETAIL__HIGH_CMD__TRAITS_HPP_
