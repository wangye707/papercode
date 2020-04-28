#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : exp_cut.py
# @Author: WangYe
# @Date  : 2020/3/31
# @Software: PyCharm
import cv2
# name = [0,5,1000,3000,6000,10000,20000,30000,40000,50000]
name = ["5.png_predict",50000]
for i in name:
    path = str(i)+'.png'
    out = 'exp/' + str(i)+'_cut.png'
    img = cv2.imread(path)
    print(img.shape)
    cropped = img[4000:4500,600:1100]  # 裁剪坐标为[y0:y1, x0:x1]
    print(cropped.shape)
    cv2.imwrite(out, cropped)