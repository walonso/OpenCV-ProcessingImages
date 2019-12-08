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
 

# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)