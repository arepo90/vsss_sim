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
// Member 'team0'
// Member 'team1'
// Member 'team2'
// Member 'op0'
// Member 'op1'
// Member 'op2'
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

  // member: team0
  {
    out << "team0: ";
    to_flow_style_yaml(msg.team0, out);
    out << ", ";
  }

  // member: team1
  {
    out << "team1: ";
    to_flow_style_yaml(msg.team1, out);
    out << ", ";
  }

  // member: team2
  {
    out << "team2: ";
    to_flow_style_yaml(msg.team2, out);
    out << ", ";
  }

  // member: op0
  {
    out << "op0: ";
    to_flow_style_yaml(msg.op0, out);
    out << ", ";
  }

  // member: op1
  {
    out << "op1: ";
    to_flow_style_yaml(msg.op1, out);
    out << ", ";
  }

  // member: op2
  {
    out << "op2: ";
    to_flow_style_yaml(msg.op2, out);
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

  // member: team0
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "team0:\n";
    to_block_style_yaml(msg.team0, out, indentation + 2);
  }

  // member: team1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "team1:\n";
    to_block_style_yaml(msg.team1, out, indentation + 2);
  }

  // member: team2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "team2:\n";
    to_block_style_yaml(msg.team2, out, indentation + 2);
  }

  // member: op0
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "op0:\n";
    to_block_style_yaml(msg.op0, out, indentation + 2);
  }

  // member: op1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "op1:\n";
    to_block_style_yaml(msg.op1, out, indentation + 2);
  }

  // member: op2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "op2:\n";
    to_block_style_yaml(msg.op2, out, indentation + 2);
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
