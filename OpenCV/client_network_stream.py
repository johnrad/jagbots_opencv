import cv2
import numpy as np
import socket
import sys
import pickle
cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',5811))
while True:
    ret,frame=cap.read()
    cv2.imshow('Sending',frame)
    print(sys.getsizeof(frame))
    print(frame)
    clientsocket.send(pickle.dumps(frame))
