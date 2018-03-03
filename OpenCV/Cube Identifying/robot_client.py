import rospy
from std_msgs.msg import String
import os
import sys
import cv2
import numpy as np
import time
import math
import RPi.GPIO as GPIO

print('Initiating')
mode=GPIO.getmode()
print(mode)

GPIO.cleanup()

Right=[26,19]
Left=[20,16]
Forward=[26,16]
Backward=[20,19]
sleeptime = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

last_command = None


def forward():
    print("Moving Forward")
    GPIO.output(Forward, GPIO.HIGH)

def reverse():
    print("Moving backward")
    GPIO.output(Backward, GPIO.HIGH)
    #GPIO.output(Backward, GPIO.LOW)

def left():
    print("Turning left")
    GPIO.output(Left, GPIO.HIGH)
    #GPIO.output(Left, GPIO.LOW)

def right():
    print("Turning right")
    GPIO.output(Right, GPIO.HIGH)

def halt():
    GPIO.output(Right, GPIO.LOW)
    GPIO.output(Left, GPIO.LOW)
    GPIO.output(Forward, GPIO.LOW)
    GPIO.output(Backward, GPIO.LOW)
def found():
    halt()
    print('target found before')

def robot_function(data):
    while not rospy.is_shutdown():
        command = (data.data)
        if command == 'left':
            left()
        elif command == 'right':
            right()
        elif command == 'forward':
            forward()
        elif command == 'halt':
            halt()
        elif command == 'found':
            found()
            
        else:
            print('Wellll.... f--k')
            quit()
        break
        
        
def robot_receiver():
    rospy.init_node('robot_client', anonymous=True)

    rospy.Subscriber('autonomous_directions', String, robot_function)
    
    rospy.spin()





if __name__ == '__main__':
    try:
        robot_receiver()
    except rospy.ROSInterruptException:
        pass
