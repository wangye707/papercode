#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 损失函数.py
# @Author: WangYe
# @Date  : 2020/3/20
# @Software: PyCharm
# print('植被（标记1）、道路（标记2）、建筑（标记3）、水体（标记4）以及其他(标记0)')
def equal():
    return 0
def weight_balance(x,predict):
    label0_weight = 1  #背景
    label1_weight = 1  #植被
    label2_weight = 1  #道路
    label3_weight = 1  #建筑
    label4_weight = 1  #水体
    #
    # weight  =   equal(x = predict,y=0)*label0_weight +
    #             equal(x = predict,y=1)*label1_weight +
    #             equal(x = predict,y=2)*label2_weight +
    #             equal(x = predict,y=3)*label3_weight +
    #             equal(x = predict,y=4)*label4_weight +
    # return weight

