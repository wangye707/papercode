#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 颜色转换.py
# @Author: WangYe
# @Date  : 2020/3/24
# @Software: PyCharm
# color[img == 0] = [255, 255, 255]  # 其他，白色，0
# color[img == 1] = [0, 255, 0]  # 植被，绿色，1
# color[img == 2] = [0, 0, 0]  # 道路，黑色，2
# color[img == 3] = [131, 139, 139]  # 建筑，黄色，3
# color[img == 4] = [139, 69, 19]  # 水体，蓝色，4

import cv2
from PIL import Image
print('植被（标记1）、道路（标记2）、建筑（标记3）、水体（标记4）以及其他(标记0)')
path = '5.png_predict_cut.png'
#{255: 277834白色, 植被：945191，道路：217109, 131: 359915建筑, 139: 305897水体}
a = {}
# label = cv2.imread(path)[:, :, 0]
# print(label.shape)
# path1 = str(i) + path
# print(path1)
image = cv2.imread(path)
sh = image.shape
for i in range(sh[0]):
    for j in range(sh[1]):
        a = []
        for k in range(3):
            label = image[i,j,k]
            a.append(label)
        # print(a)
        if a != [0, 255, 0]:
            tra = [0,0,0]
            for m in range(3):
                image[i, j, m] = tra[m]
        # else:
        #     tra = [0,0,0]
        #     for m in range(3):
        #         image[i, j, m] = tra[m]
cv2.imwrite("out.png",image)
# label1 = dataset.image.load_image(path, is_color=False).astype("float32") +1


#