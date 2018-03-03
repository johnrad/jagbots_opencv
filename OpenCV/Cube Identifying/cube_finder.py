import os
import sys
import cv2
import numpy as np
import time
import math
import collections
from collections import namedtuple

constant_height_pixels = 172
constant_distance = 36
cube_height = 11

last_command = None

font = cv2.FONT_HERSHEY_SIMPLEX

VisionFrame = namedtuple('vision_server','frame delta_x distance cube_found x_coordinate y_coordinate')

def process_image(frame):
    rows,cols = frame.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
    frame = cv2.warpAffine(frame,M,(cols,rows))

    hsv_raw = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = hsv_raw
    hsv = cv2.blur(hsv_raw,(20,20))
    lower_limit = np.array([0,70,160])
    upper_limit = np.array([70,150,250])

    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    masked_image = cv2.bitwise_and(hsv,hsv, mask= mask)

    h, s, v = cv2.split(masked_image)

    gray = v

    ret,thresh = cv2.threshold(gray,127,255,0)
    #testvariable = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #print(len(testvariable))
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contoured = cv2.drawContours(frame, contours, -1, (0,255,0), 3) 

    height, width = frame.shape[:2]
    x_center = int(width/2)
    y_center = int(height/2)
    cv2.line(frame,(0,y_center),(width,y_center),(0,0,255),2)
    cv2.line(frame,(x_center,0),(x_center,height),(0,0,255),2)

    filtered_contours = []
    
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(max(contours, key = cv2.contourArea))
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        h = float(h)
        w = float(w)
        ratio = (float(h/w))
        if float(0.4) < (ratio) < float(2):
            filtered_contours.append(cnt)
            
    if len(filtered_contours) == 0:
        print('No cubes found!')
        next_command = 'left'
        cube_found = False
        return(VisionFrame(frame,0,0,False,0,0))


    
    if len(filtered_contours) != 0:
        cube_found = True
        x,y,w,h = cv2.boundingRect(max(filtered_contours, key = cv2.contourArea))
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cube_x = int(x+(w/2))
        cube_y = int(y+(h/2))
        cv2.line(frame,(0,int((y+(h/2)))),(width,((y+int(h/2)))),(255,250,0),2)
        cv2.line(frame,((x+int(w/2)),0),((x+int(w/2)),height),(255,250,0),2)

        #print(h)

        delta_x = int(x_center-cube_x)

        delta_y = int(y_center-cube_y)
        if int(h/cube_height) != 0:
            p = float(h/cube_height)
            delta_x_inches = float(delta_x/p)
        
        
        target = "(%d,%d)"%(delta_x,delta_y)
        #print("Target dimentions: %f x %f"%(h,w))

        focal_length = float(((constant_height_pixels*constant_distance)/cube_height))

        distance_target = float(((cube_height*focal_length)/h))

        cv2.putText(frame, str(distance_target) + ' inches', (50,50), font,1,(0,255,0),5)
        cv2.putText(frame, target,(cube_x,cube_y),font,1,(0,255,0),10)

        if int(h/cube_height) != 0:
            theta = np.arcsin(delta_x_inches/distance_target)
            theta = math.degrees(theta)

            if len(filtered_contours) != 0:
                cv2.putText(frame, str(theta) + 'degrees', (50,100), font,1,(0,255,0),5)
        
    output = VisionFrame(frame,delta_x,distance_target,cube_found,cube_x,cube_y)
    return(output)