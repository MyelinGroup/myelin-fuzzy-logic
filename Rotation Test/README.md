# Rotation Test

This is the first test for the EEG pipeline. Basically, this should run on a windows computer (maybe linux?) to capture data from the Mentalab EEG using ExplorePy (I think?), and then send signals to the raspberry pi to control electronics.

The *rotation test* is a setup where the EEG is rotated 90 degrees, and should then turn on the LED light, sort of like a switch of sorts. It uses the magnetic sensors.

## How to develop pipeline code

It is a good idea to have a general strategy for creating full fledged projects like this. This project serves as an example. All the code used for this project is inside this folder and can be ran.

Here is the process I (Alex) went through to create this:

1.  Set up electronics. Set up a windows computer and connect it to the Mentalab EEG using Explore Desktop. Make sure it connects with Bluetooth correctly. Set up the Raspberry Pi. You might need to image the SD card, and set it up so you can connect to it with SSH.
2.  Start some data collection. With this experiment in mind, I connected the EEG with Explore Desktop, and recorded data found in Sensor testing. I had no electrodes connected, and just rotated the Amplifier in 90 degree turns. My code analyzing this is in rotations.ipynb
3.  Having analyzed this code, I now know I will threshold on the MX signal of ORN (orientation), whether it is >300 or <300. Now I will write python code that gets this data live. This is in livetest.py. In order for it to work, I read the documentation at https://github.com/Mentalab-hub/explorepy, and saw that you need to install explorepy with ``pip install explorepy`` (make sure to do that). Also I had to run ``sudo apt-get install libbluetooth-dev`` as I could not build the bluetooth requirement.
