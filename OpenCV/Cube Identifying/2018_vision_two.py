import os
import sys
import cv2
import numpy as np
import time
import math
import socket
from PIL import Image
import threading
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from SocketServer import ThreadingMixIn
import StringIO
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)
capture=None
firstrun = True
constant_height_pixels = 256
constant_distance = 36
cube_height = 11
font = cv2.FONT_HERSHEY_SIMPLEX


class CamHandler(BaseHTTPRequestHandler):

        def process_image(self, frame):
            hsv_raw = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            hsv = cv2.blur(hsv_raw,(10,10))
            lower_limit = np.array([0,135,135])
            upper_limit = np.array([93,253,255])

            mask = cv2.inRange(hsv, lower_limit, upper_limit)

            masked_image = cv2.bitwise_and(hsv,hsv, mask= mask)

            h, s, v = cv2.split(masked_image)

            gray = v

            ret,thresh = cv2.threshold(gray,127,255,0)
            im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            contoured = cv2.drawContours(frame, contours, -1, (0,255,0), 3) 

            height, width = frame.shape[:2]
            x_center = int(width/2)
            y_center = int(height/2)
            cv2.line(frame,(0,y_center),(width,y_center),(0,0,255),2)
            cv2.line(frame,(x_center,0),(x_center,height),(0,0,255),2)
            
            if len(contours) != 0:
                
                x,y,w,h = cv2.boundingRect(max(contours, key = cv2.contourArea))
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                cube_x = int(x+(w/2))
                cube_y = int(y+(h/2))
                cv2.line(frame,(0,int((y+(h/2)))),(width,((y+int(h/2)))),(255,250,0),2)
                cv2.line(frame,((x+int(w/2)),0),((x+int(w/2)),height),(255,250,0),2)

                delta_x = int(x_center-cube_x)

                delta_y = int(y_center-cube_y)

                p = float(h/cube_height)
                if p != 0:
                    delta_x_inches = float(delta_x/p)
                
                
                target = "(%d,%d)"%(delta_x,delta_y)

                focal_length = float(((constant_height_pixels*constant_distance)/cube_height)/cube_height)

                distance_target = float(((cube_height*focal_length)/h)*12)
                
                cv2.putText(frame, str(distance_target) + ' inches', (50,50), font,1,(0,255,0),5)
                if delta_x < 0:
                    cv2.putText(frame, target,(cube_x,cube_y),font,1,(0,255,0),10)
                if p != 0:
                    theta = np.arcsin(delta_x_inches/distance_target)
                    theta = math.degrees(theta)
                    cv2.putText(frame, str(theta) + 'degrees', (50,100), font,1,(0,255,0),5)


            return(frame)



    
	def do_GET(self):
		if self.path.endswith('.mjpg'):
			self.send_response(200)
			self.send_header('Content-type','multipart/x-mixed-replace; boundary=--jpgboundary')
			self.end_headers()
			while True:
				try:
					rc,img = capture.read()
					if not rc:
						continue
					    #refresh frame
                                        frame = self.process_image(img)

                                        
					imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
					jpg = Image.fromarray(imgRGB)
					tmpFile = StringIO.StringIO()
					jpg.save(tmpFile,'JPEG')
					self.wfile.write("--jpgboundary")
					self.send_header('Content-type','image/jpeg')
					self.send_header('Content-length',str(tmpFile.len))
					self.end_headers()
					jpg.save(self.wfile,'JPEG')
					time.sleep(0.05)
				except IOError:
                                        print('Error captured')
                                        
                                       
				except KeyboardInterrupt:
					break
                        print('returning from mjpg')

			return
		    
		if self.path.endswith('.html'):
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write('<html><head></head><body>')
			self.wfile.write('<img src="http://127.0.0.1:1181/cam.mjpg"/>')
			self.wfile.write('</body></html>')
                        
			return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""

def main():
	global capture
	capture = cv2.VideoCapture(0)
	#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320); 
	#capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240);
	#capture.set(cv2.CAP_PROP_SATURATION,0.2);
	global img
	try:
		server = ThreadedHTTPServer(('10.46.38.154', 1181), CamHandler)
		print("server started")
		server.serve_forever()
	except IOError:
                print('Error captured')
                
                server.socket.close()
	except KeyboardInterrupt:
		capture.release()
		
		server.socket.close()

if __name__ == '__main__':
	main()
