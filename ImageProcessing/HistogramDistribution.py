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


histogram_array = np.zeros(256)

m = (gray_img.shape[0])
n = (gray_img.shape[1])
pixels = m * n
for i in range(0,m):
    for j in range(0,n):
        value = gray_img[i][j]
        histogram_array[value] = histogram_array[value] + 1
plt.figure(1)
plt.plot(x,histogram_array)
plt.title('Lenna gray Histogram graph')
plt.xlabel('Value of samples of bins')
plt.ylabel('Number of occurences of pixel intensities')
plt.show()