#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 图片融合.py
# @Author: WangYe
# @Date  : 2020/3/24
# @Software: PyCharm
import cv2
import numpy as np

img1 = cv2.imread('11112.png')
print(img1.shape)
img2 = cv2.imread('1111.png')
print(img2.shape)
dst = cv2.addWeighted(img1,1,img2,0.7,0)
cv2.imwrite("green_only_out11.png", dst)
# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()