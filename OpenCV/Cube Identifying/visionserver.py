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
import cube_finder
signal(SIGPIPE,SIG_DFL)
capture=None
firstrun = True
constant_height_pixels = 256
constant_distance = 36
cube_height = 11
font = cv2.FONT_HERSHEY_SIMPLEX

ipPort = 1181

class CamHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path.endswith('.mjpg'):
			
			print('Received GET Call)')
			self.send_response(200)
			self.send_header('Content-type','multipart/x-mixed-replace; boundary=--jpgboundary')
			self.end_headers()
			while(True):
				try:
					rc,raw_cap = capture.read()
					if not rc:
						continue
					    #refresh frame
					returned = cube_finder.process_image(raw_cap)
					img = getattr(returned,'frame')

                    

                                        
					imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
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
					print('Error captured IOError')
					return                     
                                       
				except KeyboardInterrupt:
					break
                print('returning from mjpg')

			return

		else:
			print('waiting at mjpg')
		    
		if self.path.endswith('.html'):
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write('<html><head></head><body>')
			self.wfile.write('<img src="http://127.0.0.1:1181/cam.mjpg"/>')
			self.wfile.write('</body></html>')
                        
			return
		else:
			print('waiting at html')



class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""

def getIPAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipAddr = s.getsockname()[0]
    s.close()
    return(ipAddr)

def main():
	global capture
#	capture = cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)I420, framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink*")
#	capture = cv2.VideoCapture("/dev/video0")
	capture = cv2.VideoCapture(0)
#	capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320); 
#	capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240);
#	capture.set(cv2.CAP_PROP_SATURATION,0.2);
	global img
	try:
		ipAddr = getIPAddress()
		server = ThreadedHTTPServer((ipAddr, ipPort), CamHandler)
		print("server started on ip %s port %d" % (ipAddr, ipPort))
		server.serve_forever()
	except IOError:
                print('Error captured')
                
                server.socket.close()
	except KeyboardInterrupt:
		print('MAIN KI')
		capture.release()
		
		server.socket.close()

if __name__ == '__main__':
	main()
