// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from sim_msgs:srv/Controller.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__SRV__DETAIL__CONTROLLER__TRAITS_HPP_
#define SIM_MSGS__SRV__DETAIL__CONTROLLER__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "sim_msgs/srv/detail/controller__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'team0'
// Member 'team1'
// Member 'team2'
#include "sim_msgs/msg/detail/high_cmd__traits.hpp"

namespace sim_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const Controller_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: state
  {
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
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
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Controller_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << "\n";
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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Controller_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace sim_msgs

namespace rosidl_generator_traits
{

[[deprecated("use sim_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const sim_msgs::srv::Controller_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const sim_msgs::srv::Controller_Request & msg)
{
  return sim_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sim_msgs::srv::Controller_Request>()
{
  return "sim_msgs::srv::Controller_Request";
}

template<>
inline const char * name<sim_msgs::srv::Controller_Request>()
{
  return "sim_msgs/srv/Controller_Request";
}

template<>
struct has_fixed_size<sim_msgs::srv::Controller_Request>
  : std::integral_constant<bool, has_fixed_size<sim_msgs::msg::HighCmd>::value> {};

template<>
struct has_bounded_size<sim_msgs::srv::Controller_Request>
  : std::integral_constant<bool, has_bounded_size<sim_msgs::msg::HighCmd>::value> {};

template<>
struct is_message<sim_msgs::srv::Controller_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace sim_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const Controller_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Controller_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Controller_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace sim_msgs

namespace rosidl_generator_traits
{

[[deprecated("use sim_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const sim_msgs::srv::Controller_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  sim_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use sim_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const sim_msgs::srv::Controller_Response & msg)
{
  return sim_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<sim_msgs::srv::Controller_Response>()
{
  return "sim_msgs::srv::Controller_Response";
}

template<>
inline const char * name<sim_msgs::srv::Controller_Response>()
{
  return "sim_msgs/srv/Controller_Response";
}

template<>
struct has_fixed_size<sim_msgs::srv::Controller_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<sim_msgs::srv::Controller_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<sim_msgs::srv::Controller_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<sim_msgs::srv::Controller>()
{
  return "sim_msgs::srv::Controller";
}

template<>
inline const char * name<sim_msgs::srv::Controller>()
{
  return "sim_msgs/srv/Controller";
}

template<>
struct has_fixed_size<sim_msgs::srv::Controller>
  : std::integral_constant<
    bool,
    has_fixed_size<sim_msgs::srv::Controller_Request>::value &&
    has_fixed_size<sim_msgs::srv::Controller_Response>::value
  >
{
};

template<>
struct has_bounded_size<sim_msgs::srv::Controller>
  : std::integral_constant<
    bool,
    has_bounded_size<sim_msgs::srv::Controller_Request>::value &&
    has_bounded_size<sim_msgs::srv::Controller_Response>::value
  >
{
};

template<>
struct is_service<sim_msgs::srv::Controller>
  : std::true_type
{
};

template<>
struct is_service_request<sim_msgs::srv::Controller_Request>
  : std::true_type
{
};

template<>
struct is_service_response<sim_msgs::srv::Controller_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // SIM_MSGS__SRV__DETAIL__CONTROLLER__TRAITS_HPP_
