import cv2
from matplotlib import pyplot as plt
import numpy as np


cap = cv2.VideoCapture(1) #Webcam Capture
raw_template = cv2.imread('C:/Users/james/OneDrive/Robotics/Programming/Resources/exchange.jpg')

while(True):

	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	
		
	template = cv2.cvtColor(raw_template, cv2.COLOR_BGR2GRAY)
	w, h = template.shape[::-1]

	res = cv2.matchTemplate(gray,template,cv2.TM_SQDIFF)

	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

	top_left = min_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)

	cv2.rectangle(frame,top_left, bottom_right, 255, 1)
	cv2.putText(frame, 'Detected Face ID: ', (top_left[0],top_left[1]-10), 
			cv2.FONT_HERSHEY_PLAIN, 1.0, (255,255,255))
	

	cv2.imshow('Test',frame)


	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()	
