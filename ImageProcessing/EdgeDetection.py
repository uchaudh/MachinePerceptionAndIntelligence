#!usr/bin/env python3

import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread(filename = 'ParkingLot.jpg')

gray_scale = cv2.cvtColor(src =image,code =cv2.COLOR_BGR2GRAY)
blurred_gray_scale = cv2.GaussianBlur(src = gray_scale, ksize = (5,5), sigmaX = 10)

edge_detection = cv2.Canny(blurred_gray_scale, 100, 0)
lines = cv2.HoughLinesP(edge_detection, 1,np.pi/180, 60, maxLineGap = 25)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image,(x1,y1), (x2,y2), (0,255,0), 2)

plt.figure(2)
cv2.imshow("Canny Edge Detection", edge_detection)
cv2.imshow("Detected lines plotted on image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()