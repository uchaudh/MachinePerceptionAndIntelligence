#!usr/bin/env python3

import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

image = cv2.imread(filename = 'ParkingLot.jpg')

gray_scale = cv2.cvtColor(src =image,code =cv2.COLOR_BGR2GRAY)
blurred_gray_scale = cv2.GaussianBlur(src = gray_scale, ksize = (5,5), sigmaX = 10)

edge_detection = cv2.Canny(blurred_gray_scale, 100, 0)
lines = cv2.HoughLinesP(edge_detection, 1,np.pi/180, 60, maxLineGap = 25)
test = lines[0][0][0]
# print(test)
# cv2.line(image,(lines[0][1],lines[0][2]), (lines[0][3],lines[0][4]), (0,255,0), 2)

i = 0
for i in range(len(lines)):
    if i < 24:
        x1, y1, x2, y2 = lines[i][0]
        # print(x1,y1,x2,y2)
        x3, y3, x4, y4 = lines[i+1][0]
        cv2.line(image,(x1,y1), (x2,y2), (0,255,0), 2)
        # cv2.line(image,(x1,y1), (math.trunc(x2/2),math.trunc(y2/2)), (0,0,255), 2)
        cv2.line(image,(x1,y1), (x2,y2), (255,0,0), 2)
        # cv2.line(image,(x2,y2), (x4,y4), (0,0,255), 1)
        # cv2.line(image,(x3,y3), (x4,y4), (0,0,255), 1)
        # cv2.line(image,(x1,y1), (x3,y3), (0,0,255), 1)
        # print(x1,y1,x2,y2)

        # print(math.trunc(x2/2))
        i = i+1

cv2.line(image,(7,226), (478,118), (255,0,0), 2)
cv2.line(image,(130,314), (478,223), (255,0,0), 2)
cv2.line(image,(1,118), (478,14), (255,0,0), 2)
cv2.imwrite("Contour.jpg",image)

contour_image = cv2.imread("Contour.jpg")

gray = cv2.cvtColor(contour_image, cv2.COLOR_RGB2GRAY)
_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)

plt.figure(1)
plt.imshow(contour_image,cmap="gray")
plt.show()

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour = cv2.drawContours(contour_image, contours, -1, (255, 0, 0), 2)


plt.figure(2)
plt.imshow(contour)
plt.show()
# cv2.imshow("Edge", edge_detection)
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()