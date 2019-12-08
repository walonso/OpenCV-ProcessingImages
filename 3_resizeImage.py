# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 22:14:31 2019

@author: kokor
"""
# import the necessary packages
import imutils
import cv2
 
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("jp.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
 
# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)