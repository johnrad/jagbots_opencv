import cv2
import cube_finder
import collections

cap = cv2.VideoCapture(0)
while(True):
	ret,frame = cap.read()
	cv2.imshow('Frame RAW',frame)

	result = cube_finder.process_image(frame)
	#print(result)
	final = getattr(result,'frame')
	print(frame)
	cv2.imshow('frame',final)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break