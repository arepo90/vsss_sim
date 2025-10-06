// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_msgs:msg/ObjData.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__OBJ_DATA__TRAITS_HPP_
#define SIM_MSGS__MSG__DETAIL__OBJ_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_msgs/msg/detail/obj_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace sim_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ObjData & msg,
  std::ostream & out)
{
  out << "{";
  // member: obj_id
  {
    out << "obj_id: ";
    rosidl_generator_traits::value_to_yaml(msg.obj_id, out);
    out << ", ";
  }

  // member: current
  {
    out << "current: ";
    rosidl_generator_traits::value_to_yaml(msg.current, out);
    out << ", ";
  }

  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << ", ";
  }

  // member: theta
  {
    out << "theta: ";
    rosidl_generator_traits::value_to_yaml(msg.theta, out);
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

  // member: w
  {
    out << "w: ";
    rosidl_generator_traits::value_to_yaml(msg.w, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ObjData & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: obj_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "obj_id: ";
    rosidl_generator_traits::value_to_yaml(msg.obj_id, out);
    out << "\n";
  }

  // member: current
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current: ";
    rosidl_generator_traits::value_to_yaml(msg.current, out);
    out << "\n";
  }

  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }

  // member: theta
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "theta: ";
    rosidl_generator_traits::value_to_yaml(msg.theta, out);
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

  // member: w
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "w: ";
    rosidl_generator_traits::value_to_yaml(msg.w, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ObjData & msg, bool use_flow_style = false)
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
  const sim_msgs::msg::ObjData & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const sim_msgs::msg::ObjData & msg)
{
  return sim_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<sim_msgs::msg::ObjData>()
{
  return "sim_msgs::msg::ObjData";
}

template<>
inline const char * name<sim_msgs::msg::ObjData>()
{
  return "sim_msgs/msg/ObjData";
}

template<>
struct has_fixed_size<sim_msgs::msg::ObjData>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sim_msgs::msg::ObjData>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sim_msgs::msg::ObjData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SIM_MSGS__MSG__DETAIL__OBJ_DATA__TRAITS_HPP_
