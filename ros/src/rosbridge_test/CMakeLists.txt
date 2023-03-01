cmake_minimum_required(VERSION 3.8)
project(rosbridge_test)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_pytest REQUIRED)

ament_add_pytest_test(rosbridge_test script/test.py)

ament_package()
