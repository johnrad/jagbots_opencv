# import sys
import cv2
# import numpy as np
import time
# import math
import socket
import PIL
from PIL import Image
# import threading
import http.server
from http.server import BaseHTTPRequestHandler
# import socketserver
from socketserver import ThreadingMixIn
# from PIL import Image
# from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
# from SocketServer import ThreadingMixIn
from io import StringIO, BytesIO
import cube_finder

ipPort = 1181

capture = None
constant_height_pixels = 256
constant_distance = 36


class CamHandler(BaseHTTPRequestHandler):
    

    def do_GET(self):
        print('Received GET call')
        if self.path.endswith('.mjpg'):
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=--jpgboundary')
            self.end_headers()
            while True:
                # print('Entering infinite loop')
                try:
                    rc, raw_cap = capture.read()
                    if not rc:
                        continue
                    returned = cube_finder.process_image(raw_cap)
                    img = getattr(returned,'frame')
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                    #cv2.imshow('before',img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    # convert to HSV
                    #img = self.process_frame(img)
                    # print("Procesed frame")

                    #convert to jpg
                    jpg = PIL.Image.fromarray(img)
                    # print("Have JPEG file")
                    tmpFile = BytesIO()
                    jpg.save(tmpFile, 'JPEG')
                    self.wfile.write("--jpgboundary".encode())
                    self.send_header('Content-type', 'image/jpeg')
                    self.send_header('Content-length', str(tmpFile.getbuffer().nbytes))
                    self.end_headers()
                    # print('About to save JPEG')
                    tmpHold = self.wfile
                    # print('Acquired self.wfile')
                    # jpg.save(self.wfile, 'JPEG')
                    self.wfile.write(tmpFile.getbuffer())
                    # print('JPEG save')
                    time.sleep(0.05)
                except IOError:
                    print('Caught IOError in CamHandler')
                    return
                except KeyboardInterrupt:
                    break
            return

        if self.path.endswith('.html'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><head></head><body>')
            self.wfile.write('<img src="http://127.0.0.1:1181/cam.mjpg"/>')
            self.wfile.write('</body></html>')
            return


class ThreadedHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    """Handle requests in a separate thread."""


def getIPAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipAddr = s.getsockname()[0]
    s.close()
    return(ipAddr)


def main():
    global capture
    capture = cv2.VideoCapture(0)
#    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

#    capture.set(cv2.CAP_PROP_SATURATION, 0.2)
    global img
    try:
        ipAddr = getIPAddress()
        server = ThreadedHTTPServer((ipAddr, ipPort), CamHandler)
        print("server started on ip: %s port: %d" % (ipAddr, ipPort))
        server.serve_forever()
    except KeyboardInterrupt:
        capture.release()
        server.socket.close()


if __name__ == '__main__':
    main()
