#!usr/bin/env python3

import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("ParkingLot.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# create a binary thresholded image
_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
# show it
plt.figure(1)
plt.imshow(binary, cmap="gray")
plt.show()

# contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw all contours
# image = cv2.drawContours(image, contours, -1, (0, 0, 255), 2)
# plt.figure(2)
# plt.imshow(image)
# plt.show()

# for i in contours:
#     rect = cv2.minAreaRect(i)
#     box = cv2.boxPoints(rect)
#     box = np.int0(box)
#     cv2.drawContours(image,[box],0,(0,0,255),2)

# plt.figure(2)
plt.imshow(image)
plt.show()