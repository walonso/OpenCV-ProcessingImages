# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 22:35:19 2019

@author: kokor
"""
# import the necessary packages
import imutils
import cv2
 
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)


image = cv2.imread("jp.jpg")
roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
