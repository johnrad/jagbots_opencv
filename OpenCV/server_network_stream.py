import socket
import sys
import cv2
import pickle
import numpy as np
HOST=''
PORT=5811

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

while True:
    data=conn.recv(80)
    print(sys.getsizeof(data))
    frame=pickle.loads(data)
    print(frame)
    cv2.imshow('frame',frame)
