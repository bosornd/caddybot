#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>

#include <std_msgs/msg/string.h>
#include <caddybot_msgs/msg/velocity.h>

#include <stdio.h>
#include <unistd.h>
#include <time.h>

#define STRING_BUFFER_LEN 100

#define RCCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){printf("Failed status on line %d: %d. Aborting.\n",__LINE__,(int)temp_rc); return 1;}}
#define RCSOFTCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){printf("Failed status on line %d: %d. Continuing.\n",__LINE__,(int)temp_rc);}}

rcl_publisher_t mode_publisher;

rcl_subscription_t velocity_subscriber;
rcl_subscription_t led_subscriber;

void velocity_subscription_callback(const void * msgin)
{
	const caddybot_msgs__msg__Velocity *velocity = (const caddybot_msgs__msg__Velocity *)msgin;

	printf("MCU received velocity(speed=%lf, angle=%lf)\n", velocity->speed, velocity->angle);
}

void led_subscription_callback(const void * msgin)
{
	const std_msgs__msg__String *led = (const std_msgs__msg__String *)msgin;

	printf("MCU received LED(%s)\n", led->data.data ? led->data.data : "NULL");
}

int main()
{
	rcl_allocator_t allocator = rcl_get_default_allocator();
	rclc_support_t support;

	// create init_options
	RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

	// create node
	rcl_node_t node;
	RCCHECK(rclc_node_init_default(&node, "caddybot_mcu", "", &support));

	// Create a reliable mode publisher
	RCCHECK(rclc_publisher_init_default(&mode_publisher, &node, ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, String), "/mode"));

	// Create a best effort velocity subscriber
	RCCHECK(rclc_subscription_init_best_effort(&velocity_subscriber, &node, ROSIDL_GET_MSG_TYPE_SUPPORT(caddybot_msgs, msg, Velocity), "/velocity"));

	// Create a best effort LED subscriber
	RCCHECK(rclc_subscription_init_best_effort(&led_subscriber, &node, ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, String), "/led"));

	caddybot_msgs__msg__Velocity* velocity_msg = caddybot_msgs__msg__Velocity__create();
	std_msgs__msg__String* led_msg = std_msgs__msg__String__create();

	// Create executor
	rclc_executor_t executor = rclc_executor_get_zero_initialized_executor();
	RCCHECK(rclc_executor_init(&executor, &support.context, 2, &allocator));
	RCCHECK(rclc_executor_add_subscription(&executor, &velocity_subscriber, velocity_msg, &velocity_subscription_callback, ON_NEW_DATA));
	RCCHECK(rclc_executor_add_subscription(&executor, &led_subscriber, led_msg, &led_subscription_callback, ON_NEW_DATA));

	rclc_executor_spin(&executor);

	caddybot_msgs__msg__Velocity__fini(velocity_msg);
	std_msgs__msg__String__fini(led_msg);
	
	RCCHECK(rcl_publisher_fini(&mode_publisher, &node));
	RCCHECK(rcl_subscription_fini(&velocity_subscriber, &node));
	RCCHECK(rcl_subscription_fini(&led_subscriber, &node));
	RCCHECK(rcl_node_fini(&node));
}
