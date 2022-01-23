#!usr/bin/env python3

from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2

def convolve(image, kernel):
	(iH, iW) = image.shape[:2]
	(kH, kW) = kernel.shape[:2]
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float32")

	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
			k = (roi * kernel).sum()
			output[y - pad, x - pad] = k

	output = rescale_intensity(output, in_range=(0, 255))
	output = (output * 255).astype("uint8")
	return output

# construct the Sobel x-axis kernel
sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")
# construct the Sobel y-axis kernel
sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")

kernelBank = (
	("sobel_x", sobelX),
	("sobel_y", sobelY)
)

# load the input image and convert it to grayscale
image = cv2.imread('lennagray.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobelX_output= convolve(gray, sobelX)
sobelY_output= convolve(gray, sobelY)
cv2.imshow('sobelX_output',sobelX_output)
cv2.imshow('sobelY_output',sobelY_output)
cv2.waitKey(0)
cv2.destroyAllWindows()