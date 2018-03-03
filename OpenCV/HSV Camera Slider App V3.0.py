from tkinter import *

def show_values():
    print(lower_hue.get(), lower_sat.get(), lower_val.get())

HUE_MAXIMUM = 255
HUE_MINIMUM = 0

SAT_MAXIMUM = 255
SAT_MINIMUM = 0

VAL_MAXIMUM = 255
VAL_MINIMUM = 0

cameras = []

camera = 0

def camera_selection():
	global camera
	if camera == 0:
		camera = 1
	else:
		camera = 0
def hue_change(value):
	check = int(value)
	hue_delta_minimum = int(hue_delta_spinbox.get())
	lower_hue_check = int(lower_hue.get())
	upper_hue_check = int(upper_hue.get())
	hue_delta = (upper_hue_check - lower_hue_check)
	if (check == lower_hue_check):
		#The lower hue has been changed
		#Check the delta between lower and upper
		#print(delta)
		if hue_delta <= hue_delta_minimum:
			if (lower_hue_check + hue_delta_minimum) <= HUE_MAXIMUM:
				upper_hue.set(lower_hue_check+hue_delta_minimum)
			else:
				lower_hue.set(HUE_MAXIMUM - hue_delta_minimum)
	else:
		if hue_delta <= hue_delta_minimum:
			if (upper_hue_check - hue_delta_minimum) >= HUE_MINIMUM:
				lower_hue.set(upper_hue_check-hue_delta_minimum)
			else:
				upper_hue.set(HUE_MINIMUM + hue_delta_minimum)

def sat_change(value):
	check = int(value)
	sat_delta_minimum = int(sat_delta_spinbox.get())
	lower_sat_check = int(lower_sat.get())
	upper_sat_check = int(upper_sat.get())
	sat_delta = (upper_sat_check - lower_sat_check)
	if (check == lower_sat_check):
		#The lower sat has been changed
		#Check the delta between lower and upper
		#print(delta)
		if sat_delta <= sat_delta_minimum:
			if (lower_sat_check + sat_delta_minimum) <= SAT_MAXIMUM:
				upper_sat.set(lower_sat_check+sat_delta_minimum)
			else:
				lower_sat.set(SAT_MAXIMUM - sat_delta_minimum)
	else:
		if sat_delta <= sat_delta_minimum:
			if (upper_sat_check - sat_delta_minimum) >= SAT_MINIMUM:
				lower_sat.set(upper_sat_check-sat_delta_minimum)
			else:
				upper_sat.set(SAT_MINIMUM + sat_delta_minimum)

				
def val_change(value):
	check = int(value)
	val_delta_minimum = int(val_delta_spinbox.get())
	lower_val_check = int(lower_val.get())
	upper_val_check = int(upper_val.get())
	val_delta = (upper_val_check - lower_val_check)
	if (check == lower_val_check):
		#The lower val has been changed
		#Check the delta between lower and upper
		#print(delta)
		if val_delta <= val_delta_minimum:
			if (lower_val_check + val_delta_minimum) <= VAL_MAXIMUM:
				upper_val.set(lower_val_check+val_delta_minimum)
			else:
				lower_val.set(VAL_MAXIMUM - val_delta_minimum)
	else:
		if val_delta <= val_delta_minimum:
			if (upper_val_check - val_delta_minimum) >= VAL_MINIMUM:
				lower_val.set(upper_val_check-val_delta_minimum)
			else:
				upper_val.set(VAL_MINIMUM + val_delta_minimum)


				
def reset():
	lower_hue.set(HUE_MINIMUM)
	upper_hue.set(HUE_MAXIMUM)
	lower_sat.set(SAT_MINIMUM)
	upper_sat.set(SAT_MAXIMUM)
	lower_val.set(VAL_MINIMUM)
	upper_val.set(VAL_MAXIMUM)				
				
import cv2
import numpy as np
import os

def image_process():
	#print(hue,sat,val)
	
	cameras.append(cv2.VideoCapture(0))
	cameras.append(cv2.VideoCapture(1))
	
		
	while(True):
		#pull the latest values from the sliders
		master.update()
		cap = cameras[camera]
		contour_width_minimum = contour_width_min.get()
		contour_width_maximum = contour_width_max.get()
		
		#print(contour_width_maximum)
		#print(contour_width_minimum)
		
		# Capture frame-by-frame
		ret, frame = cap.read()
		
		#display capture
		cv2.imshow('initial',frame)
		
		#convert to HSV
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
		#display the hsv image
		cv2.imshow('hsv',hsv)
		
		#Set color range
		lower = np.array([lower_hue.get(),lower_sat.get(),lower_val.get()])
		upper = np.array([upper_hue.get(),upper_sat.get(),upper_val.get()])
		
		#blur
		blur = cv2.GaussianBlur(frame,(25,25),0)
		
		#define mask
		mask = cv2.inRange(blur, lower, upper)
		
		#apply mask
		masked_img = cv2.bitwise_and(hsv,hsv, mask= mask)
		
		#display the masked image
		cv2.imshow('Result',masked_img)
		
		#define the kernel
		kernel = np.ones((5,5), np.uint8)
		
		#Apply erosion
		erosion = masked_img #cv2.erode(masked_img, kernel, iterations = 1)
		
		#display eroded image
		cv2.imshow('Erosion', erosion)
		
		#convert to gray
		gray = cv2.cvtColor(erosion,cv2.COLOR_BGR2GRAY)
		
		
		#define image with edges
		edged = cv2.Canny(gray, 30, 200)
		
	   
		
		#find contours
		_, contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
		
		for i,current_contour in enumerate(contours):
			epsilon = 0.1*cv2.arcLength(current_contour,True)
			approx = cv2.approxPolyDP(current_contour,epsilon,True)
			x,y,w,h = cv2.boundingRect(current_contour)
			print(h)
			if int(contour_width_maximum) > (x+w) > int(contour_width_minimum): 
				cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		
		
		cv2.imshow('HEY!',frame)
		#diplay the contours
		cv2.imshow('edged',edged)
		
		
		#print contours and areas of contours
		#for i,cur_contour in enumerate(contours):
			#print(f"contour {i} has area of {cv2.contourArea(cur_contour)}")
		
		#find center point between two contours
			#right now this is randomly choosing two contours. Need logic to select two most similar in size, or something.
		if len(contours) >= 2:
			a = np.array(np.amin(contours[0],0)+np.amax(contours[1],0))
			b = a//2
			#print(a)
			#print(b)
			c=tuple(b[0])
			#print(c)
		
			point = cv2.circle(frame,c, 4, (0,0,255), -1)
			cv2.imshow('Result', point)
				
		#wait for the q key to end the program
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

#create the window
master = Tk()

#create slider for lower hue value
lower_hue = Scale(master, from_=0, to=255, length=200, orient=HORIZONTAL, label="Lower", command=hue_change)
#set to 0 at start
lower_hue.set(0)
#place the slider in the proper location
lower_hue.grid(column=1, row=0)
#repeat for saturation and value
lower_sat = Scale(master, from_=0, to=255, length=200, orient=HORIZONTAL, label="Lower", command=sat_change)
lower_sat.set(0)
lower_sat.grid(column=1,row=1)
lower_val = Scale(master, from_=0, to=255, length=200, orient=HORIZONTAL, label="Lower", command=val_change)
lower_val.grid(column=1,row=2)
lower_val.set(0)

#repeat for upper values
upper_hue = Scale(master, from_=0, to=255, length=200, orient=HORIZONTAL, label="Upper",  command=hue_change)
upper_hue.set(255)
upper_hue.grid(column=2,row=0)
upper_sat = Scale(master, from_=0, to=255, length=200, orient=HORIZONTAL, label="Upper", command=sat_change)
upper_sat.set(255)
upper_sat.grid(column=2,row=1)
upper_val = Scale(master, from_=0, to=255, length=200, orient=HORIZONTAL, label="Upper", command=val_change)
upper_val.grid(column=2,row=2)
upper_val.set(255)

#create labels in far left column
hue_label = Label(master, text="Hue")
hue_label.grid(column=0,row=0)

sat_label = Label(master, text="Saturation")
sat_label.grid(column=0,row=1)

val_label = Label(master, text="Value")
val_label.grid(column=0,row=2)


hue_delta_spinbox = Spinbox(master, from_=HUE_MINIMUM, to=HUE_MAXIMUM, increment=1)
hue_delta_spinbox.delete(0,'end')
hue_delta_spinbox.insert(0,10)
hue_delta_spinbox.grid(column=3,row=0)

sat_delta_spinbox = Spinbox(master, from_=SAT_MINIMUM, to=SAT_MAXIMUM, increment=1)
sat_delta_spinbox.delete(0,'end')
sat_delta_spinbox.insert(0,10)
sat_delta_spinbox.grid(column=3,row=1)

val_delta_spinbox = Spinbox(master, from_=VAL_MINIMUM, to=VAL_MAXIMUM, increment=1)
val_delta_spinbox.delete(0,'end')
val_delta_spinbox.insert(0,10)
val_delta_spinbox.grid(column=3,row=2)

reset_button = Button(master, text="RESET", command=reset)
reset_button.grid(column=1,row=3)

camera_selection_button = Button(master, text='SWITCH CAMERA', command=camera_selection)
camera_selection_button.grid(column=2,row=3)

contour_width_min = Scale(master, from_=0, to=640, orient=HORIZONTAL, length=200, label="Contour Minimum Width")
contour_width_min.set(0)
contour_width_min.grid(column=4,row=1)

contour_width_max = Scale(master, from_=0, to=640, orient=HORIZONTAL, length=200,label="Contour Maximum Width")
contour_width_max.set(640)
contour_width_max.grid(column=4,row=2)


#run the actual image processing
image_process()





#mainloop()
