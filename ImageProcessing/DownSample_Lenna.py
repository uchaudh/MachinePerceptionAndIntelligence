#!usr/bin/env python3

from __future__ import annotations
import cv2
import matplotlib.pyplot as plt

from dataclasses import dataclass, astuple
from itertools import cycle
from typing import List

import matplotlib.image as mpimg
import imageio as im

def resize(fp: str, scale: Union[float, int]) -> np.ndarray:
    _scale = lambda dim, s: int(dim * s/100)
    im: np.ndarray = cv2.imread(fp)
    width, height, channels = im.shape
    new_width: int = _scale(width, scale)
    new_height: int = _scale(width, scale)
    new_dim: tuple = (new_width, new_height)
    return cv2.resize(src=im, dsize=new_dim, interpolation=cv2.INTER_LINEAR)

lenna = im.imread("lenna.jpg")
# gray = lambda rgb : np.dot(rgb[...,:3],[0.299,0.587,0.114])
# lennagray = gray(lenna)
# im.imsave("lennagray.jpg",lennagray)

resized_lenna = resize("lennagray.jpg",12.5)
print(lenna.shape)
print(resized_lenna.shape)
plt.imshow(resized_lenna)
plt.show()
# plt.imshow(img)
