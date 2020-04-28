#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 均值化处理.py
# @Author: WangYe
# @Date  : 2020/3/13
# @Software: PyCharm
import os
import numpy as np
import cv2

# 这个是你图片的根目录，注意不要带中文路径，楼主就因为这个调试了很久。
image_path = '5.png'

# file_names = os.listdir(image_path)

count = 0
mean = np.zeros(3, np.int64)

img = cv2.imread(image_path)
#print(img)
count += 1
mean += np.sum(img, axis=(0, 1)).astype(int)
h, w = img.shape[0:-1]
print(h, w, count)
means = mean / (1.0 * h * w * count)
print('b, g, r = ', means)
img = img - means
cv2.imwrite('5_mean.png', img)