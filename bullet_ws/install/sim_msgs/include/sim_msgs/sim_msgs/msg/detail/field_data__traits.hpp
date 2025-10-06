// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_msgs:msg/FieldData.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__FIELD_DATA__TRAITS_HPP_
#define SIM_MSGS__MSG__DETAIL__FIELD_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_msgs/msg/detail/field_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'ball'
// Member 'robot0'
// Member 'robot1'
// Member 'robot2'
// Member 'robot3'
// Member 'robot4'
// Member 'robot5'
#include "sim_msgs/msg/detail/obj_data__traits.hpp"

namespace sim_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const FieldData & msg,
  std::ostream & out)
{
  out << "{";
  // member: ball
  {
    out << "ball: ";
    to_flow_style_yaml(msg.ball, out);
    out << ", ";
  }

  // member: robot0
  {
    out << "robot0: ";
    to_flow_style_yaml(msg.robot0, out);
    out << ", ";
  }

  // member: robot1
  {
    out << "robot1: ";
    to_flow_style_yaml(msg.robot1, out);
    out << ", ";
  }

  // member: robot2
  {
    out << "robot2: ";
    to_flow_style_yaml(msg.robot2, out);
    out << ", ";
  }

  // member: robot3
  {
    out << "robot3: ";
    to_flow_style_yaml(msg.robot3, out);
    out << ", ";
  }

  // member: robot4
  {
    out << "robot4: ";
    to_flow_style_yaml(msg.robot4, out);
    out << ", ";
  }

  // member: robot5
  {
    out << "robot5: ";
    to_flow_style_yaml(msg.robot5, out);
    out << ", ";
  }

  // member: score1
  {
    out << "score1: ";
    rosidl_generator_traits::value_to_yaml(msg.score1, out);
    out << ", ";
  }

  // member: score2
  {
    out << "score2: ";
    rosidl_generator_traits::value_to_yaml(msg.score2, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FieldData & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: ball
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ball:\n";
    to_block_style_yaml(msg.ball, out, indentation + 2);
  }

  // member: robot0
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot0:\n";
    to_block_style_yaml(msg.robot0, out, indentation + 2);
  }

  // member: robot1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot1:\n";
    to_block_style_yaml(msg.robot1, out, indentation + 2);
  }

  // member: robot2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot2:\n";
    to_block_style_yaml(msg.robot2, out, indentation + 2);
  }

  // member: robot3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot3:\n";
    to_block_style_yaml(msg.robot3, out, indentation + 2);
  }

  // member: robot4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot4:\n";
    to_block_style_yaml(msg.robot4, out, indentation + 2);
  }

  // member: robot5
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot5:\n";
    to_block_style_yaml(msg.robot5, out, indentation + 2);
  }

  // member: score1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "score1: ";
    rosidl_generator_traits::value_to_yaml(msg.score1, out);
    out << "\n";
  }

  // member: score2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "score2: ";
    rosidl_generator_traits::value_to_yaml(msg.score2, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FieldData & msg, bool use_flow_style = false)
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
  const sim_msgs::msg::FieldData & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_msgs::msg::FieldData & msg)
{
  return sim_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_msgs::msg::FieldData>()
{
  return "sim_msgs::msg::FieldData";
}

template<>
inline const char * name<sim_msgs::msg::FieldData>()
{
  return "sim_msgs/msg/FieldData";
}

template<>
struct has_fixed_size<sim_msgs::msg::FieldData>
  : std::integral_constant<bool, has_fixed_size<sim_msgs::msg::ObjData>::value> {};

template<>
struct has_bounded_size<sim_msgs::msg::FieldData>
  : std::integral_constant<bool, has_bounded_size<sim_msgs::msg::ObjData>::value> {};

template<>
struct is_message<sim_msgs::msg::FieldData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_MSGS__MSG__DETAIL__FIELD_DATA__TRAITS_HPP_
