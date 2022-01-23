#!usr/bin/env python3

import cv2
import numpy as np
import matplotlib.pyplot as plt
import imageio as im

lenna = im.imread("lenna.jpg")
gray = lambda rgb : np.dot(rgb[...,:3],[0.299,0.587,0.114])
lennagray = gray(lenna)
im.imsave("lennagray.jpg",lennagray)

plt.figure( figsize = (10,10))
plt.imshow(lennagray, cmap = plt.get_cmap(name = 'gray'))
plt.show()

