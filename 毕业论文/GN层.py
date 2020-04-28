#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : GN层.py
# @Author: WangYe
# @Date  : 2020/3/20
# @Software: PyCharm
def GroupNorm(x, gamma, beta, G, eps = 1e - 5):
# x: 输入特征，维度为 [N,C,H,W]
# gamma, beta: 权重和偏置项, 维度为 [1,C,1,1]
# G: GN层的Group数量
    N, C, H, W = x.shape  #获取X的维度
    x = reshape(x, [N, G, C // G, H, W])  #维度转换
    mean, var = moments(x, [2, 3, 4], keep dims=True)  #计算均值，方差
    x = (x - mean) / sqrt(var + eps)  #归一化
    x = reshape(x, [N, C, H, W])      #重构变化
return x ∗ gamma + beta