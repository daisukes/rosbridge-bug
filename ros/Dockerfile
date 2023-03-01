FROM ros:humble

WORKDIR /root

RUN apt update && apt install -y \
	ros-build-essential \
	ros-humble-rosbridge-suite \
	ros-humble-launch-pytest

RUN mkdir -p /root/src
COPY ./src /root/src
COPY ./launch.sh /root/launch.sh

RUN sed -i "s|/opt/ros/\$ROS_DISTRO|/root/install|" /ros_entrypoint.sh
RUN . /opt/ros/humble/setup.sh && colcon build
