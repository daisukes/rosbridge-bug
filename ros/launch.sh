#!/bin/bash


echo "Hello ROS"
colcon test --packages-select rosbridge_test --event-handlers console_cohesion+
