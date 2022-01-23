#!usr/bin/env python3

import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread(filename = 'ParkingLot.jpg')

result, black_white = cv2.threshold(image, 222,255,cv2.THRESH_BINARY)
plt.figure(1)
cv2.imshow("Binary Image", black_white)
cv2.waitKey(0)
cv2.destroyAllWindows()