# Example:
# https://github.com/Mentalab-hub/explorepy/blob/master/examples/acquisition-example.py

import explorepy
from explorepy.stream_processor import TOPICS
import socket

# IP of the pi to connect to
IP_ADDRESS = "10.0.0.31"
PORT = 1234
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((IP_ADDRESS, PORT))
print("Connected to Raspberry Pi server... connecting to Mentalab Explore")

# Send a command to control the lights, on or off
def control_lights(enable):
    global currently_on
    if currently_on is not None and currently_on == enable:
        return
    
    if enable:
        print(" - turning lights on")
    else:
        print(" - turning lights off")
    
    message = "ENABLE" if enable else "DISABLE"
    client_socket.send(message.encode())

    currently_on = enable


def read_data(packet):
    """A function that receives orientation packets and does some operations on the data"""
    timestamp, orn_data = packet.get_data()
    print("Received an orientation packet: ", orn_data)
    #############
    # YOUR CODE #
    #############

    # print(orn_data)
    # This is my code! We will be reading the MX data and do thresholding stuff
    mx = orn_data[6]
    print(f"MX Data: {mx}")
    control_lights(mx > 300)


# Create an Explore object
exp_device = explorepy.Explore()

# Connect to the Explore device using device bluetooth name or mac address
exp_device.connect(device_name="Explore_CA55")

print("Connected to Mentalab Explore... starting data reading and communications!")
    
# Subscribe your function to the ORN stream so we receive data on ORN
exp_device.stream_processor.subscribe(callback=read_data, topic=TOPICS.raw_orn)

# For ExG:
# exp_device.stream_processor.subscribe(callback=read_data, topic=TOPICS.raw_ExG)

# Infinite loop to keep the code running

import time

try:
    while True:
        time.sleep(.5)
except KeyboardInterrupt:
    print("Program stopped!")