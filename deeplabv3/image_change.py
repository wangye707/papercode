#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : image_change.py
# @Author: WangYe
# @Date  : 2020/2/27
# @Software: PyCharm
from PIL import Image
import numpy as np
import os

dir_img = "00003.png"
# 待处理的图片地址
dir_save = "00003_mean.png"
# 水平镜像翻转后保存的地址

list_img = dir_img

pri_image = Image.open(dir_img)
# tmppath = dir_save
# pri_image.transpose(Image.ROTATE_90).save(tmppath)

#均值化处理
import numpy as np
import paddle.dataset as dataset
import cv2
from PIL import Image

path = '11.jpg'
label = cv2.imread(path)
IMG_MEAN = np.array((103.939, 116.779, 123.68), dtype=np.float32)
label = label - IMG_MEAN
cv2.imwrite('11_mean.jpg', label)