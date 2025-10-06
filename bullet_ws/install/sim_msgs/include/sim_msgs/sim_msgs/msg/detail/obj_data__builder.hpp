// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from sim_msgs:msg/ObjData.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__MSG__DETAIL__OBJ_DATA__BUILDER_HPP_
#define SIM_MSGS__MSG__DETAIL__OBJ_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "sim_msgs/msg/detail/obj_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace sim_msgs
{

namespace msg
{

namespace builder
{

class Init_ObjData_w
{
public:
  explicit Init_ObjData_w(::sim_msgs::msg::ObjData & msg)
  : msg_(msg)
  {}
  ::sim_msgs::msg::ObjData w(::sim_msgs::msg::ObjData::_w_type arg)
  {
    msg_.w = std::move(arg);
    return std::move(msg_);
  }

private:
  ::sim_msgs::msg::ObjData msg_;
};

class Init_ObjData_vy
{
public:
  explicit Init_ObjData_vy(::sim_msgs::msg::ObjData & msg)
  : msg_(msg)
  {}
  Init_ObjData_w vy(::sim_msgs::msg::ObjData::_vy_type arg)
  {
    msg_.vy = std::move(arg);
    return Init_ObjData_w(msg_);
  }

private:
  ::sim_msgs::msg::ObjData msg_;
};

class Init_ObjData_vx
{
public:
  explicit Init_ObjData_vx(::sim_msgs::msg::ObjData & msg)
  : msg_(msg)
  {}
  Init_ObjData_vy vx(::sim_msgs::msg::ObjData::_vx_type arg)
  {
    msg_.vx = std::move(arg);
    return Init_ObjData_vy(msg_);
  }

private:
  ::sim_msgs::msg::ObjData msg_;
};

class Init_ObjData_theta
{
public:
  explicit Init_ObjData_theta(::sim_msgs::msg::ObjData & msg)
  : msg_(msg)
  {}
  Init_ObjData_vx theta(::sim_msgs::msg::ObjData::_theta_type arg)
  {
    msg_.theta = std::move(arg);
    return Init_ObjData_vx(msg_);
  }

private:
  ::sim_msgs::msg::ObjData msg_;
};

class Init_ObjData_y
{
public:
  explicit Init_ObjData_y(::sim_msgs::msg::ObjData & msg)
  : msg_(msg)
  {}
  Init_ObjData_theta y(::sim_msgs::msg::ObjData::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_ObjData_theta(msg_);
  }

private:
  ::sim_msgs::msg::ObjData msg_;
};

class Init_ObjData_x
{
public:
  explicit Init_ObjData_x(::sim_msgs::msg::ObjData & msg)
  : msg_(msg)
  {}
  Init_ObjData_y x(::sim_msgs::msg::ObjData::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_ObjData_y(msg_);
  }

private:
  ::sim_msgs::msg::ObjData msg_;
};

class Init_ObjData_current
{
public:
  explicit Init_ObjData_current(::sim_msgs::msg::ObjData & msg)
  : msg_(msg)
  {}
  Init_ObjData_x current(::sim_msgs::msg::ObjData::_current_type arg)
  {
    msg_.current = std::move(arg);
    return Init_ObjData_x(msg_);
  }

private:
  ::sim_msgs::msg::ObjData msg_;
};

class Init_ObjData_obj_id
{
public:
  Init_ObjData_obj_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ObjData_current obj_id(::sim_msgs::msg::ObjData::_obj_id_type arg)
  {
    msg_.obj_id = std::move(arg);
    return Init_ObjData_current(msg_);
  }

private:
  ::sim_msgs::msg::ObjData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::sim_msgs::msg::ObjData>()
{
  return sim_msgs::msg::builder::Init_ObjData_obj_id();
}

}  // namespace sim_msgs

#endif  // SIM_MSGS__MSG__DETAIL__OBJ_DATA__BUILDER_HPP_
