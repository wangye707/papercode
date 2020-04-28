#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: WangYe
# @Date  : 2020/3/30
# @Software: PyCharm
path = '1.txt'
for i in range(10000):
    with open(path,'a') as f:
        f.write(str(i)+'dasdas'+'\n')
        f.close()