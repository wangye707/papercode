#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : comb.py
# @Author: WangYe
# @Date  : 2020/3/27
# @Software: PyCharm
import os
import cv2
import numpy as np
path = 'cqut_image'
out_path = 'test.png'
ori_image = [6244, 3485, 3]
h_step = 47
w_step = 26
h_rest = -100
w_rest = -29
predict_list = []
files = os.listdir(path)
for file in range(len(files)):
    file_path = path+'/'+str(file)+'.png'
    im = cv2.imread(file_path)
    if im.shape!=(256,256,3):
        print(im.shape)
    predict_list.append(im[:, :, :])
# predict_list.append(ori_image[-256:, -256:, :])
count_temp = 0
tmp = np.ones([ori_image[0]-128, ori_image[1]-128,ori_image[2]])
for h in range(h_step):
    for w in range(w_step):
        print(count_temp,predict_list[count_temp][64:-64,64:-64,:].shape)
        tmp[h * 128:(h + 1) * 128,w * 128:(w + 1) * 128,:] = predict_list[count_temp][64:64+128,64:64+128,:]
        count_temp += 1
    tmp[h *128:(h + 1) * 128, w_rest : ,:] = predict_list[count_temp][64:64+128, w_rest:,:]
    count_temp += 1
for w in range(w_step - 1):
    tmp[h_rest:, (w * 128):(w * 128+128),:] = predict_list[count_temp][h_rest:, 64:64+128,:]
    count_temp += 1
tmp[h_rest:, w_rest:,:] = predict_list[count_temp][h_rest:, w_rest:,:]
print(tmp.shape)
cv2.imwrite(out_path,tmp)