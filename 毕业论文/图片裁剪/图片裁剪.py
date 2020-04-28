#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 图片裁剪.py
# @Author: WangYe
# @Date  : 2020/3/21
# @Software: PyCharm
import cv2
# name = [0,5,1000,3000,6000,10000,20000,30000,40000,50000]
name = ["1_8bits.png_predict",'1_8bits']
for i in name:
    path = str(i)+'.png'
    out = 'big11/' + str(i)+'_cut.png'
    img = cv2.imread(path)
    print(img.shape)
    cropped = img[100:-100,100:-100,:]  # 裁剪坐标为[y0:y1, x0:x1]
    print(cropped.shape)
    cv2.imwrite(out, cropped)