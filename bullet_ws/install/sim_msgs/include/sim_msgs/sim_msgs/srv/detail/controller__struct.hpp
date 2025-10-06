// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from sim_msgs:srv/Controller.idl
// generated code does not contain a copyright notice

#ifndef SIM_MSGS__SRV__DETAIL__CONTROLLER__STRUCT_HPP_
#define SIM_MSGS__SRV__DETAIL__CONTROLLER__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'settings'
#include "sim_msgs/msg/detail/field_data__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__sim_msgs__srv__Controller_Request __attribute__((deprecated))
#else
# define DEPRECATED__sim_msgs__srv__Controller_Request __declspec(deprecated)
#endif

namespace sim_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Controller_Request_
{
  using Type = Controller_Request_<ContainerAllocator>;

  explicit Controller_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : settings(_init)
  {
    (void)_init;
  }

  explicit Controller_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : settings(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _settings_type =
    sim_msgs::msg::FieldData_<ContainerAllocator>;
  _settings_type settings;

  // setters for named parameter idiom
  Type & set__settings(
    const sim_msgs::msg::FieldData_<ContainerAllocator> & _arg)
  {
    this->settings = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_msgs::srv::Controller_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_msgs::srv::Controller_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_msgs::srv::Controller_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_msgs::srv::Controller_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_msgs::srv::Controller_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::srv::Controller_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_msgs::srv::Controller_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::srv::Controller_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_msgs::srv::Controller_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_msgs::srv::Controller_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_msgs__srv__Controller_Request
    std::shared_ptr<sim_msgs::srv::Controller_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_msgs__srv__Controller_Request
    std::shared_ptr<sim_msgs::srv::Controller_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Controller_Request_ & other) const
  {
    if (this->settings != other.settings) {
      return false;
    }
    return true;
  }
  bool operator!=(const Controller_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Controller_Request_

// alias to use template instance with default allocator
using Controller_Request =
  sim_msgs::srv::Controller_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace sim_msgs


#ifndef _WIN32
# define DEPRECATED__sim_msgs__srv__Controller_Response __attribute__((deprecated))
#else
# define DEPRECATED__sim_msgs__srv__Controller_Response __declspec(deprecated)
#endif

namespace sim_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Controller_Response_
{
  using Type = Controller_Response_<ContainerAllocator>;

  explicit Controller_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit Controller_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    sim_msgs::srv::Controller_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const sim_msgs::srv::Controller_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<sim_msgs::srv::Controller_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<sim_msgs::srv::Controller_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      sim_msgs::srv::Controller_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::srv::Controller_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      sim_msgs::srv::Controller_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<sim_msgs::srv::Controller_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<sim_msgs::srv::Controller_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<sim_msgs::srv::Controller_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__sim_msgs__srv__Controller_Response
    std::shared_ptr<sim_msgs::srv::Controller_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__sim_msgs__srv__Controller_Response
    std::shared_ptr<sim_msgs::srv::Controller_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Controller_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const Controller_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Controller_Response_

// alias to use template instance with default allocator
using Controller_Response =
  sim_msgs::srv::Controller_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace sim_msgs

namespace sim_msgs
{

namespace srv
{

struct Controller
{
  using Request = sim_msgs::srv::Controller_Request;
  using Response = sim_msgs::srv::Controller_Response;
};

}  // namespace srv

}  // namespace sim_msgs

#endif  // SIM_MSGS__SRV__DETAIL__CONTROLLER__STRUCT_HPP_
