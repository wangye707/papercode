#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 图片裁剪.py
# @Author: WangYe
# @Date  : 2020/3/21
# @Software: PyCharm
import cv2
import numpy as np
# name = [0,5,1000,3000,6000,10000,20000,30000,40000,50000]
path = '0.png'
path_out = 'cqut_image'
size = 256
img = cv2.imread(path)
def total_image_predict(ori_image_path):

    ori_image = cv2.imread(ori_image_path, cv2.IMREAD_COLOR)
    ori_image1 = np.asarray(ori_image) #yuan
    ori_image = np.pad(ori_image,pad_width=((64,256),(64,256),(0,0)),mode="constant",constant_values=(0,0))

    # 开始切图 cut
    print(ori_image1.shape)
    print(ori_image.shape)
    h_step = ori_image1.shape[0] // 128
    w_step = ori_image1.shape[1] // 128
    print(h_step,w_step)
    h_rest = -(ori_image1.shape[0] - 128 * h_step)
    w_rest = -(ori_image1.shape[1] - 128 * w_step)
    print(h_rest,w_rest)
    image_list = []
    predict_list = []
    # 循环切图
    for h in range(h_step):
        for w in range(w_step):
            # 划窗采样
            image_sample = ori_image[(h * 128):(h * 128 + 256),
                           (w * 128):(w * 128 + 256), :]
            image_list.append(image_sample)
        # if ori_image[(h * 128):(h * 128 + 256), -256:, :].shape == (256, 256, 3):
        image_list.append(ori_image[(h * 128):(h * 128 + 256), -256:, :])
        # else:
        #     print(h,w)
    for w in range(w_step-1):
        image_list.append(ori_image[-256:, (w * 128):(w * 128 + 256), :])
    image_list.append(ori_image[-256:, -256:, :])
    return image_list
def total_image_predict1(ori_image_path):

    ori_image = cv2.imread(ori_image_path, cv2.IMREAD_COLOR)
    # ori_image = np.asarray(ori_image)
    # ori_image = np.pad(ori_image,pad_width=((64,64),(64,64),(0,0)),mode="constant",constant_values=(0,0))
    print(ori_image.shape)
    # 开始切图 cut
    h_step = ori_image.shape[0] // 256
    w_step = ori_image.shape[1] // 256
    print(h_step,w_step)
    h_rest = -(ori_image.shape[0] - 256 * h_step)
    w_rest = -(ori_image.shape[1] - 256 * w_step)
    print(h_rest,w_rest)
    image_list = []
    predict_list = []
    # 循环切图
    for h in range(h_step):
        for w in range(w_step):
            # 划窗采样
            image_sample = ori_image[(h * 256):(h * 256 + 256),
                           (w * 256):(w * 256 + 256), :]
            image_list.append(image_sample)
        image_list.append(ori_image[(h * 256):(h * 256 + 256), -256:, :])
    for w in range(w_step - 1):
        image_list.append(ori_image[-256:, (w * 256):(w * 256 + 256), :])
    image_list.append(ori_image[-256:, -256:, :])
    return image_list
outlist = total_image_predict(path)
print(len(outlist))
for i in outlist:
    if i.shape != (256, 256, 3):
        print(i.shape)
for i in range(len(outlist)):
    cv2.imwrite(path_out+'/'+str(i)+'.png',outlist[i])