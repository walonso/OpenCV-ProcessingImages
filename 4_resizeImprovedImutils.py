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
 
# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)