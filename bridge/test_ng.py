#!/usr/bin/env python3

import logging
import roslibpy
from roslibpy.comm import RosBridgeClientFactory
import signal
import threading
import time


# settings for roslibpy reconnection
RosBridgeClientFactory.set_initial_delay(1)
RosBridgeClientFactory.set_max_delay(3)
client = roslibpy.Ros(host='ros', port=9090)
ROS_CLIENT_CONNECTED = [False]


# logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# topic message callback
# it publish "Pong" when receive "Ping"
def topic_callback(msg):
    print(msg)
    if msg['data'] == "Ping":
        pong = roslibpy.Message({
            "data": "Pong"
        })
        topic.publish(pong)


topic = roslibpy.Topic(client, '/topic', 'std_msgs/String')
topic.subscribe(topic_callback)

alive = True


# signal handler
def handler(signum, frame):
    global alive
    logger.info("Signal catched")
    alive = False


signal.signal(signal.SIGTERM, handler)


# loop to reconnect to ROS bridge
def loop():
    while True and alive:
        time.sleep(1)
        if not client.is_connected:
            if ROS_CLIENT_CONNECTED[0]:
                ROS_CLIENT_CONNECTED[0] = False
                continue
            try:
                client.run(1.0)
                logger.info("ROS bridge is connected")
                ROS_CLIENT_CONNECTED[0] = True
            except Exception as e:
                # except Failed to connect to ROS
                pass
        else:
            pass


thread = threading.Thread(target=loop)
thread.daemon = True
thread.start()


while alive:
    time.sleep(1)
