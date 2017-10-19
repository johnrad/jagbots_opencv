#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  loadImageChlng.py
#  
#  Copyright 2017 jradko <jradko@radkofamily.com>
#  
#  This version of the program will load an image from last season, and show it
#  in color in a window.
#
#  The first challenge here is to change the program to use a filename passed
#  in as an argument.  You can find a basic sample in this directory, and a
#  more sophisticated sample in ..\util\shrinkImage.py (that one uses argparse, which
#  is pretty cool).
#
#  I will add some comments in here to explain a few parts
#  
#  

import cv2
import numpy as np
import os                    # including this so I can check the image file exists


def load_image_file(image_file):        # I used a function here to combine the test with the load
    if(os.path.isfile(image_file)):     # os.path.isfile returns true if the file exists, why is this needed?
	    img = cv2.imread(image_file)
    else:
	    print("Invalid file, exiting....")
	    exit(1)
    return(img)

def main(args):
    print("File Name?")
    file_name = input()
    image_filename = "..\..\images" + chr(92) + file_name   # this is a hard-coded image file
    
    img = load_image_file(image_filename)  
    cv2.imshow("Image", img)                          # this function will open a window with the image
    cv2.waitKey(0)                                    # this function will wait until a key is pressed
    
    cv2.destroyAllWindows()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
