#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  shrinkImage.py
#  
#  Copyright 2017 jradko <john@radkofamily.com>
#  
#  This script will resize an image file (smaller)
#  
#  


import cv2
import numpy as np
import argparse
import os


def getArguments():
    parser = argparse.ArgumentParser(description='Shrink image down')
    parser.add_argument('-D','--DEBUG', action='store_true')
    parser.add_argument('input_img_file')
    parser.add_argument('output_img_file')
    return(parser.parse_args())

def load_image_file(image_file):
    if(os.path.isfile(image_file)):     # os.path.isfile returns true if the file exists, why is this needed?
	    img = cv2.imread(image_file)
    else:
	    print("Invalid file, exiting....")
	    exit(1)
    return(img)

def main(args):
    # argument processor
    args = getArguments()
    
    # get the input image (the big one)
    img = load_image_file(args.input_img_file)
    
    # resize the image to 1/4 it's original size
    img_scaled = cv2.resize(img, None, fx=.25, fy=.25, interpolation=cv2.INTER_AREA)
    
    # save the image to the output image
    cv2.imwrite(args.output_img_file, img_scaled)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
