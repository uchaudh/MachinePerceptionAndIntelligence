#!usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

x = np.arange(0,256,1,dtype = None)
img = np.array(Image.open('lenna.jpg')).astype(np.uint8)
gray_img = np.round(0.299 * img[:, :, 0] +
                    0.587 * img[:, :, 1] +
                    0.114 * img[:, :, 2]).astype(np.uint8)
row = gray_img.shape[0]
col = gray_img.shape[1]

width = gray_img.shape[0]
height = gray_img.shape[1]

intensity_array = np.zeros(shape=(256,), dtype=np.int)

# insert the count of intensities in the intensity array
for row in gray_img:
    for pixel in row:
        intensity_array[pixel] += 1

# print(intensity_array)


size = width * height
# create an array which store the probabilities of counting of intensities
probability_intensity_array = intensity_array / float(size)
# print(probability_intensity_array)
# calculating commutative distribution function
cumulative_distribution_function = np.zeros(shape=(256,), dtype=np.float)
t_cumulative_distribution_function = np.zeros(shape=(256,), dtype=np.uint8)

value = 0
for i in range(0, len(probability_intensity_array)):
    cumulative_distribution_function[i] = value + probability_intensity_array[i]
    value = cumulative_distribution_function[i]

for i in range(0, len(cumulative_distribution_function)):
    t_cumulative_distribution_function[i] = round(i * cumulative_distribution_function[i])

imag_after_histogram_equalization = np.zeros(gray_img.shape, dtype=np.uint8)

for row_index in range(0, len(gray_img)):
    for col_index in range(0, len(img[0])):
        imag_after_histogram_equalization[row_index][col_index] = \
            t_cumulative_distribution_function[gray_img[row_index][col_index]]

histogram_equalization = np.zeros(256)

for i in range(0, len(gray_img)):
    for j in range(0, len(gray_img)):
        value = int(imag_after_histogram_equalization[i,j])
        histogram_equalization[value] += 1

plt.figure(1)
plt.bar(range(256) , histogram_equalization, 0.5)
plt.title('Histogram equalization graph')
plt.xlabel('Value of samples of bins')
plt.ylabel('Number of occurences of pixel intensities')
plt.show()

plt.figure(2)
plt.title('Lenna image before histogram equalization.jpg')
fit = plt.imshow(gray_img, cmap = plt.get_cmap('gray'))
plt.show()

plt.figure(3)
plt.title('Lenna image after histogram equalization.jpg')
fit = plt.imshow(imag_after_histogram_equalization, cmap = plt.get_cmap('gray'))
plt.show()
