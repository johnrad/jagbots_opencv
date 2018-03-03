import cv2
import numpy as np
import socket
import sys
import pickle
import struct
import admin

if not admin.isUserAdmin():
        admin.runAsAdmin()

        
cap = cv2.VideoCapture(0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect(('10.46.38.110', 1181))

while True:
    ret,frame = cap.read()
    data = pickle.dumps(frame)
    s.sendall(struct.pack("L", len(data)) + data)
