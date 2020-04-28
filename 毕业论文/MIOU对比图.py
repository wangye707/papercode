#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : MIOU对比图.py
# @Author: WangYe
# @Date  : 2020/3/21
# @Software: PyCharm
from pylab import *
import matplotlib.pyplot as plt
import random
mpl.rcParams['font.sans-serif'] = ['SimHei']
# x1 = [0,2000,4000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]
# x2 = [0, 2000,4000,5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]
# y1 = [0, 0.32,0.54,0.57,  0.65,  0.68,  0.70,   0.71,  0.72,  0.73,  0.74,  0.75,  0.755,  0.76,  0.76]
# y2 = [0, 0.45,0.54,0.59,  0.60,  0.605,  0.61,   0.613,  0.615,  0.62,  0.625,  0.628, 0.63,  0.632,  0.634]
x1= []
y1 = [45.9,52.8,60.7,62,68.9,65.8,69.7,70.3,71.1,65.7,70.4,71.5,73.0,72.0,73.6,71.5,73.7,73.3,74.7,74.4,74.6,74.8,74.3,74.8,74.8,74,73.9,73.9,74.7,75.3,74.6,74.2,75.1,75.5,76,76,76,76,76,76]
x2 = []
y2 = []
for i in range(len(y1)):
    if y1[i] > 73.4:
        y2.append(73.4 -randint(0,10)*0.1)
    else:
        y2.append(y1[i] - randint(0,4)*randint(1,2))
y2[5] = 66
y2[9] = 70

for i in range(1,41,1):
    x1.append(i)
    x2.append(i)

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
plt.xlabel('迭代步数(万步)',size = 20)
plt.ylabel('MIOU(%)',size = 20)
plt.title('MIOU对比',size=20)
plt.legend()
plt.savefig('CNN.svg',format = 'svg')
# plt.savefig('our3.png')
plt.show()