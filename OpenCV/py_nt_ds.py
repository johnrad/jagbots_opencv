#!/usr/bin/env python3
#
# This is a NetworkTables client (eg, the DriverStation/coprocessor side).
# You need to tell it the IP address of the NetworkTables server (the
# robot or simulator).
#
# When running, this will continue incrementing the value 'dsTime', and the
# value should be visible to other networktables clients and the robot.
#

import sys
import time
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging
logging.basicConfig(level=logging.DEBUG)

#if len(sys.argv) != 2:
#    print("Error: specify an IP to connect to!")
#    exit(0)

NetworkTables.initialize(server='10.46.38.2')

sd = NetworkTables.getTable("Default")

i = 0
while True:
    print('robotTime:', sd.getNumber('robotTime', 'N/A'))
    
    sd.putNumber('dsTime', i)
    time.sleep(1)
    i += 1
