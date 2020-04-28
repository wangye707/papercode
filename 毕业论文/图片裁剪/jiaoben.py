#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : jiaoben.py
# @Author: WangYe
# @Date  : 2020/3/27
# @Software: PyCharm
path = 'test.list'
with open(path,'w') as f:

    for i in range(0,335):
        ss = str(i)
        s = 'test/image/'+ss+'.png'+'\n'
        f.write(s)