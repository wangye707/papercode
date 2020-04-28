#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 异构机群与同构集群对比图.py
# @Author: WangYe
# @Date  : 2020/3/22
# @Software: PyCharm
from pylab import *
import matplotlib.pyplot as plt
import random
mpl.rcParams['font.sans-serif'] = ['SimHei']
x1 = [0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]
x2 = [0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]
y1 = [1, 0.5,  0.4,  0.32,  0.29,   0.26,   0.25,  0.22,  0.20,  0.19,  0.17,  0.16,  0.16]
y2 = [0.9, 0.47,  0.42,  0.33,  0.30,   0.29,   0.27,  0.25,  0.23,  0.22,  0.21,  0.21,  0.21]



plt.plot(x1,y1,label='改进Deeplabv3+',linewidth=3,
         color='red',
         # marker='*',
markerfacecolor='red',
         markersize=10)
plt.plot(x2,y2,linewidth=3,
         label = '传统Deeplabv3+'
         , color='black'
         # ,marker='v',
,markerfacecolor='black',markersize=12
         )
# plt.plot(x2,y2,label='SSGD')
# plt.plot(x3,y3,label='Single')
# plt.xlabel('m')
# plt.ylabel('costing time')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('迭代步数',size = 20)
plt.ylabel('损失函数',size = 20)
plt.title('损失函数对比',size=20)
plt.legend()
plt.savefig('CNN.svg',format = 'svg')
# plt.savefig('our3.png')
plt.show()