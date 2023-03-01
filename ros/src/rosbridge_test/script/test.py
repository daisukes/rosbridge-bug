#!/usr/bin/env python3

import launch
import launch_pytest
import launch_ros.actions
import pytest
import rclpy
import rclpy.node
import std_msgs.msg
import time
import threading


@launch_pytest.fixture(scope='function')
def generate_test_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package="rosbridge_server",
            executable="rosbridge_websocket",
            parameters=[{
                "port": 9090
            }],
        )
    ])


@pytest.mark.launch(fixture=generate_test_description)
def test_check_if_msgs_published():
    rclpy.init()
    try:
        node = MakeTestNode('test_node')
        # wait rosbridge is ready
        time.sleep(5)
        node.start_subscriber()
        msgs_received_flag = node.msg_event_object.wait(timeout=5.0)
        assert msgs_received_flag, 'Did not receive msgs !'
    finally:
        rclpy.shutdown()


@pytest.mark.launch(fixture=generate_test_description)
def test_check_if_msgs_published2():
    rclpy.init()
    try:
        node = MakeTestNode('test_node')
        # wait rosbridge is ready
        time.sleep(5)
        node.start_subscriber()
        msgs_received_flag = node.msg_event_object.wait(timeout=5.0)
        assert msgs_received_flag, 'Did not receive msgs !'
    finally:
        rclpy.shutdown()


class MakeTestNode(rclpy.node.Node):

    def __init__(self, name='test_node'):
        super().__init__(name)
        self.msg_event_object = threading.Event()

    def start_subscriber(self):
        # Create a subscriber
        self.subscription = self.create_subscription(
            std_msgs.msg.String,
            '/topic',
            self.subscriber_callback,
            10
        )

        self.publisher = self.create_publisher(
            std_msgs.msg.String,
            '/topic',
            10)

        msg = std_msgs.msg.String()
        msg.data = "Ping"
        self.publisher.publish(msg)

        # Add a spin thread
        self.ros_spin_thread = threading.Thread(target=lambda node: rclpy.spin(node), args=(self,))
        self.ros_spin_thread.start()

    def subscriber_callback(self, msg):
        if msg.data == "Pong":
            self.msg_event_object.set()
